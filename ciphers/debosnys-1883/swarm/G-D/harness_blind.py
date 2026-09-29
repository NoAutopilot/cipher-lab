#!/usr/bin/env python3
"""Group D's frozen classifier on the harness's texts (29 Sept 2026). Reads ONLY a control's ciphertext TSV
(controls/<id>.tsv: line, position, sign), splits it into its c1_ and c2_ lines, computes dcore.features with 400
shuffles and the frozen pair score (dcore.score 'pair'), and calls LANGUAGE when the score exceeds threshold.json's
pair threshold (4.3, fixed on this group's own calibration set before any harness text was read). The same function
runs on the real c1/c2 in the harness's own reading (drops only '_' and MULTI plus the H43 clear spans, as score.py).
Usage: harness_blind.py blind   -> BLIND_VERDICT.tsv for B1..B5
       harness_blind.py real    -> the real texts, harness reading
       harness_blind.py ID ...  -> named controls (printed only)"""
import dcore, csv, os, sys, json, random, collections
SW = os.path.dirname(dcore.HERE); TH = json.load(open(os.path.join(dcore.HERE, 'threshold.json')))['pair']['t']
def load(cid):
    by = collections.OrderedDict()
    for r in csv.DictReader(open(os.path.join(SW, 'controls', cid + '.tsv')), delimiter='\t'):
        by.setdefault(r['line'], []).append(r['sign'])
    return [v for k, v in by.items() if k.startswith('c1_')], [v for k, v in by.items() if k.startswith('c2_')]
def real():
    out = []
    for cid in ('c1', 'c2'):
        raw = dcore.settled_lines(dcore.DEB, cid, drop_clear=True)
        out.append([l for l in ([s for s in v if s not in ('_', 'MULTI')] for v in raw.values()) if l])
    return out
def call(t1, t2, seed):
    f = dcore.features(t1, t2, random.Random(seed), 400); s = dcore.score(f, 'pair')
    return ('LANGUAGE' if s > TH else 'NULL'), round(s, 2), f
if __name__ == '__main__':
    arg = sys.argv[1:]
    if arg == ['blind']:
        rows = []
        for b in ('B1', 'B2', 'B3', 'B4', 'B5'):
            t1, t2 = load(b); v, s, f = call(t1, t2, 7); rows.append((b, v)); print(b, sum(map(len, t1)), sum(map(len, t2)), v, s, flush=True)
        with open(os.path.join(dcore.HERE, 'BLIND_VERDICT.tsv'), 'w') as fo:
            fo.write('id\tverdict\n'); [fo.write(f'{b}\t{v}\n') for b, v in rows]
    elif arg == ['real']:
        t1, t2 = real(); res = []
        for seed in range(5): v, s, f = call(t1, t2, 100 + seed); res.append(s); print('real c1+c2 (harness reading)', sum(map(len, t1)), sum(map(len, t2)), v, s, flush=True)
        json.dump(dict(pair_scores=res, threshold=TH), open(os.path.join(dcore.HERE, 'harness_real.json'), 'w'), indent=1)
    else:
        for cid in arg:
            t1, t2 = load(cid); v, s, f = call(t1, t2, 7); print(cid, v, s, {k: f[k] for k in ('c2_mi1', 'c2_bg2', 'c2_rep3', 'c2_dbl', 'x21', 'x12')}, flush=True)
