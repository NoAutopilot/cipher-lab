#!/usr/bin/env python3
"""R10-SURV (verifier): PREREG_SURV.md re-test of R10-SUR693's same-system gate on the Sonnet blind pass tokens.
Writes verify_blind.out. Run from anywhere: python3 verify_blind.py"""
import os, random, collections
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.join(H, '..', '..')
key = {}
for l in open(os.path.join(T, 'key_period_codes_nieuw.tsv'), encoding='utf-8'):
    if l.startswith('#') or l.startswith('code\t') or not l.strip(): continue
    f = l.rstrip('\n').split('\t'); key[f[0]] = f[1]
EQ = {'j': 'i', 'y': 'i', 'ij': 'i', 'u': 'v'}
norm = lambda c: EQ.get(c, c)
N = {'[ij]': '[y-fam]', 'y': '[y-fam]', '[lambda]': 'λ', '[d-loop]': '[ezh-dot]'}
def letters(w):
    out, i = [], 0
    while i < len(w):
        if w[i:i+2] == 'ij': out.append('ij'); i += 2
        else: out.append(w[i]); i += 1
    return out
blind = {}
for l in open(os.path.join(H, 'passA_sonnet_blind.tsv'), encoding='utf-8'):
    f = l.rstrip('\n').split('\t')
    if len(f) > 2 and f[1] == 'cipher':
        toks = [t for t in f[2].split() if t not in ('|', '/', ',', ';', ':', "'")]
        blind[f[0]] = [None if t.startswith('[?') or t.endswith('?') else N.get(t, t) for t in toks]
pairs = []
for l in open(os.path.join(H, 'align_words.tsv'), encoding='utf-8'):
    if l.startswith('#') or l.startswith('line\t'): continue
    f = l.rstrip('\n').split('\t')
    if f[3] != 'aligned': continue
    s, p, b = f[2].split(), letters(f[1]), blind.get(f[0], [])
    best, bi = -1, 0
    for i in range(0, max(1, len(b) - len(s) + 1)):
        m = sum(1 for a, c in zip(s, b[i:i+len(s)]) if a == c)
        if m > best: best, bi = m, i
    pairs += [(bt, x, rc) for bt, x, rc in zip(b[bi:bi+len(s)], p, s) if bt is not None]
def ag(c, x): return any(norm(v) == norm(x) for v in key[c].split('|'))
def stat(pp):
    k = [(c, x) for c, x, *_ in pp if c in key]
    return sum(ag(c, x) for c, x in k) / len(k), len(k)
real, n = stat(pairs)
rnd = random.Random(6930); xs = [p[1] for p in pairs]; ctl = []
for _ in range(1000):
    rnd.shuffle(xs); ctl.append(stat([(p[0], x) for p, x in zip(pairs, xs)])[0])
ctl.sort(); p99 = ctl[989]; mean = sum(ctl) / len(ctl)
gate = 'SAME SYSTEM (blind)' if real >= 0.60 and real > p99 else 'not shown'
out = [f'blind tokens paired {len(pairs)}, keyed {n}, agree {real:.3f}; control mean {mean:.3f} p99 {p99:.3f} -> {gate}']
# descriptive: blind reads at the reconciler's candidate-code positions
for rc in ('S', '[x-dot]', 'b', 't', 'g', 'n', '[h-sec]', '[y-fam]', 'x'):
    c = collections.Counter(f'{bt}={x}' for bt, x, r in pairs if r == rc)
    out.append(f'reconciler {rc}: blind reads ' + (' '.join(f'{k}:{v}' for k, v in c.most_common()) or '(none paired)'))
open(os.path.join(H, 'verify_blind.out'), 'w').write('\n'.join(out) + '\n'); print('\n'.join(out))
