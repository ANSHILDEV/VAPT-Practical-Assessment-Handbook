# Out-of-Band SQL Injection

## Concept
The application/database causes a network interaction that can be observed through a separate channel, such as an assessor-approved DNS or HTTP callback service.

## Requirements
- Written permission for OOB testing.
- An approved callback domain/service controlled by the assessment team.
- Confirmation that outbound callback testing is in scope.
- No callbacks to internal infrastructure, cloud metadata services or unrelated third parties.

## Safe validation
1. Confirm the callback endpoint with the assessment owner.
2. Use the lab's documented OOB mechanism or an approved benign marker.
3. Correlate callback time and unique test identifier with the request.
4. Repeat once if permitted.
5. Do not use OOB to retrieve data or establish a tunnel.

## Reporting
Document the approved callback host, unique marker, request timestamp, callback evidence and scope limitations. Redact sensitive values.

OOB techniques are environment- and database-specific. If outbound network access is blocked, absence of a callback does not prove the application is free from SQL injection.
