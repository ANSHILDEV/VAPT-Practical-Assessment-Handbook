# Baseline and Validation

## Baseline fields
- Request method and endpoint
- Parameter and original value
- Authenticated role
- HTTP status
- Response length
- Key response text
- Approximate response time
- Any redirect or application state change

## Controlled comparisons
Compare:
- Original input vs harmless altered input.
- A condition expected to be true vs a condition expected to be false.
- Repeated normal requests vs repeated test requests.
- Similar requests under the same account and session.

## Strong indicators
- Repeatable database syntax error associated with the tested input.
- Consistent true/false response difference tied to the condition.
- Repeatable time difference that tracks the controlled condition.
- In a lab, controlled query output reflected in the response.

## Weak indicators / false positives
- One HTTP 500 response.
- One slow request.
- WAF block page.
- Different response caused by expired session, cache or business logic.
- Error message not demonstrably related to database processing.

A finding requires repeatability and a defensible link between input and database query behaviour.
