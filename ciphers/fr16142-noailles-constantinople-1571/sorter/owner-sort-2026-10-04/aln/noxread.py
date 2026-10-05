"""RUN6-NOXREAD (LANE-RUN6 worker, account 1, 5 Oct 2026): N8-NOX2's basin consensus key mapped onto the reconciled c262 reader
signs (witness/c262rc_recon.tsv) through RUN2-NXATL's tile alignment, scored vs c262's gloss with RUN6-NOXDEC's statistic and nulls.
Pre-registered in PREREG-NOXREAD.md (commit 1f39b1f1).
    python3 noxread.py score   -> results/noxread_summary.json
    python3 noxread.py check   rule 7: recompute and compare
"""
import collections, itertools, json, os, random, sys
import numpy as np
from keytie import consensus, L_IDX, NL_IDX, SEEDS
from decode262 import HERE, OUT, T, N, R, gold, tsv

ALN = os.path.join(T, 'run2', 'nxatl', 'c262_tile_alignment.tsv')
REC = os.path.join(T, 'witness', 'c262rc_recon.tsv')


def stream():
    rec = {}
    for ln in open(REC):
        if ln.startswith('#') or not ln.strip():
            continue
        L, toks = ln.rstrip('\n').split('\t', 1); rec[L] = toks.split()
    return [t for L in sorted(rec) for t in rec[L]]


def label_pile():
    merges = json.load(open(os.path.join(HERE, '..', 'summary.json')))['merges']
    c = collections.defaultdict(collections.Counter)
    for r in tsv(ALN):
        if r['recon_label'] not in ('', '-'):
            c[r['recon_label']][merges.get(r['cluster'], r['cluster'])] += 1
    return {lab: min(cnt, key=lambda p: (-cnt[p], p)) for lab, cnt in c.items()}


def decode(seq, lp, key):
    return ''.join(chr(97 + key[lp[t]]) for t in seq if t in lp and key.get(lp[t], -1) >= 0)


def tomokiyo(seq):  # scripts/test0.py's decode, '#' as e2
    out = []
    for t in seq:
        t = t.rstrip('?')
        if t == 'o1/e2':
            t = 'e2'
        if t.startswith('W:'):
            out.append(t[2:])
        elif len(t) > 1 and t[0].isalpha() and t[0].islower() and t[1:].isdigit():
            out.append(t[0])
    return ''.join(out)


def compute():
    K = json.load(open(os.path.join(OUT, 'basin_keys.json')))
    seq = stream(); lp = label_pile(); g = gold()
    piles = sorted(set(lp.values()) | {p for _, p in __import__('decode262').tiles()})
    cL = consensus([K[f'alt{i:02d}'] for i in L_IDX], piles)
    dec = decode(seq, lp, cL); r = R(dec, g)
    rng = random.Random(20261005)
    ks, vs = list(cL), list(cL.values()); a = []
    for _ in range(N):
        v = vs[:]; rng.shuffle(v); a.append(R(decode(seq, lp, dict(zip(ks, v))), g))
    b = []
    for _ in range(N):
        d = list(dec); rng.shuffle(d); b.append(R(''.join(d), g))
    c = [R(decode(seq, lp, consensus([K[f'shuf{s:02d}_alt{i:02d}'] for i in L_IDX], piles)), g) for s in SEEDS]
    NL = [K[f'alt{i:02d}'] for i in NL_IDX]
    d = [R(decode(seq, lp, consensus(list(sub), piles)), g) for sub in itertools.combinations(NL, 6)]
    single = {f'alt{i:02d}': round(R(decode(seq, lp, consensus([K[f'alt{i:02d}']], piles)), g), 4) for i in L_IDX}
    q = lambda xs: dict(n=len(xs), mean=round(float(np.mean(xs)), 4), p99=round(float(np.percentile(xs, 99)), 4),
                        max=round(max(xs), 4))
    labs = sorted(set(seq))
    res = dict(n_signs=len(seq), n_labels=len(labs), n_labels_mapped=sum(l in lp for l in labs),
               n_piles_used=len({lp[l] for l in labs if l in lp}), signs_decoded=len(dec), gloss_letters=len(g),
               R=round(r, 4), a_shuffled_key=q(a), b_letter_order=q(b),
               c_shuffled_dupuy=dict(values=[round(x, 4) for x in c], max=round(max(c), 4)), d_nonlocking=q(d),
               single_L=single, tomokiyo_same_stream=round(R(tomokiyo(seq), g), 4),
               label_pile={l: lp.get(l) for l in labs},
               label_letter={l: (chr(97 + cL[lp[l]]) if l in lp and cL.get(lp[l], -1) >= 0 else None) for l in labs},
               decode=dec)
    ok = r > res['a_shuffled_key']['p99'] and r > res['b_letter_order']['p99'] and r > res['c_shuffled_dupuy']['max'] \
        and r > res['d_nonlocking']['p99']
    res['verdict'] = 'PASS' if ok else 'FAIL'
    return res


def main(a):
    fn = os.path.join(OUT, 'noxread_summary.json')
    if a[:1] == ['score']:
        res = compute(); json.dump(res, open(fn, 'w'), indent=1)
        print(json.dumps({k: v for k, v in res.items() if k not in ('decode', 'label_pile')}, indent=1)); print(res['decode'])
    elif a[:1] == ['check']:
        if compute() != json.load(open(fn)):
            sys.exit('noxread_summary.json stale')
        print('noxread_summary.json up to date')
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    main(sys.argv[1:])
