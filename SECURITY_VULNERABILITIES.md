# 未验证的潜在安全漏洞

## 高风险

### CORS 配置过于宽松
- **文件**: [middleware/cors.go](file:///workspace/middleware/cors.go#L9-L16)
- **描述**: 同时设置了 `AllowAllOrigins = true` 和 `AllowCredentials = true`，这是一个危险的组合，可能导致跨站请求伪造（CSRF）攻击
- **影响**: 攻击者可能通过恶意网站诱导用户执行未授权操作
- **建议**: 明确指定允许的源或禁用凭证

### 缺少 CSRF 防护机制
- **文件**: 全局
- **描述**: 除了 CORS 配置问题外，没有发现明确的 CSRF 令牌验证机制
- **影响**: 可能导致跨站请求伪造攻击
- **建议**: 为所有状态改变的请求实现 CSRF 令牌

## 中风险

### SSRF 防护默认配置
- **文件**: [common/ssrf_protection.go](file:///workspace/common/ssrf_protection.go#L23-L30)
- **描述**: 默认配置中白名单为空，可能导致合法请求被阻止
- **影响**: 影响系统功能
- **建议**: 提供合理的默认配置或明确告知用户需要配置

### XSS 风险（使用 dangerouslySetInnerHTML）
- **文件**: web/src/components/common/DocumentRenderer/index.jsx, web/src/components/dashboard/AnnouncementsPanel.jsx
- **描述**: 使用了 dangerouslySetInnerHTML 来渲染内容
- **影响**: 可能导致 XSS 攻击
- **建议**: 确保内容经过适当的 sanitization

## 低风险

### 访问令牌分割逻辑
- **文件**: [middleware/auth.go](file:///workspace/middleware/auth.go#L209-L211)
- **描述**: 令牌分割逻辑可能对异常格式的令牌处理不当
- **影响**: 可能导致认证异常
- **建议**: 增加更严格的令牌格式验证

### SSRF 重定向验证
- **文件**: [common/ssrf_protection.go](file:///workspace/common/ssrf_protection.go#L208-L286)
- **描述**: 未对重定向进行验证
- **影响**: 可能通过重定向绕过 SSRF 防护
- **建议**: 配置客户端不跟随重定向或对重定向目标进行验证

### Creem webhook 验证
- **文件**: [controller/topup_creem.go](file:///workspace/controller/topup_creem.go#L37-L50)
- **描述**: 测试模式下跳过签名验证
- **影响**: 测试环境可能被模拟攻击
- **建议**: 确保测试环境的安全性