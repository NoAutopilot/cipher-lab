#!/usr/bin/env python3
"""A2-F61 (2 Oct 2026): score reply.tsv against key.json (committed after the reply; sha256 62bdcfbd... pre-registered) under PREREG.md's gates
and decision rule. Writes score_result.txt; --check exits 1 if the committed result is stale."""
import csv, hashlib, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
raw = open(f"{HERE}/key.json").read(); assert hashlib.sha256(raw.encode()).hexdigest().startswith("62bdcfbd"), "key sha mismatch"
key = json.loads(raw); pan = key["panel"]
ans = {r["item"]: r["answer"].strip() for r in csv.DictReader(open(f"{HERE}/reply.tsv"), delimiter="\t")}
def cls(a): return pan.get(a, a)  # panel letter -> class name; N/O stay
got = {}; reps = {}
for i, name in key["items"].items():
    v = cls(ans[i])
    if name in got: reps[name] = v
    else: got[name] = v
EXP = {"A_PLAIN_LES_W1": "O", "A_CROSS_W1": "CROSS", "A_4PI_W1": "4PI", "A_C43_W2": "C43", "A_PHI_W2": "PHI", "A_ZHOOK_W2": "ZHOOK",
       "A_4TRI_W2": "4TRI", "A_4STEM_W1": "4STEM", "A_HASH4O_W1": "HASH4O"}
L = []; ok_a = sum(got[k] == v for k, v in EXP.items())
for k, v in EXP.items(): L.append(f"anchor {k}: expected {v}, read {got[k]}")
L.append(f"observational A_PLAIN_IL_W1: read {got['A_PLAIN_IL_W1']}")
g1 = ok_a >= 8; g2 = got["R_LL_W3"] == "LL"; g3 = all(reps[k] == got[k] for k in reps)
L += [f"G1 anchors {ok_a}/9 (>=8): {'PASS' if g1 else 'FAIL'}", f"G2 in-span R_LL_W3 -> {got['R_LL_W3']}: {'PASS' if g2 else 'FAIL'}",
      f"G3 repeats " + ", ".join(f"{k} {got[k]}/{reps[k]}" for k in sorted(reps)) + f": {'PASS' if g3 else 'FAIL'}"]
T = [got[f"T_L02_0_{w}"] for w in ("W1", "W2", "W3")]; F = [got[f"F_LL_DELLA_{w}"] for w in ("W1", "W2", "W3")]
L += [f"target L02 opening W1/W2/W3: {' '.join(T)}", f"foil L07 in-word 'll' (della) W1/W2/W3: {' '.join(F)}"]
if not (g1 and g2 and g3): v = "CONTROL FAIL: nothing scored, L02 opening stays held"
elif F.count("LL") >= 2: v = "HOLD: foil reads LL, reader cannot separate in-word 'll' from the LL sign"
elif F.count("O") >= 2 and T.count("LL") >= 2: v = "ENDORSE: insert L02 0 LL (null); V13's foil condition met; cipher count 100"
elif F.count("O") >= 2 and T.count("O") >= 2: v = "REJECT: the mark is handwriting"
else: v = "HOLD: mixed"
L.append(f"verdict: {v}"); out = "\n".join(L) + "\n"; p = f"{HERE}/score_result.txt"
if "--check" in sys.argv:
    if open(p).read() != out: print("STALE"); sys.exit(1)
    print("check OK")
else: open(p, "w").write(out); print(out)
