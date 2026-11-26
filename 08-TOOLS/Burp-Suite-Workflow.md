# Burp Suite Workflow

1. Configure browser proxy and install Burp CA only in the authorised test browser/device.
2. Browse with supplied test credentials.
3. Use Proxy HTTP history to map endpoints and parameters.
4. Send selected requests to Repeater; save baseline.
5. Change one variable at a time and compare responses.
6. Use Decoder and Comparer where useful.
7. Use Intruder only within approved rate/volume limits.
8. Use Scanner only if available and explicitly permitted.
9. Save sanitised evidence and record the finding ID.

Never export live cookies, tokens or client data into public notes.
