#!/usr/bin/env python3
"""Locate headwords in full-view Google Books volumes by printed page number.

Uses the undocumented search-within-volume JSON endpoint
(books.google.com/books?id=ID&q=WORD&jscmd=SearchWithinVolume2), which works from a
plain curl with a browser User-Agent even where the Books API returns 429 and the
page-text view 403. Prints, for each volume id and word, the list of (printed page
number or Google page id, snippet start). Only "page_number" values are printed
page numbers; a "PPnn"/"PTnn" id is the scan sequence, not the printed page.

Usage: gbooks_search_within.py ID[,ID...] word [word ...]
Written 19 Sept 2026 for ciphers/wellington-maitland-1812 (dictionary-code edition search).
"""
import json, subprocess, sys, time

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"


def search_within(vid, word):
    url = f"https://books.google.com/books?id={vid}&q={word}&jscmd=SearchWithinVolume2"
    out = subprocess.run(["curl", "-sS", "-A", UA, url], capture_output=True, text=True).stdout
    try:
        d = json.loads(out)
    except ValueError:
        return None
    return [(r.get("page_number") or r.get("page_id"), r.get("snippet_text", "")[:60].replace("\n", " "))
            for r in d.get("search_results", [])]


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    words = sys.argv[2:]
    for vid in sys.argv[1].split(","):
        print("=====", vid)
        for w in words:
            r = search_within(vid, w)
            print(f"  {w:12s}", r if r is not None else "ERR/blocked")
            time.sleep(0.5)


if __name__ == "__main__":
    main()
