#!/usr/bin/env python3
"""H51 (29 Sept 2026): error hidden inside agreement, bounded with Bourdeau's independent No.9 read (cryptogram 2).
Reuses h29_bourdeau_n9.py's alignment (held out: concordance fitted on one half of the lines, non-split boxes only,
scored on the other half). Restricted to his RELIABLE codes: mapping one-to-one (or any, looser variants) onto one of our ids with >= 5 (3, 2)
training co-occurrences. On the test half, for each class of our boxes (agree-AB, settled-majority, family/base-
settled, three-way), the share where his reliable code's mapped id differs from our settled id. The agree-AB rate is
an upper bound on our readers' hidden error there (it also contains his errors and residual mapping error); the
three-way rate is the reference for boxes we already know are uncertain. Writes h51_agreed_error.json."""
import os, sys, json, collections
here = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, here); root = os.path.dirname(here)
import contextlib, io
with contextlib.redirect_stdout(io.StringIO()):
    import h29_bourdeau_n9 as h
def run(min_co, one2one):
  out = {}; tot = collections.Counter(); dis = collections.Counter()
  for fold in (0, 1):
      train = [i for i in range(25) if i % 2 == fold]; test = [i for i in range(25) if i % 2 != fold]
      c = h.fit(train)
      co = collections.Counter()
      for i in train:
          for x, y in h.nw(h.O[i], h.B[i], lambda x, y: 2 if c.get(y) == h.sig(x) else 0):
              if x and y and not h.split(x): co[(y, h.sig(x))] += 1
      inv = collections.Counter(c.values())
      reliable = {y for y, s in c.items() if (inv[s] == 1 or not one2one) and co[(y, s)] >= min_co}
      for i in test:
          for x, y in h.nw(h.O[i], h.B[i], lambda x, y: 2 if c.get(y) == h.sig(x) else 0):
              if not (x and y) or y not in reliable: continue
              cls = x['why'] if x['why'] in ('agree-AB', 'settled-majority', 'three-way') else 'family/base/seg'
              tot[cls] += 1; dis[cls] += c[y] != h.sig(x)
      out[f'fold{fold}_reliable_codes'] = len(reliable)
  for k in tot: out[k] = dict(n=tot[k], disagree=dis[k], rate=round(dis[k] / tot[k], 3))
  return out
res = {f'min{m}_{"one2one" if o else "any"}': run(m, o) for m, o in ((5, True), (3, True), (3, False), (2, False))}
for k, v in res.items(): print(k, v)
json.dump(res, open(os.path.join(root, 'h51_agreed_error.json'), 'w'), indent=1)
