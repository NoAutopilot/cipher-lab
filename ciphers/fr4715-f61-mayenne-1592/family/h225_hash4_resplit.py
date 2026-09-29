#!/usr/bin/env python3
"""H225 (runner 9 session_012NTadgrCBftz3oRtgw5jFu, 29 Sept 2026), script-only, written before the run. The row's span/overlay gate (H219's design) is a
non-test by construction here: no HASH4 or H24 lies on a known-span line of f.61 or on f.108r's overlay (f.61 L01's one HASH4 is outside the spans), so
no test key that changes only HASH4/H24 can score differently there (CLAUDE.md rule 3, a control that cannot vary). What remains is descriptive: v5's
HASH4 and H24 letter counts per leaf, before and after moving the f.188r rows H224 shape-read as the 2-hook ("2#", D) from HASH4 to H24 (A stays
HASH4; C/N and the untiled rows stay as they are). Reports d/q share of HASH4 and i/x/j/y share of H24 per leaf and pooled. No key change.
  python3 h225_hash4_resplit.py [--check]"""
import csv, os, sys
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def main():
    ans = {r["id"]: r["answer"].strip().upper() for r in rd(f"{P}/h224_reply.tsv")}
    moved = Counter(r["letter"] for r in rd(f"{HERE}/h224_items.tsv") if r["kind"] == "T" and ans.get(r["item"]) == "D")
    cnt = defaultdict(Counter)
    for l in open(f"{HERE}/key_period_v5.tsv"):
        if l.startswith("#") or not l.strip(): continue
        c = l.rstrip("\n").split("\t")
        if c[0] in ("HASH4", "H24") and c[2].isdigit(): cnt[(c[0], c[3])][c[1]] += int(c[2])
    out = [f"f.188r rows H224 read as the 2-hook (moved HASH4 -> H24): {dict(moved)}"]
    def line(tag, C):
        for code, good in (("HASH4", "dq"), ("H24", "ixjy")):
            tot = Counter();
            for (cd, leaf), c in C.items():
                if cd == code: tot += c
            n = sum(v for k, v in tot.items() if k != "-"); g = sum(v for k, v in tot.items() if k in good)
            out.append(f"{tag} {code}: {g}/{n} = {g / max(1, n):.3f} in {'/'.join(good)}  " + " ".join(f"{k}{v}" for k, v in tot.most_common() if k != "-"))
    for leaf in sorted({lf for _, lf in cnt}):
        for code, good in (("HASH4", "dq"), ("H24", "ixjy")):
            c = cnt.get((code, leaf))
            if c: n = sum(v for k, v in c.items() if k != "-"); out.append(f"v5 {code} {leaf}: {sum(v for k, v in c.items() if k in good)}/{n} in {'/'.join(good)}")
    line("v5 pooled", cnt)
    after = defaultdict(Counter, {k: Counter(v) for k, v in cnt.items()}); lf = next(l for _, l in cnt if "188r" in l)
    for k, v in moved.items(): after[("HASH4", lf)][k] -= v; after[("H24", lf)][k] += v
    line("after the H224 re-split, pooled", after)
    c = after[("HASH4", lf)]; n = sum(v for k, v in c.items() if k != "-")
    out.append(f"after, HASH4 f.188r alone: {sum(v for k, v in c.items() if k in 'dq')}/{n} in d/q (v5 {sum(v for k, v in cnt[('HASH4', lf)].items() if k in 'dq')}/{sum(v for k, v in cnt[('HASH4', lf)].items() if k != '-')})")
    out.append("span/overlay gate: non-test by construction (no HASH4/H24 on a span or overlay position); not run")
    txt = "\n".join(out) + "\n"; p = f"{HERE}/h225_hash4_resplit_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()
