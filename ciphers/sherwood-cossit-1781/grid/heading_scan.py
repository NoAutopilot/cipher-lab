#!/usr/bin/env python3
"""Heading-gap scan (SHERWOOD-GRID, 20 Oct 2026). Script only, no images.

Flags every column of book/entick_lines.tsv that carries a letter-section boundary (the OCR headword initials change
from letter X above to the next letter below, persisting) and reports the blank grid rows (empty OCR) directly above
the first line of the new section, where a centred heading ("H.") and the space before it sit. Crosses the flagged
columns with every pair the reading cites (reading.tsv) whose line W lies at or below the boundary in the same column.
  python3 grid/heading_scan.py [--all]     (--all: every page, not only cited pages)
Writes grid/flagged.tsv.
"""
import csv, os, re, sys
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def initial(txt):
    m = re.search(r"[A-Za-z]{3,}", txt or '')
    return m.group(0)[0].upper() if m else ''

grid = {}
for r in csv.reader(open(os.path.join(HERE, 'book', 'entick_lines.tsv'), encoding='utf-8'), delimiter='\t',
                    quoting=csv.QUOTE_NONE):
    if r[0] == 'page' or not r[0].isdigit():
        continue
    grid.setdefault((int(r[0]), int(r[1])), []).append((int(r[2]), r[5] if len(r) > 5 else ''))
cited = []
for r in csv.DictReader(open(os.path.join(HERE, 'reading.tsv'), encoding='utf-8'), delimiter='\t'):
    if r['kind'] == 'pair' and r['page']:
        cited.append(r)
pages = {int(r['page']) for r in cited}
if '--all' in sys.argv:
    pages = {p for p, _ in grid}
A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
flags = []
for (p, c), lines in sorted(grid.items()):
    if p not in pages:
        continue
    ini = [initial(t) for _, t in lines]
    # letter above = majority of first third, below = majority of last third
    def maj(xs):
        xs = [x for x in xs if x]
        return max(set(xs), key=xs.count) if xs else ''
    n = len(lines)
    top, bot = maj(ini[:max(n // 3, 3)]), maj(ini[-max(n // 3, 3):])
    if not top or not bot or top == bot:
        continue
    if A.find(bot) - A.find(top) not in (1, 2):  # I/J, U/V share a section in Entick; allow one skip
        continue
    # boundary: first line k where this and >=2 of the next 3 initials are the lower letter
    k = None
    for i in range(n):
        if ini[i] == bot and sum(x == bot for x in ini[i:i + 4]) >= 3:
            k = i
            break
    if k is None:
        continue
    blanks, j = 0, k - 1
    while j >= 0 and not ini[j]:
        blanks += 1
        j -= 1
    flags.append((p, c, top, bot, lines[k][0], blanks))
with open(os.path.join(HERE, 'grid', 'flagged.tsv'), 'w') as f:
    f.write('page\tcol\tabove\tbelow\tfirst_new_line\tno_text_rows_above\tcited_below\n')
    tot = 0
    for p, c, a, b, k, bl in flags:
        cb = [r for r in cited if int(r['page']) == p and int(r['W']) >= k - bl - 1 and
              (r['col'] == str(c) or r['col'] == '')]
        alt = [r for r in cited if int(r['page']) == p and int(r['W']) >= k - bl - 1 and r['col'] not in (str(c), '')]
        tot += len(cb)
        f.write('%d\t%d\t%s\t%s\t%d\t%d\t%s\n' % (p, c, a, b, k, bl, ' '.join(
            '%s:%s/%s' % (r['group'], r['entry'], r['grade']) for r in cb) +
            (' | other-col: ' + ' '.join('%s:%s/%s' % (r['group'], r['entry'], r['grade']) for r in alt) if alt else '')))
        print(p, c, a, '->', b, 'new-section line', k, 'no-text rows above', bl, 'cited:', len(cb), '+other-col', len(alt))
    print('columns flagged:', len(flags), '; cited cells at/below a flagged boundary in the same column:', tot)
