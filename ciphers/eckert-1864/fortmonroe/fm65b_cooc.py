#!/usr/bin/env python3
"""FM65-B (10 Oct 2026): loose co-occurrence search (all words within 700 chars, case-insensitive, whitespace collapsed) over the cached
print-check djvu texts (sources/ia-fulltext/print-check) for each FM65-B row. A hit list is for the reader to eyeball; a miss is a search result."""
import gzip, glob, os, re
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
Q = {'F1 5856/0': ['Hancox', 'Winants'], 'F1b': ['Winants', 'Porter'], 'F3 5857/1': ['Binney', 'mustered', 'December'], 'F3b': ['Brice', 'second expedition'],
     'F4 5858/0': ['no transportation', 'river steamer', 'Beckwith'], 'F5 5858/1': ['Sedgwick', 'Victor', 'Illinois', 'Baltic'],
     'F6 5860/1': ['Beckwith', 'overcoat'], 'F6b': ['Phillips', 'theatre', 'Butler'], 'F8 5861/1': ['Baltic', 'countermand'],
     'F9 5861/2': ['Stanton', 'Savannah', 'safely'], 'F9b': ['Beckwith', 'Butler', 'left Monroe'], 'F10 5864/1': ['Elias Smith', 'Tribune', 'expedition'],
     'F11 5866/0': ['Baltic', 'Annapolis', 'coal', 'Sampson'], 'F12 5866/2': ['Ariel', 'Sedgwick', 'Victor', 'Illinois', 'Baltic'], 'F12b': ['Ariel', 'Sedgwick', 'Baltic', 'ordered to Baltimore']}
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
