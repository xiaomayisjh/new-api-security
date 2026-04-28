from playwrightfrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://cardfrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

deffrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
from playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url":from playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headersfrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
from playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
from playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
from playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.postfrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
from playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers":from playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
from playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body elsefrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["bodyfrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_infofrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lowerfrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
from playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status}from playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["bodyfrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {respfrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with syncfrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context =from playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_pagefrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_requestfrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
from playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigatingfrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGETfrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=from playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*]from playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/from playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepagefrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\from playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = pagefrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_sfrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_screenshots/page_content.html", "w") asfrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_screenshots/page_content.html", "w") as f:
        f.write(content)
    
    printfrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_screenshots/page_content.html", "w") as f:
        f.write(content)
    
    print("\n[*] Looking for links and navigation...")
from playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_screenshots/page_content.html", "w") as f:
        f.write(content)
    
    print("\n[*] Looking for links and navigation...")
    links = page.locator("a").allfrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_screenshots/page_content.html", "w") as f:
        f.write(content)
    
    print("\n[*] Looking for links and navigation...")
    links = page.locator("a").all()
    for link in links:
        try:
from playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_screenshots/page_content.html", "w") as f:
        f.write(content)
    
    print("\n[*] Looking for links and navigation...")
    links = page.locator("a").all()
    for link in links:
        try:
            href = link.get_attribute("href")
            text = link.inner_text()
            print(f"from playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_screenshots/page_content.html", "w") as f:
        f.write(content)
    
    print("\n[*] Looking for links and navigation...")
    links = page.locator("a").all()
    for link in links:
        try:
            href = link.get_attribute("href")
            text = link.inner_text()
            print(f"  Link: {text} -> {href}")
from playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_screenshots/page_content.html", "w") as f:
        f.write(content)
    
    print("\n[*] Looking for links and navigation...")
    links = page.locator("a").all()
    for link in links:
        try:
            href = link.get_attribute("href")
            text = link.inner_text()
            print(f"  Link: {text} -> {href}")
        except:
            pass
    
    print("\nfrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_screenshots/page_content.html", "w") as f:
        f.write(content)
    
    print("\n[*] Looking for links and navigation...")
    links = page.locator("a").all()
    for link in links:
        try:
            href = link.get_attribute("href")
            text = link.inner_text()
            print(f"  Link: {text} -> {href}")
        except:
            pass
    
    print("\n[*] Looking for forms...")
    forms = pagefrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_screenshots/page_content.html", "w") as f:
        f.write(content)
    
    print("\n[*] Looking for links and navigation...")
    links = page.locator("a").all()
    for link in links:
        try:
            href = link.get_attribute("href")
            text = link.inner_text()
            print(f"  Link: {text} -> {href}")
        except:
            pass
    
    print("\n[*] Looking for forms...")
    forms = page.locator("form").all()
    print(ffrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_screenshots/page_content.html", "w") as f:
        f.write(content)
    
    print("\n[*] Looking for links and navigation...")
    links = page.locator("a").all()
    for link in links:
        try:
            href = link.get_attribute("href")
            text = link.inner_text()
            print(f"  Link: {text} -> {href}")
        except:
            pass
    
    print("\n[*] Looking for forms...")
    forms = page.locator("form").all()
    print(f"  Found {len(forms)} forms")
    
    print("\n[*] Looking for input fieldsfrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_screenshots/page_content.html", "w") as f:
        f.write(content)
    
    print("\n[*] Looking for links and navigation...")
    links = page.locator("a").all()
    for link in links:
        try:
            href = link.get_attribute("href")
            text = link.inner_text()
            print(f"  Link: {text} -> {href}")
        except:
            pass
    
    print("\n[*] Looking for forms...")
    forms = page.locator("form").all()
    print(f"  Found {len(forms)} forms")
    
    print("\n[*] Looking for input fields...")
    inputs = page.locator("input").from playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_screenshots/page_content.html", "w") as f:
        f.write(content)
    
    print("\n[*] Looking for links and navigation...")
    links = page.locator("a").all()
    for link in links:
        try:
            href = link.get_attribute("href")
            text = link.inner_text()
            print(f"  Link: {text} -> {href}")
        except:
            pass
    
    print("\n[*] Looking for forms...")
    forms = page.locator("form").all()
    print(f"  Found {len(forms)} forms")
    
    print("\n[*] Looking for input fields...")
    inputs = page.locator("input").all()
    for inp in inputs:
        tryfrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_screenshots/page_content.html", "w") as f:
        f.write(content)
    
    print("\n[*] Looking for links and navigation...")
    links = page.locator("a").all()
    for link in links:
        try:
            href = link.get_attribute("href")
            text = link.inner_text()
            print(f"  Link: {text} -> {href}")
        except:
            pass
    
    print("\n[*] Looking for forms...")
    forms = page.locator("form").all()
    print(f"  Found {len(forms)} forms")
    
    print("\n[*] Looking for input fields...")
    inputs = page.locator("input").all()
    for inp in inputs:
        try:
            inp_type = inp.get_attribute("type")
            inp_name = inp.get_attribute("namefrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_screenshots/page_content.html", "w") as f:
        f.write(content)
    
    print("\n[*] Looking for links and navigation...")
    links = page.locator("a").all()
    for link in links:
        try:
            href = link.get_attribute("href")
            text = link.inner_text()
            print(f"  Link: {text} -> {href}")
        except:
            pass
    
    print("\n[*] Looking for forms...")
    forms = page.locator("form").all()
    print(f"  Found {len(forms)} forms")
    
    print("\n[*] Looking for input fields...")
    inputs = page.locator("input").all()
    for inp in inputs:
        try:
            inp_type = inp.get_attribute("type")
            inp_name = inp.get_attribute("name")
            inp_id = inp.get_attribute("idfrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_screenshots/page_content.html", "w") as f:
        f.write(content)
    
    print("\n[*] Looking for links and navigation...")
    links = page.locator("a").all()
    for link in links:
        try:
            href = link.get_attribute("href")
            text = link.inner_text()
            print(f"  Link: {text} -> {href}")
        except:
            pass
    
    print("\n[*] Looking for forms...")
    forms = page.locator("form").all()
    print(f"  Found {len(forms)} forms")
    
    print("\n[*] Looking for input fields...")
    inputs = page.locator("input").all()
    for inp in inputs:
        try:
            inp_type = inp.get_attribute("type")
            inp_name = inp.get_attribute("name")
            inp_id = inp.get_attribute("id")
            inp_placeholder = inp.get_attribute("placeholderfrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_screenshots/page_content.html", "w") as f:
        f.write(content)
    
    print("\n[*] Looking for links and navigation...")
    links = page.locator("a").all()
    for link in links:
        try:
            href = link.get_attribute("href")
            text = link.inner_text()
            print(f"  Link: {text} -> {href}")
        except:
            pass
    
    print("\n[*] Looking for forms...")
    forms = page.locator("form").all()
    print(f"  Found {len(forms)} forms")
    
    print("\n[*] Looking for input fields...")
    inputs = page.locator("input").all()
    for inp in inputs:
        try:
            inp_type = inp.get_attribute("type")
            inp_name = inp.get_attribute("name")
            inp_id = inp.get_attribute("id")
            inp_placeholder = inp.get_attribute("placeholder")
            print(f"  Input: type={from playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_screenshots/page_content.html", "w") as f:
        f.write(content)
    
    print("\n[*] Looking for links and navigation...")
    links = page.locator("a").all()
    for link in links:
        try:
            href = link.get_attribute("href")
            text = link.inner_text()
            print(f"  Link: {text} -> {href}")
        except:
            pass
    
    print("\n[*] Looking for forms...")
    forms = page.locator("form").all()
    print(f"  Found {len(forms)} forms")
    
    print("\n[*] Looking for input fields...")
    inputs = page.locator("input").all()
    for inp in inputs:
        try:
            inp_type = inp.get_attribute("type")
            inp_name = inp.get_attribute("name")
            inp_id = inp.get_attribute("id")
            inp_placeholder = inp.get_attribute("placeholder")
            print(f"  Input: type={inp_type}, name={inp_name}, id={from playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_screenshots/page_content.html", "w") as f:
        f.write(content)
    
    print("\n[*] Looking for links and navigation...")
    links = page.locator("a").all()
    for link in links:
        try:
            href = link.get_attribute("href")
            text = link.inner_text()
            print(f"  Link: {text} -> {href}")
        except:
            pass
    
    print("\n[*] Looking for forms...")
    forms = page.locator("form").all()
    print(f"  Found {len(forms)} forms")
    
    print("\n[*] Looking for input fields...")
    inputs = page.locator("input").all()
    for inp in inputs:
        try:
            inp_type = inp.get_attribute("type")
            inp_name = inp.get_attribute("name")
            inp_id = inp.get_attribute("id")
            inp_placeholder = inp.get_attribute("placeholder")
            print(f"  Input: type={inp_type}, name={inp_name}, id={inp_id}, placeholder={inp_placeholder}")
        exceptfrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_screenshots/page_content.html", "w") as f:
        f.write(content)
    
    print("\n[*] Looking for links and navigation...")
    links = page.locator("a").all()
    for link in links:
        try:
            href = link.get_attribute("href")
            text = link.inner_text()
            print(f"  Link: {text} -> {href}")
        except:
            pass
    
    print("\n[*] Looking for forms...")
    forms = page.locator("form").all()
    print(f"  Found {len(forms)} forms")
    
    print("\n[*] Looking for input fields...")
    inputs = page.locator("input").all()
    for inp in inputs:
        try:
            inp_type = inp.get_attribute("type")
            inp_name = inp.get_attribute("name")
            inp_id = inp.get_attribute("id")
            inp_placeholder = inp.get_attribute("placeholder")
            print(f"  Input: type={inp_type}, name={inp_name}, id={inp_id}, placeholder={inp_placeholder}")
        except:
            pass
    
    print("\n[*]from playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_screenshots/page_content.html", "w") as f:
        f.write(content)
    
    print("\n[*] Looking for links and navigation...")
    links = page.locator("a").all()
    for link in links:
        try:
            href = link.get_attribute("href")
            text = link.inner_text()
            print(f"  Link: {text} -> {href}")
        except:
            pass
    
    print("\n[*] Looking for forms...")
    forms = page.locator("form").all()
    print(f"  Found {len(forms)} forms")
    
    print("\n[*] Looking for input fields...")
    inputs = page.locator("input").all()
    for inp in inputs:
        try:
            inp_type = inp.get_attribute("type")
            inp_name = inp.get_attribute("name")
            inp_id = inp.get_attribute("id")
            inp_placeholder = inp.get_attribute("placeholder")
            print(f"  Input: type={inp_type}, name={inp_name}, id={inp_id}, placeholder={inp_placeholder}")
        except:
            pass
    
    print("\n[*] Looking for buttons...")
    buttons = page.locatorfrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_screenshots/page_content.html", "w") as f:
        f.write(content)
    
    print("\n[*] Looking for links and navigation...")
    links = page.locator("a").all()
    for link in links:
        try:
            href = link.get_attribute("href")
            text = link.inner_text()
            print(f"  Link: {text} -> {href}")
        except:
            pass
    
    print("\n[*] Looking for forms...")
    forms = page.locator("form").all()
    print(f"  Found {len(forms)} forms")
    
    print("\n[*] Looking for input fields...")
    inputs = page.locator("input").all()
    for inp in inputs:
        try:
            inp_type = inp.get_attribute("type")
            inp_name = inp.get_attribute("name")
            inp_id = inp.get_attribute("id")
            inp_placeholder = inp.get_attribute("placeholder")
            print(f"  Input: type={inp_type}, name={inp_name}, id={inp_id}, placeholder={inp_placeholder}")
        except:
            pass
    
    print("\n[*] Looking for buttons...")
    buttons = page.locator("button").all()
    for btn in buttonsfrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_screenshots/page_content.html", "w") as f:
        f.write(content)
    
    print("\n[*] Looking for links and navigation...")
    links = page.locator("a").all()
    for link in links:
        try:
            href = link.get_attribute("href")
            text = link.inner_text()
            print(f"  Link: {text} -> {href}")
        except:
            pass
    
    print("\n[*] Looking for forms...")
    forms = page.locator("form").all()
    print(f"  Found {len(forms)} forms")
    
    print("\n[*] Looking for input fields...")
    inputs = page.locator("input").all()
    for inp in inputs:
        try:
            inp_type = inp.get_attribute("type")
            inp_name = inp.get_attribute("name")
            inp_id = inp.get_attribute("id")
            inp_placeholder = inp.get_attribute("placeholder")
            print(f"  Input: type={inp_type}, name={inp_name}, id={inp_id}, placeholder={inp_placeholder}")
        except:
            pass
    
    print("\n[*] Looking for buttons...")
    buttons = page.locator("button").all()
    for btn in buttons:
        try:
            text = btn.inner_textfrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_screenshots/page_content.html", "w") as f:
        f.write(content)
    
    print("\n[*] Looking for links and navigation...")
    links = page.locator("a").all()
    for link in links:
        try:
            href = link.get_attribute("href")
            text = link.inner_text()
            print(f"  Link: {text} -> {href}")
        except:
            pass
    
    print("\n[*] Looking for forms...")
    forms = page.locator("form").all()
    print(f"  Found {len(forms)} forms")
    
    print("\n[*] Looking for input fields...")
    inputs = page.locator("input").all()
    for inp in inputs:
        try:
            inp_type = inp.get_attribute("type")
            inp_name = inp.get_attribute("name")
            inp_id = inp.get_attribute("id")
            inp_placeholder = inp.get_attribute("placeholder")
            print(f"  Input: type={inp_type}, name={inp_name}, id={inp_id}, placeholder={inp_placeholder}")
        except:
            pass
    
    print("\n[*] Looking for buttons...")
    buttons = page.locator("button").all()
    for btn in buttons:
        try:
            text = btn.inner_text()
            btn_type = btn.get_attribute("typefrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_screenshots/page_content.html", "w") as f:
        f.write(content)
    
    print("\n[*] Looking for links and navigation...")
    links = page.locator("a").all()
    for link in links:
        try:
            href = link.get_attribute("href")
            text = link.inner_text()
            print(f"  Link: {text} -> {href}")
        except:
            pass
    
    print("\n[*] Looking for forms...")
    forms = page.locator("form").all()
    print(f"  Found {len(forms)} forms")
    
    print("\n[*] Looking for input fields...")
    inputs = page.locator("input").all()
    for inp in inputs:
        try:
            inp_type = inp.get_attribute("type")
            inp_name = inp.get_attribute("name")
            inp_id = inp.get_attribute("id")
            inp_placeholder = inp.get_attribute("placeholder")
            print(f"  Input: type={inp_type}, name={inp_name}, id={inp_id}, placeholder={inp_placeholder}")
        except:
            pass
    
    print("\n[*] Looking for buttons...")
    buttons = page.locator("button").all()
    for btn in buttons:
        try:
            text = btn.inner_text()
            btn_type = btn.get_attribute("type")
            print(f"  Button: {textfrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_screenshots/page_content.html", "w") as f:
        f.write(content)
    
    print("\n[*] Looking for links and navigation...")
    links = page.locator("a").all()
    for link in links:
        try:
            href = link.get_attribute("href")
            text = link.inner_text()
            print(f"  Link: {text} -> {href}")
        except:
            pass
    
    print("\n[*] Looking for forms...")
    forms = page.locator("form").all()
    print(f"  Found {len(forms)} forms")
    
    print("\n[*] Looking for input fields...")
    inputs = page.locator("input").all()
    for inp in inputs:
        try:
            inp_type = inp.get_attribute("type")
            inp_name = inp.get_attribute("name")
            inp_id = inp.get_attribute("id")
            inp_placeholder = inp.get_attribute("placeholder")
            print(f"  Input: type={inp_type}, name={inp_name}, id={inp_id}, placeholder={inp_placeholder}")
        except:
            pass
    
    print("\n[*] Looking for buttons...")
    buttons = page.locator("button").all()
    for btn in buttons:
        try:
            text = btn.inner_text()
            btn_type = btn.get_attribute("type")
            print(f"  Button: {text} (type={btn_type})")
        exceptfrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_screenshots/page_content.html", "w") as f:
        f.write(content)
    
    print("\n[*] Looking for links and navigation...")
    links = page.locator("a").all()
    for link in links:
        try:
            href = link.get_attribute("href")
            text = link.inner_text()
            print(f"  Link: {text} -> {href}")
        except:
            pass
    
    print("\n[*] Looking for forms...")
    forms = page.locator("form").all()
    print(f"  Found {len(forms)} forms")
    
    print("\n[*] Looking for input fields...")
    inputs = page.locator("input").all()
    for inp in inputs:
        try:
            inp_type = inp.get_attribute("type")
            inp_name = inp.get_attribute("name")
            inp_id = inp.get_attribute("id")
            inp_placeholder = inp.get_attribute("placeholder")
            print(f"  Input: type={inp_type}, name={inp_name}, id={inp_id}, placeholder={inp_placeholder}")
        except:
            pass
    
    print("\n[*] Looking for buttons...")
    buttons = page.locator("button").all()
    for btn in buttons:
        try:
            text = btn.inner_text()
            btn_type = btn.get_attribute("type")
            print(f"  Button: {text} (type={btn_type})")
        except:
            pass
    
    print("\n[*]from playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_screenshots/page_content.html", "w") as f:
        f.write(content)
    
    print("\n[*] Looking for links and navigation...")
    links = page.locator("a").all()
    for link in links:
        try:
            href = link.get_attribute("href")
            text = link.inner_text()
            print(f"  Link: {text} -> {href}")
        except:
            pass
    
    print("\n[*] Looking for forms...")
    forms = page.locator("form").all()
    print(f"  Found {len(forms)} forms")
    
    print("\n[*] Looking for input fields...")
    inputs = page.locator("input").all()
    for inp in inputs:
        try:
            inp_type = inp.get_attribute("type")
            inp_name = inp.get_attribute("name")
            inp_id = inp.get_attribute("id")
            inp_placeholder = inp.get_attribute("placeholder")
            print(f"  Input: type={inp_type}, name={inp_name}, id={inp_id}, placeholder={inp_placeholder}")
        except:
            pass
    
    print("\n[*] Looking for buttons...")
    buttons = page.locator("button").all()
    for btn in buttons:
        try:
            text = btn.inner_text()
            btn_type = btn.get_attribute("type")
            print(f"  Button: {text} (type={btn_type})")
        except:
            pass
    
    print("\n[*] Checking for Vue/React app indicators...")
    appfrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_screenshots/page_content.html", "w") as f:
        f.write(content)
    
    print("\n[*] Looking for links and navigation...")
    links = page.locator("a").all()
    for link in links:
        try:
            href = link.get_attribute("href")
            text = link.inner_text()
            print(f"  Link: {text} -> {href}")
        except:
            pass
    
    print("\n[*] Looking for forms...")
    forms = page.locator("form").all()
    print(f"  Found {len(forms)} forms")
    
    print("\n[*] Looking for input fields...")
    inputs = page.locator("input").all()
    for inp in inputs:
        try:
            inp_type = inp.get_attribute("type")
            inp_name = inp.get_attribute("name")
            inp_id = inp.get_attribute("id")
            inp_placeholder = inp.get_attribute("placeholder")
            print(f"  Input: type={inp_type}, name={inp_name}, id={inp_id}, placeholder={inp_placeholder}")
        except:
            pass
    
    print("\n[*] Looking for buttons...")
    buttons = page.locator("button").all()
    for btn in buttons:
        try:
            text = btn.inner_text()
            btn_type = btn.get_attribute("type")
            print(f"  Button: {text} (type={btn_type})")
        except:
            pass
    
    print("\n[*] Checking for Vue/React app indicators...")
    app_data = page.evaluate("""() => {
        returnfrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_screenshots/page_content.html", "w") as f:
        f.write(content)
    
    print("\n[*] Looking for links and navigation...")
    links = page.locator("a").all()
    for link in links:
        try:
            href = link.get_attribute("href")
            text = link.inner_text()
            print(f"  Link: {text} -> {href}")
        except:
            pass
    
    print("\n[*] Looking for forms...")
    forms = page.locator("form").all()
    print(f"  Found {len(forms)} forms")
    
    print("\n[*] Looking for input fields...")
    inputs = page.locator("input").all()
    for inp in inputs:
        try:
            inp_type = inp.get_attribute("type")
            inp_name = inp.get_attribute("name")
            inp_id = inp.get_attribute("id")
            inp_placeholder = inp.get_attribute("placeholder")
            print(f"  Input: type={inp_type}, name={inp_name}, id={inp_id}, placeholder={inp_placeholder}")
        except:
            pass
    
    print("\n[*] Looking for buttons...")
    buttons = page.locator("button").all()
    for btn in buttons:
        try:
            text = btn.inner_text()
            btn_type = btn.get_attribute("type")
            print(f"  Button: {text} (type={btn_type})")
        except:
            pass
    
    print("\n[*] Checking for Vue/React app indicators...")
    app_data = page.evaluate("""() => {
        return {
            vue: typeof Vue !== 'undefined' || typeof window.__VUE__ !== 'undefinedfrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_screenshots/page_content.html", "w") as f:
        f.write(content)
    
    print("\n[*] Looking for links and navigation...")
    links = page.locator("a").all()
    for link in links:
        try:
            href = link.get_attribute("href")
            text = link.inner_text()
            print(f"  Link: {text} -> {href}")
        except:
            pass
    
    print("\n[*] Looking for forms...")
    forms = page.locator("form").all()
    print(f"  Found {len(forms)} forms")
    
    print("\n[*] Looking for input fields...")
    inputs = page.locator("input").all()
    for inp in inputs:
        try:
            inp_type = inp.get_attribute("type")
            inp_name = inp.get_attribute("name")
            inp_id = inp.get_attribute("id")
            inp_placeholder = inp.get_attribute("placeholder")
            print(f"  Input: type={inp_type}, name={inp_name}, id={inp_id}, placeholder={inp_placeholder}")
        except:
            pass
    
    print("\n[*] Looking for buttons...")
    buttons = page.locator("button").all()
    for btn in buttons:
        try:
            text = btn.inner_text()
            btn_type = btn.get_attribute("type")
            print(f"  Button: {text} (type={btn_type})")
        except:
            pass
    
    print("\n[*] Checking for Vue/React app indicators...")
    app_data = page.evaluate("""() => {
        return {
            vue: typeof Vue !== 'undefined' || typeof window.__VUE__ !== 'undefined',
            react: typeof React !== 'undefined',
from playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_screenshots/page_content.html", "w") as f:
        f.write(content)
    
    print("\n[*] Looking for links and navigation...")
    links = page.locator("a").all()
    for link in links:
        try:
            href = link.get_attribute("href")
            text = link.inner_text()
            print(f"  Link: {text} -> {href}")
        except:
            pass
    
    print("\n[*] Looking for forms...")
    forms = page.locator("form").all()
    print(f"  Found {len(forms)} forms")
    
    print("\n[*] Looking for input fields...")
    inputs = page.locator("input").all()
    for inp in inputs:
        try:
            inp_type = inp.get_attribute("type")
            inp_name = inp.get_attribute("name")
            inp_id = inp.get_attribute("id")
            inp_placeholder = inp.get_attribute("placeholder")
            print(f"  Input: type={inp_type}, name={inp_name}, id={inp_id}, placeholder={inp_placeholder}")
        except:
            pass
    
    print("\n[*] Looking for buttons...")
    buttons = page.locator("button").all()
    for btn in buttons:
        try:
            text = btn.inner_text()
            btn_type = btn.get_attribute("type")
            print(f"  Button: {text} (type={btn_type})")
        except:
            pass
    
    print("\n[*] Checking for Vue/React app indicators...")
    app_data = page.evaluate("""() => {
        return {
            vue: typeof Vue !== 'undefined' || typeof window.__VUE__ !== 'undefined',
            react: typeof React !== 'undefined',
            localStorage: Object.keys(localStorage),
            sessionStorage:from playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_screenshots/page_content.html", "w") as f:
        f.write(content)
    
    print("\n[*] Looking for links and navigation...")
    links = page.locator("a").all()
    for link in links:
        try:
            href = link.get_attribute("href")
            text = link.inner_text()
            print(f"  Link: {text} -> {href}")
        except:
            pass
    
    print("\n[*] Looking for forms...")
    forms = page.locator("form").all()
    print(f"  Found {len(forms)} forms")
    
    print("\n[*] Looking for input fields...")
    inputs = page.locator("input").all()
    for inp in inputs:
        try:
            inp_type = inp.get_attribute("type")
            inp_name = inp.get_attribute("name")
            inp_id = inp.get_attribute("id")
            inp_placeholder = inp.get_attribute("placeholder")
            print(f"  Input: type={inp_type}, name={inp_name}, id={inp_id}, placeholder={inp_placeholder}")
        except:
            pass
    
    print("\n[*] Looking for buttons...")
    buttons = page.locator("button").all()
    for btn in buttons:
        try:
            text = btn.inner_text()
            btn_type = btn.get_attribute("type")
            print(f"  Button: {text} (type={btn_type})")
        except:
            pass
    
    print("\n[*] Checking for Vue/React app indicators...")
    app_data = page.evaluate("""() => {
        return {
            vue: typeof Vue !== 'undefined' || typeof window.__VUE__ !== 'undefined',
            react: typeof React !== 'undefined',
            localStorage: Object.keys(localStorage),
            sessionStorage: Object.keys(sessionStorage),
            cookies: document.cookiefrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_screenshots/page_content.html", "w") as f:
        f.write(content)
    
    print("\n[*] Looking for links and navigation...")
    links = page.locator("a").all()
    for link in links:
        try:
            href = link.get_attribute("href")
            text = link.inner_text()
            print(f"  Link: {text} -> {href}")
        except:
            pass
    
    print("\n[*] Looking for forms...")
    forms = page.locator("form").all()
    print(f"  Found {len(forms)} forms")
    
    print("\n[*] Looking for input fields...")
    inputs = page.locator("input").all()
    for inp in inputs:
        try:
            inp_type = inp.get_attribute("type")
            inp_name = inp.get_attribute("name")
            inp_id = inp.get_attribute("id")
            inp_placeholder = inp.get_attribute("placeholder")
            print(f"  Input: type={inp_type}, name={inp_name}, id={inp_id}, placeholder={inp_placeholder}")
        except:
            pass
    
    print("\n[*] Looking for buttons...")
    buttons = page.locator("button").all()
    for btn in buttons:
        try:
            text = btn.inner_text()
            btn_type = btn.get_attribute("type")
            print(f"  Button: {text} (type={btn_type})")
        except:
            pass
    
    print("\n[*] Checking for Vue/React app indicators...")
    app_data = page.evaluate("""() => {
        return {
            vue: typeof Vue !== 'undefined' || typeof window.__VUE__ !== 'undefined',
            react: typeof React !== 'undefined',
            localStorage: Object.keys(localStorage),
            sessionStorage: Object.keys(sessionStorage),
            cookies: document.cookie
        }
    }""")
    print(f"from playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_screenshots/page_content.html", "w") as f:
        f.write(content)
    
    print("\n[*] Looking for links and navigation...")
    links = page.locator("a").all()
    for link in links:
        try:
            href = link.get_attribute("href")
            text = link.inner_text()
            print(f"  Link: {text} -> {href}")
        except:
            pass
    
    print("\n[*] Looking for forms...")
    forms = page.locator("form").all()
    print(f"  Found {len(forms)} forms")
    
    print("\n[*] Looking for input fields...")
    inputs = page.locator("input").all()
    for inp in inputs:
        try:
            inp_type = inp.get_attribute("type")
            inp_name = inp.get_attribute("name")
            inp_id = inp.get_attribute("id")
            inp_placeholder = inp.get_attribute("placeholder")
            print(f"  Input: type={inp_type}, name={inp_name}, id={inp_id}, placeholder={inp_placeholder}")
        except:
            pass
    
    print("\n[*] Looking for buttons...")
    buttons = page.locator("button").all()
    for btn in buttons:
        try:
            text = btn.inner_text()
            btn_type = btn.get_attribute("type")
            print(f"  Button: {text} (type={btn_type})")
        except:
            pass
    
    print("\n[*] Checking for Vue/React app indicators...")
    app_data = page.evaluate("""() => {
        return {
            vue: typeof Vue !== 'undefined' || typeof window.__VUE__ !== 'undefined',
            react: typeof React !== 'undefined',
            localStorage: Object.keys(localStorage),
            sessionStorage: Object.keys(sessionStorage),
            cookies: document.cookie
        }
    }""")
    print(f"  App Framework Data: {json.dumps(app_datafrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_screenshots/page_content.html", "w") as f:
        f.write(content)
    
    print("\n[*] Looking for links and navigation...")
    links = page.locator("a").all()
    for link in links:
        try:
            href = link.get_attribute("href")
            text = link.inner_text()
            print(f"  Link: {text} -> {href}")
        except:
            pass
    
    print("\n[*] Looking for forms...")
    forms = page.locator("form").all()
    print(f"  Found {len(forms)} forms")
    
    print("\n[*] Looking for input fields...")
    inputs = page.locator("input").all()
    for inp in inputs:
        try:
            inp_type = inp.get_attribute("type")
            inp_name = inp.get_attribute("name")
            inp_id = inp.get_attribute("id")
            inp_placeholder = inp.get_attribute("placeholder")
            print(f"  Input: type={inp_type}, name={inp_name}, id={inp_id}, placeholder={inp_placeholder}")
        except:
            pass
    
    print("\n[*] Looking for buttons...")
    buttons = page.locator("button").all()
    for btn in buttons:
        try:
            text = btn.inner_text()
            btn_type = btn.get_attribute("type")
            print(f"  Button: {text} (type={btn_type})")
        except:
            pass
    
    print("\n[*] Checking for Vue/React app indicators...")
    app_data = page.evaluate("""() => {
        return {
            vue: typeof Vue !== 'undefined' || typeof window.__VUE__ !== 'undefined',
            react: typeof React !== 'undefined',
            localStorage: Object.keys(localStorage),
            sessionStorage: Object.keys(sessionStorage),
            cookies: document.cookie
        }
    }""")
    print(f"  App Framework Data: {json.dumps(app_data, indent=2)}")
    
    print("\from playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_screenshots/page_content.html", "w") as f:
        f.write(content)
    
    print("\n[*] Looking for links and navigation...")
    links = page.locator("a").all()
    for link in links:
        try:
            href = link.get_attribute("href")
            text = link.inner_text()
            print(f"  Link: {text} -> {href}")
        except:
            pass
    
    print("\n[*] Looking for forms...")
    forms = page.locator("form").all()
    print(f"  Found {len(forms)} forms")
    
    print("\n[*] Looking for input fields...")
    inputs = page.locator("input").all()
    for inp in inputs:
        try:
            inp_type = inp.get_attribute("type")
            inp_name = inp.get_attribute("name")
            inp_id = inp.get_attribute("id")
            inp_placeholder = inp.get_attribute("placeholder")
            print(f"  Input: type={inp_type}, name={inp_name}, id={inp_id}, placeholder={inp_placeholder}")
        except:
            pass
    
    print("\n[*] Looking for buttons...")
    buttons = page.locator("button").all()
    for btn in buttons:
        try:
            text = btn.inner_text()
            btn_type = btn.get_attribute("type")
            print(f"  Button: {text} (type={btn_type})")
        except:
            pass
    
    print("\n[*] Checking for Vue/React app indicators...")
    app_data = page.evaluate("""() => {
        return {
            vue: typeof Vue !== 'undefined' || typeof window.__VUE__ !== 'undefined',
            react: typeof React !== 'undefined',
            localStorage: Object.keys(localStorage),
            sessionStorage: Object.keys(sessionStorage),
            cookies: document.cookie
        }
    }""")
    print(f"  App Framework Data: {json.dumps(app_data, indent=2)}")
    
    print("\n[*] Looking for login/register buttons or links...")
    login_elements = page.locator("textfrom playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_screenshots/page_content.html", "w") as f:
        f.write(content)
    
    print("\n[*] Looking for links and navigation...")
    links = page.locator("a").all()
    for link in links:
        try:
            href = link.get_attribute("href")
            text = link.inner_text()
            print(f"  Link: {text} -> {href}")
        except:
            pass
    
    print("\n[*] Looking for forms...")
    forms = page.locator("form").all()
    print(f"  Found {len(forms)} forms")
    
    print("\n[*] Looking for input fields...")
    inputs = page.locator("input").all()
    for inp in inputs:
        try:
            inp_type = inp.get_attribute("type")
            inp_name = inp.get_attribute("name")
            inp_id = inp.get_attribute("id")
            inp_placeholder = inp.get_attribute("placeholder")
            print(f"  Input: type={inp_type}, name={inp_name}, id={inp_id}, placeholder={inp_placeholder}")
        except:
            pass
    
    print("\n[*] Looking for buttons...")
    buttons = page.locator("button").all()
    for btn in buttons:
        try:
            text = btn.inner_text()
            btn_type = btn.get_attribute("type")
            print(f"  Button: {text} (type={btn_type})")
        except:
            pass
    
    print("\n[*] Checking for Vue/React app indicators...")
    app_data = page.evaluate("""() => {
        return {
            vue: typeof Vue !== 'undefined' || typeof window.__VUE__ !== 'undefined',
            react: typeof React !== 'undefined',
            localStorage: Object.keys(localStorage),
            sessionStorage: Object.keys(sessionStorage),
            cookies: document.cookie
        }
    }""")
    print(f"  App Framework Data: {json.dumps(app_data, indent=2)}")
    
    print("\n[*] Looking for login/register buttons or links...")
    login_elements = page.locator("text=/登录|注册|login|register/i").from playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_screenshots/page_content.html", "w") as f:
        f.write(content)
    
    print("\n[*] Looking for links and navigation...")
    links = page.locator("a").all()
    for link in links:
        try:
            href = link.get_attribute("href")
            text = link.inner_text()
            print(f"  Link: {text} -> {href}")
        except:
            pass
    
    print("\n[*] Looking for forms...")
    forms = page.locator("form").all()
    print(f"  Found {len(forms)} forms")
    
    print("\n[*] Looking for input fields...")
    inputs = page.locator("input").all()
    for inp in inputs:
        try:
            inp_type = inp.get_attribute("type")
            inp_name = inp.get_attribute("name")
            inp_id = inp.get_attribute("id")
            inp_placeholder = inp.get_attribute("placeholder")
            print(f"  Input: type={inp_type}, name={inp_name}, id={inp_id}, placeholder={inp_placeholder}")
        except:
            pass
    
    print("\n[*] Looking for buttons...")
    buttons = page.locator("button").all()
    for btn in buttons:
        try:
            text = btn.inner_text()
            btn_type = btn.get_attribute("type")
            print(f"  Button: {text} (type={btn_type})")
        except:
            pass
    
    print("\n[*] Checking for Vue/React app indicators...")
    app_data = page.evaluate("""() => {
        return {
            vue: typeof Vue !== 'undefined' || typeof window.__VUE__ !== 'undefined',
            react: typeof React !== 'undefined',
            localStorage: Object.keys(localStorage),
            sessionStorage: Object.keys(sessionStorage),
            cookies: document.cookie
        }
    }""")
    print(f"  App Framework Data: {json.dumps(app_data, indent=2)}")
    
    print("\n[*] Looking for login/register buttons or links...")
    login_elements = page.locator("text=/登录|注册|login|register/i").all()
    for elem in login_elements:
from playwright.sync_api import sync_playwright
import json
import time

TARGET_URL = "https://card.tiantianyy.com/pages/index.html"

captured_requests = []
captured_responses = []

def capture_request(request):
    req_info = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "post_data": request.post_data
    }
    captured_requests.append(req_info)
    print(f"[REQUEST] {request.method} {request.url}")
    if request.post_data:
        print(f"  POST Data: {request.post_data}")

def capture_response(response):
    resp_info = {
        "url": response.url,
        "status": response.status,
        "headers": dict(response.headers)
    }
    try:
        body = response.text()
        resp_info["body"] = body[:2000] if body else None
    except:
        resp_info["body"] = None
    captured_responses.append(resp_info)
    if "api" in response.url.lower() or "login" in response.url.lower() or "register" in response.url.lower():
        print(f"[RESPONSE] {response.status} {response.url}")
        if resp_info["body"]:
            print(f"  Body: {resp_info['body'][:500]}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    
    page.on("request", capture_request)
    page.on("response", capture_response)
    
    print(f"[*] Navigating to {TARGET_URL}")
    page.goto(TARGET_URL, wait_until="networkidle", timeout=30000)
    
    print("\n[*] Taking initial screenshot...")
    page.screenshot(path="/workspace/audit_screenshots/01_homepage.png", full_page=True)
    
    print("\n[*] Page content:")
    content = page.content()
    with open("/workspace/audit_screenshots/page_content.html", "w") as f:
        f.write(content)
    
    print("\n[*] Looking for links and navigation...")
    links = page.locator("a").all()
    for link in links:
        try:
            href = link.get_attribute("href")
            text = link.inner_text()
            print(f"  Link: {text} -> {href}")
        except:
            pass
    
    print("\n[*] Looking for forms...")
    forms = page.locator("form").all()
    print(f"  Found {len(forms)} forms")
    
    print("\n[*] Looking for input fields...")
    inputs = page.locator("input").all()
    for inp in inputs:
        try:
            inp_type = inp.get_attribute("type")
            inp_name = inp.get_attribute("name")
            inp_id = inp.get_attribute("id")
            inp_placeholder = inp.get_attribute("placeholder")
            print(f"  Input: type={inp_type}, name={inp_name}, id={inp_id}, placeholder={inp_placeholder}")
        except:
            pass
    
    print("\n[*] Looking for buttons...")
    buttons = page.locator("button").all()
    for btn in buttons:
        try:
            text = btn.inner_text()
            btn_type = btn.get_attribute("type")
            print(f"  Button: {text} (type={btn_type})")
        except:
            pass
    
    print("\n[*] Checking for Vue/React app indicators...")
    app_data = page.evaluate("""() => {
        return {
            vue: typeof Vue !== 'undefined' || typeof window.__VUE__ !== 'undefined',
            react: typeof React !== 'undefined',
            localStorage: Object.keys(localStorage),
            sessionStorage: Object.keys(sessionStorage),
            cookies: document.cookie
        }
    }""")
    print(f"  App Framework Data: {json.dumps(app_data, indent=2)}")
    
    print("\n[*] Looking for login/register buttons or links...")
    login_elements = page.locator("text=/登录|注册|login|register/i").all()
    for elem in login_elements:
        try:
            print(f"  Found: {