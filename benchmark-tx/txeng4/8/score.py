#!/usr/bin/env python3
"""TXE4-8 BOX-ANCHOR scorer (PREREG-txeng4-8.md 'Scoring'). Run ONCE per committed read.
    python3 score.py PASS            PASS one of N1 N2 O1 O2 R1; reads reads/PASS.tsv (sha256 in SHA256SUMS.prescore)
O and R box rows -> positions: tokens in box order; a '-' box adds no position; several space-separated tokens add several
positions (alt kept on the first). N read as is. Writes reads/PASS.pos.tsv (O, R) and scores/PASS.txt + scores/PASS.json from
tools/tx_bench.py --bench benchmark-tx/txeng3/6/bench_test.tsv --exclude-flagged --strict --coverage-diagnostic --ci."""
import hashlib, json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
p = sys.argv[1]
src = os.path.join(HERE, 'reads', f'{p}.tsv')
sha = hashlib.sha256(open(src, 'rb').read()).hexdigest()
pre = open(os.path.join(HERE, 'SHA256SUMS.prescore')).read()
assert f'{sha}  reads/{p}.tsv' in pre, f'{p}: read not in SHA256SUMS.prescore (commit it first)'
if p[0] in 'OR':
    rows = [l.rstrip('\n').split('\t') for l in open(src, encoding='utf-8') if l.strip()]
    head = rows[0]; bi, si = head.index('box'), head.index('signs')
    ai = head.index('alt') if 'alt' in head else None; ki = head.index('conf') if 'conf' in head else None
    body = sorted(((r[0], int(r[bi]), r) for r in rows[1:] if len(r) > si), key=lambda t: (t[0], t[1]))
    out = os.path.join(HERE, 'reads', f'{p}.pos.tsv'); pos = {}
    with open(out, 'w', encoding='utf-8') as fh:
        fh.write('line\tpos\tsign\talt\tconf\n')
        for ln, b, r in body:
            toks = [t for t in r[si].split() if t and t != '-']
            for j, t in enumerate(toks):
                pos[ln] = pos.get(ln, 0) + 1
                alt = (r[ai] if ai is not None and ai < len(r) else '') if j == 0 else ''
                conf = r[ki] if ki is not None and ki < len(r) else ''
                fh.write(f'{ln}\t{pos[ln]}\t{t}\t{alt}\t{conf}\n')
    src = out
cmd = [sys.executable, os.path.join(ROOT, 'tools/tx_bench.py'), '--bench', os.path.join(ROOT, 'benchmark-tx/txeng3/6/bench_test.tsv'),
       '--exclude-flagged', '--strict', '--coverage-diagnostic', '--ci', src]
txt = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
js = subprocess.run(cmd + ['--json'], capture_output=True, text=True, cwd=ROOT)
open(os.path.join(HERE, 'scores', f'{p}.txt'), 'w').write('# ' + ' '.join(cmd[1:]) + '\n' + txt.stdout + txt.stderr)
open(os.path.join(HERE, 'scores', f'{p}.json'), 'w').write(js.stdout)
print(txt.stdout[-1500:])
