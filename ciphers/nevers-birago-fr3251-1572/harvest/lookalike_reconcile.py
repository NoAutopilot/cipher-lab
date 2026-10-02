#!/usr/bin/env python3
"""NEVBIR-LOOKALIKE step 2 reconciliation (2 Oct 2026): fold the look-alike re-read into the run's sequence.

Per flagged tile (lookalike/<run>_tiles.tsv) the re-read (lookalike/<run>_reread.tsv) is a third value-blind read.
Rule: a re-read at H or M that matches reader A or reader B settles the tile at 2-of-3 (the re-read label wins);
a re-read at H or M on a tile where A and B agreed and the re-read agrees too keeps it settled; anything else
(re-read L, SPLIT, or an H/M re-read that matches neither earlier reader) stays UNSETTLED -- passD keeps the passC
label (fixed before any score was computed: a third reader alone does not overturn two), and the tile goes to the
sorter's focus list. passD_alt.tsv takes every H/M re-read label instead, as a secondary sequence only.
Residual disagreement = unsettled / all signs of the run: the estimate of reader error after this pass that the
power control is re-run at (the two-reader rate before it was 0.24 on f.144r, 0.13 on f.168).
Writes lookalike/<run>_passD.tsv (passage, pos, sign_id, conf, note, question) and prints the counts.
"""
import csv, sys
from pathlib import Path
H = Path(__file__).resolve().parent
for run in sys.argv[1:] or ['f144r', 'f168']:
    pc = list(csv.DictReader(open(H / run / 'passC.tsv'), delimiter='\t'))
    tiles = list(csv.DictReader(open(H / 'lookalike' / f'{run}_tiles.tsv'), delimiter='\t'))
    rr = {(r['passage'], r['pos']): r for r in csv.DictReader(open(H / 'lookalike' / f'{run}_reread.tsv'), delimiter='\t')}
    tk = {(t['passage'], t['pos']): t for t in tiles}
    out, alt, uns, changed = [], [], 0, 0
    for c in pc:
        k = (c['passage'], c['pos']); lab, conf, note, q = c['sign_id'], c['conf'], 'passC', ''
        alt_lab = None
        if k in tk:
            t, r = tk[k], rr[k]
            rl, rc = r['label'], r['conf']
            firm = rc in ('H', 'M') and not rl.startswith('SPLIT')
            if firm and rl in (t['A'], t['B']):
                note = 'lookalike 2-of-3' if t['why'] == 'split' else 'lookalike confirms'
            else:
                uns += 1; note = 'lookalike UNSETTLED'
                cands = sorted({x for x in (t['A'], t['B'], t['passC'], rl.replace('SPLIT:', '').split('|')[0],
                                            *rl.replace('SPLIT:', '').split('|'), r['second']) if x})
                q = (f"{c['passage']}.{c['pos']}: readers {t['A'] or '-'}/{t['B'] or '-'}, look-alike {rl} ({rc}); "
                     f"which of {', '.join(cands)}?")
            if firm and rl in (t['A'], t['B']):   # primary (fixed before scoring): only a 2-of-3 relabels
                lab, conf = rl, rc
            if firm:
                alt_lab = rl                         # secondary: every firm re-read label, reported beside it
            if lab != c['sign_id']:
                changed += 1
        out.append(dict(passage=c['passage'], pos=c['pos'], sign_id=lab, conf=conf, note=note, question=q))
        alt.append(dict(passage=c['passage'], pos=c['pos'], sign_id=alt_lab or lab, conf=conf, note=note))
    with open(H / 'lookalike' / f'{run}_passD.tsv', 'w', newline='') as o:
        w = csv.DictWriter(o, fieldnames=list(out[0]), delimiter='\t'); w.writeheader(); w.writerows(out)
    with open(H / 'lookalike' / f'{run}_passD_alt.tsv', 'w', newline='') as o:
        w = csv.DictWriter(o, fieldnames=list(alt[0]), delimiter='\t'); w.writeheader(); w.writerows(alt)
    print(f'{run}: signs {len(pc)}, flagged {len(tiles)}, relabelled {changed}, unsettled {uns}, '
          f'residual disagreement {uns / len(pc):.3f}')
