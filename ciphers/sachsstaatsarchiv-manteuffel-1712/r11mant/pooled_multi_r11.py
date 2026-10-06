#!/usr/bin/env python3
"""R11-MANTPOOL2 (6 Oct 2026): R9-MANTPOOL's pooled multi-code-run aligner re-run with frames 0526, 0521, 0518 added,
per PREREG-R11-MANTPOOL2.md. Reuses r9mant/pooled_multi.py unchanged (load/align/score/shuffle_glosses, bins, seeds 9501+d,
MANT5 normalisation); only LEAVES grows to 10 and the fixed key is ../key.tsv minus the rows whose source names R9-MANTPOOL
(the 10 R9 codes compete again as free codes). Then R9-MANTPC's per-code test (r9mant/per_code.py functions) on every agreeing code.
Usage: pooled_multi_r11.py [--draws N] [--time-one]   (writes runs_r11.tsv, codes_r11.tsv, shuffle_r11.tsv, known_answer_r11.tsv,
per_code_r11.tsv, per_code_ka_r11.tsv here)"""
import csv, os, sys, random, time
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, '..', 'r9mant'))
import pooled_multi as pm
import per_code as pc
pm.LEAVES = pm.LEAVES + [('0526', 'f422_0526/pairs.tsv'), ('0521', 'f0521/pairs.tsv'), ('0518', 'f0518/pairs.tsv')]
R9 = {r['code'] for r in pm.rd('key.tsv') if 'R9-MANTPOOL' in r['source']}
FIX = {k: v for k, v in pm.ALLFIX.items() if str(k) not in R9}
pc.FIX0 = FIX

def one_draw(d):
    runs = pm.load(); rng = random.Random(pm.SEED + d)
    per = pm.align(runs, pm.shuffle_glosses(runs, rng), FIX)
    return len(pm.score(per, pm.free_of(per, FIX))[1])

def main():
    a = sys.argv[1:]; draws = int(a[a.index('--draws') + 1]) if '--draws' in a else pm.DRAWS
    runs = pm.load()
    if '--time-one' in a:
        t = time.time(); print('runs', len(runs), 'one shuffled draw S =', one_draw(0), 'in %.1f s' % (time.time() - t)); return
    print('runs', len(runs), 'by leaf', {l: sum(r['leaf'] == l for r in runs) for l, _ in pm.LEAVES},
          'bins', [sum(lo <= len(r['codes'].split()) <= hi for r in runs) for lo, hi in pm.BINS])
    per = pm.align(runs, [r['gloss'] for r in runs], FIX)
    free = pm.free_of(per, FIX); rec, agree = pm.score(per, free)
    with Pool(4) as pool:
        sh = sorted(pool.map(one_draw, range(draws)))
    p95 = sh[int(0.95 * draws) - 1]; mean = sum(sh) / draws
    cand = []
    for v, d in per.items():
        k = pm.KEY.get(str(v))
        if not k or k['grade'] != 'C' or not k['value'].strip(): continue
        cand.append((-len(set().union(*d.values())), v))
    hide = [v for _, v in sorted(cand)[:pm.NHIDE]]
    fx = {k: c for k, c in FIX.items() if k not in hide}
    perk = pm.align(runs, [r['gloss'] for r in runs], fx); _, agk = pm.score(perk, set(hide))
    ka = []
    for v in hide:
        d = perk[v]; best = max(((len(s), ch) for ch, s in d.items() if ch), default=(0, ''))
        ok = v in agk and agk[v] in pm.alts(str(v))
        ka.append([v, pm.KEY[str(v)]['value'], len(set().union(*d.values())), best[1], best[0], 'yes' if ok else 'no'])
    nka = sum(r[-1] == 'yes' for r in ka); S = len(agree); passed = S > p95 and nka >= 3
    print(f'REAL: free codes recurring in >=2 runs {len(rec)}, agreeing S = {S}')
    print(f'SHUFFLE ({draws} draws, bins): mean {mean:.2f}, p95 {p95}, max {sh[-1]}')
    print(f'KNOWN-ANSWER: {nka}/{pm.NHIDE}: ' + '; '.join(f'{r[0]}={r[1]!r} -> {r[3]!r} x{r[4]} ({r[5]})' for r in ka))
    print('GATE (S > p95 AND known-answer >= 3/5):', 'PASS' if passed else 'FAIL')
    w0 = lambda n: open(os.path.join(HERE, n), 'w')
    with w0('runs_r11.tsv') as f:
        w = csv.DictWriter(f, ['leaf', 'line', 'codes', 'gloss'], delimiter='\t', lineterminator='\n'); w.writeheader(); w.writerows(runs)
    with w0('codes_r11.tsv') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n'); w.writerow(['code', 'n_runs', 'leaves', 'chunks(runs)', 'agree_chunk', 'licence'])
        for v in sorted(rec):
            d = per[v]; ids = set().union(*d.values()); ch = ' | '.join(f'{c or "-"}({len(s)})' for c, s in sorted(d.items(), key=lambda kv: -len(kv[1])))
            w.writerow([v, len(ids), ','.join(sorted({runs[i]['leaf'] for i in ids})), ch, agree.get(v, ''),
                        ('pooled-PASS' if passed else 'gate-failed') if v in agree else 'disagree'])
    with w0('shuffle_r11.tsv') as f:
        f.write('draw_sorted\tS\n' + ''.join(f'{i}\t{x}\n' for i, x in enumerate(sh)))
    with w0('known_answer_r11.tsv') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n'); w.writerow(['code', 'key_value', 'n_runs', 'top_chunk', 'top_runs', 'recovered']); w.writerows(ka)
    if not passed or '--no-per-code' in a:
        return
    # per-code test (R9-MANTPC design) on every agreeing code; positive control = R9-MANTPC's 5 known-answer codes
    target = sorted(agree)
    pc.TARGET = target; pc.FIXKA = {k: c for k, c in FIX.items() if k not in pc.KA}   # set before the fork
    with Pool(4) as pool:
        t = pc.test('t', target, FIX, draws, pool)
        k = pc.test('k', pc.KA, pc.FIXKA, draws, pool)
    for name, rows in (('per_code_r11.tsv', t), ('per_code_ka_r11.tsv', k)):
        with w0(name) as f:
            w = csv.DictWriter(f, list(rows[0]), delimiter='\t', lineterminator='\n'); w.writeheader(); w.writerows(rows)
    print('per-code target pass', sum(r['BH_q010'] == 'PASS' for r in t), '/', len(t), '; known-answer pass', sum(r['BH_q010'] == 'PASS' for r in k), '/ 5')

if __name__ == '__main__':
    main()
