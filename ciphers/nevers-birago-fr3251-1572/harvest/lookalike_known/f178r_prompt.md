# Look-alike re-read, f178r (value-blind)

You are re-reading 40 sign tiles of a symbol-cipher transcription. Two earlier readers disagreed on some of them, or
gave a label that is often confused with another. You see only the line crops and a sheet of the candidate sign shapes,
labelled by id. You are never told what any sign means; do not guess letters or words.

Line crops (read these images): /home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/f178r/slope/f178r_L01_s1.jpg, /home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/f178r/slope/f178r_L01_s2.jpg, /home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/f178r/slope/f178r_L01_s3.jpg, /home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/f178r/slope/f178r_L02_s1.jpg, /home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/f178r/slope/f178r_L02_s2.jpg, /home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/f178r/slope/f178r_L02_s3.jpg, /home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/f178r/slope/f178r_L03_s1.jpg, /home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/f178r/slope/f178r_L03_s2.jpg, /home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/f178r/slope/f178r_L03_s3.jpg
Candidate sheet (ids only): /home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/lookalike_known/f178r_candidates.png

For each tile below, find the sign at that passage and position (the passC sequence of the line is given for
orientation; 'before'/'after' are the neighbouring labels) and pick the candidate id whose shape it is.
Answer one TSV row per tile, header: passage<TAB>pos<TAB>label<TAB>conf<TAB>second<TAB>note
  label  one of the tile's candidates, X_NEW if none fits, or SPLIT:a|b if you cannot choose between two
  conf   H (clear), M (probable), L (guess); second = your runner-up id or empty; note = the shape feature you used.

Tiles (passage, pos, candidates, before | after):
L01	4	T83,T24,X_NEW,T29	T45 T33 T45 | T19 T95 X_NEW
L01	6	T95,T98,T51,T66	T45 T83 T19 | X_NEW X_NEW T78
L01	7	X_NEW,T83,T92	T83 T19 T95 | X_NEW T78 T63
L01	8	X_NEW,T83,T92	T19 T95 X_NEW | T78 T63 T86
L01	11	T86,T60,T19	X_NEW T78 T63 | X_NEW T19 T58
L01	12	X_NEW,T83,T92	T78 T63 T86 | T19 T58 T53
L01	20	T83,T24,X_NEW,T29	T70 T25 T19 | T60 T80 T86
L01	21	T60,T86	T25 T19 T83 | T80 T86 T83
L01	23	T86,T60,T19	T83 T60 T80 | T83 T37 T85
L01	24	T83,T24,X_NEW,T29	T60 T80 T86 | T37 T85 T92
L01	27	T92,X_NEW,T50	T83 T37 T85 | T66 T83 T63
L01	29	T83,T24,X_NEW,T29	T85 T92 T66 | T63 T45
L02	1	T60,T86	 | T45 T98 T25
L02	3	T98,T18,X_NEW	T60 T45 | T25 T90 T97
L02	5	T90,X_NEW,T45	T45 T98 T25 | T97 T45 T65
L02	9	T86,T60,T19	T97 T45 T65 | T76 T18 T45
L02	11	T18,T98,T36	T65 T86 T76 | T45 T37 T36
L02	20	T86,T60,T19	T33 T45 T70 | T90 T80 T49
L02	21	T90,X_NEW,T45	T45 T70 T86 | T80 T49 T85
L02	25	T83,T24,X_NEW,T29	T80 T49 T85 | T25 T53 T19
L02	29	T83,T24,X_NEW,T29	T25 T53 T19 | T60 T37
L02	30	T60,T86	T53 T19 T83 | T37
L03	1	T83,T24,X_NEW,T29	 | T45 T37 X_NEW
L03	4	X_NEW,T83,T92	T83 T45 T37 | X_S X_NEW T37
L03	6	X_NEW,T83,T92	T37 X_NEW X_S | T37 T92 T55
L03	8	T92,X_NEW,T50	X_S X_NEW T37 | T55 T65 T19
L03	9	T55,X_NEW	X_NEW T37 T92 | T65 T19 T85
L03	16	T83,T24,X_NEW,T29	T76 T63 T37 | T92 T45 T60
L03	17	T92,X_NEW,T50	T63 T37 T83 | T45 T60 T45
L03	19	T60,T86	T83 T92 T45 | T45 T85 T46
L03	23	T90,X_NEW,T45	T45 T85 T46 | T53 T19 T58
L03	27	?,T65,T18,T95	T53 T19 T58 | T52 T95 T25
L03	28	T52,T64	T19 T58 T65 | T95 T25 T96
L03	29	T95,T51,T66	T58 T65 T52 | T25 T96 T66
L03	30	T25	T65 T52 T95 | T96 T66 T60
L03	31	T96	T52 T95 T25 | T66 T60 T90
L03	32	T66,T95,X_NEW	T95 T25 T96 | T60 T90 X_NEW
L03	33	T60,T86	T25 T96 T66 | T90 X_NEW
L03	34	T90,X_NEW,T45	T96 T66 T60 | X_NEW
L03	35	X_NEW,T83,T92	T66 T60 T90 | 

Line sequences (passC, for orientation only):
L01: T45 T33 T45 T83 T19 T95 X_NEW X_NEW T78 T63 T86 X_NEW T19 T58 T53 T96 T70 T25 T19 T83 T60 T80 T86 T83 T37 T85 T92 T66 T83 T63 T45
L02: T60 T45 T98 T25 T90 T97 T45 T65 T86 T76 T18 T45 T37 T36 T56 T37 T33 T45 T70 T86 T90 T80 T49 T85 T83 T25 T53 T19 T83 T60 T37
L03: T83 T45 T37 X_NEW X_S X_NEW T37 T92 T55 T65 T19 T85 T76 T63 T37 T83 T92 T45 T60 T45 T85 T46 T90 T53 T19 T58 T65 T52 T95 T25 T96 T66 T60 T90 X_NEW
