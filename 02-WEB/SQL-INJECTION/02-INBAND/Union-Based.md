# UNION-Based SQL Injection

## Concept
A UNION operation combines rows from compatible SELECT statements. For a UNION to work, the SELECT statements generally need compatible column counts and data types.

## Safe lab workflow
1. Use a PortSwigger or intentionally vulnerable lab.
2. Capture the normal request and move it to Repeater.
3. Identify whether the candidate input is numeric or string-based.
4. In the lab, determine the compatible column count using the lab's guided method.
5. Identify a response position that displays a harmless marker.
6. Confirm the marker is caused by the input.
7. Do not enumerate schemas or extract user data on a client/interview target unless the written scope explicitly requires and permits it.

## Conceptual lab markers
```text
' UNION SELECT NULL--
' UNION SELECT 'marker',NULL--
```
These examples are context-dependent and may require a different number/type of columns, comment syntax or quote closure. Use only in a lab.

## Report evidence
Baseline request, test request, response containing the harmless marker, exact parameter and reproduction steps.
