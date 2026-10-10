#!/usr/bin/env python3
"""FV-L17a (10 Oct 2026; copied from fv_l16a_print.py): letters-only phrase grep of E581 E582 E583 E585 E586 E587 decoded phrases over every cached print-check djvu
text (sources/ia-fulltext/print-check: OR I/46 pts 1-3, I/42 pt 3, I/47 pt 2, ORN I/11-12, Butler Corr. IV-V and the rest), then KWIC for
vessel and person names in the Dec 1864-Jan 1865 volumes. A miss is a search result, not a novelty verdict (rule 10). Usage: fv_l17a_print.py"""
import gzip, os, re, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'E581 5862/0': ['River Queen left', 'left about eleven', 'with General Butler on board', 'had gone up the James', 'gone up James',
                 'was going the same way', 'himself was going'],
 'E582 5862/2': ['either will be good', 'either would be good', 'or Ord either', 'to relieve General Foster', 'to relieve Foster',
                 'good men to relieve', 'Mrs Foster'],
 'E583 5872/0': ['Illinois goes to sea', 'goes to sea at eleven', 'goes to sea at 11', 'twelve hundred and eighty seven', 'Illinois sailed'],
 'E585 5872/2': ['has but forty rounds', 'but 40 rounds', 'forty rounds of ammunition', 'shall I take more', 'Second Division Nineteenth Corps'],
 'E586 5874/1': ['forty rounds of ammunition will answer', 'rounds of ammunition will answer', 'need not wait to get more', "needn't wait", 'will answer you need not'],
 'E587 5883/2': ['wait at Fort Monroe until I get there', 'wait at Fortress Monroe until', 'until I get there', 'leave Annapolis at five', 'leave Annapolis at 5',
                 'I will leave Annapolis'],
}
texts = {os.path.basename(p)[:-12]: gzip.open(p, 'rt', errors='ignore').read() for p in sorted(glob.glob(os.path.join(D, '*_djvu.txt.gz')))}
N = {k: norm(v) for k, v in texts.items()}
print('volumes searched:', len(texts))
for e, phs in PH.items():
    for ph in phs:
        hits = [f'{v}[{t.count(norm(ph))}]' for v, t in N.items() if norm(ph) in t]
        print(e, '|', ph, '|', ','.join(hits) or 'none')
Y65 = ['warofrebellion423unit', 'warofrebellion461unit', 'warofrebellion014602rootrich', 'warofrebellion462unit', 'warofrebellion431unit',
       'officialrecordso0011unse', 'officialrecords10librgoog', 'privateofficialc05butl']
print('Y65 present:', [v for v in Y65 if v in texts])
for name, rx in [('River Queen', r'Butler|January|Jan'), ('Grover', r'ammunition|rounds|Savannah|Illinois|Monroe'), ('Illinois', r'steamer|Grover|sea|transport'),
                 ('Palmer', r'Monroe|Annapolis|Grant|wait'), ('Annapolis', r'Grant|Palmer|January 2|5 a'), ('relieve Foster', ''), ('relieve General Foster', ''),
                 ('Foster', r'leg|wound|relieve|Ord'), ('Mulford', r'Varina|Blair'), ('gone up the James', '')]:
    for v in Y65:
        if v not in texts: continue
        t = texts[v]
        for m in list(re.finditer(re.escape(name), t))[:15]:
            ctx = ' '.join(t[max(0, m.start()-240):m.start()+280].split())
            if rx and not re.search(rx, ctx): continue
            print('KWIC', name, v, m.start(), '::', ctx)

