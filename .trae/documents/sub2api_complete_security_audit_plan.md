# sub2api (New API) 完整安全审计计划

## 项目概述
- **项目名称**: New API (原 sub2api)
- **技术栈**: Go 1.25.1 + Gin + GORM + SQLite/MySQL/PostgreSQL + Redis
- **项目类型**: LLM 网关和 AI 资产管理系统
- **主要功能**:
  - API 转发、模型管理、用户认证
  - 计费、订阅、支付集成
  - 多模型支持（OpenAI、Claude、Gemini 等）
- **审计日期**: 2026-04-27

## 审计策略

### 审计架构
使用 **RedTeam_Auto_Auditor** 技能，通过以下架构进行审计：
- **主控 Agent**: 环境管理、任务调度
- **Auditor Sub-Agent**: 单个文件深度审计
- **Verifier Sub-Agent**: 发现验证、PoC 编写

### 审计范围
分 4 个批次对项目核心文件进行审计：

---

## 批次 1：核心认证和安全层

### 目标文件
1. `/workspace/middleware/auth.go` - 认证中间件
2. `/workspace/model/user.go` - 用户模型
3. `/workspace/model/token.go` - Token 管理
4. `/workspace/common/crypto.go` - 加密实现
5. `/workspace/service/passkey/service.go` - Passkey 认证

### 审计重点
- 认证绕过风险
- Session 管理
- 密码哈希强度
- JWT 安全
- Token 泄漏风险

---

## 批次 2：API 路由和控制器

### 目标文件
1. `/workspace/controller/user.go` - 用户控制器
2. `/workspace/controller/relay.go` - 转发控制器
3. `/workspace/controller/channel.go` - 渠道管理
4. `/workspace/router/main.go` - 路由设置
5. `/workspace/router/api-router.go` - API 路由

### 审计重点
- API 授权检查
- 参数注入风险
- SSRF 防护
- 权限提升
- 输入验证

---

## 批次 3：数据持久化和支付

### 目标文件
1. `/workspace/model/main.go` - 数据库初始化
2. `/workspace/controller/topup.go` - 充值功能
3. `/workspace/service/billing.go` - 计费逻辑
4. `/workspace/service/stripe.go` (如果存在) - Stripe 集成
5. `/workspace/controller/subscription_payment_stripe.go` - 订阅支付

### 审计重点
- SQL 注入
- 支付逻辑漏洞
- 数据加密
- 配额绕过
- 事务处理

---

## 批次 4：协议转发和外部集成

### 目标文件
1. `/workspace/relay/chat_completions_via_responses.go` - Chat 转发
2. `/workspace/relay/channel/openai/relay-openai.go` - OpenAI 适配器
3. `/workspace/common/ssrf_protection.go` - SSRF 防护
4. `/workspace/service/http_client.go` - HTTP 客户端
5. `/workspace/relay/websocket.go` - WebSocket 处理

### 审计重点
- SSRF 风险
- 外部服务调用
- 数据泄露
- 请求/响应篡改
- WebSocket 安全

---

## 执行计划

### 阶段 1：环境准备
1. 检查 Docker 环境
2. 创建审计工作目录结构:
   - `.audit_work/audit_findings/`
   - `.audit_work/verified_results/`
   - `.audit_work/poc_scripts/`
3. 生成初始审计日志文件

### 阶段 2：分批次审计
对于每个文件:
1. 使用 RedTeam_Auto_Auditor 技能进行审计
2. Auditor Sub-Agent 生成发现报告
3. 如果有发现，Verifier Sub-Agent 进行验证
4. 生成最终报告（Case_[ID]_[Logic_Type].md）

### 阶段 3：结果汇总
1. 汇总所有审计发现
2. 按严重程度分类
3. 生成完整审计报告
4. 提供修复建议

---

## 风险分类标准

### Critical (严重)
- 远程代码执行 (RCE)
- 认证绕过
- 数据库完全访问
- 敏感数据大规模泄露

### High (高危)
- SQL 注入
- SSRF 到内部网络
- 权限提升
- 支付逻辑漏洞

### Medium (中危)
- XSS 漏洞
- 信息泄露
- 不安全的直接对象引用 (IDOR)
- 业务逻辑缺陷

### Low (低危)
- 配置问题
- 过时的依赖
- 日志敏感信息

---

## 注意事项

1. **每个 skill 调用只审计一个文件** - 按 Lead Agent 指令执行
2. **使用无害探测逻辑** - PoC 使用 sleep/echo/读取非敏感文件
3. **使用安全术语** - 漏洞 → Security_Finding, Payload → Interaction_Logic 等
4. **结果持久化** - 所有中间结果保存到 `.audit_work/` 目录

---

## 开始审计

准备就绪后，我们将从 **批次 1** 开始，第一个文件是:
`/workspace/middleware/auth.go`

是否继续执行？
