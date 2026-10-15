# MONL-K04 blind sort B (value-blind)

You are sorting handwritten cipher signs by SHAPE only. You are never told what any sign means; do not guess letters or words.

Reference sheets: /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/sort/k04/candidates.png (two candidate cells, left K04, right K12, cut from a printed key table) and
/home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/images/keysheet_monluc1_ids.png (the full table, ids only) so you can recognise the context signs.

Each tile has its own window in a montage (captioned in blue with passage.pos). Red ticks top and bottom mark the ESTIMATED position of
the sign (the estimate can be off by 1-3 signs): find the sign with the ids of the 3 signs before and after it, then decide which of its
TWO candidate cells its shape matches. The pair order is numeric; nothing tells you which is right, and any mix of answers is possible.
Shape cue: K04 vs K12 = how the stem of the '9'-like sign ends (a straight blunt vertical stem vs a stem curving down-left into a tail).
Montage captions use the passage ids in the list below (pages c268d, c268c and c172 are different montages).

Montages: /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/sort/k04/win/k04268d_win_01.png, /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/sort/k04/win/k04268c_win_01.png, /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/sort/k04/win/k04172_win_01.png

Use the Read tool on each image. Answer ONLY one TSV block, one row per tile, header: page<TAB>passage<TAB>pos<TAB>label<TAB>conf<TAB>note
  label = K04 or K12, X_NEW if neither fits, or SPLIT if you cannot choose; conf H clear / M probable / L guess (use L whenever you could
  not find the sign in its window); note = the shape feature you SAW (a few words).

Tiles (page, passage, pos, context, candidates):
c172	L04	13	before: K01 K13 K01 | after: K26 K16 K05	candidates: K04 or K12
c172	L03	26	before: K06 K41 K39 | after: K49 K13 K09	candidates: K04 or K12
c268c	L06	14	before: K40 K11 K01 | after: K04 K05 K15	candidates: K04 or K12
c268d	L07	37	before: K05 K62 K26 | after: 	candidates: K04 or K12
c268d	L07	32	before: K62 K38 K26 | after: K04 K05 K62	candidates: K04 or K12
c268d	L07	27	before: K26 K02 K33 | after: K05 K62 K38	candidates: K04 or K12
c268d	L07	8	before: K09 K37 K33 | after: K01 K10 K09	candidates: K04 or K12
c268d	L06	6	before: K19 K09 K26 | after: K25 K36 K01	candidates: K04 or K12
c268d	L05	18	before: W:Sepbre K05 ?x[looped_c] | after: K26 K37 ?double_slash	candidates: K04 or K12
c268d	L04	20	before: K26 W:Cur W:apuril | after: K05 K07 K33	candidates: K04 or K12
c268d	L03	16	before: K05 K29 K07 | after: K05 K19 K36	candidates: K04 or K12
c268d	L03	11	before: K05 K11 K33 | after: K14 K05 K29	candidates: K04 or K12
