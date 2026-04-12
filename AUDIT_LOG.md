# 红队自动化审计日志

## 1. 项目架构描述

### 1.1 技术栈识别
- **后端**: Go语言，使用Gin框架
- **前端**: React + JavaScript
- **数据库**: 可能使用MySQL/PostgreSQL（基于SQL迁移文件）
- **鉴权中间件**: 存在auth.go中间件
- **其他组件**: Redis（用于缓存和速率限制）

### 1.2 关键目录结构
- `controller/`: API控制器
- `middleware/`: 中间件（包含鉴权）
- `router/`: 路由定义
- `relay/`: 第三方服务集成
- `service/`: 业务逻辑
- `web/`: 前端代码

## 2. Entry_Points (路由) 识别

### 2.1 API 路由
- `/api/setup` (GET/POST)
- `/api/status` (GET)
- `/api/uptime/status` (GET)
- `/api/models` (GET) - 需要认证
- `/api/user/register` (POST)
- `/api/user/login` (POST)
- `/api/user/login/2fa` (POST)
- `/api/user/passkey/login/begin` (POST)
- `/api/user/passkey/login/finish` (POST)
- `/api/user/logout` (GET)
- `/api/user/self` (GET) - 需要认证
- `/api/user/self/models` (GET) - 需要认证
- `/api/user/self/token` (GET) - 需要认证
- `/api/user/topup` (POST) - 需要认证
- `/api/stripe/webhook` (POST)
- `/api/creem/webhook` (POST)
- `/api/waffo/webhook` (POST)
- `/api/verify` (POST) - 需要认证
- `/api/oauth/:provider` (GET)
- `/api/oauth/wechat` (GET)
- `/api/oauth/telegram/login` (GET)
- `/api/oauth/telegram/bind` (GET)

### 2.2 Relay 路由
- `/v1/models` (GET)
- `/v1/models/:model` (GET)
- `/v1/chat/completions` (POST)
- `/v1/completions` (POST)
- `/v1/responses` (POST)
- `/v1/embeddings` (POST)
- `/v1/audio/transcriptions` (POST)
- `/v1/audio/translations` (POST)
- `/v1/audio/speech` (POST)
- `/v1/rerank` (POST)
- `/v1/moderations` (POST)
- `/v1beta/models` (GET)
- `/v1beta/models/*path` (POST)

### 2.3 Midjourney 路由
- `/mj/image/:id` (GET)
- `/mj/submit/action` (POST) - 需要认证
- `/mj/submit/imagine` (POST) - 需要认证
- `/mj/task/:id/fetch` (GET) - 需要认证

### 2.4 Suno 路由
- `/suno/submit/:action` (POST) - 需要认证
- `/suno/fetch` (POST) - 需要认证
- `/suno/fetch/:id` (GET) - 需要认证

## 3. Sensitive_Sinks (执行/查询/文件操作) 标记

### 3.1 命令执行
- `common/utils.go:OpenBrowser` - 使用 exec.Command 打开浏览器

### 3.2 数据库操作
- `model/main.go` - 包含 DB.Exec, DB.Query 等操作
- `model/ability.go` - 数据库查询操作
- `model/task_cas_test.go` - 数据库测试操作
- `service/task_billing_test.go` - 数据库测试操作

### 3.3 文件操作
- `common/utils.go:SaveTmpFile` - 创建临时文件
- `common/body_storage.go` - 存储请求体
- `common/pprof.go` - 性能分析文件操作
- `controller/video_proxy.go` - 视频文件处理
- `relay/channel/openai/relay-openai.go` - 文件操作
- `relay/channel/dify/relay-dify.go` - 文件操作
- `relay/channel/cloudflare/adaptor.go` - 文件操作
- `relay/relay_task.go` - 文件操作
- `service/http.go` - HTTP 文件处理
- `service/image.go` - 图像文件处理

### 3.4 网络操作
- `service/http.go` - HTTP 客户端请求
- `relay/channel/*` - 第三方 API 调用

## 4. 待审计文件清单

### 4.1 路由层
- `router/main.go`
- `router/api-router.go`
- `router/relay-router.go`
- `router/web-router.go`
- `router/video-router.go`
- `router/dashboard.go`

### 4.2 控制器层
- `controller/auth.go`
- `controller/user.go`
- `controller/channel.go`
- `controller/token.go`
- `controller/relay.go`
- `controller/playground.go`
- `controller/topup.go`
- `controller/subscription.go`
- `controller/video_proxy.go`

### 4.3 中间件层
- `middleware/auth.go`
- `middleware/rate-limit.go`
- `middleware/cors.go`
- `middleware/secure_verification.go`
- `middleware/turnstile-check.go`

### 4.4 服务层
- `service/http.go`
- `service/image.go`
- `service/task.go`
- `service/channel.go`
- `service/billing.go`

### 4.5 模型层
- `model/main.go`
- `model/user.go`
- `model/channel.go`
- `model/token.go`
- `model/ability.go`

### 4.6 公共工具
- `common/utils.go`
- `common/body_storage.go`
- `common/ssrf_protection.go`
- `common/url_validator.go`

### 4.7 Relay 适配器
- `relay/relay.go`
- `relay/channel/openai/relay-openai.go`
- `relay/channel/claude/relay-claude.go`
- `relay/channel/gemini/relay-gemini.go`
