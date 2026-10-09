#!/usr/bin/env python3
"""FM-R3c: re-run FM-PRE's share scorer from HEAD (fm_entries.build()) on the FM-R3c rows, print the three shares,
and write fm_r3c_entries.txt (### F<n> | row | ...; entry lines) for the book-per-entry step (fm_r3c.py)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fm_entries
ROWS = ["5839/2","5734/2","5736/1","5760/0","5683/0","5831/2","5670/1","5729/1","5837/1","5837/0"]
codes, ents = fm_entries.build()
idx = {f"{e['pointer']}/{e['entry_on_page']}": e for e in ents}
out = []
for i, r in enumerate(ROWS, 1):
    e = idx.get(r)
    if not e: print(r, "NOT FOUND"); continue
    print(f"{r} date={e['date']} dir={e['direction']} words={e['words']} s1/s2/s9={e['s1']}/{e['s2']}/{e['s9']} share_book={e['share_book']} best_book={e['best_book']} cont={e['cont']} hdr={e['header']!r}")
    out.append(f"### F{i} | row {r} | FM-R3c, mssEC 25 / obj 5952, pointer {e['pointer']} | {e['header']}\n" + "\n".join(e["lines"]) + "\n")
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fm_r3c_entries.txt"), "w").write("\n".join(out))
