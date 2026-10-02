#!/usr/bin/env python3
"""List the WRONG signs of a sequence (score_known.py rule) and whether the look-alike packet flagged each tile.
  python3 wrong_list.py SEQ.tsv --span f179r --tiles f179r_tiles.tsv"""
import argparse, csv, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from score_known import score
ap = argparse.ArgumentParser(); ap.add_argument('seq'); ap.add_argument('--span', required=True); ap.add_argument('--tiles', required=True)
a = ap.parse_args()
fl = {(t['passage'], t['pos']): t['why'] for t in csv.DictReader(open(a.tiles), delimiter='\t')}
rows, st = score(a.seq, a.span)
w = [(r, fl.get((r['passage'], r['pos']), '-')) for r, s in zip(rows, st) if s == 'WRONG']
for r, f in w:
    print(f"{r['passage']}.{r['pos']}\t{r['sign_id']}\tflagged={f}")
print(f'wrong {len(w)}, flagged {sum(f != "-" for _, f in w)}')
