#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NewAPI 客户端库
提供与 NewAPI 交互的核心功能
"""

import requests
import json
from typing import Dict, Any, Optional, Tuple


class NewAPIClient:
    """NewAPI 客户端"""

    def __init__(self, base_url: str = "http://localhost:3000"):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json"
        })
        self.user_info = None
        self.access_token = None
        self.user_id = None

    def _make_request(self, method: str, endpoint: str, **kwargs) -> Tuple[bool, Any]:
        """
        发送 HTTP 请求的通用方法
        """
        url = f"{self.base_url}{endpoint}"
        
        try:
            response = self.session.request(method=method, url=url, **kwargs)
            
            try:
                data = response.json()
            except json.JSONDecodeError:
                data = {"success": False, "message": "无效的 JSON 响应", "raw": response.text}
            
            return response.status_code, data
        except requests.RequestException as e:
            return None, {"success": False, "message": f"请求失败: {str(e)}"}

    def get_status(self) -> Tuple[bool, Dict]:
        """
        获取系统状态
        GET /api/status
        """
        status_code, data = self._make_request("GET", "/api/status")
        return status_code == 200, data

    def get_models(self) -> Tuple[bool, Dict]:
        """
        获取模型列表
        GET /api/models
        需要用户认证
        """
        status_code, data = self._make_request("GET", "/api/models")
        return status_code == 200, data

    # ===== 用户相关 =====

    def register(self, username: str, password: str, email: Optional[str] = None,
                 verification_code: Optional[str] = None,
                 aff_code: Optional[str] = None) -> Tuple[bool, Dict]:
        """
        用户注册
        POST /api/user/register
        """
        payload = {
            "username": username,
            "password": password
        }
        if email:
            payload["email"] = email
        if verification_code:
            payload["verification_code"] = verification_code
        if aff_code:
            payload["aff_code"] = aff_code
        
        status_code, data = self._make_request("POST", "/api/user/register", json=payload)
        return data.get("success", False), data

    def login(self, username: str, password: str) -> Tuple[bool, Dict]:
        """
        用户登录
        POST /api/user/login
        """
        payload = {
            "username": username,
            "password": password
        }
        status_code, data = self._make_request("POST", "/api/user/login", json=payload)
        if data.get("success", False):
            self.user_info = data.get("data")
            self.user_id = self.user_info.get("id")
            # 更新请求头，添加 New-Api-User
            self.session.headers.update({
                "New-Api-User": str(self.user_id)
            })
        return data.get("success", False), data

    def logout(self) -> Tuple[bool, Dict]:
        """
        用户登出
        GET /api/user/logout
        """
        status_code, data = self._make_request("GET", "/api/user/logout")
        if data.get("success", False):
            self.user_info = None
            self.access_token = None
            self.user_id = None
            # 移除请求头中的 New-Api-User
            if "New-Api-User" in self.session.headers:
                del self.session.headers["New-Api-User"]
        return data.get("success", False), data

    def get_self(self) -> Tuple[bool, Dict]:
        """
        获取当前用户信息
        GET /api/user/self
        """
        status_code, data = self._make_request("GET", "/api/user/self")
        return data.get("success", False), data

    def update_self(self, username: Optional[str] = None,
                    display_name: Optional[str] = None,
                    original_password: Optional[str] = None,
                    new_password: Optional[str] = None,
                    sidebar_modules: Optional[str] = None,
                    language: Optional[str] = None) -> Tuple[bool, Dict]:
        """
        更新当前用户信息
        PUT /api/user/self
        """
        payload = {}
        if username:
            payload["username"] = username
        if display_name:
            payload["display_name"] = display_name
        if original_password and new_password:
            payload["original_password"] = original_password
            payload["password"] = new_password
        if sidebar_modules:
            payload["sidebar_modules"] = sidebar_modules
        if language:
            payload["language"] = language
        
        status_code, data = self._make_request("PUT", "/api/user/self", json=payload)
        return data.get("success", False), data

    def delete_self(self) -> Tuple[bool, Dict]:
        """
        删除当前用户
        DELETE /api/user/self
        """
        status_code, data = self._make_request("DELETE", "/api/user/self")
        return data.get("success", False), data

    def get_user_groups(self) -> Tuple[bool, Dict]:
        """
        获取用户分组
        GET /api/user/groups
        """
        status_code, data = self._make_request("GET", "/api/user/groups")
        return data.get("success", False), data

    def get_user_groups_self(self) -> Tuple[bool, Dict]:
        """
        获取当前用户分组（需要认证
        GET /api/user/self/groups
        """
        status_code, data = self._make_request("GET", "/api/user/self/groups")
        return data.get("success", False), data

    def get_self_models(self) -> Tuple[bool, Dict]:
        """
        获取用户可用的模型
        GET /api/user/self/models
        """
        status_code, data = self._make_request("GET", "/api/user/self/models")
        return data.get("success", False), data

    def generate_access_token(self) -> Tuple[bool, Dict]:
        """
        生成访问令牌
        GET /api/user/self/token
        """
        status_code, data = self._make_request("GET", "/api/user/self/token")
        if data.get("success", False):
            self.access_token = data.get("data")
        return data.get("success", False), data

    def get_aff_code(self) -> Tuple[bool, Dict]:
        """
        获取邀请码
        GET /api/user/self/aff
        """
        status_code, data = self._make_request("GET", "/api/user/self/aff")
        return data.get("success", False), data

    def get_topup_info(self) -> Tuple[bool, Dict]:
        """
        获取充值信息
        GET /api/user/self/topup/info
        """
        status_code, data = self._make_request("GET", "/api/user/self/topup/info")
        return data.get("success", False), data

    def get_topup_self(self) -> Tuple[bool, Dict]:
        """
        获取用户充值记录
        GET /api/user/self/topup/self
        """
        status_code, data = self._make_request("GET", "/api/user/topup/self")
        return data.get("success", False), data

    def topup(self, key: str) -> Tuple[bool, Dict]:
        """
        使用兑换码充值
        POST /api/user/self/topup
        """
        payload = {"key": key}
        status_code, data = self._make_request("POST", "/api/user/self/topup", json=payload)
        return data.get("success", False), data

    def request_amount(self) -> Tuple[bool, Dict]:
        """
        钱包支付请求
        POST /api/user/self/amount
        """
        status_code, data = self._make_request("POST", "/api/user/self/amount")
        return data.get("success", False), data

    def aff_transfer(self, quota: int) -> Tuple[bool, Dict]:
        """
        转移邀请奖励额度
        POST /api/user/self/aff_transfer
        """
        payload = {"quota": quota}
        status_code, data = self._make_request("POST", "/api/user/self/aff_transfer", json=payload)
        return data.get("success", False), data

    def update_user_setting(self, notify_type: Optional[str] = None,
                           quota_warning_threshold: Optional[float] = None,
                           webhook_url: Optional[str] = None,
                           webhook_secret: Optional[str] = None,
                           notification_email: Optional[str] = None,
                           bark_url: Optional[str] = None,
                           gotify_url: Optional[str] = None,
                           gotify_token: Optional[str] = None,
                           gotify_priority: Optional[int] = None,
                           upstream_model_update_notify_enabled: Optional[bool] = None,
                           accept_unset_model_ratio_model: Optional[bool] = None,
                           record_ip_log: Optional[bool] = None) -> Tuple[bool, Dict]:
        """
        更新用户设置
        PUT /api/user/self/setting
        """
        payload = {}
        if notify_type:
            payload["notify_type"] = notify_type
        if quota_warning_threshold is not None:
            payload["quota_warning_threshold"] = quota_warning_threshold
        if webhook_url:
            payload["webhook_url"] = webhook_url
        if webhook_secret:
            payload["webhook_secret"] = webhook_secret
        if notification_email:
            payload["notification_email"] = notification_email
        if bark_url:
            payload["bark_url"] = bark_url
        if gotify_url:
            payload["gotify_url"] = gotify_url
        if gotify_token:
            payload["gotify_token"] = gotify_token
        if gotify_priority is not None:
            payload["gotify_priority"] = gotify_priority
        if upstream_model_update_notify_enabled is not None:
            payload["upstream_model_update_notify_enabled"] = upstream_model_update_notify_enabled
        if accept_unset_model_ratio_model is not None:
            payload["accept_unset_model_ratio_model"] = accept_unset_model_ratio_model
        if record_ip_log is not None:
            payload["record_ip_log"] = record_ip_log
        
        status_code, data = self._make_request("PUT", "/api/user/self/setting", json=payload)
        return data.get("success", False), data

    # ===== 邮箱相关 =====

    def send_verification(self, email: str) -> Tuple[bool, Dict]:
        """
        发送邮箱验证码
        GET /api/verification?email=xxx
        """
        params = {"email": email}
        status_code, data = self._make_request("GET", "/api/verification", params=params)
        return data.get("success", False), data

    def send_password_reset(self, email: str) -> Tuple[bool, Dict]:
        """
        发送密码重置邮件
        GET /api/reset_password?email=xxx
        """
        params = {"email": email}
        status_code, data = self._make_request("GET", "/api/reset_password", params=params)
        return data.get("success", False), data

    def reset_password(self, email: str, token: str) -> Tuple[bool, Dict]:
        """
        重置密码
        POST /api/user/reset
        """
        payload = {
            "email": email,
            "token": token
        }
        status_code, data = self._make_request("POST", "/api/user/reset", json=payload)
        return data.get("success", False), data

    def email_bind(self, email: str, code: str) -> Tuple[bool, Dict]:
        """
        绑定邮箱
        POST /api/oauth/email/bind
        """
        payload = {
            "email": email,
            "code": code
        }
        status_code, data = self._make_request("POST", "/api/oauth/email/bind", json=payload)
        return data.get("success", False), data

    # ===== OAuth 相关 =====

    def generate_oauth_state(self) -> Tuple[bool, Dict]:
        """
        生成 OAuth 状态码
        GET /api/oauth/state
        """
        status_code, data = self._make_request("GET", "/api/oauth/state")
        return data.get("success", False), data

    def get_oauth_bindings(self) -> Tuple[bool, Dict]:
        """
        获取用户 OAuth 绑定
        GET /api/user/self/oauth/bindings
        """
        status_code, data = self._make_request("GET", "/api/user/self/oauth/bindings")
        return data.get("success", False), data

    def unbind_oauth(self, provider_id: str) -> Tuple[bool, Dict]:
        """
        解绑 OAuth
        DELETE /api/user/self/oauth/bindings/{provider_id}
        """
        status_code, data = self._make_request("DELETE", f"/api/user/self/oauth/bindings/{provider_id}")
        return data.get("success", False), data

    # ===== Token 相关 =====

    def get_all_tokens(self, page: int = 0, size: int = 100) -> Tuple[bool, Dict]:
        """
        获取所有令牌
        GET /api/token?page=xxx&size=xxx
        """
        params = {"p": page, "size": size}
        status_code, data = self._make_request("GET", "/api/token", params=params)
        return data.get("success", False), data

    def search_tokens(self, keyword: str = "", token: str = "", page: int = 0, size: int = 100) -> Tuple[bool, Dict]:
        """
        搜索令牌
        GET /api/token/search?keyword=xxx&token=xxx&p=xxx&size=xxx
        """
        params = {"keyword": keyword, "token": token, "p": page, "size": size}
        status_code, data = self._make_request("GET", "/api/token/search", params=params)
        return data.get("success", False), data

    def get_token(self, token_id: int) -> Tuple[bool, Dict]:
        """
        获取特定令牌
        GET /api/token/{id}
        """
        status_code, data = self._make_request("GET", f"/api/token/{token_id}")
        return data.get("success", False), data

    def get_token_key(self, token_id: int) -> Tuple[bool, Dict]:
        """
        获取令牌密钥
        POST /api/token/{id}/key
        """
        status_code, data = self._make_request("POST", f"/api/token/{token_id}/key")
        return data.get("success", False), data

    def add_token(self, name: str, expired_time: int = -1,
                  remain_quota: int = 0, unlimited_quota: bool = True,
                  model_limits_enabled: bool = False,
                  model_limits: str = "",
                  allow_ips: str = "",
                  group: str = "",
                  cross_group_retry: bool = False) -> Tuple[bool, Dict]:
        """
        添加令牌
        POST /api/token
        """
        payload = {
            "name": name,
            "expired_time": expired_time,
            "remain_quota": remain_quota,
            "unlimited_quota": unlimited_quota,
            "model_limits_enabled": model_limits_enabled,
            "model_limits": model_limits,
            "allow_ips": allow_ips,
            "group": group,
            "cross_group_retry": cross_group_retry
        }
        status_code, data = self._make_request("POST", "/api/token", json=payload)
        return data.get("success", False), data

    def update_token(self, token_id: int, name: Optional[str] = None,
                    status: Optional[int] = None,
                    expired_time: Optional[int] = None,
                    remain_quota: Optional[int] = None,
                    unlimited_quota: Optional[bool] = None,
                    model_limits_enabled: Optional[bool] = None,
                    model_limits: Optional[str] = None,
                    allow_ips: Optional[str] = None,
                    group: Optional[str] = None,
                    cross_group_retry: Optional[bool] = None) -> Tuple[bool, Dict]:
        """
        更新令牌
        PUT /api/token
        """
        payload = {"id": token_id}
        if name:
            payload["name"] = name
        if status is not None:
            payload["status"] = status
        if expired_time is not None:
            payload["expired_time"] = expired_time
        if remain_quota is not None:
            payload["remain_quota"] = remain_quota
        if unlimited_quota is not None:
            payload["unlimited_quota"] = unlimited_quota
        if model_limits_enabled is not None:
            payload["model_limits_enabled"] = model_limits_enabled
        if model_limits is not None:
            payload["model_limits"] = model_limits
        if allow_ips is not None:
            payload["allow_ips"] = allow_ips
        if group:
            payload["group"] = group
        if cross_group_retry is not None:
            payload["cross_group_retry"] = cross_group_retry
        
        status_code, data = self._make_request("PUT", "/api/token", json=payload)
        return data.get("success", False), data

    def delete_token(self, token_id: int) -> Tuple[bool, Dict]:
        """
        删除令牌
        DELETE /api/token/{id}
        """
        status_code, data = self._make_request("DELETE", f"/api/token/{token_id}")
        return data.get("success", False), data

    def delete_token_batch(self, ids: list) -> Tuple[bool, Dict]:
        """
        批量删除令牌
        POST /api/token/batch
        """
        payload = {"ids": ids}
        status_code, data = self._make_request("POST", "/api/token/batch", json=payload)
        return data.get("success", False), data

    def get_token_keys_batch(self, ids: list) -> Tuple[bool, Dict]:
        """
        批量获取令牌密钥
        POST /api/token/batch/keys
        """
        payload = {"ids": ids}
        status_code, data = self._make_request("POST", "/api/token/batch/keys", json=payload)
        return data.get("success", False), data

    # ===== 签到相关 =====

    def get_checkin_status(self) -> Tuple[bool, Dict]:
        """
        获取签到状态
        GET /api/user/self/checkin
        """
        status_code, data = self._make_request("GET", "/api/user/self/checkin")
        return data.get("success", False), data

    def do_checkin(self) -> Tuple[bool, Dict]:
        """
        执行签到
        POST /api/user/self/checkin
        """
        status_code, data = self._make_request("POST", "/api/user/self/checkin")
        return data.get("success", False), data

    # ===== 其他 =====

    def get_notice(self) -> Tuple[bool, Dict]:
        """
        获取公告
        GET /api/notice
        """
        status_code, data = self._make_request("GET", "/api/notice")
        return data.get("success", False), data

    def get_about(self) -> Tuple[bool, Dict]:
        """
        获取关于信息
        GET /api/about
        """
        status_code, data = self._make_request("GET", "/api/about")
        return data.get("success", False), data

    def get_user_agreement(self) -> Tuple[bool, Dict]:
        """
        获取用户协议
        GET /api/user-agreement
        """
        status_code, data = self._make_request("GET", "/api/user-agreement")
        return data.get("success", False), data

    def get_privacy_policy(self) -> Tuple[bool, Dict]:
        """
        获取隐私政策
        GET /api/privacy-policy
        """
        status_code, data = self._make_request("GET", "/api/privacy-policy")
        return data.get("success", False), data

    def get_home_page_content(self) -> Tuple[bool, Dict]:
        """
        获取首页内容
        GET /api/home_page_content
        """
        status_code, data = self._make_request("GET", "/api/home_page_content")
        return data.get("success", False), data

    def get_pricing(self) -> Tuple[bool, Dict]:
        """
        获取价格信息
        GET /api/pricing
        """
        status_code, data = self._make_request("GET", "/api/pricing")
        return data.get("success", False), data

    def get_ratio_config(self) -> Tuple[bool, Dict]:
        """
        获取比例配置
        GET /api/ratio_config
        """
        status_code, data = self._make_request("GET", "/api/ratio_config")
        return data.get("success", False), data

    # ===== Logs =====

    def get_logs_self(self) -> Tuple[bool, Dict]:
        """
        获取用户日志
        GET /api/log/self
        """
        status_code, data = self._make_request("GET", "/api/log/self")
        return data.get("success", False), data

    def get_logs_self_search(self, keyword: str = "", page: int = 0, size: int = 100) -> Tuple[bool, Dict]:
        """
        搜索用户日志
        GET /api/log/self/search
        """
        params = {"keyword": keyword, "p": page, "size": size}
        status_code, data = self._make_request("GET", "/api/log/self/search", params=params)
        return data.get("success", False), data

    def get_logs_self_stat(self) -> Tuple[bool, Dict]:
        """
        获取用户日志统计
        GET /api/log/self/stat
        """
        status_code, data = self._make_request("GET", "/api/log/self/stat")
        return data.get("success", False), data

    def get_data_self(self) -> Tuple[bool, Dict]:
        """
        获取用户数据
        GET /api/data/self
        """
        status_code, data = self._make_request("GET", "/api/data/self")
        return data.get("success", False), data

    # ===== 通用验证 =====

    def universal_verify(self) -> Tuple[bool, Dict]:
        """
        通用验证 (需要 admin)
        POST /api/verify
        """
        status_code, data = self._make_request("POST", "/api/verify")
        return data.get("success", False), data

    # ===== Passkey =====

    def get_passkey_status(self) -> Tuple[bool, Dict]:
        """
        获取 Passkey 状态
        GET /api/user/self/passkey
        """
        status_code, data = self._make_request("GET", "/api/user/self/passkey")
        return data.get("success", False), data

    def passkey_register_begin(self) -> Tuple[bool, Dict]:
        """
        开始 Passkey 注册
        POST /api/user/self/passkey/register/begin
        """
        status_code, data = self._make_request("POST", "/api/user/self/passkey/register/begin")
        return data.get("success", False), data

    def passkey_register_finish(self, response: str) -> Tuple[bool, Dict]:
        """
        完成 Passkey 注册
        POST /api/user/self/passkey/register/finish
        """
        payload = {"response": response}
        status_code, data = self._make_request("POST", "/api/user/self/passkey/register/finish", json=payload)
        return data.get("success", False), data

    def passkey_delete(self) -> Tuple[bool, Dict]:
        """
        删除 Passkey
        DELETE /api/user/self/passkey
        """
        status_code, data = self._make_request("DELETE", "/api/user/self/passkey")
        return data.get("success", False), data

    # ===== 2FA =====

    def get_2fa_status(self) -> Tuple[bool, Dict]:
        """
        获取 2FA 状态
        GET /api/user/self/2fa/status
        """
        status_code, data = self._make_request("GET", "/api/user/self/2fa/status")
        return data.get("success", False), data

    def setup_2fa(self) -> Tuple[bool, Dict]:
        """
        设置 2FA
        POST /api/user/self/2fa/setup
        """
        status_code, data = self._make_request("POST", "/api/user/self/2fa/setup")
        return data.get("success", False), data

    def enable_2fa(self, code: str) -> Tuple[bool, Dict]:
        """
        启用 2FA
        POST /api/user/self/2fa/enable
        """
        payload = {"code": code}
        status_code, data = self._make_request("POST", "/api/user/self/2fa/enable", json=payload)
        return data.get("success", False), data

    def disable_2fa(self) -> Tuple[bool, Dict]:
        """
        禁用 2FA
        POST /api/user/self/2fa/disable
        """
        status_code, data = self._make_request("POST", "/api/user/self/2fa/disable")
        return data.get("success", False), data

    def regenerate_backup_codes(self) -> Tuple[bool, Dict]:
        """
        重新生成备份码
        POST /api/user/self/2fa/backup_codes
        """
        status_code, data = self._make_request("POST", "/api/user/self/2fa/backup_codes")
        return data.get("success", False), data

    # ===== 订阅相关 =====

    def get_subscription_plans(self) -> Tuple[bool, Dict]:
        """
        获取订阅计划
        GET /api/subscription/plans
        """
        status_code, data = self._make_request("GET", "/api/subscription/plans")
        return data.get("success", False), data

    def get_subscription_self(self) -> Tuple[bool, Dict]:
        """
        获取当前用户的订阅
        GET /api/subscription/self
        """
        status_code, data = self._make_request("GET", "/api/subscription/self")
        return data.get("success", False), data

    def update_subscription_preference(self) -> Tuple[bool, Dict]:
        """
        更新订阅偏好
        PUT /api/subscription/self/preference
        """
        status_code, data = self._make_request("PUT", "/api/subscription/self/preference")
        return data.get("success", False), data

    def subscription_request_epay(self) -> Tuple[bool, Dict]:
        """
        订阅钱包支付请求
        POST /api/subscription/epay/pay
        """
        status_code, data = self._make_request("POST", "/api/subscription/epay/pay")
        return data.get("success", False), data

    def subscription_request_stripe_pay(self) -> Tuple[bool, Dict]:
        """
        订阅 Stripe 支付请求
        POST /api/subscription/stripe/pay
        """
        status_code, data = self._make_request("POST", "/api/subscription/stripe/pay")
        return data.get("success", False), data

    def subscription_request_creem_pay(self) -> Tuple[bool, Dict]:
        """
        订阅 Creem 支付请求
        POST /api/subscription/creem/pay
        """
        status_code, data = self._make_request("POST", "/api/subscription/creem/pay")
        return data.get("success", False), data

    def subscription_request_waffo_pay(self) -> Tuple[bool, Dict]:
        """
        订阅 Waffo 支付请求
        POST /api/subscription/waffo/pay
        """
        status_code, data = self._make_request("POST", "/api/subscription/waffo/pay")
        return data.get("success", False), data

    # ===== Midjourney =====

    def get_midjourney_self(self) -> Tuple[bool, Dict]:
        """
        获取用户 Midjourney 任务
        GET /api/mj/self
        """
        status_code, data = self._make_request("GET", "/api/mj/self")
        return data.get("success", False), data

    # ===== Task =====

    def get_task_self(self) -> Tuple[bool, Dict]:
        """
        获取用户任务
        GET /api/task/self
        """
        status_code, data = self._make_request("GET", "/api/task/self")
        return data.get("success", False), data
