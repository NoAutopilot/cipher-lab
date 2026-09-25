#!/usr/bin/env python3
"""Offline test for ciphers/fr2933-salviati-1525/control/codemark_curve.py CM_ERR (LANE R7 CM3, 25 Sept 2026): the
measured error mix deletes, inserts and confuses signs at the asked rates (within 3 sigma), keeps the truth index aligned
with the surviving tokens, and only names confusable partners in a code swap. Also: the --help text prints and the
CM_ERR row suffix is set. Runs build() only (no anneal), about 2 s."""
import os, subprocess, sys, importlib.util, math
from collections import Counter
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
P = os.path.join(R, 'ciphers', 'fr2933-salviati-1525', 'control', 'codemark_curve.py')
h = subprocess.run([sys.executable, P, '--help'], capture_output=True, text=True, check=True).stdout
assert 'CM_ERR' in h and 'CM_MIX' in h and 'CM_BACKOFF' in h, h[:200]
os.environ['CM_ERR'] = '0.05'; os.environ['CM_MIX'] = '0.5:0.3:0.2'
sys.argv = ['codemark_curve.py', 'stats', '--leaves', 'all']
spec = importlib.util.spec_from_file_location('cmc', P); cm = importlib.util.module_from_spec(spec); spec.loader.exec_module(cm)
assert cm.RSUF.endswith('_err0.05'), cm.RSUF
seq, toks, info = cm.build('cm', 2820, 1)
n = 2820
for k, share in (('del', 0.5), ('ins', 0.3)):
    p = 0.05 * share; mu, sd = n * p, math.sqrt(n * p * (1 - p))
    assert abs(info[k] - mu) <= 3 * sd, (k, info[k], mu, sd)
assert 0 < info['code'] <= 0.05 * 0.2 * n + 3 * math.sqrt(n * 0.01), info
tix = cm.TRUTH_INDEX
assert len(tix) == len(seq) == n - info['del'] + info['ins'], (len(tix), len(seq), info)
kept = [j for j in tix if j is not None]
assert kept == sorted(kept) and len(kept) == n - info['del'] and tix.count(None) == info['ins']
# a clean build with the same seed gives the truth stream; every surviving non-confused sign matches it, every confused
# one differs only in the base code and names a listed partner
os.environ['CM_ERR'] = '0'; cm.ERR = 0.0
clean, toks2, _ = cm.build('cm', 2820, 1)
assert toks2 == toks
partners = set(cm.CONFUSE) | {(b, a) for a, b in cm.CONFUSE}
diff = 0
for i, j in enumerate(tix):
    if j is None:
        continue
    if seq[i] != clean[j]:
        diff += 1
        (c1, m1), (c2, m2) = clean[j].split('^', 1), seq[i].split('^', 1)
        assert m1 == m2 and c1 != c2, (clean[j], seq[i])
        if c1 in {a for p in cm.CONFUSE for a in p}:
            assert (c1, c2) in partners, (c1, c2)
assert diff == info['code'], (diff, info)
print('ok measured noise', info)
