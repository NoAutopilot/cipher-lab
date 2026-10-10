#!/usr/bin/env python3
"""THUR-MEAD (LANE FAMILY-A2s, 10 Oct 2026): Philip Meadowe's period key sheet, BL Add MS 4166 f.102v-103r (DECODE R4890, images
IMG_R4890_I28428_P2/P3), regenerated from the blind transcription passes.

python3 meadowe_sheet.py [--check]

Inputs (passes/):
  A_p2_letters.tsv, B_p2_letters.tsv      letter table on f.102v (column letter, row, code), two blind Sonnet passes
  A_p3_head.tsv, B_p3_head.tsv            f.103r head: letter-table columns Y/Z continued, and the "Nulls" table
  A_p3_uncypher.tsv, B_p3_uncypher.tsv    f.103r "To uncypher" table, codes 1-104 -> letter or nul (a second witness on the same sheet)
  A_p3_names.tsv, B_p3_names.tsv          f.103r name list, codes 539-614
  eye_r4891.tsv                           worker's eye read of the second copy's letter table (R4891 P2, columns A-P)
  eye_conflicts.tsv                       worker's eye check of every table/uncypher disagreement (listed, not settled)
Output: key_period_meadowe_f102.tsv (code, value, class, sheet_label, passes, sheet_witness2, r4891, grade, note).
  grade H = read from the period key with both blind passes agreeing and, for letters, the sheet's two tables agreeing;
  M = the period key itself carries two values (table vs uncypher), or one witness only where the other is hidden.
  The word list (codes ~105-538, f.102v body and f.103r left column) is NOT transcribed here (gap).
--check: exit 1 unless the regenerated table equals the committed key_period_meadowe_f102.tsv byte for byte.
"""
import csv, io, os, sys
H = os.path.dirname(os.path.abspath(__file__))
P = os.path.join(H, 'passes')
SRC = 'BL Add MS 4166 f.102v-103r (DECODE R4890)'

def tsv(name):
    return list(csv.DictReader(open(os.path.join(P, name), encoding='utf-8'), delimiter='\t'))

def norm_name(s):
    return s.replace('^', '').replace(' ', '').replace('y^e', 'ye').lower().rstrip('.:')

def letters(pass_):
    out = {}
    for r in tsv(f'{pass_}_p2_letters.tsv'):
        if r['code'].isdigit() and r['letter'] != '?':
            out.setdefault(int(r['code']), []).append(r['letter'])
    for r in tsv(f'{pass_}_p3_head.tsv'):
        if r['section'] != 'nulls' and r['code'].isdigit():
            out.setdefault(int(r['code']), []).append(r['column'])
    return out

def build():
    LA, LB = letters('A'), letters('B')
    UA = {int(r['code']): r['value'] for r in tsv('A_p3_uncypher.tsv')}
    UB = {int(r['code']): r['value'] for r in tsv('B_p3_uncypher.tsv')}
    NA = sorted(int(r['code']) for r in tsv('A_p3_head.tsv') if r['section'] == 'nulls')
    NB = sorted(int(r['code']) for r in tsv('B_p3_head.tsv') if r['section'] == 'nulls')
    r91 = {}
    for r in tsv('eye_r4891.tsv'):
        for c in r['codes_r4891_p2'].split():
            r91.setdefault(int(c), []).append(r['letter'])
    conf = {int(r['code']): r for r in tsv('eye_conflicts.tsv')}
    rows = []
    lv = lambda L: L.lower().replace('j', 'i')
    for c in range(1, 105):
        la, lb, ua, ub = LA.get(c), LB.get(c), UA.get(c), UB.get(c)
        passes = 'agree' if (la == lb and ua == ub) else 'differ'
        if c in NA or ua == 'nul':
            w2 = 'agree' if (c in NA and ua == 'nul') else 'one table only'
            rows.append([c, 'nul', 'null', 'Nulls' if c in NA else '', passes, w2, '', 'H' if w2 == 'agree' and passes == 'agree' else 'M',
                         'Nulls table and To-uncypher "nul"' if w2 == 'agree' else 'To-uncypher only'])
            continue
        r4 = r91.get(c)
        if la is None:  # letter-table column hidden in the binding (Y)
            rows.append([c, ua, 'letter', ua.upper(), passes, 'uncypher only', '', 'M',
                         'letter-table column Y at the binding on f.102v (only a digit 8 visible in two rows); value from To-uncypher'])
            continue
        tl = sorted(set(lv(x) for x in la))
        r4s = '' if r4 is None else ('agree' if sorted(set(lv(x) for x in r4)) == tl else 'differ: ' + ','.join(r4))
        if c in conf or tl != [ua]:
            vals = '|'.join(tl + ([ua] if ua not in tl else []))
            note = 'table ' + ','.join(la) + ' vs To-uncypher ' + ua + '; ' + (conf[c]['note'] if c in conf else 'not eye-checked')
            rows.append([c, vals, 'letter', ','.join(la), passes, 'differ', r4s, 'M', note])
        else:
            rows.append([c, ua, 'letter', ','.join(la), passes, 'agree', r4s, 'H' if passes == 'agree' else 'M', 'letter table and To-uncypher agree'])
    for c in sorted(set(NA) | set(NB)):
        if c > 104 and not any(r[0] == c for r in rows):
            n = NA.count(c)
            rows.append([c, 'nul', 'null', 'Nulls', 'agree' if NA.count(c) == NB.count(c) else 'differ', 'Nulls table only', '', 'M',
                         'above the To-uncypher range; the word list (not transcribed) may also use this number' + ('; written twice in the Nulls table' if n > 1 else '')])
    NmA = {int(r['code']): r for r in tsv('A_p3_names.tsv')}
    NmB = {int(r['code']): r for r in tsv('B_p3_names.tsv')}
    for c in sorted(set(NmA) | set(NmB)):
        a, b = NmA.get(c), NmB.get(c)
        same = a and b and norm_name(a['name']) == norm_name(b['name'])
        notes = '; '.join(x for x in ((a or {}).get('note', ''), (b or {}).get('note', '')) if x)
        grade = 'H' if same and (a['conf'] == 'H' and b['conf'] == 'H') else 'M'
        rows.append([c, (a or b)['name'], 'name', (a or b)['name'], 'agree' if same else 'differ', '', '', grade,
                     notes + ('; pass B filled codes as a running sequence' if c == 539 else '')])
    rows.sort(key=lambda r: r[0])
    buf = io.StringIO()
    w = csv.writer(buf, delimiter='\t', lineterminator='\n')
    w.writerow(['code', 'value', 'class', 'sheet_label', 'passes', 'sheet_witness2', 'r4891', 'grade', 'note'])
    for r in rows:
        w.writerow(r)
    w.writerow([f'# source: {SRC}; read by THUR-MEAD 10 Oct 2026 (two blind Sonnet passes + worker eye on conflicts); words ~105-538 not transcribed'] + [''] * 8)
    return buf.getvalue()

def main():
    out = build()
    dst = os.path.join(H, 'key_period_meadowe_f102.tsv')
    if '--check' in sys.argv:
        ok = os.path.exists(dst) and open(dst, encoding='utf-8').read() == out
        print('meadowe_sheet --check:', 'OK' if ok else 'STALE')
        sys.exit(0 if ok else 1)
    open(dst, 'w', encoding='utf-8').write(out)
    rows = [l.split('\t') for l in out.splitlines()[1:] if not l.startswith('#')]
    from collections import Counter
    print('rows', len(rows), dict(Counter((r[2], r[7]) for r in rows)))

if __name__ == '__main__':
    main()
