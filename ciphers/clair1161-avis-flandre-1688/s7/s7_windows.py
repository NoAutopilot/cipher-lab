#!/usr/bin/env python3
"""CL1161-S7 (15 Oct 2026): sample S, single-7 and plant (q+qb) tokens, cut windows, write montages + key files.
Uses tools/lookalike_pass.py helpers on la/crops/manifest.json (c186R lines -> c186Rblk crops, as D2-C1161LA).
  python3 s7/s7_windows.py      (run from the target folder; seed 1161, PREREG-CL1161-S7.md)"""
import csv, collections, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(T, '..', '..', 'tools'))
import lookalike_pass as LP
rows = list(csv.DictReader(open(os.path.join(T, 'ciphertext.tsv')), delimiter='\t'))
seq = collections.defaultdict(list)
for r in rows:
    seq[r['line']].append(r['sign'])
def toks(pred):
    out = []
    for ln, s in seq.items():
        for i, x in enumerate(s):
            if pred(s, i):
                out.append((ln, i + 1, x))
    return out
single7 = lambda s, i: s[i] == '7' and not (i > 0 and s[i-1] == '7') and not (i + 1 < len(s) and s[i+1] == '7')
def draw(pool, n, rng):
    rng.shuffle(pool); per, got = collections.Counter(), []
    for t in pool:
        if per[t[0]] < 2:
            got.append(t); per[t[0]] += 1
        if len(got) == n:
            break
    return got
rng = random.Random(1161)
sets = {'S': draw(toks(lambda s, i: s[i] == 'S'), 12, rng),
        '7': draw(toks(single7), 12, rng),
        'plant': draw(toks(lambda s, i: s[i] == 'q'), 6, rng) + draw(toks(lambda s, i: s[i] == 'qb'), 6, rng)}
build = LP._line_strips(os.path.join(T, 'la', 'crops', 'manifest.json'), '', '{line}_s*')
strips = {}
os.makedirs(os.path.join(HERE, 'win'), exist_ok=True)
with open(os.path.join(HERE, 'windows_key.tsv'), 'w') as kf:
    kf.write('set\twid\tline\tpos\tlabel\n')
    for name, ts in sets.items():
        rng.shuffle(ts); wins = []
        for k, (ln, pos, lab) in enumerate(ts, 1):
            if ln not in strips:
                S = build(ln); strips[ln] = (S,) + LP._ink_extent(S, 110, 2)
            S, a, b = strips[ln]
            wins.append((f'W{k:02d}', LP._window(S, a, b, len(seq[ln]), pos, 2.5, 2)))
            kf.write(f'{name}\tW{k:02d}\t{ln}\t{pos}\t{lab}\n')
        print(name, LP._montages(wins, os.path.join(HERE, 'win'), f'{name}_', 6))
