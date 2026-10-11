#!/usr/bin/env python3
"""TXE3-5: score every Birago arm with tx_bench (as measured + flagged-excluded, paired against machine), write scores.tsv and a summary.
Wilson 95% computed here (tx_bench's --coverage-diagnostic line omits it)."""
import subprocess, sys, re, math, glob, os, statistics
R = 'benchmark-tx/txeng3/5'
def wilson(k, n, z=1.96):
    p = k / n; d = 1 + z * z / n; c = p + z * z / (2 * n); h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (c - h) / d, (c + h) / d
def score(path):
    o = subprocess.run([sys.executable, 'tools/tx_bench.py', path, '--item', 'birago1572-no87', '--coverage-diagnostic', '--exclude-flagged',
                        '--paired', f'{R}/outputs/machine.signs.tsv'], capture_output=True, text=True).stdout
    m = re.search(r'as measured: err_true\(0.75-indel align\) ([\d.]+) \((\d+)/(\d+)\).*?: S (\d+) D (\d+) I (\d+)', o)
    f = re.search(r'flagged excluded.*?err_true\(0.75-indel align\) ([\d.]+) \((\d+)/(\d+)\)', o)
    p = re.search(r'lines improved (\d+), worsened (\d+), tied (\d+); line sign test p = ([\d.]+); unit-cost edits base (\d+) -> output (\d+)', o)
    return dict(err=float(m.group(1)), k=int(m.group(2)), n=int(m.group(3)), S=int(m.group(4)), D=int(m.group(5)), I=int(m.group(6)),
                err_f=float(f.group(1)), k_f=int(f.group(2)), n_f=int(f.group(3)),
                imp=int(p.group(1)), wors=int(p.group(2)), tied=int(p.group(3)), p=float(p.group(4)), base=int(p.group(5)), out=int(p.group(6)))
rows = {}
for path in sorted(glob.glob(f'{R}/outputs/*.signs.tsv')):
    rows[os.path.basename(path)[:-10]] = score(path)
with open(f'{R}/scores.tsv', 'w') as f:
    f.write('arm\terr_true\tk\tn\twilson95\terr_true_flagged_excl\tk_f\tn_f\twilson95_f\tS\tD\tI\tlines_improved\tlines_worsened\ttied\tsign_p\tedits_vs_machine\n')
    for a, r in rows.items():
        lo, hi = wilson(r['k'], r['n']); lf, hf = wilson(r['k_f'], r['n_f'])
        f.write(f"{a}\t{r['err']:.3f}\t{r['k']}\t{r['n']}\t{lo:.3f}-{hi:.3f}\t{r['err_f']:.3f}\t{r['k_f']}\t{r['n_f']}\t{lf:.3f}-{hf:.3f}\t{r['S']}\t{r['D']}\t{r['I']}\t{r['imp']}\t{r['wors']}\t{r['tied']}\t{r['p']}\t{r['out'] - r['base']}\n")
print(open(f'{R}/scores.tsv').read())
ctl = [r for a, r in rows.items() if a.startswith('control_')]
own = rows['owner']; mac = rows['machine']
d_own = own['k'] - mac['k']; d_ctl = [r['k'] - mac['k'] for r in ctl]
print(f"owner edits delta vs machine: {d_own} (as measured), {own['k_f'] - mac['k_f']} (flagged excl)")
print(f"control deltas ({len(ctl)} seeds): mean {statistics.mean(d_ctl):+.2f} sd {statistics.pstdev(d_ctl):.2f} min {min(d_ctl):+d} max {max(d_ctl):+d}; "
      f"seeds with delta <= owner's: {sum(d <= d_own for d in d_ctl)}/{len(ctl)}; seeds better than machine (delta<0): {sum(d < 0 for d in d_ctl)}")
print(f"control err_true mean {statistics.mean(r['err'] for r in ctl):.3f} (min {min(r['err'] for r in ctl):.3f} max {max(r['err'] for r in ctl):.3f}); "
      f"flagged-excl mean {statistics.mean(r['err_f'] for r in ctl):.3f}")
