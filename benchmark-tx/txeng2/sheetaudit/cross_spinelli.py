#!/usr/bin/env python3
"""TXE2-SHEETAUDIT (9 Oct 2026): cross every exemplar of a Spinelli reader sheet (glyphs/atlas*.tsv) against the
confirm item's truth, reading truth rows ONLY at exemplar positions.

sid p1_LL_BBB / p2L1_01_BBB / p2L2_01_BBB -> (page, line, box) -> passes/p{1,2}_reconciled_v4.tsv (line, box) -> pos
(v6 keeps v4's page/line/pos keys, build_v6_split.py) -> truth line p1c_L0<line> / p2c_L0<line>, pos.

    python3 benchmark-tx/txeng2/sheetaudit/cross_spinelli.py ciphers/spinelli-beinecke-c1515/glyphs/atlas.tsv
"""
import csv, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
F = os.path.join(ROOT, 'ciphers/spinelli-beinecke-c1515')
TRUTH = os.path.join(ROOT, 'benchmark-tx/spinelli-c1519-confirm.truth.tsv')
# v3 merges (atlas.tsv desc): a v6 code belongs to a v3 cell if its base is the cell or a merged member
MERGE = {'HOOK': {'HOOK', 'ELOOP', 'ECAP', 'RHO', 'TLOOP', 'UCURL', 'MU', 'JHOOK'}, 'OMEGABAR': {'OMEGABAR', 'OMEGA2'},
         'SEVEN': {'SEVEN', 'SEVENB', 'CARET'}, 'TWO': {'TWO', 'TWOFLAT', 'DEE'}}
# atlas_v2 cells are finer than the truth's code families: fold a v2 cell to its v3 cell first (atlas.tsv desc)
V2TO3 = {c: k for k, v in MERGE.items() for c in v}


def rd(p):
    with open(p, newline='') as f:
        return list(csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t'))


def base(code):
    return code.split('_')[0]


def main(atlas):
    box = {}
    for fn, pg in (('p1_reconciled_v4.tsv', 'p1'), ('p2_reconciled_v4.tsv', 'p2')):
        for r in rd(os.path.join(F, 'passes', fn)):
            box.setdefault((pg, int(r['line']), int(r['box'])), []).append((int(r['pos']), r['code']))
    want = {}
    rows = rd(atlas)
    for r in rows:
        for sid in r['exemplars'].split(','):
            unit, ln, b = sid.split('_')
            pg, line = ('p1', int(ln)) if unit == 'p1' else ('p2', 1 if unit == 'p2L1' else 2)
            hits = box.get((pg, line, int(b)), [])
            want[sid] = (r['code'], pg, line, hits)
    # read truth only at the exemplar positions
    keys = {(f'{pg}c_L{line:02d}', str(p)) for (_, pg, line, hits) in want.values() for p, _ in hits}
    truth = {(t['line'], t['pos']): t for t in rd(TRUTH) if (t['line'], t['pos']) in keys}
    w = csv.writer(sys.stdout, delimiter='\t', lineterminator='\n')
    w.writerow(['sheet', 'cell', 'box', 'truth_pos', 'v4_code', 'truth', 'plain', 'status', 'verdict'])
    for r in rows:
        for sid in r['exemplars'].split(','):
            cell, pg, line, hits = want[sid]
            if not hits:
                w.writerow([os.path.basename(atlas), cell, sid, '-', '-', '-', '-', 'not in v4 reconciliation', 'no-truth (box not a committed sign)'])
                continue
            for p, v4 in hits:
                t = truth.get((f'{pg}c_L{line:02d}', str(p)))
                if t is None:
                    w.writerow([os.path.basename(atlas), cell, sid, f'{pg}c_L{line:02d}.{p}', v4, '-', '-', 'no truth row', 'no-truth'])
                    continue
                tv = t['truth']
                c3 = V2TO3.get(cell, cell)
                mem = MERGE.get(c3, {c3})
                if not tv:
                    verdict = 'no-truth (' + t['status'] + ')'
                elif any(base(c) in mem for c in tv.split('|')):
                    verdict = 'OK'
                else:
                    verdict = 'MISLABELLED'
                w.writerow([os.path.basename(atlas), cell, sid, f'{pg}c_L{line:02d}.{p}', v4, tv, t['plain'], t['status'], verdict])


if __name__ == '__main__':
    main(sys.argv[1])
