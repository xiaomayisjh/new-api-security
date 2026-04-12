# CORS配置漏洞复现指南

## 漏洞信息
- **漏洞类型**: CORS配置错误
- **严重程度**: 高
- **所在文件**: [middleware/cors.go](file:///workspace/middleware/cors.go#L9-L16)
- **函数**: `CORS()`
- **漏洞描述**: 同时设置了 `AllowAllOrigins = true` 和 `AllowCredentials = true`，这是一个危险的组合，可能导致跨站请求伪造（CSRF）攻击

## 部署步骤
1. 确保项目已在本地成功构建
2. 启动后端服务：`go run main.go`
3. 确保服务运行在 http://localhost:3000

## 执行步骤
1. 进入 Case_001_CORS 目录
2. 运行 PoC 脚本：`python3 poc.py`
3. 观察输出结果

## 观察指标
- **成功触发时**：脚本输出 "[VULNERABLE] CORS configuration allows cross-origin requests with credentials!"
- **响应头**：应包含 `Access-Control-Allow-Origin: http://evil.com` 和 `Access-Control-Allow-Credentials: true`

## 根因分析
1. **配置问题**：在 [middleware/cors.go](file:///workspace/middleware/cors.go#L11-L12) 中，同时设置了 `AllowAllOrigins = true` 和 `AllowCredentials = true`
2. **安全风险**：这允许任何网站发送带有用户凭证的请求到目标服务器，可能导致 CSRF 攻击
3. **影响范围**：所有应用了 CORS 中间件的路由，包括 API 路由和中继路由

## 加固建议
1. **方案一**：如果需要允许跨域请求但不需要凭证
   - 设置 `AllowCredentials = false`

2. **方案二**：如果需要允许跨域请求且需要凭证
   - 明确指定允许的源，不要使用 `AllowAllOrigins = true`
   - 示例：
     ```go
     config.AllowOrigins = []string{"https://your-domain.com"}
     config.AllowCredentials = true
     ```

3. **方案三**：使用环境变量配置
   - 从环境变量读取允许的源，便于不同环境的配置

4. **额外建议**：
   - 对于敏感操作，实现 CSRF 令牌验证
   - 确保会话 Cookie 设置了 `SameSite=Strict` 或 `SameSite=Lax`