#!/usr/bin/env python3
"""Controls A, B, B0 of tools/tests/PREREG-MQS-SEGMENTER.md (MQS-SEGMENTER, 9 Oct 2026). Run once; prints the numbers."""
import random, re, string, sys
from collections import Counter
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import judge_plaintext as jp
import segmenter as sg

t = re.sub(r"-\s*\n\s*", "", jp.read_corpus(jp.LANG_CORPORA["fr"][0]))
words = [w for w in (jp.fold(x) for x in re.findall(r"[^\W\d_]+", t)) if w]
cut = int(0.7 * len(words))
lex = sg.Lexicon(Counter(words[:cut]), singles=("a", "y"))
held = words[cut:]
stream = "".join(held); bounds = set(); o = 0
for w in held:
    o += len(w); bounds.add(o)
rnd = random.Random(1); N = 500; W = []
for _ in range(20):
    j = rnd.randrange(0, len(stream) - N)
    W.append((stream[j:j + N], {b - j for b in bounds if j < b < j + N}))

def f1(pred, truth):
    tp = len(pred & truth)
    if not tp: return 0.0
    p, r = tp / len(pred), tp / len(truth); return 2 * p * r / (p + r)

def bset(toks):
    s, o = set(), 0
    for tk, _ in toks[:-1]:
        o += len(tk); s.add(o)
    return s

A, An = [], []
for k, (w, tr) in enumerate(W):
    A.append(f1(bset(sg.segment(w, lex)), tr))
    ws = list(w); random.Random(100 + k).shuffle(ws)
    An.append(f1(bset(sg.segment("".join(ws), lex)), tr))
mA, mx = sum(A) / 20, max(An)
print(f"A: mean boundary F1 {mA:.3f} (min {min(A):.3f}); null mean {sum(An)/20:.3f} max {mx:.3f}; "
      f"gate F1>=0.80 and > null max: {'PASS' if mA >= 0.80 and mA > mx else 'FAIL'}")

L = string.ascii_lowercase
def fl(s): return sum(x[1] for x in sg.fragments(s, lex, 12))
prec_n = prec_d = 0; wins = 0; B0 = 0; rows = []
for k, (w, _) in enumerate(W):
    r = random.Random(1000 + k)
    bad = r.sample(L, 8); m = {c: c for c in L}
    for i, c in enumerate(bad): m[c] = bad[(i + 1) % 8]
    dec = "".join(m[c] for c in w)
    fr = sg.fragments(dec, lex, 12)
    for o, n, _ in fr:
        prec_n += sum(dec[o + i] == w[o + i] for i in range(n)); prec_d += n
    tgt = sum(n for _, n, _ in fr)
    nulls = []
    for s in range(20):
        d = list(dec); random.Random(5000 + 20 * k + s).shuffle(d); nulls.append(fl("".join(d)))
    p95 = sorted(nulls)[int(0.95 * 19)]
    wins += tgt > p95; rows.append((tgt, p95))
    perm = list(L); r.shuffle(perm); pm = dict(zip(L, perm))
    B0 += bool(sg.fragments("".join(pm[c] for c in w), lex, 12))
prec = prec_n / prec_d if prec_d else 0.0
print(f"B: fragment-letter precision {prec:.3f} ({prec_n}/{prec_d}); target > null p95 in {wins}/20 windows; "
      f"gate prec>=0.90 and >=16/20: {'PASS' if prec >= 0.90 and wins >= 16 else 'FAIL'}")
print("B rows (target fragment letters, null p95):", rows)
print(f"B0: wholly wrong key, windows with any fragment {B0}/20; gate <=2: {'PASS' if B0 <= 2 else 'FAIL'}")
