"""RUN6-NOXDEC (LANE-RUN6 worker, account 1, 5 Oct 2026): decode c262 (not aligned to Dupuy) with N8-NOX2's count-based basin
consensus key and score it against c262's period gloss with test0.py's statistic. Pre-registered in PREREG-DECODE.md (commit 6de3a59e).
    python3 decode262.py score   -> results/decode262_summary.json
    python3 decode262.py check   rule 7: recompute and compare with results/decode262_summary.json
"""
import csv, difflib, itertools, json, os, random, re, sys
import numpy as np
from keytie import consensus, L_IDX, NL_IDX, SEEDS

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'results')
T = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
N = 1000


def norm(s):  # scripts/test0.py's norm, verbatim
    s = s.lower().replace('v', 'u').replace('j', 'i').replace('y', 'i')
    s = re.sub(r'[éèêë]', 'e', s)
    return re.sub(r'[^a-z]', '', s)


def tsv(p):
    return list(csv.DictReader((l for l in open(p) if not l.startswith('#')), delimiter='\t'))


def tiles():
    merges = json.load(open(os.path.join(HERE, '..', 'summary.json')))['merges']
    rows = [r for r in tsv(os.path.join(T, 'run2', 'nxatl', 'sequences.tsv')) if r['leaf'] == 'c262']
    rows.sort(key=lambda r: (r['line'], int(r['pos'])))
    return [(r['cluster'], merges.get(r['cluster'], r['cluster'])) for r in rows]


def gold():
    gl = {}
    for ln in open(os.path.join(T, 'gloss.tsv')):
        if ln.startswith('#') or not ln.strip():
            continue
        p = ln.rstrip('\n').split('\t'); gl[p[0]] = p[1] if len(p) > 1 else ''
    return norm(''.join(gl[l] for l in sorted(gl)))


def R(dec, g):
    return difflib.SequenceMatcher(None, norm(dec), g, autojunk=False).ratio()


def decode(seq, key):
    return ''.join(chr(97 + key[p]) for p in seq if key.get(p, -1) >= 0)


def compute():
    K = json.load(open(os.path.join(OUT, 'basin_keys.json')))
    tl = tiles(); seq = [p for _, p in tl]; piles = sorted(set(seq)); g = gold()
    L = [K[f'alt{i:02d}'] for i in L_IDX]
    cL = consensus(L, piles)
    dec = decode(seq, cL); r = R(dec, g)
    rng = random.Random(20261005)
    ks, vs = list(cL), list(cL.values()); a = []
    for _ in range(N):
        v = vs[:]; rng.shuffle(v); a.append(R(decode(seq, dict(zip(ks, v))), g))
    b = []
    for _ in range(N):
        d = list(dec); rng.shuffle(d); b.append(R(''.join(d), g))
    c = [R(decode(seq, consensus([K[f'shuf{s:02d}_alt{i:02d}'] for i in L_IDX], piles)), g) for s in SEEDS]
    NL = [K[f'alt{i:02d}'] for i in NL_IDX]
    d = [R(decode(seq, consensus(list(sub), piles)), g) for sub in itertools.combinations(NL, 6)]
    single = {f'alt{i:02d}': round(R(decode(seq, consensus([K[f'alt{i:02d}']], piles)), g), 4) for i in L_IDX}
    prov = {x['cluster']: x['label'].split('/')[0] for x in tsv(os.path.join(T, 'run2', 'nxatl', 'cluster_provisional_names.tsv'))}
    pdec = ''.join(prov.get(raw, '')[2:] if prov.get(raw, '').startswith('W:') else
                   (prov.get(raw, '')[:1] if prov.get(raw, '')[:1].islower() else '') for raw, _ in tl)
    q = lambda xs: dict(n=len(xs), mean=round(float(np.mean(xs)), 4), p99=round(float(np.percentile(xs, 99)), 4),
                        max=round(max(xs), 4))
    res = dict(n_tiles=len(seq), n_piles=len(piles), n_piles_keyed=sum(cL.get(p, -1) >= 0 for p in piles),
               decoded_letters=len(dec), gloss_letters=len(g), R=round(r, 4),
               a_shuffled_key=q(a), b_letter_order=q(b), c_shuffled_dupuy=dict(values=[round(x, 4) for x in c], max=round(max(c), 4)),
               d_nonlocking=q(d), single_L=single, provisional_ceiling=round(R(pdec, g), 4), decode=dec)
    ok = r > res['a_shuffled_key']['p99'] and r > res['b_letter_order']['p99'] and r > res['c_shuffled_dupuy']['max'] \
        and r > res['d_nonlocking']['p99']
    res['verdict'] = 'PASS' if ok else 'FAIL'
    return res


def main(a):
    if a[:1] == ['score']:
        res = compute()
        json.dump(res, open(os.path.join(OUT, 'decode262_summary.json'), 'w'), indent=1)
        print(json.dumps({k: v for k, v in res.items() if k != 'decode'}, indent=1)); print(res['decode'])
    elif a[:1] == ['check']:
        if compute() != json.load(open(os.path.join(OUT, 'decode262_summary.json'))):
            sys.exit('decode262_summary.json stale')
        print('decode262_summary.json up to date')
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    main(sys.argv[1:])
