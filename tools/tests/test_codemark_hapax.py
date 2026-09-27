#!/usr/bin/env python3
"""Offline test for ciphers/fr2933-salviati-1525/control/codemark_curve.py CM_HAPAX=exclude (SALV-HAPAX, 27 Sept 2026).
(1) On the committed corrected split, hapax_types() finds exactly the 8 unread `?` hapax types (read from the rows,
not hard-coded) and none of the 114 real count-1 code+mark types. (2) On a 200-token toy stream with 5 injected unread
hapaxes, split_wild() excludes exactly 5 positions, run() anneals the other 195 and fills the 5 back, returning a
200-letter decode whose non-wild letters equal the key applied to the spliced stream. Exits non-zero on any mismatch.
About 20 s (corpus model build plus a 2-restart, 3,000-iteration anneal)."""
import os, sys, importlib.util, random
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(R, 'ciphers', 'fr2933-salviati-1525', 'control', 'codemark_curve.py')
os.environ.update(CM_HAPAX='exclude', CM_RESTARTS='2', CM_ITERS='3000')
os.environ.pop('CM_ERR', None)
sys.argv = ['codemark_curve.py', 'stats', '--leaves', 'all']
spec = importlib.util.spec_from_file_location('cmh', P); cm = importlib.util.module_from_spec(spec); spec.loader.exec_module(cm)
assert cm.RSUF.endswith('_hxexclude'), cm.RSUF
hx = cm.hapax_types()
assert len(hx) == 8 and all(t.startswith('?') for t in hx), sorted(hx)
# toy: 200 tokens over 20 ordinary symbols plus 5 unread hapaxes at fixed positions
rng = random.Random(3)
toy = [f"s{rng.randrange(20)}^" for _ in range(200)]
inject = [7, 50, 51, 120, 199]
toyhx = {f"?toy.{i}^" for i in inject}
for i in inject:
    toy[i] = f"?toy.{i}^"
wild, sub = cm.split_wild(toy, toyhx)
assert wild == inject and len(sub) == 195, (wild, len(sub))
cm.HX = toyhx
sc, key, dec, model, free, w2 = cm.run(toy, 1)
assert w2 == inject and len(dec) == 200, (w2, len(dec))
assert all(dec[i] in cm.ha.ALPHA for i in inject), [dec[i] for i in inject]
assert "".join(dec[i] for i in range(200) if i not in set(inject)) == "".join(key[s] for s in sub)
print('ok hapax exclude: 8 target hapax types', sorted(hx), '| toy excluded', len(wild), 'of 200')
