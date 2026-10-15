# MONL-ADH blind sort A1 (value-blind)

You are sorting handwritten cipher signs by SHAPE only. You are never told what any sign means; do not guess letters or words.

Reference sheets: /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/sort/adh/candidates.png (eight candidate cells, left to right K04, K12, K11, K62, K37, K43, K14, K17, cut from a
printed key table) and /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/images/keysheet_monluc1_ids.png (the full table, ids only) so you can recognise the context signs.

Each tile has its own window in a montage (captioned in blue with passage.pos). Red ticks top and bottom mark the ESTIMATED position of
the sign (the estimate can be off by 1-3 signs): find the sign with the ids of the 3 signs before and after it, then decide which of its
TWO candidate cells its shape matches. The pair order is numeric; nothing tells you which is right. Shape cues: K04 vs K12 = how the stem
of the '9' ends (straight blunt vertical stem vs a stem curving down-left into a tail); K11 vs K62 = compare the top loop and the
cross-bar(s) of the two loop-and-cross cells; K37 vs K43 = a 'K' built on an upright stem vs a bowtie of two crossing diagonals with
closed sides; K14 vs K17 = closed 'b'-like form vs a hooked stroke opening to the right. Montage captions use the passage ids in the list
below (page c268c and c172 are two different pages).

Montages: /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/sort/adh/win/adh268c_win_01.png, /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/sort/adh/win/adh172_win_01.png

Use the Read tool on each image. Answer ONLY one TSV block, one row per tile, header: page<TAB>passage<TAB>pos<TAB>label<TAB>conf<TAB>note
  label = one of the tile's two candidate ids, X_NEW if neither fits, or SPLIT if you cannot choose; conf H clear / M probable /
  L guess (use L whenever you could not find the sign in its window); note = the shape feature you SAW (a few words).

Tiles (page, passage, pos, context, candidates):
c268c	L06	12	before: K35 K15 K40 | after: K01 K04 K04	candidates: K11 or K62
c268c	L06	14	before: K40 K11 K01 | after: K04 K05 K15	candidates: K04 or K12
c268c	L06	23	before: K14 K29 K33 | after: K32 K05 K10	candidates: K04 or K12
c268c	L08	3	before: K35 K05 | after: K41 K29 K30	candidates: K11 or K62
c268c	L08	7	before: K41 K29 K30 | after: K14 K33 K62	candidates: K37 or K43
c268c	L08	10	before: K37 K14 K33 | after: K05 K19 K39	candidates: K11 or K62
c268c	L08	14	before: K05 K19 K39 | after: K05 K37 K01	candidates: K04 or K12
c172	L02	48	before: K15 K39 K26 | after: K39 K39 K16	candidates: K14 or K17
c172	L02	54	before: K16 K42 K11 | after: K05 K14 K03	candidates: K14 or K17
c172	L03	26	before: K06 K41 K39 | after: K49 K13 K09	candidates: K04 or K12
c172	L03	40	before: K39 K14 K38 | after: K13 K09 K01	candidates: K14 or K17
