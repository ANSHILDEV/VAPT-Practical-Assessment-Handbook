# JWT, OAuth 2.0 and API Gateway

## JWT
A JWT commonly has header, payload and signature parts. A signed JWT is not necessarily encrypted; payload is generally readable. Validate signature, allowed algorithms, `iss`, `aud`, `exp`, `nbf`, token purpose and privileges. Do not place secrets in readable payloads.

## OAuth 2.0
OAuth 2.0 is an authorisation framework. Authorization Code + PKCE is common for user-facing apps; Client Credentials is common for machine-to-machine. Do not embed confidential client secrets in browser/mobile apps.

## API Gateway
Can provide routing, authentication policies, throttling, TLS termination and logging. It does not replace backend object-level authorisation.

## IBM context
IBM API Connect is an API management platform; IBM DataPower can provide gateway/runtime capabilities. Architecture varies by deployment. Do not assume the gateway connects directly to a core banking database.
