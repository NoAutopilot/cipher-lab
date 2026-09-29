#!/usr/bin/env python3
"""HARNESS-2 K3 (29 Sept 2026): group B's two order-shuffled refits that cleared beats_all under both frozen nulls on
the fold (G-B/refit/refit_c1+c2a_15.tsv: en_quad, es_dict; _34: fr_dict), scored in their fitted direction
c1+c2a -> c2b under bar v2's refit and cross-language conditions. Null: B's own fitter (G-B/fit_key.py, unchanged,
its own --shuffle-seed shuffle) on c1+c2a -- B's 40 refits minus the key under test, plus refits 41-51 made by the
harness with B's unchanged method (k3_refits/; model rebuilt from B's manifest, sizes matched) = 50.
Run from swarm/: python3 R2/HARNESS-2/k3_bkeys.py > R2/HARNESS-2/k3.json"""
import glob, json, os, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
SW = HERE.parents[1]; sys.path.insert(0, str(SW)); os.chdir(SW)
sys.path.insert(0, str(HERE))
import score_v21 as score
FIT, TEST = 'c1+c2a', 'c2b'
res = {}
new = sorted(glob.glob(str(HERE / 'k3_refits' / 'refit_c1+c2a_4[1-9].tsv')) + glob.glob(str(HERE / 'k3_refits' / 'refit_c1+c2a_5[01].tsv')))
for n, claimed in ((15, ('en_quad', 'es_dict')), (34, ('fr_dict',))):
    kf = f'G-B/refit/refit_c1+c2a_{n}.tsv'
    sib = [f for f in glob.glob('G-B/refit/refit_c1+c2a_*.tsv') if not f.endswith(f'_{n}.tsv')]
    keys = sorted(sib) + new
    fro = score.run_heldout(kf, FIT, TEST, 1000)
    rr = score.refit_report(kf, FIT, TEST, keys, 'precomputed (B fitter, B shuffle)')
    row = {'key': kf, 'refits': rr['refits'], 'coverage_test': fro['coverage_test'], 'read_letters': fro['read_letters']}
    for st in claimed + ('en_quad', 'fr_quad', 'es_quad', 'pt_quad', 'la_quad'):
        s, f = fro['stats'][st], rr['stats'][st]
        fz = s['beats_all'] and s['beats_all_strat'] and fro['coverage_test'] >= 0.5 and fro['read_letters'] >= 60
        rf = rr['refits'] >= score.MIN_REFITS and f['above_p99']
        row[st] = {'pct': s['pct'], 'pct_strat': s['pct_strat'], 'frozen': fz, 'refits_below': f['refits_below'],
                   'refit_p99': f['refit_p99'], 'real': f['real'], 'above_p99': f['above_p99'], 'z': f['z'],
                   'xlang_D': f.get('xlang_D'), 'xlang_D_p99': f.get('xlang_D_p99'), 'xlang': f.get('xlang'),
                   'passes_fitted_direction': bool(fz and rf and f.get('xlang'))}
    res[f'B_refit_{n}'] = row
print(json.dumps(res, indent=1))
