#!/usr/bin/env python3
"""R2-5 second instrument: group B's fit-vs-shuffle gap on split texts (PREREG.md, last section).
One job = one text instance: fit B's annealer (G-B/hsolve5b, English Witten-Bell 5-gram) on the real order and on 2
order-shuffled copies (gb.shuffled_stream); gap = per-window fit (real) - mean per-window fit (shuffled).
Usage: bgap.py TEXT INSTANCE OUT     TEXT in real-T real-N folger null-T  (null-T = NULL-SPLIT of real-T at 0.20)
Needs G-B's model5_en.bin and hsolve5b built (not committed; G-B/.gitignore)."""
import os, sys, json, random
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..', '..', 'G-B'))
import gb, r25

R, I = 20, 3000000

def stream(lines):
    out = []
    for l in lines: out += l + [None]
    return out[:-1]

def fit(st, seed):
    signs, seq = gb.encode(st); gb.ROBUST = 0.1
    best, _, _ = gb.run_solver(seq, len(signs), R, I, seed, 1.0, 2.5, model=gb.MODELS[5])
    nwin = sum(1 for i in range(len(seq) - 4) if min(seq[i:i + 5]) >= 0)
    return best / nwin

if __name__ == '__main__':
    tid, inst, out = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    if tid.startswith('real'):
        M = r25.REAL_MAPS[tid]; lines = r25.apply_split(r25.R1, M) + r25.apply_split(r25.R2, M)
    elif tid == 'folger':
        rng = random.Random(f'r25-bgap-folger-{inst}'); boxes, M = r25.text_source('folger', rng)
        a, b = r25.noisy_pair(boxes, M, rng, 0.20); lines = a + b
    elif tid == 'null-T':
        _, _, _, ids, M = r25.shape('real-T'); rng = random.Random(f'r25-bgap-null-{inst}')
        a, b = r25.null_split(ids, M, rng, 0.20); lines = a + b
    st = stream(lines)
    real = fit(st, 1); sh = [fit(gb.shuffled_stream(st, 100 + k), 1) for k in range(2)]
    res = dict(text=tid, inst=inst, N=sum(map(len, lines)), K=len({s for l in lines for s in l}), R=R, I=I,
               real=round(real, 4), shuffled=[round(x, 4) for x in sh], gap=round(real - sum(sh) / 2, 4))
    json.dump(res, open(out, 'w')); print(res)
