#!/usr/bin/env python3
"""SYL-31 (13 Oct 2026): build key_no31.tsv (BnF fr.3995 f.62r, Nevers no.31, '1590 Ch. d'Hespagne', canvas f126) from the two
blind Sonnet passes (no31_passes/passA.tsv, passB.tsv) and the reconciler's eye settlements below (made on the native region
images/fr3995/no31/src_image_v3_..._f126_1250_1700_2750_4457.jpg and its crops; regen_crops.sh rebuilds both).
Grade H = both passes agree and the image shows nothing against it; M = settled by the reconciler (a pass split, or a plain
letter / sign boundary the passes drew differently). A period key sheet: H/M grade the transcription, not any letter's reading.
  python3 build_no31.py [--check]   (--check: exit 1 if the committed TSV differs from a rebuild)
"""
import csv, os, sys
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(H, 'no31_passes')
OUT = os.path.join(H, 'key_no31.tsv')
load = lambda f: [r for r in csv.DictReader(open(os.path.join(P, f)), delimiter='\t')]
A, B = load('passA.tsv'), load('passB.tsv')
grid = lambda R: {(int(r['row']), int(r['col'])): r for r in R if r['section'] == 'grid'}
ga, gb = grid(A), grid(B)
# grid settlements: (row, col): (value, code, note)
GS = {
 (1, 1): ('ba', '10', 'b blotted/overwritten (A "ba?"), code 10 both passes'),
 (18, 5): ('ʒu', '39', 'last digit partly blotted (A "39?"); 9 by shape'),
}
for c, v in zip(range(1, 6), 'aeiou'):
    GS[(19, c)] = ('z' + v, str(703 + c), 'first digit split A 7 / B 1; eye: top bar and slanted descender as the 7 of 97 (x row) and the last 7 of 707; the sheet\'s 1s (10-14) are upright strokes -> 7')
rows = []
for k in sorted(ga):
    a, b = ga[k], gb.get(k)
    va, vb = a['plain'].lower(), (b['plain'].lower() if b else '')
    ca, cb = a['code'], (b['code'] if b else '')
    val = va
    if k[0] == 18: val = 'ʒ' + va[1:]   # the y row of no.54, written with a ʒ here (D4-SYL54); passes both wrote z
    if k in GS:
        val, code, note = GS[k]; conf = 'M'
        if k[0] == 18: val = 'ʒ' + val[1:]
    elif (va, ca) == (vb, cb):
        code, conf, note = ca, 'H', ('row letter written ʒ (no.54 y row), passes wrote z' if k[0] == 18 else '')
    else:
        code, conf, note = ca, 'M', 'unsettled split'
    rows.append(dict(code=code, value=val, kind='syllable', conf=conf, passA=f'{va}={ca}', passB=f'{vb}={cb}',
                     settled_by='both passes' if conf == 'H' else 'reconciler eye', note=note))
# letter signs: plain letter -> cipher signs (from the eye on the native region; the passes' raw cells kept in no31_passes/)
LET = [  # (plain, signs, conf, note)
 ('a', 'ʒ 4', 'H', 'a z-angled sign and 4; dots between are separators'),
 ('c', '8', 'M', 'both passes took the hooked plain c for a sign; sign is 8'),
 ('d', 'o', 'H', 'a filled o'),
 ('e', 'n f q', 'H', ''),
 ('l', 'h', 'M', 'plain l (A "k-like", B "l-like"); sign h'),
 ('m', 'v y 2', 'H', 'B also listed the plain m'),
 ('s', '[triangle] d', 'H', 'B also listed the plain s'),
 ('t', '8 r', 'M', 'plain t written as a cross (as in the grid ta row); both passes took it for a sign'),
 ('u', 'a 6', 'H', 'A also listed the plain u'),
 ('y', '∂ p q', 'M', 'third column: plain written ʒ (= the y of no.54, as in the grid row); signs a looped d, p, q'),
 ('z', 'd', 'M', 'third column: plain written Z (as in the grid z row); sign d'),
]
NONE = 'b f g h i n o p q r x'
for p, s, c, n in LET:
    rows.append(dict(code=s, value=p, kind='letter', conf=c, passA='see no31_passes', passB='see no31_passes',
                     settled_by='both passes' if c == 'H' else 'reconciler eye', note=n))
rows.append(dict(code='-', value=NONE, kind='letter-nosign', conf='M', passA='see no31_passes', passB='see no31_passes',
                 settled_by='reconciler eye', note='plain letters with no sign written beside them (i missed by both passes)'))
LEG = [  # (mark, text, conf)
 ('[c-curl]', 'apres une syllabe a', 'H'), ('+', 'apres e', 'H'), ('[delta/8-loop]', 'apres i', 'M'),
 ('[dot]', 'dessus l apres', 'H'), ('[dot]', 'apres n apres', 'H'), ('[caret]', 'dessus s apres', 'H'),
 ('[T-hook]', 'dessus r entredeux', 'H'), ('[v]', 'dessus l entredeux', 'M'), ('[colon]', 'apres r apres', 'M'),
 ('[two dots]', 'dessus double', 'M'), ('+', 'dessus m apres', 'H'), ('[o]', 'dessus h entredeux', 'M'),
 ('[dash]', 'dessous marque de nulle', 'H'), ('[double cross]', 'dessus marque de nulle', 'M'),
 ('[dash]', 'dessus marque de nombre', 'M'),
]
for i, (m, t, c) in enumerate(LEG, 1):
    rows.append(dict(code=m, value=t, kind=f'legend{i:02d}', conf=c, passA='see no31_passes', passB='see no31_passes',
                     settled_by='both passes' if c == 'H' else 'reconciler eye (marks at the band cut read on the overview)', note=''))
F = ['code', 'value', 'kind', 'conf', 'passA', 'passB', 'settled_by', 'note']
import io
buf = io.StringIO()
buf.write("# BnF fr.3995 f.62r (Nevers no.31, '1590 Ch. d'Hespagne'), Gallica btv1b525085665 canvas f126; SYL-31, 13 Oct 2026. Period key sheet: H/M grade the transcription.\n")
w = csv.DictWriter(buf, F, delimiter='\t', lineterminator='\n'); w.writeheader(); w.writerows(rows)
if '--check' in sys.argv:
    ok = os.path.exists(OUT) and open(OUT).read() == buf.getvalue()
    print('key_no31.tsv', 'up to date' if ok else 'STALE'); sys.exit(0 if ok else 1)
open(OUT, 'w').write(buf.getvalue())
from collections import Counter
print(len(rows), 'rows;', dict(Counter(r['conf'] for r in rows)), dict(Counter(r['kind'][:6] for r in rows)))
