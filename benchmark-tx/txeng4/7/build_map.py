#!/usr/bin/env python3
"""TXE4-7 PILE-LM (12 Oct 2026, account 3): the machine-only box-to-token maps, R4a (benchmark-tx/PREREG-txeng4-7.md).

  python3 benchmark-tx/txeng4/7/build_map.py r1      # round-1 training labels (atlas/secure_tokens.tsv minus f152r) + kNN
  python3 benchmark-tx/txeng4/7/build_map.py r2      # round-2: f174v/f174vB L01-11 aligned with the round-1 kNN (shift check
                                                     # pasted), PASS-line 1:1 boxes join the training set, kNN re-run
  python3 benchmark-tx/txeng4/7/build_map.py targets # no.87 (f178v L01-23, f179r L01-03) and f152r (L01-04) maps with
                                                     # --loo --check-labels (top-1, steered -> leave-one-out) --check-bound
No truth file, no sorter status, no owner pile, no labels.json label (--only-train-labels). Run from the repo root."""
import csv, os, subprocess, sys
from collections import defaultdict
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
os.chdir(ROOT)
A = 'ciphers/nevers-birago-fr3251-1572/atlas'; H = 'ciphers/nevers-birago-fr3251-1572/harvest'
X = 'benchmark-tx/txeng4/7'; K = f'{X}/knn'; M = f'{X}/map'
HOLD = ['--holdout', 'f152r_', '--holdout', 'f178r_', '--holdout', 'f178v_', '--holdout', 'f179r_']
R2_PAGES = {'f174v': ('f174v', 11), 'f174vB': ('f174vB', 11)}   # harvest dir -> (atlas page, lines 1..n = L01..Ln)


def rd(p):
    return list(csv.DictReader((l for l in open(p) if not l.startswith('#')), delimiter='\t'))


def wr(p, cols, rows):
    with open(p, 'w') as f:
        f.write('\t'.join(cols) + '\n')
        for r in rows:
            f.write('\t'.join(str(r.get(c, '')) for c in cols) + '\n')


def sh(*a):
    print('$', ' '.join(a), flush=True)
    subprocess.run(list(a), check=True)


def classify(train, out):
    sh(sys.executable, 'tools/glyph_atlas.py', 'classify', '--out', A, '--labels', f'{A}/labels.json', '--page', 'all',
       '--tsv', out, '--topk', '3', '--train-labels', train, '--only-train-labels', *HOLD)
    # a check-labels file carrying BOTH the topk columns (box, k1..k3) and sid, label (= top-1), so one file can be
    # passed as --topk and --check-labels (box_token_align then scores the leave-one-out row: steered).
    rows = rd(out)
    for r in rows:
        r['sid'] = r['box']; r['label'] = r['k1']
    wr(out, ['sid', 'label', 'box', 'page', 'line', 'pos', 'k1', 'd1', 's1', 'k2', 'd2', 's2', 'k3', 'd3', 's3'], rows)


def r1():
    rows = [r for r in rd(f'{A}/secure_tokens.tsv') if r['page'] != 'f152r']
    wr(f'{K}/train_r1.tsv', ['box', 'code', 'page', 'grade'], [dict(box=r['sid'], code=r['code'], page=r['page'], grade=r['grade']) for r in rows])
    print(f'round-1 training labels: {len(rows)} boxes (secure_tokens.tsv minus f152r)')
    classify(f'{K}/train_r1.tsv', f'{K}/topk_r1.tsv')


def sib_read(sib, page, n):
    """harvest/<sib>/passC_agreement.tsv -> read TSV lines <page>_L01..Lnn, pos in file order, sign = merged | idA | idB."""
    out = []
    for r in rd(f'{H}/{sib}/passC_agreement.tsv'):
        psg = r['passage']
        if not (psg.startswith('L') and psg[1:].isdigit() and int(psg[1:]) <= n):
            continue
        sg = r['merged'] or r['idA'] or r['idB']
        if not sg or sg == '?':
            continue
        out.append(dict(line=f'{page}_L{int(psg[1:]):02d}', sign=sg))
    pos = defaultdict(int); rows = []
    for r in out:
        pos[r['line']] += 1; rows.append(dict(line=r['line'], pos=pos[r['line']], sign=r['sign']))
    return rows


def align(read_tsv, topk, out, signs=f'{A}/signs.tsv'):
    sh(sys.executable, 'tools/box_token_align.py', '--signs', signs, '--read', read_tsv, '--topk', topk,
       '--check-labels', topk, '--check-bound', '--out', out, '--lines-out', out.replace('.tsv', '_lines.tsv'))


def pass_lines(map_tsv):
    import json
    sc = json.load(open(map_tsv + '.joincheck.json'))
    return sc['verdict'], {ln: d['verdict'] for ln, d in sc['lines'].items()}


def r2():
    train = rd(f'{K}/train_r1.tsv'); have = {r['box'] for r in train}
    added = 0
    for sib, (page, n) in R2_PAGES.items():
        read = sib_read(sib, page, n)
        wr(f'{M}/read_{page}.tsv', ['line', 'pos', 'sign'], read)
        sign_at = {(r['line'], r['pos']): r['sign'] for r in read}
        try:
            align(f'{M}/read_{page}.tsv', f'{K}/topk_r1.tsv', f'{M}/map_{page}_r2.tsv')
        except subprocess.CalledProcessError as e:
            print(f'{page}: box_token_align exit {e.returncode} (FAIL or UNCHECKABLE; see sidecar)')
        verdict, per = pass_lines(f'{M}/map_{page}_r2.tsv')
        print(f'{page}: join_check {verdict}; lines ' + ' '.join(f'{l}:{v}' for l, v in sorted(per.items())))
        for r in rd(f'{M}/map_{page}_r2.tsv'):
            if verdict == 'PASS' and r['op'] == '1:1' and per.get(r['line']) == 'pass' and r['sid'] not in have:
                sg = sign_at.get((r['line'], int(r['pos'])))
                if sg and sg != '?':
                    train.append(dict(box=r['sid'], code=sg, page=page, grade='S-r2')); have.add(r['sid']); added += 1
    wr(f'{K}/train_r2.tsv', ['box', 'code', 'page', 'grade'], train)
    print(f'round-2 training labels: {len(train)} boxes ({added} added from PASS lines of ' + ', '.join(R2_PAGES) + ')')
    classify(f'{K}/train_r2.tsv', f'{K}/topk_r2.tsv')


def targets():
    # no.87: passC lines f178v L01-23, f179r L01-03 (f178r is not a unit line; not mapped, as the prior maps)
    rows = [r for r in rd('benchmark-tx/outputs/birago1572-no87/passC.tsv') if not r['line'].startswith('f178r')]
    wr(f'{M}/read_no87.tsv', ['line', 'pos', 'sign'], rows)
    try:
        align(f'{M}/read_no87.tsv', f'{K}/topk_r2.tsv', f'{M}/map_no87.tsv')
    except subprocess.CalledProcessError as e:
        print(f'no87: box_token_align exit {e.returncode}')
    # f152r: atlas page lines 2-5 = letter L01-L04, TXE3-7's x bounds (benchmark-tx/txeng3/7/map_f152r.py, unchanged):
    # L01 keeps boxes with centre x > 2520, L04 boxes with centre x < 2460 (the prose boxes dropped). The signs file is
    # rewritten for the DP with line = atlas line - 1 so the read lines can be named f152r_L01..L04.
    XB = {1: lambda cx: cx > 2520, 4: lambda cx: cx < 2460}
    S = rd(f'{A}/signs.tsv'); keep = []
    for r in S:
        if r['page'] != 'f152r':
            continue
        ln = int(r['line']) - 1
        if ln < 1 or ln > 4:
            continue
        cx = int(r['x']) + int(r['w']) / 2
        if ln in XB and not XB[ln](cx):
            continue
        r = dict(r); r['line'] = str(ln); keep.append(r)
    wr(f'{M}/signs_f152r.tsv', list(S[0].keys()), keep)
    print(f'f152r: {len(keep)} atlas boxes kept on lines 2-5 -> L01-L04')
    rows = rd('benchmark-tx/outputs/birago1572-f152r/passZ_pipeline.tsv')
    wr(f'{M}/read_f152r.tsv', ['line', 'pos', 'sign'], rows)
    try:
        align(f'{M}/read_f152r.tsv', f'{K}/topk_r2.tsv', f'{M}/map_f152r.tsv', signs=f'{M}/signs_f152r.tsv')
    except subprocess.CalledProcessError as e:
        print(f'f152r: box_token_align exit {e.returncode}')
    for t in ('no87', 'f152r'):
        verdict, per = pass_lines(f'{M}/map_{t}.tsv')
        print(f'{t}: join_check {verdict}; lines ' + ' '.join(f'{l}:{v}' for l, v in sorted(per.items())))


if __name__ == '__main__':
    {'r1': r1, 'r2': r2, 'targets': targets}[sys.argv[1]]()
