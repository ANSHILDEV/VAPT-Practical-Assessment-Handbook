# Nmap Quick Reference

Only scan authorised targets and approved ports:
```bash
nmap -sn <authorised-CIDR>
nmap -sT -p 22,80,443 <authorised-host>
nmap -sT -sV -p <approved-ports> <authorised-host>
nmap -sT -sV -p <approved-ports> -oN evidence-nmap.txt <authorised-host>
```
Avoid aggressive/full-port/UDP scans and NSE vulnerability scripts unless rules explicitly permit them. Verify findings before reporting.
