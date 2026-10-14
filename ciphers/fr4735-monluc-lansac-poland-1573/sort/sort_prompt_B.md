# MONL-SORT blind sort B (value-blind)

You are sorting handwritten cipher signs by SHAPE only. You are never told what any sign means; do not guess letters or words.

Reference sheets: /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/sort/candidates.png (the six candidate cells K04, K12, K14, K17, K34, K53, cut from a printed key table) and
/home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/images/keysheet_monluc1_ids.png (the full table, ids only) so you can recognise the context signs named before/after each tile.

Each tile has its own window in a montage (captioned in blue with passage.pos; a montage holds up to 6 windows). Red ticks top and bottom
mark the ESTIMATED position of the sign (the estimate can be off by 1-3 signs): find the sign with the labels of the 3 signs before and
after it, then decide which of its TWO candidate cells its shape matches. The pair order is numeric; nothing tells you which is right.
Shape cues to look at: K04 vs K12 = how the stem of the '9' ends (straight down vs a tail sweeping left); K14 vs K17 = 'b'-like closed
form vs a hooked stroke opening to the right; K34 vs K53 = upright beta with straight stem vs slanted beta whose foot sweeps down-left.

Montages for page c172 (passages c172): /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/sort/win/s172_win_01.png, /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/sort/win/s172_win_02.png, /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/sort/win/s172_win_03.png
Montages for page c268 (passages c268): /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/sort/win/s268_win_01.png, /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/sort/win/s268_win_02.png, /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/sort/win/s268_win_03.png, /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/sort/win/s268_win_04.png, /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/sort/win/s268_win_05.png, /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/sort/win/s268_win_06.png

Answer ONLY one TSV block, one row per tile, header: page<TAB>passage<TAB>pos<TAB>label<TAB>conf<TAB>note
  label = one of the tile's two candidate ids, X_NEW if neither fits, or SPLIT if you cannot choose; conf H clear / M probable /
  L guess (use L whenever you could not find the sign in its window); note = the shape feature you SAW (a few words).

Tiles (page, passage, pos, context, candidates):
c172	L02	3	before: K38 K05 | after: K11 K39 K09	candidates: 
c172	L02	21	before: K09 K03 K38 | after: K05 K07 K01	candidates: 
c172	L02	30	before: K16 K01 K05 | after: K38 K41 K18	candidates: 
c172	L02	48	before: K15 K39 K26 | after: K39 K39 K16	candidates: 
c172	L02	54	before: K16 K42 K11 | after: K05 K14 K03	candidates: 
c172	L02	56	before: K11 K14 K05 | after: K03 K08 K26	candidates: 
c172	L03	5	before: K09 K26 K39 | after: K38 K15 K39	candidates: 
c172	L03	26	before: K06 K41 K39 | after: K49 K13 K09	candidates: 
c172	L03	38	before: K01 K05 K39 | after: K38 K14 K13	candidates: 
c172	L03	40	before: K39 K14 K38 | after: K13 K09 K01	candidates: 
c172	L03	52	before: K16 K07 ?vertical_bar | after: K05 K01 ?vertical_bar	candidates: 
c172	L04	4	before: K15 K39 K10 | after: K13 K09 K07	candidates: 
c172	L04	8	before: K13 K09 K07 | after: K09 K01 K13	candidates: 
c172	L04	13	before: K01 K13 K01 | after: K26 K16 K05	candidates: 
c172	L04	19	before: K05 K01 K01 | after: K16 K42 K38	candidates: 
c172	L04	24	before: K42 K38 K42 | after: K11 K13 K07	candidates: 
c268	L01	4	before: K10 K26 K37 | after: K05 K36 K39	candidates: K14 or K17
c268	L01	21	before: K15 K39 K09 | after: K34 K26 K37	candidates: K04 or K12
c268	L01	22	before: K39 K09 K12 | after: K26 K37 K34	candidates: K34 or K53
c268	L01	25	before: K34 K26 K37 | after: K22 K36 K07	candidates: K34 or K53
c268	L01	29	before: K22 K36 K07 | after: K26 K12 K38	candidates: K04 or K12
c268	L01	31	before: K07 K12 K26 | after: K38 K10 K08	candidates: K04 or K12
c268	L02	14	before: K22 K36 K05 | after: K19 K38 K22	candidates: K14 or K17
c268	L02	21	before: K38 K09 K33 | after: K32 K29 K10	candidates: K04 or K12
c268	L02	28	before: K22 ?double_slash K33 | after: K14 ?double_slash K29	candidates: K04 or K12
c268	L02	29	before: ?double_slash K33 K12 | after: ?double_slash K29 K26	candidates: K14 or K17
c268	L02	33	before: ?double_slash K29 K26 | after: ?h_bar K05 K12	candidates: K04 or K12
c268	L02	36	before: K12 ?h_bar K05 | after: K19	candidates: K04 or K12
c268	L03	1	before:  | after: K33 K34 K10	candidates: K14 or K17
c268	L03	3	before: K14 K33 | after: K10 K33 K12	candidates: K34 or K53
c268	L03	6	before: K34 K10 K33 | after: K06 K22 K09	candidates: K04 or K12
c268	L03	11	before: K22 K09 K38 | after: K22 K36 K10	candidates: K34 or K53
c268	L03	21	before: K26 K36 K33 | after: K12 K05 K25	candidates: K34 or K53
c268	L03	22	before: K36 K33 K34 | after: K05 K25 K41	candidates: K04 or K12
c268	L03	27	before: K25 K41 K62 | after: K05 K62 K22	candidates: K04 or K12
c268	L03	36	before: K15 K63 K59 | after: 	candidates: K04 or K12
c268	L04	2	before: K19 | after: K26 K12 K14	candidates: K34 or K53
c268	L04	4	before: K19 K34 K26 | after: K14 K12 K29	candidates: K04 or K12
c268	L04	5	before: K34 K26 K12 | after: K12 K29 K12	candidates: K14 or K17
c268	L04	6	before: K26 K12 K14 | after: K29 K12 K62	candidates: K04 or K12
c268	L04	8	before: K14 K12 K29 | after: K62 K41 K09	candidates: K04 or K12
c268	L04	15	before: K37 K26 K38 | after: K33 K66 K26	candidates: K04 or K12
c268	L04	23	before: K38 K41 K05 | after: K38 K26 K22	candidates: K04 or K12
c268	L05	4	before: K26 K05 K13 | after: K09 K10 K41	candidates: K34 or K53
c268	L05	12	before: K09 K36 K05 | after: K38 K12 K05	candidates: K04 or K12
c268	L05	14	before: K05 K12 K38 | after: K05 K30 K41	candidates: K04 or K12
c268	L05	19	before: K30 K41 K40 | after: K05 K20 ?double_slash	candidates: K04 or K12
c268	L05	25	before: ?double_slash K10 K39 | after: K09 K33 K12	candidates: K14 or K17
c268	L05	28	before: K14 K09 K33 | after: K15 K15 K29	candidates: K04 or K12
