# Boolean-Based Blind SQL Injection

## Concept
The response changes depending on whether an injected logical condition evaluates true or false.

## Lab-only conceptual probes
```text
' AND '1'='1'--
' AND '1'='2'--
1 AND 1=1
1 AND 1=2
```
Adapt quote closure, comment syntax and data type to the lab query context.

## Procedure
1. Capture a normal baseline.
2. Send a condition expected to be true.
3. Send a condition expected to be false.
4. Compare status, response length and stable page content.
5. Alternate true/false requests to rule out state, cache and timing effects.
6. Reproduce before reporting.

## What not to do
Do not automate extraction of database values or enumerate real customer records. A true/false difference alone must be linked to SQL query behaviour, not ordinary business logic.

## Remediation
Parameterised queries, input validation by expected type, least-privilege database access and secure error handling.
