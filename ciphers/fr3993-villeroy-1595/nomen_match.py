#!/usr/bin/env python3
"""VILL-NOMEN (3 Oct 2026, fr3995/PREREG-VILL-NOMEN.md): count the target's adjacent figure pairs ('o' = 0) that form a code
of the f159 nomenclator (keys/key_f159_nomen.tsv, codes agreed by both readers; 50/51 and 60/61 disputed, left out), against
200 random two-figure code sets of the same size disjoint from it (10-99). Also counts target K (= Nulles N3, certified by
both readers). An observation, not a gate. Usage: python3 nomen_match.py [--check]  (writes nomen_match.tsv)"""
import sys, random
from pathlib import Path
HERE = Path(__file__).resolve().parent
DIG = set("0123456789o")

def target_lines():
    out = []
    for f in ("bourdeau/ct_f148r.txt", "bourdeau/ct_f148v_149r.txt"):
        for l in open(HERE / f):
            if l.startswith("#") or not l.strip(): continue
            out.append(l.split())
    return out

def pairs(lines):
    ps = []
    for t in lines:
        for a, b in zip(t, t[1:]):
            if a in DIG and b in DIG: ps.append((a + b).replace("o", "0"))
    return ps

def main():
    codes = set()
    for l in open(HERE / "keys/key_f159_nomen.tsv"):
        if l.startswith("#") or not l.strip(): continue
        c = l.split("\t")[0]
        if c.isdigit() and len(c) == 2: codes.add(c)
    lines = target_lines(); ps = pairs(lines); ntok = sum(len(t) for t in lines)
    hit = sum(p in codes for p in ps)
    rnd = random.Random(1); pool = [f"{i}" for i in range(10, 100) if f"{i}" not in codes]
    null = sorted(sum(p in s for p in ps) for s in (set(rnd.sample(pool, min(len(codes), len(pool)))) for _ in range(200)))
    mean = sum(null) / len(null); p95 = null[int(0.95 * len(null)) - 1]
    nK = sum(t.count("K") for t in lines)
    out = ("codes_agreed\ttarget_tokens\tadjacent_figure_pairs\tpairs_in_code_set\tnull_mean\tnull_p95\ttarget_K_tokens\n"
           f"{len(codes)}\t{ntok}\t{len(ps)}\t{hit}\t{mean:.1f}\t{p95}\t{nK}\n")
    f = HERE / "nomen_match.tsv"
    if "--check" in sys.argv: sys.exit(0 if f.exists() and f.read_text() == out else 1)
    f.write_text(out); print(out)

if __name__ == "__main__":
    main()
