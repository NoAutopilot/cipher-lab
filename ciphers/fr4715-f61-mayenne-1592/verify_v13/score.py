#!/usr/bin/env python3
"""VERIFY-F61-V13: score c1_reply.tsv (verbatim) against key.json (sha256 99e9abf7..., pre-registered in PREREG.md) under PREREG's gates and
decision rules. python3 score.py [--check]"""
import csv, hashlib, json, os, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); CHECK = "--check" in sys.argv
raw = open(f"{HERE}/key.json").read(); assert hashlib.sha256(raw.encode()).hexdigest().startswith("99e9abf7cb852be9"), "key hash"
k = json.loads(raw); rows = list(csv.DictReader(open(f"{HERE}/c1_reply.tsv"), delimiter="\t"))
def dec(r):
    p = "A" if r["part"] == "A" else "B"; tile = k[f"items{p}"][r["item"]]; a = r["answer"]
    return tile, k[f"panel{p}"].get(a, a)
A = [(t, c, r["part"]) for r in rows for t, c in [dec(r)]]
def exp(tile):
    base = tile.rsplit("_", 1)[0]
    return {"A_4STEM": "4STEM", "A_HASHL": "HASHL", "A_HASH4O": "HASH4O", "A_CROSS": "CROSS", "A_4PI": "4PI", "A_PLAIN_IL": "O",
            "A_PLAIN_LES": "O", "A_C43": "C43", "A_PHI": "PHI", "A_ZHOOK": "ZHOOK", "A_4TRI": "4TRI"}.get(base)
out = []; pa = [(t, c) for t, c, p in A if p == "A"]; pb = [(t, c) for t, c, p in A if p == "B"]
anch = [(t, c, exp(t)) for t, c in pa if t.startswith("A_")]
g1 = sum(c == e for t, c, e in anch); out.append(f"G1 anchors {g1}/{len(anch)} (gate 12): {'PASS' if g1 >= 12 else 'FAIL'}; misses: {[(t, c) for t, c, e in anch if c != e]}")
ins = {t: c for t, c in pa if t.startswith("R_")}; g2 = ins == {"R_CROSS_W2": "CROSS", "R_4PI_W2": "4PI", "R_LL_W3": "LL"}
out.append(f"G2 in-span controls {ins}: {'PASS' if g2 else 'FAIL'}")
tw = {}; 
for t, c in pa:
    if t.startswith("T_"): tw.setdefault(t, []).append(c)
rep = sum(len(v) == 2 and v[0] == v[1] for t, v in tw.items() if t.endswith("_W1")); out.append(f"G3 repeats {rep}/3 consistent (gate 2): {'PASS' if rep >= 2 else 'FAIL'}")
b = dict(pb); g4 = b["R_CROSS_W3"] == "N" and b["R_LL_W2"] == "N" and b["A_4STEM_W2"] == "4STEM" and b["A_4PI_W2"] == "4PI"
out.append(f"G4 anti-steering (B) L07/10 {b['R_CROSS_W3']}, L05/16 {b['R_LL_W2']}, anchors {b['A_4STEM_W2']} {b['A_4PI_W2']}; 4-over-hash off panel -> {b['A_HASH4O_W2']}: {'PASS' if g4 else 'FAIL'}")
ok = g1 >= 12 and g2 and rep >= 2 and g4
for tgt, name in (("T_L11_8", "L11/8"), ("T_L01_11", "L01/11"), ("T_L02_0", "L02 opening")):
    w = [tw[f"{tgt}_{x}"][0] for x in ("W1", "W2", "W3")]; cnt = Counter(w); top, n = cnt.most_common(1)[0]
    if not ok: v = "not scored (CONTROL FAIL)"
    elif tgt == "T_L11_8": v = "endorse CROSS" if cnt["CROSS"] >= 2 else "reject (4STEM stands)" if cnt["4STEM"] >= 2 else "hold"
    elif tgt == "T_L01_11": v = "endorse 4-over-hash (no change)" if cnt["HASH4O"] >= 2 else "reject runner 16 / conflict (4PI)" if cnt["4PI"] >= 2 else "hold (HASH4 stands as coded, no change)"
    else:
        il = dict(pa)["A_PLAIN_IL_W1"]
        v = ("endorse LL insert" if il == "O" else "hold (plain 'Il' anchor -> LL: shape cannot separate)" if il == "LL" else
             f"hold (endorse condition unmet: plain 'Il' anchor -> {il}, not O)") if cnt["LL"] >= 2 else "reject" if cnt["O"] >= 2 else "hold"
    out.append(f"{name}: W1/W2/W3 {w}, repeat {tw[f'{tgt}_W1'][1]}, Part B W2 {b[f'{tgt}_W2']} -> {v}")
txt = "\n".join(out) + "\n"; p = f"{HERE}/score_result.txt"
if CHECK: s = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if s else "STALE"); sys.exit(0 if s else 1)
open(p, "w").write(txt); print(txt, end="")
