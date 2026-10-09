#!/usr/bin/env python3
"""DV1c supplementary, POST HOC, NOT gating (TXE2-VIV102-ANCHOR, 9 Oct 2026): where in the clerk text does the f.102r stretch
align best? The f.102r collapsed stream is aligned (B.align, same DP/band) to a 2,700-letter window of dec_norm starting at offset s
(dec_norm coordinates; the registered j0 = 1265), published key vs 50 value-shuffled keys (seed 20261009). Prints shares only."""
import os, random, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import anchor as A
B = A.B
pub, let, st, seq, amap, dec = A.stream()
allet = B.sa.letters(open(os.path.join(B.TX, 'dec_norm.txt'), encoding='utf-8').read())
i0, i1 = A.line_starts(st, 'f102r')[0], A.line_starts(st, 'f102v')[0]
seg = seq[i0:i1]
W = 2700
def share(key, w):
    am, dc = B.align(seg, w, key)
    n = sum(1 for k in range(len(seg)) if dc[k] >= 0 and k in am)
    return sum(1 for k in range(len(seg)) if dc[k] >= 0 and k in am and dc[k] == w[am[k]]) / max(1, n)
def scan():
    out = []
    for s in range(0, 5001, 250):
        w = allet[s:s + W]
        real = share(pub, w)
        ids, vv = list(pub), [pub[c] for c in pub]
        rng = random.Random(20261009); sh = []
        for _ in range(50):
            rng.shuffle(vv); sh.append(share(dict(zip(ids, vv)), w))
        r = dict(s=s, real=round(real, 4), shuf_max=round(max(sh), 4), shuf_mean=round(sum(sh) / 50, 4), margin=round(real - max(sh), 4))
        out.append(r); print(json.dumps(r), flush=True)
    json.dump(out, open(os.path.join(HERE, 'j0scan.json'), 'w'), indent=1)


if __name__ == '__main__':
    scan()
