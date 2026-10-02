#!/usr/bin/env python3
"""A2-HDK3, 2 Oct 2026: write ../key.tsv from HCPortal key 255's letter table (HStAM 4 d Nr. 1234 f.13, endorsed
'Clavis ... mit Secretario Lincker 1666'), reusing the table already typed in key255_gloss_test.py (one source of truth).
Grade S: a key of the same office, tested against the letter's own gloss with a relabelled-table control
(NOTES 'Known-keys and sibling check' step 5); not H until a reconciled transcription confirms 1672 used the 1666 table.
Rows: 120 letter homophones, 24 doubled-letter codes, nulls ('Blinde Zahlen') as the key lists them. The key lists
'1 biss 20' as nulls, but its own table gives 20 = A, and the letter's gloss reads 20 as A three times: 20 is kept as A
(note column) and nulls run 1-19. The syllable row (au eu ei ... tz) is written in symbols, not codes: not in key.tsv.
20 = A is also what the period decipher scale for this key (DECODE 4690 P2) gives ('20 a').
The nomenclator 180-407 is left out (it does not read the letter's 3-digit groups). --check: exit 1 if key.tsv is stale."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__)); sys.argv_saved = sys.argv; sys.argv = [sys.argv[0], "--quiet"]
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    import key255_gloss_test as g
sys.argv = sys.argv_saved
SRC = "HCPortal key 255 f.13 (keys/hcportal_key255_0013.jpg)"
rows = [("code", "value", "grade", "source", "note")]
for lab in g.L:
    for n in g.NUM[lab]:
        note = "key also lists 1-20 as nulls; kept as A (table, and gloss 3x)" if n == 20 else ""
        rows.append((str(n), lab.lower(), "S", SRC, note))
for lab in g.L:
    rows.append((g.DBL[lab], lab.lower(), "S", SRC, "doubled-letter row, shifted by two"))
nulls = list(dict.fromkeys(list(range(1, 20)) + [121, 131, 141, 151, 161, 171] + list(range(123, 140, 2)) + list(range(143, 170, 2)) + [173, 175, 177, 178, 179]))  # the key lists 131, 151, 161 once; the odd runs repeat them
for n in nulls:
    rows.append((str(n), "NULL", "S", SRC, "Blinde Zahlen"))
# 128, 148, 158: no letter in key 255's table and not in its null list; the period decipher scale in DECODE 4690
# ('Scala ... mit Secretarium Linckern', A2-HDK3) marks each '-' (no value). Added as NULL from that witness only.
for n in (128, 148, 158):
    rows.append((str(n), "NULL", "S", "DECODE 4690 P2 scale", "dash in the Lincker decipher scale; not on key 255 f.13"))
codes = [r[0] for r in rows[1:]]
assert len(codes) == len(set(codes)), "duplicate code"
text = "".join("\t".join(r) + "\n" for r in rows)
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "key.tsv")
if "--check" in sys.argv:
    ok = os.path.exists(out) and open(out).read() == text
    print("key.tsv", "up to date" if ok else "STALE"); sys.exit(0 if ok else 1)
open(out, "w").write(text); print(f"wrote key.tsv: {len(rows)-1} rows ({len(nulls)} nulls)")
