#!/usr/bin/env python3
"""H179 (runner 6, 28 Sept 2026; pre-registered here before the run): a TEST key, not v4 and not a merge -- key v4's rows with the
classes that fr.3984 f.176r/fol. 177r decides (H177b stage 2a, build_f176_key_result.txt) narrowed to f.176r's letters: VBAR_A {t, g},
EBR (EBR, EBR_A, EBR_B) {l}, 4STEM {p, c}, HASH4 {d, q}; a decided letter with no v4 row takes f.176r's row. Then
test_period_key.py --key key_period_v4n176.tsv --collapse-ebr --min 2 --frac 0.1 --sbs --perms 200 on Tomokiyo's 55 known letters
of f.61 (v4: 48/55). Reading: the narrowing can only remove letters from the tested cells, so a count >= 48 means f.176r's choice is
consistent with Tomokiyo's letters on f.61 wherever those cells occur; each lost letter is listed as a contradiction.
  python3 narrow_v4_f176.py"""
import csv, os
HERE = os.path.dirname(os.path.abspath(__file__))
KEEP = {"VBAR_A": {"t", "g"}, "EBR": {"l"}, "EBR_A": {"l"}, "EBR_B": {"l"}, "4STEM": {"p", "c"}, "HASH4": {"d", "q"}}
src = [l for l in open(f"{HERE}/key_period_v4.tsv")]
hdr = [l for l in src if l.startswith("#")]; rows = list(csv.DictReader((l for l in src if not l.startswith("#")), delimiter="\t"))
out = [r for r in rows if r["class"] not in KEEP or r["letter"] in KEEP[r["class"]]]
f176 = list(csv.DictReader((l for l in open(f"{HERE}/key_period_f176.tsv") if not l.startswith("#")), delimiter="\t"))
for c, lets in KEEP.items():
    for x in lets:
        if not any(r["class"] == c and r["letter"] == x for r in out):
            out += [r for r in f176 if r["class"] == c and r["letter"] == x]
with open(f"{HERE}/key_period_v4n176.tsv", "w") as f:
    f.write("# key_period_v4n176.tsv -- H179 TEST key (runner 6): key v4 narrowed on VBAR_A/EBR/4STEM/HASH4 to fr.3984 f.176r's letters; NOT v4, NOT merged\n")
    w = csv.DictWriter(f, fieldnames=["class", "letter", "n", "leaf", "bands"], delimiter="\t", extrasaction="ignore"); w.writeheader(); w.writerows(out)
print(len(rows), "v4 rows ->", len(out), "test rows")
