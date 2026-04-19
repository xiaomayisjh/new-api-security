#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NewAPI Token 功能测试
包括：创建 API Key、查看、编辑、删除等功能
"""

import sys
import os
from api_client import NewAPIClient
import time
import random
import string

class Color:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'


def print_info(message: str):
    print(f"{Color.BLUE}[INFO]{Color.ENDC} {message}")


def print_success(message: str):
    print(f"{Color.GREEN}[SUCCESS]{Color.ENDC} {message}")


def print_error(message: str):
    print(f"{Color.RED}[ERROR]{Color.ENDC} {message}")


def print_warning(message: str):
    print(f"{Color.YELLOW}[WARNING]{Color.ENDC} {message}")


def print_header(title: str):
    print(f"\n{Color.BOLD}{'=' * 60}{Color.ENDC}")
    print(f"{Color.BOLD}{title}{Color.ENDC}")
    print(f"{Color.BOLD}{'=' * 60}{Color.ENDC}\n")


def generate_random_string(length: int = 8) -> str:
    """生成随机字符串"""
    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for _ in range(length))


class TokenTest:
    def __init__(self, client: NewAPIClient, test_username: str = None, test_password: str = None):
        self.client = client
        self.results = []
        
        # 生成测试用户信息
        if test_username:
            self.test_username = test_username
        else:
            self.test_username = f"token_test_{generate_random_string(8)}"
        
        if test_password:
            self.test_password = test_password
        else:
            self.test_password = "Test@123456"
        
        self.created_token_ids = []
        self.test_token_id = None
        
        print_info(f"测试用户名: {self.test_username}")

    def setup_user(self):
        """设置用户：注册或登录"""
        print_info("\n--- 设置测试用户 ---")
        # 尝试注册
        success, data = self.client.register(self.test_username, self.test_password)
        if success:
            print_success("用户注册成功!")
        
        # 尝试登录
        success, data = self.client.login(self.test_username, self.test_password)
        if success:
            print_success("用户登录成功!")
            return True
        else:
            print_error(f"用户登录失败: {data.get('message', '未知错误')}")
            return False

    def test_add_token(self) -> bool:
        """测试添加 Token"""
        print_info("\n--- 测试添加 Token ---")
        try:
            token_name = f"test_token_{generate_random_string(6)}"
            success, data = self.client.add_token(
                name=token_name,
                unlimited_quota=True
            )
            if success:
                print_success(f"Token 添加成功! 名称: {token_name}")
                self.results.append(("test_add_token", True, "Token 添加成功"))
                return True
            else:
                print_error(f"Token 添加失败: {data.get('message', '未知错误')}")
                self.results.append(("test_add_token", False, data.get('message', '未知错误')}"))
                return False
        except Exception as e:
            print_error(f"Token 添加异常: {str(e)}")
            self.results.append(("test_add_token", False, str(e)))
            return False

    def test_get_all_tokens(self) -> list:
        """测试获取所有 Token"""
        print_info("\n--- 测试获取所有 Token ---")
        try:
            success, data = self.client.get_all_tokens()
            if success:
                print_success("获取所有 Token 成功!")
                tokens = data.get('data', {}).get('items', [])
                print(f"  Token 数量: {len(tokens)}")
                if tokens:
                    # 保存第一个 Token 的 ID 用于后续测试
                    self.test_token_id = tokens[0].get('id')
                    print(f"  将使用 Token ID: {self.test_token_id} 进行后续测试")
                self.results.append(("test_get_all_tokens", True, "获取所有 Token 成功"))
                return tokens
            else:
                print_error(f"获取 Token 失败: {data.get('message', '未知错误')}")
                self.results.append(("test_get_all_tokens", False, data.get('message', '未知错误')}"))
                return []
        except Exception as e:
            print_error(f"获取 Token 异常: {str(e)}")
            self.results.append(("test_get_all_tokens", False, str(e)))
            return []

    def test_get_token(self) -> bool:
        """测试获取单个 Token"""
        if not self.test_token_id:
            print_warning("没有可用的 Token ID，跳过此测试")
            return False
        
        print_info(f"\n--- 测试获取 Token (ID: {self.test_token_id}) ---")
        try:
            success, data = self.client.get_token(self.test_token_id)
            if success:
                print_success("获取 Token 成功!")
                token_data = data.get('data', {})
                print(f"  Token 名称: {token_data.get('name', 'N/A')}")
                print(f"  Token 状态: {token_data.get('status', 'N/A')}")
                self.results.append(("test_get_token", True, "获取 Token 成功"))
                return True
            else:
                print_error(f"获取 Token 失败: {data.get('message', '未知错误')}")
                self.results.append(("test_get_token", False, data.get('message', '未知错误')}"))
                return False
        except Exception as e:
            print_error(f"获取 Token 异常: {str(e)}")
            self.results.append(("test_get_token", False, str(e)))
            return False

    def test_get_token_key(self) -> bool:
        """测试获取 Token Key"""
        if not self.test_token_id:
            print_warning("没有可用的 Token ID，跳过此测试")
            return False
        
        print_info(f"\n--- 测试获取 Token Key (ID: {self.test_token_id}) ---")
        try:
            success, data = self.client.get_token_key(self.test_token_id)
            if success:
                print_success("获取 Token Key 成功!")
                token_key = data.get('data', {}).get('key', '')
                print(f"  Token Key: {token_key[:20]}...")
                self.results.append(("test_get_token_key", True, "获取 Token Key 成功"))
                return True
            else:
                print_error(f"获取 Token Key 失败: {data.get('message', '未知错误')}")
                self.results.append(("test_get_token_key", False, data.get('message', '未知错误')}"))
                return False
        except Exception as e:
            print_error(f"获取 Token Key 异常: {str(e)}")
            self.results.append(("test_get_token_key", False, str(e)))
            return False

    def test_update_token(self) -> bool:
        """测试更新 Token"""
        if not self.test_token_id:
            print_warning("没有可用的 Token ID，跳过此测试")
            return False
        
        print_info(f"\n--- 测试更新 Token (ID: {self.test_token_id}) ---")
        try:
            new_name = f"updated_token_{generate_random_string(6)}"
            success, data = self.client.update_token(
                self.test_token_id,
                name=new_name
            )
            if success:
                print_success("更新 Token 成功!")
                print(f"  新名称: {new_name}")
                self.results.append(("test_update_token", True, "更新 Token 成功"))
                return True
            else:
                print_error(f"更新 Token 失败: {data.get('message', '未知错误')}")
                self.results.append(("test_update_token", False, data.get('message', '未知错误')}"))
                return False
        except Exception as e:
            print_error(f"更新 Token 异常: {str(e)}")
            self.results.append(("test_update_token", False, str(e)))
            return False

    def test_search_tokens(self) -> bool:
        """测试搜索 Token"""
        print_info("\n--- 测试搜索 Token ---")
        try:
            success, data = self.client.search_tokens(keyword="test")
            if success:
                print_success("搜索 Token 成功!")
                self.results.append(("test_search_tokens", True, "搜索 Token 成功"))
                return True
            else:
                print_warning(f"搜索 Token 失败: {data.get('message', '未知错误')}")
                self.results.append(("test_search_tokens", False, data.get('message', '未知错误')}"))
                return False
        except Exception as e:
            print_error(f"搜索 Token 异常: {str(e)}")
            self.results.append(("test_search_tokens", False, str(e)))
            return False

    def test_delete_token(self) -> bool:
        """测试删除 Token"""
        if not self.test_token_id:
            print_warning("没有可用的 Token ID，跳过此测试")
            return False
        
        print_info(f"\n--- 测试删除 Token (ID: {self.test_token_id}) ---")
        try:
            success, data = self.client.delete_token(self.test_token_id)
            if success:
                print_success("删除 Token 成功!")
                self.results.append(("test_delete_token", True, "删除 Token 成功"))
                # 清除记录，避免重复删除
                self.test_token_id = None
                return True
            else:
                print_error(f"删除 Token 失败: {data.get('message', '未知错误')}")
                self.results.append(("test_delete_token", False, data.get('message', '未知错误')}"))
                return False
        except Exception as e:
            print_error(f"删除 Token 异常: {str(e)}")
            self.results.append(("test_delete_token", False, str(e)))
            return False

    def test_multiple_token_operations(self) -> bool:
        """测试多个 Token 的操作（批量添加、查看、删除）"""
        print_info("\n--- 测试多个 Token 操作 ---")
        temp_ids = []
        
        try:
            # 创建多个 Token
            for i in range(3):
                name = f"multi_test_{i}_{generate_random_string(4)}"
                success, data = self.client.add_token(name=name)
                if success:
                    print_success(f"创建 Token 成功: {name}")
            
            # 获取所有 Token 并找到新创建的
            success, data = self.client.get_all_tokens()
            if success:
                tokens = data.get('data', {}).get('items', [])
                # 保存几个 Token ID 用于批量操作
                for token in tokens[:2]:
                    temp_ids.append(token.get('id'))
                
                if temp_ids:
                    # 测试批量获取 Token Keys
                    print_info("\n尝试批量获取 Token Keys...")
                    success_batch, data_batch = self.client.get_token_keys_batch(temp_ids)
                    if success_batch:
                        print_success("批量获取 Token Keys 成功!")
                    
                    # 测试批量删除
                    print_info("\n尝试批量删除 Token...")
                    success_delete, data_delete = self.client.delete_token_batch(temp_ids)
                    if success_delete:
                        print_success("批量删除 Token 成功!")
                        self.results.append(("test_multiple_token_operations", True, "多个 Token 操作成功"))
                        return True
            
            print_warning("批量操作部分完成或未完成")
            return False
            
        except Exception as e:
            print_error(f"多个 Token 操作异常: {str(e)}")
            self.results.append(("test_multiple_token_operations", False, str(e)))
            return False

    def test_create_multiple_token_types(self) -> bool:
        """测试创建不同类型的 Token"""
        print_info("\n--- 测试创建不同类型的 Token ---")
        try:
            # 创建有配额限制的 Token
            print_info("创建有配额限制的 Token...")
            success1, data1 = self.client.add_token(
                name="token_with_quota",
                unlimited_quota=False,
                remain_quota=1000000
            )
            
            # 创建有过期时间的 Token
            print_info("创建有过期时间的 Token...")
            import time
            future_time = int(time.time()) + 86400  # 24小时后
            success2, data2 = self.client.add_token(
                name="token_with_expiration",
                expired_time=future_time
            )
            
            if success1 and success2:
                print_success("创建多种类型 Token 成功!")
                self.results.append(("test_create_multiple_token_types", True, "创建多种类型 Token 成功"))
                return True
            else:
                print_warning("创建部分 Token 可能失败")
                return False
                
        except Exception as e:
            print_error(f"创建多种 Token 类型异常: {str(e)}")
            self.results.append(("test_create_multiple_token_types", False, str(e)))
            return False

    def run_all(self):
        """运行所有 Token 测试"""
        print_header("Token 管理功能测试")
        
        # 设置用户
        print_info("\n=== 步骤 1: 设置用户 ===")
        login_success = self.setup_user()
        time.sleep(0.5)
        
        if not login_success:
            print_error("用户登录失败，无法继续测试")
            # 尝试使用现有用户信息
            return False
        
        # 开始 Token 测试
        print_info("\n=== 步骤 2: Token 功能测试 ===")
        
        # 1. 添加新 Token
        self.test_add_token()
        time.sleep(0.5)
        
        # 2. 获取所有 Token
        tokens = self.test_get_all_tokens()
        time.sleep(0.5)
        
        if not tokens:
            print_warning("没有找到 Token，尝试添加一个...")
            self.test_add_token()
            time.sleep(0.5)
            tokens = self.test_get_all_tokens()
        
        if self.test_token_id:
            # 3. 获取单个 Token
            self.test_get_token()
            time.sleep(0.5)
            
            # 4. 获取 Token Key
            self.test_get_token_key()
            time.sleep(0.5)
            
            # 5. 更新 Token
            self.test_update_token()
            time.sleep(0.5)
            
            # 6. 搜索 Token
            self.test_search_tokens()
            time.sleep(0.5)
        
        # 7. 测试多种类型 Token 创建
        self.test_create_multiple_token_types()
        time.sleep(0.5)
        
        # 8. 测试批量操作
        self.test_multiple_token_operations()
        time.sleep(0.5)
        
        # 9. 清理 - 最后删除测试 Token（如果还存在）
        if self.test_token_id:
            self.test_delete_token()
        
        # 结果汇总
        print("\n" + "="*60)
        print("测试结果汇总:")
        print("="*60)
        
        total = len(self.results)
        passed = sum(1 for _, success, _ in self.results if success)
        failed = total - passed
        
        for name, success, message in self.results:
            status = f"{Color.GREEN}通过{Color.ENDC}" if success else f"{Color.RED}失败{Color.ENDC}"
            print(f"  {name}: {status} - {message}")
        
        print(f"\n总计: {total} 个测试")
        print(f"通过: {passed} 个")
        print(f"失败: {failed} 个")
        
        return passed == total


def main():
    import argparse

    parser = argparse.ArgumentParser(description="NewAPI Token 管理功能测试")
    parser.add_argument("--base-url", type=str, default="http://localhost:3000",
                        help="NewAPI 服务器地址")
    parser.add_argument("--username", type=str, default=None, help="测试用户名")
    parser.add_argument("--password", type=str, default=None, help="测试密码")
    
    args = parser.parse_args()

    client = NewAPIClient(base_url=args.base_url)
    tester = TokenTest(client, test_username=args.username, test_password=args.password)
    
    try:
        success = tester.run_all()
        if success:
            print_info("所有测试通过!")
            return 0
        else:
            print_error("部分测试失败!")
            return 1
    except KeyboardInterrupt:
        print_warning("测试被中断!")
        return 130


if __name__ == "__main__":
    sys.exit(main())
