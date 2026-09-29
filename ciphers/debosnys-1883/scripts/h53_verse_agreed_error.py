#!/usr/bin/env python3
"""H53 (29 Sept 2026): H51 on the verse. Bourdeau's verse read (verse_transcription.lines(), 20 lines) against our
settled c4 draft (ciphertext_c34_draft.tsv, verse line 1 = c4a0), punctuation-class boxes dropped; the h29/h51
held-out alignment (concordance fitted on odd or even lines, non-split boxes only, applied to the other half); codes
with >= 3 (>= 2) training co-occurrences; disagreement rate of his mapped id with our settled id by settlement class.
Writes h53_verse_agreed_error.json."""
import os, sys, json, csv, collections, contextlib, io
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here); root = os.path.dirname(here)
repo = os.path.dirname(os.path.dirname(root))
with contextlib.redirect_stdout(io.StringIO()):
    import h29_bourdeau_n9 as h
sys.path.insert(0, os.path.join(repo, 'sources/bourdeau/cyphersolver-targets-debosnys')); import verse_transcription as v
rows = list(csv.DictReader(open(os.path.join(root, 'ciphertext_c34_draft.tsv')), delimiter='\t'))
by = collections.OrderedDict()
for r in rows:
    if r['line'].startswith('c4'): by.setdefault(r['line'], []).append(r)
keys = sorted(by, key=lambda k: (0 if k.startswith('c4a0') else 1 if k.startswith('c4a') else 2, k))
h.O = [[r for r in by[k] if r['sign'].rstrip('?') not in h.PUNCT] for k in keys]; h.B = [list(l) for l in v.lines()]
assert len(h.O) == len(h.B) == 20
res = {}
for min_co in (3, 2):
    tot = collections.Counter(); dis = collections.Counter()
    for fold in (0, 1):
        train = [i for i in range(20) if i % 2 == fold]; test = [i for i in range(20) if i % 2 != fold]
        c = h.fit(train); co = collections.Counter()
        for i in train:
            for x, y in h.nw(h.O[i], h.B[i], lambda x, y: 2 if c.get(y) == h.sig(x) else 0):
                if x and y and not h.split(x): co[(y, h.sig(x))] += 1
        rel = {y for y, s in c.items() if co[(y, s)] >= min_co}
        for i in test:
            for x, y in h.nw(h.O[i], h.B[i], lambda x, y: 2 if c.get(y) == h.sig(x) else 0):
                if not (x and y) or y not in rel: continue
                cls = x['why'] if x['why'] in ('agree-AB', 'settled-majority', 'three-way') else 'other'
                tot[cls] += 1; dis[cls] += c[y] != h.sig(x)
    res[f'min{min_co}_any'] = {k: dict(n=tot[k], disagree=dis[k], rate=round(dis[k] / tot[k], 3)) for k in tot}
    print(min_co, res[f'min{min_co}_any'])
json.dump(res, open(os.path.join(root, 'h53_verse_agreed_error.json'), 'w'), indent=1)
