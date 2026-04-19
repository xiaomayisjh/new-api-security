#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
调试登录功能，查看登录返回的数据结构
"""

from api_client import NewAPIClient


def debug_login():
    """调试登录功能"""
    # 初始化客户端，使用实际的服务器地址
    client = NewAPIClient(base_url="https://meaior.cn")
    
    # 测试账号信息
    username = "xiaomayisjh"
    password = "sjh@101709"
    
    print("=== 开始调试登录 ===")
    print(f"测试账号: {username}")
    
    # 测试登录，打印详细信息
    print("\n1. 测试登录...")
    status_code, data = client._make_request("POST", "/api/user/login", json={"username": username, "password": password})
    print(f"状态码: {status_code}")
    print(f"返回数据: {data}")
    print(f"Cookies: {dict(client.session.cookies)}")
    
    # 测试获取用户信息，打印详细信息
    print("\n2. 测试获取用户信息...")
    status_code, data = client._make_request("GET", "/api/user/self")
    print(f"状态码: {status_code}")
    print(f"返回数据: {data}")
    
    print("\n=== 调试完成 ===")


if __name__ == "__main__":
    debug_login()
