# Look-alike re-read, f51v_a (value-blind; ES132-LOOK, 9 Oct 2026, from tools/lookalike_pass.py packet --hide-passc)

You are re-reading 56 sign tiles of a 16th-century symbol-cipher transcription (numerals with small marks). Two earlier readers
disagreed on some of them, or gave a label that is often confused with another. You see only the line crops (s1 = left half,
s2 = right half of the same line; the halves overlap a little: do not count a token twice). You are never told what any sign
means; do not guess letters or words; do not try to decipher.

Line crops (read every one of these images with the Read tool before answering): /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L11_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L11_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L12_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L12_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L13_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L13_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L14_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L14_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L15_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L15_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L16_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L16_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L17_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L17_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L18_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L18_s2.jpg

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
Write the TSV (header + exactly 56 rows, same order) to /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/lookalike/calls/f51v_a_reread.tsv and reply only "done N rows".

Tiles (passage, pos, candidates, before | after):
L11	1	77ρ,7ρ,7σ	 | 231+@s y 68
L11	2	23+@s,231+@s	7ρ | y 68 20ρ@r
L11	3	7,y,{y}	7ρ 231+@s | 68 20ρ@r 7+@r
L11	4	368,68,68+,8	7ρ 231+@s y | 20ρ@r 7+@r 23+
L11	7	13+,23+,231	68 20ρ@r 7+@r | 28 r. 23
L11	9	26.,r.,x.	7+@r 23+ 28 | 23 20. 24ρ
L11	15	25.,25.@r,x.	24ρ 6. 10 | r 23 18
L11	16	25.@r,6,6.@r,r	6. 10 25. | 23 18
L12	4	23+,231,23⊣	4@s 24ρ 10 | 12.@r 16+ 12ρ
L12	9	1835+,35+,35ρ,5+	16+ 12ρ 28 | 21 24+@n 6ρ
L12	11	24+,24+@n,x+@n	28 35+ 21 | 6ρ 7σ@n 231@s
L12	12	6+,6ρ,6σ	35+ 21 24+@n | 7σ@n 231@s 21
L12	13	7ρ@n,7σ,7σ@n	21 24+@n 6ρ | 231@s 21 4@r
L12	14	23+@s,231@s	24+@n 6ρ 7σ@n | 21 4@r 29+
L13	3	24,24+,x+	6. 10 | 14+@r 15. 231@s
L13	6	23+@s,231@s	24+ 14+@r 15. | 6. 23σ 11
L13	8	23ρ,23σ,6	15. 231@s 6. | 11 17ρ@s 28ρ
L13	11	25ρ,28ρ,28σ,ρ	23σ 11 17ρ@s | 15. 10 281
L13	14	1,281	28ρ 15. 10 | 6+ r 610
L13	16	6,6.@r,r	10 281 6+ | 610 2
L13	17	10,610	281 6+ r | 2
L14	1	38ρ,6,71	 | 6σ r 610
L14	2	16σ,6ρ,6σ,x	71 | r 610 77ρ
L14	3	6,6.@r,r	71 6σ | 610 77ρ mρ
L14	4	10,610	71 6σ r | 77ρ mρ 23.
L14	5	77,77ρ,7ρ	6σ r 610 | mρ 23. 6.
L14	6	12ρ,mρ,nρ	r 610 77ρ | 23. 6. 37
L14	10	10,610	23. 6. 37 | 10 24+@l 6.
L14	12	24+,24+@l,24@l	37 610 10 | 6. 16ρ@n 3
L14	14	16ρ@n,6ρ@n	10 24+@l 6. | 3 6+ 7618
L14	17	1,7618	16ρ@n 3 6+ | 
L15	4	23+,231,23⊣	12. 7+ 20ρ@r | 20+@r 24 /
L15	6	24,24.,24.@n	20ρ@r 231 20+@r | / 28 4@n
L15	13	6+,6ρ,6σ	18ρ 23. 1@n | 6. 15 6.
L16	1	11,11.@s	 | 21. 28ρ 12ρ@l
L16	2	11.,21.	11.@s | 28ρ 12ρ@l 1
L16	5	1,1+,161	21. 28ρ 12ρ@l | 1+ r 610
L16	6	1,1+,14+,x	28ρ 12ρ@l 1 | r 610 21.
L16	7	6,6.@r,r	12ρ@l 1 1+ | 610 21. 4@l
L16	8	10,610	1 1+ r | 21. 4@l 6σ
L16	9	11.,21.	1+ r 610 | 4@l 6σ 7.
L16	11	16σ,6ρ,6σ	610 21. 4@l | 7. r. y
L16	12	22,7+,7.,7σ	21. 4@l 6σ | r. y 4@n
L16	13	26.,r.,x.	4@l 6σ 7. | y 4@n 24.@n
L16	14	7,y,{y}	6σ 7. r. | 4@n 24.@n 6σ
L16	17	16σ,6ρ,6σ	y 4@n 24.@n | 4 23
L17	2	15+,15+@n,15+@s	7ρ@n | 18 7+ 23σ
L17	5	23ρ,23σ,6	15+ 18 7+ | 18@n 6. 15+
L17	8	15+,15+@n,15+@s	23σ 18@n 6. | 7+ r 24+
L17	10	6,6.@r,r,x	6. 15+ 7+ | 24+ 21 15.
L17	11	24,24+,x+	15+ 7+ r | 21 15. h+
L17	18	183,3,3@l	25σ 10 3@s | 
L18	3	11.,21.	20 24ρ | 4 r+ 231
L18	5	r+,x+	24ρ 21. 4 | 231 14@n 24.@n
L18	6	23+,231,23⊣	21. 4 r+ | 14@n 24.@n 7σ
L18	16	11.,21.	17σ 16ρ 20ρ@r | 1
