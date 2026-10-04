#!/usr/bin/env python3
"""Known-answer check (rule 3) for Tomokiyo's D'Avaux key on Baluze 167 f.157r, whose cipher runs carry a period
interlinear decipherment (gloss.tsv). Expected values are the gloss phrase split along the cipher tokens by hand
(EXPECTED below); agreement = tokens whose key value equals the expected value. Null: the same key with its values
shuffled within each sign class (acute / diaeresis / overbar / plain / letter), 2000 draws, seed 1.
  python3 known_answer.py           prints real and null agreement; exit 1 if real < 0.8 or real <= null p99
"""
import csv, random, re, sys, os
D = os.path.dirname(os.path.abspath(__file__))
# gloss 'le lieu ou l'on traitera la paix generale' / 'des gens raisonnables', split along the tokens of ciphertext.txt
EXPECTED = {
 '167f157 L03': [None, None, None, 'le', 'li', 'e', 'u', 'o', 'u', 'lo', 'n', 'traitte', 'ra', 'la', 'pa', 'i', 'x', 'general', 'le'],
 '167f157 R2':  [None, None, 'des', 'ge', 'n', 's', 'ra', 'i', 'so', 'n', 'n', 'a', 'b', 'le', 's'],
}
key = {}
for r in csv.reader((l for l in open(f'{D}/key.tsv') if not l.startswith('#')), delimiter='\t'):
    if r[0] != 'code': key[r[0]] = r[1]
toks = {}
for l in open(f'{D}/ciphertext.txt'):
    if l.startswith('#') or '|' not in l: continue
    h, b = l.split('|', 1); toks[h.strip()] = [t.rstrip('?') for t in b.split()]
def cls(c):
    return 'L' if c.startswith('L:') else c[-1] if c[-1] in "':=" else 'plain'
def score(k):
    n = ok = 0
    for line, exp in EXPECTED.items():
        for t, e in zip(toks[line], exp):
            if e is None or t.startswith('w:'): continue
            n += 1; ok += k.get(t) == e
    return ok, n
ok, n = score(key)
groups = {}
for c in key: groups.setdefault(cls(c), []).append(c)
rng = random.Random(1); nulls = []
for _ in range(2000):
    k2 = {}
    for g, cs in groups.items():
        vs = [key[c] for c in cs]; rng.shuffle(vs); k2.update(zip(cs, vs))
    nulls.append(score(k2)[0] / n)
nulls.sort(); p99 = nulls[int(0.99 * len(nulls))]
num = [(t, e) for line, exp in EXPECTED.items() for t, e in zip(toks[line], exp) if e and not t.startswith(('w:', 'L:'))]
nok = sum(key.get(t) == e for t, e in num)
print(f'real agreement {ok}/{n} = {ok/n:.3f} (numeral codes only {nok}/{len(num)}); shuffled-key null mean {sum(nulls)/len(nulls):.3f}, p99 {p99:.3f}')
sys.exit(0 if ok / n >= 0.8 and ok / n > p99 else 1)
