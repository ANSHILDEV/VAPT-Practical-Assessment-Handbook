# Error-Based SQL Injection

## Concept
An input changes SQL syntax or type handling and the database error is exposed to the user or observable in application behaviour.

## Lab-only starter probes
Try one at a time in a deliberately vulnerable lab and adapt to the input context:
```text
'
"
`
')
")
```

These are syntax probes, not universal exploit payloads. A secure application may safely handle them without an error.

## What to inspect
- Does the response contain a database product/error signature?
- Does the error occur only for the altered parameter?
- Is the response repeatable?
- Does the application suppress details but still show a consistent query-dependent difference?

## Avoid
Do not use error functions to extract database contents from a real target. Do not intentionally crash or overload the database.

## Reporting
State whether the database error itself was exposed, whether query manipulation was confirmed, and what impact was demonstrated.
