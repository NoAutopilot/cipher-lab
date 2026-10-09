#!/usr/bin/env python3
"""MANT-CEN2 (9 Oct 2026): writes inv08e.tsv from sheet_key_e.tsv, the fetch log and the worker's eye reads (hand-entered below)."""
import csv, sys
log={l.split('\t')[0]:l.rstrip('\n').split('\t') for l in open(sys.argv[1]) if '\t' in l}
key=list(csv.DictReader(open('mant0608/sheet_key_e.tsv'),delimiter='\t'))
read={'D1-6':'possible','D2-1':'code','D2-9':'code','D2-5':'possible','D2-10':'possible','D1-12':'possible','D3-4':'possible','D4-9':'possible','D4-11':'possible','D5-1':'possible','D5-4':'possible','D5-8':'possible','D5-10':'possible','D1-2':'code','D5-5':'code','D3-9':'code','D2-11':'possible','D4-10':'possible'}
eye={
'0136':('y','partly','heavy','60-90','stamp ~102 left leaf: code runs in most lines of the right page, small words above some runs (interlinear)'),
'0146':('y','partly','medium','40-60','Berl. 25 juin 1712, stamp 111 (No. 48): two long runs in one paragraph, marginal words above some groups'),
'0182':('y','n','light','25-35','right-hand text with two code runs (13.25.19.29.1 ... 25.90.2.17.28.10.38.29), unglossed, inline'),
'0164':('n','-','-','','sheet possible; clear French text, no code groups at ~1100 px (stamp 125)'),
'0174':('y','partly','medium','35-50','stamp 133: code runs in the right page lines, small words above some groups, marginal note'),
'0169':('y','partly','medium','35-50','stamp 129: runs in lines of both pages, words above several groups'),
'0202':('n','-','-','','sheet possible; copy of a letter ("Copie d\'une lettre", 1712), clear, no code'),
'0212':('y','n','light','5-8','stamp 163: a few short groups (33 / 1 / 9) in two lines'),
'0222':('n','-','-','','sheet possible; clear text (stamp 172), no code groups'),
'0263':('n','-','-','','sheet possible; clear text (stamp 203), no code groups'),
'0253':('y','n','light','12-18','stamp 145: one run near the foot (7.60.44.12.33.3.11.9.21) and 51.28.257, unglossed'),
'0250':('y','partly','light','4-8','stamp 193, Mezieres 8 juillet 1712: single codes (155, 55.177) with marginal words'),
'0248':('y','n','light','6-10','stamp 192: short run in line 3 of the right page (29.2.5.1)'),
}
out=['# MANT-CEN2 (9 Oct 2026, LANE FAMILY-A2j account 2): Loc. 694/08 unseen frames 0133-0266 (first 50 of the 139 still uncovered past 0130, in frame order; 0177 skipped = read by MANT-0177) + planted controls. www.archiv.sachsen.de frames.tsv full-size URLs, 51 requests (50 targets + clear control 0125), 2.3 s apart, all HTTP 200 image/jpeg; images in scratch only (re-fetch from images/loc694-08-09/frames.tsv); code controls 0510/0511/0579/0580 read from disk. 5 sheets of 12 tiles (10 targets + code control + clear control 0125), sheets_d.py seed 6085, key sheet_key_e.tsv read after all five were classified. sheet_read = blind read at 600 px; a frame read code or possible was eye-checked at ~1100 px (code column = that result); a sheet "none" is NOT eye-checked (weak evidence: light single codes can be missed). Grade M throughout: eye readings, no transcription.',
'loc\tframe\tkind\tsheet_label\tsheet_read\tcode\tglossed\tdensity_eye\test_tokens\tnote\thttp\tsha256_16']
for r in key:
    fr,lab,kind=r['frame'],r['label'],r['kind']; h=log[fr]; sr=read.get(lab,'none')
    if kind=='control+': row=('y','-','','','planted control (control+), sheet read '+sr)
    elif kind=='control-': row=('n','-','-','','planted control (control-), sheet read '+sr)
    elif fr in eye: row=eye[fr]
    else: row=('n','-','-','','sheet none, not eye-checked')
    http='200 image/jpeg' if h[1].startswith('200') else 'disk'
    sha=h[2] if h[1].startswith('200') else h[2]
    out.append('\t'.join(['694/08',fr,kind,lab,sr,row[0],row[1],row[2],row[3],row[4],http,sha]))
open('mant0608/inv08e.tsv','w').write('\n'.join(out)+'\n')
