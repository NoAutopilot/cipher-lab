#!/usr/bin/env python3
"""C1161-JOINT9 (4 Oct 2026): the nine C1161-LOLO proposals as one hypothesis, joint dG and dJ vs 50 random joint keys
(values drawn from key.tsv's value-frequency distribution). Pre-registered in tx/PREREG_joint9.md.

  python3 two/joint9.py
"""
import csv, json, os, random, re, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE); ROOT = os.path.dirname(os.path.dirname(T))
sys.path.insert(0, os.path.join(ROOT, "tools")); sys.path.insert(0, os.path.join(T, "glossctl"))
import judge_plaintext as jp
from glossctl import block_tokens, gloss_letters, stat

PROP = [("K", "s"), ("iib", "d"), ("l", "f"), ("ls", "m"), ("o", "m"), ("rot", "h"), ("spiralG", "n"), ("to", "s"), ("x", "f")]
real = {r["sign"]: r["value"] for r in csv.DictReader(open(os.path.join(T, "key.tsv")), delimiter="\t")}
allt = [r["sign"] for r in csv.DictReader(open(os.path.join(T, "ciphertext.tsv")), delimiter="\t") if r["sign"] != "/"]
blk, g = block_tokens(), gloss_letters()
spec = json.load(open(os.path.join(ROOT, "specs", "clair1161-avis-flandre-1688.json")))
model = jp.NgramModel([jp.read_corpus(os.path.join(ROOT, p)) for p in spec["judge"]["corpora"]])
assert "".join(real.get(t, "") for t in allt) == re.sub("[^a-z]", "", open(os.path.join(HERE, "full_decode.txt")).read())

def G(k): return stat("".join(k.get(t, "?") for t in blk), g)
def J(k): return model.score("".join(k.get(t, "") for t in allt))
def with_(d): k = dict(real); k.update(d); return k

vf = Counter(real.values()); vals = sorted(vf); w = [vf[v] for v in vals]
G0, J0 = G(real), J(real)
k9 = with_(dict(PROP)); dG, dJ = G(k9) - G0, J(k9) - J0
rows, nG, nJ = [], [], []
for seed in range(1, 51):
    rnd = random.Random(seed)
    d = {s: rnd.choices(vals, weights=w)[0] for s, _ in PROP}
    x, y = G(with_(d)) - G0, J(with_(d)) - J0
    nG.append(x); nJ.append(y); rows.append([seed, "".join(d[s] for s, _ in PROP), f"{x:.4f}", f"{y:.5f}"])
p95 = lambda xs: sorted(xs)[47]
ok = dG > p95(nG) and dJ > p95(nJ) and dG > 0
with open(os.path.join(HERE, "joint9.tsv"), "w") as f:
    f.write("seed\tvalues_K_iib_l_ls_o_rot_spiralG_to_x\tdG\tdJ\n")
    f.write(f"real\t{''.join(b for _, b in PROP)}\t{dG:.4f}\t{dJ:.5f}\n")
    f.write("".join("\t".join(map(str, r)) + "\n" for r in rows))
print(f"key.tsv G {G0:.4f} J {J0:.5f}; nine block tokens {sum(blk.count(s) for s, _ in PROP)}")
print(f"real dG {dG:+.4f} dJ {dJ:+.5f}")
print(f"null dG mean {sum(nG)/50:+.4f} p95 {p95(nG):+.4f} max {max(nG):+.4f}; dJ mean {sum(nJ)/50:+.5f} p95 {p95(nJ):+.5f} max {max(nJ):+.5f}")
print("PASS" if ok else "FAIL")
