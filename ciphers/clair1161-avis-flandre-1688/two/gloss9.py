#!/usr/bin/env python3
"""C1161-GLOSS9 (4 Oct 2026): gloss match + fr16 judge of the nine C1161-LOLO value proposals vs key.tsv
(pre-registered in tx/PREREG_gloss9.md). Reuses two/glossjudge.py's G, J and 50-key shuffled null.

  python3 two/gloss9.py
"""
import csv, difflib, glob, json, os, re, sys
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

def dec(k, toks): return "".join(k.get(t, "") for t in toks)
def G(k): return stat("".join(k.get(t, "?") for t in blk), g)
def J(k): return model.score(dec(k, allt))
def with_(k, d): k2 = dict(k); k2.update(d); return k2
def occ(k, s):
    d = "".join(k.get(t, "?") for t in blk)   # one char per block token, so index == token position
    inside = set()
    for b in difflib.SequenceMatcher(None, d, g, autojunk=False).get_matching_blocks():
        inside.update(range(b.a, b.a + b.size))
    return sum(1 for i, t in enumerate(blk) if t == s and i in inside)

shuf = []
for p in sorted(glob.glob(os.path.join(HERE, "cons", "key_shuf*_s*.tsv"))):
    k = dict(real); k.update({r["sign"]: r["value"] for r in csv.DictReader(open(p), delimiter="\t")}); shuf.append((os.path.basename(p), k))
assert len(shuf) == 50, len(shuf)
assert dec(real, allt) == re.sub("[^a-z]", "", open(os.path.join(HERE, "full_decode.txt")).read())
p95 = lambda xs: sorted(xs)[47]; p05 = lambda xs: sorted(xs)[2]

G0, J0 = G(real), J(real)
rows, gate, okA = [], [], []
for s, B in PROP:
    A = real[s]; n = blk.count(s)
    kb = with_(real, {s: B})
    dG, dJ = G(kb) - G0, J(kb) - J0
    dO = occ(kb, s) - occ(real, s)
    nd = []
    for name, k in shuf:
        x = G(with_(k, {s: B})) - G(with_(k, {s: A})); nd.append(x); rows.append([s, f"{A}->{B}", name, f"{x:.4f}", ""])
    nG = p95(nd)
    if n == 0: a = "no evidence"
    else: a = "hold" if (dG > 0 and dO > 0 and dG > nG) else "fail"
    if a == "hold" and dJ >= 0: okA.append((s, B))
    gate.append([s, A, B, n, f"{dG:.4f}", dO, f"{nG:.4f}", a, f"{dJ:.5f}", "ok" if dJ >= 0 else "worse"])

k9 = with_(real, dict(PROP)); dJ9 = J(k9) - J0; dG9 = G(k9) - G0
nj = []
for name, k in shuf:
    x = J(with_(k, dict(PROP))) - J(with_(k, {s: real[s] for s, _ in PROP})); nj.append(x); rows.append(["ALL9", "A->B", name, "", f"{x:.5f}"])
dJsub = J(with_(real, dict(okA))) - J0 if okA else 0.0
final = [s for s, _ in okA] if dJsub >= 0 else []
for r in gate:
    r.append("PASS" if r[0] in final else "fail")
with open(os.path.join(HERE, "gloss9.tsv"), "w") as f:
    f.write("sign\tswap\tnull_key\tdG\tdJ\n" + "".join("\t".join(map(str, r)) + "\n" for r in rows))
with open(os.path.join(HERE, "gloss9_gate.tsv"), "w") as f:
    f.write("sign\tA\tB\tblock_tokens\tdG\tdOcc\tnull_p95_dG\tgloss_half\tdJ_alone\tjudge_alone\tverdict\n")
    f.write("".join("\t".join(map(str, r)) + "\n" for r in gate))
print(f"key.tsv G {G0:.4f} J {J0:.5f}")
print(f"all nine: G {G(k9):.4f} (d {dG9:+.4f})  J {J(k9):.5f} (dJ9 {dJ9:+.5f}); shuffled-key dJ9 mean {sum(nj)/50:+.5f} p05 {p05(nj):+.5f} p95 {p95(nj):+.5f}")
print(f"passing subset after (a): {okA} dJ {dJsub:+.5f} -> final PASS {final}")
for r in gate: print("\t".join(map(str, r)))
