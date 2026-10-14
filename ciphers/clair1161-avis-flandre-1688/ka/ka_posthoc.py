#!/usr/bin/env python3
"""CL1161-KA POST-HOC (not in PREREG-CL1161-KA, no gate): per sign, the Lasry-paragraph chunk each c186R token aligns to
under V2 (same alignment as ka_score.py). Usage (from ciphers/clair1161-avis-flandre-1688):
python3 ka/ka_posthoc.py > ka/ka_posthoc.tsv."""
import sys, collections, importlib.util, io, contextlib
from pathlib import Path
sys.argv = ['x', '--draws', '1']
spec = importlib.util.spec_from_file_location('ka', Path(__file__).with_name('ka_score.py')); m = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(m)
vals = [m.k2.get(s, '') or '' for s in m.tk2]; ch, _ = m.align(vals)
d = collections.defaultdict(collections.Counter)
for s, v, c in zip(m.tk2, vals, ch): d[(s, m.F(v) or '-')][c or '(none)'] += 1
print('# POST-HOC (not in PREREG-CL1161-KA, no gate): c186R V2 token -> aligned Lasry chunk, per sign')
print('sign\tv2_value\tn\tagree\tchunks')
for (s, v), c in sorted(d.items(), key=lambda x: -sum(x[1].values())):
    n = sum(c.values()); print(f"{s}\t{v}\t{n}\t{c.get(v, 0)}\t{','.join(f'{k}:{x}' for k, x in c.most_common())}")
