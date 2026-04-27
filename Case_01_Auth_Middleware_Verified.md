# 安全审计报告 - 批次 1：认证与安全层

## 审计日期
2026-04-27

## 审计范围

| 文件路径 | 状态 |
|---------|------|
| `/workspace/middleware/auth.go` | ✅ 审计完成 |
| `/workspace/model/user.go` | ✅ 审计完成 |
| `/workspace/model/token.go` | ✅ 审计完成 |
| `/workspace/common/crypto.go` | ✅ 审计完成 |

---

## 发现汇总

### 1. 发现：管理员 Token 指定渠道功能缺少访问权限验证

| 属性 | 值 |
|------|-----|
| **严重程度** | 中 (Medium) |
| **发现类型** | Potential_Access_Control |
| **受影响文件** | `/workspace/middleware/auth.go`, `/workspace/middleware/distributor.go` |
| **状态** | ✅ 已验证 |

#### 详细描述

在 `/workspace/middleware/auth.go` 的第 392-394 行，当用户使用格式为 `sk-<token>-<channel_id>` 的 Token 时，如果该用户是管理员，`parts[1]` 会被直接设置为 `specific_channel_id` 并存入上下文。

然后在 `/workspace/middleware/distributor.go` 的第 33-53 行，`specific_channel_id` 会被读取并直接传递给 `model.GetChannelById(id, true)` 来获取对应的 channel，而**没有验证该管理员是否有权限访问该 channel**。

#### 问题代码

**auth.go 第 392-394 行:**
```go
if len(parts) > 1 {
    if model.IsAdmin(token.UserId) {
        c.Set("specific_channel_id", parts[1])
```

**distributor.go 第 33-53 行:**
```go
channelId, ok := common.GetContextKey(c, constant.ContextKeyTokenSpecificChannelId)
// ...
if ok {
    id, err := strconv.Atoi(channelId.(string))
    if err != nil {
        // ...
    }
    channel, err := model.GetChannelById(id, true)
    // ... 直接使用，没有验证权限
```

#### 潜在影响

1. 管理员可以访问系统中的任意 channel
2. 如果管理员 Token 泄露，攻击者可以访问所有 channel

#### 修复建议

1. **方案一（推荐）：在 `distributor.go` 中增加权限验证**
   - 验证当前用户是否有权限访问该 channel
   - 或者验证该 channel 是否属于用户的可用分组

2. **方案二：在 `auth.go` 中验证 channel_id 的合法性**
   - 在设置 `specific_channel_id` 时就验证该 channel 是否可用

3. **代码示例（方案一）:**
   ```go
   if ok {
       id, err := strconv.Atoi(channelId.(string))
       if err != nil {
           // ...
       }
       
       // 增加权限验证
       userId := c.GetInt("id")
       userGroup := common.GetContextKeyString(c, constant.ContextKeyUserGroup)
       
       channel, err := model.GetChannelById(id, true)
       if err != nil {
           // ...
       }
       
       // 验证该 channel 是否对当前用户可用
       if !model.IsChannelEnabledForGroupModel(userGroup, "", channel.Id) {
           abortWithOpenAiMessage(c, http.StatusForbidden, "无权访问该渠道")
           return
       }
       // ...
   }
   ```

---

### 2. 其他发现

#### user.go：误报 - commonGroupCol 列注入风险

**状态：** ❌ 误报（False Positive）

**说明：** `commonGroupCol` 是在 `model/main.go` 的 `initCol()` 函数中初始化的内部变量，根据数据库类型设置为 `` `group` `` 或 `"group"`，不接受任何外部输入，因此不存在列注入风险。

---

### 3. token.go 和 crypto.go：无发现

**状态：** ✅ 通过审计

---

## 总结

| 发现总数 | 已验证 | 误报 | 需要修复 |
|---------|--------|------|---------|
| 2 | 1 | 1 | 1 |

**需要修复的问题：** 管理员 Token 指定渠道功能缺少访问权限验证（中危）

---

## 后续审计计划

接下来将进行批次 2 审计，包括 API 路由和控制器文件。
