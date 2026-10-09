# Look-alike re-read, f52r_b (value-blind; ES132-LOOK, 9 Oct 2026, from tools/lookalike_pass.py packet --hide-passc)

You are re-reading 94 sign tiles of a 16th-century symbol-cipher transcription (numerals with small marks). Two earlier readers
disagreed on some of them, or gave a label that is often confused with another. You see only the line crops (s1 = left half,
s2 = right half of the same line; the halves overlap a little: do not count a token twice). You are never told what any sign
means; do not guess letters or words; do not try to decipher.

Line crops (read every one of these images with the Read tool before answering): /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L12_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L12_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L13_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L13_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L14_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L14_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L15_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L15_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L16_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L16_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L17_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L17_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L18_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L18_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L19_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L19_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L20_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L20_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L21_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L21_s2.jpg

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
Write the TSV (header + exactly 94 rows, same order) to /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/lookalike/calls/f52r_b_reread.tsv and reply only "done N rows".

Tiles (passage, pos, candidates, before | after):
L12	1	183,3,3@l	 | 6ρ 23. 24+
L12	2	36ρ,6+,6ρ,6σ	3 | 23. 24+ 8σ
L12	4	24,24+,x+	3 6ρ 23. | 8σ 4@n 21.
L12	6	4+@n,4@l,4@n	23. 24+ 8σ | 21. 7ρ 6
L12	7	11.,21.	24+ 8σ 4@n | 7ρ 6 6.
L12	8	77ρ,7ρ,7σ	8σ 4@n 21. | 6 6. 14+
L12	9	24σ,6,6.,7ρ	4@n 21. 7ρ | 6. 14+ 6σ
L12	12	16σ,6ρ,6σ	6 6. 14+ | 4@s 3 6+
L12	14	183,3,3@l	14+ 6σ 4@s | 6+ 16. 24
L12	15	16+,36+,6+	6σ 4@s 3 | 16. 24 24.
L12	17	24,24.,24.@n,26	3 6+ 16. | 24. 15. 10@n
L12	18	12.,24,24.	6+ 16. 24 | 15. 10@n 24.
L12	21	12.,24,24.	24. 15. 10@n | 
L13	1	2,2σ,7	 | 0ρ@n 14+ 28@s
L13	2	0ρ@n,20ρ@n	2 | 14+ 28@s 4@l
L13	7	24,24+,x+	28@s 4@l 4@s | 6ρ 6. 23@s
L13	8	6+,6ρ,6σ	4@l 4@s 24+ | 6. 23@s 23+@s
L13	11	23+,23+@s,231@s	6ρ 6. 23@s | 7ρ 23+@s 28
L13	12	77ρ,7ρ,7σ	6. 23@s 23+@s | 23+@s 28 15+
L13	15	15+,15+@n,15+@s	7ρ 23+@s 28 | 7ρ@n 21 23σ
L13	18	23ρ,23σ,6	15+ 7ρ@n 21 | 18@n
L14	2	11.,21.	4@n | 23. 20 4
L14	4	10,20,201	4@n 21. 23. | 4 6@n 16.
L14	5	201,4,4+,4.	21. 23. 20 | 6@n 16. 24.
L14	6	35σ@n,6.@n,6@n	23. 20 4 | 16. 24. r
L14	8	12.,24,24.	4 6@n 16. | r 23σ 4@s
L14	9	6,6.@r,r	6@n 16. 24. | 23σ 4@s 24ρ
L14	10	23ρ,23σ,6	16. 24. r | 4@s 24ρ 6.
L14	18	13ρ,23ρ,23σ	6. 10 15+@n | 24
L14	19	24,24.,24.@n,26	10 15+@n 23ρ | 
L15	2	13+,23+,231	20+ | 10 6. 15+@r
L15	5	15+,15+@l,15+@n,15+@r	23+ 10 6. | 24. 28 21.
L15	6	12.,24,24.	10 6. 15+@r | 28 21. 6
L15	8	11.,21.	15+@r 24. 28 | 6 7 15+
L15	9	24σ,6,6.	24. 28 21. | 7 15+ 23
L15	10	2,67,7,7ρ	28 21. 6 | 15+ 23 7ρ
L15	11	15+,15+@n,15+@s	21. 6 7 | 23 7ρ 23+@s
L15	13	77ρ,7ρ,7σ	7 15+ 23 | 23+@s 6. 26
L15	16	12σ,26,x	7ρ 23+@s 6. | 6@s 6ρ 8+
L15	17	26@s,6@s	23+@s 6. 26 | 6ρ 8+
L15	18	6+,6ρ,6σ,?ρ	6. 26 6@s | 8+
L16	8	2,2σ,7	7+@n 42 28ρ | 4@n 24. 14ρ
L16	9	4+@n,4@l,4@n	42 28ρ 2 | 24. 14ρ 18
L16	10	12.,24,24.	28ρ 2 4@n | 14ρ 18 3
L16	11	1+,14+,14ρ,7ρ	2 4@n 24. | 18 3 6ρ@s
L16	15	25.,r.,x.	18 3 6ρ@s | 28 24ρ 23
L16	17	24+,24ρ,24σ,26ρ	6ρ@s x. 28 | 23
L17	2	6+,6ρ,6σ,?ρ	28 | 23 7ρ@n 21.
L17	5	11.,21.	6ρ 23 7ρ@n | 20ρ 6. r
L17	8	6,6.@r,r	21. 20ρ 6. | 10 7 24
L17	10	2,7,7ρ	6. r 10 | 24 6 6
L17	11	24,24.,24.@n	r 10 7 | 6 6 r
L17	12	24σ,6,6.,74	10 7 24 | 6 r 10
L17	13	24σ,6,6.,6σ	7 24 6 | r 10 x.
L17	14	6,6.@r,r	24 6 6 | 10 x. 16.
L17	16	25.,r.,x.	6 r 10 | 16. 6. 6
L17	18	6,6.,6.@s	10 x. 16. | 6 6 18
L17	19	24σ,6,6.	x. 16. 6. | 6 18 6.
L17	20	24σ,6,6.,6_σ	16. 6. 6 | 18 6. 10
L17	24	11.,21.	18 6. 10 | 
L18	1	15ρ,15ρ@2,15ρ@s	 | 28 4 15ρ@2
L18	4	15ρ,15ρ@2,15ρ@s	15ρ@2 28 4 | 23ρ 15ρ 4
L18	5	13ρ,23ρ,23σ	28 4 15ρ@2 | 15ρ 4 23.
L18	6	12ρ,15ρ,15σ	4 15ρ@2 23ρ | 4 23. 22
L18	9	22,22+,22.@s	15ρ 4 23. | 22. 28 24ρ
L18	12	24+,24ρ,24σ,26ρ	22 22. 28 | 21. 23σ 7ρ
L18	13	11.,21.	22. 28 24ρ | 23σ 7ρ 4@n
L18	14	23ρ,23σ,6	28 24ρ 21. | 7ρ 4@n 7+@n
L18	15	77ρ,7ρ,7σ	24ρ 21. 23σ | 4@n 7+@n
L19	1	24,24.,24.@n,26+	 | 4 25ρ@s 36+
L19	12	6,6.,6.@n	23. 20. 4 | 25.@r 4@n 16
L19	13	.,25.,25.@r	20. 4 6.@n | 4@n 16 1
L19	15	10,16,161	6.@n 25.@r 4@n | 1 7ρ 20.
L19	16	1,1+,161	25.@r 4@n 16 | 7ρ 20.
L19	17	77ρ,7ρ,7σ	4@n 16 1 | 20.
L20	1	15ρ,15σ,18σ	 | 34ρ 23σ 21.
L20	3	23ρ,23σ,6	15σ 34ρ | 21. 6+ r
L20	4	11.,21.	15σ 34ρ 23σ | 6+ r 15.@s
L20	6	6,6.@r,r	23σ 21. 6+ | 15.@s 18 3
L20	8	1.,18,18@s	6+ r 15.@s | 3 6ρ x.
L20	9	183,3,3@l	r 15.@s 18 | 6ρ x. y
L20	10	6+,6ρ,6σ	15.@s 18 3 | x. y 17ρ@s
L20	11	25.,r.,x.	18 3 6ρ | y 17ρ@s 6ρ@n
L20	12	7,y,{y}	3 6ρ x. | 17ρ@s 6ρ@n 6.
L20	16	8ρ,8ρ@l	17ρ@s 6ρ@n 6. | 25.@r 23 /
L20	17	.,25.,25.@r	6ρ@n 6. 8ρ@l | 23 / 21.
L20	20	11.,21.	25.@r 23 / | y+
L20	21	7+,?4+,y+	23 / 21. | 
L21	7	6+,6ρ,6σ	12+ 12. 7+ | 4@n 15+ 18
L21	9	15+,15+@n,15+@s	7+ 6ρ 4@n | 18 x. 14+
L21	11	25.,r.,x.	4@n 15+ 18 | 14+ 10 {bul}
L21	16	24,24+,x+	10 {bul} 4@s | x+ 29ρ /.
L21	17	24+,25+,r+,x+	{bul} 4@s 24+ | 29ρ /.
L21	19	/,/.	24+ x+ 29ρ | 
