#!/usr/bin/env python3
"""BAL167-GSEQ tile-test scorer (PREREG-BAL-GPLUS.md (b) gates, as applied by PREREG-BAL-GSEQ.md); written by GSEQ-SCORER
(13 Oct 2026) for the rule-7 gap AUDIT 6 named. Regenerates score1.out from the blind read and the tile key.
Usage (this folder): python3 score_gplus.py [READ.tsv KEY.tsv OUT] [--check]
Defaults: tileread1.tsv r20261013/key_private.tsv score1.out. Without --check prints the score; with --check exits 1 if OUT differs."""
import csv, sys
args = [a for a in sys.argv[1:] if a != '--check']
read, keyf, outf = (args + ['tileread1.tsv', 'r20261013/key_private.tsv', 'score1.out'][len(args):])[:3]
rd = {r['tile']: r for r in csv.DictReader(open(read), delimiter='\t')}
arms = {}
for k in csv.DictReader(open(keyf), delimiter='\t'):
    r = rd[k['id']]
    arms.setdefault(k['role'].split(':')[0], []).append((k['id'], k['where'], r['same'], r['confidence']))
rate = lambda a: sum(x[2] == 'yes' for x in arms[a]) / len(arms[a])
g1 = rate('P+') >= 0.75
g2 = rate('P-') <= 0.25 and rate('P-') <= rate('P+') - 0.50
out = ''.join(f'{a} {sorted(arms[a])}\n' for a in ('P+', 'P-', 'T'))
out += (f"P+ yes-rate {rate('P+'):.3f} G1 (>=0.75) {'PASS' if g1 else 'FAIL'}; "
        f"P- yes-rate {rate('P-'):.3f} G2 (<=0.25 and <=P+-0.50) {'PASS' if g2 else 'FAIL'}\n")
out += f"T confirmed {sum(x[2] == 'yes' for x in arms['T'])}/{len(arms['T'])}\n"
if '--check' in sys.argv:
    ok = open(outf).read() == out
    print(f'{outf}: {"up to date" if ok else "STALE"}')
    sys.exit(0 if ok else 1)
sys.stdout.write(out)
