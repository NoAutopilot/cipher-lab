#!/usr/bin/env python3
"""N6-VIV63 post-hoc diagnostic (NOT pre-registered, no gate): can a WRONG key pass b2? For 50 shuffled keys, decode ink 63
(ff.190r-191v) and test that decode against its own 200-draw letter-order-shuffle null exactly as b2 does. If wrong keys pass b2
often, b2 measures transcription structure, not the key. Seed 20260967-diag. Prints counts; writes tx/viv63_diag_wrongkey.json.
"""
import json, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import viv63_test as t, viv63_decode as v63, viv54_decode as vd, judge_plaintext as jp  # noqa: E402

k = {c: v for c, (v, g) in vd.key().items()}
m = jp.NgramModel([jp.read_corpus(p) for p in t.FR16])
seq = [c for _, _, s in v63.lines() for c, _ in s]
codes = sorted(k); rng = random.Random('20260967-diag'); rows = []
for _ in range(50):
    v = [k[c] for c in codes]; rng.shuffle(v); km = dict(zip(codes, v))
    r, _ = t.run(m, km, seq, 200, 'diag')
    rows.append({'s': r['s'], 'b2_p99': r['b2']['null_p99'], 'pass': r['b2']['pass'], 'margin': round(r['s'] - r['b2']['null_p99'], 4)})
n = sum(x['pass'] for x in rows); ms = sorted(x['margin'] for x in rows)
out = {'wrong_keys': 50, 'b2_passes': n, 'margin_median': ms[25], 'margin_max': ms[-1]}
json.dump({'summary': out, 'rows': rows}, open(os.path.join(HERE, 'viv63_diag_wrongkey.json'), 'w'), indent=1)
print(out)
