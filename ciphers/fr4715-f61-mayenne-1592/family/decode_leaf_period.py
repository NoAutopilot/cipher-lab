#!/usr/bin/env python3
"""F61-FAMILY-4 (28 Sept 2026), brief step 2: decode one family leaf's reconciled sign draft (passes/rec<PREFIX>/
ciphertext_draft.tsv, with align_period.py's H24 rule from the two passes) under a merged period key, decode_period.py's
rule (pairs n >= 2 and n >= --frac x the leaf class total, EBR_A/EBR_B folded into EBR when the leaf's own passes did not
split them -- they did here, so no fold), and write family/<PREFIX>_decode_period<suffix>.tsv/.txt with per-token grades:
C one period letter attested by one leaf, C+ by two or more leaves, S a rare-class row (source column 'rare-S'), M a period
pair (choice by context not made here), '-' unread. --drop FILE: a TSV of (line, segment) crops whose signs are held out
(f.124r: the s5 crops of L28-L30, where --track drifted one row and the two readers listed the neighbouring row).
  python3 decode_leaf_period.py PREFIX --key key_period_v4.tsv [--frac 0.1] [--drop passes/f124r_drop.tsv] [--check]
"""
import csv, os, sys
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"
pre = sys.argv[1]
KEYFILE = sys.argv[sys.argv.index("--key") + 1] if "--key" in sys.argv else "key_period_v3.tsv"; KEYFILE = KEYFILE if os.path.isabs(KEYFILE) else f"{HERE}/{KEYFILE}"
FRAC = float(sys.argv[sys.argv.index("--frac") + 1]) if "--frac" in sys.argv else 0.1
SUF = "_" + os.path.basename(KEYFILE).replace("key_period_", "").replace(".tsv", "")
drop = set()
if "--drop" in sys.argv:
    for r in csv.DictReader((l for l in open(sys.argv[sys.argv.index("--drop") + 1]) if not l.startswith("#")), delimiter="\t"): drop.add((r["line"], r["segment"]))
rows = [r for r in csv.DictReader((l for l in open(KEYFILE) if not l.startswith("#")), delimiter="\t")]
tot = defaultdict(int); key = defaultdict(dict); leaves = defaultdict(lambda: defaultdict(set)); src = defaultdict(dict)
for r in rows:
    if r["letter"] != "-": tot[(r["class"], r["leaf"])] += int(r["n"])
for r in rows:
    cl = r["class"]; s = r.get("source", "period")
    if cl in ("OTHER", "PLAIN", "DASH"): continue   # the readers' uncoded sign (a word code on de Diou's hand) is not a key class
    if r["letter"] != "-" and (s == "rare-S" or (int(r["n"]) >= 2 and int(r["n"]) >= FRAC * tot[(cl, r["leaf"])])):
        key[cl][r["letter"]] = key[cl].get(r["letter"], 0) + int(r["n"]); leaves[cl][r["letter"]].add(r["leaf"]); src[cl][r["letter"]] = s
A = {(r["line"], r["pos"]): r for r in csv.DictReader(open(f"{P}/{pre}_signsA.tsv"), delimiter="\t")}
B = {(r["line"], r["pos"]): r for r in csv.DictReader(open(f"{P}/{pre}_signsB.tsv"), delimiter="\t")}
lines = defaultdict(list)
for r in csv.DictReader(open(f"{P}/rec{pre}/ciphertext_draft.tsv"), delimiter="\t"):
    a = A.get((r["line"], r["position"])); b = B.get((r["line"], r["position"])); code = r["sign"]
    if a and b and {a["sign"], b["sign"]} == {"HASH4", "4STEM"}: code = "H24"
    if a and (r["line"], a["segment"]) in drop: continue
    lines[r["line"]].append((code, (a or {}).get("note", "")))
out = []; tsv = ["line\tpos\tclass\tperiod_letters\tgrade"]; tot_g = defaultdict(int)
for line in sorted(lines):
    toks = []
    for i, (c, note) in enumerate(lines[line], 1):
        if c == "PLAIN": toks.append("{" + (note.strip().split()[0] if note.strip() else "word") + "}"); g = "P"; letters = "-"
        else:
            v = key.get(c, {}); letters = "/".join(sorted(v, key=lambda k: -v[k]))
            if len(v) == 1: g = "S" if src[c][letters] == "rare-S" else ("C+" if len(leaves[c][letters]) >= 2 else "C")
            elif v: g = "M"
            else: g = "-"
            toks.append(letters if g in ("C", "C+", "S") else (f"[{letters}]" if g == "M" else f"<{c}>"))
        tot_g[g] += 1; tsv.append(f"{line}\t{i}\t{c}\t{letters}\t{g}")
    out.append(f"{line}: " + " ".join(toks))
n = sum(v for k, v in tot_g.items() if k != "P")
hdr = f"# {pre} under {os.path.basename(KEYFILE)} (period pairs n>=2, n >= {FRAC:g} x the leaf class total, rare-S rows as given; no refit), 28 Sept 2026: {n} signs, C {tot_g['C']} C+ {tot_g['C+']} S {tot_g['S']} M {tot_g['M']} unread {tot_g['-']}, clear words {tot_g['P']}; firm (C/C+/S) {(tot_g['C']+tot_g['C+']+tot_g['S'])/n:.3f}, covered {(n-tot_g['-'])/n:.3f}. [a/b] = period pair, choice by context not made here; <CLASS> = no period pair; {{word}} = clear word in the row.\n"
txt = hdr + "\n".join(out) + "\n"; tsvt = "\n".join(tsv) + "\n"
tp, tt = f"{HERE}/{pre}_decode_period{SUF}.txt", f"{HERE}/{pre}_decode_period{SUF}.tsv"
if "--check" in sys.argv:
    ok = os.path.exists(tp) and open(tp).read() == txt and open(tt).read() == tsvt; print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
open(tp, "w").write(txt); open(tt, "w").write(tsvt); print(hdr.strip()); print("\n".join(out[:3]))
