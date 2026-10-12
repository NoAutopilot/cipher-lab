#!/usr/bin/env python3
"""TXE4-1 scoring (PREREG-txeng4-1.md 'Endpoint'): ONE tx_bench call per pass (refuses to run twice: scores/<RUN>.txt must
not exist), plus the registered paired per-line calls of the same round (W against D as the base; H/Hx never ran).
  python3 benchmark-tx/txeng4/1/score.py single D1 W1 D2 W2     # scores/<RUN>.txt
  python3 benchmark-tx/txeng4/1/score.py paired 1 2             # scores/paired_W<r>_vs_D<r>.txt
Every call: --bench benchmark-tx/txeng3/6/bench_test.tsv --item vivonne1573-f102r-dev2 --exclude-flagged --strict
--coverage-diagnostic --ci (the outputs name only the 13 test lines; coverage 417/417 is confirmed in each file)."""
import os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
ARGS = ['--bench', os.path.join(REPO, 'benchmark-tx/txeng3/6/bench_test.tsv'), '--item', 'vivonne1573-f102r-dev2',
        '--exclude-flagged', '--strict', '--coverage-diagnostic', '--ci']


def call(outs, extra, dst):
    if os.path.exists(dst):
        sys.exit(f'{dst} exists: scored once already')
    cmd = [sys.executable, os.path.join(REPO, 'tools/tx_bench.py')] + outs + ARGS + extra
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=REPO)
    open(dst, 'w').write('$ ' + ' '.join(cmd[1:]).replace(REPO + '/', '') + '\n' + r.stdout + r.stderr)
    print(dst, 'exit', r.returncode)


def main():
    os.makedirs(os.path.join(HERE, 'scores'), exist_ok=True)
    if sys.argv[1] == 'single':
        for run in sys.argv[2:]:
            call([os.path.join(HERE, 'reads', f'{run}.tsv')], [], os.path.join(HERE, 'scores', f'{run}.txt'))
    else:
        for rnd in sys.argv[2:]:
            call([os.path.join(HERE, 'reads', f'W{rnd}.tsv')], ['--paired', os.path.join(HERE, 'reads', f'D{rnd}.tsv')],
                 os.path.join(HERE, 'scores', f'paired_W{rnd}_vs_D{rnd}.txt'))


if __name__ == '__main__':
    main()
