#!/usr/bin/env python3
"""H288 (runner 10 session_0148wt8Aokh6aZEdJsXzYiZX, 29 Sept 2026), script-only. H283/H286: on f.61 the signs LOOPSTEM1 and CH stand where French wants a
noun and a verb ('que les [ ] [ ] trop avancees'). On the glossed family leaves, do the same two classes ever take a whole word in the period gloss?
From the alignment outputs family/passes/{{f101r,f188r,f108vg,f106r,f124r,f274}}_align.tsv (tools/interlinear_align.py: plain_chunk per token), the
distribution of plain_chunk length (0 = null-or-unaligned, 1 = a letter, 2+ = a word) for LOOPSTEM1 and CH, beside the same distribution for every class
(the baseline that says whether the aligner emits 2+ chunks at all -- if it never does, this is a non-test by construction, rule 3).
Descriptive.  python3 h288_wordcode_family.py [--check]"""
import csv, os, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"
def band(ch): return "0" if not ch else ("1" if len(ch) == 1 else "2+")
rows = []; tot_t = Counter(); tot_all = Counter()
for f in ("f101r_align.tsv", "f188r_align.tsv", "f108vg_align.tsv", "f106r_align.tsv", "f124r_align.tsv", "f274_align.tsv"):
    if not os.path.exists(f"{P}/{f}"): continue
    d = list(csv.DictReader(open(f"{P}/{f}"), delimiter="\t")); t = Counter(); a = Counter(); ex = []
    for r in d:
        b = band(r.get("plain_chunk", "")); a[b] += 1
        if r.get("value") in ("LOOPSTEM1", "CH"): t[(r["value"], b)] += 1; ex.append(f"{r['value']}:{r.get('plain_chunk') or '-'}")
    tot_all.update(a); tot_t.update(t)
    rows.append(f"{f}: all classes 0/1/2+ = {a['0']}/{a['1']}/{a['2+']}; LOOPSTEM1 0/1/2+ = {t[('LOOPSTEM1','0')]}/{t[('LOOPSTEM1','1')]}/{t[('LOOPSTEM1','2+')]}; CH = {t[('CH','0')]}/{t[('CH','1')]}/{t[('CH','2+')]}" + (f"; chunks {' '.join(ex)}" if ex else ""))
rows.append(f"pooled: all classes 2+ chunks {tot_all['2+']} of {sum(tot_all.values())}; LOOPSTEM1/CH 2+ chunks {tot_t[('LOOPSTEM1','2+')] + tot_t[('CH','2+')]} of {sum(tot_t.values())}")
rows.append("read-out: " + ("NON-TEST by construction: the aligner never emits a chunk of 2+ letters for any class" if tot_all['2+'] == 0 else ("LOOPSTEM1/CH take a word somewhere in the family" if tot_t[('LOOPSTEM1','2+')] + tot_t[('CH','2+')] else "LOOPSTEM1/CH take single letters or nothing everywhere in the family")))
out = "\n".join(rows) + "\n"; p = f"{HERE}/h288_wordcode_family_result.txt"
if "--check" in sys.argv:
    ok = os.path.exists(p) and open(p).read() == out; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(p, "w").write(out); print(out, end="")
