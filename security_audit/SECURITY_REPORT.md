# Security Assessment Report

## Target Information
- **URL**: https://card.tiantianyy.com
- **Type**: Card/Key Management System (卡密商城)
- **Assessment Date**: 2026-04-28
- **Assessment Type**: Black-box Security Testing (Authorized)

---

## Executive Summary

This security assessment identified multiple security findings ranging from MEDIUM to HIGH severity. The application has basic security controls in place but lacks several important protections against common web attacks.

### Risk Summary
| Severity | Count |
|----------|-------|
| HIGH | 2 |
| MEDIUM | 3 |
| LOW | 2 |
| **Total** | **7** |

---

## Detailed Findings

### Finding 1: User Enumeration Vulnerability
**Severity**: HIGH  
**Category**: Information Disclosure  
**CVSS**: 5.3 (Medium)

**Description**:  
The login endpoint returns different error messages for existing vs non-existing usernames, allowing attackers to enumerate valid user accounts.

**Evidence**:
```
Existing user (admin): "message":"密码错误" (Password incorrect)
Non-existing user (guest): "message":"用户不存在" (User not found)
```

**Impact**:  
- Attackers can identify valid usernames
- Facilitates targeted brute force attacks
- Enables account harvesting

**Recommendation**:  
Use generic error messages like "Invalid username or password" for both cases.

---

### Finding 2: No Rate Limiting on Authentication Endpoints
**Severity**: HIGH  
**Category**: Rate Limiting  
**CVSS**: 5.3 (Medium)

**Description**:  
The login and registration endpoints have no rate limiting, allowing unlimited authentication attempts.

**Evidence**:
- Successfully made 15+ login attempts without blocking
- Successfully registered 5+ accounts in rapid succession
- No CAPTCHA or throttling mechanism detected

**Impact**:
- Enables brute force password attacks
- Allows automated account creation
- Facilitates credential stuffing attacks

**Recommendation**:  
Implement rate limiting (e.g., 5 failed attempts per 15 minutes) and CAPTCHA after failed attempts.

---

### Finding 3: Device Fingerprint Bypass
**Severity**: MEDIUM  
**Category**: Authentication Bypass  
**CVSS**: 4.3 (Medium)

**Description**:  
The device fingerprint mechanism can be easily bypassed by providing arbitrary device_id values.

**Evidence**:
```json
// Registration with arbitrary device_id succeeds
{"username":"test_user","device_id":"bypass_12345"} 
// Response: "message":"注册成功"
```

**Impact**:
- One-device-per-user restriction can be bypassed
- Enables mass account creation
- Defeats fraud prevention measures

**Recommendation**:  
Validate device fingerprints server-side and implement more robust device identification.

---

### Finding 4: Sensitive Information in API Responses
**Severity**: MEDIUM  
**Category**: Information Disclosure  
**CVSS**: 4.0 (Medium)

**Description**:  
API responses expose sensitive user information including internal IDs, device IDs, and registration IPs.

**Evidence**:
```json
{
  "openid": "U69f0d126caacb9807",
  "device_id": "test_fp_001",
  "register_ip": "180.184.77.101",
  "invite_code": "QFF9DK",
  "id": 486
}
```

**Impact**:
- Internal system information exposed
- User privacy concerns
- Aids attackers in reconnaissance

**Recommendation**:  
Minimize data returned in API responses. Only return necessary fields.

---

### Finding 5: Weak Token Structure
**Severity**: MEDIUM  
**Category**: Authentication  
**CVSS**: 4.0 (Medium)

**Description**:  
The authentication token uses a custom format (base64 payload + signature) rather than a standard JWT implementation.

**Evidence**:
```
Token format: base64(payload).signature
Payload: {"user_id":486,"exp":1777994662}
```

**Positive Finding**: Token signature verification is working (forged tokens are rejected)

**Impact**:
- Non-standard implementation may have undiscovered vulnerabilities
- Harder to integrate with security tools
- Potential for implementation flaws

**Recommendation**:  
Consider using standard JWT libraries with proper RS256 signing.

---

### Finding 6: Admin Account Exists with Predictable Username
**Severity**: LOW  
**Category**: Configuration  
**CVSS**: 3.1 (Low)

**Description**:  
The admin account uses a predictable username "admin" which is commonly targeted.

**Evidence**:
```
admin: "message":"密码错误" (confirms user exists)
```

**Impact**:
- Attackers know which account to target
- Combined with no rate limiting, enables targeted attacks

**Recommendation**:  
Use non-predictable admin usernames or implement additional security layers.

---

### Finding 7: Stock Information Publicly Accessible
**Severity**: LOW  
**Category**: Information Disclosure  
**CVSS**: 2.0 (Low)

**Description**:  
Product stock levels are accessible without authentication.

**Evidence**:
```json
// GET /api/key.php?action=getStock returns:
{"success":true,"data":[{"stock":21,"sold":73,...}]}
```

**Impact**:
- Business intelligence leakage
- Competitors can monitor inventory

**Recommendation**:  
Consider requiring authentication for detailed stock information.

---

## Positive Security Findings

1. **SQL Injection Protection**: No SQL injection vulnerabilities detected in login/registration
2. **Token Signature Verification**: Forged tokens are properly rejected
3. **Input Validation**: Basic input validation is implemented
4. **Authentication Required**: Protected endpoints properly require authentication
5. **Admin Access Control**: Admin endpoints properly check for admin privileges

---

## API Endpoints Discovered

### User Endpoints
| Endpoint | Method | Auth Required | Notes |
|----------|--------|---------------|-------|
| /api/user.php?action=login | POST | No | User enumeration possible |
| /api/user.php?action=register | POST | No | No rate limiting |
| /api/user.php?action=getInfo | POST | Yes | Returns sensitive data |
| /api/user.php?action=findAccountByKey | POST | No | Account recovery |
| /api/user.php?action=resetPasswordByKey | POST | No | Key validation required |

### Admin Endpoints
| Endpoint | Method | Auth Required | Notes |
|----------|--------|---------------|-------|
| /api/admin.php?action=checkAdmin | POST | Yes | Admin check |
| /api/admin.php?action=getUsers | POST | Admin | Properly protected |
| /api/admin.php?action=getStats | POST | Admin | Properly protected |
| /api/admin.php?action=initAdmin | POST | No | Only works if no admin exists |

### Key/Product Endpoints
| Endpoint | Method | Auth Required | Notes |
|----------|--------|---------------|-------|
| /api/key.php?action=getCategories | POST | No | Public catalog |
| /api/key.php?action=getStock | POST | No | Stock info exposed |
| /api/key.php?action=buy | POST | Yes | Proper validation |

---

## Testing Tools Created

The following scripts were created for this assessment:

1. **register.py** - User registration and login testing
2. **brute_force.py** - Credential testing script
3. **vuln_scanner.py** - Comprehensive vulnerability scanner

---

## Recommendations Summary

### Critical (Immediate Action)
1. Implement rate limiting on all authentication endpoints
2. Fix user enumeration vulnerability with generic error messages

### High Priority
1. Strengthen device fingerprint validation
2. Minimize sensitive data in API responses

### Medium Priority
1. Consider standard JWT implementation
2. Add CAPTCHA after failed login attempts
3. Implement account lockout policy

### Low Priority
1. Use non-predictable admin usernames
2. Require authentication for stock information

---

## Disclaimer

This assessment was conducted with explicit authorization. The findings and recommendations are provided for security improvement purposes only. All testing was performed in a controlled manner to minimize impact on the production system.

---

*Report generated: 2026-04-28*
