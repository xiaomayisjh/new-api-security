#!/usr/bin/env python3
import requests#!/usr/bin/env python3
import requests
import json
import time
import hashlib
import hmac

# 配置
BASE_URL = "https://timyai.com"#!/usr/bin/env python3
import requests
import json
import time
import hashlib
import hmac

# 配置
BASE_URL = "https://timyai.com"
USERNAME = "antplayer"
PASSWORD = "sj@101709"

# Webhook测试配置
TEST_W#!/usr/bin/env python3
import requests
import json
import time
import hashlib
import hmac

# 配置
BASE_URL = "https://timyai.com"
USERNAME = "antplayer"
PASSWORD = "sj@101709"

# Webhook测试配置
TEST_WEBHOOKS = {
    "stripe": "/api/stripe/webhook",
    "creem": "/api/creem#!/usr/bin/env python3
import requests
import json
import time
import hashlib
import hmac

# 配置
BASE_URL = "https://timyai.com"
USERNAME = "antplayer"
PASSWORD = "sj@101709"

# Webhook测试配置
TEST_WEBHOOKS = {
    "stripe": "/api/stripe/webhook",
    "creem": "/api/creem/webhook",
    "waffo": "/api/waffo/webhook",
    "epay_user": "/api/user/ep#!/usr/bin/env python3
import requests
import json
import time
import hashlib
import hmac

# 配置
BASE_URL = "https://timyai.com"
USERNAME = "antplayer"
PASSWORD = "sj@101709"

# Webhook测试配置
TEST_WEBHOOKS = {
    "stripe": "/api/stripe/webhook",
    "creem": "/api/creem/webhook",
    "waffo": "/api/waffo/webhook",
    "epay_user": "/api/user/epay/notify",
    "epay_subscription": "/api/subscription/epay/notify",
}

def print_header(title):#!/usr/bin/env python3
import requests
import json
import time
import hashlib
import hmac

# 配置
BASE_URL = "https://timyai.com"
USERNAME = "antplayer"
PASSWORD = "sj@101709"

# Webhook测试配置
TEST_WEBHOOKS = {
    "stripe": "/api/stripe/webhook",
    "creem": "/api/creem/webhook",
    "waffo": "/api/waffo/webhook",
    "epay_user": "/api/user/epay/notify",
    "epay_subscription": "/api/subscription/epay/notify",
}

def print_header(title):
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*6#!/usr/bin/env python3
import requests
import json
import time
import hashlib
import hmac

# 配置
BASE_URL = "https://timyai.com"
USERNAME = "antplayer"
PASSWORD = "sj@101709"

# Webhook测试配置
TEST_WEBHOOKS = {
    "stripe": "/api/stripe/webhook",
    "creem": "/api/creem/webhook",
    "waffo": "/api/waffo/webhook",
    "epay_user": "/api/user/epay/notify",
    "epay_subscription": "/api/subscription/epay/notify",
}

def print_header(title):
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60)

def test_login():
    print_header("登录测试")
    
    # 尝试不同的登录端点
    login_endpoints =#!/usr/bin/env python3
import requests
import json
import time
import hashlib
import hmac

# 配置
BASE_URL = "https://timyai.com"
USERNAME = "antplayer"
PASSWORD = "sj@101709"

# Webhook测试配置
TEST_WEBHOOKS = {
    "stripe": "/api/stripe/webhook",
    "creem": "/api/creem/webhook",
    "waffo": "/api/waffo/webhook",
    "epay_user": "/api/user/epay/notify",
    "epay_subscription": "/api/subscription/epay/notify",
}

def print_header(title):
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60)

def test_login():
    print_header("登录测试")
    
    # 尝试不同的登录端点
    login_endpoints = [
        "/api/user/login",
        "/api/login",
        "/login"
    ]
    
    for endpoint in login_endpoints