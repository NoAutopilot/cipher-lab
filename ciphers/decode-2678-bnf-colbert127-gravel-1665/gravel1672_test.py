#!/usr/bin/env python3
"""R9-DEC2678C: pre-registered test (PREREG-gravel1672-2026-10-06.md) of Tomokiyo's Colbert-Gravel 1672 key on R2678.
Reads key_gravel1672.tsv, ciphertext.tsv, tools/data/fr17/*.txt.gz; prints T, p1, p2, power; deterministic (seed 2678).
python3 gravel1672_test.py [--check]  (--check: exit 1 if gravel1672_test.out differs from a fresh run)"""
import gzip, glob, math, random, re, sys, os, unicodedata
D = os.path.dirname(os.path.abspath(__file__))
def fold(s):
    s = unicodedata.normalize("NFD", s.lower()); return re.sub(r"[^a-z]", "", "".join(c for c in s if not unicodedata.combining(c)))
key = {}
for l in open(f"{D}/key_gravel1672.tsv"):
    if l.startswith("#") or l.startswith("code\t"): continue
    p = l.rstrip("\n").split("\t")
    if len(p) >= 2: key[p[0]] = p[1]
def letters(v):  # value -> letters for T; ambiguous / null / nomenclature give nothing
    return "" if ("|" in v or v == "null" or v.startswith("<")) else fold(v)
toks = {}
for l in open(f"{D}/ciphertext.tsv"):
    if l.startswith("#") or l.startswith("line\t"): continue
    ln, pos, t, conf = l.rstrip("\n").split("\t")[:4]
    if not t.startswith("[PLAIN"): toks.setdefault(ln, []).append(t)
passages = [toks["P2"], toks["P3"]]
N = sum(len(p) for p in passages)
corpus = ""
for f in sorted(glob.glob(f"{D}/../../tools/data/fr17/*.txt.gz")):
    corpus += fold(gzip.open(f, "rt", errors="ignore").read())
from collections import Counter
tri = Counter(corpus[i:i+3] for i in range(len(corpus)-2)); bi = Counter(corpus[i:i+2] for i in range(len(corpus)-1))
def T(s):
    if len(s) < 3: return -9.0
    return sum(math.log10((tri[s[i-2:i+1]]+1)/(bi[s[i-2:i]]+26)) for i in range(2, len(s))) / (len(s)-2)
def dec(ps, k): return "".join(letters(k.get(t, "")) for p in ps for t in p)
rng = random.Random(2678)
codes = list(key); vals = [key[c] for c in codes]
def shuf_key():
    v = vals[:]; rng.shuffle(v); return dict(zip(codes, v))
real = dec(passages, key); Tr = T(real)
S = 2000
p1 = sum(T(dec(passages, shuf_key())) >= Tr for _ in range(S)) / S
def shuf_tgt():
    out = []
    for p in passages: q = p[:]; rng.shuffle(q); out.append(q)
    return out
p2 = sum(T(dec(shuf_tgt(), key)) >= Tr for _ in range(S)) / S
# power: fr17 spans enciphered greedily (longest key value first) to exactly N tokens
inv = {}
for c, v in key.items():
    if letters(v) and "|" not in v and v != "null": inv.setdefault(letters(v), []).append(c)
vlist = sorted(inv, key=len, reverse=True)
def encipher(start):
    out, i = [], start
    while len(out) < N and i < len(corpus):
        for v in vlist:
            if corpus.startswith(v, i): out.append(rng.choice(inv[v])); i += len(v); break
        else: i += 1  # letter with no cell (e.g. j, k, v, w, y, h alone): skipped, as a cipher clerk would respell
    return out
hits = 0; R = 200; PS = 500
for _ in range(R):
    ct = encipher(rng.randrange(len(corpus) - 200)); ps = [ct]
    Ts = T(dec(ps, key))
    if sum(T(dec(ps, shuf_key())) >= Ts for _ in range(PS)) / PS < 0.05: hits += 1
power = hits / R
marked = [t for p in passages for t in p if t[-1] in "^_:'"]
exact = [t for t in marked if t in key]
gate = "PASS" if (p1 < 0.05 and p2 < 0.05) else "FAIL"
out = (f"decoded letters (P2+P3): {real}\nN tokens {N}; T real {Tr:.4f}\n"
       f"control 1 shuffled key: p1 = {p1:.4f} ({S})\ncontrol 2 shuffled target order: p2 = {p2:.4f} ({S})\n"
       f"control 3 power at N={N}: {power:.3f} ({R} fr17 spans x {PS} key shuffles)\n"
       f"marked tokens with an exact same-mark cell: {len(exact)}/{len(marked)} ({' '.join(exact)})\n"
       f"gate: {gate}" + ("" if gate == "PASS" or power >= 0.8 else " (power < 0.80: non-test)") + "\n")
if "--check" in sys.argv:
    old = open(f"{D}/gravel1672_test.out").read()
    print("check ok" if old == out else "STALE"); sys.exit(0 if old == out else 1)
print(out, end=""); open(f"{D}/gravel1672_test.out", "w").write(out)
