#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NewAPI 基础功能测试
包括：获取系统状态、公开信息等
"""

import sys
import os
from api_client import NewAPIClient
from typing import Dict, Any
from pprint import pprint
import json
import time


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


class BasicTest:
    def __init__(self, client: NewAPIClient):
        self.client = client
        self.results = []

    def test_get_status(self) -> bool:
        """测试获取系统状态"""
        print_info("正在测试获取系统状态...")
        try:
            success, data = self.client.get_status()
            if success:
                print_success("获取系统状态成功!")
                print(f"  系统名称: {data.get('data', {}).get('system_name', 'N/A')}")
                print(f"  版本号: {data.get('data', {}).get('version', 'N/A')}")
                print(f"  启动时间: {data.get('data', {}).get('start_time', 'N/A')}")
                self.results.append(("test_get_status", True, "成功获取系统状态"))
                return True
            else:
                print_error(f"获取系统状态失败: {data.get('message', '未知错误')}")
                self.results.append(("test_get_status", False, data.get('message', '未知错误')}"))
                return False
        except Exception as e:
            print_error(f"获取系统状态异常: {str(e)}")
            self.results.append(("test_get_status", False, str(e)))
            return False

    def test_get_notice(self) -> bool:
        """测试获取公告"""
        print_info("正在测试获取公告...")
        try:
            success, data = self.client.get_notice()
            if success:
                print_success("获取公告成功!")
                notice_content = data.get('data', '')
                print(f"  公告长度: {len(notice_content) if notice_content else '无'")
                self.results.append(("test_get_notice", True, "成功获取公告"))
                return True
            else:
                print_warning(f"获取公告失败: {data.get('message', '未知错误')}")
                self.results.append(("test_get_notice", False, data.get('message', '未知错误')}"))
                return False
        except Exception as e:
            print_error(f"获取公告异常: {str(e)}")
            self.results.append(("test_get_notice", False, str(e)))
            return False

    def test_get_about(self) -> bool:
        """测试获取关于信息"""
        print_info("正在测试获取关于信息...")
        try:
            success, data = self.client.get_about()
            if success:
                print_success("获取关于信息成功!")
                self.results.append(("test_get_about", True, "成功获取关于信息"))
                return True
            else:
                print_warning(f"获取关于信息失败: {data.get('message', '未知错误')}")
                self.results.append(("test_get_about", False, data.get('message', '未知错误')}"))
                return False
        except Exception as e:
            print_error(f"获取关于信息异常: {str(e)}")
            self.results.append(("test_get_about", False, str(e)))
            return False

    def test_get_user_agreement(self) -> bool:
        """测试获取用户协议"""
        print_info("正在测试获取用户协议...")
        try:
            success, data = self.client.get_user_agreement()
            if success:
                print_success("获取用户协议成功!")
                self.results.append(("test_get_user_agreement", True, "成功获取用户协议"))
                return True
            else:
                print_warning(f"获取用户协议失败: {data.get('message', '未知错误')}")
                self.results.append(("test_get_user_agreement", False, data.get('message', '未知错误')}"))
                return False
        except Exception as e:
            print_error(f"获取用户协议异常: {str(e)}")
            self.results.append(("test_get_user_agreement", False, str(e)))
            return False

    def test_get_privacy_policy(self) -> bool:
        """测试获取隐私政策"""
        print_info("正在测试获取隐私政策...")
        try:
            success, data = self.client.get_privacy_policy()
            if success:
                print_success("获取隐私政策成功!")
                self.results.append(("test_get_privacy_policy", True, "成功获取隐私政策"))
                return True
            else:
                print_warning(f"获取隐私政策失败: {data.get('message', '未知错误')}")
                self.results.append(("test_get_privacy_policy", False, data.get('message', '未知错误')}"))
                return False
        except Exception as e:
            print_error(f"获取隐私政策异常: {str(e)}")
            self.results.append(("test_get_privacy_policy", False, str(e)))
            return False

    def test_get_home_page_content(self) -> bool:
        """测试获取首页内容"""
        print_info("正在测试获取首页内容...")
        try:
            success, data = self.client.get_home_page_content()
            if success:
                print_success("获取首页内容成功!")
                self.results.append(("test_get_home_page_content", True, "成功获取首页内容"))
                return True
            else:
                print_warning(f"获取首页内容失败: {data.get('message', '未知错误')}")
                self.results.append(("test_get_home_page_content", False, data.get('message', '未知错误')}"))
                return False
        except Exception as e:
            print_error(f"获取首页内容异常: {str(e)}")
            self.results.append(("test_get_home_page_content", False, str(e)))
            return False

    def test_get_pricing(self) -> bool:
        """测试获取价格信息"""
        print_info("正在测试获取价格信息...")
        try:
            success, data = self.client.get_pricing()
            if success:
                print_success("获取价格信息成功!")
                print(f"  价格数据: {data.get('data', {})}")
                self.results.append(("test_get_pricing", True, "成功获取价格信息"))
                return True
            else:
                print_warning(f"获取价格信息失败: {data.get('message', '未知错误')}")
                self.results.append(("test_get_pricing", False, data.get('message', '未知错误')}"))
                return False
        except Exception as e:
            print_error(f"获取价格信息异常: {str(e)}")
            self.results.append(("test_get_pricing", False, str(e)))
            return False

    def test_get_ratio_config(self) -> bool:
        """测试获取比例配置"""
        print_info("正在测试获取比例配置...")
        try:
            success, data = self.client.get_ratio_config()
            if success:
                print_success("获取比例配置成功!")
                self.results.append(("test_get_ratio_config", True, "成功获取比例配置"))
                return True
            else:
                print_warning(f"获取比例配置失败: {data.get('message', '未知错误')}")
                self.results.append(("test_get_ratio_config", False, data.get('message', '未知错误')}"))
                return False
        except Exception as e:
            print_error(f"获取比例配置异常: {str(e)}")
            self.results.append(("test_get_ratio_config", False, str(e)))
            return False

    def run_all(self):
        """运行所有基础测试"""
        print_header("基础功能测试")
        tests = [
            self.test_get_status,
            self.test_get_notice,
            self.test_get_about,
            self.test_get_user_agreement,
            self.test_get_privacy_policy,
            self.test_get_home_page_content,
            self.test_get_pricing,
            self.test_get_ratio_config,
        ]

        for test in tests:
            print_info(f"\n--- 运行测试: {test.__name__} ---")
            test()
            time.sleep(0.5)  # 防止请求过快

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

    parser = argparse.ArgumentParser(description="NewAPI 基础功能测试")
    parser.add_argument("--base-url", type=str, default="http://localhost:3000",
                        help="NewAPI 服务器地址")
    
    args = parser.parse_args()

    client = NewAPIClient(base_url=args.base_url)
    tester = BasicTest(client)
    
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
