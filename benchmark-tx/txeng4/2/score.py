#!/usr/bin/env python3
"""TXE4-2 DINT-PIC: the ONE scoring call per output (PREREG-txeng4-2.md "Endpoint"). Runs tools/tx_bench.py on dint-f128-print
mapped (primary, --label-map benchmark-tx/dint128_label_map.tsv) and raw, each with --coverage-diagnostic --strict --ci and
--exclude-flagged (no flags file: identical mask), writes the full console to scores/<name>.<mapped|raw>.txt (the truth-value
confusion lines stay there, never on the worker's screen) and prints only the headline lines. Refuses to score a name twice.
    python3 benchmark-tx/txeng4/2/score.py NAME OUTPUT.tsv [--paired BASE.tsv]     (NAME in baseline_A, baseline_B, T1, P1, S1, T2, P2, S2)
"""
import os, re, subprocess, sys
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
HERE = os.path.dirname(os.path.abspath(__file__))
KEEP = re.compile(r'err_true|standard SER|strict|flagged|coverage|scored|Wilson|edits|McNemar|improved|bootstrap|^\S+\.tsv|sign test|SER-diff')
HIDE = re.compile(r'<-|->|confusion|truth value|per value|per_value')


def run(name, out, paired=None):
    for tag, extra in (('mapped', ['--label-map', 'benchmark-tx/dint128_label_map.tsv']), ('raw', [])):
        dst = os.path.join(HERE, 'scores', f'{name}.{tag}.txt')
        if os.path.exists(dst):
            sys.exit(f'{dst} exists: {name} was already scored ({tag}); one score per output')
        cmd = ['python3', 'tools/tx_bench.py', out, '--bench', 'BENCHMARK-TX.tsv', '--item', 'dint-f128-print',
               '--coverage-diagnostic', '--strict', '--ci', '--exclude-flagged'] + extra
        if paired:
            cmd += ['--paired', paired]
        p = subprocess.run(cmd, cwd=R, capture_output=True, text=True)
        open(dst, 'w').write('# ' + ' '.join(cmd) + '\n' + p.stdout + p.stderr)
        print(f'== {name} {tag} (full console in {os.path.relpath(dst, R)})')
        for ln in p.stdout.splitlines():
            if KEEP.search(ln) and not HIDE.search(ln):
                print('  ' + ln[:260])


if __name__ == '__main__':
    a = sys.argv[1:]
    paired = a[a.index('--paired') + 1] if '--paired' in a else None
    run(a[0], a[1], paired)
