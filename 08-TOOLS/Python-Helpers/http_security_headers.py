#!/usr/bin/env python3
"""Fetch headers from one explicitly authorised URL; no crawling or fuzzing."""
import argparse
import requests

def main():
    p = argparse.ArgumentParser()
    p.add_argument("url")
    p.add_argument("--timeout", type=int, default=10)
    a = p.parse_args()
    if not a.url.startswith(("http://", "https://")):
        p.error("URL must begin with http:// or https://")
    try:
        r = requests.get(a.url, timeout=a.timeout, allow_redirects=False)
    except requests.RequestException as e:
        raise SystemExit(f"Request failed: {e}")
    print(f"Status: {r.status_code}")
    for h in ["Strict-Transport-Security", "Content-Security-Policy",
              "X-Content-Type-Options", "X-Frame-Options", "Referrer-Policy",
              "Permissions-Policy", "Cache-Control", "Access-Control-Allow-Origin",
              "Access-Control-Allow-Credentials", "Location"]:
        print(f"{h}: {r.headers.get(h, '[not present]')}")

if __name__ == "__main__":
    main()
