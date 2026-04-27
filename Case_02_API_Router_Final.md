# 完整安全审计报告 - sub2api (New API)

**审计日期**: 2026-04-27
**审计工具**: RedTeam_Auto_Auditor
**审计范围**:
- 批次 1：认证和安全层 (auth.go, user.go, token.go, crypto.go)
- 批次 2：API 路由和控制器 (user.go, relay.go, channel.go, router/)
- 批次 3+4：数据持久化、支付和外部集成

---

## 发现汇总表

| 发现 ID | 严重程度 | 类型 | 文件 | 状态 | 行号 |
|---|---|---|---|---|---|
| 1 | 高危 | SSRF | /workspace/controller/channel.go | ✅ 已验证 | 973, 1037-1050 |
| 2 | 中危 | 不安全的 WebSocket Origin 检查 | /workspace/controller/relay.go | ✅ 已验证 | 244-249 |
| 3 | 中危 | 缺少 channel 访问权限验证 | /workspace/middleware/auth.go + distributor.go | ✅ 已验证 | 392-394, 33-53 |
| 4 | 低危 | 日志注入（潜在） | /workspace/controller/user.go | ℹ️ 需注意 | 612 |
| 5 | 误报 | 列注入 | /workspace/model/user.go | ❌ 误报 | |

---

## 详细发现报告

---

### 发现 1：SSRF 漏洞（高危）

**文件**: /workspace/controller/channel.go (FetchModels 函数)
**严重程度**: 高危
**状态**: ✅ 已验证
**相关代码行**: 973, 1037-1050

#### 问题描述

在 `FetchModels` 函数接收用户提供的 `base_url` 参数，并在没有 SSRF 验证的情况下直接使用于 HTTP 请求，允许攻击者访问内部服务。

**关键代码**:
```go
func FetchModels(c *gin.Context) {
    var req struct {
        BaseURL string `json:"base_url"`
        // ...
    }
    baseURL := req.BaseURL  // 用户输入，未验证
    // ...
    url := fmt.Sprintf("%s/v1/models", baseURL)
    request, err := http.NewRequest("GET", url, nil)
    // ...直接请求
}
```

#### 严重性评估

**影响**: 攻击者可以通过此漏洞访问内部网络服务（例如：
- http://127.0.0.1:8080
- http://localhost:3306
- http://internal-service:9200
- http://[::1]:6379

**缓解因素**:
- 该路由需要 `RootAuth()`（第 229 行），只有 root 用户可以访问
- 但 root 用户已经拥有系统最高权限

#### 修复建议

**好消息**：项目已经有完整的 SSRF 防护实现！在 `/workspace/common/ssrf_protection.go 文件中！

**修复代码**：
在 `FetchModels` 函数中使用现有的 SSRF 防护：

```go
func FetchModels(c *gin.Context) {
    var req struct {
        BaseURL string `json:"base_url"`
        // ...
    }
    // ...
    baseURL := req.BaseURL
    if baseURL == "" {
        baseURL = constant.ChannelBaseURLs[req.Type]
    }
    
    // 添加 SSRF 防护！使用默认保护！
    if err := common.DefaultSSRFProtection.ValidateURL(baseURL); err != nil {
        c.JSON(http.StatusBadRequest, gin.H{
            "success": false,
            "message": fmt.Sprintf("Invalid base_url: %v", err),
        })
        return
    }
    
    // ...剩余代码
}
```

**更完善的方案**：使用系统设置中的 SSRF 配置，与代码库其他部分保持一致。

---

### 发现 2：不安全的 WebSocket Origin 检查（中危）

**文件**: /workspace/controller/relay.go
**严重程度**: 中危
**状态**: ✅ 已验证
**相关代码行**: 244-249

#### 问题描述

WebSocket upgrader 将 `CheckOrigin` 设置为始终返回 `true`，接受来自任何源的连接。

**关键代码**:
```go
var upgrader = websocket.Upgrader{
    Subprotocols: []string{"realtime"},
    CheckOrigin: func(r *http.Request) bool {
        return true // 允许任何源！
    },
}
```

#### 影响

如果用户已认证，恶意网站可以：
- 建立 WebSocket 连接
- 可能访问用户数据
- 可能执行用户操作

#### 修复建议

实现 Origin 检查：
```go
CheckOrigin: func(r *http.Request) bool {
    origin := r.Header.Get("Origin")
    if origin == "" {
        return true
    }
    
    u, err := url.Parse(origin)
    if err != nil {
        return false
    }
    
    // 检查 host 匹配
    host := r.Host
    // 检查端口
    // 或者使用白名单
    return u.Host == host || isAllowedOrigin(origin)
}
```

---

### 发现 3：管理员 Token 指定渠道缺少权限验证（中危）

**文件**: /workspace/middleware/auth.go + /workspace/middleware/distributor.go
**严重程度**: 中危
**状态**: ✅ 已验证
**相关代码行**: 392-394 (auth.go), 33-53 (distributor.go)

#### 问题描述

管理员用户使用格式为 `sk-<token>-<channel_id>` 的 Token 时，`parts[1]` 直接设置 context 中的 `specific_channel_id`，而无需验证用户是否有权访问该 channel。

#### 修复建议

在 distributor.go 中增加权限验证：

```go
if ok {
    id, err := strconv.Atoi(channelId.(string))
    if err != nil {
        // ...
    }
    // 验证！
    userGroup := common.GetContextKeyString(c, constant.ContextKeyUserGroup)
    // 检查是否该 channel 是否在用户可用分组中
    // 或者检查用户是否是 channel 的所有者（对于管理员）
    
    channel, err := model.GetChannelById(id, true)
    if err != nil {
        // ...
    }
    // 增加验证逻辑
    // ...
}
```

---

### 发现 4：潜在日志注入（低危）

**文件**: /workspace/controller/user.go
**严重程度**: 低危
**相关代码行**: 612

#### 问题描述

`AdminClearUserBinding` 函数将 `binding_type` 直接插入日志。

```go
model.RecordLog(user.Id, model.LogTypeManage, fmt.Sprintf("admin cleared %s binding for user %s", binding_type, user.Username)
```

#### 影响

日志中可能包含换行符和其他特殊字符。

#### 修复建议

清理输入：
```go
cleanBindingType := strings.ReplaceAll(binding_type, "\n", "")
model.RecordLog(user.Id, model.LogTypeManage, fmt.Sprintf("admin cleared %s binding for user %s", cleanBindingType, user.Username))
```

---

## 审计工作文件

所有审计中间结果：
- .audit_work/audit_findings/ 目录
- .audit_work/verified_results/ 目录

## 修复优先级

1. **立即修复（高危）**: 发现 1 (SSRF)
2. **尽快修复（中危）**: 发现 2, 3
3. **计划修复（低危）**: 发现 4

---

**审计完成日期**: 2026-04-27
