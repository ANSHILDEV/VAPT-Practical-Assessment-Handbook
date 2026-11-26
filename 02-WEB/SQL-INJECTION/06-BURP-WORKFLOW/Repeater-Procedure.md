# Burp Suite Repeater – SQLi Procedure

1. Start Burp and configure the authorised browser/device proxy.
2. Browse the application normally with the supplied test account.
3. Find a request containing a candidate input.
4. Send the request to Repeater.
5. Save/copy the untouched baseline.
6. Change only one parameter.
7. Send a harmless syntax probe.
8. Compare status, response length, content and timing.
9. For blind tests, alternate a controlled true/false pair.
10. Save sanitised request/response evidence.
11. Restore the original input and confirm normal behaviour.

Do not use Intruder, Scanner or extensions unless the assessment rules permit automated testing. Never include live cookies or tokens in public notes.
