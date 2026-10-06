#!/usr/bin/env python3
"""A4-RFCOL, 6 Oct 2026: known-answer test of key_f24.tsv's C codes against the canvas 20-21 interlinear glosses.
key_f24 was built from f.24 (canvas 27) alone, before canvas 20-21's glosses were re-read as word-for-word, so its
C codes are predictions here. Statistic: occurrences of a C code whose predicted chunk appears in the unit's gloss
(spaces removed, lower case) within +-WIN of the token's relative position in the run. Control: the same cipher
units with the glosses dealt in a random derangement (no unit keeps its own), N seeds; the control changes which
gloss a run meets, which the statistic depends on, so it can fail differently. Per-code breakdown printed too.
Deterministic. Usage: python3 c20c21_knownanswer.py"""
import csv, os, random, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__)); SEED, N, WIN = 20261006, 2000, 0.25
def norm(s): return ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if c.isalpha())
key = {r['code']: r['value'] for r in csv.DictReader(open(os.path.join(HERE, '..', 'key_f24.tsv')), delimiter='\t') if r['grade'] == 'C'}
units = [(r['cipher_tokens'].split(), norm(r['gloss_text'].replace('[?]', ''))) for r in csv.DictReader(open(os.path.join(HERE, 'c20c21_reconciled.tsv')), delimiter='\t')]
def score(pairs, per=None):
    hits = n = 0
    for toks, g in pairs:
        for i, t in enumerate(toks):
            if t not in key: continue
            n += 1; p = (i + 0.5) / len(toks); v = norm(key[t]); ok = False
            for j in range(len(g) - len(v) + 1):
                if g[j:j+len(v)] == v and abs((j + len(v) / 2) / max(len(g), 1) - p) <= WIN: ok = True; break
            hits += ok
            if per is not None: per.setdefault(t, [0, 0]); per[t][0] += ok; per[t][1] += 1
    return hits, n
per = {}; real, n = score(units, per)
rng = random.Random(SEED); gl = [g for _, g in units]; ctl = []
for _ in range(N):
    while True:
        s = gl[:]; rng.shuffle(s)
        if all(a != b for a, b in zip(s, gl)): break
    ctl.append(score([(t, g) for (t, _), g in zip(units, s)])[0])
ctl.sort(); mean = sum(ctl) / N; p95 = ctl[int(0.95 * N)]; pv = sum(c >= real for c in ctl) / N
print(f"C codes from key_f24: {', '.join(f'{k}={v}' for k, v in sorted(key.items()))}")
print(f"real: {real}/{n} occurrences read their predicted chunk in place; control mean {mean:.2f}, p95 {p95}, max {ctl[-1]}, P(control>=real) {pv:.4f}")
for k in sorted(per): print(f"  {k}={key[k]}: {per[k][0]}/{per[k][1]}")
