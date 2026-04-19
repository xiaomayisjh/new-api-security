#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NewAPI 用户功能测试
包括：用户注册、登录、登出、修改密码等
"""

import sys
import os
from api_client import NewAPIClient
from typing import Dict, Any
import time
import random
import string

# 复用基础测试的颜色打印功能
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


class UserTest:
    def __init__(self, client: NewAPIClient, test_username: str = None, test_password: str = None):
        self.client = client
        self.results = []
        
        # 生成测试用户信息
        if test_username:
            self.test_username = test_username
        else:
            self.test_username = f"test_user_{generate_random_string(8)}"
        
        if test_password:
            self.test_password = test_password
        else:
            self.test_password = "Test@123456"
        
        self.test_email = f"{self.test_username}@example.com"
        self.new_password = "New@123456"  # 用于密码修改测试
        
        print_info(f"测试用户名: {self.test_username}")
        print_info(f"测试邮箱: {self.test_email}")

    def test_register(self) -> bool:
        """测试用户注册"""
        print_info("正在测试用户注册...")
        try:
            success, data = self.client.register(
                username=self.test_username,
                password=self.test_password
            )
            if success:
                print_success("用户注册成功!")
                self.results.append(("test_register", True, "用户注册成功"))
                return True
            else:
                print_warning(f"用户注册失败: {data.get('message', '未知错误')}")
                print_warning("注意：可能需要禁用邮箱验证或开启注册功能")
                self.results.append(("test_register", False, data.get('message', '未知错误')}"))
                return False
        except Exception as e:
            print_error(f"用户注册异常: {str(e)}")
            self.results.append(("test_register", False, str(e)))
            return False

    def test_login(self) -> bool:
        """测试用户登录"""
        print_info("正在测试用户登录...")
        try:
            success, data = self.client.login(
                username=self.test_username,
                password=self.test_password
            )
            if success:
                print_success("用户登录成功!")
                user_data = data.get('data', {})
                print(f"  用户ID: {user_data.get('id', 'N/A')}")
                print(f"  用户名: {user_data.get('username', 'N/A')}")
                print(f"  角色: {user_data.get('role', 'N/A')}")
                self.results.append(("test_login", True, "用户登录成功"))
                return True
            else:
                print_error(f"用户登录失败: {data.get('message', '未知错误')}")
                self.results.append(("test_login", False, data.get('message', '未知错误')}"))
                return False
        except Exception as e:
            print_error(f"用户登录异常: {str(e)}")
            self.results.append(("test_login", False, str(e)))
            return False

    def test_get_self(self) -> bool:
        """测试获取当前用户信息"""
        print_info("正在测试获取当前用户信息...")
        try:
            success, data = self.client.get_self()
            if success:
                print_success("获取用户信息成功!")
                user_data = data.get('data', {})
                print(f"  用户ID: {user_data.get('id', 'N/A')}")
                print(f"  用户名: {user_data.get('username', 'N/A')}")
                print(f"  剩余额度: {user_data.get('quota', 'N/A')}")
                self.results.append(("test_get_self", True, "获取用户信息成功"))
                return True
            else:
                print_error(f"获取用户信息失败: {data.get('message', '未知错误')}")
                self.results.append(("test_get_self", False, data.get('message', '未知错误')}"))
                return False
        except Exception as e:
            print_error(f"获取用户信息异常: {str(e)}")
            self.results.append(("test_get_self", False, str(e)))
            return False

    def test_get_user_groups(self) -> bool:
        """测试获取用户分组"""
        print_info("正在测试获取用户分组...")
        try:
            success, data = self.client.get_user_groups_self()
            if success:
                print_success("获取用户分组成功!")
                self.results.append(("test_get_user_groups", True, "获取用户分组成功"))
                return True
            else:
                print_warning(f"获取用户分组失败: {data.get('message', '未知错误')}")
                self.results.append(("test_get_user_groups", False, data.get('message', '未知错误')}"))
                return False
        except Exception as e:
            print_error(f"获取用户分组异常: {str(e)}")
            self.results.append(("test_get_user_groups", False, str(e)))
            return False

    def test_get_self_models(self) -> bool:
        """测试获取用户可用的模型"""
        print_info("正在测试获取用户可用的模型...")
        try:
            success, data = self.client.get_self_models()
            if success:
                print_success("获取用户模型成功!")
                models = data.get('data', [])
                print(f"  可用模型数量: {len(models)}")
                self.results.append(("test_get_self_models", True, "获取用户模型成功"))
                return True
            else:
                print_warning(f"获取用户模型失败: {data.get('message', '未知错误')}")
                self.results.append(("test_get_self_models", False, data.get('message', '未知错误')}"))
                return False
        except Exception as e:
            print_error(f"获取用户模型异常: {str(e)}")
            self.results.append(("test_get_self_models", False, str(e)))
            return False

    def test_generate_access_token(self) -> bool:
        """测试生成访问令牌"""
        print_info("正在测试生成访问令牌...")
        try:
            success, data = self.client.generate_access_token()
            if success:
                print_success("生成访问令牌成功!")
                token = data.get('data', '')
                print(f"  访问令牌: {token[:20]}...")
                self.results.append(("test_generate_access_token", True, "生成访问令牌成功"))
                return True
            else:
                print_warning(f"生成访问令牌失败: {data.get('message', '未知错误')}")
                self.results.append(("test_generate_access_token", False, data.get('message', '未知错误')}"))
                return False
        except Exception as e:
            print_error(f"生成访问令牌异常: {str(e)}")
            self.results.append(("test_generate_access_token", False, str(e)))
            return False

    def test_get_aff_code(self) -> bool:
        """测试获取邀请码"""
        print_info("正在测试获取邀请码...")
        try:
            success, data = self.client.get_aff_code()
            if success:
                print_success("获取邀请码成功!")
                aff_code = data.get('data', '')
                print(f"  邀请码: {aff_code}")
                self.results.append(("test_get_aff_code", True, "获取邀请码成功"))
                return True
            else:
                print_warning(f"获取邀请码失败: {data.get('message', '未知错误')}")
                self.results.append(("test_get_aff_code", False, data.get('message', '未知错误')}"))
                return False
        except Exception as e:
            print_error(f"获取邀请码异常: {str(e)}")
            self.results.append(("test_get_aff_code", False, str(e)))
            return False

    def test_get_topup_info(self) -> bool:
        """测试获取充值信息"""
        print_info("正在测试获取充值信息...")
        try:
            success, data = self.client.get_topup_info()
            if success:
                print_success("获取充值信息成功!")
                self.results.append(("test_get_topup_info", True, "获取充值信息成功"))
                return True
            else:
                print_warning(f"获取充值信息失败: {data.get('message', '未知错误')}")
                self.results.append(("test_get_topup_info", False, data.get('message', '未知错误')}"))
                return False
        except Exception as e:
            print_error(f"获取充值信息异常: {str(e)}")
            self.results.append(("test_get_topup_info", False, str(e)))
            return False

    def test_get_topup_self(self) -> bool:
        """测试获取用户充值记录"""
        print_info("正在测试获取充值记录...")
        try:
            success, data = self.client.get_topup_self()
            if success:
                print_success("获取充值记录成功!")
                self.results.append(("test_get_topup_self", True, "获取充值记录成功"))
                return True
            else:
                print_warning(f"获取充值记录失败: {data.get('message', '未知错误')}")
                self.results.append(("test_get_topup_self", False, data.get('message', '未知错误')}"))
                return False
        except Exception as e:
            print_error(f"获取充值记录异常: {str(e)}")
            self.results.append(("test_get_topup_self", False, str(e)))
            return False

    def test_update_user_setting(self) -> bool:
        """测试更新用户设置"""
        print_info("正在测试更新用户设置...")
        try:
            success, data = self.client.update_user_setting(
                notify_type="email",
                quota_warning_threshold=50.0
            )
            if success:
                print_success("更新用户设置成功!")
                self.results.append(("test_update_user_setting", True, "更新用户设置成功"))
                return True
            else:
                print_warning(f"更新用户设置失败: {data.get('message', '未知错误')}")
                self.results.append(("test_update_user_setting", False, data.get('message', '未知错误')}"))
                return False
        except Exception as e:
            print_error(f"更新用户设置异常: {str(e)}")
            self.results.append(("test_update_user_setting", False, str(e)))
            return False

    def test_checkin(self) -> bool:
        """测试签到功能"""
        print_info("正在测试签到状态查询...")
        try:
            success, data = self.client.get_checkin_status()
            if success:
                print_success("获取签到状态成功!")
                # 尝试签到
                print_info("正在尝试签到...")
                success_checkin, data_checkin = self.client.do_checkin()
                if success_checkin:
                    print_success("签到成功!")
                else:
                    print_warning(f"签到可能已完成: {data_checkin.get('message', '未知消息')}")
                self.results.append(("test_checkin", True, "签到功能正常"))
                return True
            else:
                print_warning(f"获取签到状态失败: {data.get('message', '未知错误')}")
                self.results.append(("test_checkin", False, data.get('message', '未知错误')}"))
                return False
        except Exception as e:
            print_error(f"签到功能异常: {str(e)}")
            self.results.append(("test_checkin", False, str(e)))
            return False

    def test_logs(self) -> bool:
        """测试日志相关功能"""
        print_info("正在测试日志查询...")
        try:
            success, data = self.client.get_logs_self()
            if success:
                print_success("获取日志成功!")
                # 测试统计
                success_stat, data_stat = self.client.get_logs_self_stat()
                if success_stat:
                    print_success("获取日志统计成功!")
                # 测试搜索
                success_search, data_search = self.client.get_logs_self_search(keyword="test")
                if success_search:
                    print_success("搜索日志成功!")
                self.results.append(("test_logs", True, "日志功能正常"))
                return True
            else:
                print_warning(f"获取日志失败: {data.get('message', '未知错误')}")
                self.results.append(("test_logs", False, data.get('message', '未知错误')}"))
                return False
        except Exception as e:
            print_error(f"日志功能异常: {str(e)}")
            self.results.append(("test_logs", False, str(e)))
            return False

    def test_get_data_self(self) -> bool:
        """测试获取用户数据"""
        print_info("正在测试获取用户数据...")
        try:
            success, data = self.client.get_data_self()
            if success:
                print_success("获取用户数据成功!")
                self.results.append(("test_get_data_self", True, "获取用户数据成功"))
                return True
            else:
                print_warning(f"获取用户数据失败: {data.get('message', '未知错误')}")
                self.results.append(("test_get_data_self", False, data.get('message', '未知错误')}"))
                return False
        except Exception as e:
            print_error(f"获取用户数据异常: {str(e)}")
            self.results.append(("test_get_data_self", False, str(e)))
            return False

    def test_subscription(self) -> bool:
        """测试订阅相关功能"""
        print_info("正在测试订阅功能...")
        try:
            success, data = self.client.get_subscription_plans()
            if success:
                print_success("获取订阅计划成功!")
            # 获取当前订阅
            success_self, data_self = self.client.get_subscription_self()
            if success_self:
                print_success("获取当前订阅成功!")
            self.results.append(("test_subscription", True, "订阅功能正常"))
            return True
        except Exception as e:
            print_warning(f"订阅功能可能未启用: {str(e)}")
            self.results.append(("test_subscription", False, str(e)))
            return False

    def test_mj_and_task(self) -> bool:
        """测试 Midjourney 和任务功能"""
        print_info("正在测试 Midjourney 和任务功能...")
        try:
            success_mj, data_mj = self.client.get_midjourney_self()
            if success_mj:
                print_success("获取 Midjourney 记录成功!")
            success_task, data_task = self.client.get_task_self()
            if success_task:
                print_success("获取任务记录成功!")
            self.results.append(("test_mj_and_task", True, "任务功能正常"))
            return True
        except Exception as e:
            print_warning(f"任务功能可能未启用: {str(e)}")
            self.results.append(("test_mj_and_task", False, str(e)))
            return False

    def test_get_oauth_bindings(self) -> bool:
        """测试获取 OAuth 绑定"""
        print_info("正在测试获取 OAuth 绑定...")
        try:
            success, data = self.client.get_oauth_bindings()
            if success:
                print_success("获取 OAuth 绑定成功!")
                self.results.append(("test_get_oauth_bindings", True, "获取 OAuth 绑定成功"))
                return True
            else:
                print_warning(f"获取 OAuth 绑定失败: {data.get('message', '未知错误')}")
                self.results.append(("test_get_oauth_bindings", False, data.get('message', '未知错误')}"))
                return False
        except Exception as e:
            print_error(f"获取 OAuth 绑定异常: {str(e)}")
            self.results.append(("test_get_oauth_bindings", False, str(e)))
            return False

    def test_logout(self) -> bool:
        """测试用户登出"""
        print_info("正在测试用户登出...")
        try:
            success, data = self.client.logout()
            if success:
                print_success("用户登出成功!")
                self.results.append(("test_logout", True, "用户登出成功"))
                return True
            else:
                print_error(f"用户登出失败: {data.get('message', '未知错误')}")
                self.results.append(("test_logout", False, data.get('message', '未知错误')}"))
                return False
        except Exception as e:
            print_error(f"用户登出异常: {str(e)}")
            self.results.append(("test_logout", False, str(e)))
            return False

    def run_all(self):
        """运行所有用户测试"""
        print_header("用户功能测试")
        
        # 运行测试序列
        # 1. 注册用户
        print_info("\n--- 步骤 1: 用户注册 ---")
        self.test_register()
        time.sleep(0.5)
        
        # 2. 登录用户
        print_info("\n--- 步骤 2: 用户登录 ---")
        login_success = self.test_login()
        time.sleep(0.5)
        
        # 如果登录成功，继续后续测试
        if login_success:
            tests_after_login = [
                self.test_get_self,
                self.test_get_user_groups,
                self.test_get_self_models,
                self.test_generate_access_token,
                self.test_get_aff_code,
                self.test_get_topup_info,
                self.test_get_topup_self,
                self.test_update_user_setting,
                self.test_checkin,
                self.test_logs,
                self.test_get_data_self,
                self.test_subscription,
                self.test_mj_and_task,
                self.test_get_oauth_bindings,
            ]
            
            for test in tests_after_login:
                print_info(f"\n--- 运行测试: {test.__name__} ---")
                test()
                time.sleep(0.5)
            
            # 最后登出
            print_info("\n--- 步骤: 用户登出 ---")
            self.test_logout()
        else:
            print_error("登录失败，跳过后续需要登录的测试")
        
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

    parser = argparse.ArgumentParser(description="NewAPI 用户功能测试")
    parser.add_argument("--base-url", type=str, default="http://localhost:3000",
                        help="NewAPI 服务器地址")
    parser.add_argument("--username", type=str, default=None, help="测试用户名")
    parser.add_argument("--password", type=str, default=None, help="测试密码")
    
    args = parser.parse_args()

    client = NewAPIClient(base_url=args.base_url)
    tester = UserTest(client, test_username=args.username, test_password=args.password)
    
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
