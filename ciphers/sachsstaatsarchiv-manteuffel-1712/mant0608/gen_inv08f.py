#!/usr/bin/env python3
"""MANT-CEN3 (9 Oct 2026): writes inv08f.tsv from sheet_key_f.tsv, sheet_blind_f.tsv (blind sheet reads, saved before the key was opened),
fetch_log_f.tsv and the worker's eye reads (hand-entered below). Run from the target folder: python3 mant0608/gen_inv08f.py"""
import csv, hashlib
log={l.split('\t')[0]:l.rstrip('\n').split('\t') for l in open('mant0608/fetch_log_f.tsv') if '\t' in l}
key=list(csv.DictReader(open('mant0608/sheet_key_f.tsv'),delimiter='\t'))
read=dict(l.split() for l in open('mant0608/sheet_blind_f.tsv') if l.strip())
eye={
'0290':('y','n','medium','30-45','stamp 224, 17 Sept 1712: code run in lines 1-3 of the right page and short groups lower; superscript marks at top, no clear gloss words'),
'0317':('y','partly','medium','30-45','stamp 246, 17 Sept 1712: runs in numbered paragraphs 1-3 with small words above groups'),
'0314':('y','partly','heavy','60-80','stamp 244, Extrait de la resolution (15 Sept 1712): code groups in nearly every line, small words above many groups'),
'0312':('y','partly','heavy','60-80','stamp 242, Extrait de la relation: groups (66.60.21.12.120 etc.) throughout, words above many groups; left leaf: clear marginal note'),
'0309':('y','partly','medium','40-60','stamp 240, 16 Sept 1712: runs in the right-page lines, small words above some groups'),
'0337':('y','n','light','3-6','stamp 264: one short run on the right page (about 17.35.58), clear text otherwise'),
'0334':('y','n','light','10-20','stamp 261, 28 Sept 1712: runs low on the right page; left leaf marginal notes clear'),
'0327':('y','n','light','8-14','stamp 255: two short runs (177.120.35 and 15.16.27.49), unglossed, inline'),
'0389':('y','n','light','4-8','stamp 311, 10 Oct 1712: single codes inline (46, 45, 150), no run'),
'0383':('y','n','medium','25-40','stamp 307: runs low on the right page (7 60.66.55.35 etc.); long marginal text on the left margin is words, not glosses'),
'0373':('y','n','light','8-15','stamp 298: one run (about 41.21.21.5.77) lower left page plus 177.120; unglossed'),
}
cleared={'0278':'clear text (stamp 215)','0270':'clear text, Pro memoria (stamp 208), numbered paragraphs, no code groups seen','0302':'clear text (stamp 234, Charlottenbourg 14 Sept)',
'0339':'clear text (stamp 266)','0364':'clear text (stamp 289)','0359':'clear text (stamp 284)','0354':'clear text (stamp 280)','0362':'clear text (stamp 287)','0388':'clear text (stamp 310)'}
out=['# MANT-CEN3 (9 Oct 2026, LANE FAMILY-A2j account 2): Loc. 694/08 unseen frames 0268-0399 (first 50 of the 89 still uncovered from 0268 on, in frame order) + planted controls. www.archiv.sachsen.de frames.tsv full-size URLs, 51 requests (50 targets + clear control 0125), 2.3 s apart, all HTTP 200 image/jpeg; images in scratch only (re-fetch from images/loc694-08-09/frames.tsv); code controls 0510/0511/0579/0580 read from disk. 5 sheets of 12 tiles (10 targets + code control + clear control 0125), sheets_d.py seed 6086, blind reads saved in sheet_blind_f.tsv before the key sheet_key_f.tsv was opened. sheet_read = blind read at 600 px; every frame read code or possible was eye-checked at ~1100 px (code column = that result; crops census/eye_f1-5.jpg); a sheet "none" is NOT eye-checked (weak evidence: light single codes can be missed). Grade M throughout: eye readings, no transcription.',
'loc\tframe\tkind\tsheet_label\tsheet_read\tcode\tglossed\tdensity_eye\test_tokens\tnote\thttp\tsha256_16']
for r in key:
    fr,lab,kind=r['frame'],r['label'],r['kind']; h=log.get(fr) or [fr,'disk',hashlib.sha256(open('images/loc694-08-09/694-08_%s.jpg'%fr,'rb').read()).hexdigest()[:16]]; sr=read.get(lab,'none')
    if kind=='control+': row=('y','-','','','planted control (control+), sheet read '+sr)
    elif kind=='control-': row=('n','-','-','','planted control (control-), sheet read '+sr)
    elif fr in eye: row=eye[fr]
    elif fr in cleared: row=('n','-','-','','sheet possible; cleared at ~1100 px: '+cleared[fr])
    else: row=('n','-','-','','sheet none, not eye-checked')
    http='200 image/jpeg' if h[1].startswith('200') else 'disk'
    out.append('\t'.join(['694/08',fr,kind,lab,sr,row[0],row[1],row[2],row[3],row[4],http,h[2]]))
open('mant0608/inv08f.tsv','w').write('\n'.join(out)+'\n')
