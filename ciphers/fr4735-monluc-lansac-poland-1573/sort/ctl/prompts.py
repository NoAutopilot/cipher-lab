#!/usr/bin/env python3
"""MONL-CTL: candidates.png (K04, K12 cut from the key sheet, as sort/k04/build_k04.py) and the 2 blind sort prompts
(sort/ctl/prompt_{A,B}.md, same wording as sort/k04/prompts.py); B lists the same 10 tiles in reverse order. Run from the folder after the
two lookalike_pass.py windows runs (ctl268d_win, ctl268c_win)."""
import csv, os
from PIL import Image
D = os.path.abspath('.')
ks = Image.open('images/keysheet_monluc1_ids.png').convert('RGB'); W, H = 136, 176
S = Image.new('RGB', (W * 2, H), 'white')
for j, k in enumerate(['K04', 'K12']):
    n = int(k[1:]) - 1; col, row = n % 8, n // 8
    S.paste(ks.crop((col * W, row * H, col * W + W, row * H + H)), (j * W, 0))
S.save('sort/ctl/win/candidates.png')
def tiles(f, page):
    return [(page, r['passage'], r['pos'], r['before'], r['after']) for r in csv.DictReader(open(f), delimiter='\t')]
ts = tiles('sort/ctl/ctl268d_win_tiles.tsv', 'c268d') + tiles('sort/ctl/ctl268c_win_tiles.tsv', 'c268c')
assert len(ts) == 10, len(ts)
ms = ', '.join(f'{D}/sort/ctl/win/{x}' for x in ('ctl268d_win_01.png', 'ctl268c_win_01.png'))
HEAD = f"""# MONL-CTL blind sort {{s}} (value-blind)

You are sorting handwritten cipher signs by SHAPE only. You are never told what any sign means; do not guess letters or words.

Reference sheets: {D}/sort/ctl/win/candidates.png (two candidate cells, left K04, right K12, cut from a printed key table) and
{D}/images/keysheet_monluc1_ids.png (the full table, ids only) so you can recognise the context signs.

Each tile has its own window in a montage (captioned in blue with passage.pos). Red ticks top and bottom mark the ESTIMATED position of
the sign (the estimate can be off by 1-3 signs): find the sign with the ids of the 3 signs before and after it, then decide which of its
TWO candidate cells its shape matches. The pair order is numeric; nothing tells you which is right, and any mix of answers is possible.
Shape cue: K04 vs K12 = how the stem of the '9'-like sign ends (a straight blunt vertical stem vs a stem curving down-left into a tail).
Montage captions use the passage ids in the list below (pages c268d and c268c are different montages).

Montages: {ms}

Use the Read tool on each image. Answer ONLY one TSV block, one row per tile, header: page<TAB>passage<TAB>pos<TAB>label<TAB>conf<TAB>note
  label = K04 or K12, X_NEW if neither fits, or SPLIT if you cannot choose; conf H clear / M probable / L guess (use L whenever you could
  not find the sign in its window); note = the shape feature you SAW (a few words).

Tiles (page, passage, pos, context, candidates):
"""
for s in 'AB':
    rows = ts if s == 'A' else ts[::-1]
    txt = HEAD.format(s=s) + ''.join(f"{p}\t{a}\t{q}\tbefore: {bf} | after: {af}\tcandidates: K04 or K12\n" for p, a, q, bf, af in rows)
    open(f'sort/ctl/prompt_{s}.md', 'w').write(txt)
print('sort/ctl/prompt_A.md, prompt_B.md', len(ts))
