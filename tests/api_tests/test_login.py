#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试登录功能和基本 API 调用
使用提供的账号测试 API 功能
"""

from api_client import NewAPIClient


def test_login_and_basic_api():
    """测试登录和基本 API 功能"""
    # 初始化客户端，使用实际的服务器地址
    client = NewAPIClient(base_url="https://meaior.cn")
    
    # 测试账号信息
    username = "xiaomayisjh"
    password = "sjh@101709"
    
    print("=== 开始测试 API ===")
    print(f"测试账号: {username}")
    
    # 1. 测试登录
    print("\n1. 测试登录...")
    success, data = client.login(username, password)
    print(f"登录结果: {'成功' if success else '失败'}")
    if not success:
        print(f"登录失败原因: {data.get('message', '未知错误')}")
        return
    
    # 2. 测试获取当前用户信息
    print("\n2. 测试获取用户信息...")
    success, data = client.get_self()
    print(f"获取用户信息结果: {'成功' if success else '失败'}")
    if success:
        user_data = data.get('data', {})
        print(f"用户名: {user_data.get('username')}")
        print(f"邮箱: {user_data.get('email')}")
        print(f"余额: {user_data.get('quota')}")
    
    # 3. 测试获取系统状态
    print("\n3. 测试获取系统状态...")
    success, data = client.get_status()
    print(f"获取系统状态结果: {'成功' if success else '失败'}")
    if success:
        status_data = data.get('data', {})
        print(f"系统状态: {status_data.get('status')}")
        print(f"版本: {status_data.get('version')}")
    
    # 4. 测试获取模型列表
    print("\n4. 测试获取模型列表...")
    success, data = client.get_models()
    print(f"获取模型列表结果: {'成功' if success else '失败'}")
    if success:
        models = data.get('data', {})
        print(f"模型数据类型: {type(models)}")
        print(f"模型提供商数量: {len(models)}")
        if models:
            print("部分模型提供商:")
            for provider_id, provider_models in list(models.items())[:3]:
                if isinstance(provider_models, list):
                    print(f"提供商 {provider_id}: {len(provider_models)} 个模型")
                    if provider_models:
                        print(f"  部分模型: {', '.join(provider_models[:3])}...")
    
    # 5. 测试获取用户日志
    print("\n5. 测试获取用户日志...")
    success, data = client.get_logs_self()
    print(f"获取用户日志结果: {'成功' if success else '失败'}")
    if success:
        log_data = data.get('data', {})
        print(f"日志总数: {log_data.get('total', 0)}")
        print(f"当前页: {log_data.get('page', 0)}")
        print(f"每页大小: {log_data.get('page_size', 0)}")
        items = log_data.get('items', [])
        if items:
            print("最近的日志:")
            for item in items[:2]:
                print(f"- {item.get('content', '')}")
    
    # 6. 测试获取公告
    print("\n6. 测试获取公告...")
    success, data = client.get_notice()
    print(f"获取公告结果: {'成功' if success else '失败'}")
    if success:
        notices = data.get('data', [])
        print(f"公告数量: {len(notices)}")
    
    # 7. 测试获取关于信息
    print("\n7. 测试获取关于信息...")
    success, data = client.get_about()
    print(f"获取关于信息结果: {'成功' if success else '失败'}")
    if success:
        about_data = data.get('data', {})
        print(f"关于信息: {about_data}")
    
    # 8. 测试获取价格信息
    print("\n8. 测试获取价格信息...")
    success, data = client.get_pricing()
    print(f"获取价格信息结果: {'成功' if success else '失败'}")
    if success:
        pricing_data = data.get('data', {})
        print(f"价格信息: {pricing_data}")
    
    print("\n=== 测试完成 ===")


if __name__ == "__main__":
    test_login_and_basic_api()
