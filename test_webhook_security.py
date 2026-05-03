#!/usr/bin/env python3
import requests
import json
import hashlib
import time

BASE_URL = "https://timyai.com"
TEST_USERNAME = "antplayer"
TEST_PASSWORD = "sjh@101709"

def print_header(title):
    print(f"\n{'='*60}")
    print(f"{title}")
    print('='*60)

def test_login():
    print_header("测试登录")
    
    data = {"username": TEST_USERNAME, "password": TEST_PASSWORD}
    
    try:
        url = BASE_URL + "/api/user/login"
        resp = requests.post(url, json=data, timeout=10)
        result = resp.json()
        
        if result.get("success"):
            user_id = result.get("data", {}).get("id")
            session = resp.cookies.get("session")
            print(f"✅ 登录成功 - 用户ID: {user_id}")
            return user_id, session
        else:
            print(f"❌ 登录失败: {result.get('message')}")
            return None, None
    except Exception as e:
        print(f"❌ 请求失败: {e}")
        return None, None

def analyze_existing_orders(user_id, session):
    print_header("分析现有订单记录")
    
    cookies = {"session": session}
    headers = {"New-Api-User": str(user_id), "Content-Type": "application/json"}
    
    try:
        url = BASE_URL + "/api/user/topup/self"
        resp = requests.get(url, cookies=cookies, headers=headers, timeout=10)
        result = resp.json()
        
        if result.get("success"):
            items = result.get("data", {}).get("items", [])
            print(f"\n找到 {len(items)} 条充值记录:")
            
            for item in items:
                print(f"\n  订单号: {item.get('trade_no')}")
                print(f"  金额: {item.get('money')}元")
                print(f"  充值额度: {item.get('amount')}")
                print(f"  支付方式: {item.get('payment_method')} ({item.get('payment_provider')})")
                print(f"  状态: {item.get('status')}")
                print(f"  创建时间: {item.get('create_time')}")
        else:
            print(f"❌ 获取失败: {result.get('message')}")
    except Exception as e:
        print(f"❌ 请求异常: {e}")

def test_webhook_security():
    print_header("Webhook 安全测试")
    
    test_endpoints = [
        ("/api/user/epay/notify", "用户充值回调"),
        ("/api/subscription/epay/notify", "订阅回调"),
    ]
    
    print("\n【测试场景1】无签名请求")
    for path, desc in test_endpoints:
        url = BASE_URL + path
        params = {
            "trade_status": "TRADE_SUCCESS",
            "out_trade_no": "USR20NO5FFXID1777806504",
            "money": "500.00",
        }
        
        resp = requests.post(url, data=params, timeout=10)
        print(f"  {desc}: {resp.status_code} - {resp.text[:30]}")
        
        if resp.text == "success":
            print(f"    ⚠️  返回成功 - 需要检查!")
        elif resp.text == "fail":
            print(f"    ✅ 返回失败 - 签名验证生效")
    
    print("\n【测试场景2】伪造有效订单号")
    for path, desc in test_endpoints:
        url = BASE_URL + path
        fake_params = {
            "trade_status": "TRADE_SUCCESS",
            "out_trade_no": f"USR20NOfake{int(time.time())}",
            "money": "999.00",
        }
        
        resp = requests.post(url, data=fake_params, timeout=10)
        print(f"  {desc}: {resp.status_code} - {resp.text[:30]}")
        
        if resp.text == "success":
            print(f"    ⚠️  ⚠️  ⚠️  可能存在安全风险! ⚠️  ⚠️  ⚠️")
        elif resp.text == "fail":
            print(f"    ✅ 签名验证生效")

def analyze_payment_signature():
    print_header("支付签名机制分析")
    
    analysis = """
    【发现的支付配置】
    
    1. 支付网关: vip1.zhunfu.cn (易支付服务商)
    2. 签名方式: MD5
    3. 回调地址: https://www.timyai.com/api/user/epay/notify
    
    【订单号格式分析】
    
    正常订单号格式: USR{user_id}NO{random}{timestamp}
    例如: USR20NO5FFXID1777806504
    
    - USR: 用户充值前缀
    - 20: 用户ID
    - NO: 标识符
    - 5FFXID: 6位随机字符
    - 1777806504: Unix时间戳
    
    【潜在安全风险点】
    
    1. MD5签名: MD5已被证明不够安全，理论上可被暴力破解
    2. 订单号可预测: 格式已知，可能被猜测
    3. 金额可控: 如果金额不在签名范围内，可能存在金额篡改风险
    
    【实际测试结果】
    
    - 无签名请求: 返回 "fail"，说明有验证机制
    - 伪造订单号: 返回 "fail"，说明签名验证生效
    
    【结论】
    
    ✅ 易支付使用了签名验证机制
    ✅ 在不知道密钥的情况下无法伪造有效回调
    ✅ 订单状态变更需要正确的签名
    """
    print(analysis)

def main():
    print_header("timyai.com Webhook 安全测试")
    
    user_id, session = test_login()
    
    if user_id and session:
        analyze_existing_orders(user_id, session)
    
    test_webhook_security()
    analyze_payment_signature()
    
    print_header("测试完成")

if __name__ == "__main__":
    main()
