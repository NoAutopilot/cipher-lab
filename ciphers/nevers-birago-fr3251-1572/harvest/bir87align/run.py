#!/usr/bin/env python3
"""BIR87-ALIGN step 2 (4 Oct 2026), per PREREG.md: clerk-sheet alignment of no.87 under the owner's piles + shuffled-sheet null.
  python3 run.py [--seeds 20]      (from anywhere; disk only, deterministic)
Writes align_<seq>.tsv, key_<seq>.tsv, codes_<seq>.tsv, null.tsv, piles.tsv, splits.tsv, summary.json."""
import argparse, csv, json, subprocess, sys, tempfile
from collections import Counter, defaultdict
from pathlib import Path
D = Path(__file__).resolve().parent; A = D.parent / 'align87'; TOOL = D.parents[3] / 'tools/interlinear_align.py'
ap = argparse.ArgumentParser(); ap.add_argument('--seeds', type=int, default=20); a = ap.parse_args()
OPT = ['--floor', '5000', '--digits', '4', '--keep-fs', '--word-prior', '--prior', str(A / 'prior.tsv')]
tmp = Path(tempfile.mkdtemp()); rd = lambda p: list(csv.DictReader(open(p), delimiter='\t'))

def run(seq, shuffle=None, keep=False):
    args = [] if seq is None else ['--cipher-dir', str(D / seq)]
    if shuffle is not None: args += ['--shuffle-words', str(shuffle)]
    tag = seq or 'committed'
    pr, co = tmp / 'p.tsv', (D / f'codes_{tag}.tsv' if keep else tmp / 'c.tsv')
    subprocess.run([sys.executable, str(A / 'build_pairs.py'), '--out', str(pr), '--codes', str(co)] + args, check=True, capture_output=True)
    al, k = (D / f'align_{tag}.tsv', D / f'key_{tag}.tsv') if keep else (tmp / 'a.tsv', tmp / 'k.tsv')
    subprocess.run([sys.executable, str(TOOL), 'align', str(pr), str(al), str(k)] + OPT, check=True, capture_output=True)
    st = [r['status'] for r in rd(al)]
    key = {int(r['value']): (r['meaning'], int(r['n']), int(r['agree'])) for r in rd(k)}
    return sum(s == 'agrees' for s in st) / len(st), key, co

out = {}; nullrows = []
for seq in (None, 'cipher_owner', 'cipher_moved'):
    tag = seq or 'committed'
    real, key, co = run(seq, keep=True)
    codes = {}
    for r in rd(co): codes.setdefault(int(r['code']), r['sign_id'])
    piles = {c: s for c, s in codes.items() if s.startswith('P:')}
    nul = []; pnull = defaultdict(list)
    for s in range(1, a.seeds + 1):
        x, k, _ = run(seq, shuffle=s); nul.append(x); nullrows.append((tag, s, f'{x:.4f}'))
        for c in piles:
            m, n, ag = k.get(c, ('', 0, 0)); pnull[c].append(ag / n if n else 0.0)
    gate = real > max(nul)
    out[tag] = dict(real=round(real, 4), null_mean=round(sum(nul) / len(nul), 4), null_max=round(max(nul), 4), gate=gate)
    print(tag, out[tag], flush=True)
    if not piles: continue
    rows = []
    for c, s in sorted(piles.items(), key=lambda x: x[1]):
        m, n, ag = key.get(c, ('', 0, 0)); sh = ag / n if n else 0.0
        above = sh > max(pnull[c])
        if n < 2: g = 'no evidence'
        elif gate and ag >= 2 and sh >= 0.6 and above: g = 'C'
        else: g = 'M'
        ntok = sum(1 for v in codes.values() if v == s)
        rows.append(dict(seq=tag, pile=s[2:], code=c, tokens=sum(1 for r in rd(co) if r['sign_id'] == s), aligned_n=n, value=m,
                         agree=ag, share=round(sh, 3), null_max_share=round(max(pnull[c]), 3), above_null=above, grade=g))
    out[tag]['piles'] = rows
cols = list(out['cipher_owner']['piles'][0])
with open(D / 'piles.tsv', 'w') as f:
    f.write('\t'.join(cols) + '\n')
    for t in ('cipher_owner', 'cipher_moved'):
        for r in out[t]['piles']: f.write('\t'.join(str(r[c]) for c in cols) + '\n')
with open(D / 'null.tsv', 'w') as f:
    f.write('seq\tseed\tagrees\n' + ''.join('\t'.join(map(str, r)) + '\n' for r in nullrows))
json.dump(out, open(D / 'summary.json', 'w'), indent=1)
