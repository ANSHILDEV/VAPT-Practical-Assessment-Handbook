# API Security Testing Checklist

## Discovery
- [ ] Identify base URL, version, methods and content types.
- [ ] Review supplied OpenAPI/Swagger documentation.
- [ ] Capture requests from web/mobile client.
- [ ] Map endpoints, object IDs, parameters and roles.

## Authentication/authorisation
- [ ] Missing, invalid and expired token handling.
- [ ] JWT signature, issuer, audience, expiry and algorithm validation.
- [ ] BOLA: user A accessing user B's object.
- [ ] Function-level authorisation across roles.
- [ ] Property-level authorisation and mass assignment.
- [ ] Token scope and privilege enforcement.
- [ ] API secrets not exposed in client apps/repositories.

## Input/resource controls
- [ ] Injection in query, path, header and JSON fields.
- [ ] Rate limits, pagination and response-size limits.
- [ ] File upload and URL-fetching features.
- [ ] CORS, content-type and error handling.

## Banking logic
- [ ] Account ownership and beneficiary validation.
- [ ] Amount/currency/limit validation server-side.
- [ ] Duplicate transfer and replay protection.
- [ ] Idempotency, maker-checker and audit events.
- [ ] No sensitive data in URLs or excessive responses.

Use test accounts and test records. Never initiate real transfers or enumerate customer identifiers without explicit written permission.
