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
    print_header("测试登录 (密码修正版)")
    
    data = {
        "username": TEST_USERNAME,
        "password": TEST_PASSWORD
    }
    
    try:
        url = BASE_URL + "/api/user/login"
        print(f"\n[+] 尝试登录: {url}")
        resp = requests.post(url, json=data, timeout=10)
        print(f"    状态: {resp.status_code}")
        
        if resp.text:
            try:
                result = resp.json()
                print(f"    JSON: {json.dumps(result, ensure_ascii=False)[:300]}")
                
                if result.get("success"):
                    user_id = result.get("data", {}).get("id")
                    session = resp.cookies.get("session")
                    print(f"    ✅ 登录成功 - 用户ID: {user_id}")
                    if session:
                        print(f"    Session: {session[:50]}...")
                    return user_id, session
                else:
                    print(f"    ❌ 登录失败: {result.get('message')}")
            except:
                print(f"    响应: {resp.text[:200]}")
    except Exception as e:
        print(f"    ❌ 请求失败: {e}")
    
    return None, None

def test_authenticated_endpoints(user_id, session):
    print_header("测试需要认证的接口")

    if not session:
        print("❌ 没有有效的 session")
        return False

    cookies = {"session": session}
    headers = {
        "New-Api-User": str(user_id),
        "Content-Type": "application/json"
    }

    endpoints = [
        ("/api/user/self", "用户信息", "GET"),
        ("/api/user/topup/info", "充值信息", "GET"),
        ("/api/user/topup/self", "充值记录", "GET"),
        ("/api/subscription/plans", "订阅计划", "GET"),
    ]

    success = False
    for path, desc, method in endpoints:
        try:
            url = BASE_URL + path
            print(f"\n[+] {desc} ({path})")
            
            if method == "GET":
                resp = requests.get(url, cookies=cookies, headers=headers, timeout=10)
            else:
                resp = requests.post(url, cookies=cookies, headers=headers, json={}, timeout=10)
            
            print(f"    状态: {resp.status_code}")
            result = resp.json()
            
            if result.get("success"):
                print(f"    ✅ 成功")
                if "data" in result and result["data"]:
                    data_str = json.dumps(result["data"], ensure_ascii=False)
                    print(f"    数据: {data_str[:200]}...")
                success = True
            else:
                print(f"    ❌ {result.get('message', '未知错误')}")
        except Exception as e:
            print(f"    ❌ 请求异常: {e}")
    
    return success

def test_create_topup_order(user_id, session):
    print_header("测试创建充值订单")
    
    if not session:
        print("❌ 没有有效的 session")
        return

    cookies = {"session": session}
    headers = {
        "New-Api-User": str(user_id),
        "Content-Type": "application/json"
    }

    order_data = {
        "amount": 500,
        "payment_method": "alipay"
    }
    
    try:
        url = BASE_URL + "/api/user/pay"
        print(f"\n[+] 创建500元充值订单")
        print(f"    请求: {json.dumps(order_data)}")
        
        resp = requests.post(url, cookies=cookies, headers=headers, json=order_data, timeout=10)
        print(f"    状态: {resp.status_code}")
        
        if resp.text:
            try:
                result = resp.json()
                print(f"    响应: {json.dumps(result, ensure_ascii=False)[:400]}")
                
                if result.get("success"):
                    print(f"    ✅ 订单创建成功")
                    if "url" in result.get("data", {}):
                        print(f"    支付链接: {result['data']['url'][:100]}...")
                else:
                    print(f"    ❌ 创建失败: {result.get('message')}")
            except:
                print(f"    响应: {resp.text[:200]}")
    except Exception as e:
        print(f"    ❌ 请求异常: {e}")

def analyze_external_payment_link():
    print_header("分析外部支付链接")
    
    payment_link = "https://vip1.zhunfu.cn/pay/wap/2026050319070998608/"
    
    print(f"\n[+] 访问支付链接: {payment_link}")
    
    try:
        resp = requests.get(payment_link, timeout=15, allow_redirects=True)
        print(f"    最终URL: {resp.url}")
        print(f"    状态: {resp.status_code}")
        print(f"    Content-Type: {resp.headers.get('Content-Type', 'N/A')}")
        
        if resp.status_code == 200:
            content_preview = resp.text[:500] if resp.text else "空内容"
            print(f"    内容预览: {content_preview}...")
            
            if "alipay" in resp.text.lower() or "支付宝" in resp.text:
                print(f"    ⚠️  包含支付宝相关内容")
            if "wechat" in resp.text.lower() or "微信" in resp.text:
                print(f"    ⚠️  包含微信支付相关内容")
    except Exception as e:
        print(f"    ❌ 请求失败: {e}")

def test_webhook_endpoints():
    print_header("测试 Webhook 端点")

    test_endpoints = [
        ("/api/user/epay/notify", "用户充值回调"),
        ("/api/subscription/epay/notify", "订阅回调"),
    ]

    for path, desc in test_endpoints:
        try:
            url = BASE_URL + path
            print(f"\n[+] 测试 {desc}")
            
            params = {
                "trade_status": "TRADE_SUCCESS",
                "service_trade_no": f"SIM{U}20{int(time.time())}",
                "money": "500.00",
            }
            
            resp_get = requests.get(url, params=params, timeout=10)
            print(f"    GET: {resp_get.status_code} - {resp_get.text[:30]}")
            
            resp_post = requests.post(url, data=params, timeout=10)
            print(f"    POST: {resp_post.status_code} - {resp_post.text[:30]}")
            
            if resp_get.text == "fail" and resp_post.text == "fail":
                print(f"    ✅ 签名验证失败（安全）")
            elif resp_get.text == "success":
                print(f"    ⚠️  可能存在问题，请检查")
        except Exception as e:
            print(f"    ❌ 请求异常: {e}")

def main():
    print_header("timyai.com 安全测试 (修正版)")
    
    user_id, session = test_login()
    
    if user_id and session:
        test_authenticated_endpoints(user_id, session)
        test_create_topup_order(user_id, session)
    
    test_webhook_endpoints()
    analyze_external_payment_link()
    
    print_header("测试完成")

if __name__ == "__main__":
    main()
