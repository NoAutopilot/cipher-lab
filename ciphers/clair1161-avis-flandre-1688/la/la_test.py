#!/usr/bin/env python3
"""D2-C1161LA (5 Oct 2026): pre-registered relabel test (la/PREREG_c1161la.md). Input: la/passD.tsv from
`tools/lookalike_pass.py reconcile` (2-of-3). Relabel set R = positions where passD sign_id != passC sign_id.
Statistics under the UNCHANGED key.tsv: G = glossctl stat on the c186R block vs its period gloss; J = judge_plaintext
NgramModel.score (spec fr16 corpora) on the letters-only decode of all tokens; L = longest run of C/S-graded tokens
(token grade = key grade, lowered to M when the transcription conf is not H) -- L reported, not gated.
Control: 50 seeds; each seed applies the same multiset of (from -> to) relabels at positions drawn at random (without
replacement, excluding R) among all positions carrying the same `from` label. Gate: real dG > null p95 AND real dJ > null p95.
Writes la/la_test.tsv (one row per run) and prints the gate.
  python3 la/la_test.py
"""
import csv, json, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE); ROOT = os.path.dirname(os.path.dirname(T))
sys.path.insert(0, os.path.join(ROOT, "tools")); sys.path.insert(0, os.path.join(T, "glossctl"))
import judge_plaintext as jp
from glossctl import gloss_letters, stat
rd = lambda p: list(csv.DictReader(open(p), delimiter="\t"))
key = {r["sign"]: (r["value"], r["grade"]) for r in rd(os.path.join(T, "key.tsv"))}
ct = rd(os.path.join(T, "ciphertext.tsv"))
pc = rd(os.path.join(HERE, "passC.tsv")); pd = rd(os.path.join(HERE, "passD.tsv"))
assert [r["sign_id"] for r in pc] == [r["sign"] for r in ct]
R = [(i, a["sign_id"], b["sign_id"], b.get("conf", "")) for i, (a, b) in enumerate(zip(pc, pd)) if a["sign_id"] != b["sign_id"]]
spec = json.load(open(os.path.join(ROOT, "specs", "clair1161-avis-flandre-1688.json")))
model = jp.NgramModel([jp.read_corpus(os.path.join(ROOT, p)) for p in spec["judge"]["corpora"]])
g = gloss_letters()

def stats(signs, confs):
    v = lambda s: key.get(s, ("", "U"))[0]
    blk = "".join(key.get(s, ("?",))[0] or "?" for s, r in zip(signs, ct) if r["line"].startswith("c186R") and s != "/")
    J = model.score("".join(v(s) for s in signs if s != "/"))
    best = cur = 0
    for s, c in zip(signs, confs):
        if s == "/":
            continue
        gr = key.get(s, ("", "U"))[1]
        gr = gr if c == "H" else ("M" if gr in "CS" else gr)
        cur = cur + 1 if gr in "CS" else 0; best = max(best, cur)
    return stat(blk, g), J, best

base_s = [r["sign"] for r in ct]; base_c = [r["conf"] for r in ct]
G0, J0, L0 = stats(base_s, base_c)
rows = [dict(run="base", n=0, G=f"{G0:.4f}", J=f"{J0:.5f}", L=L0, dG="0", dJ="0", dL=0)]
print(f"relabel set R: {len(R)}", [(ct[i]['line'], ct[i]['pos'], a, b) for i, a, b, _ in R])
if R:
    s1, c1 = list(base_s), list(base_c)
    for i, a, b, c in R:
        s1[i] = b; c1[i] = c or "M"
    G1, J1, L1 = stats(s1, c1)
    rows.append(dict(run="real", n=len(R), G=f"{G1:.4f}", J=f"{J1:.5f}", L=L1, dG=f"{G1-G0:+.4f}", dJ=f"{J1-J0:+.5f}", dL=L1 - L0))
    Rpos = {i for i, *_ in R}
    nd = []
    for seed in range(1, 51):
        rng = random.Random(seed); s2, c2, used = list(base_s), list(base_c), set(Rpos)
        for i, a, b, c in R:
            pool = [k for k, s in enumerate(base_s) if s == a and k not in used]
            k = rng.choice(pool); used.add(k); s2[k] = b
        G2, J2, L2 = stats(s2, c2)
        nd.append((G2 - G0, J2 - J0))
        rows.append(dict(run=f"null{seed}", n=len(R), G=f"{G2:.4f}", J=f"{J2:.5f}", L=L2, dG=f"{G2-G0:+.4f}", dJ=f"{J2-J0:+.5f}", dL=L2 - L0))
    p95 = lambda xs: sorted(xs)[47]
    pG, pJ = p95([d[0] for d in nd]), p95([d[1] for d in nd])
    passG, passJ = G1 - G0 > pG, J1 - J0 > pJ
    print(f"dG real {G1-G0:+.4f} null p95 {pG:+.4f} -> {passG}; dJ real {J1-J0:+.5f} null p95 {pJ:+.5f} -> {passJ}; "
          f"L {L0}->{L1}; GATE {'PASS' if passG and passJ else 'FAIL'}")
else:
    print("R empty: nothing to test (no relabel moved a passC label)")
with open(os.path.join(HERE, "la_test.tsv"), "w") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(rows)
