#!/usr/bin/env python3
import requests
import json

# Test webhook authentication bypass
webhook_urls = [
    "http://localhost:3000/api/stripe/webhook",
    "http://localhost:3000/api/creem/webhook",
    "http://localhost:3000/api/waffo/webhook"
]

# Test payload
payload = {
    "event": "test.event",
    "data": {
        "object": {
            "id": "test_id",
            "amount": 1000
        }
    }
}

print("Testing webhook authentication bypass...")
for url in webhook_urls:
    print(f"\nTesting: {url}")
    try:
        response = requests.post(url, json=payload)
        print(f"Status code: {response.status_code}")
        print(f"Response: {response.text[:200]}...")
        if response.status_code == 200:
            print("[WARNING] Webhook endpoint accepted request without signature verification!")
        else:
            print("[INFO] Webhook endpoint returned non-200 status")
    except Exception as e:
        print(f"[ERROR] Failed to connect: {e}")

print("\nWebhook test completed.")
