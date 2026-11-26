# Web Application Testing Checklist

## Mapping
- [ ] Browse functions using supplied test account.
- [ ] Capture requests in Burp Proxy.
- [ ] Identify parameters in URL, body, cookies and headers.
- [ ] Map roles, uploads, downloads, search, export and transaction flows.

## Authentication/session
- [ ] Login enumeration and error behaviour.
- [ ] MFA and recovery flow.
- [ ] Reset token expiry, single-use and account binding.
- [ ] Session rotation after login/privilege change.
- [ ] Logout invalidates session.
- [ ] Cookie flags: Secure, HttpOnly, SameSite.
- [ ] Session timeout.

## Authorisation
- [ ] Compare access using two supplied test accounts.
- [ ] Test direct access to another test user's object (IDOR).
- [ ] Test low-privilege access to privileged functions.
- [ ] Verify server-side enforcement, not just hidden UI controls.

## Input/configuration
- [ ] SQLi, XSS, command injection indicators.
- [ ] Path traversal, SSRF, unsafe redirects.
- [ ] File upload type/content/size/storage checks.
- [ ] CORS, CSP, cache directives, HSTS and clickjacking protection.
- [ ] Verbose errors, debug endpoints and directory listing.

## Business logic
- [ ] Can steps be skipped or repeated?
- [ ] Are amount, beneficiary, ownership and limits checked server-side?
- [ ] Are duplicate/replayed requests handled safely?
- [ ] Is re-authentication/approval required for sensitive actions?
