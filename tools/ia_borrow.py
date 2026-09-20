#!/usr/bin/env python3
"""Borrow one lending-only Internet Archive item for a named page check, save the requested pages, return
the loan. Reads IA_USER and IA_PASS from the environment (never prints them).

  python3 tools/ia_borrow.py IDENTIFIER --pages 68-74 --out ciphers/<target>/images/

One book at a time, for one named check, returned when done -- never bulk (Access playbook rule).

IMPORTANT, confirmed 20 Sept 2026: archive.org login requires an email address. IA_USER must contain
one ("user@example.com"), not a screen name. A screen-name-shaped IA_USER fails both routes tried this
session: the login API (https://archive.org/services/xauthn/?op=login) returns
{"success": false, "values": {"reason": "account_not_found"}}, and the current archive.org login page
(https://archive.org/login, a JS app) renders only an "Email address" field, no username field. Do not
substitute a guessed email for IA_USER -- get the correct value from the person.

There is no official Python client for the lending/BookReader system (the `internetarchive` PyPI
package covers uploads/downloads/search of open items only), so this script speaks the same raw HTTP
endpoints archive.org's own web reader uses:
  1. POST https://archive.org/services/xauthn/?op=login  (email, password) -> logged-in-user/-sig cookies
  2. POST https://archive.org/services/loans/loan/  action=browse_book, identifier=IDENTIFIER
  3. GET  https://{server}/BookReader/BookReaderJSIA.php?id=...&itemPath=...&server=...&format=json
     while the loan is active, for the per-leaf image URLs, then fetch the leaves in --pages
  4. POST https://archive.org/services/loans/loan/  action=return_loan, identifier=IDENTIFIER (always,
     even on error)

Steps 1-2 and 4 were exercised this session (20 Sept 2026) and their request shapes are as tested; step 2
returned {"error": "Not logged in."} because step 1 could not complete without a valid email IA_USER, so
step 3's exact response shape is NOT verified this session -- confirm it against a real loan before
trusting the image URLs it returns.
"""
import argparse
import os
import sys
import time

import requests

def die(msg):
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(1)

def login(session, email, password):
    r = session.post("https://archive.org/services/xauthn/", params={"op": "login"},
                      data={"email": email, "password": password}, timeout=30)
    time.sleep(2)  # archive.org rate-limits rapid login attempts
    j = r.json()
    if not j.get("success"):
        reason = j.get("values", {}).get("reason", j.get("error", "unknown"))
        die(f"login failed: {reason}")
    session.cookies.update({
        "logged-in-user": j["values"]["cookies"]["logged-in-user"],
        "logged-in-sig": j["values"]["cookies"]["logged-in-sig"],
    })

def browse_book(session, identifier):
    r = session.post("https://archive.org/services/loans/loan/",
                      data={"action": "browse_book", "identifier": identifier},
                      headers={"Referer": f"https://archive.org/details/{identifier}"}, timeout=30)
    if r.status_code != 200:
        die(f"borrow failed ({r.status_code}): {r.text[:300]}")
    return r.json()

def return_loan(session, identifier):
    r = session.post("https://archive.org/services/loans/loan/",
                      data={"action": "return_loan", "identifier": identifier},
                      headers={"Referer": f"https://archive.org/details/{identifier}"}, timeout=30)
    return r.status_code == 200

def get_item_server_path(identifier):
    r = requests.get(f"https://archive.org/metadata/{identifier}", timeout=30)
    d = r.json()
    return d["server"], d["dir"]

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("identifier", help="IA item identifier")
    ap.add_argument("--pages", required=True, help="leaf range, e.g. 68-74 or a single leaf number")
    ap.add_argument("--out", default=".", help="output directory for saved page images")
    args = ap.parse_args()

    user = os.environ.get("IA_USER")
    pw = os.environ.get("IA_PASS")
    if not user or not pw:
        die("IA_USER/IA_PASS not set in the environment")
    if "@" not in user:
        die("IA_USER is not an email address; see the module docstring. Not attempting login.")

    lo, _, hi = args.pages.partition("-")
    lo = int(lo)
    hi = int(hi) if hi else lo

    session = requests.Session()
    session.headers["User-Agent"] = "Mozilla/5.0 (cipher-lab access worker)"
    login(session, user, pw)
    print("login: ok")

    loaned = False
    try:
        browse_book(session, args.identifier)
        loaned = True
        print(f"borrowed: {args.identifier}")

        server, path = get_item_server_path(args.identifier)
        r = session.get(f"https://{server}/BookReader/BookReaderJSIA.php",
                         params={"id": args.identifier, "itemPath": path, "server": server,
                                  "format": "json", "requestUri": f"/details/{args.identifier}"},
                         timeout=30)
        manifest = r.json()
        leaf_urls = manifest.get("data", {}).get("brOptions", {}).get("data", [])
        flat = [leaf for row in leaf_urls for leaf in row]

        os.makedirs(args.out, exist_ok=True)
        for leaf_num in range(lo, hi + 1):
            if leaf_num >= len(flat):
                print(f"warning: leaf {leaf_num} out of range ({len(flat)} leaves in manifest)",
                      file=sys.stderr)
                continue
            img_url = flat[leaf_num]["uri"]
            img = session.get(img_url, timeout=60)
            out_path = os.path.join(args.out, f"{args.identifier}_leaf{leaf_num:04d}.jpg")
            with open(out_path, "wb") as f:
                f.write(img.content)
            print(f"saved: {out_path}")
    finally:
        if loaned:
            ok = return_loan(session, args.identifier)
            print("loan returned" if ok else
                  f"warning: return_loan may have failed, check https://archive.org/details/{args.identifier}")

if __name__ == "__main__":
    main()
