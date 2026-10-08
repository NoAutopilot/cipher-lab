#!/usr/bin/env python3
"""LS-R6 step 2 (8 Oct 2026): does Cipher No. 1 (key.md) still read the 1865 rows of mssEC 19?

Share of non-function tokens (volunteer text, entries_mssEC19 segmentation) found in key.md's code-word column, for every
priority-1 1865 row with words >= 40, against the read 1864 entries E21-E54 (control, same tokenisation). Script only."""
import csv, statistics, sys, re
import entries_mssEC19 as m
m.load_vocab()
K1 = m.K1 - m.FW
pages = m.load_pages()
ents = {(e["pointer"], e["entry_on_page"]): e for e in m.segment(pages)}
rows = list(csv.DictReader((l for l in open("entries-mssEC19.tsv") if not l.startswith("#")), delimiter="\t"))
first65 = min(int(r["pointer"]) for r in rows if "1865" in r["header"])
def share(r):
    e = ents.get((int(r["pointer"]), int(r["entry_on_page"])))
    if not e: return None
    t = [w for w in m.toks(" ".join(e["lines"])) if w not in m.FW and len(w) > 1]
    return (sum(1 for w in t if w in K1) / len(t), len(t)) if t else None
def dist(label, rs):
    v = [s[0] for s in map(share, rs) if s]
    v.sort()
    p10 = v[max(0, int(0.1 * len(v)))] if v else float("nan")
    print(f"{label}\tn={len(v)}\tmedian={statistics.median(v):.3f}\tp10={p10:.3f}")
    return statistics.median(v)
p1 = [r for r in rows if r["priority"] == "1" and int(r["words"]) >= 40 and int(r["pointer"]) >= first65 - 0]
y65 = [r for r in p1 if "1864" not in r["header"]]
ctrl = [r for r in rows if re.search(r"\bE(2[1-9]|3\d|4\d|5[0-4])\b(?! \(run-on)", r["already_read"] or "")]
print("first pointer with 1865 in header:", first65)
a = dist("1865 priority-1 words>=40", y65)
b = dist("control E21-E54 (read 1864)", ctrl)
dist("  of which cipher_guess=1", [r for r in y65 if r["cipher_guess"]=="1"])
print("verdict:", "No. 1 reads 1865 rows" if abs(a - b) <= 0.1 else "No. 1 does not read 1865 rows (Nos. 3/4 not in hand)", f"(diff {a-b:+.3f})")
