#!/usr/bin/env python3
"""MONL-K04: write the 2 blind sort prompts (sort/k04/prompt_{A,B}.md); B lists the same 12 tiles in reverse order. Run from the folder
after the three lookalike_pass.py windows runs (k04268d_win, k04268c_win, k04172_win)."""
import csv, os
D = os.path.abspath('.')
def tiles(f, page):
    return [(page, r['passage'], r['pos'], r['before'], r['after']) for r in csv.DictReader(open(f), delimiter='\t')]
ts = tiles('sort/k04/k04268d_win_tiles.tsv', 'c268d') + tiles('sort/k04/k04268c_win_tiles.tsv', 'c268c') + tiles('sort/k04/k04172_win_tiles.tsv', 'c172')
assert len(ts) == 12, len(ts)
ms = ', '.join(f'{D}/sort/k04/win/{x}' for x in ('k04268d_win_01.png', 'k04268c_win_01.png', 'k04172_win_01.png'))
HEAD = f"""# MONL-K04 blind sort {{s}} (value-blind)

You are sorting handwritten cipher signs by SHAPE only. You are never told what any sign means; do not guess letters or words.

Reference sheets: {D}/sort/k04/candidates.png (two candidate cells, left K04, right K12, cut from a printed key table) and
{D}/images/keysheet_monluc1_ids.png (the full table, ids only) so you can recognise the context signs.

Each tile has its own window in a montage (captioned in blue with passage.pos). Red ticks top and bottom mark the ESTIMATED position of
the sign (the estimate can be off by 1-3 signs): find the sign with the ids of the 3 signs before and after it, then decide which of its
TWO candidate cells its shape matches. The pair order is numeric; nothing tells you which is right, and any mix of answers is possible.
Shape cue: K04 vs K12 = how the stem of the '9'-like sign ends (a straight blunt vertical stem vs a stem curving down-left into a tail).
Montage captions use the passage ids in the list below (pages c268d, c268c and c172 are different montages).

Montages: {ms}

Use the Read tool on each image. Answer ONLY one TSV block, one row per tile, header: page<TAB>passage<TAB>pos<TAB>label<TAB>conf<TAB>note
  label = K04 or K12, X_NEW if neither fits, or SPLIT if you cannot choose; conf H clear / M probable / L guess (use L whenever you could
  not find the sign in its window); note = the shape feature you SAW (a few words).

Tiles (page, passage, pos, context, candidates):
"""
for s in 'AB':
    rows = ts if s == 'A' else ts[::-1]
    txt = HEAD.format(s=s) + ''.join(f"{p}\t{a}\t{q}\tbefore: {bf} | after: {af}\tcandidates: K04 or K12\n" for p, a, q, bf, af in rows)
    open(f'sort/k04/prompt_{s}.md', 'w').write(txt)
print('sort/k04/prompt_A.md, prompt_B.md', len(ts))
