# Look-alike re-read, f52r_a (value-blind; ES132-LOOK, 9 Oct 2026, from tools/lookalike_pass.py packet --hide-passc)

You are re-reading 92 sign tiles of a 16th-century symbol-cipher transcription (numerals with small marks). Two earlier readers
disagreed on some of them, or gave a label that is often confused with another. You see only the line crops (s1 = left half,
s2 = right half of the same line; the halves overlap a little: do not count a token twice). You are never told what any sign
means; do not guess letters or words; do not try to decipher.

Line crops (read every one of these images with the Read tool before answering): /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L01_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L01_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L02_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L02_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L03_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L03_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L04_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L04_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L05_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L05_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L06_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L06_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L07_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L07_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L08_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L08_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L09_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L09_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L10_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L10_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L11_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L11_s2.jpg

Notation of the candidate labels (the transcription's own, shape names only):
  the number as written; a vowel sign written right after it: '+' small cross, '.' dot, 'ρ' looped e/p-like tail, 'σ' hook like a
  small 6 that is not clearly a digit, '⊣' u-like hook; a mark ABOVE the number: @n circumflex/hat ^, @s straight bar, @l short
  slanted acute stroke, @m wavy tilde, @r small v- or r-shaped hooked mark, @2 two dots; '_' underline; {y} or y the letter y;
  '/' slash; '-' or an empty candidate never appears: if the sign is not there at all (one reader saw a token that is not on the
  page), answer X_NEW with note 'absent'; if two tokens are written together as one group (or one group split), say so in note.

For each tile below, find the token at that line and position ('pos' counts tokens from the left of the line; it may be off by one
or two, so use the 'before'/'after' neighbouring labels to find it) and pick the candidate whose shape it is. Candidates are in
alphabetical order. Labels shown anywhere here are earlier readers' and may be wrong: judge the shape in the image, never copy a label.
Answer one TSV row per tile, header: passage<TAB>pos<TAB>label<TAB>conf<TAB>second<TAB>note
  label  one of the tile's candidates, X_NEW if none fits, or SPLIT:a|b if you cannot choose between two
  conf   H (clear), M (probable), L (guess); second = your runner-up or empty; note = the shape feature you used.
Write the TSV (header + exactly 92 rows, same order) to /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/lookalike/calls/f52r_a_reread.tsv and reply only "done N rows".

Tiles (passage, pos, candidates, before | after):
L01	3	1,1+,14@l,161	20ρ@r 24+@n | 20+@r 24+@n 24.
L01	4	20+,20+@r	20ρ@r 24+@n 1 | 24+@n 24. 28
L01	6	12.,24,24.	1 20+@r 24+@n | 28 7ρ@n 29.
L01	11	24σ,6,6.	7ρ@n 29. 26 | 4@n 24. 20+
L01	13	12.,24,24.	26 6 4@n | 20+ 24+ 4@l
L01	15	24,24+,25+,x+	4@n 24. 20+ | 4@l 8. 24.
L01	18	12.,24,24.,26.	24+ 4@l 8. | 
L02	7	77ρ,7ρ,7σ	6. 16σ 23 | 23+@s 28 6.
L02	11	15+,15+@n,15+@s	23+@s 28 6. | 73 6. 23+
L02	14	13+,23+,231	15+ 73 6. | 7ρ 24+ (.
L02	15	77ρ,7ρ,7σ	73 6. 23+ | 24+ (.
L02	16	24,24+,26+,x+	6. 23+ 7ρ | (.
L02	17	(.,/	23+ 7ρ 24+ | 
L03	2	11.,21.	12. | 26 6ρ 10
L03	4	6+,6ρ,6σ	12. 21. 26 | 10 25 6
L03	11	12ρ,15ρ,15σ	23+@r 18@s 6. | 21. 4@n 4@s
L03	12	11.,21.	18@s 6. 15ρ | 4@n 4@s 24ρ
L03	18	13+,23+,231	24ρ 12+ 20+ | 6ρ
L03	19	6+,6ρ,6σ	12+ 20+ 23+ | 
L04	3	2,7,7ρ	7ρ@n 4@l | 26. 18 21.
L04	6	11.,21.	7 26. 18 | 12+ 6σ 7ρ
L04	8	16σ,6ρ,6σ	18 21. 12+ | 7ρ 6. 23
L04	9	77ρ,7ρ,7σ	21. 12+ 6σ | 6. 23 23
L04	11	201,23,23.	6σ 7ρ 6. | 23 20+ 7+
L04	15	15+,15+@n,15+@s	23 20+ 7+ | 4 1+ 7ρ@n
L04	17	1,1+,14+,14ρ	7+ 15+ 4 | 7ρ@n 15+ 24.
L04	19	15+,15+@n,15+@s	4 1+ 7ρ@n | 24. 23
L04	20	12.,24,24.,26.	1+ 7ρ@n 15+ | 23
L05	1	10,20,201	 | 4@s 24+ 6.
L05	3	24,24+,x+	20 4@s | 6. 24ρ 6ρ
L05	6	6+,6ρ,6σ	24+ 6. 24ρ | 4@s 24ρ 20+
L05	10	24,24+,25+,x+	4@s 24ρ 20+ | 21. 4@s 24.
L05	11	11.,21.	24ρ 20+ 24+ | 4@s 24. 28@s
L05	13	12.,24,24.	24+ 21. 4@s | 28@s 35. 25.
L05	18	6+,6ρ,6σ	35. 25. 26 | 
L06	3	24,24+,25+,x+	28 20+ | 21. 23σ 36+
L06	4	11.,21.	28 20+ 24+ | 23σ 36+ 24+
L06	5	23ρ,23σ,6	20+ 24+ 21. | 36+ 24+ r.
L06	7	24,24+,x+	21. 23σ 36+ | r. 24 7ρ@n
L06	8	26.,r.,x.	23σ 36+ 24+ | 24 7ρ@n 25ρ@s
L06	9	24,24.,24.@n,26	36+ 24+ r. | 7ρ@n 25ρ@s 23ρ
L06	12	13ρ,23ρ,23σ	24 7ρ@n 25ρ@s | 30. 15+ 16+
L06	14	15+,15+@n,15+@s	25ρ@s 23ρ 30. | 16+ 24@l 6
L06	16	24,24+@l,24@l	30. 15+ 16+ | 6 10
L06	17	24σ,25@l,6,6.	15+ 16+ 24@l | 10
L07	5	77ρ,7ρ,7σ	20+ 28 23 | 10 25. y
L07	8	7,y,{y}	7ρ 10 25. | 23 6. 35+
L07	14	6,6.@r,r	35+ 7. 6. | 21. 12+ 6.
L07	15	11.,21.	7. 6. r | 12+ 6. 23@r
L07	20	15+,15+@n,15+@s	6. 23@r 4@n | 
L08	1	10,16,161	 | 6 23 16+
L08	2	16σ,24σ,6,6.	16 | 23 16+ 2ρ
L08	6	16+,26+,36+,6+	23 16+ 2ρ | (.
L08	7	(.,/	16+ 2ρ 6+ | 
L09	2	24,24+,26+,x+	25 | 7ρ 23+ 23.
L09	3	77ρ,7ρ,7σ	25 24+ | 23+ 23. 24
L09	4	13+,23+,231	25 24+ 7ρ | 23. 24 8σ
L09	6	24,24.,24.@n	7ρ 23+ 23. | 8σ 4@l 12.
L09	10	10,10.,610	8σ 4@l 12. | 10 6 25
L09	14	6,6@r	10 6 25 | 24+ y@s 21.
L09	15	24,24+,x+	6 25 6@r | y@s 21. 4@n
L09	16	?@s,y@s	25 6@r 24+ | 21. 4@n 4@l
L09	17	11.,21.	6@r 24+ y@s | 4@n 4@l 6σ
L09	20	16σ,6ρ,6σ	21. 4@n 4@l | 23 7@r 23ρ
L09	23	13ρ,23ρ,23σ	6σ 23 7@r | 
L10	2	15+,15+@2,15+@s	6. | 35+ 24 6
L10	4	24,24.,24.@n	6. 15+@s 35+ | 6 7+ 23
L10	5	24σ,6,6.	15+@s 35+ 24 | 7+ 23 21
L10	9	24,24.,24.@n	7+ 23 21 | 25 6 4
L10	10	15,23,241,25	23 21 24 | 6 4 r.
L10	11	24σ,25σ,6,6.	21 24 25 | 4 r. 6.
L10	13	26.,?.,r.,x.	25 6 4 | 6. 23 23ρ
L10	16	13ρ,23ρ,23σ	r. 6. 23 | 30. 4@s 24+
L10	19	24,24+,x+	23ρ 30. 4@s | 16+ 24.
L10	21	12.,24,24.	4@s 24+ 16+ | 
L11	1	12σ,26,x	 | 6 10@s 7ρ@n
L11	2	24σ,25,6,6.	26 | 10@s 7ρ@n 15+
L11	5	15+,15+@n,15+@s	6 10@s 7ρ@n | 26. y 24+
L11	6	24.,25.,26.	10@s 7ρ@n 15+ | y 24+ 16+
L11	7	7,y,{y}	7ρ@n 15+ 26. | 24+ 16+ 6.
L11	8	24,24+,26+,x+	15+ 26. y | 16+ 6. 6.
L11	10	6,6.,6.@s	y 24+ 16+ | 6. 26. 18
L11	11	/,6,6.,6.@s	24+ 16+ 6. | 26. 18 7ρ@n
L11	12	24.,25.,26.	16+ 6. 6. | 18 7ρ@n 10@l
L11	15	10@l,10@n	26. 18 7ρ@n | 14@n 18 3
L11	17	1.,18,18@s	7ρ@n 10@l 14@n | 3 6ρ 16
L11	18	183,3,3@l	10@l 14@n 18 | 6ρ 16 6
L11	19	6+,6ρ,6σ	14@n 18 3 | 16 6 24
L11	20	10,16,161	18 3 6ρ | 6 24 6
L11	21	24σ,6,6.	3 6ρ 16 | 24 6
L11	22	16σ,24,24.,24.@n	6ρ 16 6 | 6
L11	23	24σ,26,6,6.	16 6 24 | 
