# TLS and Encryption Review Without Production Keys

## Checks possible without production keys
- TLS versions, cipher suites, certificate validity, hostname match and trust chain.
- Cleartext HTTP/mixed content.
- Sensitive data in URLs, logs, responses or client storage.
- Source/config review for hardcoded secrets, if supplied.
- Algorithm/mode, IV/nonce generation and authentication design, if implementation is reviewable.
- Key storage, access controls, rotation and lifecycle documentation.
- Password storage: secure password hashing (e.g. Argon2id/bcrypt), not reversible encryption.

## When keys are needed
For end-to-end encryption/decryption validation, request a dedicated test environment, test keys and synthetic data. Never request production secrets or bypass key controls.

AES-256 alone does not guarantee security; mode, nonce/IV handling, authentication and key management matter. A signed JWT is not automatically encrypted.

If access/code/configuration is unavailable, document exactly what could not be verified. Do not conclude encryption is secure merely because ciphertext could not be decrypted.
