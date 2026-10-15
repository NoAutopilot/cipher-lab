#!/usr/bin/env python3
"""MONL-ADH: write the 4 blind sort prompts (sort/adh/prompt_{A,B}{1,2}.md); B lists the same tiles in reverse order. Run from the folder."""
import csv, os
D = os.path.abspath('.')
def tiles(f, page):
    return [(page, r['passage'], r['pos'], r['before'], r['after'], r['candidates'].replace(',', ' or '))
            for r in csv.DictReader(open(f), delimiter='\t')]
b, c = tiles('sort/adh/adh268c_win_tiles.tsv', 'c268c'), tiles('sort/adh/adh172_win_tiles.tsv', 'c172')
calls = [(['adh268c_win_01.png', 'adh172_win_01.png'], b[:7] + c[:4]), (['adh268c_win_02.png', 'adh172_win_02.png'], b[7:] + c[4:])]
HEAD = f"""# MONL-ADH blind sort {{s}}{{i}} (value-blind)

You are sorting handwritten cipher signs by SHAPE only. You are never told what any sign means; do not guess letters or words.

Reference sheets: {D}/sort/adh/candidates.png (eight candidate cells, left to right K04, K12, K11, K62, K37, K43, K14, K17, cut from a
printed key table) and {D}/images/keysheet_monluc1_ids.png (the full table, ids only) so you can recognise the context signs.

Each tile has its own window in a montage (captioned in blue with passage.pos). Red ticks top and bottom mark the ESTIMATED position of
the sign (the estimate can be off by 1-3 signs): find the sign with the ids of the 3 signs before and after it, then decide which of its
TWO candidate cells its shape matches. The pair order is numeric; nothing tells you which is right. Shape cues: K04 vs K12 = how the stem
of the '9' ends (straight blunt vertical stem vs a stem curving down-left into a tail); K11 vs K62 = compare the top loop and the
cross-bar(s) of the two loop-and-cross cells; K37 vs K43 = a 'K' built on an upright stem vs a bowtie of two crossing diagonals with
closed sides; K14 vs K17 = closed 'b'-like form vs a hooked stroke opening to the right. Montage captions use the passage ids in the list
below (page c268c and c172 are two different pages).

Montages: {{m}}

Use the Read tool on each image. Answer ONLY one TSV block, one row per tile, header: page<TAB>passage<TAB>pos<TAB>label<TAB>conf<TAB>note
  label = one of the tile's two candidate ids, X_NEW if neither fits, or SPLIT if you cannot choose; conf H clear / M probable /
  L guess (use L whenever you could not find the sign in its window); note = the shape feature you SAW (a few words).

Tiles (page, passage, pos, context, candidates):
"""
for s in 'AB':
    for i, (ms, ts) in enumerate(calls, 1):
        rows = ts if s == 'A' else ts[::-1]
        m = ', '.join(f'{D}/sort/adh/win/{x}' for x in ms)
        txt = HEAD.format(s=s, i=i, m=m) + ''.join(f"{p}\t{a}\t{q}\tbefore: {bf} | after: {af}\tcandidates: {c}\n" for p, a, q, bf, af, c in rows)
        open(f'sort/adh/prompt_{s}{i}.md', 'w').write(txt)
print([len(t) for _, t in calls])
