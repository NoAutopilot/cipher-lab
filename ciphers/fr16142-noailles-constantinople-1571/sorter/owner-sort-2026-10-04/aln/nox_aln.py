#!/usr/bin/env python3
"""NOX-ALN (account 3 worker, 4 Oct 2026): re-run RUN2-NXALN's atlas alignment on the owner's settled labels.
Pre-registered in PREREG.md (same folder). Imports run2/nxaln/nxaln.py unchanged.
    python3 nox_aln.py target            after-sort target, full nulls -> results/target_after.json
    python3 nox_aln.py randmerge N       N random size-matched 18-merge sets, target accuracy only -> results/randmerge.json
    python3 nox_aln.py control P SEED    design control at 108 piles -> results/control_design108_pP_sSEED.json
    python3 nox_aln.py check             rule 7: re-learn the after-sort train key and compare with results/target_after_counts.tsv
"""
import csv, json, os, random, sys
from collections import Counter
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.normpath(os.path.join(HERE, '../../..'))
sys.path.insert(0, os.path.join(T, 'run2', 'nxaln'))
import nxaln as nx
sa = nx.sa
OUT = os.path.join(HERE, 'results')


def tsv(p):
    return list(csv.DictReader((l for l in open(p) if not l.startswith('#')), delimiter='\t'))


rows = [r for r in tsv(os.path.join(T, 'run2', 'nxatl', 'sequences.tsv')) if r['leaf'] != 'c262']
settled = {r['sid']: r for r in tsv(os.path.join(HERE, '..', 'settled_labels.tsv'))}
merges = json.load(open(os.path.join(HERE, '..', 'summary.json')))['merges']
size = Counter(r['cluster'] for r in rows)


def owner_label(r, mp=None):
    """Owner pile for a tile; with mp (a random merge map) the owner's merges are replaced by mp, moves/bad cuts kept."""
    s = settled.get(r['tile'])
    if s is None:
        return r['cluster'] if mp is None else mp.get(r['cluster'], r['cluster'])
    if s['status'] == 'bad-cut':
        return None
    if mp is None:
        return s['new_sign']
    if s['status'] == 'merged':
        return mp.get(r['cluster'], r['cluster'])
    if s['status'] == 'moved':
        return s['new_sign']
    return mp.get(r['cluster'], r['cluster'])


def streams(mp=None, use_owner=True):
    tr, he = [], []
    for r in rows:
        lab = owner_label(r, mp) if use_owner else r['cluster']
        if lab is None:
            continue
        (tr if r['leaf'] in nx.TRAIN_LEAVES else he if r['leaf'] in nx.HELD_LEAVES else []).append(lab)
    return tr, he


def nearest(p, excl, k=8):
    c = [q for q in size if q not in excl]
    return sorted(c, key=lambda q: (abs(size[q] - size[p]), q))[:k]


def ids_of(tr, he):
    ids = {s: n for n, s in enumerate(sorted(set(tr + he)))}
    return ids, [ids[s] for s in tr], [ids[s] for s in he]


def main(a):
    os.makedirs(OUT, exist_ok=True)
    dtext = nx.dupuy_stream()
    if a[0] == 'target':
        tr_s, he_s = streams()
        ids, tr, he = ids_of(tr_s, he_s)
        rng = random.Random(1574)
        res, counts, path, key = nx.run_pipeline(tr, he, dtext, len(ids), 200, rng, sa.letters(nx.fr16_text()),
                                                 'target atlas after owner sort', None)
        res['n_symbols'] = len(ids)
        json.dump(res, open(os.path.join(OUT, 'target_after.json'), 'w'), indent=1)
        inv = {n: s for s, n in ids.items()}
        with open(os.path.join(OUT, 'target_after_counts.tsv'), 'w') as f:
            f.write('pile\t' + '\t'.join(chr(97 + i) for i in range(26)) + '\n')
            for n in range(len(ids)):
                f.write(inv[n] + '\t' + '\t'.join(str(int(x)) for x in counts[n]) + '\n')
        # per-train-tile aligned letter (for step 3)
        with open(os.path.join(OUT, 'target_after_path.tsv'), 'w') as f:
            f.write('train_index\tpile\tletter\n')
            let = sa.letters(dtext)
            for i, j in path:
                f.write(f'{i}\t{tr_s[i]}\t{chr(97 + int(let[j]))}\n')
        print(nx.summary(res))
    elif a[0] == 'randmerge':
        n = int(a[1]); let = sa.letters(dtext); out = []
        for k in range(n):
            rnd = random.Random(20261004 + k)
            mp, used = {}, set()
            for x0, y0 in merges.items():
                x = rnd.choice(nearest(x0, used | {x0}))
                y = rnd.choice(nearest(y0, used | {x, y0}))
                used |= {x, y}; mp[x] = y
            ids, tr, he = ids_of(*streams(mp))
            counts, path = sa.learn(np.array(tr), let, len(ids))
            key = sa.decode(counts)
            jend = path[-1][1] + 1 if path else 0
            acc = sa.nw_score(key[np.array(he)], let[jend:])
            out.append(dict(set=k, acc=round(float(acc), 4), n_symbols=len(ids)))
            print(k, round(float(acc), 4), flush=True)
        json.dump(out, open(os.path.join(OUT, 'randmerge.json'), 'w'), indent=1)
    elif a[0] == 'control':
        p, seed = float(a[1]), int(a[2])
        fr = nx.fr16_text(); tr_real, he_real = streams()
        rng = random.Random(seed)
        L = len(sa.letters(dtext))
        off = len(fr) // 2 + seed * 50000
        words, m = [], 0
        for w in fr[off:].split():
            words.append(w); m += len(w)
            if m >= L:
                break
        ctext = ' '.join(''.join(nx.FOLDS.get(c, c) for c in w) for w in words)
        key = nx.make_design_key(ctext)
        seq = nx.encipher_design(ctext, key, rng)
        noisy = nx.atlas_noise(seq, key[4], rng, p, n_clu=108)
        cut = int(len(noisy) * len(tr_real) / (len(tr_real) + len(he_real)))
        res, *_ = nx.run_pipeline(noisy[:cut], noisy[cut:], ctext, 108, 50, rng, sa.letters(fr[: len(fr) // 2]),
                                  f'control design 108 piles p={p} seed={seed}', None)
        json.dump(res, open(os.path.join(OUT, f'control_design108_p{int(p*100)}_s{seed}.json'), 'w'), indent=1)
        print(nx.summary(res))
    elif a[0] == 'check':
        ids, tr, he = ids_of(*streams())
        counts, _ = sa.learn(np.array(tr), sa.letters(dtext), len(ids))
        for r in tsv(os.path.join(OUT, 'target_after_counts.tsv')):
            if [int(r[chr(97 + i)]) for i in range(26)] != [int(x) for x in counts[ids[r['pile']]]]:
                sys.exit(f"stale at {r['pile']}")
        print('target_after_counts.tsv up to date')
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    main(sys.argv[1:])
