# VAPT Practical Assessment Handbook

A field handbook for authorised web, API, mobile and infrastructure assessments.

## Workflow
1. Read `00-START-HERE/Practical-Runbook.md`.
2. Complete `00-START-HERE/Scope-and-Rules.md`.
3. Select the relevant Web, API, Mobile or Infrastructure checklist.
4. Record evidence using `06-EVIDENCE/Evidence-Log.md`.
5. Write confirmed findings using `07-REPORTING/Finding-Template.md`.
6. Complete the report and CISO briefing.

## Contents
- `00-START-HERE/` – scope, runbook, time management and target selection
- `01-UNIVERSAL/` – universal VAPT checklist
- `02-WEB/` – web testing and common vulnerabilities
- `03-API/` – API, JWT and OAuth testing
- `04-MOBILE/` – Android/iOS assessment
- `05-INFRASTRUCTURE/` – network and TLS checks
- `06-EVIDENCE/` – evidence handling
- `07-REPORTING/` – report, severity and CISO briefing
- `08-TOOLS/` – Burp, Nmap and Python helpers
- `09-REFERENCE/` – safe test patterns and glossary

## Safety
Only test assets explicitly in written scope. Confirm whether scanners, scripts, fuzzing and active scanning are allowed. Do not perform DoS, brute force, destructive actions, bulk extraction or out-of-scope testing. Use test accounts and synthetic data. Never commit client evidence, credentials, tokens, keys or personal data to public GitHub. Create a private repository first.
