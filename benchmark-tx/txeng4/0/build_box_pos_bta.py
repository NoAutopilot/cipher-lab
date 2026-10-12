#!/usr/bin/env python3
"""TXE4-0 REPAIR unit 2 (12 Oct 2026, account 3): build benchmark-tx/txeng/compare/box_pos_bta.tsv and the
pair/{dev_tune,eval_heldout} twins with tools/box_token_align.py's label-aware DP, extending coverage to f178r
(which atlas/no87_map.py's own --label-aware never covered: "f.178r is left out: its three lines slope across one
another and the segmenter's line split mixes them"). Same steering labels as atlas/no87_map.py --label-aware
(benchmark-tx/txeng/compare/topk_no87_allheld.tsv's classify top-3, plus the sorter seed/settled family tag), same
lam/neutral/own-label-leave-one-out defaults. Never reads a truth file.

Per line, runs tools/join_check.py's bounded gate (check labels = sorter/no87/seed.tsv's atlas top-1, leave-one-out,
since that label is part of what steers the map). An f178r line that FAILs or is UNCHECKABLE is left out of
box_pos_bta.tsv and listed on stdout and in RESULTS.md (BOXMAP-LA: f178r's line assignment is itself unreliable,
so this job does not spend trust pretending otherwise).

f178v/f179r rows are compared against benchmark-tx/txeng/rescore_boxmapLA/box_pos.tsv (the earlier BOXMAP-RESCORE
job's rebuild, itself a straight reformat of the committed atlas/no87_box_token_labelaware.tsv) on every shared
box; any difference is printed (there should be none: both read the same committed label-aware map for those two
pages).

Usage: python3 benchmark-tx/txeng4/0/build_box_pos_bta.py
"""
import csv
import os
import re
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import box_token_align as BA  # noqa: E402
import join_check as JC  # noqa: E402

T = os.path.join(ROOT, 'ciphers/nevers-birago-fr3251-1572')
H = os.path.join(T, 'harvest')
COMPARE = os.path.join(ROOT, 'benchmark-tx/txeng/compare')
PAIR = os.path.join(ROOT, 'benchmark-tx/txeng/pair')
OLD_RESCORE = os.path.join(ROOT, 'benchmark-tx/txeng/rescore_boxmapLA/box_pos.tsv')

LINES = [f'f178r_L{i:02d}' for i in (1, 2, 3)] + [f'f178v_L{i:02d}' for i in range(1, 24)] + \
        [f'f179r_L{i:02d}' for i in (1, 2, 3)]
rd = BA.rd


def fam(p):
    m = re.match(r'^(T\d+)(-[a-z])?$', (p or '').strip())
    return m.group(1) if m else None


def build():
    signs = rd(os.path.join(T, 'atlas/signs.tsv'))
    L = [r for r in rd(os.path.join(ROOT, 'benchmark-tx/outputs/birago1572-no87/labels.tsv')) if r['line'] in LINES]
    labels = BA.read_labels(os.path.join(COMPARE, 'topk_no87_allheld.tsv'))
    seed = {r['sid']: r for r in rd(os.path.join(T, 'sorter/no87/seed.tsv'))}
    settled = {r['sid']: r for r in rd(os.path.join(T, 'sorter/no87/owner-sort-2026-10-04/settled_no87.tsv'))}
    for sid, r in settled.items():
        f1 = fam(r['new_sign']) if r['status'] == 'moved' else fam(seed.get(sid, {}).get('seed'))
        if f1:
            labels[sid][f1] = 1.0
    status = {sid: BA.norm_status(r['status']) for sid, r in settled.items()}
    rows, per = BA.build_map(signs, L, labels, status, LINES, BA.LAM, BA.NEUTRAL, True, ())
    chk = {sid: r['atlas'] for sid, r in seed.items() if r.get('atlas') and r['atlas'] != '_'}
    rs = JC.read_sign_table(L)
    pos_loo = BA.positions(rows, loo=True)
    result = JC.evaluate(pos_loo, chk, rs)
    # f178r lines excluded by a 'fail' B1 verdict, or every f178r line when the whole check reads UNCHECKABLE; a
    # per-line 'unchecked' (<5 placed tiles) is kept -- that is thin evidence, not a shift failure.
    excluded = set()
    if result['verdict'] == 'UNCHECKABLE':
        excluded = {ln for ln in result['lines'] if ln.startswith('f178r')}
    else:
        excluded = {ln for ln, d in result['lines'].items() if ln.startswith('f178r') and d['verdict'] == 'fail'}
    kept_rows = [r for r in rows if r['line'] not in excluded]
    return rows, kept_rows, per, result, excluded


def to_old_format(rows):
    """box_token_align's own 9-col rows -> the old box_pos.tsv 4-col convention (sid, line, pos, op): a 2:1 pair's
    first box only, a 1:2 box's first token only, unsure kept with its own op (never 1:1)."""
    out, s2, s12 = [], set(), set()
    for r in rows:
        op = r['op']
        if op == '2:1':
            if (r['line'], r['pos']) in s2:
                continue
            s2.add((r['line'], r['pos']))
        elif op == '1:2':
            if r['sid'] in s12:
                continue
            s12.add(r['sid'])
        out.append(dict(sid=r['sid'], line=r['line'], pos=r['pos'], op=op))
    return out


def main():
    rows, kept_rows, per, result, excluded = build()
    old4 = to_old_format(kept_rows)
    os.makedirs(COMPARE, exist_ok=True)
    out = os.path.join(COMPARE, 'box_pos_bta.tsv')
    with open(out, 'w') as f:
        f.write('sid\tline\tpos\top\n' + ''.join(f"{r['sid']}\t{r['line']}\t{r['pos']}\t{r['op']}\n" for r in old4))

    # compare f178v/f179r rows against the earlier rebuild (both read the same committed label-aware map for those
    # pages, so this should be an exact match)
    ref = {(r['sid'], r['line'], r['pos'], r['op']) for r in rd(OLD_RESCORE) if not r['line'].startswith('f178r')}
    mine = {(r['sid'], r['line'], r['pos'], r['op']) for r in old4 if not r['line'].startswith('f178r')}
    diff = (ref - mine) | (mine - ref)

    sidecar_pos = BA.positions(kept_rows, loo=False)
    chk = {sid: r['atlas'] for sid, r in {r['sid']: r for r in rd(os.path.join(T, 'sorter/no87/seed.tsv'))}.items()
           if r.get('atlas') and r['atlas'] != '_'}
    rs = JC.read_sign_table([r for r in rd(os.path.join(ROOT, 'benchmark-tx/outputs/birago1572-no87/labels.tsv'))
                             if r['line'] in LINES])
    kept_result = JC.evaluate(sidecar_pos, chk, rs)
    sc = JC.write_sidecar(out, kept_result, inputs=[os.path.join(COMPARE, 'topk_no87_allheld.tsv'),
                                                     os.path.join(T, 'sorter/no87/seed.tsv')])

    print(f'box_pos_bta.tsv: {len(kept_rows)} rows ({len(rows)} before excluding f178r lines), '
          f'ops {dict((op, sum(1 for r in kept_rows if r["op"] == op)) for op in ("1:1", "unsure", "2:1", "1:2", "bad-cut", "aside", "skiptok"))}')
    print('f178r lines excluded (FAIL or whole-check UNCHECKABLE):', sorted(excluded) or 'none')
    print('f178v/f179r rows differing from rescore_boxmapLA/box_pos.tsv:', len(diff), diff if diff else '')
    print(f"join_check on box_pos_bta.tsv (in-sample positions): {kept_result['verdict']} "
          f"share0={kept_result['share0']:.3f} -> {sc}")

    # pair/{dev_tune,eval_heldout} twins: the same rows' 1:1 sid/line/pos, per unit's lines (tools/tx_pair_reread.py's
    # own box_pos.tsv has extra columns (L, es, cut, thin, selected, partner); this twin carries only the join, which
    # is what every consumer of its box_pos.tsv actually keys on)
    units = {'dev_tune': [f'f178v_L{i:02d}' for i in range(1, 13)],
             'eval_heldout': [f'f178v_L{i:02d}' for i in range(13, 24)] + [f'f179r_L{i:02d}' for i in (1, 2, 3)]}
    for unit, lines in units.items():
        sub = [r for r in kept_rows if r['line'] in lines]
        d = os.path.join(PAIR, unit)
        os.makedirs(d, exist_ok=True)
        p = os.path.join(d, 'box_pos_bta.tsv')
        with open(p, 'w') as f:
            f.write('sid\tline\tpos\top\n' + ''.join(f"{r['sid']}\t{r['line']}\t{r['pos']}\t{r['op']}\n"
                                                      for r in to_old_format(sub)))
        pos_u = BA.positions(sub, loo=False)
        chk_u = {sid: lab for sid, lab in chk.items() if sid in pos_u}
        rs_u = JC.read_sign_table([r for r in rd(os.path.join(ROOT, 'benchmark-tx/outputs/birago1572-no87/labels.tsv'))
                                   if r['line'] in lines])
        ru = JC.evaluate(pos_u, chk_u, rs_u)
        scu = JC.write_sidecar(p, ru, inputs=[])
        print(f'{unit}: {p} ({len(sub)} rows); join_check {ru["verdict"]} -> {scu}')


if __name__ == '__main__':
    main()
