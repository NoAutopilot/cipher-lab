#!/usr/bin/env python3
"""A1-POSNULL (3 Oct 2026): position-shuffled-lattice null for the printed 1572 key at lam 4 (PREREG.md in this folder,
pushed before any score). Run from ciphers/: python3 nevers-birago-fr3251-1572/harvest/tx_decode/posnull/posnull.py
Writes posnull/posnull.json. Disk only."""
import json, random, statistics, sys, time
from multiprocessing import Pool
sys.path.insert(0, '../tools'); import key_decode_lattice as K
from judge_plaintext import LANG_CORPORA, NgramModel, read_corpus
O = 'nevers-birago-fr3251-1572/harvest/tx_decode/'; D = O + 'posnull/'
KEY = K.read_key('nevers-birago-fr3251-1572/harvest/key_1572_sheet.tsv')
LETTERS = [('f144r', 'it16dip'), ('f168', 'it16dip'), ('f117', 'fr')]
SEEDS = list(range(1000, 1200)); _M = {}

def model(g):
    if g not in _M:
        m = NgramModel([read_corpus(p) for p in LANG_CORPORA[g]]); _M[g] = (m, K.LM(m))
    return _M[g]

def job(args):
    L, g, seed = args
    m, lm = model(g); lat = K.read_topk(O + L + '_topk.tsv')
    if seed is not None:
        random.Random(seed).shuffle(lat)
    c = K.control(lat, KEY, lm, m, 200, 1, 4.0, 64)['lattice']
    return (L, seed, c['real'], c['rank'], c['z'])

if __name__ == '__main__':
    t = time.time(); jobs = [(L, g, s) for L, g in LETTERS for s in [None] + SEEDS]
    with Pool(4) as p:
        rows = p.map(job, jobs, chunksize=4)
    out = {}
    for L, _ in LETTERS:
        real = [r for r in rows if r[0] == L and r[1] is None][0]; sh = [r for r in rows if r[0] == L and r[1] is not None]
        S = sorted(r[2] for r in sh); Z = sorted(r[4] for r in sh); p95 = S[189]; zp95 = Z[189]
        g = 'PASS' if real[3] == 1 and real[2] > p95 else 'FAIL'
        out[L] = {'n_shuf': len(sh), 'real_S': real[2], 'real_rank': real[3], 'real_z': real[4],
                  'shuf_S_p95': p95, 'shuf_S_max': S[-1], 'shuf_S_mean': statistics.mean(S),
                  'real_S_rank_among_shuf': 1 + sum(s >= real[2] for s in S),
                  'shuf_rank1_frac': sum(r[3] == 1 for r in sh) / len(sh), 'shuf_rank_median': statistics.median(r[3] for r in sh),
                  'shuf_z_p95': zp95, 'shuf_z_max': Z[-1], 'gate': g,
                  'per_seed': [{'seed': r[1], 'S': r[2], 'rank': r[3], 'z': r[4]} for r in sh]}
        print(L, {k: v for k, v in out[L].items() if k != 'per_seed'}, flush=True)
    json.dump(out, open(D + 'posnull.json', 'w'), indent=1); print('elapsed', round(time.time() - t), 's')
