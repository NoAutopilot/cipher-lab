#!/usr/bin/env python3
"""WIT-GROEN (PREREG-txeng2-19 addendum, 01:2x UTC 10 Oct 2026): Groen van Prinsterer IV pp.90*-91* (IA archivesoucorre03housgoog),
the closing passage of the 8 June 1573 dispatch printed from another manuscript copy, as the clerk-independent test of the f.103r
END anchor (registered f.103r stretch = dec_norm 6655-9554; dec_norm is the folder's clerk reading). Method as wit_anchor.py:
passage pulled by script from the on-disk OCR, normalised (letters only, v->u, j->i, y->i, k->c), split into its p.90* part
(clean OCR) and its p.91* part (damaged OCR; reported separately), each part's best window over dec_norm by SequenceMatcher ratio
(step 10, refined at step 1); selection-fair null = letter-shuffled copies each taking their own best window (200 clean / 50 damaged).
Gate (declared): SUPPORTED if the clean part's best window ends within 150 letters of dec_norm's end AND ratio - null max >= 0.03.
Reads no truth file, no output file. Run from the repo root: python3 -I benchmark-tx/txeng2/witanchor/wit_groen.py
"""
import difflib, gzip, json, random, re, unicodedata, os
HERE = os.path.dirname(os.path.abspath(__file__))
def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if c.isascii() and c.isalpha())
    return s.translate(str.maketrans('vjyk', 'uiic'))
ocr = gzip.open('sources/ia-fulltext/print-check/archivesoucorre03housgoog_djvu.txt.gz', 'rt', encoding='utf-8', errors='replace').read()
m1 = re.search(r"L.Empereur\s+fait\s+asseur", ocr); assert m1
m2 = re.search(r"rem[ée]dier\s+ses\s+af\S*aires", ocr[m1.start():]); assert m2
raw = ocr[m1.start():m1.start() + m2.end()]
# the page break "— 9r —" (p.91* running head in the OCR) splits the clean p.90* part from the damaged p.91* part
parts = re.split(r"\n\s*[—-]\s*9\S*\s*[—-]\s*\n", raw)
if len(parts) != 2:
    parts = [raw[:raw.find('Siegcn')], raw[raw.find('Siegcn'):]]
segs = [norm(x) for x in parts]
dec = norm(open('ciphers/fr16104-vivonne-spain-1572/tx/dec_norm.txt', encoding='utf-8').read())
def best(seq, step=10):
    L = len(seq); bestr, besto = -1.0, None
    for o in range(0, max(1, len(dec) - L + 1), step):
        r = difflib.SequenceMatcher(None, seq, dec[o:o + L], autojunk=False).ratio()
        if r > bestr: bestr, besto = r, o
    for o in range(max(0, besto - step), min(len(dec) - L, besto + step) + 1):
        r = difflib.SequenceMatcher(None, seq, dec[o:o + L], autojunk=False).ratio()
        if r > bestr: bestr, besto = r, o
    return bestr, besto
res = {'dec_len': len(dec), 'registered_f103r_span': [6655, 9554], 'segments': []}
rng = random.Random(20261010)
for k, (label, s) in enumerate(zip(['p90_clean', 'p91_damaged'], segs)):
    r, o = best(s)
    null = []
    for _ in range(200 if k == 0 else 50):
        sh = list(s); rng.shuffle(sh); null.append(best(''.join(sh), step=20)[0])
    null.sort()
    g = {'part': label, 'letters': len(s), 'ratio': round(r, 4), 'offset': o, 'end': o + len(s), 'end_gap_to_dec_end': len(dec) - (o + len(s)),
         'null_max': round(null[-1], 4), 'null_p95': round(null[int(0.95 * len(null)) - 1], 4), 'margin_vs_max': round(r - null[-1], 4),
         'null_n': len(null), 'head': s[:30]}
    res['segments'].append(g); print(g)
c = res['segments'][0]
res['verdict'] = 'SUPPORTED' if (c['end_gap_to_dec_end'] <= 150 and c['margin_vs_max'] >= 0.03) else 'NOT SUPPORTED'
print('Verdict (clean part):', res['verdict'])
json.dump(res, open(os.path.join(HERE, 'result_groen.json'), 'w'), indent=1)
