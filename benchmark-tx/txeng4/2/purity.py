#!/usr/bin/env python3
"""TXE4-2 step 2f (read-free): the purity gate on the round-1/round-2 joins and the tile table tiles/TILES.tsv.
(i) among the boxes placed at agreed (keep.tsv) positions in round 2, the share with op 1:1 >= 0.80;
(ii) tiles kept = 1:1 at the SAME position in round 1 and round 2 (op '1:1', never 'unsure'); >= 15 of the 27 f.128 labels
    must have >= 2 kept tiles; (iii) the shift check (join_check --steered) PASSed -- read from the sidecar.
    python3 purity.py [TILE_DIR]   (default tiles/)"""
import csv, json, os, collections
import sys
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.join(HERE, sys.argv[1] if len(sys.argv) > 1 else 'tiles')
rd = lambda fn: list(csv.DictReader((l for l in open(fn if os.path.isabs(fn) else os.path.join(HERE, fn)) if not l.startswith('# ')), delimiter='\t'))  # '# ' comments; the '#' label row is data
keep = {(r['line'], r['pos']) for r in rd(os.path.join(T, 'keep.tsv'))}
labels27 = [r['code'] for r in rd('row_text.tsv')]
r1 = {(r['sid'], r['line'], r['pos']) for r in rd(os.path.join(T, 'r1_map.tsv')) if r['op'] == '1:1' and r['sid']}
r2 = rd(os.path.join(T, 'r2_map.tsv'))
at_keep = [r for r in r2 if r['sid'] and (r['line'], r['pos']) in keep]
ops = collections.Counter(r['op'] for r in at_keep)
share = ops['1:1'] / max(1, len(at_keep))
sign_at = {(r['line'], r['pos']): r['sign'] for r in rd(os.path.join(T, 'read.tsv'))}
tiles = [dict(sid=r['sid'], code=sign_at[(r['line'], r['pos'])], line=r['line'], pos=r['pos'])
         for r in at_keep if r['op'] == '1:1' and (r['sid'], r['line'], r['pos']) in r1]
per = collections.Counter(t['code'] for t in tiles)
have2 = [c for c in labels27 if per[c] >= 2]
jc = json.load(open(os.path.join(T, 'r2_map.tsv.joincheck.json')))
print(f"(i) boxes at agreed positions in round 2: {len(at_keep)}, ops {dict(ops)}, share 1:1 = {share:.3f} ({'PASS' if share >= 0.80 else 'FAIL'} at 0.80)")
print(f"(ii) tiles 1:1 at the same position in both rounds: {len(tiles)}; per label " +
      ', '.join(f'{c} {per[c]}' for c in labels27 if per[c]) + f"; labels with >= 2 tiles: {len(have2)} of 27 ({'PASS' if len(have2) >= 15 else 'FAIL'} at 15)" +
      (f"; non-inventory labels among tiles: {dict((c, n) for c, n in per.items() if c not in labels27)}" if any(c not in labels27 for c in per) else ''))
print(f"(iii) shift check sidecar: {jc.get('verdict')} (steered {jc.get('steered')}, share0 {jc.get('share0')}, p95_0 {jc.get('p95_0')}, share+-1 {jc.get('sharepm1')}, bound {jc.get('b2_bound')})")
with open(os.path.join(T, 'TILES.tsv'), 'w') as f:
    f.write('sid\tcode\tline\tpos\n' + ''.join(f"{t['sid']}\t{t['code']}\t{t['line']}\t{t['pos']}\n" for t in tiles))
ok = share >= 0.80 and len(have2) >= 15 and jc.get('verdict') == 'PASS'
print('PURITY GATE:', 'PASS' if ok else 'FAIL', '-> tiles/TILES.tsv', len(tiles), 'rows')
