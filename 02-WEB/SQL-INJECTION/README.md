# SQL Injection – Practical VAPT Module

This module is a structured field guide for identifying, validating, documenting and remediating SQL injection in authorised labs and explicitly approved assessments.

## Folder map
- `00-START-HERE/` – workflow and decision tree
- `01-DETECTION/` – parameter discovery, baseline and validation
- `02-INBAND/` – error-based and UNION-based SQLi
- `03-BLIND/` – boolean-based and time-based SQLi
- `04-OUT-OF-BAND/` – OOB concepts and controlled validation
- `05-PAYLOAD-CHEATSHEET/` – context and database reference
- `06-BURP-WORKFLOW/` – Repeater and evidence workflow
- `07-REPORTING/` – finding template and remediation
- `08-PRACTICE/` – lab checklist and learning plan

## The three technique families
1. **In-band:** The same application channel returns useful database errors or query results. Includes error-based and UNION-based techniques.
2. **Blind / inferential:** The application does not directly return query results; the tester infers behaviour from true/false responses or controlled timing differences.
3. **Out-of-band (OOB):** A database/server interaction causes an observable callback through a separate channel. This requires an approved callback service and explicit permission.

## Safety rules
- Use PortSwigger Web Security Academy or another deliberately vulnerable lab for payload practice.
- On a client or interview target, follow the written scope and rules of engagement.
- Use harmless proof-of-concept tests and synthetic/test data.
- Do not dump database contents, enumerate real customer records, modify/delete data, create accounts, or run heavy delay payloads unless explicitly authorised.
- Do not use OOB callbacks to internal, cloud metadata or third-party systems. Use only an assessor-approved callback endpoint.
- Never put real target URLs, credentials, cookies, tokens or evidence in this public learning repository.
- A database error or a single slow response is not proof. Establish repeatable, controlled differences.

## Suggested study order
Read `00-START-HERE/SQLi-Workflow.md`, then practise detection in a PortSwigger lab. Learn error-based and UNION-based concepts, then boolean/time-based blind techniques. Study OOB last.
