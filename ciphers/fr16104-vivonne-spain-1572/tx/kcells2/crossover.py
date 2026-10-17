#!/usr/bin/env python3
"""VIV-KCELLS2 step 4 (PREREG-VIV-KCELLS2.md): ERR-SIM sweep with key.tsv + trial cells c->p, 2->m (grade C).

    python3 tx/kcells2/crossover.py [--out tx/kcells2/crossover.json]

tx/err_sim/err_sim.py run() unchanged; confusion_AB.tsv has no row for c or 2, so (declared) each pass gives them its own mean
keyed-sign error rate and draws the wrong label from its pooled off-diagonal distribution.
"""
import json, os, sys
from collections import defaultdict
H = os.path.dirname(os.path.abspath(__file__)); TX = os.path.dirname(H)
sys.path.insert(0, os.path.join(TX, 'err_sim'))
import err_sim as es  # noqa: E402
TRIAL = {'c': ('p', 'C'), '2': ('m', 'C')}


def main():
    out = sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv else os.path.join(H, 'crossover.json')
    shape, freq, rows = es.target_shape(); key = {**es.load_key(), **TRIAL}; M = es.load_conf()
    base = es.load_key()
    for p in 'AB':
        pooled = defaultdict(float); ers = []
        for t in base:
            row = M[p].get(t, {})
            for r, q in row.items():
                if r != t:
                    pooled[r] += q
        have = [t for t in base if M[p].get(t, {}).get(t) is not None]
        mean_err = sum(1 - M[p][t][t] for t in have) / len(have); tot = sum(pooled.values())
        # post-registration fix (NOTES): keyed signs with no confusion row get the same fill as c and 2 (the sweep crashed on them)
        for c in list(TRIAL) + [t for t in base if t not in have]:   # diagonal 1 - mean_err; off-diagonal mass spread as the pooled distribution
            M[p][c] = {c: 1 - mean_err, **{r: mean_err * q / tot for r, q in pooled.items()}}
    pt, src = es.plaintext(sum(n for _, n in shape))
    sv = sys.argv; sys.argv = [sv[0], '--strict']; V = es.vs.vocab(); sys.argv = sv
    res = {'AD': es.AD, 'runs': []}
    for e in (0.0, 0.05, 0.10, 0.14, 0.19, 0.23):
        for s in range(1, 6):
            r = es.run(e, s, key, freq, shape, M, pt, V); res['runs'].append(r); print(json.dumps(r), flush=True)
    cross = {}
    for stat in ('hrun', 'hrun_correct'):
        ok = [e for e in (0.0, 0.05, 0.10, 0.14, 0.19, 0.23) if sum(r[stat] >= es.AD for r in res['runs'] if r['e'] == e) >= 3]
        cross[stat] = max(ok) if ok else None
    res['crossover'] = cross; print('crossover', cross)
    json.dump(res, open(out, 'w'), indent=1)


if __name__ == '__main__':
    main()
