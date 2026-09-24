#!/usr/bin/env python3
"""Apply key_1659.tsv to a reconciled numeral-cipher transcription and write the graded reading (rules 4 and 7).

  python3 decode_1659.py                write reading_f86.tsv/.txt (and reading_f88.* when ciphertext_f88.tsv exists)
  python3 decode_1659.py --check        exit 1 if a committed reading differs from a regeneration

Per-token grade: C when the key value is attested (key grade C), the group was read with conf H, and the key value is
the f.87 text the joint alignment puts at this very position (align_f86_joint.tsv, align_f88.tsv); M when the
group's transcription conf is M or L, the key row is marked conflict, or the key value differs from the f.87 text
aligned here (AUDIT.md s.4, 24 Sept 2026: a C must be supported by the known plaintext at its own position); U when
the group is not in the key or was not read ('?').
Clear-French words ([word], M.) are carried through as P (plain in the manuscript) and are not counted as decoded.
"""
import csv, os, sys

KEY = 'key_1659.tsv'
TARGETS = [('ciphertext_f86.tsv', 'reading_f86', 'align_f86_joint.tsv'), ('ciphertext_f88.tsv', 'reading_f88', 'align_f88.tsv')]


def load_align(path):
    return {(r['line'], r['pos']): {'#': 'M.', '': '0'}.get(r['plain'], r['plain'])
            for r in csv.DictReader(open(path), delimiter='\t')}


def load_key():
    return {r['code']: r for r in csv.DictReader(open(KEY), delimiter='\t')}


def decode(ct, key, align):
    rows = []
    for r in csv.DictReader(open(ct), delimiter='\t'):
        g = r['group']
        if g.startswith('[') or g in ('M.', 'M.r', 'M.e'):
            rows.append((r['line'], r['pos'], g, g.strip('[]'), 'P', ''))
            continue
        k = key.get(g)
        if not k:
            rows.append((r['line'], r['pos'], g, '?', 'U', align.get((r['line'], r['pos']), '')))
            continue
        grade = 'C'
        a = align.get((r['line'], r['pos']))
        if r.get('conf', 'H') != 'H' or k['note'] == 'conflict' or a != k['value']:
            grade = 'M'
        v = '' if k['value'] == '0' else k['value']
        rows.append((r['line'], r['pos'], g, v, grade, '' if a is None else a))
    return rows


def render(rows):
    tsv = 'line\tpos\tgroup\tvalue\tgrade\tf87_aligned\n' + ''.join('\t'.join(x) + '\n' for x in rows)
    lines, cur, last = [], [], None
    for ln, pos, g, v, gr, _ in rows:
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
    for ct, out, al in TARGETS:
        if not os.path.exists(ct):
            continue
        tsv, txt = render(decode(ct, key, load_align(al)))
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
