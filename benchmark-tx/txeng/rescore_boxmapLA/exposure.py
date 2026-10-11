#!/usr/bin/env python3
"""BOXMAP-RESCORE (others), 11 Oct 2026, account 3: how much of each txeng / txeng2 result sat on a shifted box.

For every committed pass that changed the line read L on no.87 (paired vs benchmark-tx/txeng/units/labels_<unit>.tsv), each changed
position is classed fixed / broken / both-wrong / both-right (homophone) (tools/tx_bench.py position_errors, flagged truth rows kept, as measured) and
marked `shifted` when its 1:1 box differs between the old map (compare/box_pos.tsv) and the label-aware one (shifted_positions.tsv,
written by box_pos_la.py) -- i.e. the tile a reader saw, or the box a read-free signal was computed on, belonged to a neighbouring
token. A FAIL whose broken positions sit mostly on shifted boxes may be the map's; one whose changes avoid them is not.
Writes exposure.tsv (one row per pass) and exposure_positions.tsv. Usage: python3 benchmark-tx/txeng/rescore_boxmapLA/exposure.py
"""
import csv, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import tx_bench as tb  # noqa: E402
O = os.path.join(ROOT, 'benchmark-tx/outputs/birago1572-no87')
PASSES = [  # (experiment, pass file, unit)
    ('TXE-A compare', 'passG_compare_dev_tune.tsv', 'dev_tune'),
    ('TXE-A M1b H_all', 'passG_compare_dev_tune_m1b_H_all.tsv', 'dev_tune'),
    ('TXE-A M1b H_top1', 'passG_compare_dev_tune_m1b_H_top1.tsv', 'dev_tune'),
    ('TXE-A M1b any_top1', 'passG_compare_dev_tune_m1b_any_top1.tsv', 'dev_tune'),
    ('TXE-S library', 'passG2_library_dev_tune.tsv', 'dev_tune'),
    ('TXE-S library r1', 'passG2_library_dev_tune_r1.tsv', 'dev_tune'),
    ('TXE-S library r2', 'passG2_library_dev_tune_r2.tsv', 'dev_tune'),
    ('TXE-L ordered', 'passT_ordered_dev.tsv', 'dev_tune'),
    ('TXE-L shuffled', 'passT_shuffled_dev.tsv', 'dev_tune'),
    ('TXE-K adjud fable', 'passS_adj_fable_dev_tune.tsv', 'dev_tune'),
    ('TXE-K adjud opus', 'passS_adj_opus_dev_tune.tsv', 'dev_tune'),
    ('TXE-C pair re-read', 'passJ_pair_dev_tune.tsv', 'dev_tune'),
    ('TXE-J stab', 'passR_stab_dev_tune.tsv', 'dev_tune'),
    ('TXE-D prep sr4', 'passK2_sr4_dev_tune.tsv', 'dev_tune'),
    ('TXE2-CELLS real', 'passX13_real_dev_tune.tsv', 'dev_tune'),
    ('TXE2-SAME X7', '../../txeng2/same/passX7_dev_tune.tsv', 'dev_tune'),
    ('TXE2-SAME X7 swap ctrl', '../../txeng2/same/passX7swap_dev_tune.tsv', 'dev_tune'),
    ('TXE2-LATT word LOO', '../../txeng2/latt/out/word_loo.tsv', 'dev_tune'),
]


def main():
    sh = {(r['line'], r['pos']) for r in csv.DictReader(open(os.path.join(HERE, 'shifted_positions.tsv')), delimiter='\t')}
    truth = tb.read_tsv(os.path.join(ROOT, 'benchmark-tx/birago1572-no87.truth.tsv'))
    out, pos = [], []
    for exp, f, unit in PASSES:
        p = os.path.join(O, f)
        if not os.path.exists(p):
            print('missing', f); continue
        L = tb.load_output([os.path.join(ROOT, f'benchmark-tx/txeng/units/labels_{unit}.tsv')])
        X = tb.load_output([p], None)
        X = {k: v for k, v in X.items() if k in L}
        eL, eX = tb.position_errors(truth, L), tb.position_errors(truth, X)
        Ls = {(ln, p_): s for ln, v in tb_rows(os.path.join(ROOT, f'benchmark-tx/txeng/units/labels_{unit}.tsv')).items() for p_, s in v}
        Xs = {(ln, p_): s for ln, v in tb_rows(p).items() for p_, s in v}
        ch = [k for k in Ls if k in Xs and Xs[k] != Ls[k]]
        c = dict(exp=exp, file=f, unit=unit, changed=len(ch), changed_shifted=sum(k in sh for k in ch), fixed=0, fixed_shifted=0,
                 broken=0, broken_shifted=0, both_wrong=0, both_right=0, unscored=0)
        for k in ch:
            if k not in eL or k not in eX:
                c['unscored'] += 1; cls = 'unscored'
            elif eL[k] and not eX[k]:
                c['fixed'] += 1; c['fixed_shifted'] += k in sh; cls = 'fixed'
            elif eX[k] and not eL[k]:
                c['broken'] += 1; c['broken_shifted'] += k in sh; cls = 'broken'
            elif eL[k]:
                c['both_wrong'] += 1; cls = 'both-wrong'
            else:
                c['both_right'] += 1; cls = 'both-right (homophone)'
            pos.append(dict(exp=exp, line=k[0], pos=k[1], L=Ls[k], out=Xs[k], cls=cls, shifted=int(k in sh)))
        out.append(c)
    cols = list(out[0])
    with open(os.path.join(HERE, 'exposure.tsv'), 'w') as fh:
        fh.write('\t'.join(cols) + '\n' + ''.join('\t'.join(str(r[c]) for c in cols) + '\n' for r in out))
    pc = list(pos[0])
    with open(os.path.join(HERE, 'exposure_positions.tsv'), 'w') as fh:
        fh.write('\t'.join(pc) + '\n' + ''.join('\t'.join(str(r[c]) for c in pc) + '\n' for r in pos))
    for r in out:
        print('\t'.join(str(r[c]) for c in cols))


def tb_rows(p):
    d = {}
    for r in tb.read_tsv(p):
        d.setdefault(r['line'], []).append((str(r['pos']), r['sign']))
    return d


if __name__ == '__main__':
    main()
