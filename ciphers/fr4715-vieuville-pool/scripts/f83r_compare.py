#!/usr/bin/env python3
"""PREREG7 (GAPS96, 3 Oct 2026): blind read of f.83r top block vs Tomokiyo no.60 DUMP.

usage: f83r_compare.py BLIND_TSV   (one group per line in column 'group'; '?' = unreadable)
Exit 0 PASS, 2 FAIL, 4 NON-TEST. Written before the vision call; see witness/no60/PREREG7_f83r.md.
"""
import csv, random, re, sys, html
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "sources/cryptiana/web/bnf4715.htm"


def dump(anchor, nxt):
    t = SRC.read_bytes().decode("cp932", "replace")
    s = t[t.find(f'<A NAME="{anchor}">'):t.find(f'<A NAME="{nxt}">')]
    s = s[s.find("DUMP"):]
    s = re.sub(r"<[^>]+>", " ", html.unescape(s))
    s = re.sub(r"\([^)]*\)", " ", s)          # drop Tomokiyo's (plaintext) glosses
    out = []
    for tok in s.split():
        tok = tok.strip("'~*[]x").replace("[", "").replace("]", "")
        if tok == "DUMP" or tok.startswith("..."):
            continue
        m = re.match(r"\d+", tok)
        if tok == "▽":
            out.append(tok)
        elif m:
            out.append(m.group(0))
    return out


def norm(g):
    g = g.strip()
    if g in ("?", ""):
        return None
    d = re.sub(r"[^0-9]", "", g)
    return d or None


def lcs(a, b):
    prev = [0] * (len(b) + 1)
    for x in a:
        cur = [0]
        for j, y in enumerate(b):
            cur.append(prev[j] + 1 if (x is not None and x == y) else max(prev[j + 1], cur[j]))
        prev = cur
    return prev[-1]


def main():
    rows = list(csv.DictReader(open(sys.argv[1]), delimiter="\t"))
    B = [norm(r["group"]) for r in rows]
    T = dump("no60", "no61")[:250]
    C27 = dump("no27", "no38")[:250]
    C58 = dump("no58", "no59")[:250]
    print(f"len(B)={len(B)} readable={sum(x is not None for x in B)} len(T)={len(T)} no27={len(C27)} no58={len(C58)}")
    if len(B) < 30:
        print("NON-TEST: len(B) < 30"); sys.exit(4)
    L = lcs(B, T); R = L / len(B)
    rng = random.Random(7)
    sh = []
    for _ in range(1000):
        p = T[:]; rng.shuffle(p); sh.append(lcs(B, p))
    sh.sort(); p99 = sh[989]; mx = sh[-1]; mean = sum(sh) / len(sh)
    l27 = lcs(B, C27); l58 = lcs(B, C58)
    ge = sum(s >= L for s in sh)
    print(f"LCS={L} R={R:.3f} | shuffle mean {mean:.1f} p99 {p99} max {mx} (>= real: {ge}/1000) | no27 {l27} no58 {l58}")
    ok = R >= 0.40 and L > p99 and L > l27 and L > l58
    print("PASS" if ok else "FAIL"); sys.exit(0 if ok else 2)


if __name__ == "__main__":
    main()
