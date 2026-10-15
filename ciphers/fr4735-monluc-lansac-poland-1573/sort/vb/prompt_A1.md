# MONL-VB blind sort A1 (value-blind)

You are sorting handwritten cipher signs by SHAPE only. You are never told what any sign means; do not guess letters or words.

Reference sheets: /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/sort/vb/candidates.png (seven candidate cells, left to right K04, K12, K14, K17, K22, K34, K53, cut from a
printed key table) and /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/images/keysheet_monluc1_ids.png (the full table, ids only) so you can recognise the context signs.

Each tile has its own window in a montage (captioned in blue with passage.pos). Red ticks top and bottom mark the ESTIMATED position of
the sign (the estimate can be off by 1-3 signs): find the sign with the ids of the 3 signs before and after it, then decide which of its
TWO candidate cells its shape matches. The pair order is numeric; nothing tells you which is right. Shape cues: K04 vs K12 = how the stem
of the '9' ends (straight blunt vertical stem vs a stem curving down-left into a tail); K14 vs K17 = closed 'b'-like form vs a hooked
stroke opening to the right; K34 vs K53 = upright beta with straight stem vs slanted beta whose foot sweeps down-left; K12 vs K22 = compare
the descender with both cells. Montage captions use the passage ids in the list below (page c268b and c268a are two parts of one page; c172 another page).

Montages: /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/sort/vb/win/vb268b_win_01.png

Use the Read tool on each image. Answer ONLY one TSV block, one row per tile, header: page<TAB>passage<TAB>pos<TAB>label<TAB>conf<TAB>note
  label = one of the tile's two candidate ids, X_NEW if neither fits, or SPLIT if you cannot choose; conf H clear / M probable /
  L guess (use L whenever you could not find the sign in its window); note = the shape feature you SAW (a few words).

Tiles (page, passage, pos, context, candidates):
c268b	L01	5	before: K37 K38 K19 | after: K34 K33 K67	candidates: K04 or K12
c268b	L01	6	before: K38 K19 K04 | after: K33 K67 K09	candidates: K34 or K53
c268b	L01	18	before: K05 K62 K33 | after: K14 K26 K09	candidates: K04 or K12
c268b	L01	19	before: K62 K33 K04 | after: K26 K09 K07	candidates: K14 or K17
c268b	L01	23	before: K26 K09 K07 | after: K05 K39 K36	candidates: K04 or K12
c268b	L01	34	before: K38 K39 K05 | after: K09 K36	candidates: K04 or K12
c268b	L02	1	before:  | after: K12 K36 K04	candidates: K34 or K53
c268b	L02	2	before: K34 | after: K36 K04 K05	candidates: K04 or K12
c268b	L02	4	before: K34 K12 K36 | after: K05 K19 K41	candidates: K04 or K12
c268b	L02	12	before: K15 K42 K33 | after: K29 K05 K34	candidates: K34 or K53
c268b	L02	15	before: K34 K29 K05 | after: K41 K12 K14	candidates: K34 or K53
c268b	L02	17	before: K05 K34 K41 | after: K14 K05 K22	candidates: K04 or K12
