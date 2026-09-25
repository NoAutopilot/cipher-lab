#!/usr/bin/env python3
"""Fetch _djvu.txt for chosen codebook identifiers, once each, to codes/. Writes manifest.json."""
import hashlib
import json
import sys
import time
import urllib.request

UA = "cipher-lab research script (contact via repository)"
OUTDIR = "specs/cheap-tests/lima/codes"

BOOKS = {
    "abc_code": ("abcuniversalcom00clau", "ABC Universal Commercial Electric Telegraphic Code, 1901 (5th ed.)"),
    "western_union": ("WesternUnionTelegraphicCode", "Western Union Telegraphic Code, 1901"),
    "lieber": ("standardtelegrap00liebuoft", "Lieber's Standard Telegraphic Code, 1896"),
    "bentley": ("bentleyscomplete00bentuoft", "Bentley's Complete Phrase Code, 1909 (closest available ed. to 1906)"),
}

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()

def main():
    manifest = []
    for key, (ident, desc) in BOOKS.items():
        url = f"https://archive.org/download/{ident}/{ident}_djvu.txt"
        out_path = f"{OUTDIR}/{key}.txt"
        try:
            data = fetch(url)
        except Exception as e:
            print(f"{key} ({ident}): FETCH ERROR {e}", file=sys.stderr)
            manifest.append({"key": key, "identifier": ident, "desc": desc, "url": url, "error": str(e)})
            time.sleep(1.6)
            continue
        with open(out_path, "wb") as f:
            f.write(data)
        sha1 = hashlib.sha1(data).hexdigest()
        manifest.append({
            "key": key, "identifier": ident, "desc": desc, "url": url,
            "bytes": len(data), "sha1": sha1, "local": out_path,
        })
        print(f"{key} ({ident}): {len(data)} bytes -> {out_path}")
        time.sleep(1.6)
    with open(f"{OUTDIR}/manifest.json", "w") as f:
        json.dump(manifest, f, indent=1)

if __name__ == "__main__":
    main()
