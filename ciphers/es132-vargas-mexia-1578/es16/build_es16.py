#!/usr/bin/env python3
"""build_es16.py -- 1560s-1580s Spanish chancery-letter corpus from Teulet, Relations politiques ... vol.5 (1862),
IA relationspolitiq05teul _djvu.txt (RUN1-ES132, 4 Oct 2026; V6-PTCORP pattern).

Keeps OCR paragraphs whose Spanish function-word count beats the French one by a margin; drops the two known-answer
texts (Philip II to Vargas, 19 Sept 1578 and 15 Oct 1578: everything between the '1578. -- 19 Septembre. -- Madrid.'
heading and the '1578. -- 27 Octobre' heading) so the judge never trains on the answer. Splits the kept text into
5 chronological folds (equal letter counts) for the leave-one-file-out check (rule 3 es17c/EN-FOLDS lesson).
Usage: build_es16.py TEULET5_DJVU.txt OUTDIR
"""
import re, sys, gzip
from pathlib import Path
src, out = Path(sys.argv[1]), Path(sys.argv[2])
L = src.read_text(encoding='utf-8', errors='replace').split('\n')
# cut the known-answer window
a = next(i for i, l in enumerate(L) if re.search(r'1578\.\s+.\s+19\s+Septembre\.\s+.\s*Madrid', l))
b = next(i for i, l in enumerate(L) if i > a and re.search(r'1578\.\s+.\s+27\s+Octobre', l))
L = L[:a] + L[b:]
paras, cur = [], []
for l in L:
    if not l.strip():
        if cur: paras.append(' '.join(cur)); cur = []
    else: cur.append(l.strip())
if cur: paras.append(' '.join(cur))
ES = set('que y los las con por se lo del mas para su sus como esto esta este porque quanto aunque ha hazer dezir muy ya'.split())
FR = set('le les et du des il est qui pour au ce une sont aux avec dans par ont été cette'.split())
keep = []
for p in paras:
    w = re.findall(r'[a-záéíóúñç]+', p.lower())
    if len(w) < 12: continue
    e = sum(x in ES for x in w); f = sum(x in FR for x in w)
    if e >= 4 and e >= 3 * max(1, f): keep.append(p)
text = '\n'.join(keep)
n = len(text); k = 5
out.mkdir(parents=True, exist_ok=True)
cuts = [0] + [text.find('\n', n * i // k) for i in range(1, k)] + [n]
for i in range(k):
    with gzip.open(out / f'teulet5_es_fold{i+1}.txt.gz', 'wt', encoding='utf-8') as fh:
        fh.write(text[cuts[i]:cuts[i + 1]])
print(f'kept {len(keep)} of {len(paras)} paragraphs, {n} chars, excluded lines {a}-{b} (known answers)')
