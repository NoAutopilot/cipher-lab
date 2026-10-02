# Look-alike re-read, f21v_L01-06 (value-blind)

You are re-reading 27 sign tiles of a symbol-cipher transcription. Two earlier readers disagreed on some of them, or
gave a label that is often confused with another. You see only the line crops and a sheet of the candidate sign shapes,
labelled by id. You are never told what any sign means; do not guess letters or words.

Line crops (read these images): /home/user/cipher-lab/ciphers/ceppo-nevers-fr3251-1570s/harvest/f21v/lookalike/crops/f21v_L01_band_pos1-18.jpg, /home/user/cipher-lab/ciphers/ceppo-nevers-fr3251-1570s/harvest/f21v/lookalike/crops/f21v_L03_band_pos1-18.jpg, /home/user/cipher-lab/ciphers/ceppo-nevers-fr3251-1570s/harvest/f21v/lookalike/crops/f21v_L07_10.jpg, /home/user/cipher-lab/ciphers/ceppo-nevers-fr3251-1570s/harvest/f21v/lookalike/crops/f21v_L07_27.jpg, /home/user/cipher-lab/ciphers/ceppo-nevers-fr3251-1570s/harvest/f21v/lookalike/crops/f21v_L07_7.jpg, /home/user/cipher-lab/ciphers/ceppo-nevers-fr3251-1570s/harvest/f21v/lookalike/crops/f21v_L09_1.jpg, /home/user/cipher-lab/ciphers/ceppo-nevers-fr3251-1570s/harvest/f21v/lookalike/crops/f21v_L09_17.jpg, /home/user/cipher-lab/ciphers/ceppo-nevers-fr3251-1570s/harvest/f21v/lookalike/crops/f21v_L09_6.jpg
Candidate sheet (ids only): /home/user/cipher-lab/ciphers/ceppo-nevers-fr3251-1570s/harvest/f21v/lookalike/f21v_L01-06_candidates.png

For each tile below, find the sign at that passage and position (the passC sequence of the line is given for
orientation; 'before'/'after' are the neighbouring labels) and pick the candidate id whose shape it is.
Answer one TSV row per tile, header: passage<TAB>pos<TAB>label<TAB>conf<TAB>second<TAB>note
  label  one of the tile's candidates, X_NEW if none fits, or SPLIT:a|b if you cannot choose between two
  conf   H (clear), M (probable), L (guess); second = your runner-up id or empty; note = the shape feature you used.

Tiles (passage, pos, candidates, before | after):
L01	3	S74,S77	S84 S75 | S80 S37 S97
L01	4	S65,S80	S84 S75 S77 | S37 S97 S67
L01	10	S65,S80	S67 S56 S89 | S61 S52 S23
L01	11	S61,S94	S56 S89 S80 | S52 S23 S75
L01	15	S49,S73	S52 S23 S75 | S94 S35 S89
L01	27	S65,S80	S88 S62 S89 | S52 S74 S35
L02.2	2	S65,S80	S61 | 
L03	7	S49,S73	S94 S75 S17 | S53 S75 S49
L03	10	S49,S73	S49 S53 S75 | S37 S93 S62
L03	14	S49,S73	S37 S93 S62 | S75 S74 S62
L03	20	S65,S80	S62 S57 S88 | S20 S47 S75
L03	24	S26,S10	S20 S47 S75 | S53 S80 S37
L03	26	S65,S80	S75 S10 S53 | S37 S80 S56
L03	28	S65,S80	S53 S80 S37 | S56 S17 S37
L03	34	S65,S80	S37 S97 S94 | S89 S93 S25
L03	39	S65,S80	S93 S25 S47 | 
L04	10	S26,S10	S52 S23 S75 | S17 S23 S75
L04	15	S26,S10	S23 S75 S56 | S47 S80 S89
L04	17	S65,S80	S56 S10 S47 | S89
L05	7	S26,S10	S84 S23 S62 | S75 S56 X_POUND
L05	13	S40,S32,S25	X_POUND S93 S74 | S66 S75 S89
L05	28	S26,S10	S62 S52 S53 | S75 S56 S47
L06.2	1	S65,S80	 | S47 S97 S23
L06.2	6	S65,S80	S97 S23 S95 | S56 S31 S17
L06.2	12	S60,S69,X_THETA2	S17 S23 S62 | S80 S62 S13
L06.2	13	S65,S80	S23 S62 X_THETA2 | S62 S13
L06.2	15	S13,S69,X_NEW	X_THETA2 S80 S62 | 

Line sequences (passC, for orientation only):
L01: S84 S75 S77 S80 S37 S97 S67 S56 S89 S80 S61 S52 S23 S75 S49 S94 S35 S89 S75 X_POUND S53 S47 S53 S88 S62 S89 S80 S52 S74 S35 S52 S65 S52 S53 S66 S93 S23 S56 S75
L02.1: S47 S57 S88 S23 S75 S89 S17 X_POUND S62 S56 S88
L02.2: S61 S80
L03: S56 S97 S23 S94 S75 S17 S49 S53 S75 S49 S37 S93 S62 S49 S75 S74 S62 S57 S88 S80 S20 S47 S75 S10 S53 S80 S37 S80 S56 S17 S37 S97 S94 S80 S89 S93 S25 S47 S80
L04: S37 S56 S75 S89 S62 S84 S52 S23 S75 S10 S17 S23 S75 S56 S10 S47 S80 S89
L05: S37 S17 S62 S84 S23 S62 S10 S75 S56 X_POUND S93 S74 S40 S66 S75 S89 S52 S56 S47 S17 S47 S75 S23 S89 S62 S52 S53 S10 S75 S56 S47 S75 S23 S89
L06.1: S17 S62
L06.2: S80 S47 S97 S23 S95 S80 S56 S31 S17 S23 S62 X_THETA2 S80 S62 S13
