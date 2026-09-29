#!/usr/bin/env python3
"""HARNESS-2 self-test of bar v2 (29 Sept 2026), the known-answer controls of PREREG.md: K1 planted FR-HOMO key,
K2 random permutation of it, K4 climber on NULL, K5 climber on FR-HOMO and FR-HOMO-N15 (reachability), each on both
pairs with the harness climber as the refit fitter (50 refits per direction). K3 (group B's shuffled refits) is
k3_bkeys.py. Keys built from the sealed answer live only in a temp dir, are deleted, and never printed; only numbers
are written. Run from swarm/: python3 R2/HARNESS-2/selftest2.py [--only K1,K2] [--refits 50] > R2/HARNESS-2/selftest2.json"""
import argparse, collections, json, os, random, subprocess, sys, tempfile, pathlib
HERE = pathlib.Path(__file__).resolve().parent
SW = HERE.parents[1]
sys.path.insert(0, str(SW)); os.chdir(SW)
sys.path.insert(0, str(HERE))
import score_v21 as score
CMD = 'python3 R2/HARNESS-2/climb_fast.py {fit} {out} --seed {seed}'


def summarise(r):
    out = {'pair': r['pair'], 'on': r['on'], 'passes_bar_v2': r['passes_bar_v2'], 'rows': {}}
    for st in ('fr_quad', 'fr_dict', 'en_quad', 'pt_quad', 'vocab'):
        row = []
        for d in r['directions']:
            if d.get('missing_key'):
                row.append('missing'); continue
            s, f = d['stats'][st], d['refit']['stats'][st]
            row.append({'dir': f"{d['fit']}>{d['test']}", 'pct': s['pct'], 'pct_strat': s['pct_strat'],
                        'cov': d['coverage_test'], 'letters': d['read_letters'], 'rec': d.get('recovery_pct_test'),
                        'refit_below': f"{f['refits_below']}/{d['refit']['refits']}", 'above_p99': f['above_p99'],
                        'z': f['z'], 'xlang_D': f.get('xlang_D'), 'xlang_D_p99': f.get('xlang_D_p99'), 'xlang': f.get('xlang')})
        out['rows'][st] = {'directions': row, 'conds': r['verdict'][st]['directions'], 'passes': r['verdict'][st]['passes']}
    return out


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--only', default='K1,K2,K4,K5'); ap.add_argument('--refits', type=int, default=50)
    ap.add_argument('--shuffles', type=int, default=1000)
    a = ap.parse_args(); only = a.only.split(',')
    tmp = tempfile.mkdtemp(prefix='st2_')
    sealed = {}
    for part in ('c1', 'c2'):
        for s, v in zip(score.flat(score.load_control(f'FR-HOMO.{part}')), score.load_sealed(f'FR-HOMO.{part}')):
            sealed.setdefault(s, collections.Counter())[v] += 1
    true_key = {s: c.most_common(1)[0][0] for s, c in sealed.items()}
    vals = list(true_key.values()); random.Random(7).shuffle(vals)
    rand_key = dict(zip(true_key, vals))
    def wkey(k, name):
        p = os.path.join(tmp, name)
        open(p, 'w').write(''.join(f'{s}\t{v}\n' for s, v in k.items())); return p
    res = {}
    try:
        jobs = []
        if 'K1' in only:
            p = wkey(true_key, 'planted.tsv'); jobs += [('K1_planted', p, p, pair, 'FR-HOMO') for pair in ('c1c2', 'fold')]
        if 'K2' in only:
            p = wkey(rand_key, 'random.tsv'); jobs += [('K2_random', p, p, pair, 'FR-HOMO') for pair in ('c1c2', 'fold')]
        for tag, cid in (('K4_climber_NULL', 'NULL'), ('K5_climber_FR-HOMO', 'FR-HOMO'), ('K5_climber_FR-HOMO-N15', 'FR-HOMO-N15')):
            if tag.split('_')[0] not in only:
                continue
            for pair in ('c1c2', 'fold'):
                ks = []
                for f, _ in score.PAIRS[pair]:
                    fid = score.on_control(f, cid); out = os.path.join(tmp, f'{tag}_{fid}.tsv')
                    subprocess.run(['python3', 'R2/HARNESS-2/climb_fast.py', fid, out, '--seed', '3'], check=True, capture_output=True)
                    ks.append(out)
                jobs.append((tag, ks[0], ks[1], pair, cid))
        for tag, ka, kb, pair, cid in jobs:
            r = score.run_claim(ka, kb, pair, cid, a.refits, CMD, 4, a.shuffles)
            res[f'{tag}|{pair}'] = summarise(r)
            print(f'{tag} {pair}: passes {r["passes_bar_v2"]}', file=sys.stderr, flush=True)
    finally:
        for f in pathlib.Path(tmp).glob('*'):
            os.unlink(f)
        os.rmdir(tmp)
    print(json.dumps(res, indent=1))


if __name__ == '__main__':
    main()
