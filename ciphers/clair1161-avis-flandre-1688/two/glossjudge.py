#!/usr/bin/env python3
"""RUN4-C1161GJ (4 Oct 2026): gloss-and-judge value test of contested key letters (pre-registered in
tx/PREREG_glossjudge.md). Per sign: G (glossctl statistic on the c186R block) and J (judge_plaintext NgramModel.score,
fr16, on the 3389-sign letters-only decode) for value A (key.tsv) vs B (consensus letter), against a shuffled-key null
(two/cons/key_shuf*_s*.tsv, 50 keys) and a 26-letter null. Writes two/glossjudge.tsv and two/glossjudge_gate.tsv.

  python3 two/glossjudge.py
"""
import csv, glob, json, os, re, string, sys
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE); ROOT = os.path.dirname(os.path.dirname(T))
sys.path.insert(0, os.path.join(ROOT, "tools")); sys.path.insert(0, os.path.join(T, "glossctl"))
import judge_plaintext as jp
from glossctl import block_tokens, gloss_letters, stat

SIGNS = [("2", "t"), ("tz", "l"), ("qb", "e"), ("4", "e"), ("S", "n")]
real = {r["sign"]: r["value"] for r in csv.DictReader(open(os.path.join(T, "key.tsv")), delimiter="\t")}
allt = [r["sign"] for r in csv.DictReader(open(os.path.join(T, "ciphertext.tsv")), delimiter="\t") if r["sign"] != "/"]
blk, g = block_tokens(), gloss_letters()
spec = json.load(open(os.path.join(ROOT, "specs", "clair1161-avis-flandre-1688.json")))
model = jp.NgramModel([jp.read_corpus(os.path.join(ROOT, p)) for p in spec["judge"]["corpora"]])

def dec(k, toks): return "".join(k.get(t, "") for t in toks)
def G(k): return stat("".join(k.get(t, "?") for t in blk), g)
def J(k): return model.score(dec(k, allt))
def with_(k, s, v): k2 = dict(k); k2[s] = v; return k2

shuf = []
for p in sorted(glob.glob(os.path.join(HERE, "cons", "key_shuf*_s*.tsv"))):
    k = dict(real); k.update({r["sign"]: r["value"] for r in csv.DictReader(open(p), delimiter="\t")}); shuf.append((os.path.basename(p), k))
assert len(shuf) == 50, len(shuf)
assert dec(real, allt) == re.sub("[^a-z]", "", open(os.path.join(HERE, "full_decode.txt")).read())

rows, gate = [], []
p95 = lambda xs: sorted(xs)[47]
for s, B in SIGNS:
    A = real[s]; nblk = blk.count(s)
    sc = {v: (G(with_(real, s, v)), J(with_(real, s, v))) for v in string.ascii_lowercase}
    for v, (gv, jv) in sc.items():
        rows.append([s, v, "real", f"{gv:.4f}", f"{jv:.5f}"])
    nd = []
    for name, k in shuf:
        ga, ja = G(with_(k, s, A)), J(with_(k, s, A)); gb, jb = G(with_(k, s, B)), J(with_(k, s, B))
        nd.append((gb - ga, jb - ja)); rows.append([s, f"{A}->{B}", name, f"{gb-ga:.4f}", f"{jb-ja:.5f}"])
    for V, W, sign in ((B, A, 1), (A, B, -1)):
        dG, dJ = sc[V][0] - sc[W][0], sc[V][1] - sc[W][1]
        nG, nJ = p95([sign * x[0] for x in nd]), p95([sign * x[1] for x in nd])
        rG = sum(1 for v in sc if sc[v][0] > sc[V][0]); rJ = sum(1 for v in sc if sc[v][1] > sc[V][1])
        c1 = dG > 0 and dJ > 0; c2 = dG > nG and dJ > nJ; c3 = rG <= 1 and rJ <= 1; floor = nblk >= 3
        ok = c1 and c2 and c3 and floor
        topG = max(sc, key=lambda v: sc[v][0]); topJ = max(sc, key=lambda v: sc[v][1])
        gate.append([s, A, B, V, nblk, f"{dG:.4f}", f"{nG:.4f}", f"{dJ:.5f}", f"{nJ:.5f}", rG + 1, rJ + 1, topG, topJ,
                     int(c1), int(c2), int(c3), int(floor), "PASS" if ok else "fail"])
with open(os.path.join(HERE, "glossjudge.tsv"), "w") as f:
    f.write("sign\tvalue\tkey\tG_or_dG\tJ_or_dJ\n" + "".join("\t".join(map(str, r)) + "\n" for r in rows))
with open(os.path.join(HERE, "glossjudge_gate.tsv"), "w") as f:
    f.write("sign\tA\tB\ttested\tblock_tokens\td_G\tnull_p95_dG\td_J\tnull_p95_dJ\trank_G\trank_J\ttop_G\ttop_J\ti\tii\tiii\tfloor\tverdict\n")
    f.write("".join("\t".join(map(str, r)) + "\n" for r in gate))
# information only: all five B at once
kB = dict(real); kB.update(dict(SIGNS))
print(f"info joint all-B: G {G(real):.4f}->{G(kB):.4f}  J {J(real):.5f}->{J(kB):.5f}")
for r in gate: print("\t".join(map(str, r)))
