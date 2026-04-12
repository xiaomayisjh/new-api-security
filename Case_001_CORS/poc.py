import requests
import json

# 目标URL - 这里使用一个不需要认证的端点来测试CORS
TARGET_URL = "http://localhost:3000/api/status"

# 恶意网站的源（模拟攻击场景）
MALICIOUS_ORIGIN = "http://evil.com"

def test_cors_config():
    print("Testing CORS configuration...")
    print(f"Target URL: {TARGET_URL}")
    print(f"Malicious origin: {MALICIOUS_ORIGIN}")
    print("=" * 60)
    
    # 发送带有恶意Origin头的请求
    headers = {
        "Origin": MALICIOUS_ORIGIN,
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(TARGET_URL, headers=headers, allow_redirects=False)
        
        print(f"Status Code: {response.status_code}")
        print("Response Headers:")
        for key, value in response.headers.items():
            if "cors" in key.lower() or "origin" in key.lower():
                print(f"  {key}: {value}")
        
        # 检查是否返回了允许跨域的头部
        has_access_control = "Access-Control-Allow-Origin" in response.headers
        has_credentials = "Access-Control-Allow-Credentials" in response.headers
        
        if has_access_control and has_credentials:
            print("\n[VULNERABLE] CORS configuration allows cross-origin requests with credentials!")
            print("This is a security risk as it may allow CSRF attacks.")
        else:
            print("\n[SAFE] CORS configuration does not allow cross-origin requests with credentials.")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_cors_config()