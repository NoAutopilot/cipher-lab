"""D1-F16142A (LANE DEFAULT-account-1-20261006-1240, account 1, 6 Oct 2026): RUN6-NOXALIGN's leave-one-label-out masked alignment with
denser anchors (W: signs spell their published word) and gap <= 5. Pre-registered in PREREG-D1F16142A.md (pushed f0566635a).
    python3 noxalign_dense.py score   -> results/noxalign_dense_summary.json
    python3 noxalign_dense.py check   rule 7: recompute and compare
"""
import collections, difflib, json, os, random, sys
import numpy as np
from keytie import consensus, L_IDX
from decode262 import OUT, gold, tiles
from noxread import stream, label_pile
from noxalign import settle, tom_letter

NG = NK = 200


def recover(units, X, g, gap):
    s, pos = [], []
    for lab, txt in units:
        if lab == X:
            pos.append(len(s)); s.append('*')
        else:
            s.extend(txt)
    if not pos:
        return []
    star = set(pos); out = []
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ''.join(s), g, autojunk=False).get_opcodes():
        if op == 'replace' and i2 - i1 == j2 - j1 <= gap:
            out += [g[j1 + i - i1] for i in range(i1, i2) if i in star]
    return out


def units_for(seq, lp, key, dense):
    u = []
    for t in seq:
        b = t.rstrip('?')
        if dense and b.startswith('W:'):
            u.append((t, b[2:]))
        elif t in lp and key.get(lp[t], -1) >= 0:
            u.append((t, chr(97 + key[lp[t]])))
    return u


def evaluate(units, g, gap):
    ll = {}
    for lab, txt in units:
        if not lab.rstrip('?').startswith('W:'):
            ll[lab] = txt
    rec = {X: recover(units, X, g, gap) for X in sorted(ll)}
    return sum(settle(r) == ll[X] for X, r in rec.items()), rec, ll


def gated(seq, lp, key, g, gap, dense, seed):
    s, rec, ll = evaluate(units_for(seq, lp, key, dense), g, gap)
    rng = random.Random(seed); gn, kn = [], []
    for _ in range(NG):
        h = list(g); rng.shuffle(h); gn.append(evaluate(units_for(seq, lp, key, dense), ''.join(h), gap)[0])
    ks, vs = list(key), list(key.values())
    for _ in range(NK):
        v = vs[:]; rng.shuffle(v); kn.append(evaluate(units_for(seq, lp, dict(zip(ks, v)), dense), g, gap)[0])
    q = lambda xs: dict(n=len(xs), mean=round(float(np.mean(xs)), 3), p99=round(float(np.percentile(xs, 99)), 3), max=max(xs))
    r = dict(S=s, n_masked=len(ll), g_shuffled_gloss=q(gn), k_shuffled_key=q(kn))
    r['verdict'] = 'PASS' if s > r['g_shuffled_gloss']['p99'] and s > r['k_shuffled_key']['p99'] else 'FAIL'
    return r, rec, ll


def compute():
    K = json.load(open(os.path.join(OUT, 'basin_keys.json')))
    seq = stream(); lp = label_pile(); g = gold()
    piles = sorted(set(lp.values()) | {p for _, p in tiles()})
    cL = consensus([K[f'alt{i:02d}'] for i in L_IDX], piles)
    prim, rec, ll = gated(seq, lp, cL, g, 5, True, 16142)
    per = {X: dict(n_signs=sum(t == X for t in seq), basin=ll[X], tomokiyo=tom_letter(X), recovered=len(rec[X]),
                   gloss_letters=''.join(sorted(rec[X])), settled=settle(rec[X])) for X in ll}
    dis = {}
    for X, p in per.items():
        if p['tomokiyo'] and p['tomokiyo'] != p['basin']:
            st = p['settled']
            dis[X] = dict(p, gloss_says=('none' if st is None else 'basin' if st == p['basin'] else
                                         'tomokiyo' if st == p['tomokiyo'] else 'neither'))
    res = dict(primary_dense_gap5=prim,
               reported_dense_gap3=gated(seq, lp, cL, g, 3, True, 16142)[0],
               reported_basin_gap5=gated(seq, lp, cL, g, 5, False, 16142)[0],
               tomokiyo_settled_dense=sum(per[X]['settled'] == per[X]['tomokiyo'] for X in per if per[X]['tomokiyo']),
               per_label=per, disagree_basin_vs_tomokiyo=dis, verdict=prim['verdict'])
    return json.loads(json.dumps(res))


def main(a):
    fn = os.path.join(OUT, 'noxalign_dense_summary.json')
    if a[:1] == ['score']:
        res = compute(); json.dump(res, open(fn, 'w'), indent=1)
        print(json.dumps({k: v for k, v in res.items() if k != 'per_label'}, indent=1))
    elif a[:1] == ['check']:
        if compute() != json.load(open(fn)):
            sys.exit('noxalign_dense_summary.json stale')
        print('noxalign_dense_summary.json up to date')
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    main(sys.argv[1:])
