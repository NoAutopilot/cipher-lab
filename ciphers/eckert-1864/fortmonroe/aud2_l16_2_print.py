#!/usr/bin/env python3
"""AUD2-LEDGER16-2 (10 Oct 2026, second audit of E518 E526 E527 E546 E553 E554): KWIC over cached print-check texts the first audit
(FV-L16b) did not read for these names, or read only for one name: ORN I/12 (officialrecords10librgoog), Gordon's War Diary (all 1865
Norfolk pages, not only 'Vogdes'), O'Brien 1910, Plum II, Dana's Recollections (1898), Butler Corr. V, OR I/46 pts 1-3. A miss is a
search result, not a novelty verdict (rule 10). Usage: aud2_l16_2_print.py"""
import gzip, os, re
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
VOLS = ['officialrecords10librgoog', 'wardiaryevents00gordrich', 'telegraphinginba00obri', 'militarytelegraph02plumrich',
        'recollectionsofc00danauoft', 'privateofficialc05butl', 'warofrebellion461unit', 'warofrebellion014602rootrich', 'warofrebellion463unit']
TERMS = [r'Elias Smith', r'Tribune corre', r'Webster', r'Carney', r'Frank J\. White|Colonel White', r'Lanman', r'Parker', r'Foster',
         r'Portsmouth, N', r'Abbott', r'Vogdes', r'Sheldon', r'Emerick', r'Eastern District']
CTX = r'1865|January|February|Jan\.|Feb\.|Minnesota|Fort Monroe|Fortress Monroe|Norfolk|expedition|Butler'
for v in VOLS:
    p = os.path.join(D, v + '_djvu.txt.gz')
    if not os.path.exists(p): print('MISSING', v); continue
    t = gzip.open(p, 'rt', errors='ignore').read()
    for term in TERMS:
        ms = list(re.finditer(term, t)); shown = 0
        for m in ms:
            ctx = ' '.join(t[max(0, m.start()-200):m.start()+260].split())
            if not re.search(CTX, ctx) or shown >= 6: continue
            shown += 1; print(f'{v} | {term} | {m.start()} :: {ctx}')
        print(f'COUNT {v} | {term} | {len(ms)} total, {shown} shown')
