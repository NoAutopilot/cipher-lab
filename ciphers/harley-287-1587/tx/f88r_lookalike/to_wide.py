#!/usr/bin/env python3
"""R11A-HAR, 6 Oct 2026: turn gloss/pass{A,B}_f88r.tsv (band, pair, ..., cipher) into reconcile_passes.py 'wide'
files, one row per band, runs joined in order, '/' (word break) and '?' (unread) dropped so only labelled signs align."""
import sys
from collections import defaultdict
from pathlib import Path
here = Path(__file__).resolve().parent
root = here.parents[1]
for p in 'AB':
    bands = defaultdict(list)
    for ln in (root / f'gloss/pass{p}_f88r.tsv').read_text().splitlines()[1:]:
        f = ln.split('\t')
        if len(f) < 4:
            continue
        bands[f[0]] += [t for t in f[3].split() if t not in ('/', '?', '-')]
    out = ''.join(f'{b}\t{" ".join(v)}\n' for b, v in sorted(bands.items()) if v)
    (here / f'pass{p}_wide.tsv').write_text('row\tcodes\n' + out)
