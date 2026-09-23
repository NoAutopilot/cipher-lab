#!/usr/bin/env python3
"""Borrow one lending-only Internet Archive item for a named page check, save the requested pages, return
the loan. Reads IA_USER and IA_PASS from the environment (never prints them).

  python3 tools/ia_borrow.py IDENTIFIER --pages 68-74 --out ciphers/<target>/images/

One book at a time, for one named check, returned when done -- never bulk (Access playbook rule).

IMPORTANT, confirmed 20 Sept 2026: archive.org login requires an email address. IA_USER must contain
one ("user@example.com"), not a screen name. A screen-name-shaped IA_USER fails both routes tried this
session: the login API (https://archive.org/services/xauthn/?op=login) returns
{"success": false, "values": {"reason": "account_not_found"}}, and the current archive.org login page
(https://archive.org/login, a JS app) renders only an "Email address" field, no username field.

UPDATE, confirmed 21 Sept 2026: the person rotated IA_USER to an email-format value and the password.
Login STILL fails with the same {"success": false, "values": {"reason": "account_not_found"}} from
POST https://archive.org/services/xauthn/?op=login (HTTP 401) -- this is no longer the format problem
above; archive.org reports no account under that email at all. Possible causes not distinguished this
session: the email is mistyped, the intended archive.org account is registered under a different email,
or the account only supports sign-in-with-Google (no password login via xauthn for such accounts). Do
not retry this pair again without the person confirming which archive.org account IA_USER/IA_PASS should
reach -- xauthn rate-limits/locks out repeated failed logins. One attempt was made this session, per the
no-repeat-retry rule in the Access playbook; flagged in ROOM.md and ASKS.md.

UPDATE, 23 Sept 2026 (credential session, ytbiz account): login now succeeds (the person registered the
account), and steps 2 and 4 work as written: `browse_book` returns {"success": true} and opens a one-hour
SESSION_LOAN, `return_loan` returns it. Step 3 needed three changes, now in the code below: (a) the
`loan-<identifier>` cookie, whose value comes from POST /services/loans/loan/ action=create_token (needs
Origin and Referer headers, else HTTP 400); (b) the image host is the `server` field of /metadata/<id>
(ia8xxxxx), not the host in the BookReaderJSIA `uri` (ia6xxxxx), which answered 404 "Image error: not
found" for every leaf; (c) a Referer header on the image request. With those, BookReaderImages.php
answers 200 image/jpeg. BUT for a lending item (`lendingInfo.shouldProtectImages` true) the body is not a
JPEG: archive.org serves the leaf obfuscated for its own web reader (an `X-Obfuscate` header, no JPEG
markers anywhere in the payload). Decoding that outside the reader is circumventing the lending protection
and is not done here: this script now stops and reports when it sees a protected payload. So for
controlled-digital-lending items the loan can be held from a script, but the pages must be read by the
person in the archive.org reader (or through search-inside snippets, be-api, which need no login). Open
items are served as ordinary JPEGs by the same endpoint and this script reads them, but those need no
loan in the first place.

There is no official Python client for the lending/BookReader system (the `internetarchive` PyPI
package covers uploads/downloads/search of open items only), so this script speaks the same raw HTTP
endpoints archive.org's own web reader uses:
  1. POST https://archive.org/services/xauthn/?op=login  (email, password) -> logged-in-user/-sig cookies
  2. POST https://archive.org/services/loans/loan/  action=browse_book, identifier=IDENTIFIER
  3. GET  https://{server}/BookReader/BookReaderJSIA.php?id=...&itemPath=...&server=...&format=json
     while the loan is active, for the per-leaf image URLs, then fetch the leaves in --pages
  4. POST https://archive.org/services/loans/loan/  action=return_loan, identifier=IDENTIFIER (always,
     even on error)

Steps 1-2 and 4 were exercised on 20 and 21 Sept 2026 and their request shapes are as tested; step 1 has
now failed on two different accounts/credential shapes (bad format, then account_not_found), so step 2
has still never received a successful login to run against, and step 3's exact response shape remains
UNVERIFIED -- confirm it against a real loan before trusting the image URLs it returns.
"""
import argparse
import os
import re
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

def create_token(session, identifier):
    """Loan token for the loan-<identifier> cookie the image server checks (renewed by the web reader
    every couple of minutes; one token is enough for a short page check)."""
    r = session.post("https://archive.org/services/loans/loan/",
                      data={"action": "create_token", "identifier": identifier},
                      headers={"Referer": f"https://archive.org/details/{identifier}",
                               "Origin": "https://archive.org"}, timeout=30)
    try:
        j = r.json()
    except ValueError:
        die(f"create_token failed ({r.status_code})")
    if not j.get("success") or not j.get("token"):
        die(f"create_token failed ({r.status_code}): {j.get('error', '')}")
    session.cookies.set(f"loan-{identifier}", j["token"], domain=".archive.org", path="/")

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

        time.sleep(1.5)
        create_token(session, args.identifier)
        time.sleep(1.5)
        server, path = get_item_server_path(args.identifier)
        time.sleep(1.5)
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
            # Use the metadata server (ia8...) for the image host; the uri's own host (ia6...) 404s.
            img_url = re.sub(r"^https?://[^/]+", f"https://{server}", flat[leaf_num]["uri"])
            if "scale=" not in img_url:
                img_url += "&scale=2&rotate=0"
            time.sleep(1.5)
            img = session.get(img_url, timeout=60,
                              headers={"Referer": f"https://archive.org/details/{args.identifier}"})
            if img.headers.get("X-Obfuscate") or not img.content.startswith(b"\xff\xd8"):
                print(f"leaf {leaf_num}: served protected (obfuscated for the archive.org reader, "
                      f"status {img.status_code}, {len(img.content)} bytes); not saved. Read this item in "
                      f"the reader as the person, or use search-inside snippets.", file=sys.stderr)
                break
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
