# Blind / Inferential SQL Injection

The application does not directly display query results. The tester infers whether a condition is true or false.

## A. Boolean-based blind
A true condition and a false condition cause a repeatable difference in the response.

**Look for:** response text, record count, status, length or a stable page element.

## B. Time-based blind
A condition causes a measurable delay. Use only in a lab or when specifically authorised.

**Look for:** repeatable timing difference compared with control requests. Network latency and load can create false positives.

## Validation
- Alternate control and test requests.
- Repeat several times.
- Compare medians or consistent patterns rather than one request.
- Keep delay small and approved.
- Stop if the application becomes slow or unstable.

Do not use blind SQLi to extract customer data or perform prolonged delays on banking systems.
