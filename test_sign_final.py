#!/usr/bin/env python3
import requests
import hashlib
import time
from urllib.parse import urlencode

BASE_URL = "https://timyai.com"
TEST_USERNAME = "antplayer"
TEST_PASSWORD = "sjh@101709"
REAL_TRADE_NO = "USR20NO5FFXID1777806504"

def test_login():
    print("\n[1] 登录...")
    data = {"username": TEST_USERNAME, "password": TEST_PASSWORD}
    resp = requests.post(BASE_URL + "/api/user/login", json=data, timeout=10)
    result = resp.json()
    if result.get("success"):
        return result.get("data", {}).get("id"), resp.cookies.get("session")
    return None, None

def get_order_info(user_id, session):
    print("\n[2] 获取订单...")
    cookies = {"session": session}
    headers = {"New-Api-User": str(user_id)}
    resp = requests.get(BASE_URL + "/api/user/topup/self", 
                       cookies=cookies, headers=headers, timeout=10)
    result = resp.json()
    
    if result.get("success"):
        for item in result.get("data", {}).get("items", []):
            if item.get('trade_no') == REAL_TRADE_NO:
                print(f"✅ 订单: {item.get('trade_no')}, {item.get('money')}元, {item.get('payment_method')}")
                return item
    return None

def generate_sign_epay(params, key):
    """易支付官方签名算法"""
    # 1. 过滤: 删除sign, sign_type和空值参数
    filtered = {k: v for k, v in params.items() if k not in ['sign', 'sign_type'] and v}
    
    # 2. 按ASCII码从小到大排序
    sorted_keys = sorted(filtered.keys())
    
    # 3. 拼接成URL键值对格式
    url_string = '&'.join([f"{k}={filtered[k]}" for k in sorted_keys])
    
    # 4. MD5(URL字符串 + key)
    sign_source = url_string + key
    sign = hashlib.md5(sign_source.encode()).hexdigest()
    
    return sign, url_string, sign_source

def test_various_param_combinations(order):
    print("\n[3] 测试不同参数组合...")
    
    url = BASE_URL + "/api/user/epay/notify"
    
    # 参数组合1: 使用money参数
    params1 = {
        "pid": "1378",
        "out_trade_no": order.get('trade_no'),
        "trade_status": "TRADE_SUCCESS",
        "money": str(order.get('money')),
        "type": order.get('payment_method'),
    }
    
    # 参数组合2: 使用trade_fee参数
    params2 = {
        "pid": "1378",
        "out_trade_no": order.get('trade_no'),
        "trade_status": "TRADE_SUCCESS",
        "trade_fee": str(order.get('money')),
        "type": order.get('payment_method'),
    }
    
    # 参数组合3: 添加更多参数
    params3 = {
        "pid": "1378",
        "out_trade_no": order.get('trade_no'),
        "trade_status": "TRADE_SUCCESS",
        "money": str(order.get('money')),
        "type": order.get('payment_method'),
        "time": str(int(time.time())),
    }
    
    param_sets = [
        ("money参数", params1),
        ("trade_fee参数", params2),
        ("money+time参数", params3),
    ]
    
    # 常见密钥
    keys = ["test", "123456", "key", "secret", "epay", "zhunfu", "1378", "timyai", ""]
    
    for name, params in param_sets:
        print(f"\n--- 测试 {name} ---")
        
        for key in keys:
            sign, url_str, source = generate_sign_epay(params.copy(), key)
            test_params = params.copy()
            test_params['sign'] = sign
            
            try:
                resp = requests.post(url, data=test_params, timeout=10)
                
                if resp.text == "success":
                    print(f"\n✅✅✅ 成功! 参数: {name}, 密钥: '{key}'")
                    print(f"   URL字符串: {url_str}")
                    print(f"   签名源: {source}")
                    print(f"   签名: {sign}")
                    return True, key, sign, url_str
                    
            except Exception as e:
                pass
        
        print(f"  ❌ {name} 所有密钥失败")
    
    return False, None, None, None

def test_with_real_sign_format(order):
    """测试实际的签名格式"""
    print("\n[4] 测试实际回调参数...")
    
    url = BASE_URL + "/api/user/epay/notify"
    
    # 根据易支付SDK，Verify方法接收的回调参数
    # 可能包含: pid, out_trade_no, trade_status, trade_fee, type, trade_no等
    
    params = {
        "pid": "1378",
        "out_trade_no": order.get('trade_no'),
        "trade_status": "TRADE_SUCCESS",
        "trade_fee": str(order.get('money')),
        "type": order.get('payment_method'),
    }
    
    print(f"参数: {params}")
    
    # 生成签名并测试
    keys_to_try = ["test", "epay", "key", "secret"]
    
    for key in keys_to_try:
        sign, url_str, source = generate_sign_epay(params.copy(), key)
        
        print(f"\n尝试密钥: '{key}'")
        print(f"  URL字符串: {url_str}")
        print(f"  签名: {sign}")
        
        test_params = params.copy()
        test_params['sign'] = sign
        
        try:
            resp = requests.post(url, data=test_params, timeout=10)
            print(f"  响应: {resp.text}")
            
            if resp.text == "success":
                print(f"  ✅ 成功!")
                return True
        except Exception as e:
            print(f"  异常: {e}")
    
    return False

def verify_order_status(user_id, session, trade_no):
    print("\n[5] 验证订单状态...")
    cookies = {"session": session}
    headers = {"New-Api-User": str(user_id)}
    
    try:
        resp = requests.get(BASE_URL + "/api/user/topup/self", 
                          cookies=cookies, headers=headers, timeout=10)
        result = resp.json()
        
        if result.get("success"):
            for item in result.get("data", {}).get("items", []):
                if item.get('trade_no') == trade_no:
                    print(f"订单状态: {item.get('status')}, 金额: {item.get('money')}元")
                    return item.get('status')
    except Exception as e:
        print(f"验证异常: {e}")
    
    return None

def main():
    print("="*60)
    print("timyai.com 签名验证测试 (修正版)")
    print("="*60)
    
    print("""
易支付官方签名算法:
1. 参数按ASCII码从小到大排序
2. sign、sign_type和空值不参与签名
3. 拼接成 a=b&c=d&e=f 格式
4. MD5(字符串 + key)
""")
    
    user_id, session = test_login()
    if not user_id:
        return
    
    order = get_order_info(user_id, session)
    if not order:
        return
    
    success, key, sign, url_str = test_various_param_combinations(order)
    
    if not success:
        test_with_real_sign_format(order)
    
    verify_order_status(user_id, session, REAL_TRADE_NO)
    
    print("\n" + "="*60)
    print("测试完成")
    print("="*60)

if __name__ == "__main__":
    main()
