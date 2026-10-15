#!/usr/bin/env python3
"""MONL-SORT2: candidates.png (8 cells cut from the key sheet as sort/ctl/prompts.py, labelled by id) and the 2 blind sort prompts
(sort/srt/prompt_{A,B}.md; MONL-CTL's wording with a per-tile candidate pair); B lists the 40 tiles in reverse order. No value, reading,
clear text, current label, role or decode is shown. Run from the folder after the three lookalike_pass.py windows runs."""
import csv, os
from PIL import Image, ImageDraw
D = os.path.abspath('.')
ks = Image.open('images/keysheet_monluc1_ids.png').convert('RGB'); W, H = 136, 176
CELLS = ['K04', 'K12', 'K14', 'K37', 'K39', 'K45', 'K40', 'K41']
S = Image.new('RGB', (W * 8, H + 24), 'white'); dr = ImageDraw.Draw(S)
for j, k in enumerate(CELLS):
    n = int(k[1:]) - 1; col, row = n % 8, n // 8
    S.paste(ks.crop((col * W, row * H, col * W + W, row * H + H)), (j * W, 24)); dr.text((j * W + 50, 4), k, fill=(0, 0, 0))
S.save('sort/srt/win/candidates.png')
ts = []
for pg in ('c268c', 'c268d', 'c268e'):
    ts += [(pg, r['passage'], r['pos'], r['before'], r['after'], r['candidates'].replace(',', ' or '))
           for r in csv.DictReader(open(f'sort/srt/win/srt_{pg}_tiles.tsv'), delimiter='\t')]
assert len(ts) == 40, len(ts)
ms = ', '.join(f'{D}/sort/srt/win/win/{x}' for x in sorted(os.listdir('sort/srt/win/win')) if x.endswith('.png'))
HEAD = f"""# MONL-SORT2 blind sort {{s}} (value-blind)

You are sorting handwritten cipher signs by SHAPE only. You are never told what any sign means; do not guess letters or words.

Reference sheets: {D}/sort/srt/win/candidates.png (eight candidate cells cut from a printed key table, each labelled with its id above it)
and {D}/images/keysheet_monluc1_ids.png (the full table, ids only) so you can recognise the context signs.

Each tile has its own window in a montage (captioned in blue with passage.pos). Red ticks top and bottom mark the ESTIMATED position of
the sign (the estimate can be off by 1-3 signs): find the sign with the ids of the 3 signs before and after it, then decide which of its
TWO candidate cells (given per tile) its shape matches. The pair order is numeric; nothing tells you which is right, and any mix of answers
is possible. Shape cues: K04 vs K12 = how the stem of the '9'-like sign ends (a straight blunt vertical stem vs a stem curving down-left into
a tail); for the other pairs compare the whole shape with the two cells.
Montages are named by page (c268c, c268d, c268e); the same passage id on two pages is two different lines, so use the page too.

Montages: {ms}

Use the Read tool on each image. Answer ONLY one TSV block, one row per tile, header: page<TAB>passage<TAB>pos<TAB>label<TAB>conf<TAB>note
  label = one of the tile's two candidate ids, X_NEW if neither fits, or SPLIT if you cannot choose; conf H clear / M probable / L guess
  (use L whenever you could not find the sign in its window); note = the shape feature you SAW (a few words).

Tiles (page, passage, pos, context, candidates):
"""
for s in 'AB':
    rows = ts if s == 'A' else ts[::-1]
    txt = HEAD.format(s=s) + ''.join(f"{p}\t{a}\t{q}\tbefore: {bf} | after: {af}\tcandidates: {c}\n" for p, a, q, bf, af, c in rows)
    open(f'sort/srt/prompt_{s}.md', 'w').write(txt)
print('sort/srt/prompt_A.md, prompt_B.md', len(ts))
