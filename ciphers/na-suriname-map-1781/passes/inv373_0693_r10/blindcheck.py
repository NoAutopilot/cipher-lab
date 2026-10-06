#!/usr/bin/env python3
"""R10-SUR693: how far the reconciler's sign reads (align_words.tsv, read with the gloss in view) are matched by the Sonnet
blind pass (passA_sonnet_blind.tsv, read without values). Per aligned word: best position-wise match of the word's sign
sequence against any same-length window of the blind tokens of the same line; reports exact-sign agreement. Writes blindcheck.out."""
import os
H = os.path.dirname(os.path.abspath(__file__))
N = {'[ij]': '[y-fam]', 'y': '[y-fam]', '[lambda]': 'λ', '[d-loop]': '[ezh-dot]', 'd': None}
def n(t):
    t = t.rstrip('?')
    return N.get(t, t) if t not in ('d',) else t
blind = {}
for l in open(os.path.join(H, 'passA_sonnet_blind.tsv'), encoding='utf-8'):
    f = l.rstrip('\n').split('\t')
    if len(f) > 2 and f[1] == 'cipher':
        blind[f[0]] = [n(t) for t in f[2].split() if t not in ('|', '/', ',', ';', ':', "'")]
tot = same = 0; rv_tot = rv_same = 0; out = []
for l in open(os.path.join(H, 'align_words.tsv'), encoding='utf-8'):
    if l.startswith('#') or l.startswith('line\t'): continue
    f = l.rstrip('\n').split('\t')
    if f[3] != 'aligned': continue
    s = f[2].split(); b = blind.get(f[0], []); best = 0
    for i in range(0, max(1, len(b) - len(s) + 1)):
        best = max(best, sum(1 for a, c in zip(s, b[i:i+len(s)]) if a == c))
    tot += len(s); same += best
    if f[4] == '1': rv_tot += len(s); rv_same += best
    out.append(f'{f[0]}\t{f[1]}\t{best}/{len(s)}')
r = f'blind pass matches reconciler sign reads at {same}/{tot} positions ({same/tot:.3f}); rv=1 words {rv_same}/{rv_tot}'
open(os.path.join(H, 'blindcheck.out'), 'w').write(r + '\n' + '\n'.join(out) + '\n'); print(r)
