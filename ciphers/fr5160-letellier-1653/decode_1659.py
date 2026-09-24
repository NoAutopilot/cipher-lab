#!/usr/bin/env python3
"""Apply key_1659.tsv to a reconciled numeral-cipher transcription and write the graded reading (rules 4 and 7).

  python3 decode_1659.py                write reading_f86.tsv/.txt (and reading_f88.* when ciphertext_f88.tsv exists)
  python3 decode_1659.py --check        exit 1 if a committed reading differs from a regeneration

Per-token grade: C when the key value is attested (key grade C) and the group was read with conf H; M when the
group's transcription conf is M or the key row is marked conflict; U when the group is not in the key.
Clear-French words ([word], M.) are carried through as P (plain in the manuscript) and are not counted as decoded.
"""
import csv, os, sys

KEY = 'key_1659.tsv'
TARGETS = [('ciphertext_f86.tsv', 'reading_f86'), ('ciphertext_f88.tsv', 'reading_f88')]


def load_key():
    return {r['code']: r for r in csv.DictReader(open(KEY), delimiter='\t')}


def decode(ct, key):
    rows = []
    for r in csv.DictReader(open(ct), delimiter='\t'):
        g = r['group']
        if g.startswith('[') or g in ('M.', 'M.r', 'M.e'):
            rows.append((r['line'], r['pos'], g, g.strip('[]'), 'P'))
            continue
        k = key.get(g)
        if not k:
            rows.append((r['line'], r['pos'], g, '?', 'U'))
            continue
        grade = 'C'
        if r.get('conf', 'H') != 'H' or k['note'] == 'conflict':
            grade = 'M'
        v = '' if k['value'] == '0' else k['value']
        rows.append((r['line'], r['pos'], g, v, grade))
    return rows


def render(rows):
    tsv = 'line\tpos\tgroup\tvalue\tgrade\n' + ''.join('\t'.join(x) + '\n' for x in rows)
    lines, cur, last = [], [], None
    for ln, pos, g, v, gr in rows:
        if ln != last and cur:
            lines.append(f'{last}  ' + ' '.join(cur)); cur = []
        last = ln
        cur.append(f'[{v}]' if gr == 'P' else (v.upper() if gr == 'U' else v))
    if cur:
        lines.append(f'{last}  ' + ' '.join(cur))
    counts = {}
    for x in rows:
        counts[x[4]] = counts.get(x[4], 0) + 1
    head = '# grades: ' + ' '.join(f'{k}={counts[k]}' for k in sorted(counts)) + '  (P = clear in the manuscript; ? = unkeyed)\n'
    return tsv, head + '\n'.join(lines) + '\n'


def main():
    key = load_key()
    stale = False
    for ct, out in TARGETS:
        if not os.path.exists(ct):
            continue
        tsv, txt = render(decode(ct, key))
        for path, body in ((out + '.tsv', tsv), (out + '.txt', txt)):
            if '--check' in sys.argv:
                if not os.path.exists(path) or open(path).read() != body:
                    print('STALE', path); stale = True
            else:
                open(path, 'w').write(body)
        print(out, txt.split('\n')[0])
    sys.exit(1 if stale else 0)


if __name__ == '__main__':
    main()
