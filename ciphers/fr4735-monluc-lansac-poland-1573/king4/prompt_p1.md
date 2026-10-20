# Look-alike re-read by window, c258_win (value-blind)

42 tiles (part 1 of 3). Each has its own window image: open the montages below IN ORDER (6 windows each, captioned in blue with the
tile id passage.pos). In each window the red ticks top and bottom mark the ESTIMATED position of the sign (the estimate can be off by 1-3
signs). Find the sign using the labels of the 3 signs before and after it, then decide which candidate's SHAPE it is.
The candidate list is alphabetical; nothing tells you which is "right". You are never told what any sign means; do not guess
letters or words.


Answer one TSV row per tile, header: passage<TAB>pos<TAB>label<TAB>conf<TAB>second<TAB>note
  label = one candidate id, X_NEW if none fits, SPLIT:a|b if you cannot choose; conf H clear / M probable / L guess (use L
  whenever you could not find the sign in its window); second = runner-up or empty; note = the shape feature you SAW.

L01	1	before:  | after: K40 K14 K01	candidates: W:molina = a word written in clear letters: molina; W:molino = a word written in clear letters: molino

Montages (open each with the Read tool, in order): /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/king4/win/c258_win_01.png, /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/king4/win/c258_win_02.png, /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/king4/win/c258_win_03.png, /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/king4/win/c258_win_04.png, /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/king4/win/c258_win_05.png, /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/king4/win/c258_win_06.png, /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/king4/win/c258_win_07.png
Candidate sheet (open with the Read tool; each cell shows a sign shape and its id): /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/king4/candidates.png

Write your answer as a TSV file (header row exactly: passage	pos	label	conf	second	note) to /home/user/cipher-lab/ciphers/fr4735-monluc-lansac-poland-1573/king4/reread_p1.tsv with the Write tool, then reply "done" and the row count. Do not open any other file in the repository.

Tiles (passage, pos, context, candidates):
L01	1	before:  | after: K40 K14 K01	candidates: W:molina = a word written in clear letters: molina; W:molino = a word written in clear letters: molino
L01	6	before: K14 K01 K04 | after: K26 ?x[vertical_stroke] K68	candidates: K59 = the cell labelled K59 in candidates.png; K61 = the cell labelled K61 in candidates.png
L01	8	before: K04 K59 K26 | after: K68 K02 K01	candidates: ?x[short_vertical_stroke] = not on the sheet: short vertical stroke; ?x[vertical_stroke] = not on the sheet: vertical stroke; K64 = the cell labelled K64 in candidates.png
L01	9	before: K59 K26 ?x[vertical_stroke] | after: K02 K01 K10	candidates: K37 = the cell labelled K37 in candidates.png; K68 = the cell labelled K68 in candidates.png
L01	18	before: K09 K14 K05 | after: K26 K38 K05	candidates: K11 = the cell labelled K11 in candidates.png; K62 = the cell labelled K62 in candidates.png
L01	25	before: K32 K04 K33 | after: K40 K01 K29	candidates: K19 = the cell labelled K19 in candidates.png; K39 = the cell labelled K39 in candidates.png
L01	34	before: K26 K23 K30 | after: K09	candidates: K19 = the cell labelled K19 in candidates.png; K39 = the cell labelled K39 in candidates.png
L02	13	before: K26 K11 K42 | after: K38 ?double_slash K05	candidates: K01 = the cell labelled K01 in candidates.png; K04 = the cell labelled K04 in candidates.png
L02	27	before: K05 K14 K36 | after: K04 K38 ?x[short_vertical_stroke]	candidates: K01 = the cell labelled K01 in candidates.png; K04 = the cell labelled K04 in candidates.png
L02	30	before: K01 K04 K38 | after: K64 K39 K26	candidates: ?x[short_vertical_stroke] = not on the sheet: short vertical stroke; ?x[vertical_stroke] = not on the sheet: vertical stroke
L02	31	before: K04 K38 ?x[short_vertical_stroke] | after: K39 K26 K59	candidates: ?x[vertical_stroke] = not on the sheet: vertical stroke; K64 = the cell labelled K64 in candidates.png
L02	32	before: K38 ?x[short_vertical_stroke] K64 | after: K26 K59 K05	candidates: K38 = the cell labelled K38 in candidates.png; K39 = the cell labelled K39 in candidates.png
L02	34	before: K64 K39 K26 | after: K05 K36 K05	candidates: K59 = the cell labelled K59 in candidates.png; K61 = the cell labelled K61 in candidates.png
L02	43	before: K07 K04 K33 | after: 	candidates: ?x[A-like_sign_at_edge] = not on the sheet: A-like sign at edge; K66 = the cell labelled K66 in candidates.png
L03	1	before:  | after: K05 K10 K26	candidates: ?x[C_with_horizontal_bar] = not on the sheet: C with horizontal bar; K52 = the cell labelled K52 in candidates.png
L03	7	before: K26 K40 K11 | after: K04 K14 K36	candidates: K19 = the cell labelled K19 in candidates.png; K39 = the cell labelled K39 in candidates.png
L03	14	before: K33 K39 K05 | after: K02 K26 K04	candidates: K14 = the cell labelled K14 in candidates.png; K36 = the cell labelled K36 in candidates.png
L03	25	before: K38 K36 K05 | after: K26 K36 K09	candidates: K19 = the cell labelled K19 in candidates.png; K39 = the cell labelled K39 in candidates.png
L03	34	before: K02 K10 K05 | after: K15 ?x[looped_l] K05	candidates: ?x[short_vertical_stroke] = not on the sheet: short vertical stroke; ?x[vertical_stroke] = not on the sheet: vertical stroke
L03	36	before: K05 ?x[short_vertical_stroke] K15 | after: K05	candidates: ?x[looped_l] = not on the sheet: looped l; ?x[small_i-stroke] = not on the sheet: small i-stroke
L04	6	before: K10 K26 K37 | after: K06 K33 K30	candidates: ?x[short_vertical_stroke] = not on the sheet: short vertical stroke; ?x[vertical_stroke] = not on the sheet: vertical stroke
L04	19	before: K26 K04 K06 | after: K04 K14 K05	candidates: K01 = the cell labelled K01 in candidates.png; K04 = the cell labelled K04 in candidates.png
L04	26	before: K38 K04 K04 | after: K38 K04 K04	candidates: K19 = the cell labelled K19 in candidates.png; K39 = the cell labelled K39 in candidates.png
L04	32	before: K04 K08 K15 | after: K59 K10 ?x[L-shaped_stroke]	candidates: K19 = the cell labelled K19 in candidates.png; K39 = the cell labelled K39 in candidates.png
L04	33	before: K08 K15 K19 | after: K10 ?x[L-shaped_stroke] K04	candidates: K59 = the cell labelled K59 in candidates.png; K61 = the cell labelled K61 in candidates.png
L04	35	before: K19 K59 K10 | after: K04 K05 K49	candidates: ?x[L-shaped_bracket] = not on the sheet: L-shaped bracket; ?x[L-shaped_stroke] = not on the sheet: L-shaped stroke
L04	38	before: ?x[L-shaped_stroke] K04 K05 | after: K08 K05 K10	candidates: K36 = the cell labelled K36 in candidates.png; K49 = the cell labelled K49 in candidates.png
L05	1	before:  | after: K61 K29 K01	candidates: K15 = the cell labelled K15 in candidates.png; K64 = the cell labelled K64 in candidates.png
L05	2	before: K64 | after: K29 K01 K14	candidates: K38 = the cell labelled K38 in candidates.png; K61 = the cell labelled K61 in candidates.png
L05	10	before: K36 K30 K05 | after: K42 K04 ?double_slash	candidates: ?x[short_vertical_stroke] = not on the sheet: short vertical stroke; ?x[vertical_stroke] = not on the sheet: vertical stroke
L05	39	before: K39 K05 K26 | after: 	candidates: ?x[A-like_sign_at_edge] = not on the sheet: A-like sign at edge; K66 = the cell labelled K66 in candidates.png
L06	3	before: K21 K26 | after: K15 K61 K42	candidates: K15 = the cell labelled K15 in candidates.png; K61 = the cell labelled K61 in candidates.png; K64 = the cell labelled K64 in candidates.png
L06	5	before: K26 K15 K15 | after: K42 W:Marie K30	candidates: K38 = the cell labelled K38 in candidates.png; K61 = the cell labelled K61 in candidates.png
L06	26	before: K14 K04 K26 | after: K19 K02 K05	candidates: K10 = the cell labelled K10 in candidates.png; K11 = the cell labelled K11 in candidates.png
L07	3	before: K36 K05 | after: K10 K26 K04	candidates: K38 = the cell labelled K38 in candidates.png; K61 = the cell labelled K61 in candidates.png
L07	4	before: K36 K05 K61 | after: K26 K04 K33	candidates: K10 = the cell labelled K10 in candidates.png; K11 = the cell labelled K11 in candidates.png
L07	22	before: K36 W:Juno K26 | after: K14 K33 K36	candidates: K04 = the cell labelled K04 in candidates.png; K12 = the cell labelled K12 in candidates.png
L07	26	before: K14 K33 K36 | after: K05 K36 K10	candidates: K38 = the cell labelled K38 in candidates.png; K61 = the cell labelled K61 in candidates.png
L07	29	before: K38 K05 K36 | after: K12 K04 K33	candidates: K10 = the cell labelled K10 in candidates.png; K11 = the cell labelled K11 in candidates.png
L07	31	before: K36 K10 K12 | after: K33 K68 K26	candidates: K04 = the cell labelled K04 in candidates.png; K12 = the cell labelled K12 in candidates.png
L07	35	before: K33 K68 K26 | after: K05	candidates: K58 = the cell labelled K58 in candidates.png; K62 = the cell labelled K62 in candidates.png
L08	3	before: K26 K37 | after: K12 K10 K33	candidates: K38 = the cell labelled K38 in candidates.png; K39 = the cell labelled K39 in candidates.png; K61 = the cell labelled K61 in candidates.png
