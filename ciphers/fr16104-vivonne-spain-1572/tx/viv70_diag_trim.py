#!/usr/bin/env python3
"""VIV-70 POST-HOC diagnostic, NOT a gate (PREREG-VIV70's registered verdict is FAIL, rank 2 of 201): the same control with
the target string trimmed to the opening of dec70, length fixed by ink 67's own ratio (1,403 aligned letters for 1,270 signs)
plus 200. Names the next registered run; nothing is built or registered from it.

    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv70_diag_trim.py [--check]   (writes tx/vivk70_diag_trim.json)
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'benchmark-tx'))
import build_vivonne_f211r as b  # noqa: E402

pub, force, grade, let, stream = b.load()
seq = [t[0] for t in stream]
k = int(len(seq) * 1403 / 1270) + 200
r = {'post_hoc': True, 'trim_letters': k, 'control_published': b.control(seq, let[:k], pub)}
out = json.dumps(r, indent=1) + '\n'
P = os.path.join(HERE, 'vivk70_diag_trim.json')
if '--check' in sys.argv:
    ok = open(P).read() == out; print('ok' if ok else 'stale'); sys.exit(0 if ok else 1)
open(P, 'w').write(out); print(out)
