# Look-alike re-read, f179r (value-blind)

You are re-reading 31 sign tiles of a symbol-cipher transcription. Two earlier readers disagreed on some of them, or
gave a label that is often confused with another. You see only the line crops and a sheet of the candidate sign shapes,
labelled by id. You are never told what any sign means; do not guess letters or words.

Line crops (read these images): /home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/f179r/f179r_L01_s1.jpg, /home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/f179r/f179r_L01_s2.jpg, /home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/f179r/f179r_L01_s3.jpg, /home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/f179r/f179r_L02_s1.jpg, /home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/f179r/f179r_L02_s2.jpg, /home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/f179r/f179r_L02_s3.jpg, /home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/f179r/f179r_L03_s1.jpg, /home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/f179r/f179r_L03_s2.jpg, /home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/f179r/f179r_L03_s3.jpg, /home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/f179r/src_ark_12148_btv1b9060248g_f183_4800_1000_3000_620.jpg
Candidate sheet (ids only): /home/user/cipher-lab/ciphers/nevers-birago-fr3251-1572/harvest/lookalike_known/f179r_candidates.png

For each tile below, find the sign at that passage and position (the passC sequence of the line is given for
orientation; 'before'/'after' are the neighbouring labels) and pick the candidate id whose shape it is.
Answer one TSV row per tile, header: passage<TAB>pos<TAB>label<TAB>conf<TAB>second<TAB>note
  label  one of the tile's candidates, X_NEW if none fits, or SPLIT:a|b if you cannot choose between two
  conf   H (clear), M (probable), L (guess); second = your runner-up id or empty; note = the shape feature you used.

Tiles (passage, pos, candidates, before | after):
L01	1	T92,X_NEW,T50	 | T45 T58 T92
L01	4	T92,X_NEW,T50	T92 T45 T58 | T45 T56 T85
L01	9	T86,T60,T19	T56 T85 T33 | T57 T45 T37
L01	13	T24,X_NEW,T83,T29	T57 T45 T37 | T85 T83 T45
L01	15	T83,T24,X_NEW,T29	T37 T24 T85 | T45 T83 T45
L01	17	T83,T24,X_NEW,T29	T85 T83 T45 | T45 T53 T83
L01	20	T83,T24,X_NEW,T29	T83 T45 T53 | T45 T60 T36
L01	22	T60,T86	T53 T83 T45 | T36 T64 T96
L01	27	X_NEW,T83,T92	T64 T96 T37 | T86 T76 T65
L01	28	T86,T60,T19	T96 T37 X_NEW | T76 T65 T19
L02	1	T92,X_NEW,T50	 | T19 T90 T83
L02	3	T90,X_NEW,T45	T92 T19 | T83 T85 T88
L02	4	T83,T24,X_NEW,T29	T92 T19 T90 | T85 T88 T33
L02	8	T24,X_NEW,T83,T29	T85 T88 T33 | T92 T53 T37
L02	9	T92,X_NEW,T50	T88 T33 T24 | T53 T37 T70
L02	14	T60,T86	T37 T70 T45 | T53 T86 T58
L02	16	T86,T60,T19	T45 T60 T53 | T58 T37 T33
L02	22	T83,T24,X_NEW,T29	T33 T63 T37 | T45 T25 T90
L02	25	T90,X_NEW,T45	T83 T45 T25 | T80 T33 T65
L02	30	T92,X_NEW,T50	T33 T65 T19 | T53
L03	2	T98,T18,X_NEW	T19 | T81 T83 T80
L03	4	T83,T24,X_NEW,T29	T19 T98 T81 | T80 T70 T85
L03	8	T83,T24,X_NEW,T29	T80 T70 T85 | T92 T45 T76
L03	9	T92,X_NEW,T50	T70 T85 T83 | T45 T76 T45
L03	17	T83,T24,X_NEW,T29	T85 T58 T53 | T96 X_NEW T86
L03	19	X_NEW,T83,T92	T53 T83 T96 | T86 T60 T53
L03	20	T86,T60,T19	T83 T96 X_NEW | T60 T53 T80
L03	21	T60,T86	T96 X_NEW T86 | T53 T80 X_NEW
L03	24	X_NEW,T83,T92	T60 T53 T80 | X_NEW X_NEW T54
L03	25	X_NEW,T83,T92	T53 T80 X_NEW | X_NEW T54
L03	26	X_NEW,T83,T92	T80 X_NEW X_NEW | T54

Line sequences (passC, for orientation only):
L01: T92 T45 T58 T92 T45 T56 T85 T33 T86 T57 T45 T37 T24 T85 T83 T45 T83 T45 T53 T83 T45 T60 T36 T64 T96 T37 X_NEW T86 T76 T65 T19
L02: T92 T19 T90 T83 T85 T88 T33 T24 T92 T53 T37 T70 T45 T60 T53 T86 T58 T37 T33 T63 T37 T83 T45 T25 T90 T80 T33 T65 T19 T92 T53
L03: T19 T98 T81 T83 T80 T70 T85 T83 T92 T45 T76 T45 T89 T85 T58 T53 T83 T96 X_NEW T86 T60 T53 T80 X_NEW X_NEW X_NEW T54
