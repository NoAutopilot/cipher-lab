#!/usr/bin/env python3
"""TXD-HOLDOUT (3 Oct 2026): held-out controls for the TX-DECODE lam-4 rank-1 results (PREREG.md in this folder, pushed
before any score). Run from ciphers/: python3 nevers-birago-fr3251-1572/harvest/tx_decode/holdout/holdout.py [c|a|b|all]
Writes holdout/<part>.json. Disk only."""
import json, random, statistics, sys, time
from multiprocessing import Pool
sys.path.insert(0, '../tools'); import key_decode_lattice as K
from judge_plaintext import LANG_CORPORA, NgramModel, read_corpus
H = 'nevers-birago-fr3251-1572/harvest/'; O = H + 'tx_decode/'; D = O + 'holdout/'
KEY = K.read_key(H + 'key_1572_sheet.tsv'); CLERK = K.read_key(H + 'key_1572_clerkvar.tsv')
LETTERS = [('f144r', 'it16dip'), ('f168', 'it16dip'), ('f117', 'fr')]
LAMS = [1.0, 2.0, 3.0, 4.0, 6.0, 8.0]
_M = {}

def model(g):
    if g not in _M:
        m = NgramModel([read_corpus(p) for p in LANG_CORPORA[g]]); _M[g] = (m, K.LM(m))
    return _M[g]

def score(lat, key, g, lam):
    m, lm = model(g)
    seq = K.viterbi(lat, key, lm, lam, 64)[0]
    return m.score(K.text_of(seq, key)), seq

def w1_keys(n, seed):
    """partition-preserving relabelings: distinct letters permuted among themselves, distinct words among themselves."""
    rnd = random.Random(seed); vals = sorted(set(KEY.values()) - {''})
    let = [v for v in vals if len(v) == 1]; wd = [v for v in vals if len(v) > 1]; out = []
    while len(out) < n:
        a = let[:]; b = wd[:]; rnd.shuffle(a); rnd.shuffle(b)
        if a == let and b == wd:
            continue
        mp = dict(zip(let, a)); mp.update(zip(wd, b)); mp[''] = ''
        out.append({s: mp[v] for s, v in KEY.items()})
    return out

def w2_keys():
    let = sorted({v for v in KEY.values() if len(v) == 1}); out = []
    for k in range(1, len(let)):
        mp = {c: let[(i + k) % len(let)] for i, c in enumerate(let)}
        out.append({s: mp.get(v, v) for s, v in KEY.items()})
    return out

def job(args):
    L, g, lam, kind, idx, key = args
    lat = K.read_topk(O + L + '_topk.tsv')
    return (L, lam, kind, idx, score(lat, key, g, lam)[0])

def part_c():
    lat = K.read_topk(O + 'no87_topk.tsv')
    truth = {(r['line'], r['pos']): r['value'] for r in K.read_tsv(O + 'truth87.tsv')}
    def held(line):
        return line.startswith('f178r') or line.startswith('f179r') or (line.startswith('f178v_L') and int(line[7:]) >= 12)
    res = []
    for lam in LAMS:
        _, seq = score(lat, KEY, 'it16dip', lam)
        tot = wrong = unk = 0
        for (k, _), c in zip(lat, seq):
            kk = (k[0], str(k[1])) if isinstance(k, tuple) else k
            t = truth.get(kk)
            if t is None or not held(kk[0]):
                continue
            tot += 1
            if c not in KEY: unk += 1
            elif KEY[c] != t: wrong += 1
        res.append({'lam': lam, 'aligned': tot, 'wrong': wrong, 'U': unk, 'err': wrong / tot, 'err_U': (wrong + unk) / tot})
        print('c', res[-1], flush=True)
    best = min(res, key=lambda r: (r['err'], r['err_U'], abs(r['lam'] - 1)))
    out = {'held_out_lines': 'f178v_L12-L23, f178r_*, f179r_*', 'rows': res, 'chosen_lam': best['lam']}
    json.dump(out, open(D + 'c.json', 'w'), indent=1); return out

def part_a(lam=4.0, tag='a'):
    w1 = w1_keys(200, 11); w2 = w2_keys(); jobs = []
    for L, g in LETTERS:
        jobs.append((L, g, lam, 'printed', 0, KEY)); jobs.append((L, g, lam, 'clerkvar', 0, CLERK))
        jobs += [(L, g, lam, 'W1', i, k) for i, k in enumerate(w1)]
        jobs += [(L, g, lam, 'W2', i, k) for i, k in enumerate(w2)]
    with Pool(4) as p:
        rows = p.map(job, jobs, chunksize=8)
    out = {}
    for L, g in LETTERS:
        r = [x for x in rows if x[0] == L]
        pr = [x[4] for x in r if x[2] == 'printed'][0]; cl = [x[4] for x in r if x[2] == 'clerkvar'][0]
        s1 = [x[4] for x in r if x[2] == 'W1']; s2 = [x[4] for x in r if x[2] == 'W2']
        rk1, z1, mu1, mx1 = K.rank_z(pr, s1); rk2, z2, mu2, mx2 = K.rank_z(pr, s2)
        out[L] = {'lam': lam, 'printed': pr, 'clerkvar': cl,
                  'W1': {'n': len(s1), 'rank': rk1, 'z': z1, 'mean': mu1, 'max': mx1, 'n_ge_printed': sum(s >= pr for s in s1)},
                  'W2': {'n': len(s2), 'rank': rk2, 'z': z2, 'mean': mu2, 'max': mx2, 'n_ge_printed': sum(s >= pr for s in s2)},
                  'gate_a': 'PASS' if pr > max(s1 + s2) else 'FAIL'}
        print(tag, L, json.dumps(out[L]), flush=True)
    json.dump(out, open(D + tag + '.json', 'w'), indent=1); return out

def bjob(args):
    L, g, lam = args
    m, lm = model(g); lat = K.read_topk(O + L + '_topk.tsv')
    c = K.control(lat, KEY, lm, m, 200, 1, lam, 64)
    return (L, lam, c['lattice']['rank'], c['lattice']['z'], c['lattice']['real'], c['lattice']['shuf_max'])

def part_b():
    with Pool(4) as p:
        rows = p.map(bjob, [(L, g, lam) for L, g in LETTERS for lam in LAMS])
    out = {}
    for L, _ in LETTERS:
        r = sorted([x for x in rows if x[0] == L], key=lambda x: x[1])
        ranks = {x[1]: x[2] for x in r}
        n1 = sum(1 for v in ranks.values() if v == 1); others = sum(1 for l, v in ranks.items() if v == 1 and l != 4.0)
        lab = ('robust' if all(ranks[l] == 1 for l in (3.0, 4.0, 6.0)) and n1 >= 4 else
               'tuned-only' if ranks[4.0] == 1 and others <= 2 else 'mixed')
        out[L] = {'rows': [{'lam': x[1], 'rank': x[2], 'z': x[3], 'real': x[4], 'shuf_max': x[5]} for x in r], 'label': lab}
        print('b', L, lab, [(x[1], x[2], round(x[3], 2)) for x in r], flush=True)
    json.dump(out, open(D + 'b.json', 'w'), indent=1); return out

if __name__ == '__main__':
    what = sys.argv[1] if len(sys.argv) > 1 else 'all'; t = time.time()
    if what in ('c', 'all'): part_c()
    if what in ('a', 'all'): part_a()
    if what in ('b', 'all'): part_b()
    print('elapsed', round(time.time() - t), 's')

# ---- post-hoc diagnostic (NOT pre-registered; added after parts a-c were scored): can gate (a) fail? Same W1/W2 gate on
# position-shuffled lattices (seeds 100-104, as shuffled_target.py). If the printed key still beats every wrong key on a
# shuffled target, gate (a) measures letter-frequency fit, not text, and its PASS on the real order licenses little.
def sjob(args):
    L, g, seed, kind, idx, key = args
    lat = K.read_topk(O + L + '_topk.tsv'); random.Random(seed).shuffle(lat)
    return (L, seed, kind, idx, score(lat, key, g, 4.0)[0])

def part_ad():
    w1 = w1_keys(200, 11); w2 = w2_keys(); jobs = []
    for L, g in LETTERS:
        for sd in range(100, 105):
            jobs.append((L, g, sd, 'printed', 0, KEY))
            jobs += [(L, g, sd, 'W', i, k) for i, k in enumerate(w1 + w2)]
    with Pool(4) as p:
        rows = p.map(sjob, jobs, chunksize=8)
    out = {}
    for L, _ in LETTERS:
        out[L] = []
        for sd in range(100, 105):
            r = [x for x in rows if x[0] == L and x[1] == sd]
            pr = [x[4] for x in r if x[2] == 'printed'][0]; s = [x[4] for x in r if x[2] == 'W']
            rk, z, mu, mx = K.rank_z(pr, s)
            out[L].append({'seed': sd, 'rank': rk, 'z': z, 'n_ge_printed': sum(v >= pr for v in s), 'gate_a': 'PASS' if pr > mx else 'FAIL'})
        print('ad', L, [(d['rank'], round(d['z'], 2)) for d in out[L]], flush=True)
    json.dump(out, open(D + 'a_shuffled_target.json', 'w'), indent=1); return out

if __name__ == '__main__' and len(sys.argv) > 1 and sys.argv[1] == 'ad':
    part_ad()
