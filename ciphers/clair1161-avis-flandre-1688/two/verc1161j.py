#!/usr/bin/env python3
"""VER-C1161J (4 Oct 2026, account-3 verifier): selection-matched nulls for the nine C1161-JOINT9 values.
Pre-registered in tx/PREREG_verc1161j.md.   python3 two/verc1161j.py
"""
import csv, json, os, random, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE); ROOT = os.path.dirname(os.path.dirname(T))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(ROOT, "tools")); sys.path.insert(0, os.path.join(T, "glossctl"))
import judge_plaintext as jp, family_run as fr
from glossctl import block_tokens, gloss_letters, stat
import reanneal as ra

PROP = [("K", "s"), ("iib", "d"), ("l", "f"), ("ls", "m"), ("o", "m"), ("rot", "h"), ("spiralG", "n"), ("to", "s"), ("x", "f")]
pre = {r["sign"]: r["value"] for r in csv.DictReader(open(os.path.join(HERE, "key_pre_joint9.tsv")), delimiter="\t")}
allt = [r["sign"] for r in csv.DictReader(open(os.path.join(T, "ciphertext.tsv")), delimiter="\t") if r["sign"] != "/"]
blk, g = block_tokens(), gloss_letters()
spec = json.load(open(os.path.join(ROOT, "specs", "clair1161-avis-flandre-1688.json")))
model = jp.NgramModel([jp.read_corpus(os.path.join(ROOT, p)) for p in spec["judge"]["corpora"]])
ra.NORM = "none"; ra.OUT = os.path.join(HERE, "ra"); ra.setup("ctl")

def with_(d): k = dict(pre); k.update(d); return k
def dec(k, toks): return "".join(k.get(t, "?") for t in toks)
def G(k, ref=None): return stat(dec(k, blk), g if ref is None else ref)
def J(k): return model.score("".join(k.get(t, "") for t in allt))
def L4(k): return ra.L4("".join(k.get(s, pre[s]) for s in ra.SEQ))

k9 = with_(dict(PROP)); G0, J0, L0 = G(pre), J(pre), L4(pre)
dG, dJ, dL = G(k9) - G0, J(k9) - J0, L4(k9) - L0
out = [["test", "draw", "dG", "dJ", "dL4", "note"], ["real", "-", f"{dG:.4f}", f"{dJ:.5f}", f"{dL:.5f}", "nine vs key_pre_joint9"]]

# T2: content-specificity, 200 fr16 windows of gloss length
text = "".join(re.sub("[^a-z]", "", jp.read_corpus(p)) for p in fr.corpus_paths(spec, None))
rng = random.Random(1); wd = []
for i in range(200):
    s = rng.randrange(len(text) - len(g)); w = text[s:s + len(g)]
    wd.append(G(k9, w) - G(pre, w)); out.append(["T2", i + 1, f"{wd[-1]:.4f}", "", "", f"window@{s}"])
w95 = sorted(wd)[189]; t2 = dG > w95

# T3: best-of-K by L4, K=2000, 50 draws
L = "abcdefghijklmnopqrstuvwxyz"; sg, sj, sl = [], [], []
for seed in range(1, 51):
    r = random.Random(seed); best = None
    for _ in range(2000):
        d = {s: r.choice(L) for s, _ in PROP}; v = L4(with_(d))
        if best is None or v > best[0]: best = (v, d)
    k = with_(best[1]); sg.append(G(k) - G0); sj.append(J(k) - J0); sl.append(best[0] - L0)
    out.append(["T3", seed, f"{sg[-1]:.4f}", f"{sj[-1]:.5f}", f"{sl[-1]:.5f}", "".join(best[1][s] for s, _ in PROP)])
g95 = sorted(sg)[47]; t3 = dG > g95
open(os.path.join(HERE, "verc1161j.tsv"), "w").write("".join("\t".join(map(str, r)) + "\n" for r in out))
m = lambda xs: sum(xs) / len(xs)
print(f"real dG {dG:+.4f} dJ {dJ:+.5f} dL4 {dL:+.5f}")
print(f"T2 windows dG mean {m(wd):+.4f} p95 {w95:+.4f} max {max(wd):+.4f} -> {'PASS' if t2 else 'FAIL'}")
print(f"T3 best-of-2000 dG mean {m(sg):+.4f} p95 {g95:+.4f} max {max(sg):+.4f}; dJ mean {m(sj):+.5f} max {max(sj):+.5f}; "
      f"dL4 mean {m(sl):+.5f} max {max(sl):+.5f} -> {'PASS' if t3 else 'FAIL'}")
print("S STANDS" if (t2 and t3) else "BACK TO M")
