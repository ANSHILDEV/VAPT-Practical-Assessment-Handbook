# Universal VAPT Checklist

## Understand the application
- [ ] Business purpose and sensitive data identified.
- [ ] Roles, privileges and key workflows mapped.
- [ ] Entry points, trust boundaries and integrations identified.
- [ ] Authentication, session and authorisation mechanisms understood.

## Identity and access
- [ ] Login, logout, password reset and MFA.
- [ ] Session rotation, expiry and invalidation.
- [ ] Horizontal access control: user A versus user B.
- [ ] Vertical access control: low privilege versus privileged functions.
- [ ] Server-side checks on every sensitive action.

## Input and output
- [ ] SQL/NoSQL/OS injection.
- [ ] Reflected, stored and DOM XSS.
- [ ] Path traversal / local file access.
- [ ] File upload validation and storage.
- [ ] SSRF in URL fetch, webhook or import features.
- [ ] XML parsing risks if XML is accepted.
- [ ] Unsafe deserialisation/template handling if relevant.
- [ ] Error leakage and security headers.

## Data protection and business logic
- [ ] TLS and certificate validation.
- [ ] Sensitive data in URLs, responses, logs and client storage.
- [ ] Encryption design and key management where reviewable.
- [ ] Password hashing rather than reversible password encryption.
- [ ] Transaction ownership, limits, beneficiary and approval checks.
- [ ] Duplicate/replay protection, idempotency and audit trail.

## Reporting
- [ ] Findings reproducible and evidence sanitised.
- [ ] Impact demonstrated, not exaggerated.
- [ ] Severity justified and remediation actionable.
