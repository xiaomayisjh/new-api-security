#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
调试 API 调用，查看失败的 API 详细信息
"""

from api_client import NewAPIClient


def debug_api_calls():
    """调试 API 调用"""
    # 初始化客户端，使用实际的服务器地址
    client = NewAPIClient(base_url="https://meaior.cn")
    
    # 测试账号信息
    username = "xiaomayisjh"
    password = "sjh@101709"
    
    print("=== 开始调试 API 调用 ===")
    print(f"测试账号: {username}")
    
    # 1. 测试登录
    print("\n1. 测试登录...")
    status_code, data = client._make_request("POST", "/api/user/login", json={"username": username, "password": password})
    print(f"状态码: {status_code}")
    print(f"返回数据: {data}")
    print(f"Cookies: {dict(client.session.cookies)}")
    
    if data.get("success", False):
        client.user_info = data.get("data")
        client.user_id = client.user_info.get("id")
        client.session.headers.update({"New-Api-User": str(client.user_id)})
        print(f"设置的 New-Api-User: {client.session.headers.get('New-Api-User')}")
    else:
        print("登录失败，无法继续测试")
        return
    
    # 2. 测试获取用户信息
    print("\n2. 测试获取用户信息...")
    status_code, data = client._make_request("GET", "/api/user/self")
    print(f"状态码: {status_code}")
    print(f"返回数据: {data}")
    
    # 3. 测试获取用户可用模型
    print("\n3. 测试获取用户可用模型...")
    status_code, data = client._make_request("GET", "/api/user/self/models")
    print(f"状态码: {status_code}")
    print(f"返回数据: {data}")
    
    # 4. 测试获取签到状态
    print("\n4. 测试获取签到状态...")
    status_code, data = client._make_request("GET", "/api/user/self/checkin")
    print(f"状态码: {status_code}")
    print(f"返回数据: {data}")
    
    # 5. 测试生成访问令牌
    print("\n5. 测试生成访问令牌...")
    status_code, data = client._make_request("GET", "/api/user/self/token")
    print(f"状态码: {status_code}")
    print(f"返回数据: {data}")
    
    # 6. 测试获取用户日志
    print("\n6. 测试获取用户日志...")
    status_code, data = client._make_request("GET", "/api/log/self")
    print(f"状态码: {status_code}")
    print(f"返回数据: {data}")
    
    print("\n=== 调试完成 ===")


if __name__ == "__main__":
    debug_api_calls()
