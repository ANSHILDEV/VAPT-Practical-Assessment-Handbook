# In-band SQL Injection

In-band means the result or useful database feedback returns through the same application response channel.

## A. Error-based SQLi
The application exposes database errors or differences that reveal query behaviour.

**Detection**
1. Capture a baseline.
2. In a lab, introduce a harmless syntax-breaking character in one candidate parameter.
3. Compare the response with baseline.
4. Look for a database-specific error or a consistent error-handling difference.
5. Repeat and rule out generic server errors.

**Evidence**
Sanitised request/response, affected parameter, exact error text, repeatability and role.

**Caution**
Detailed database errors may be information disclosure, but an error message alone does not always prove exploitable SQL injection.

## B. UNION-based SQLi
UNION combines results from compatible SELECT queries. A vulnerable query may expose selected values in the application response.

**Lab learning sequence**
1. Establish that the input is query-controlled.
2. In a deliberately vulnerable lab, determine whether the query expects a compatible number of columns.
3. Determine which output position is reflected.
4. Use harmless static markers in the lab to understand the reflection.
5. Stop at the authorised proof point; do not extract real records.

**Evidence**
Show the controlled marker appearing in a response, plus the baseline and reproduction steps.

**Remediation**
Use parameterised queries. Do not concatenate user input into SQL. Apply least privilege and safe error handling.
