# Look-alike re-read, f21v_L07-11 (value-blind)

You are re-reading 13 sign tiles of a symbol-cipher transcription. Two earlier readers disagreed on some of them, or
gave a label that is often confused with another. You see only the line crops and a sheet of the candidate sign shapes,
labelled by id. You are never told what any sign means; do not guess letters or words.

Line crops (read these images): /home/user/cipher-lab/ciphers/ceppo-nevers-fr3251-1570s/harvest/f21v/lookalike/crops/f21v_L01_band_pos1-18.jpg, /home/user/cipher-lab/ciphers/ceppo-nevers-fr3251-1570s/harvest/f21v/lookalike/crops/f21v_L03_band_pos1-18.jpg, /home/user/cipher-lab/ciphers/ceppo-nevers-fr3251-1570s/harvest/f21v/lookalike/crops/f21v_L07_10.jpg, /home/user/cipher-lab/ciphers/ceppo-nevers-fr3251-1570s/harvest/f21v/lookalike/crops/f21v_L07_27.jpg, /home/user/cipher-lab/ciphers/ceppo-nevers-fr3251-1570s/harvest/f21v/lookalike/crops/f21v_L07_7.jpg, /home/user/cipher-lab/ciphers/ceppo-nevers-fr3251-1570s/harvest/f21v/lookalike/crops/f21v_L09_1.jpg, /home/user/cipher-lab/ciphers/ceppo-nevers-fr3251-1570s/harvest/f21v/lookalike/crops/f21v_L09_17.jpg, /home/user/cipher-lab/ciphers/ceppo-nevers-fr3251-1570s/harvest/f21v/lookalike/crops/f21v_L09_6.jpg
Candidate sheet (ids only): /home/user/cipher-lab/ciphers/ceppo-nevers-fr3251-1570s/harvest/f21v/lookalike/f21v_L07-11_candidates.png

For each tile below, find the sign at that passage and position (the passC sequence of the line is given for
orientation; 'before'/'after' are the neighbouring labels) and pick the candidate id whose shape it is.
Answer one TSV row per tile, header: passage<TAB>pos<TAB>label<TAB>conf<TAB>second<TAB>note
  label  one of the tile's candidates, X_NEW if none fits, or SPLIT:a|b if you cannot choose between two
  conf   H (clear), M (probable), L (guess); second = your runner-up id or empty; note = the shape feature you used.

Tiles (passage, pos, candidates, before | after):
L07	10	S23,S97,S42	S97 S47 S80 | S53 S17 S20
L07	27	S23,S97,S42	S17 S53 S62 | X_POUND S75 S47
L07	34	X_NEW,S26,S10	S80 X_THETA2 S31 | 
L09	1	S23,S97,S42	 | S95 X_NEW S53
L09	3	X_NEW,S13,X_POUND	S23 S95 | S53 S80 S23
L09	5	S80,S65	S95 X_NEW S53 | S23 S53 S62
L09	6	S23,S97,S42	X_NEW S53 S80 | S53 S62 S89
L09	17	S23,S97,S42	X_POUND S52 S17 | S89 S17 S47
L10	6	S13,S69,S60	S37 S17 S62 | S52 S74 S53
L11	2	X_NEW,S25,X_POUND,S13	S53 | S74 S69 S97
L11	4	S13,S69,S60	S53 X_NEW S74 | S97 S53 S88
L11	9	S80,S65	S53 S88 S62 | S84 X_NEW S75
L11	22	S13,S69,S60	S97 S89 S17 | S17 S37 S47

Line sequences (passC, for orientation only):
L07: X_THETA2 S80 S23 S62 X_THETA2 S75 S97 S47 S80 S23 S53 S17 S20 S47 S80 X_POUND S37 S61 S75 S23 S80 X_THETA2 S53 S17 S53 S62 S23 X_POUND S75 S47 S80 X_THETA2 S31 S26
L08.1: S17 S20 S47 S80
L08.2: S80
L09: S23 S95 X_NEW S53 S80 S23 S53 S62 S89 S17 S23 S80 X_THETA2 X_POUND S52 S17 S23 S89 S17 S47 S52 X_THETA2 S66 S35 S37 S88 X_NEW S52
L10: S67 S80 S37 S17 S62 S69 S52 S74 S53 S17 X_NEW S75
L11: S53 X_NEW S74 S69 S97 S53 S88 S62 S65 S84 X_NEW S75 X_THETA2 S80 S74 S75 S73 S95 S97 S89 S17 S69 S17 S37 S47 X_POUND S53 S80
