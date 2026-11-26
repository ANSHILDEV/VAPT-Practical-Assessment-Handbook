# SQL Injection – Practical Workflow

## Step 1: Understand the application
- Identify the function: login, search, filter, sort, report, lookup or record detail.
- Identify the HTTP method and content type.
- Note the parameter location: query string, form body, JSON, cookie or header.
- Use only the account and test data supplied for the assessment.

## Step 2: Capture a baseline
1. Interact with the feature normally.
2. Capture the request in Burp Proxy.
3. Send it to Repeater.
4. Save the original request and response.
5. Record status code, response length, key text and normal response time.

## Step 3: Identify candidate input
Prioritise parameters that appear to affect database-backed search, filtering, sorting, authentication or record retrieval. Change one parameter at a time.

## Step 4: Test safely
- Begin with harmless syntax probes appropriate to the input context.
- Compare normal input with a controlled true/false condition.
- Look for a repeatable response difference.
- If an error appears, determine whether it is database-related rather than a generic application/WAF error.
- Use time-based checks only where permitted, with short, controlled delays and repeat measurements.
- Avoid extraction or data-changing statements.

## Step 5: Confirm and assess impact
- Reproduce the behaviour.
- Confirm the exact endpoint and parameter.
- Establish the likely database/query context only as far as needed.
- Demonstrate minimum necessary impact using lab or synthetic data.
- Record any restrictions that prevent deeper validation.

## Step 6: Report
Record endpoint, method, parameter, account role, baseline, test case, response difference, reproduction steps, impact, evidence, severity and remediation.

## Quick decision tree
- Database error visible? Investigate **error-based in-band**.
- Query result can be safely reflected? Investigate **UNION-based in-band** in a lab.
- No result/error, but true/false changes response? Investigate **boolean blind**.
- No visible difference, but a repeatable permitted delay is observed? Investigate **time-based blind**.
- A separate approved callback is observed? Investigate **OOB**.
- No repeatable difference? Do not report SQLi; investigate other causes.
