#!/usr/bin/env python3
"""AUD2D-OLD2442 (8 Oct 2026): longest H/C/S stretch per block in consecutive digit tokens (cipher = digits 2,3,4,7,8;
an M or I word breaks the stretch; a word with no digit neither adds nor breaks), plus digit-token and word-token grade
shares. Usage: python3 aud2d_runs.py  (reads ../reading_tokens.tsv)"""
import csv
from collections import Counter
from pathlib import Path
T = Path(__file__).resolve().parents[1] / "reading_tokens.tsv"
rows = list(csv.DictReader(open(T, encoding="utf-8"), delimiter="\t"))
for b in ("B", "C1"):
    r = [x for x in rows if x["block"] == b]
    wg = Counter(x["grade"] for x in r)
    dg = Counter(); best = (0, None, None); cur = 0; start = None
    for x in r:
        n = sum(c in "23478" for c in x["raw_used"])
        dg[x["grade"]] += n
        if x["grade"] in "HCS":
            if n and cur == 0:
                start = x["token_index"]
            cur += n
            if cur > best[0]:
                best = (cur, start, x["token_index"])
        else:
            cur = 0
    nd = sum(dg.values()); hcs = sum(dg[g] for g in "HCS")
    span = [x["value"] for x in r if best[1] and int(best[1]) <= int(x["token_index"]) <= int(best[2])]
    print(f"{b}: words {len(r)} {dict(wg)} word-share HCS {sum(wg[g] for g in 'HCS')/len(r):.1%}; "
          f"digits {nd} {dict(dg)} digit-share HCS {hcs/nd:.1%}")
    print(f"  longest H/C/S stretch: {best[0]} digit tokens, words {b}{best[1]}-{b}{best[2]}: {' '.join(span)}")
