# Infrastructure VAPT Checklist

## Scope
Confirm exact IPs/CIDRs, hostnames, allowed ports, UDP permission, scan window and production restrictions.

## Low-impact discovery examples
Only within authorised scope:
```bash
nmap -sn <authorised-CIDR>
nmap -sT -sV --top-ports 100 <authorised-host>
nmap -sT -sV -p <approved-ports> -oN evidence-nmap.txt <authorised-host>
```
Use approved port lists. Avoid aggressive/full-port/UDP scans and NSE vulnerability scripts unless explicitly permitted.

## Service review
- [ ] Exposed services have a business need.
- [ ] Unnecessary ports/services identified.
- [ ] Service versions verified; banners can mislead.
- [ ] TLS certificates/protocols reviewed.
- [ ] Admin interfaces restricted.
- [ ] SSH/RDP/SMB/database/web services reviewed if in scope.

Record host, port, protocol, service, evidence, exposure and remediation. Do not claim a CVE from a banner alone.
