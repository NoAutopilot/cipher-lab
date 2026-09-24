#!/usr/bin/env python3
"""Extract letter 5549's cipher groups from Groen, Archives, Supplement (1847), Lettre 45, pp.140-146.

Reads gpas_lettre45.txt (tools/html2text.py of the DBNL page groe009arch09_01_0048.php, fetched 24 Sept 2026)
and writes groen_5549.tsv: one row per token in print order, with the Groen page, a run id (a maximal stretch
of numerals and short clear fragments), the token, its kind (num / clear-fragment) and 40 characters of clear
context either side of the run. Groen's print is a transcription, not the image: check it against images/05549_p*.jpg.
Usage: python3 extract_5549.py [--check]   (--check exits 1 if groen_5549.tsv is stale)
"""
import re, sys, os
here = os.path.dirname(os.path.abspath(__file__))
t = open(os.path.join(here, 'gpas_lettre45.txt'), encoding='utf-8').read()
s = t.index('Die verendertte'); e = t.index('PS. Nachdem')
body = t[s:e]
page = 140
parts = re.split(r'\[p\. (\d+)\*\]', body)
text = ''
marks = []
for i, p in enumerate(parts):
    if i % 2 == 1:
        marks.append((len(text), int(p))); continue
    p = re.sub(r'\[pagina[^\]]*\]|Ga naar (margenoot|voetnoot)\S*\s*\[#\d+\]', '', p)
    text += p
text = re.sub(r'\s+', ' ', text)
def page_at(pos):
    pg = 140
    for m, n in marks:
        if m <= pos: pg = n
    return pg
# a run: numerals "NNN." possibly separated by short lowercase fragments (<=4 letters) that sit inside the run
tok = re.compile(r'(?<![\w])(\d{1,3})\.?(?=\s|$)|(?<![\w])([a-zäöüß]{1,4})\.?(?=\s)')
rows = []; run = 0; last_end = -10
for m in re.finditer(r'\d{1,3}\.', text):
    pass
spans = [(m.start(), m.end(), int(m.group(1))) for m in re.finditer(r'(?<![\d\w])(\d{1,3})\.(?!\d)', text)]
# group numerals into runs: gap between consecutive numerals is at most one short fragment
runs = []
for st, en, n in spans:
    if runs and re.fullmatch(r'\s*(?:[a-zäöüß]{1,4}\.?\s*)?', text[runs[-1][-1][1]:st]):
        runs[-1].append((st, en, n))
    else:
        runs.append([(st, en, n)])
out = ['run\tpage\tpos\ttoken\tkind\tleft\tright']
for ri, r in enumerate(runs, 1):
    left = text[max(0, r[0][0]-40):r[0][0]].strip(); right = text[r[-1][1]:r[-1][1]+40].strip()
    k = 0; prev = None
    for st, en, n in r:
        if prev is not None:
            frag = text[prev:st].strip().rstrip('.')
            if frag:
                k += 1; out.append(f'{ri}\t{page_at(st)}\t{k}\t{frag}\tclear\t\t')
        k += 1; out.append(f'{ri}\t{page_at(st)}\t{k}\t{n}\tnum\t{left if k==1 else ""}\t{right if (st,en,n)==r[-1] else ""}')
        prev = en
new = '\n'.join(out) + '\n'
path = os.path.join(here, 'groen_5549.tsv')
if '--check' in sys.argv:
    sys.exit(0 if os.path.exists(path) and open(path, encoding='utf-8').read() == new else 1)
open(path, 'w', encoding='utf-8').write(new)
nums = [l for l in out[1:] if '\tnum\t' in l]
print(f'{len(runs)} runs, {len(nums)} numeral tokens, {len(out)-1-len(nums)} clear fragments inside runs')
