# Safe Test Patterns – Authorised Labs Only

| Area | Initial check | Compare |
|---|---|---|
| SQLi | Quote / controlled boolean condition | Baseline vs true/false behaviour |
| XSS | Harmless marker, then context-appropriate lab payload | Reflected/stored/DOM output and encoding |
| IDOR/BOLA | Same object request as two supplied users | Owner vs non-owner response |
| Path traversal | Check whether file path is constrained | Normal path vs controlled lab test |
| SSRF | Assessor-approved callback endpoint | Whether server makes expected callback |
| CORS | Controlled Origin header | ACAO, credentials and browser behaviour |
| Cache | Inspect sensitive response directives | Browser/shared-cache behaviour |
| Upload | Benign test files | Validation, storage and retrieval |

Do not use payloads to extract data, execute commands, persist access, disrupt service or reach internal/cloud metadata systems unless explicitly authorised and safely controlled.
