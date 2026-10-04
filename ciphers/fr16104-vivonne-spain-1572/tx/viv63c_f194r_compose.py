#!/usr/bin/env python3
"""N6-VIV63C: compose tx/f194r_pass{A,B}.tsv from two crop sets of fr.16105 f.194r (NOTES "N6-VIV63C").

    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv63c_f194r_compose.py

The first cut (iiif_lines --follow-slope, crops c199_f194r_LNN) is usable for page lines 1-4 only (row-by-row pass A/B similarity
0.76-0.93 on the same row; from row L05 the bands straddle two written lines and the readers took different ones -- A L08~B L09 0.83,
A L09~B L10 0.91, A L10~B L11 0.94 -- so rows L05-L10 are dropped, page lines 5-10 unread here, a Remaining gap). Further, from band L11 on, the slope fit
snapped bands onto neighbouring lines (both readers marked L12, L16, L19 DUP; page lines 14 and 16 had no band; checked by eye on a crop
stack). Page lines 11-20 were re-cut from the same native region deskewed by -1.4 deg (crops c199_f194r_low_LNN, 3 segments, flat bands;
images/p63/manifest_f194r_low.json) and read by two further blind passes. So: rows L01-L04 from tx/f194r_top_pass{A,B}.tsv, rows L11-L20 =
tx/f194r_low_pass{A,B}.tsv L01-L10 renumbered. Pass A joins pass A, B joins B (each line still read by two independent blind readers).
A '[...]' nested inside a '[PLAIN:...]' (low pass A L10, the plain close) is rewritten '(...)' so tx/viv63_clean.py removes the whole
plain stretch; no sign is changed.
N7-VIV63G (4 Oct 2026, PREREG-N7VIV63G.md): page lines 5-10 re-cut flat from the same region deskewed -1.4 deg (rows 840-1530; crops
c199_f194r_mid_LNN, 3 segments; images/p63/manifest_f194r_mid.json) and read by two more blind Sonnet passes, tx/f194r_mid_pass{A,B}.tsv
L01-L06, inserted here as rows L05-L10 (A joins A, B joins B). Rows L01-L04 and L11-L20 unchanged.
"""
import re
import os
HERE = os.path.dirname(os.path.abspath(__file__))
for p in 'AB':
    rows = []
    for ln in open(os.path.join(HERE, f'f194r_top_pass{p}.tsv'), encoding='utf-8'):
        r = ln.rstrip('\n').split('\t', 1)
        if r[0].startswith('L') and int(r[0][1:]) <= 4:
            rows.append(f'{r[0]}\t{r[1] if len(r) > 1 else ""}')
    for ln in open(os.path.join(HERE, f'f194r_mid_pass{p}.tsv'), encoding='utf-8'):
        r = ln.rstrip('\n').split('\t', 1)
        if r[0].startswith('L'):
            rows.append(f'L{int(r[0][1:]) + 4:02d}\t{r[1] if len(r) > 1 else ""}')
    for ln in open(os.path.join(HERE, f'f194r_low_pass{p}.tsv'), encoding='utf-8'):
        r = ln.rstrip('\n').split('\t', 1)
        if r[0].startswith('L'):
            body = r[1] if len(r) > 1 else ''
            if '[PLAIN:' in body:
                k = body.index('[PLAIN:') + 7; body = body[:k] + body[k:].replace('[...]', '(...)')
            rows.append(f'L{int(r[0][1:]) + 10:02d}\t{body}')
    with open(os.path.join(HERE, f'f194r_pass{p}.tsv'), 'w', encoding='utf-8') as f:
        f.write('row\tcodes\n' + '\n'.join(rows) + '\n')
    print(p, len(rows), 'rows')
