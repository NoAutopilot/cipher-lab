#!/usr/bin/env python3
"""BNF-G60C step A: synthetic matched control for key no.60 at f.91's length with 32% reader error (registered in
.claude/briefs/runs/2026-10-08-ytbiz-bnf-g60c.md). Scripts only, no image calls. Usage: g60c_control.py [N]"""
import sys, random, statistics
from pathlib import Path
R = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(R / "tools"))
import judge_plaintext as J
N = int(sys.argv[1]) if len(sys.argv) > 1 else 190
ERR, SEEDS, SHUF = 0.32, 10, 200
rows = [l.rstrip("\n").split("\t") for l in (R/"ciphers/fr3986-nevers-revol-1593/key.tsv").read_text().splitlines()
        if l and not l.startswith("#") and not l.startswith("sign\t")]
key = {r[0]: [J.fold(a) for a in r[1].split("|")] for r in rows}
key = {s: [a for a in v if a] for s, v in key.items()}
tags = sorted(key)
homo = {}
for s, alts in key.items():
    for a in alts:
        if len(a) == 1: homo.setdefault(a, []).append(s)
print("letters with homophones:", len(homo), "tags:", len(tags))
model = J.NgramModel([J.read_corpus(p) for p in J.LANG_CORPORA["fr"]])
raw = model.raw
def decode(seq, k): return "".join(k[s][0] for s in seq if k.get(s))
def shuffled(rnd):
    vals = [key[s] for s in tags]; rnd.shuffle(vals); return dict(zip(tags, vals))
npass = 0
for seed in range(SEEDS):
    rnd = random.Random(1000 + seed)
    # plaintext window: N enciphered letters, only letters having a homophone
    while True:
        j = rnd.randrange(0, len(raw) - 3 * N); w = [c for c in raw[j:j + 3 * N] if c in homo][:N]
        if len(w) == N: break
    seq = [rnd.choice(homo[c]) for c in w]
    seq = [rnd.choice(tags) if rnd.random() < ERR else s for s in seq]
    real = model.score(decode(seq, key))
    nul = sorted(model.score(decode(seq, shuffled(rnd))) for _ in range(SHUF))
    p99 = J.pct(nul, 0.99); ok = real > p99; npass += ok
    print(f"seed {seed}: real {real:.3f} shuf mean {statistics.mean(nul):.3f} p99 {p99:.3f} max {nul[-1]:.3f} {'PASS' if ok else 'FAIL'}")
print(f"N={N} err={ERR} PASS {npass}/{SEEDS}  GATE>=8: {'OPEN' if npass >= 8 else 'STOP'}")
