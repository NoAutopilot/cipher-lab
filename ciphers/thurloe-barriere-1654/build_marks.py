#!/usr/bin/env python3
"""Reconciles the two blind mark-typing subagent passes (ZX-BAR2, 25 Sept 2026) against mark_positions.tsv and
key_gloss.tsv, writes marks.tsv (run, position, code, mark, grade) and key_gloss_marked.tsv (key_gloss.tsv with
'code' replaced by the 'BARECODE-MARK' unit). Disagreements are listed for manual settling from the image crop
(NOTES.md documents each one); this script does not itself look at any image.

Usage: python3 build_marks.py passX.tsv passY.tsv [--settle settle.tsv]
Input pass files: crop_id, position(1-based int), token_text, mark, confidence -- pipe- or tab-separated (this
parser accepts either), one header line starting with 'crop_id' ignored if present.
--settle is an optional TSV (crop_id, position, mark) giving the human-settled value for every disagreement;
without it, disagreements are printed and left out of key_gloss_marked.tsv (grade M rows still list the two
raw calls in the note field for the record).
"""
import argparse
import csv
import sys

VALID_MARKS = {'circumflex', 'grave', 'acute', 'macron', 'caron', 'diaeresis', 'dot', 'none', 'unreadable'}


def load_pass(path):
    rows = {}
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.lower().startswith('crop_id'):
                continue
            sep = '|' if '|' in line else '\t'
            parts = [p.strip() for p in line.split(sep)]
            if len(parts) < 4:
                continue
            crop_id, pos, token_text, mark = parts[0], parts[1], parts[2], parts[3]
            mark = mark.lower()
            if mark not in VALID_MARKS:
                continue
            try:
                pos = int(pos)
            except ValueError:
                continue
            rows[(crop_id, pos)] = mark
    return rows


def load_tsv(path):
    rows = []
    with open(path) as f:
        header = None
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            row = line.rstrip('\n').split('\t')
            if header is None:
                header = row
                continue
            rows.append(dict(zip(header, row)))
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('passX')
    ap.add_argument('passY')
    ap.add_argument('--settle', default=None, help='TSV of crop_id, position, mark for manually-settled disagreements')
    ap.add_argument('--positions', default='mark_positions.tsv')
    ap.add_argument('--keygloss', default='key_gloss.tsv')
    args = ap.parse_args()

    passX = load_pass(args.passX)
    passY = load_pass(args.passY)
    settled = {}
    if args.settle:
        for r in load_tsv(args.settle):
            settled[(r['crop_id'], int(r['position']))] = r['mark']

    positions = load_tsv(args.positions)
    keygloss = load_tsv(args.keygloss)
    kg_by_key = {(d['code'], d['source_run']): d for d in keygloss}

    marks_out = []
    disagreements = []
    marked_out_rows = []
    for p in positions:
        key = (p['crop_id'], int(p['position']))
        mx = passX.get(key)
        my = passY.get(key)
        kg = kg_by_key.get((p['code'], p['source_run']))
        if kg is None:
            print(f'WARNING: {p} has no matching key_gloss.tsv row', file=sys.stderr)
            continue
        if mx is None or my is None:
            print(f'WARNING: missing pass data for {key} (code {p["code"]})', file=sys.stderr)
            continue
        if mx == my:
            final, grade = mx, 'H'
        elif key in settled:
            final, grade = settled[key], 'M'
        else:
            disagreements.append((p['crop_id'], p['position'], p['code'], p['source_run'], mx, my))
            continue
        marks_out.append({'source_run': p['source_run'], 'position': p['position'], 'code': p['code'],
                           'mark': final, 'grade': grade, 'passX': mx, 'passY': my})
        marked_code = p['code'].split('(')[0] + '-' + final
        # preserve the '(Nth obs)' suffix if present, so permutation_test.py's own split('(')[0] still works
        suffix = p['code'][len(p['code'].split('(')[0]):]
        marked_code = p['code'].split('(')[0] + '-' + final + suffix
        marked_out_rows.append({**kg, 'code': marked_code})

    with open('marks.tsv', 'w') as f:
        f.write('# Reconciled mark type per key_gloss.tsv occurrence (ZX-BAR2, 25 Sept 2026). grade H = both\n')
        f.write('# blind subagent passes agreed; grade M = settled from the image crop after disagreement.\n')
        f.write('source_run\tposition\tcode\tmark\tgrade\tpassX_call\tpassY_call\n')
        for m in marks_out:
            f.write(f"{m['source_run']}\t{m['position']}\t{m['code']}\t{m['mark']}\t{m['grade']}\t{m['passX']}\t{m['passY']}\n")

    if marked_out_rows:
        header = ['code', 'value', 'grade', 'status', 'source_run', 'note']
        with open('key_gloss_marked.tsv', 'w') as f:
            f.write('# key_gloss.tsv with code+mark as the key unit (ZX-BAR2, 25 Sept 2026). See NOTES.md ZX-BAR2\n')
            f.write('# section and marks.tsv/mark_positions.tsv for how each mark was read and reconciled.\n')
            f.write('# status/note columns are copied unchanged from key_gloss.tsv (they describe the BARE-code\n')
            f.write('# conflict, not recomputed for code+mark -- the conflict count after marking is reported in\n')
            f.write('# NOTES.md, not by these columns).\n')
            f.write('\t'.join(header) + '\n')
            for r in marked_out_rows:
                f.write('\t'.join(r.get(h, '') for h in header) + '\n')

    print(f'{len(marks_out)} rows settled ({sum(1 for m in marks_out if m["grade"]=="H")} H, '
          f'{sum(1 for m in marks_out if m["grade"]=="M")} M), {len(disagreements)} unresolved disagreements')
    for d in disagreements:
        print('DISAGREEMENT', d)


if __name__ == '__main__':
    main()
