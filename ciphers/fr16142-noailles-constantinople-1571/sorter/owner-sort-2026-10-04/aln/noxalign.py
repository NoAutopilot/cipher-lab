"""RUN6-NOXALIGN (LANE-RUN6 worker, account 1, 5 Oct 2026): leave-one-label-out masked alignment of the c262 basin decode
(RUN6-NOXREAD) to c262's gloss: what the gloss says at each label's positions when that label cannot steer the alignment.
Pre-registered in PREREG-NOXALIGN.md (commit a5c1277d).
    python3 noxalign.py score   -> results/noxalign_summary.json
    python3 noxalign.py check   rule 7: recompute and compare
"""
import collections, difflib, json, os, random, sys
import numpy as np
from keytie import consensus, L_IDX
from decode262 import OUT, gold, tiles
from noxread import stream, label_pile

NG = NK = 200


def recover(units, X, g):
    """units: list of (label, text); signs of X become '*'. Returns gloss letters at recovered '*' positions."""
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
        if op == 'replace' and i2 - i1 == j2 - j1 <= 3:
            out += [g[j1 + i - i1] for i in range(i1, i2) if i in star]
    return out


def settle(rec):
    if len(rec) < 3:
        return None
    c = collections.Counter(rec).most_common()
    if len(c) > 1 and c[0][1] == c[1][1]:
        return None
    return c[0][0] if c[0][1] >= 2 and c[0][1] / len(rec) >= 0.5 else None


def tom_letter(t):
    t = t.rstrip('?')
    if t == 'o1/e2':
        return 'e'
    return t[0] if len(t) > 1 and t[0].isalpha() and t[0].islower() and t[1:].isdigit() else None


def basin_units(seq, lp, key):
    return [(t, chr(97 + key[lp[t]])) for t in seq if t in lp and key.get(lp[t], -1) >= 0]


def run(units, labs, g):
    return {X: recover(units, X, g) for X in labs}


def S(units, labs, g, ll):
    return sum(settle(r) == ll[X] for X, r in run(units, labs, g).items())


def compute():
    K = json.load(open(os.path.join(OUT, 'basin_keys.json')))
    seq = stream(); lp = label_pile(); g = gold()
    piles = sorted(set(lp.values()) | {p for _, p in tiles()})
    cL = consensus([K[f'alt{i:02d}'] for i in L_IDX], piles)
    units = basin_units(seq, lp, cL); labs = sorted({u[0] for u in units})
    ll = {X: dict(units)[X] for X in labs}
    rec = run(units, labs, g); s = sum(settle(rec[X]) == ll[X] for X in labs)
    tl = {X: tom_letter(X) for X in labs}
    rng = random.Random(20261005); gn = []
    for _ in range(NG):
        h = list(g); rng.shuffle(h); gn.append(S(units, labs, ''.join(h), ll))
    ks, vs = list(cL), list(cL.values()); kn = []
    for _ in range(NK):
        v = vs[:]; rng.shuffle(v); kk = dict(zip(ks, v)); u = basin_units(seq, lp, kk)
        kn.append(S(u, sorted({x[0] for x in u}), g, {x[0]: x[1] for x in u}))
    # Tomokiyo-anchored reference: W: signs spell their word, letter labels masked
    tu = []
    for t in seq:
        b = t.rstrip('?')
        if b.startswith('W:'):
            tu.append((t, b[2:]))
        elif tom_letter(t):
            tu.append((t, tom_letter(t)))
    tlabs = sorted({x[0] for x in tu if tom_letter(x[0])})
    trec = run(tu, tlabs, g)
    q = lambda xs: dict(n=len(xs), mean=round(float(np.mean(xs)), 3), p99=round(float(np.percentile(xs, 99)), 3), max=max(xs))
    per = {X: dict(n_signs=sum(u[0] == X for u in units), basin=ll[X], tomokiyo=tl[X], recovered=len(rec[X]),
                   gloss_letters=''.join(sorted(rec[X])), settled=settle(rec[X])) for X in labs}
    dis = {}
    for X, p in per.items():
        if p['tomokiyo'] and p['tomokiyo'] != p['basin']:
            st = p['settled']
            dis[X] = dict(p, gloss_says=('none' if st is None else 'basin' if st == p['basin'] else
                                         'tomokiyo' if st == p['tomokiyo'] else 'neither'))
    res = dict(n_labels=len(labs), S=s, g_shuffled_gloss=q(gn), k_shuffled_key=q(kn),
               tomokiyo_settled_basin_anchor=sum(per[X]['settled'] == tl[X] for X in labs if tl[X]),
               tomokiyo_anchor_ref=dict(n_letter_labels=len(tlabs),
                                        settled_to_tomokiyo=sum(settle(trec[X]) == tom_letter(X) for X in tlabs),
                                        settled_any=sum(settle(trec[X]) is not None for X in tlabs)),
               per_label=per, disagree_basin_vs_tomokiyo=dis)
    res['verdict'] = 'PASS' if s > res['g_shuffled_gloss']['p99'] and s > res['k_shuffled_key']['p99'] else 'FAIL'
    return res


def main(a):
    fn = os.path.join(OUT, 'noxalign_summary.json')
    if a[:1] == ['score']:
        res = compute(); json.dump(res, open(fn, 'w'), indent=1)
        print(json.dumps({k: v for k, v in res.items() if k != 'per_label'}, indent=1))
    elif a[:1] == ['check']:
        if compute() != json.load(open(fn)):
            sys.exit('noxalign_summary.json stale')
        print('noxalign_summary.json up to date')
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    main(sys.argv[1:])
