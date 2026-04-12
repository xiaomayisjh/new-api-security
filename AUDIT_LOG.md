# 安全审计清单

## 项目基本信息
- 技术栈：Go 1.25.1, React 18.2.0
- 框架：Gin (Go), Vite (React)
- 数据库：支持SQLite/MySQL/PostgreSQL
- 核心功能：API接口、认证授权、支付处理、模型管理

## 审计文件列表

### 根目录文件
- [Completed] .dockerignore
- [Completed] .env.example
- [Completed] .gitattributes
- [Completed] .gitignore
- [Relationship_Mapped] AGENTS.md
- [Pending] AUDIT_LOG.md
- [Pending] CLAUDE.md
- [Pending] Dockerfile
- [Pending] LICENSE
- [Pending] README.fr.md
- [Pending] README.ja.md
- [Pending] README.md
- [Pending] README.zh_CN.md
- [Pending] README.zh_TW.md
- [Pending] SECURITY_AUDIT_REPORT.md
- [Pending] SECURITY_VULNERABILITIES.md
- [Pending] VERSION
- [Pending] docker-compose.yml
- [Pending] go.mod
- [Pending] go.sum
- [Pending] main.go (核心文件)
- [Pending] makefile
- [Pending] new-api.service

### .cursor目录
- [Pending] .cursor/rules/project.mdc

### .github目录
- [Pending] .github/CODE_OF_CONDUCT.md
- [Pending] .github/PULL_REQUEST_TEMPLATE.md
- [Pending] .github/SECURITY.md
- [Pending] .github/ISSUE_TEMPLATE/bug_report.md
- [Pending] .github/ISSUE_TEMPLATE/bug_report_en.md
- [Pending] .github/ISSUE_TEMPLATE/config.yml
- [Pending] .github/ISSUE_TEMPLATE/feature_request.md
- [Pending] .github/ISSUE_TEMPLATE/feature_request_en.md
- [Pending] .github/workflows/docker-image-alpha.yml
- [Pending] .github/workflows/docker-image-arm64.yml
- [Pending] .github/workflows/electron-build.yml
- [Pending] .github/workflows/pr-check.yml
- [Pending] .github/workflows/release.yml
- [Pending] .github/workflows/sync-to-gitee.yml

### bin目录
- [Pending] bin/migration_v0.2-v0.3.sql
- [Pending] bin/migration_v0.3-v0.4.sql
- [Pending] bin/time_test.sh

### common目录
- [Pending] common/api_type.go
- [Pending] common/audio.go
- [Pending] common/body_storage.go
- [Pending] common/constants.go
- [Pending] common/copy.go
- [Pending] common/crypto.go
- [Pending] common/custom-event.go
- [Pending] common/database.go (核心文件)
- [Pending] common/disk_cache.go
- [Pending] common/disk_cache_config.go
- [Pending] common/email-outlook-auth.go
- [Pending] common/email.go
- [Pending] common/embed-file-system.go
- [Pending] common/endpoint_defaults.go
- [Pending] common/endpoint_type.go
- [Pending] common/env.go (核心文件)
- [Pending] common/gin.go
- [Pending] common/go-channel.go
- [Pending] common/gopool.go
- [Pending] common/hash.go
- [Pending] common/init.go (核心文件)
- [Pending] common/ip.go
- [Pending] common/json.go
- [Pending] common/model.go
- [Pending] common/page_info.go
- [Pending] common/performance_config.go
- [Pending] common/pprof.go
- [Pending] common/pyro.go
- [Pending] common/quota.go
- [Pending] common/rate-limit.go
- [Pending] common/redis.go
- [Pending] common/ssrf_protection.go (核心文件)
- [Pending] common/str.go
- [Pending] common/sys_log.go
- [Pending] common/system_monitor.go
- [Pending] common/system_monitor_unix.go
- [Pending] common/system_monitor_windows.go
- [Pending] common/topup-ratio.go
- [Pending] common/totp.go
- [Pending] common/url_validator.go
- [Pending] common/url_validator_test.go
- [Pending] common/utils.go
- [Pending] common/validate.go
- [Pending] common/verification.go
- [Pending] common/limiter/limiter.go

### constant目录
- [Pending] constant/README.md
- [Pending] constant/api_type.go
- [Pending] constant/azure.go
- [Pending] constant/cache_key.go
- [Pending] constant/channel.go
- [Pending] constant/context_key.go
- [Pending] constant/endpoint_type.go
- [Pending] constant/env.go
- [Pending] constant/finish_reason.go
- [Pending] constant/midjourney.go
- [Pending] constant/multi_key_mode.go
- [Pending] constant/setup.go
- [Pending] constant/task.go
- [Pending] constant/waffo_pay_method.go

### controller目录
- [Pending] controller/billing.go
- [Pending] controller/channel-billing.go
- [Pending] controller/channel-test.go
- [Pending] controller/channel.go
- [Pending] controller/channel_affinity_cache.go
- [Pending] controller/channel_upstream_update.go
- [Pending] controller/channel_upstream_update_test.go
- [Pending] controller/checkin.go
- [Pending] controller/codex_oauth.go
- [Pending] controller/codex_usage.go
- [Pending] controller/console_migrate.go
- [Pending] controller/custom_oauth.go
- [Pending] controller/deployment.go
- [Pending] controller/group.go
- [Pending] controller/image.go
- [Pending] controller/log.go
- [Pending] controller/midjourney.go
- [Pending] controller/misc.go
- [Pending] controller/missing_models.go
- [Pending] controller/model.go
- [Pending] controller/model_meta.go
- [Pending] controller/model_sync.go
- [Pending] controller/oauth.go
- [Pending] controller/option.go
- [Pending] controller/passkey.go
- [Pending] controller/performance.go
- [Pending] controller/playground.go
- [Pending] controller/prefill_group.go
- [Pending] controller/pricing.go
- [Pending] controller/ratio_config.go
- [Pending] controller/ratio_sync.go
- [Pending] controller/redemption.go
- [Pending] controller/relay.go
- [Pending] controller/secure_verification.go
- [Pending] controller/setup.go
- [Pending] controller/subscription.go
- [Pending] controller/subscription_payment_creem.go
- [Pending] controller/subscription_payment_epay.go
- [Pending] controller/subscription_payment_stripe.go
- [Pending] controller/swag_video.go
- [Pending] controller/task.go
- [Pending] controller/telegram.go
- [Pending] controller/token.go
- [Pending] controller/token_test.go
- [Pending] controller/topup.go
- [Pending] controller/topup_creem.go
- [Pending] controller/topup_stripe.go
- [Pending] controller/topup_waffo.go
- [Pending] controller/twofa.go
- [Pending] controller/uptime_kuma.go
- [Pending] controller/usedata.go
- [Pending] controller/user.go (核心文件)
- [Pending] controller/vendor_meta.go
- [Pending] controller/video_proxy.go
- [Pending] controller/video_proxy_gemini.go
- [Pending] controller/wechat.go

### docs目录
- [Pending] docs/ionet-client.md
- [Pending] docs/translation-glossary.fr.md
- [Pending] docs/translation-glossary.md
- [Pending] docs/translation-glossary.ru.md
- [Pending] docs/channel/other_setting.md
- [Pending] docs/images/aionui.png
- [Pending] docs/images/aliyun.png
- [Pending] docs/images/cherry-studio.png
- [Pending] docs/images/io-net.png
- [Pending] docs/images/pku.png
- [Pending] docs/images/ucloud.png
- [Pending] docs/installation/BT.md
- [Pending] docs/openapi/api.json
- [Pending] docs/openapi/relay.json

### dto目录
- [Pending] dto/audio.go
- [Pending] dto/channel_settings.go
- [Pending] dto/claude.go
- [Pending] dto/embedding.go
- [Pending] dto/error.go
- [Pending] dto/gemini.go
- [Pending] dto/gemini_generation_config_test.go
- [Pending] dto/gemini_isstream_test.go
- [Pending] dto/midjourney.go
- [Pending] dto/notify.go
- [Pending] dto/openai_compaction.go
- [Pending] dto/openai_image.go
- [Pending] dto/openai_request.go (核心文件)
- [Pending] dto/openai_request_zero_value_test.go
- [Pending] dto/openai_response.go
- [Pending] dto/openai_responses_compaction_request.go
- [Pending] dto/openai_video.go
- [Pending] dto/playground.go
- [Pending] dto/pricing.go
- [Pending] dto/ratio_sync.go
- [Pending] dto/realtime.go
- [Pending] dto/request_common.go
- [Pending] dto/rerank.go
- [Pending] dto/sensitive.go
- [Pending] dto/suno.go
- [Pending] dto/task.go
- [Pending] dto/user_settings.go
- [Pending] dto/values.go
- [Pending] dto/video.go

### electron目录
- [Pending] electron/README.md
- [Pending] electron/build.sh
- [Pending] electron/create-tray-icon.js
- [Pending] electron/entitlements.mac.plist
- [Pending] electron/icon.png
- [Pending] electron/main.js
- [Pending] electron/package-lock.json
- [Pending] electron/package.json
- [Pending] electron/preload.js
- [Pending] electron/tray-icon-windows.png
- [Pending] electron/tray-iconTemplate.png
- [Pending] electron/tray-iconTemplate@2x.png

### i18n目录
- [Pending] i18n/i18n.go
- [Pending] i18n/keys.go
- [Pending] i18n/locales/en.yaml
- [Pending] i18n/locales/zh-CN.yaml
- [Pending] i18n/locales/zh-TW.yaml

### logger目录
- [Pending] logger/logger.go

### middleware目录
- [Pending] middleware/auth.go (核心文件)
- [Pending] middleware/body_cleanup.go
- [Pending] middleware/cache.go
- [Pending] middleware/cors.go (核心文件)
- [Pending] middleware/disable-cache.go
- [Pending] middleware/distributor.go
- [Pending] middleware/email-verification-rate-limit.go
- [Pending] middleware/gzip.go
- [Pending] middleware/i18n.go
- [Pending] middleware/jimeng_adapter.go
- [Pending] middleware/kling_adapter.go
- [Pending] middleware/logger.go
- [Pending] middleware/model-rate-limit.go
- [Pending] middleware/performance.go
- [Pending] middleware/rate-limit.go
- [Pending] middleware/recover.go
- [Pending] middleware/request-id.go
- [Pending] middleware/secure_verification.go
- [Pending] middleware/stats.go
- [Pending] middleware/turnstile-check.go
- [Pending] middleware/utils.go

### model目录
- [Pending] model/ability.go
- [Pending] model/channel.go
- [Pending] model/channel_cache.go
- [Pending] model/channel_satisfy.go
- [Pending] model/checkin.go
- [Pending] model/custom_oauth_provider.go
- [Pending] model/db_time.go
- [Pending] model/log.go
- [Pending] model/main.go (核心文件)
- [Pending] model/midjourney.go
- [Pending] model/missing_models.go
- [Pending] model/model_extra.go
- [Pending] model/model_meta.go
- [Pending] model/option.go
- [Pending] model/passkey.go
- [Pending] model/prefill_group.go
- [Pending] model/pricing.go
- [Pending] model/pricing_default.go
- [Pending] model/pricing_refresh.go
- [Pending] model/redemption.go
- [Pending] model/setup.go
- [Pending] model/subscription.go
- [Pending] model/task.go
- [Pending] model/task_cas_test.go
- [Pending] model/token.go
- [Pending] model/token_cache.go
- [Pending] model/topup.go
- [Pending] model/twofa.go
- [Pending] model/usedata.go
- [Pending] model/user.go (核心文件)
- [Pending] model/user_cache.go
- [Pending] model/user_oauth_binding.go
- [Pending] model/utils.go
- [Pending] model/vendor_meta.go

### oauth目录
- [Pending] oauth/discord.go
- [Pending] oauth/generic.go
- [Pending] oauth/github.go
- [Pending] oauth/linuxdo.go
- [Pending] oauth/oidc.go
- [Pending] oauth/provider.go
- [Pending] oauth/registry.go
- [Pending] oauth/types.go

### pkg目录
- [Pending] pkg/cachex/codec.go
- [Pending] pkg/cachex/hybrid_cache.go
- [Pending] pkg/cachex/namespace.go
- [Pending] pkg/ionet/client.go
- [Pending] pkg/ionet/container.go
- [Pending] pkg/ionet/deployment.go
- [Pending] pkg/ionet/hardware.go
- [Pending] pkg/ionet/jsonutil.go
- [Pending] pkg/ionet/types.go

### relay目录
- [Pending] relay/audio_handler.go
- [Pending] relay/chat_completions_via_responses.go
- [Pending] relay/claude_handler.go
- [Pending] relay/compatible_handler.go
- [Pending] relay/embedding_handler.go
- [Pending] relay/gemini_handler.go
- [Pending] relay/image_handler.go
- [Pending] relay/mjproxy_handler.go
- [Pending] relay/param_override_error.go
- [Pending] relay/relay_adaptor.go
- [Pending] relay/relay_task.go
- [Pending] relay/rerank_handler.go
- [Pending] relay/responses_handler.go
- [Pending] relay/websocket.go
- [Pending] relay/channel/adapter.go
- [Pending] relay/channel/api_request.go
- [Pending] relay/channel/api_request_test.go
- [Pending] relay/common/billing.go
- [Pending] relay/common/override.go
- [Pending] relay/common/override_test.go
- [Pending] relay/common/relay_info.go
- [Pending] relay/common/relay_info_test.go
- [Pending] relay/common/relay_utils.go
- [Pending] relay/common/request_conversion.go
- [Pending] relay/common/stream_status.go
- [Pending] relay/common/stream_status_test.go
- [Pending] relay/common_handler/rerank.go
- [Pending] relay/constant/relay_mode.go
- [Pending] relay/helper/common.go
- [Pending] relay/helper/model_mapped.go
- [Pending] relay/helper/price.go
- [Pending] relay/helper/stream_result.go
- [Pending] relay/helper/stream_scanner.go
- [Pending] relay/helper/stream_scanner_test.go
- [Pending] relay/helper/valid_request.go
- [Pending] relay/reasonmap/reasonmap.go

### router目录
- [Pending] router/api-router.go (核心文件)
- [Pending] router/dashboard.go
- [Pending] router/main.go (核心文件)
- [Pending] router/relay-router.go
- [Pending] router/video-router.go
- [Pending] router/web-router.go

### service目录
- [Pending] service/audio.go
- [Pending] service/billing.go
- [Pending] service/billing_session.go
- [Pending] service/channel.go
- [Pending] service/channel_affinity.go
- [Pending] service/channel_affinity_template_test.go
- [Pending] service/channel_affinity_usage_cache_test.go
- [Pending] service/channel_select.go
- [Pending] service/codex_credential_refresh.go
- [Pending] service/codex_credential_refresh_task.go
- [Pending] service/codex_oauth.go
- [Pending] service/codex_wham_usage.go
- [Pending] service/convert.go
- [Pending] service/download.go
- [Pending] service/epay.go
- [Pending] service/error.go
- [Pending] service/error_test.go
- [Pending] service/file_decoder.go
- [Pending] service/file_service.go
- [Pending] service/funding_source.go
- [Pending] service/group.go
- [Pending] service/http.go
- [Pending] service/http_client.go
- [Pending] service/image.go
- [Pending] service/log_info_generate.go
- [Pending] service/midjourney.go
- [Pending] service/notify-limit.go
- [Pending] service/openai_chat_responses_compat.go
- [Pending] service/openai_chat_responses_mode.go
- [Pending] service/quota.go
- [Pending] service/sensitive.go
- [Pending] service/str.go
- [Pending] service/subscription_reset_task.go
- [Pending] service/task.go
- [Pending] service/task_billing.go
- [Pending] service/task_billing_test.go
- [Pending] service/task_polling.go
- [Pending] service/text_quota.go
- [Pending] service/text_quota_test.go
- [Pending] service/token_counter.go
- [Pending] service/token_estimator.go
- [Pending] service/tokenizer.go
- [Pending] service/usage_helpr.go
- [Pending] service/user_notify.go
- [Pending] service/violation_fee.go
- [Pending] service/webhook.go
- [Pending] service/openaicompat/chat_to_responses.go
- [Pending] service/openaicompat/policy.go
- [Pending] service/openaicompat/regex.go
- [Pending] service/openaicompat/responses_to_chat.go
- [Pending] service/passkey/service.go
- [Pending] service/passkey/session.go
- [Pending] service/passkey/user.go

### setting目录
- [Pending] setting/auto_group.go
- [Pending] setting/chat.go
- [Pending] setting/midjourney.go
- [Pending] setting/payment_creem.go
- [Pending] setting/payment_stripe.go
- [Pending] setting/payment_waffo.go
- [Pending] setting/rate_limit.go
- [Pending] setting/sensitive.go
- [Pending] setting/user_usable_group.go
- [Pending] setting/config/config.go (核心文件)
- [Pending] setting/console_setting/config.go
- [Pending] setting/console_setting/validation.go
- [Pending] setting/model_setting/claude.go
- [Pending] setting/model_setting/gemini.go
- [Pending] setting/model_setting/global.go
- [Pending] setting/model_setting/grok.go
- [Pending] setting/model_setting/qwen.go
- [Pending] setting/operation_setting/channel_affinity_setting.go
- [Pending] setting/operation_setting/checkin_setting.go
- [Pending] setting/operation_setting/general_setting.go
- [Pending] setting/operation_setting/monitor_setting.go
- [Pending] setting/operation_setting/operation_setting.go
- [Pending] setting/operation_setting/payment_setting.go
- [Pending] setting/operation_setting/payment_setting_old.go
- [Pending] setting/operation_setting/quota_setting.go
- [Pending] setting/operation_setting/status_code_ranges.go
- [Pending] setting/operation_setting/status_code_ranges_test.go
- [Pending] setting/operation_setting/token_setting.go
- [Pending] setting/operation_setting/tools.go
- [Pending] setting/performance_setting/config.go
- [Pending] setting/ratio_setting/cache_ratio.go
- [Pending] setting/ratio_setting/compact_suffix.go
- [Pending] setting/ratio_setting/expose_ratio.go
- [Pending] setting/ratio_setting/exposed_cache.go
- [Pending] setting/ratio_setting/group_ratio.go
- [Pending] setting/ratio_setting/model_ratio.go
- [Pending] setting/reasoning/suffix.go
- [Pending] setting/system_setting/discord.go
- [Pending] setting/system_setting/fetch_setting.go
- [Pending] setting/system_setting/legal.go
- [Pending] setting/system_setting/oidc.go
- [Pending] setting/system_setting/passkey.go
- [Pending] setting/system_setting/system_setting_old.go

### types目录
- [Pending] types/channel_error.go
- [Pending] types/error.go
- [Pending] types/file_data.go
- [Pending] types/file_source.go
- [Pending] types/price_data.go
- [Pending] types/relay_format.go
- [Pending] types/request_meta.go
- [Pending] types/rw_map.go
- [Pending] types/set.go

### web目录
- [Pending] web/.eslintrc.cjs
- [Pending] web/.gitignore
- [Pending] web/.prettierrc.mjs
- [Pending] web/bun.lock
- [Pending] web/i18next.config.js
- [Pending] web/index.html
- [Pending] web/jsconfig.json
- [Pending] web/package.json
- [Pending] web/postcss.config.js
- [Pending] web/tailwind.config.js
- [Pending] web/vercel.json
- [Pending] web/vite.config.js
- [Pending] web/public/azure_model_name.png
- [Pending] web/public/cover-4.webp
- [Pending] web/public/favicon.ico
- [Pending] web/public/logo.png
- [Pending] web/public/pay-apple.png
- [Pending] web/public/pay-card.png
- [Pending] web/public/pay-google.png
- [Pending] web/public/ratio.png
- [Pending] web/public/robots.txt
- [Pending] web/src/App.jsx
- [Pending] web/src/index.css
- [Pending] web/src/index.jsx

## 审计状态说明
- [Pending]：未开始审计
- [In_Progress]：正在审计
- [Relationship_Mapped]：关联关系已映射
- [Completed]：审计完成

## 核心文件说明
- 配置文件：涉及系统配置、安全设置的文件
- 核心路由：API路由定义、请求处理入口
- 中间件：认证、授权、CORS等安全相关中间件
- 模型文件：数据模型定义、数据库操作
- 控制器：请求处理逻辑
- 服务层：业务逻辑实现