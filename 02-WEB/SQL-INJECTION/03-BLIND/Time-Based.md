# Time-Based Blind SQL Injection

## Concept
A database query is made to wait under a controlled condition. The tester observes a timing difference rather than returned data.

## Lab-only examples
Database syntax differs. Examples below illustrate the concept and are not universal:
```text
' AND SLEEP(2)--
'; WAITFOR DELAY '00:00:02'--
```
Use only in a deliberately vulnerable lab. Do not run delay tests against a bank target unless explicitly authorised.

## Validation
1. Record several baseline timings.
2. Alternate normal and controlled test requests.
3. Repeat only a small, approved number of times.
4. Compare median timings.
5. Confirm the delay tracks the condition and is not network/server load.
6. Stop if latency or service health is affected.

## Reporting
Include the number of trials, baseline timing range, test timing range, controlled delay and limitations. Do not report a single slow request as proof.
