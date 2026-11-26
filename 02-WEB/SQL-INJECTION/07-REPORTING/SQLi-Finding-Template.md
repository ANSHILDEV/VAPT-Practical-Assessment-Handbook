# Finding – SQL Injection

- Finding ID:
- Title:
- Affected URL/API:
- HTTP method:
- Parameter:
- User role:
- SQLi category: Error-based / UNION-based / Boolean blind / Time blind / OOB
- Severity:
- CWE / OWASP mapping (if requested):

## Description
Explain how untrusted input affects SQL query processing.

## Preconditions
Required account, role, workflow or configuration.

## Reproduction
1. Describe how to reach the function.
2. Identify the request and parameter.
3. Explain the controlled test input (sanitised).
4. Describe the repeatable response difference.

## Evidence
Attach baseline and test request/response, screenshots and timing table if relevant.

## Impact
State only the impact demonstrated. Do not claim database takeover or data exposure unless proven and authorised.

## Recommendation
- Parameterised queries / prepared statements.
- Avoid dynamic SQL concatenation.
- Validate input by expected type and allowlist where appropriate.
- Least-privilege DB account.
- Suppress detailed database errors from users.
- Add security tests to the development pipeline.

## Limitations and retest
Record unavailable source code, database access, keys, test accounts or restricted validation.
