"""Score the R16 blind context fills on mssDE 68 (control_r16_fills.tsv) against 68's own ink decipherment.
Mask: every 68 figure not glossed in 37/55 hidden (88 of 177 tokens). Figures whose 68 value the filler had already
seen (NOTES 'R6 progress' list, or shown in reading_108A.txt lines p1 L01-p2 L04 before the control) are 'leaked' and
not scored.  python3 control_r16.py [--check]  -> control_r16.tsv"""
import csv, collections, io, os, re, sys
D = os.path.dirname(os.path.abspath(__file__)); P = lambda f: os.path.join(D, f)
pairs = list(csv.DictReader(open(P('pairs_contemporary.tsv')), delimiter='\t'))
t = collections.defaultdict(collections.Counter)
for r in pairs:
    if r['item'] == 'mssDE68': t[r['group']][r['gloss']] += 1
leak = set(open(P('control_r16_leak.txt')).read().split())
n = lambda x: re.sub(r"[?'\s]", '', x)
rows = [['figure', 'fill', 'confidence', 'truth_68', 'leaked', 'strict', 'same_word']]
variants = {('ai', 'ait'), ('roi', 'roy')}  # spelling variants of the same word
for f in csv.DictReader(open(P('control_r16_fills.tsv')), delimiter='\t'):
    tr = [n(x) for x in t[f['figure']]]
    strict = n(f['fill']) in tr
    same = strict or any((n(f['fill']), x) in variants for x in tr)
    rows.append([f['figure'], f['fill'], f['confidence'], '/'.join(t[f['figure']]), 'yes' if f['figure'] in leak else '',
                 'right' if strict else 'wrong', 'right' if same else 'wrong'])
s = io.StringIO(); csv.writer(s, delimiter='\t', lineterminator='\n').writerows(rows)
sc = [r for r in rows[1:] if not r[4]]
for c in ('firm', 'weak'):
    x = [r for r in sc if r[2] == c]
    print(c, 'scored', len(x), 'strict', sum(r[5] == 'right' for r in x), 'same-word', sum(r[6] == 'right' for r in x))
if '--check' in sys.argv:
    ok = open(P('control_r16.tsv')).read() == s.getvalue(); print('ok' if ok else 'stale'); sys.exit(0 if ok else 1)
open(P('control_r16.tsv'), 'w').write(s.getvalue())
