# MONL-SORT2 blind sort A (value-blind)

You are sorting handwritten cipher signs by SHAPE only. You are never told what any sign means; do not guess letters or words.

Reference sheets: /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/sort/srt/win/candidates.png (eight candidate cells cut from a printed key table, each labelled with its id above it)
and /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/images/keysheet_monluc1_ids.png (the full table, ids only) so you can recognise the context signs.

Each tile has its own window in a montage (captioned in blue with passage.pos). Red ticks top and bottom mark the ESTIMATED position of
the sign (the estimate can be off by 1-3 signs): find the sign with the ids of the 3 signs before and after it, then decide which of its
TWO candidate cells (given per tile) its shape matches. The pair order is numeric; nothing tells you which is right, and any mix of answers
is possible. Shape cues: K04 vs K12 = how the stem of the '9'-like sign ends (a straight blunt vertical stem vs a stem curving down-left into
a tail); for the other pairs compare the whole shape with the two cells.
Montages are named by page (c268c, c268d, c268e); the same passage id on two pages is two different lines, so use the page too.

Montages: /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/sort/srt/win/win/srt_c268c_01.png, /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/sort/srt/win/win/srt_c268c_02.png, /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/sort/srt/win/win/srt_c268d_01.png, /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/sort/srt/win/win/srt_c268e_01.png, /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/sort/srt/win/win/srt_c268e_02.png

Use the Read tool on each image. Answer ONLY one TSV block, one row per tile, header: page<TAB>passage<TAB>pos<TAB>label<TAB>conf<TAB>note
  label = one of the tile's two candidate ids, X_NEW if neither fits, or SPLIT if you cannot choose; conf H clear / M probable / L guess
  (use L whenever you could not find the sign in its window); note = the shape feature you SAW (a few words).

Tiles (page, passage, pos, context, candidates):
c268c	L01	18	before: K05 K62 K33 | after: K14 K26 K09	candidates: K04 or K12
c268c	L01	23	before: K26 K09 K07 | after: K05 K39 K36	candidates: K04 or K12
c268c	L01	34	before: K38 K39 K05 | after: K09 K36	candidates: K04 or K12
c268c	L03	6	before: K16 K62 K41 | after: K05 ?double_slash K33	candidates: K14 or K37
c268c	L03	10	before: K05 ?double_slash K33 | after: K12 K26 K33	candidates: K04 or K12
c268c	L03	19	before: K09 K14 K33 | after: K24 W:uing K14	candidates: K04 or K12
c268c	L03	22	before: K04 K24 W:uing | after: K34 K06 K22	candidates: K14 or K37
c268c	L04	27	before: K19 K38 K41 | after: K38 K25 K33	candidates: K04 or K12
c268c	L05	33	before: K04 K19 K05 | after: K19 K41	candidates: K04 or K12
c268c	L06	5	before: K04 K36 K29 | after: K66 K49 ?h_bar	candidates: K14 or K37
c268c	L06	20	before: K15 K19 K05 | after: K29 K33 K12	candidates: K14 or K37
c268c	L07	8	before: K05 K10 K33 | after: K14 K36 K05	candidates: K04 or K12
c268c	L07	9	before: K10 K33 K12 | after: K36 K05 K29	candidates: K14 or K37
c268c	L07	21	before: K06 K09 K10 | after: ?x[looped_q] K05 K15	candidates: K40 or K41
c268c	L08	13	before: K62 K05 K19 | after: K04 K05 K37	candidates: K39 or K45
c268c	L08	14	before: K05 K19 K39 | after: K05 K37 K01	candidates: K04 or K12
c268c	L09	13	before: K34 K36 K12 | after: K04 K36 K26	candidates: K04 or K12
c268c	L09	14	before: K36 K12 K12 | after: K36 K26 K10	candidates: K04 or K12
c268c	L10	4	before: K06 K16 K22 | after: K19 K05 K26	candidates: K04 or K12
c268c	L10	11	before: K12 K62 K05 | after: K62 K26 K37	candidates: K14 or K37
c268d	L03	16	before: K05 K29 K07 | after: K05 K19 K36	candidates: K04 or K12
c268d	L04	7	before: K01 K25 K26 | after: K01 K37 K10	candidates: K14 or K37
c268d	L05	18	before: W:Sepbre K05 ?x[looped_c] | after: K26 K37 ?double_slash	candidates: K04 or K12
c268d	L05	25	before: K01 K34 K15 | after: K09 K10 K26	candidates: K39 or K45
c268e	L02	7	before: K15 K19 K09 | after: K33 K04 K63	candidates: K14 or K37
c268e	L02	9	before: K09 K14 K33 | after: K63 K22 K62	candidates: K04 or K12
c268e	L02	13	before: K63 K22 K62 | after: K38 K05 K19	candidates: K40 or K41
c268e	L02	18	before: K05 K19 K36 | after: K25 K05 K10	candidates: K14 or K37
c268e	L03	6	before: K36 K05 K19 | after: K62 K33 K32	candidates: K40 or K41
c268e	L03	14	before: K05 K29 K07 | after: K26 K19 K36	candidates: K04 or K12
c268e	L04	16	before: K05 K10 K01 | after: K05 K34 K01	candidates: K04 or K12
c268e	L05	3	before: W:Juno K34 | after: K09 K37 K04	candidates: K39 or K45
c268e	L05	10	before: K29 K36 K05 | after: K29 K04 K33	candidates: K14 or K37
c268e	L05	12	before: K05 K14 K29 | after: K33 K32 K15	candidates: K04 or K12
c268e	L05	16	before: K33 K32 K15 | after: K26 W:Mare K14	candidates: K39 or K45
c268e	L05	26	before: K14 K40 K02 | after: K38 K39 K40	candidates: K40 or K41
c268e	L05	29	before: K41 K38 K39 | after: 	candidates: K40 or K41
c268e	L06	16	before: K33 K08 K05 | after: K04 K05 K10	candidates: K40 or K41
c268e	L06	17	before: K08 K05 K40 | after: K05 K10 K26	candidates: K04 or K12
c268e	L06	26	before: K05 K36 K01 | after: ?double_slash K05 K26	candidates: K04 or K12
