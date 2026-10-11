#!/usr/bin/env python3
"""TXE3-1: score the eval k-dumps of tools/tx_sorter_curve.py with tools/tx_bench.py (the brief's figure, Wilson 95%).
Unit = eval_heldout lines only, so --coverage-diagnostic (other truth lines listed, not charged). The x-run dumps report
the flagged-excluded line, the m-run dumps the as-measured line. Run from the repo root; writes eval/tx_bench_dumps.tsv."""
import os, re, subprocess, sys, time
sys.path.insert(0, 'tools'); import tx_bench  # noqa: E402
O = 'benchmark-tx/txeng3/1/eval'
pat = re.compile(r'err_true\(0.75-indel align\) ([0-9.]+) \((\d+)/(\d+)\)')
rows = ['# tools/tx_bench.py on the eval k-dumps (eval_heldout lines, --coverage-diagnostic); x = flagged excluded, m = as measured; '
        'Wilson 95%%; %s\nmode\tordering\tk\tconv\terr_true\twrong\tscored\twilson_lo\twilson_hi' % time.strftime('%d %b %Y %H:%M UTC', time.gmtime())]
for mode in ('pile',):
    for conv in ('x', 'm'):
        d = '%s/dump_%s_%s_lam1' % (O, mode, conv)
        for ord_ in ('disagree', 'lattice', 'margin', 'a_doubt', 'disagree_margin', 'b_size', 'd_oracle'):
            for k in (10, 20, 50, 100):
                f = '%s/%s_k%d.tsv' % (d, ord_, k)
                if not os.path.exists(f):
                    continue
                cmd = [sys.executable, 'tools/tx_bench.py', f, '--item', 'birago1572-no87', '--coverage-diagnostic']
                if conv == 'x':
                    cmd.append('--exclude-flagged')
                out = subprocess.run(cmd, capture_output=True, text=True).stdout
                line = [l for l in out.split('\n') if ('flagged excluded' if conv == 'x' else 'as measured') in l][0]
                m = pat.search(line); w, n = int(m.group(2)), int(m.group(3))
                lo, hi = tx_bench.wilson(w, n)
                rows.append('%s\t%s\t%d\t%s\t%s\t%d\t%d\t%.3f\t%.3f' % (mode, ord_, k, conv, m.group(1), w, n, lo, hi))
open(O + '/tx_bench_dumps.tsv', 'w').write('\n'.join(rows) + '\n')
print('\n'.join(rows))
