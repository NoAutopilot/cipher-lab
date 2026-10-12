#!/usr/bin/env python3
"""Offline test of tools/tx_bench.py --perm-null and --seg-boxes (TXE4-10 RECOG-CUT, 12 Oct 2026). A 3-line synthetic
truth (6 positions a line, two excluded) and a bench row pointing at it. Must-catch: --perm-null on a perfect output
reports a null mean err_true above the real 0.0 and a positive gain; --seg-boxes on boxes that match the truth
positions 1:1 reports a 1:1 share of 1.0 and |boxes - positions| 0, and with two boxes merged into one wide box reports
a 2:1 step and share < 1. Must-not-block: the ordinary scores are unchanged by either option. No truth file of the
repository is read; everything is written to a temp dir."""
import json, os, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(HERE, '..', 'tx_bench.py')
SIGNS = ['a', 'b', 'c', 'd', 'e', 'f']


def main():
    d = tempfile.mkdtemp()
    truth = os.path.join(d, 'truth.tsv')
    with open(truth, 'w') as f:
        f.write('line\tpos\tref_sign\ttruth\tplain\tstatus\tflag\n')
        for li in (1, 2, 3):
            for p, s in enumerate(SIGNS, 1):
                st = 'excluded:x' if p == 6 else 'scored'
                f.write(f'p_L{li:02d}\t{p}\t{s}\t{s}\t{s}\t{st}\t\n')
    bench = os.path.join(d, 'bench.tsv')
    with open(bench, 'w') as f:
        f.write('item\tfolder\tleaf\tlines\tcrops\ttruth\ttruth_source\ttruth_grade\tkey_family\thand\tsplit\tn_positions\tn_scored\tn_excluded\toutputs\tnotes\n')
        f.write('syn\t.\tleaf\tp_L01-L03\t\ttruth.tsv\tsyn\tC\tsyn\tsyn\tdev\t18\t15\t3\t\t\n')
    out = os.path.join(d, 'out.tsv')
    with open(out, 'w') as f:
        f.write('line\tpos\tsign\n')
        for li in (1, 2, 3):
            for p, s in enumerate(SIGNS, 1):
                f.write(f'p_L{li:02d}\t{p}\t{s}\n')
    boxes = os.path.join(d, 'boxes.tsv')
    with open(boxes, 'w') as f:
        f.write('line\tpos\tsid\tx_line\tw\n')
        for li in (1, 2, 3):
            for p in range(1, 7):
                f.write(f'p_L{li:02d}\t{p}\tb{li}_{p}\t{100 * p}\t60\n')
    merged = os.path.join(d, 'merged.tsv')
    with open(merged, 'w') as f:
        f.write('line\tpos\tsid\tx_line\tw\n')
        for li in (1, 2, 3):
            f.write(f'p_L{li:02d}\t1\tm{li}_1\t100\t160\n')     # boxes 1+2 as one wide box
            for p in range(3, 7):
                f.write(f'p_L{li:02d}\t{p - 1}\tm{li}_{p}\t{100 * p}\t60\n')
    topk = os.path.join(d, 'topk.tsv')
    with open(topk, 'w') as f:
        f.write('box\tk1\tk2\tk3\n')
        for li in (1, 2, 3):
            for p, s in enumerate(SIGNS, 1):
                f.write(f'b{li}_{p}\t{s}\t_\t_\n')

    def run(*extra):
        r = subprocess.run([sys.executable, TOOL, out, '--bench', bench, '--json', *extra], capture_output=True, text=True)
        assert r.returncode == 0, r.stdout + r.stderr
        return json.loads(r.stdout)['items'][0]
    base = run()
    assert base['err_true'] == 0.0, base
    pn = run('--perm-null', '30', '--perm-seed', '3')
    assert pn['err_true'] == 0.0
    n = pn['perm_null']['as_measured']
    assert n['n'] == 30 and n['mean'] > 0.5 and n['gain_over_chance'] == n['mean'], n
    sb = run('--seg-boxes', boxes, '--seg-topk', topk)['seg_boxes']
    assert sb['boxes'] == 18 and sb['truth_positions'] == 18 and sb['abs_diff'] == 0, sb
    assert sb['share_1to1'] == 1.0 and sb['boxes_2to1'] == 0, sb
    assert sb['shift_check_loo']['verdict'] in ('PASS', 'UNCHECKABLE'), sb['shift_check_loo']
    sm = run('--seg-boxes', merged)['seg_boxes']
    assert sm['boxes'] == 15 and sm['abs_diff'] == 3 and sm['tokens_1to2'] >= 3 and sm['share_1to1'] < 1.0, sm
    assert 'shift_check_loo' not in sm
    print('ok')


if __name__ == '__main__':
    main()
