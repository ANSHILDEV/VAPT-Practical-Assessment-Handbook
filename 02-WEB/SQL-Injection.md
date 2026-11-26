# SQL Injection – Practical Note

SQL injection occurs when untrusted input changes the structure or meaning of a database query.

## Where to look
Search, login, filters, sorting, report generation, record IDs, JSON fields, cookies and headers.

## Safe workflow
1. Capture a normal request in Burp.
2. Send it to Repeater and save a baseline.
3. Change one parameter at a time.
4. Compare normal input with harmless syntax-breaking input and controlled true/false conditions.
5. Look for repeatable differences in status, content, response length or timing.
6. Confirm only with authorised test data and non-destructive proof.
7. Do not dump tables, enumerate real users, modify data or run heavy time delays unless explicitly authorised.

## Illustrative lab patterns
Use only on explicitly authorised labs/targets; syntax depends on query context:
```text
'
''
1' AND '1'='1
1' AND '1'='2
```

## Record
Endpoint/method, parameter, baseline and test requests/responses, repeatability, role, evidence, demonstrated impact and limitations.

## False positives
A generic 500 error, WAF block, caching difference or one-off timing spike does not prove SQLi.

## Remediation
Prepared statements/parameterised queries, avoid dynamic SQL concatenation, validate expected input types, least-privilege DB accounts and safe error handling.
