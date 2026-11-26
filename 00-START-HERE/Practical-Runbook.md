# Practical Assessment Runbook

## Before testing
- [ ] Read written scope, rules and testing window.
- [ ] Confirm target URLs, IPs, app package, API base URL and environment.
- [ ] Confirm test credentials and user roles.
- [ ] Ask whether automated scanners, scripts, SQLmap, brute-force checks and active scanning are permitted.
- [ ] Confirm prohibited actions, emergency contact, report format and deadline.
- [ ] Create a local evidence folder; do not store target evidence in public GitHub.

## Identify target
- Browser URL: Web track.
- API documentation/JSON endpoints: API track.
- APK/IPA/installed app: Mobile track.
- IP address/range: Infrastructure track.
- Multiple components: map and assess each in scope.

## Testing sequence
1. Understand business purpose, roles and sensitive workflows.
2. Perform reconnaissance and map entry points.
3. Establish normal behaviour with baseline requests.
4. Test systematically using the relevant checklist.
5. Validate suspected issues with minimal, non-destructive proof.
6. Capture sanitised evidence immediately.
7. Remove duplicates and unverified scanner alerts.
8. Prepare report and CISO briefing.

## Stop and ask
Stop if you encounter real customer data, service instability, an out-of-scope asset, irreversible action or a risk to banking operations.
