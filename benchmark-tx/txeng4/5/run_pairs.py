#!/usr/bin/env python3
"""TXE4-5 PAIR-BANK units 3-4 (12 Oct 2026, account 3; PREREG benchmark-tx/PREREG-txeng4-5.md). Run arguments on record (rule 7).

  python3 benchmark-tx/txeng4/5/run_pairs.py gates      # G1 (LOGO vs 20 shuffled) and the G2 dev outputs for the ten pairs
  python3 benchmark-tx/txeng4/5/run_pairs.py score-dev  # tx_bench on the committed G2 outputs -> gates/summary.tsv, passing.txt
  python3 benchmark-tx/txeng4/5/run_pairs.py eval       # passing pairs applied to the four bases + controls (no score)
  python3 benchmark-tx/txeng4/5/run_pairs.py score      # tx_bench on the committed eval outputs -> eval/scores.tsv

Pools (machine labels only): agree/sib_pool_agree.tsv : maps/sib_pool_map.tsv (sibling leaves, join_check PASS) and
agree/no87_agree.tsv : maps/no87_passA.tsv (no.87's own A/B agreement; --exclude-own-line keeps the applied line out).
Maps for application: maps/no87_passA.tsv, no87_labels.tsv, f152r_passA.tsv, f152r_passZ.tsv (each with its PASS sidecar).
No truth file is opened here; tx_bench is the only reader of truth (R3)."""
import csv, os, re, subprocess, sys, itertools
from math import comb

O = 'benchmark-tx/txeng4/5'; U = 'benchmark-tx/txeng/units'; OUT = 'benchmark-tx/outputs'
AT = 'ciphers/nevers-birago-fr3251-1572/atlas'
PAIRS = [('T18', 'T98'), ('T90', 'T53'), ('T76', 'T86'), ('T76', 'T45'), ('T76', 'T66'), ('T50', 'T92'), ('T24', 'T29'),
         ('T60', 'T86'), ('T95', 'T51'), ('T64', 'T38')]
LOOKED = {('T18', 'T98'), ('T90', 'T53')}   # TXE3-10 looked at these on no.87 eval: reported, excluded from the gate there
POOLS = ['--pool-agreed', f'{O}/agree/sib_pool_agree.tsv:{O}/maps/sib_pool_map.tsv',
         '--pool-agreed', f'{O}/agree/no87_agree.tsv:{O}/maps/no87_passA.tsv']
BASES = {  # name: (unit file, map, item, own-line exclusion)
    'no87_passA': (f'{U}/passA_eval_heldout.tsv', f'{O}/maps/no87_passA.tsv', 'birago1572-no87', True),
    'no87_L': (f'{U}/labels_eval_heldout.tsv', f'{O}/maps/no87_labels.tsv', 'birago1572-no87', True),
    'f152r_passA': (f'{OUT}/birago1572-f152r/passA.tsv', f'{O}/maps/f152r_passA.tsv', 'birago1572-f152r', False),
    'f152r_Z': (f'{OUT}/birago1572-f152r/passZ_pipeline.tsv', f'{O}/maps/f152r_passZ.tsv', 'birago1572-f152r', False),
}


def sh(cmd, log=None):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if log:
        with open(log, 'a') as f:
            f.write('$ ' + ' '.join(cmd) + '\n' + r.stdout + r.stderr + '\n')
    if r.returncode != 0:
        sys.stderr.write(r.stdout[-2000:] + r.stderr[-2000:])
    return r


def classify(args, log):
    return sh([sys.executable, f'{O}/scratch/tools/glyph_atlas.py', 'classify', '--out', AT, '--feature-bank'] + POOLS + args, log)


def rd(p):
    return list(csv.DictReader(open(p), delimiter='\t'))


def gates():
    os.makedirs(f'{O}/gates', exist_ok=True); log = f'{O}/gates/commands.log'; open(log, 'w').close()
    for A, B in PAIRS:
        r = classify(['--pair', A, B, '--map', f'{O}/maps/no87_labels.tsv', '--apply-unit', f'{U}/labels_dev_tune.tsv',
                      '--exclude-own-line', '--shuffle-lolo', '20', '--tsv', f'{O}/gates/dev_{A}_{B}.tsv',
                      '--report', f'{O}/gates/report_{A}_{B}.tsv', '--touched', f'{O}/gates/touched_dev_{A}_{B}.tsv'], log)
        print(f'{A}/{B}: rc {r.returncode}; ' + (r.stdout.strip().split('\n')[-1] if r.stdout.strip() else ''))


def g1_verdict(A, B):
    rep = rd(f'{O}/gates/report_{A}_{B}.tsv')
    f1 = [r for r in rep if r['fold'] == '1'][0]
    sh_ = [float(x) for x in f1['shuffled'].split()] if f1['shuffled'] else []
    acc = float(f1['lolo_acc']) if f1['lolo_acc'] else None
    enabled = sum(int(r['enabled']) for r in rep)
    return dict(pool_a=f1['pool_a'], pool_b=f1['pool_b'], groups=f1['groups'], lolo=acc, shuf_max=max(sh_) if sh_ else None,
                chance=f1['chance'], enabled_folds=f'{enabled}/{len(rep)}', kept=f1['kept'],
                g1='PASS' if acc is not None and sh_ and acc > max(sh_) else 'FAIL')


def bench(out, base, item, extra=()):
    """fixed/broken/p on both masks + err lines, parsed from tx_bench."""
    cmd = [sys.executable, 'tools/tx_bench.py', '--item', item, '--exclude-flagged', '--strict', '--paired', base] + list(extra) + [out]
    r = sh(cmd)
    res = {}
    for m in re.finditer(r'\[(as measured|flagged excluded[^\]]*)\]:.*?fixed (\d+), broken (\d+); exact p = ([0-9.]+)', r.stdout):
        key = 'meas' if m.group(1).startswith('as') else 'flag'
        res[key] = (int(m.group(2)), int(m.group(3)), float(m.group(4)))
    errs = re.findall(r'err_true\(0\.75-indel align\) ([0-9.]+ \(\d+/\d+\))', r.stdout)
    res['err'] = errs[:2]
    res['raw'] = r.stdout
    return res


def score_dev():
    rows = []; passing = []
    for A, B in PAIRS:
        g = g1_verdict(A, B)
        b = bench(f'{O}/gates/dev_{A}_{B}.tsv', f'{U}/labels_dev_tune.tsv', 'birago1572-no87', ['--coverage-diagnostic'])
        fm, bm, pm = b.get('meas', (0, 0, 1.0)); ff, bf, pf = b.get('flag', (0, 0, 1.0))
        considered = len(rd(f'{O}/gates/touched_dev_{A}_{B}.tsv'))
        g2 = 'PASS' if bm == 0 else 'FAIL'
        both = g['g1'] == 'PASS' and g2 == 'PASS' and g['enabled_folds'].split('/')[0] != '0'
        rows.append(dict(pair=f'{A}/{B}', **g, considered=considered, fixed=fm, broken=bm, p=pm, fixed_fl=ff, broken_fl=bf,
                         g2=g2, both='PASS' if both else 'FAIL'))
        if both:
            passing.append((A, B))
    cols = list(rows[0].keys())
    with open(f'{O}/gates/summary.tsv', 'w') as f:
        f.write('\t'.join(cols) + '\n' + ''.join('\t'.join(str(r[c]) for c in cols) + '\n' for r in rows))
    with open(f'{O}/gates/passing.txt', 'w') as f:
        f.write(''.join(f'{A} {B}\n' for A, B in passing))
    for r in rows:
        print('\t'.join(str(r[c]) for c in cols))
    print('passing:', passing)


def evaluate():
    os.makedirs(f'{O}/eval', exist_ok=True); log = f'{O}/eval/commands.log'; open(log, 'w').close()
    pairs = [l.split() for l in open(f'{O}/gates/passing.txt') if l.strip()]
    if not pairs:
        print('no passing pair: nothing applied'); return
    for name, (unit, mp, item, own) in BASES.items():
        runs = [('real', [])]
        if name.endswith('passA'):
            runs += [(f'ctrl{s}f', ['--seed', str(s), '--force-t', '0']) for s in range(1, 6)] + [('rev', ['--reverse-labels'])]
        for tag, extra in runs:
            stem = f'{O}/eval/{name}_{tag}'
            r = classify(['--pairs', f'{O}/gates/passing.txt', '--map', mp, '--apply-unit', unit] + (['--exclude-own-line'] if own else [])
                         + ['--tsv', f'{stem}.tsv', '--report', f'{stem}_report.tsv', '--touched', f'{stem}_touched.tsv'] + extra, log)
            print(f'{name} {tag}: rc {r.returncode}; ' + (r.stdout.strip().split('\n')[-1] if r.stdout.strip() else ''))


def exact_p(f, b):
    n = f + b
    if n == 0:
        return 1.0
    k = min(f, b)
    return min(1.0, 2 * sum(comb(n, i) for i in range(k + 1)) / 2 ** n)


def score():
    pairs = [tuple(l.split()) for l in open(f'{O}/gates/passing.txt') if l.strip()]
    rows = []
    for name, (unit, mp, item, own) in BASES.items():
        tags = ['real'] + ([f'ctrl{s}f' for s in range(1, 6)] + ['rev'] if name.endswith('passA') else [])
        for tag in tags:
            stem = f'{O}/eval/{name}_{tag}'
            extra = ['--coverage-diagnostic'] if item == 'birago1572-no87' else []
            for A, B in pairs + [('ALL', 'ALL')]:
                out = f'{stem}.tsv' if A == 'ALL' else f'{stem}_{A}_{B}.tsv'
                if not os.path.exists(out):
                    continue
                b = bench(out, unit, item, extra)
                fm, bm, pm = b.get('meas', (0, 0, 1.0)); ff, bf, pf = b.get('flag', (0, 0, 1.0))
                tf = f'{stem}_{A}_{B}.touched' if A != 'ALL' else f'{stem}_touched.tsv'
                tf = tf if os.path.exists(tf) else (f'{stem}_{A}_{B}.tsv.touched' if os.path.exists(f'{stem}_{A}_{B}.tsv.touched') else None)
                considered = len(rd(tf)) if tf else ''
                in_gate = 'no' if (A == 'ALL' or (item == 'birago1572-no87' and (A, B) in LOOKED)) else 'yes'
                rows.append(dict(base=name, tag=tag, pair=f'{A}/{B}', considered=considered, fixed=fm, broken=bm, p=pm,
                                 fixed_fl=ff, broken_fl=bf, p_fl=pf, err=' | '.join(b['err']), in_gate=in_gate))
    cols = list(rows[0].keys()) if rows else []
    with open(f'{O}/eval/scores.tsv', 'w') as f:
        f.write('\t'.join(cols) + '\n' + ''.join('\t'.join(str(r[c]) for c in cols) + '\n' for r in rows))
    for r in rows:
        print('\t'.join(str(r[c]) for c in cols))
    # pooled gate
    for mask in ('', '_fl'):
        for base_kind in ('passA', 'L'):
            sel = [r for r in rows if r['tag'] == 'real' and r['in_gate'] == 'yes' and
                   ((r['base'] in ('no87_passA', 'f152r_passA')) if base_kind == 'passA' else (r['base'] in ('no87_L', 'f152r_Z')))]
            F = sum(r['fixed' + mask] for r in sel); Bk = sum(r['broken' + mask] for r in sel)
            print(f'POOLED {base_kind} [{"as measured" if not mask else "flagged excluded"}]: fixed {F} broken {Bk} net {F - Bk} exact p {exact_p(F, Bk):.4f}')
        for tag in [f'ctrl{s}f' for s in range(1, 6)] + ['rev']:
            sel = [r for r in rows if r['tag'] == tag and r['in_gate'] == 'yes']
            F = sum(r['fixed' + mask] for r in sel); Bk = sum(r['broken' + mask] for r in sel)
            print(f'CONTROL {tag} pooled [{"meas" if not mask else "flag"}]: fixed {F} broken {Bk} net {F - Bk}')


if __name__ == '__main__':
    {'gates': gates, 'score-dev': score_dev, 'eval': evaluate, 'score': score}[sys.argv[1]]()
