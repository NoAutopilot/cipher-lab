#!/usr/bin/env python3
"""VIV-HUMAN (PREREG-VIVHUMAN.md): question sets W and R on f.201r (vivonne1573-f201r-dev) and the sorter inputs.

W = unflagged scored truth positions where passA or passB (or both) is wrong; R = unflagged scored positions where both are right.
Each pass is aligned to the truth rows with tools/tx_bench.align (the scorer's own alignment). A position can be a question only
if it has a single pen-unit tile: passA's token at that position is mapped 1:1 to exactly one tile in VIV-CLS's committed
round-2 map (tx/vivcls/real/map_r2_f201r.tsv, op 1:1). Sample with seed 20261014: 30 from W (all if fewer), 12 from R, shuffled.

  python3 ciphers/fr16104-vivonne-spain-1572/tx/vivhuman/sets.py            # writes questions.tsv (the answer sheet, truth inside)
  python3 ciphers/fr16104-vivonne-spain-1572/tx/vivhuman/sets.py --check    # exit 1 if questions.tsv is stale
The tile boxes and the page are built by build_inputs.py (needs the crops on disk); this script needs no image.
"""
import csv, os, random, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__))
FOLD = os.path.abspath(os.path.join(HERE, '..', '..'))
REPO = os.path.abspath(os.path.join(FOLD, '..', '..'))
sys.path.insert(0, os.path.join(REPO, 'tools'))
import tx_bench  # noqa: E402
BT = os.path.join(REPO, 'benchmark-tx')
TRUTH = os.path.join(BT, 'vivonne1573-f201r-dev.truth.tsv')
OUTS = os.path.join(BT, 'outputs', 'vivonne1573-f201r-dev')
MAP = os.path.join(FOLD, 'tx', 'vivcls', 'real', 'map_r2_f201r.tsv')
SEED, NW, NR = 20261014, 30, 12
# PREREG-VIVHUMAN.md Addendum A (box check before publishing, no answer yet): box not on the position's one sign
EXCLUDED = {'Q06': 'box on the sign after the s (map off by one)', 'Q10': 'box holds two signs (6 and the next)'}


def rd(p):
    return list(csv.DictReader((l for l in open(p) if not l.startswith('#')), delimiter='\t'))


def aligned(truth_by_line, out_rows):
    """(line, truth pos) -> (out sign, out pos) for every truth row the pass aligns a token to."""
    by = collections.defaultdict(list)
    for r in out_rows:
        by[r['line']].append(r)
    res = {}
    for ln, rows in truth_by_line.items():
        toks = sorted(by.get(ln, []), key=lambda r: int(r['pos']))
        ts = [set(filter(None, r['truth'].split('|'))) for r in rows]
        path = tx_bench.align([r['ref_sign'] for r in rows], ts, [t['sign'] for t in toks])
        j = 0
        for ri, osg in path:
            tok = None
            if osg is not None:
                tok = toks[j]; j += 1
            if ri is not None and tok is not None:
                res[(ln, rows[ri]['pos'])] = (tok['sign'], tok['pos'])
    return res


def build():
    truth = rd(TRUTH)
    tl = collections.defaultdict(list)
    for r in truth:
        tl[r['line']].append(r)
    for ln in tl:
        tl[ln].sort(key=lambda r: float(r['pos']))
    A = aligned(tl, rd(os.path.join(OUTS, 'passA.tsv')))
    B = aligned(tl, rd(os.path.join(OUTS, 'passB.tsv')))
    tile = collections.defaultdict(list)
    for m in rd(MAP):
        if m['op'] == '1:1':
            tile[(m['line'], m['pos'])].append(m['sid'])
    W, R, n_unfl, n_cov = [], [], 0, 0
    for r in truth:
        if r['status'] != 'scored' or r['flag']:
            continue
        n_unfl += 1
        T = set(filter(None, r['truth'].split('|')))
        a, b = A.get((r['line'], r['pos'])), B.get((r['line'], r['pos']))
        if not a:
            continue
        sids = tile.get((r['line'], a[1]), [])
        if len(sids) != 1:
            continue
        n_cov += 1
        aok, bok = a[0] in T, bool(b) and b[0] in T
        row = dict(sid=sids[0], line=r['line'], tpos=r['pos'], ref_sign=r['ref_sign'], truth='|'.join(sorted(T)), plain=r['plain'],
                   passA=a[0], passB=b[0] if b else '', a_ok=int(aok), b_ok=int(bok))
        (R if aok and bok else W).append(row)
    rng = random.Random(SEED)
    w = W if len(W) <= NW else rng.sample(W, NW)
    rr = R if len(R) <= NR else rng.sample(R, NR)
    q = [dict(x, set='W') for x in w] + [dict(x, set='R') for x in rr]
    rng.shuffle(q)
    for i, x in enumerate(q, 1):
        x['qid'] = f'Q{i:02d}'
        x['excluded'] = EXCLUDED.get(x['qid'], '')
    return q, dict(unflagged_scored=n_unfl, covered=n_cov, W=len(W), R=len(R))


COLS = ['qid', 'set', 'sid', 'line', 'tpos', 'ref_sign', 'truth', 'plain', 'passA', 'passB', 'a_ok', 'b_ok', 'excluded']


def render(q, st):
    lines = ['# VIV-HUMAN answer sheet (PREREG-VIVHUMAN.md): ' + ', '.join(f'{k} {v}' for k, v in st.items()) + f'; seed {SEED}',
             '\t'.join(COLS)]
    lines += ['\t'.join(str(x[c]) for c in COLS) for x in q]
    return '\n'.join(lines) + '\n'


if __name__ == '__main__':
    q, st = build()
    txt = render(q, st)
    p = os.path.join(HERE, 'questions.tsv')
    if '--check' in sys.argv:
        ok = os.path.exists(p) and open(p).read() == txt
        print('questions.tsv', 'current' if ok else 'STALE'); sys.exit(0 if ok else 1)
    open(p, 'w').write(txt)
    print(st, 'questions', len(q))
