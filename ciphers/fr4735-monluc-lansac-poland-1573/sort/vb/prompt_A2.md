# MONL-VB blind sort A2 (value-blind)

You are sorting handwritten cipher signs by SHAPE only. You are never told what any sign means; do not guess letters or words.

Reference sheets: /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/sort/vb/candidates.png (seven candidate cells, left to right K04, K12, K14, K17, K22, K34, K53, cut from a
printed key table) and /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/images/keysheet_monluc1_ids.png (the full table, ids only) so you can recognise the context signs.

Each tile has its own window in a montage (captioned in blue with passage.pos). Red ticks top and bottom mark the ESTIMATED position of
the sign (the estimate can be off by 1-3 signs): find the sign with the ids of the 3 signs before and after it, then decide which of its
TWO candidate cells its shape matches. The pair order is numeric; nothing tells you which is right. Shape cues: K04 vs K12 = how the stem
of the '9' ends (straight blunt vertical stem vs a stem curving down-left into a tail); K14 vs K17 = closed 'b'-like form vs a hooked
stroke opening to the right; K34 vs K53 = upright beta with straight stem vs slanted beta whose foot sweeps down-left; K12 vs K22 = compare
the descender with both cells. Montage captions use the passage ids in the list below (page c268b and c268a are two parts of one page; c172 another page).

Montages: /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/sort/vb/win/vb268b_win_02.png

Use the Read tool on each image. Answer ONLY one TSV block, one row per tile, header: page<TAB>passage<TAB>pos<TAB>label<TAB>conf<TAB>note
  label = one of the tile's two candidate ids, X_NEW if neither fits, or SPLIT if you cannot choose; conf H clear / M probable /
  L guess (use L whenever you could not find the sign in its window); note = the shape feature you SAW (a few words).

Tiles (page, passage, pos, context, candidates):
c268b	L02	18	before: K34 K41 K12 | after: K05 K22 K39	candidates: K14 or K17
c268b	L02	24	before: K39 K33 K09 | after: K34 K41 K38	candidates: K14 or K17
c268b	L02	25	before: K33 K09 K14 | after: K41 K38 K09	candidates: K34 or K53
c268b	L03	6	before: K16 K62 K41 | after: K05 ?double_slash K33	candidates: K14 or K17
c268b	L03	10	before: K05 ?double_slash K33 | after: K12 K26 K33	candidates: K04 or K12
c268b	L03	11	before: ?double_slash K33 K04 | after: K26 K33 K36	candidates: K04 or K12
c268b	L03	17	before: K36 K22 K09 | after: K33 K04 K24	candidates: K14 or K17
c268b	L03	19	before: K09 K14 K33 | after: K24 W:uing K14	candidates: K04 or K12
c268b	L03	22	before: K04 K24 W:uing | after: K34 K06 K22	candidates: K14 or K17
c268b	L03	23	before: K24 W:uing K14 | after: K06 K22 K39	candidates: K34 or K53
c268b	L04	15	before: K05 K11 K33 | after: K05 K04 K32	candidates: K34 or K53
c268b	L04	17	before: K33 K34 K05 | after: K32 K33 K39	candidates: K04 or K12
