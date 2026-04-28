#!/usr/bin/env python3
"""
Registration Script for Security Testing
Target: card.tiantianyy.com
"""

import requests
import json
import random
import string
import time

BASE_URL = "https://card.tiantianyy.com/api"

def generate_random_username(length=10):
    return "test_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def generate_random_device_id():
    return ''.join(random.choices(string.hexdigits.lower(), k=32))

def register_user(username, password, invite_code="", device_id=None):
    if device_id is None:
        device_id = generate_random_device_id()
    
    url = f"{BASE_URL}/user.php?action=register"
    payload = {
        "username": username,
        "password": password,
        "invite_code": invite_code,
        "device_id": device_id
    }
    
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        return response.json()
    except Exception as e:
        return {"success": False, "error": str(e)}

def login_user(username, password):
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
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        return response.json()
    except Exception as e:
        return {"success": False, "error": str(e)}

def get_user_info(token):
    url = f"{BASE_URL}/user.php?action=getInfo"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
    
    try:
        response = requests.post(url, json={}, headers=headers, timeout=10)
        return response.json()
    except Exception as e:
        return {"success": False, "error": str(e)}

def main():
    print("=" * 60)
    print("Registration and Login Test Script")
    print("Target: card.tiantianyy.com")
    print("=" * 60)
    
    username = generate_random_username()
    password = "Test@123456"
    
    print(f"\n[*] Attempting to register user: {username}")
    result = register_user(username, password)
    print(f"[+] Registration result: {json.dumps(result, indent=2, ensure_ascii=False)}")
    
    if result.get("success"):
        token = result.get("data", {}).get("token")
        user = result.get("data", {}).get("user", {})
        
        print(f"\n[*] Registration successful!")
        print(f"    - User ID: {user.get('id')}")
        print(f"    - Username: {user.get('username')}")
        print(f"    - Invite Code: {user.get('invite_code')}")
        print(f"    - Token: {token[:50]}...")
        
        print(f"\n[*] Testing login with registered credentials...")
        login_result = login_user(username, password)
        print(f"[+] Login result: {json.dumps(login_result, indent=2, ensure_ascii=False)}")
        
        print(f"\n[*] Testing get user info with token...")
        info_result = get_user_info(token)
        print(f"[+] User info: {json.dumps(info_result, indent=2, ensure_ascii=False)}")
    else:
        print(f"[-] Registration failed: {result.get('message')}")

if __name__ == "__main__":
    main()
