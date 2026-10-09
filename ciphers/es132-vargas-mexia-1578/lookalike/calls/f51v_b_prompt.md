# Look-alike re-read, f51v_b (value-blind; ES132-LOOK, 9 Oct 2026, from tools/lookalike_pass.py packet --hide-passc)

You are re-reading 49 sign tiles of a 16th-century symbol-cipher transcription (numerals with small marks). Two earlier readers
disagreed on some of them, or gave a label that is often confused with another. You see only the line crops (s1 = left half,
s2 = right half of the same line; the halves overlap a little: do not count a token twice). You are never told what any sign
means; do not guess letters or words; do not try to decipher.

Line crops (read every one of these images with the Read tool before answering): /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L19_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L19_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L20_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L20_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L21_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L21_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L22_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L22_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L23_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L23_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L24_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L24_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L25_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L25_s2.jpg

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
Write the TSV (header + exactly 49 rows, same order) to /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/lookalike/calls/f51v_b_reread.tsv and reply only "done N rows".

Tiles (passage, pos, candidates, before | after):
L19	11	15+,15+@n,15+@r	23+@m 10 6. | 24. 4@n 4@s
L19	12	12.,24,24.	10 6. 15+@n | 4@n 4@s 24.
L19	15	12.,24,24.	24. 4@n 4@s | n. 11ρ 7
L19	18	2,7,7ρ	24. n. 11ρ | 
L20	1	7,y,{y}	 | 7ρ@n 4@s 24ρ
L20	11	16σ,6ρ,6σ	25σ 18 4@l | 7ρ {bul} 16
L20	12	77ρ,7ρ,7σ	18 4@l 6σ | {bul} 16 1
L20	17	77ρ,7ρ,7σ	16 1 28 | 24.@n 24+
L20	19	24,24+,x+	28 7ρ 24.@n | 
L21	1	13+,23+,231	 | 24σ 23 2.
L21	2	24ρ,24σ,6	23+ | 23 2. 7ρ
L21	5	77ρ,7ρ,7σ	24σ 23 2. | 6 15+ r.
L21	7	15+,15+@n,15+@s	2. 7ρ 6 | r. 23 201
L21	8	26.,r.,x.	7ρ 6 15+ | 23 201 4@s
L21	10	1,20+,201	15+ r. 23 | 4@s 24+ 14
L21	12	24,24+,x+	23 201 4@s | 14 33. 7σ
L21	17	6+,6ρ,6σ	33. 7σ 4@n | 6. 1
L22	1	16,29.@r,29σ@r	 | 161 28 814
L22	2	1,16,161	29.@r | 28 814 nρ@s
L22	4	4,814	29.@r 161 28 | nρ@s 18 26
L22	8	18@s,7618@s	nρ@s 18 26 | 7ρ@n 231 101
L22	10	10,23+,231,23⊣	26 7618@s 7ρ@n | 101 6ρ 102
L22	11	1,101	7618@s 7ρ@n 231 | 6ρ 102 362
L22	12	6+,6ρ,6σ	7ρ@n 231 101 | 102 362 368
L22	13	102,6	231 101 6ρ | 362 368
L22	14	23,362	101 6ρ 102 | 368
L22	15	368,68	6ρ 102 362 | 
L23	2	6+,6ρ,6σ	15ρ@s | 20@n 1 24ρ@s
L23	7	11.,21.	1 24ρ@s 4@n | 16. 12+ 29σ
L23	10	29,29ρ,29σ,6	21. 16. 12+ | 10 12+ 30_
L23	14	6+,6ρ,6σ	10 12+ 30_ | 77ρ 7ρ 20
L23	15	77,77ρ,7ρ	12+ 30_ 6ρ | 7ρ 20
L23	16	77ρ,7ρ,7σ,nρ	30_ 6ρ 77ρ | 20
L24	1	11.,21.	 | 7ρ@n 15+ 18
L24	3	15+,15+@n,15+@s	21. 7ρ@n | 18 7+ 23σ
L24	6	23ρ,23σ,6	15+ 18 7+ | 18@n 6. 15ρ@s
L24	11	70ρ@n,77@n,7ρ@n,m.@n	6. 15ρ@s 23. | 3+ 23. 10
L24	15	36+,6+	3+ 23. 10 | 8+ 1
L25	1	11.,21.	 | 15+ 10 16σ
L25	2	15+,15+@n,15+@s	21. | 10 16σ 23
L25	4	16ρ,16σ,6σ	21. 15+ 10 | 23 24+ 6
L25	6	24,24+,x+	10 16σ 23 | 6 21. 4@l
L25	8	11.,21.	23 24+ 6 | 4@l 35ρ 201
L25	10	1,35+,35ρ	6 21. 4@l | 201 23ρ 15ρ@s
L25	11	1,20+,201,23	21. 4@l 35ρ | 23ρ 15ρ@s 18
L25	12	13ρ,23ρ,23σ,5ρ	4@l 35ρ 201 | 15ρ@s 18 36+@s
L25	15	3,36+@s	23ρ 15ρ@s 18 | 6 6 10
L25	16	24σ,6,6+@s,6.	15ρ@s 18 36+@s | 6 10
L25	17	24σ,6,6.,6σ	18 36+@s 6 | 10
