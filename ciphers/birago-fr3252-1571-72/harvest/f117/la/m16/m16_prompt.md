# Look-alike re-read by window, m16 (value-blind)

16 tiles. Each has its own window image: open the montages below IN ORDER (8 windows each, captioned in blue with the
tile id passage.pos). In each window the red ticks top and bottom mark the ESTIMATED position of the sign (the estimate can be off by 1-3
signs). Find the sign using the labels of the 3 signs before and after it, then decide which candidate's SHAPE it is.
The candidate list is alphabetical; nothing tells you which is "right". You are never told what any sign means; do not guess
letters or words.

Candidate shapes (ids only): /home/user/cipher-lab/ciphers/birago-fr3252-1571-72/harvest/f117/la/m16/m16_candidates.png

Montages: /home/user/cipher-lab/ciphers/birago-fr3252-1571-72/harvest/f117/la/m16/win/m16_01.png, /home/user/cipher-lab/ciphers/birago-fr3252-1571-72/harvest/f117/la/m16/win/m16_02.png

Answer one TSV row per tile, header: passage<TAB>pos<TAB>label<TAB>conf<TAB>second<TAB>note
  label = one candidate id, X_NEW if none fits, SPLIT:a|b if you cannot choose; conf H clear / M probable / L guess (use L
  whenever you could not find the sign in its window); second = runner-up or empty; note = the shape feature you SAW.

Tiles (passage, pos, context, candidates):
L01	13	before: T54 X_NEW T33 | after: T58 T88 T49	candidates: T45; T89; T90; X_NEW
L02	2	before: T95 | after: T60 T60 T25	candidates: T85; X_NEW
L02	15	before: T19 T60 T18 | after: T50 T19 T60	candidates: T66; T95; X_NEW
L02	27	before: T37 T49 T60 | after: X_NEW X_NEW	candidates: T18; T98; X_NEW
L03	5	before: T55 T33 T83 | after: T33 T19 T80	candidates: T51; T65; T66; T95; X_NEW
L05	19	before: T98 T45 T65 | after: X_NEW T66 T83	candidates: T45; T89; T90; X_NEW
L06	18	before: T98 T66 T60 | after: T95 T83 T60	candidates: T45; T89; T90; X_NEW
L06	24	before: T60 T96 T64 | after: T98 T45 T66	candidates: T45; T89; T90; X_NEW
L06	26	before: T64 T45 T98 | after: T66 T80 T66	candidates: T45; T89; T90; X_NEW
L06	31	before: T80 T66 T66 | after: 	candidates: T27; T36; T88; X_NEW
L07	23	before: X_K T65 T80 | after: T63 T37 X_NEW	candidates: T60; T86; X_NEW
L07	27	before: T63 T37 X_NEW | after: T60 T81	candidates: T18; T98; X_NEW
L07	29	before: X_NEW T98 T60 | after: 	candidates: T81; T83; X_NEW
L10	6	before: T33 T57 T80 | after: T60 X_NEW T84	candidates: T57; X_NEW
L10	9	before: T57 T60 X_NEW | after: T70 X_NEW	candidates: T70; T84; X_NEW
L10	10	before: T60 X_NEW T84 | after: X_NEW	candidates: T70; T84; X_NEW; X_S
