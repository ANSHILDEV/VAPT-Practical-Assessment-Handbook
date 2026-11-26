# Headers, CORS, CSP and Cache

## CORS
Origin = scheme + host + port. Inspect `Access-Control-Allow-Origin`, `Access-Control-Allow-Credentials`, methods and headers. Test with a controlled Origin and verify in a browser. Reflecting arbitrary origins while allowing credentials can be dangerous. `*` cannot be used for credentialed browser CORS. CORS is not authentication or authorisation.

## CSP
Review `default-src`, `script-src`, `object-src`, `base-uri`, `frame-ancestors` and `connect-src`. CSP can reduce some XSS impact but does not replace output encoding.

## Cache
`no-store` means do not store; `no-cache` means revalidate before reuse. Review sensitive pages/API responses for shared-cache exposure.

## Other headers
Review HSTS, X-Content-Type-Options, Referrer-Policy and clickjacking protections. Missing header alone is not always a vulnerability; assess context and impact.
