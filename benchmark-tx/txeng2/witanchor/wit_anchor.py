#!/usr/bin/env python3
"""WIT-ANCHOR (PREREG-txeng2-19): Gachard II p.428's verbatim passage as a read-free anchor check of dec_norm.
Reads: the on-disk OCR (sources/ia-fulltext/print-check/labibliothquen02gachuoft_djvu.txt.gz) and the folder's clerk reading
ciphers/fr16104-vivonne-spain-1572/tx/dec_norm.txt. Reads no truth file, no output file. Run from the repo root:
  python3 -I benchmark-tx/txeng2/witanchor/wit_anchor.py
"""
import difflib, gzip, json, random, re, unicodedata, os
HERE = os.path.dirname(os.path.abspath(__file__))
def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if c.isascii() and c.isalpha())
    return s.translate(str.maketrans('vjyk', 'uiic'))
ocr = gzip.open('sources/ia-fulltext/print-check/labibliothquen02gachuoft_djvu.txt.gz', 'rt', encoding='utf-8', errors='replace').read()
# the passage: from "Quant a la paix que l'on dit" to "appaisees par la force" (vivwit RESULTS, p.428); the OCR carries
# double spaces and line breaks, so the bounds are found by whitespace-tolerant search around the normalised hit
import sys
m1 = re.search(r"ilz\s+s.en\s*\n?\s*deffendent\s+bien", ocr); assert m1, 'anchor 1 not found'
start = ocr.rfind('Quant', 0, m1.start()); assert start > 0
m2 = re.compile(r"appais\S{0,3}\s+par\s+la\s+force").search(ocr, start); assert m2, 'anchor 2 not found'
raw = ocr[start:m2.end()]
segs = [norm(x) for x in re.split(r'\.\s*\.\s*\.\s*\.', raw)]
segs = [s for s in segs if len(s) >= 40]
dec = norm(open('ciphers/fr16104-vivonne-spain-1572/tx/dec_norm.txt', encoding='utf-8').read())
def best(seq, step=10):
    L = len(seq); bestr, besto = -1.0, None
    for o in range(0, max(1, len(dec) - L + 1), step):
        r = difflib.SequenceMatcher(None, seq, dec[o:o + L], autojunk=False).ratio()
        if r > bestr: bestr, besto = r, o
    # refine at step 1 around the best
    for o in range(max(0, besto - step), min(len(dec) - L, besto + step) + 1):
        r = difflib.SequenceMatcher(None, seq, dec[o:o + L], autojunk=False).ratio()
        if r > bestr: bestr, besto = r, o
    return bestr, besto
res = {'passage_letters': sum(len(s) for s in segs), 'segments': []}
rng = random.Random(20261010)
for k, s in enumerate(segs):
    r, o = best(s)
    null = []
    for _ in range(200 if k == 0 else 50):
        sh = list(s); rng.shuffle(sh); null.append(best(''.join(sh), step=20)[0])
    null.sort()
    res['segments'].append({'k': k, 'letters': len(s), 'ratio': round(r, 4), 'offset': o, 'end': o + len(s),
                            'null_max': round(null[-1], 4), 'null_p95': round(null[int(0.95 * len(null)) - 1], 4),
                            'margin_vs_max': round(r - null[-1], 4), 'null_n': len(null), 'head': s[:30]})
json.dump(res, open(os.path.join(HERE, 'result.json'), 'w'), indent=1)
for g in res['segments']:
    print(g)
