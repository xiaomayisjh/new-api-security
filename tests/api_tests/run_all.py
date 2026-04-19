#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NewAPI 综合测试脚本
依次运行所有测试：基础功能、用户管理、Token 管理
"""

import sys
import os
import time

# 添加当前目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from api_client import NewAPIClient
from test_basic import BasicTest
from test_user import UserTest
from test_token import TokenTest


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
    print(f"\n{Color.BOLD}{'='*60}{Color.ENDC}")
    print(f"{Color.BOLD}{title}{Color.ENDC}")
    print(f"{Color.BOLD}{'='*60}{Color.ENDC}\n")


def run_test_section(test_name, test_func):
    """运行一个测试部分"""
    print_header(test_name)
    try:
        result = test_func()
        return result
    except Exception as e:
        print_error(f"{test_name} 执行异常: {str(e)}")
        return False


def main():
    import argparse
    parser = argparse.ArgumentParser(description="NewAPI 综合功能测试")
    parser.add_argument("--base-url", type=str, default="http://localhost:3000",
                        help="NewAPI 服务器地址")
    parser.add_argument("--username", type=str, default=None, help="测试用户名")
    parser.add_argument("--password", type=str, default=None, help="测试密码")
    parser.add_argument("--skip-basic", action="store_true", help="跳过基础测试")
    parser.add_argument("--skip-user", action="store_true", help="跳过用户测试")
    parser.add_argument("--skip-token", action="store_true", help="跳过Token测试")
    
    args = parser.parse_args()
    
    print_header("NewAPI 综合测试开始")
    print_info(f"服务器地址: {args.base_url}")
    
    client = NewAPIClient(base_url=args.base_url)
    
    all_results = {}
    total_passed = 0
    total_tests = 0
    
    # 1. 基础功能测试
    if not args.skip_basic:
        print_header("第 1 部分: 基础功能测试")
        basic_tester = BasicTest(client)
        basic_result = basic_tester.run_all()
        all_results['basic'] = {
            'success': basic_result,
            'details': basic_tester.results
        }
        total_tests += len(basic_tester.results)
        total_passed += sum(1 for _, s, _ in basic_tester.results if s)
        time.sleep(1)
    else:
        print_warning("跳过基础功能测试")
    
    # 2. 用户管理测试
    if not args.skip_user:
        print_header("第 2 部分: 用户管理测试")
        user_tester = UserTest(client, test_username=args.username, test_password=args.password)
        user_result = user_tester.run_all()
        all_results['user'] = {
            'success': user_result,
            'details': user_tester.results
        }
        total_tests += len(user_tester.results)
        total_passed += sum(1 for _, s, _ in user_tester.results if s)
        time.sleep(1)
    else:
        print_warning("跳过用户管理测试")
    
    # 3. Token管理测试
    if not args.skip_token:
        print_header("第 3 部分: Token 管理测试")
        token_tester = TokenTest(client, test_username=args.username, test_password=args.password)
        token_result = token_tester.run_all()
        all_results['token'] = {
            'success': token_result,
            'details': token_tester.results
        }
        total_tests += len(token_tester.results)
        total_passed += sum(1 for _, s, _ in token_tester.results if s)
    else:
        print_warning("跳过Token管理测试")
    
    # 总结报告
    print_header("测试总结")
    
    print_info("各部分测试结果:")
    for section, result in all_results.items():
        section_name = {
            'basic': '基础功能',
            'user': '用户管理',
            'token': 'Token管理'
        }.get(section, section)
        
        status = f"{Color.GREEN}通过{Color.ENDC}" if result['success'] else f"{Color.RED}失败{Color.ENDC}"
        print(f"  {section_name}: {status}")
    
    print(f"\n总体统计:")
    print(f"  总测试数: {total_tests}")
    print(f"  通过: {Color.GREEN}{total_passed}{Color.ENDC}")
    print(f"  失败: {Color.RED}{total_tests - total_passed}{Color.ENDC}")
    
    if total_tests > 0:
        pass_rate = (total_passed / total_tests) * 100
        print(f"  通过率: {pass_rate:.2f}%")
    
    # 总体结果
    overall_success = total_tests > 0 and total_passed == total_tests
    if overall_success:
        print_success("\n🎉 所有测试通过!")
        return 0
    else:
        print_warning("\n⚠️  部分测试失败，请检查上述结果")
        return 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print_warning("\n测试被用户中断")
        sys.exit(130)
