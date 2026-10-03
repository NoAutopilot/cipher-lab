#!/usr/bin/env python3
"""Mechanical reconciliation of the two blind passes on fr.4712 f.7r (GAPS-fr4715-vieuville-pool-16, 3 Oct 2026).
No third vision call was made (box). Rule, fixed before the gates ran: groups and glosses from pass B (its own
pair-grouping, 8 for the looped glyph); pass A's [lo] = 8 (both passes describe the same looped glyph); a mark is kept
on a group only if pass A marks a group of the same value in the same run with the same mark class (' '' ~);
bracketed non-digit glyphs and '?' are dropped. Gloss words are pass B's, with '(struck)' words removed.
Writes witness/f4712_7r_pairs.tsv (plain_line, plain_raw, cipher_line, cipher_raw; tokens N / dN / tN / bN)."""
import csv, re
from pathlib import Path
W = Path(__file__).resolve().parent.parent / "witness"

def rows(p):
    out = {}
    for l in open(p, encoding="utf-8"):
        if l.startswith("## "):
            break
        f = l.rstrip("\n").split("\t")
        if f[0] == "band" or len(f) < 7:
            continue
        out[(f[0], f[1], f[2])] = (f[5], f[6])
    return out

def toks(c, lo8=False):
    if lo8:
        c = c.replace("[lo]", "8")
    c = re.sub(r"\[[^\]]*\]", " ", c)
    res = []
    for t in c.split():
        m = re.fullmatch(r"(''|'|~)?([0-9]{1,3})", t.replace(".", ""))
        if m:
            res.append((m.group(1) or "", m.group(2)))
    return res

A, B = rows(W / "f4712_7r_pass_A.tsv"), rows(W / "f4712_7r_pass_B.tsv")
amarks = {}
for (b, ln, r), (c, g) in A.items():
    for mk, n in toks(c, True):
        if mk:
            amarks.setdefault((b, ln), set()).add((mk, str(int(n))))
CLS = {"'": "d", "''": "t", "~": "b"}
with open(W / "f4712_7r_pairs.tsv", "w", encoding="utf-8") as f:
    f.write("# fr.4712 f.7r reconciled pairs (scripts/f4712_7r_reconcile.py); marks kept only where both passes agree\n")
    f.write("plain_line\tplain_raw\tcipher_line\tcipher_raw\n")
    for (b, ln, r), (c, g) in B.items():
        gl = [re.sub(r"\[[^\]]*\]", "", w) for w in g.split("|") if "(struck)" not in w]
        gl = " ".join(w for w in gl if re.search(r"[A-Za-z]", w))
        if not gl:
            continue
        out = []
        for mk, n in toks(c):
            n2 = str(int(n))
            if len(n) > 2:
                continue
            keep = mk and (mk, n2) in amarks.get((b, ln), set())
            out.append((CLS[mk] if keep else "") + n2)
        tag = f"{b}.{ln}.{r}"
        f.write(f"{tag}\t{gl}\t{tag}\t{' '.join(out)}\n")
