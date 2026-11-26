# Authentication, Session and Access-Control Testing

## Authentication
Test login, logout, reset, MFA and recovery. Check rate limiting without password spraying. Reset tokens should be random, single-use, expiring and account-bound.

## Session
Check token rotation after login/privilege changes, expiry, server-side logout invalidation and cookie flags Secure/HttpOnly/SameSite. Avoid tokens in URLs, logs or public notes.

## IDOR / BOLA
1. Use two test accounts supplied for the assessment.
2. Capture a request for an object owned by account A.
3. Replay as account B, changing only the object reference.
4. Verify server-side ownership enforcement.
5. Use test records only; never access real customer data.

## Remediation
Enforce authorisation on every request and object, use deny-by-default policies, bind objects to the authenticated principal and test role/ownership boundaries.
