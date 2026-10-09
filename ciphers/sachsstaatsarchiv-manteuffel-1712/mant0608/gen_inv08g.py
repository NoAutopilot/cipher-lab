#!/usr/bin/env python3
"""MANT-CEN4 (9 Oct 2026): writes inv08g.tsv from sheet_key_g.tsv, sheet_blind_g.tsv (blind sheet reads, saved before the key was opened),
fetch_log_g.tsv and the worker's eye reads (hand-entered below). Run from the target folder: python3 mant0608/gen_inv08g.py"""
import csv
log={l.split('\t')[0]:l.rstrip('\n').split('\t') for l in open('mant0608/fetch_log_g.tsv') if '\t' in l}
key=list(csv.DictReader(open('mant0608/sheet_key_g.tsv'),delimiter='\t'))
read=dict(l.split() for l in open('mant0608/sheet_blind_g.tsv') if l.strip())
eye={
'0503':('y','y','heavy','100-130','page no. 403: left page code lines throughout (e.g. 253.322.114.90.75...) with small words above many groups; right page German clear text; re-photograph of the leaf N9-MANT saw as 0502/0503 (NOTES line 1146) -- check there before any work'),
'0490':('y','partly','heavy','200-260','page no. 392: both pages code runs in nearly every paragraph, words above many groups, "beschaedigt" tag; stride-5 inventory (NOTES line 1631) listed 0490 as CLEAR -- that read was wrong'),
'0496':('y','partly','light','12-20','page no. 397, Manteuffel 20 Nov 1712 at the camp: one run (23.26.16.17.33.29.2.60.6.19.10.28.26.10.53) in the 9th-10th lines of the right page with words written above and below; rest clear; left page blank'),
'0483':('y','n','light','12-20','page no. 386, 11 Nov 1712: runs in numbered para 3 (about 6.21.2.28.6.35.5.10) and last line (103.34.26), words above only as insertions; left page blank'),
'0453':('y','n','medium','20-30','page no. 360: runs in numbered para 3 (60.35.21.33.14.15.10.26) and para 1 (15.60.33.51.29.35) plus inline 170, 257, 150; unglossed; NOTES lines 2163-2206 list 0452/0453 as unseen and the 0454 letter as beginning before 0454'),
'0414':('y','partly','light','6-9','page no. 329, Berlin 19 Oct 1712: one short run (10.8.35.21.39.27.257, a gloss "provenir le Roy de Prusse" written above) at the foot of the right page; rest clear'),
}
cleared={'0432':'clear text (page no. 341)','0443':'clear text (page no. 350)','0429':'clear text (page no. 338; small interlinear insertions are words, not glosses of code)'}
out=['# MANT-CEN4 (9 Oct 2026, LANE FAMILY-A2j account 2): Loc. 694/08 last uncovered frames 0402-0503 (39 frames; 0177 was recomputed uncovered but is MANT-0177\'s leaf and left out) + planted controls. www.archiv.sachsen.de frames.tsv full-size URLs, 40 requests (39 targets + clear control 0125), 2.3 s apart, all HTTP 200 image/jpeg; images in scratch only (re-fetch from images/loc694-08-09/frames.tsv); code controls 0510/0511/0579/0580 read from disk. 4 sheets (10,10,10,9 targets + a code control + clear control 0125 each), sheets_d.py seed 6087, blind reads saved in sheet_blind_g.tsv before the key sheet_key_g.tsv was opened. sheet_read = blind read at 600 px; every frame read code or possible was eye-checked at ~1900 px (code column = that result; crops census/eye_g_<frame>.jpg); a sheet "none" is NOT eye-checked (weak evidence: light single codes can be missed). Grade M throughout: eye readings, no transcription.',
'loc\tframe\tkind\tsheet_label\tsheet_read\tcode\tglossed\tdensity_eye\test_tokens\tnote\thttp\tsha256_16']
for r in key:
    fr,lab,kind=r['frame'],r['label'],r['kind']; h=log.get(fr) or [fr,'disk','']; sr=read.get(lab,'none')
    if kind=='control+': row=('y','-','','','planted control (control+), sheet read '+sr)
    elif kind=='control-': row=('n','-','-','','planted control (control-), sheet read '+sr)
    elif fr in eye: row=eye[fr]
    elif fr in cleared: row=('n','-','-','','sheet possible; cleared at ~1900 px: '+cleared[fr])
    else: row=('n','-','-','','sheet none, not eye-checked')
    http='200 image/jpeg' if h[1].startswith('200') else 'disk'
    out.append('\t'.join(['694/08',fr,kind,lab,sr,row[0],row[1],row[2],row[3],row[4],http,h[2]]))
open('mant0608/inv08g.tsv','w').write('\n'.join(out)+'\n')
