# SQL Injection Remediation

## Primary fix
Use parameterised queries / prepared statements so user input is treated as data, not executable SQL.

## Additional controls
- Avoid building SQL through string concatenation.
- Use allowlists for dynamic identifiers such as column names and sort directions; bind variables generally cannot parameterise identifiers.
- Apply server-side validation based on expected data types and business rules.
- Use least-privilege database accounts.
- Avoid exposing detailed SQL/database errors to end users.
- Log safely without recording passwords, tokens or sensitive customer data.
- Add unit/integration security tests for affected query paths.
- Review ORM/raw-query usage and stored procedures.

Input filtering alone is not a reliable primary defence.
