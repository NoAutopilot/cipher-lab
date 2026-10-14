# Look-alike re-read by window, s172_win (value-blind)

16 tiles. Each has its own window image: open the montages below IN ORDER (6 windows each, captioned in blue with the
tile id passage.pos). In each window the red ticks top and bottom mark the ESTIMATED position of the sign (the estimate can be off by 1-3
signs). Find the sign using the labels of the 3 signs before and after it, then decide which candidate's SHAPE it is.
The candidate list is alphabetical; nothing tells you which is "right". You are never told what any sign means; do not guess
letters or words.

Montages: /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/sort/win/s172_win_01.png, /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/sort/win/s172_win_02.png, /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/sort/win/s172_win_03.png

Answer one TSV row per tile, header: passage<TAB>pos<TAB>label<TAB>conf<TAB>second<TAB>note
  label = one candidate id, X_NEW if none fits, SPLIT:a|b if you cannot choose; conf H clear / M probable / L guess (use L
  whenever you could not find the sign in its window); second = runner-up or empty; note = the shape feature you SAW.

Tiles (passage, pos, context, candidates):
L02	3	before: K38 K05 | after: K11 K39 K09	candidates: K14; K17
L02	21	before: K09 K03 K38 | after: K05 K07 K01	candidates: K14; K17
L02	30	before: K16 K01 K05 | after: K38 K41 K18	candidates: K14; K17
L02	48	before: K15 K39 K26 | after: K39 K39 K16	candidates: K14; K17
L02	54	before: K16 K42 K11 | after: K05 K14 K03	candidates: K14; K17
L02	56	before: K11 K14 K05 | after: K03 K08 K26	candidates: K14; K17
L03	5	before: K09 K26 K39 | after: K38 K15 K39	candidates: K14; K17
L03	26	before: K06 K41 K39 | after: K49 K13 K09	candidates: K04; K12
L03	38	before: K01 K05 K39 | after: K38 K14 K13	candidates: K14; K17
L03	40	before: K39 K14 K38 | after: K13 K09 K01	candidates: K14; K17
L03	52	before: K16 K07 ?vertical_bar | after: K05 K01 ?vertical_bar	candidates: K04; K12
L04	4	before: K15 K39 K10 | after: K13 K09 K07	candidates: K14; K17
L04	8	before: K13 K09 K07 | after: K09 K01 K13	candidates: K14; K17
L04	13	before: K01 K13 K01 | after: K26 K16 K05	candidates: K04; K12
L04	19	before: K05 K01 K01 | after: K16 K42 K38	candidates: K04; K12
L04	24	before: K42 K38 K42 | after: K11 K13 K07	candidates: K14; K17
