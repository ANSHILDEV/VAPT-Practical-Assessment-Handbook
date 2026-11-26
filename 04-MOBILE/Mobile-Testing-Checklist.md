# Mobile Application VAPT Checklist

First confirm Android/iOS, app version, package/bundle ID, test build, test accounts and whether emulator/rooted/jailbroken device and proxying are permitted.

## Static review
- [ ] Permissions appropriate and minimal.
- [ ] No embedded secrets, credentials or private keys.
- [ ] Debug logging/flags disabled in release.
- [ ] Android exported components and deep links protected.
- [ ] Backup and cleartext traffic settings appropriate.
- [ ] Cryptography and key storage use platform protections.
- [ ] WebView settings and JavaScript bridges reviewed.

## Dynamic review
- [ ] Observe app with test account.
- [ ] Inspect network traffic through authorised proxy.
- [ ] Confirm TLS certificate validation.
- [ ] Check sensitive data in logs, clipboard, screenshots, notifications.
- [ ] Review local storage, preferences, databases and cache.
- [ ] Check session expiry/logout, deep links and inter-app communication.
- [ ] Review root/jailbreak behaviour in context.

## Tools
JADX, MobSF, adb, Burp Suite and (only if permitted) Frida. Record device/OS/app version, role, steps and sanitised evidence. Never publish APK/IPA, certificates, tokens or customer data.
