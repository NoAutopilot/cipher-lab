#!/usr/bin/env python3
"""TXE4-10 RECOG-CUT unit 4 (PREREG-txeng4-10.md 'Endpoint'): score every arm once with tx_bench.py (the patched copy named by
$TXE4_10_TOOLS carries --perm-null and --seg-boxes; benchmark-tx/txeng4/10/tx_bench.patch). Per arm: both masks, --strict, --ci,
the 200-permutation label null (seed 1), --seg-boxes with the arm's own boxes and its frozen-kNN top-3; then --paired rec vs pen
and rec vs each rec_perm seed. Writes scores/<arm>.txt, scores/<arm>.json, scores/paired_*.txt and scores/summary.tsv.
The truth is opened only by tx_bench.py. Run once; the outputs' sha256 are in SHA256SUMS.prescore (checked first)."""
import csv, hashlib, json, os, subprocess, sys
ROOT = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(ROOT, '..', '..', '..'))
TOOLS = os.environ.get('TXE4_10_TOOLS', os.path.join(REPO, 'tools'))
TXB = os.path.join(TOOLS, 'tx_bench.py')
BENCH = os.path.join(REPO, 'benchmark-tx/txeng3/6/bench_test.tsv')
T36 = os.path.join(REPO, 'benchmark-tx/txeng3/6/seg')
ARMS = ['pen', 'sign', 'rand1', 'rand2', 'rand3', 'rec', 'rec_perm1', 'rec_perm2', 'rec_perm3']


def boxes_of(arm):
    return os.path.join(T36 if arm in ARMS[:5] else os.path.join(ROOT, 'seg'), arm, 'boxes.tsv')


def check_prescore():
    bad = []
    for l in open(os.path.join(ROOT, 'SHA256SUMS.prescore')):
        h, p = l.split()
        if hashlib.sha256(open(os.path.join(ROOT, p), 'rb').read()).hexdigest() != h:
            bad.append(p)
    if bad:
        sys.exit('prescore hash mismatch: ' + ', '.join(bad))


def run(args):
    r = subprocess.run([sys.executable, TXB, *args], cwd=REPO, capture_output=True, text=True)
    if r.returncode:
        sys.exit(' '.join(args) + '\n' + r.stdout + r.stderr)
    return r.stdout


def main():
    check_prescore()
    sd = os.path.join(ROOT, 'scores')
    os.makedirs(sd, exist_ok=True)
    summ = []
    for arm in ARMS:
        out = os.path.join(ROOT, 'outputs', f'{arm}.top1.tsv')
        common = [out, '--bench', BENCH, '--exclude-flagged', '--strict', '--ci', '--perm-null', '200', '--perm-seed', '1',
                  '--seg-boxes', boxes_of(arm), '--seg-topk', os.path.join(ROOT, 'outputs', f'{arm}.topk.tsv')]
        txt = run(common)
        open(os.path.join(sd, f'{arm}.txt'), 'w').write(' '.join(os.path.relpath(x, REPO) if os.path.isabs(x) else x for x in common) + '\n' + txt)
        js = json.loads(run(common + ['--json']))['items'][0]
        json.dump(js, open(os.path.join(sd, f'{arm}.json'), 'w'), indent=1)
        fe = js['flagged_excluded']
        summ.append(dict(arm=arm, boxes=js['read'], err_true=js['err_true'], errors=js['errors'], scored=js['scored'],
                         ser=js['ser'], S=js['ser_S'], D=js['ser_D'], I=js['ser_I'],
                         strict_err=js['strict']['err_true'], null_mean=js['perm_null']['as_measured']['mean'],
                         null_lo=js['perm_null']['as_measured']['p2_5'], null_hi=js['perm_null']['as_measured']['p97_5'],
                         gain=js['perm_null']['as_measured']['gain_over_chance'],
                         fe_err_true=fe['err_true'], fe_errors=fe['errors'], fe_scored=fe['scored'], fe_ser=fe['ser'],
                         fe_null_mean=js['perm_null']['flagged_excluded']['mean'], fe_gain=js['perm_null']['flagged_excluded']['gain_over_chance'],
                         share_1to1=js['seg_boxes']['share_1to1'], abs_diff=js['seg_boxes']['abs_diff'],
                         boxes_2to1=js['seg_boxes']['boxes_2to1'], tokens_1to2=js['seg_boxes']['tokens_1to2'],
                         shift=js['seg_boxes'].get('shift_check_loo', {}).get('verdict', '')))
        print(f"{arm}: err_true {js['err_true']:.3f} ({js['errors']}/{js['scored']}) | null {summ[-1]['null_mean']:.3f} gain {summ[-1]['gain']:.3f} "
              f"| 1:1 {summ[-1]['share_1to1']:.3f} | fe {fe['err_true']:.3f}")
    with open(os.path.join(sd, 'summary.tsv'), 'w') as f:
        cols = list(summ[0])
        f.write('\t'.join(cols) + '\n')
        for r in summ:
            f.write('\t'.join(str(r[c]) for c in cols) + '\n')
    for base in ['pen', 'rec_perm1', 'rec_perm2', 'rec_perm3', 'sign']:
        args = [os.path.join(ROOT, 'outputs', 'rec.top1.tsv'), '--bench', BENCH, '--exclude-flagged', '--ci',
                '--paired', os.path.join(ROOT, 'outputs', f'{base}.top1.tsv')]
        txt = run(args)
        open(os.path.join(sd, f'paired_rec_vs_{base}.txt'), 'w').write(' '.join(os.path.relpath(x, REPO) if os.path.isabs(x) else x for x in args) + '\n' + txt)
        for l in txt.splitlines():
            if l.startswith('paired') and 'as measured' in l:
                print(l[:230])


if __name__ == '__main__':
    main()
