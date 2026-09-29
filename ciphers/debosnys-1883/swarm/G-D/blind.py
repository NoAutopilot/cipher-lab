#!/usr/bin/env python3
"""Blind control. make: write 100 unlabeled feature rows (blind_features.jsonl) and the sealed labels (to a path
outside this folder). classify: frozen thresholds -> blind_calls.jsonl (reads only features). unseal: compare."""
import dcore, random, json, sys, os
mode = sys.argv[1]; sealed = sys.argv[2]
if mode == 'make':
    t1, t2 = dcore.target('c1'), dcore.target('c2'); L1 = [len(l) for l in t1]; L2 = [len(l) for l in t2]
    cv = dcore.curve_of(t1 + t2); rng = random.Random(os.urandom(16)); lab = {}
    with open('blind_features.jsonl', 'w') as fo:
        for i in range(100):
            d = 'NULL-IID' if rng.random() < 0.5 else rng.choice(['FR-HOMO', 'EN-HOMO', 'PT-HOMO', 'FR-SYLL'])
            p = rng.choice([0.10, 0.15, 0.20]); x = rng.choice([0, 0.13]); bid = os.urandom(4).hex()
            a, b = dcore.make_pair(d, L1, L2, cv, rng, p, x); lab[bid] = dict(design=d, p=p, x=x)
            fo.write(json.dumps(dict(id=bid, f=dcore.features(a, b, rng))) + '\n')
    json.dump(lab, open(sealed, 'w'))
elif mode == 'classify':
    th = json.load(open('threshold.json'))
    with open('blind_calls.jsonl', 'w') as fo:
        for l in open('blind_features.jsonl'):
            r = json.loads(l); fo.write(json.dumps(dict(id=r['id'], call={w: 'LANGUAGE' if dcore.score(r['f'], w) > th[w]['t'] else 'NULL' for w in th})) + '\n')
elif mode == 'unseal':
    lab = json.load(open(sealed)); calls = [json.loads(l) for l in open('blind_calls.jsonl')]; res = {}
    for w in ('c1', 'c2', 'pair'):
        L = [c for c in calls if lab[c['id']]['design'] != 'NULL-IID']; N = [c for c in calls if lab[c['id']]['design'] == 'NULL-IID']
        tl = sum(c['call'][w] == 'LANGUAGE' for c in L) / len(L); tn = sum(c['call'][w] == 'NULL' for c in N) / len(N)
        miss = {}
        for c in L:
            if c['call'][w] == 'NULL': k = '%s p%s x%s' % (lab[c['id']]['design'], lab[c['id']]['p'], lab[c['id']]['x']); miss[k] = miss.get(k, 0) + 1
        res[w] = dict(n_lang=len(L), n_null=len(N), lang_recall=round(tl, 3), null_recall=round(tn, 3), bal_acc=round((tl + tn) / 2, 3), missed_language=miss)
    print(json.dumps(res, indent=1)); json.dump(dict(result=res, labels=lab), open('blind_result.json', 'w'), indent=1)
