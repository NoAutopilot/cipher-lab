#!/usr/bin/env python3
"""FM65-D (10 Oct 2026): loose co-occurrence search (all words within 700 chars, case-insensitive, whitespace collapsed) over the cached
print-check djvu texts (sources/ia-fulltext/print-check) for each FM65-D row. A hit list is for the reader to eyeball; a miss is a search result."""
import gzip, glob, os, re
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
Q = {'F1 5879/0': ['Vanderbilt', 'magazine', 'Fisher', 'garrison'], 'F1b': ['Tribune', 'correspondent', 'Fisher is ours'], 'F2 5883/0': ['Mulford', 'Varina', 'Blair'], 'F2b': ['Blair', 'passed through', 'Ord', 'Varina'],
     'F4 5885/1': ['torpedo', 'Lynch', 'Parker', 'Lawrence'], 'F5 5886/0': ['torpedo', 'Lynch', 'Wise', 'Parker'], 'F6 5887/0': ['Nevada', 'Rucker', 'recruits'], 'F6b': ['torpedoes', 'Stromboli', 'Wise'],
     'F7 5887/1': ['Saugus', 'Grant', 'needs'], 'F7b': ['Saugus', 'Monroe', 'Washington', 'Fox'], 'F8 5888/1': ['Ord', 'absent', 'several days'], 'F8b': ['Ord', 'take charge', 'headquarters'],
     'F9 5888/2': ['Palmer', 'Newbern', '6,000'], 'F9b': ['Palmer', 'Newbern', 'prepare accordingly'], 'F10 5889/2': ['Schofield', 'battery', 'division', 'Willard'], 'F10b': ['Schofield', 'Boyd', 'Willard', 'mules'],
     'F11 5890/2': ['Portsmouth', 'detached', 'executive officer'], 'F13 5895/2': ['Bates', 'President', 'Annapolis', 'Point Lookout'], 'F13b': ['Eckert', 'Bates', 'Annapolis', 'boat'],
     'F14 5896/2': ['Stager', 'Schofield', 'operator', 'construction'], 'F15 5897/0': ['Blodget', 'Schofield', 'Sherman', 'Annapolis'], 'F15b': ['Anderson', 'Schofield', 'despatches', 'Annapolis'],
     'F16 5861/2b': ['Beckwith', 'Butler', 'left Monroe'], 'F16b': ['Butler', 'enquired', 'Beckwith', 'Sheldon']}
texts = {}
for p in sorted(glob.glob(os.path.join(D, '*_djvu.txt.gz'))):
    texts[os.path.basename(p)[:-12]] = re.sub(r'\s+', ' ', gzip.open(p, 'rt', errors='ignore').read()).lower()
print('volumes', len(texts))
for tag, words in Q.items():
    ws = [w.lower() for w in words]; hits = []
    for v, t in texts.items():
        for m in re.finditer(re.escape(ws[0]), t):
            a = m.start(); seg = t[max(0, a - 700): a + 700]
            if all(w in seg for w in ws[1:]): hits.append((v, a)); break
    print(tag, '|', ', '.join(f'{v}@{a}' for v, a in hits) or 'none')
