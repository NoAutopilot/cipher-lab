#!/usr/bin/env python3
"""R7A-HEL53 (6 Oct 2026): align a blind image read of R1953 (passA_*.tsv: line<TAB>space-separated groups, '_'/'='
underline marks, '?' doubtful digit, '#' illegible) to DECODE's transcription (doc_tokens.tsv, from doc_tokens.py),
page by page, with a global edit-distance alignment on whole groups. Writes compare.tsv: pos, image, DECODE group,
image-read group, status (same / doubt (same digits, read marked '?') / differ / doc_only / read_only), current grade in key_r4369/reading_R1953_tokens.tsv.
Usage: python3 compare.py doc_tokens.tsv passA_P2.tsv passA_P3P1.tsv > compare.tsv"""
import re, sys, os, csv
HERE = os.path.dirname(os.path.abspath(__file__))
norm = lambda s: re.sub(r'[^0-9]', '', s)
doc = [r for r in csv.DictReader(open(sys.argv[1]), delimiter='\t')]
grades = {int(r['pos']) if False else i: r['grade'] for i, r in enumerate(csv.DictReader(
    open(os.path.join(HERE, '..', 'key_r4369', 'reading_R1953_tokens.tsv')), delimiter='\t'))}
pagemap = {'P2': '13447', 'P3': '13448', 'P1': '13446'}
read = {v: [] for v in pagemap.values()}
for f in sys.argv[2:]:
    for r in csv.DictReader(open(f), delimiter='\t'):
        pg = pagemap[r['line'][:2]]
        for g in r['tokens'].split():
            read[pg].append((r['line'], g))
def align(a, b):
    n, m = len(a), len(b)
    D = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1): D[i][0] = i
    for j in range(m + 1): D[0][j] = j
    def sub(x, y):
        x, y = norm(x), norm(y)
        if x == y: return 0
        # one-digit slips cost less than a wholly different group
        if len(x) == len(y) and sum(p != q for p, q in zip(x, y)) == 1: return 0.6
        return 1.2
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i][j] = min(D[i-1][j] + 1, D[i][j-1] + 1, D[i-1][j-1] + sub(a[i-1], b[j-1]))
    i, j, out = n, m, []
    while i > 0 or j > 0:
        if i > 0 and j > 0 and abs(D[i][j] - (D[i-1][j-1] + sub(a[i-1], b[j-1]))) < 1e-9:
            out.append((i-1, j-1)); i -= 1; j -= 1
        elif i > 0 and abs(D[i][j] - (D[i-1][j] + 1)) < 1e-9:
            out.append((i-1, None)); i -= 1
        else:
            out.append((None, j-1)); j -= 1
    return out[::-1]
print('pos\timage\tdoc_line\tdoc\tread_line\tread\tstatus\tgrade')
for pg in ['13447', '13448', '13446']:
    d = [r for r in doc if r['image'] == pg]
    rd = read[pg]
    for i, j in align([r['doc_raw'] for r in d], [g for _, g in rd]):
        if i is None:
            print(f'\t{pg}\t\t\t{rd[j][0]}\t{rd[j][1]}\tread_only\t'); continue
        r = d[i]; pos = int(r['pos'])
        if j is None:
            print(f"{pos}\t{pg}\t{r['line']}\t{r['doc_raw']}\t\t\tdoc_only\t{grades[pos]}"); continue
        st = 'same' if norm(r['doc_raw']) == norm(rd[j][1]) else 'differ'
        if st == 'same' and ('?' in rd[j][1] or '#' in rd[j][1]): st = 'doubt'
        print(f"{pos}\t{pg}\t{r['line']}\t{r['doc_raw']}\t{rd[j][0]}\t{rd[j][1]}\t{st}\t{grades[pos]}")
