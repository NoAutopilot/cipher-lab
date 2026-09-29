#!/usr/bin/env python3
"""H37 (29 Sept 2026): the numeral-shaped ids (EIGHT, NINE, NINE-BAR, NINE-DASH, SIX-CURL, THREE, FIVE, TWO, SEVEN;
31 settled tokens). If Debosnys wrote numbers in digits inside the cipher (as the clear 516 inside No.9), numeral ids
would sit next to each other; if they are ordinary cipher signs that happen to look like digits they scatter.
Statistics on the settled lines (punctuation dropped): numeral-numeral adjacencies, line-initial / line-final
numerals, against 10,000 within-line shuffles; the same adjacency count on Bourdeau's No.9 read (tokens with a digit
word in their code: EIGHT/NINE/... or NUM_*, or the digit glyph codes he uses). Also each numeral's neighbours.
Writes h37_numerals.json."""
import os, json, random, collections, sys, re
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here); repo = os.path.dirname(os.path.dirname(root))
sys.path.insert(0, here); from settled_lines import settled_lines
PUNCT = {'BLOB', 'HOOK-L', 'DASH-H', '_', 'MULTI'}
NUM = {'EIGHT', 'NINE', 'NINE-BAR', 'NINE-DASH', 'SIX-CURL', 'THREE', 'FIVE', 'TWO', 'SEVEN'}
lines = [(k, [s for s in v if s not in PUNCT]) for k, v in settled_lines(root, 'c').items()]
lines = [(k, l) for k, l in lines if len(l) >= 2]
def prof(ls, isn):
    adj = ini = fin = 0
    for l in ls:
        adj += sum(isn(a) and isn(b) for a, b in zip(l, l[1:])); ini += isn(l[0]); fin += isn(l[-1])
    return adj, ini, fin
def test(ls, isn, T=10000, seed=37):
    rng = random.Random(seed); obs = prof(ls, isn); null = []
    for _ in range(T):
        sh = []
        for l in ls: c = l[:]; rng.shuffle(c); sh.append(c)
        null.append(prof(sh, isn))
    res = {}
    for i, n in enumerate(('adjacent', 'line_initial', 'line_final')):
        v = sorted(x[i] for x in null); res[n] = dict(obs=obs[i], lo=v[250], hi=v[9749], p_ge=sum(x >= obs[i] for x in v) / T)
    return res
out = dict(ours=test([l for _, l in lines], lambda s: s in NUM), tokens=sum(s in NUM for _, l in lines for s in l))
out['neighbours'] = [(k, i, ' '.join(l[max(0, i - 2):i + 3])) for k, l in lines for i, s in enumerate(l) if s in NUM]
sys.path.insert(0, os.path.join(repo, 'sources/bourdeau/cyphersolver-targets-debosnys')); import n9_transcription as n9
B = [[t for t in l.split() if not t.startswith('CLEAR')] for l in n9.N9]
bnum = lambda t: t.startswith('NUM') or bool(re.match(r'^(EIGHT|NINE|SIX|THREE|FIVE|TWO|SEVEN|D3|GAM9|Z7|B3|Z3|8|9|6|3|5|2|7)', t))
out['bourdeau_n9'] = test(B, bnum); out['bourdeau_n9_tokens'] = sum(bnum(t) for l in B for t in l)
out['bourdeau_n9_types'] = sorted({t for l in B for t in l if bnum(t)})
print('ours', out['tokens'], out['ours']); print('bourdeau', out['bourdeau_n9_tokens'], out['bourdeau_n9_types'], out['bourdeau_n9'])
for x in out['neighbours']: print(x)
json.dump(out, open(os.path.join(root, 'h37_numerals.json'), 'w'), indent=1)
