<!-- operator note (N7-LKTOOL, 4 Oct 2026): this prompt shows the committed label sequence and whole line crops; it drew
7/7 Sonnet re-reads that echoed passC on Vivonne inks 53/54 (voided). Prefer `windows` (per-tile crops, label hidden) or
--hide-passc, and treat a re-read that agrees with passC everywhere as an echo, not a confirmation. -->
# Proofreading audit, f52r_b (value-blind)

You are proofreading 60 signs of a symbol-cipher transcription against the manuscript. The reading below is what the
transcription currently says; some of it may be wrong. For each bracketed position, look at the sign in the line crop
and pick, from the listed candidate ids, the one whose shape it is -- whether or not it is the label the reading shows;
never copy a label from the reading.
You are never told what any sign means; do not guess letters or words.

Line crops (read these images; s1 = left half, s2 = right half of one line; halves overlap a little): /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L12_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L12_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L13_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L13_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L14_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L14_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L15_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L15_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L16_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L16_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L17_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L17_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L18_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L18_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L19_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L19_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L20_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L20_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L21_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L21_s2.jpg
Notation of the candidate labels (the transcription's own, shape names only):
  the number as written; a vowel sign written right after it: '+' small cross, '.' dot, 'ρ' looped e/p-like tail, 'σ' hook like a
  small 6 that is not clearly a digit, '⊣' u-like hook; a mark ABOVE the number: @n circumflex/hat ^, @s straight bar, @l short
  slanted acute stroke, @m wavy tilde, @r small v- or r-shaped hooked mark, @2 two dots; '_' underline; {y} or y the letter y;
  '/' slash; '-' or an empty candidate never appears: if the sign is not there at all (one reader saw a token that is not on the
  page), answer X_NEW with note 'absent'; if two tokens are written together as one group (or one group split), say so in note.
No candidate sheet exists for this hand: judge from the shapes as written.

Answer one TSV row per item, header: item<TAB>label<TAB>conf<TAB>second<TAB>note
  label  one of the item's candidates, X_NEW if none fits, or SPLIT:a|b if you cannot choose between two
  conf   H (clear), M (probable), L (guess); second = your runner-up id or empty; note = the shape feature you used.

Items (item, line, pos, candidates in random order, reading before | after):
1	L12	3	12.,23,23.	3 6ρ | 24+ 8σ 4@n
2	L18	17	7+@l,7+,7+@n	[28:23σ] 7ρ [15:4@n] | 
3	L19	2	4,4+,4.	24 | [10:25ρ@s] 36+ 8+
4	L17	24	11.,21.	18 [57:6.] 10 | 
5	L20	4	11.,21.	15σ 34ρ [50:23σ] | [46:6+] r 15.@s
6	L21	15	4@s,20+@s,14@s	[24:14+] [34:10] {bul} | 24+ x+ [14:29ρ]
7	L13	6	20+@s,14@s,4@s	[33:14+] 28@s 4@l | 24+ 6ρ 6.
8	L20	10	6+,6σ,6ρ	15.@s 18 3 | x. y 17ρ@s
9	L18	13	11.,21.	[45:22.] [54:28] 24ρ | [28:23σ] 7ρ [15:4@n]
10	L19	3	25ρ,12ρ@s,25ρ@s	24 [3:4] | 36+ 8+ [16:14ρ@s]
11	L19	18	20,20+,20.	16 1 7ρ | 
12	L21	1	55.	 | 23. 15. 12+
13	L13	14	28,128,28σ	23+@s [42:7ρ] [44:23+@s] | 15+ 7ρ@n 21
14	L21	18	29ρ,29σ	[6:4@s] 24+ x+ | /.
15	L18	16	4+@n,4@n,4@l	[9:21.] [28:23σ] 7ρ | [2:7+@n]
16	L19	6	14ρ@s	[10:25ρ@s] 36+ 8+ | [47:4+@n] [58:4@l] 23.
17	L16	16	28σ,128,28	3 [31:6ρ@s] x. | 24ρ 23
18	L15	7	28σ,28,128	6. 15+@r 24. | 21. 6 7
19	L15	14	231@s,23+,23+@s	15+ 23 7ρ | [32:6.] 26 6@s
20	L18	6	15ρ,12ρ,15σ	4 15ρ@2 23ρ | 4 [23:23.] 22
21	L14	14	1,15,11⊣	4@s 24ρ [51:6.] | 6. [27:10] 15+@n
22	L16	3	6,6.,6.@s	[39:27ρ@s] 20+ | 29 7+@n [59:42]
23	L18	8	23.,12.,23	23ρ [20:15ρ] 4 | 22 [45:22.] [54:28]
24	L21	12	11+,14+,1+	[55:15+] 18 x. | [34:10] {bul} [6:4@s]
25	L19	10	20,20.,20+	[47:4+@n] [58:4@l] 23. | [43:4] 6.@n 25.@r
26	L14	2	11.,21.	[29:4@n] | [40:23.] 20 4
27	L14	16	610,10,10.	[51:6.] [21:15] 6. | 15+@n 23ρ 24
28	L18	14	23ρ,23σ,6	[54:28] 24ρ [9:21.] | 7ρ [15:4@n] [2:7+@n]
29	L14	1	4+@n,4@n,4@l	 | [26:21.] [40:23.] 20
30	L20	19	/,/.,(.	8ρ@l 25.@r [41:23] | [49:11.] y+
31	L16	14	6ρ@s	14ρ [56:18] 3 | x. [17:28] 24ρ
32	L15	15	6,6.,6.@s	23 7ρ [19:23+@s] | 26 6@s 6ρ
33	L13	3	11+,14+,1+	2 0ρ@n | 28@s 4@l [7:4@s]
34	L21	13	10,610,10.	18 x. [24:14+] | {bul} [6:4@s] 24+
35	L12	8	7σ,77ρ,7ρ	8σ 4@n 21. | 6 6. 14+
36	L17	15	610,10,10.	6 6 r | x. 16. 6.
37	L15	2	13+,23+,231	20+ | 10 6. 15+@r
38	L17	1	28,128,28σ	 | 6ρ 23 7ρ@n
39	L16	1	27ρ@s	 | 20+ [22:6.] 29
40	L14	3	23.,23,12.	[29:4@n] [26:21.] | 20 4 6@n
41	L20	18	201,23.,23	6. 8ρ@l 25.@r | [30:/] [49:11.] y+
42	L13	12	7σ,7ρ,77ρ	6. 23@s 23+@s | [44:23+@s] [13:28] 15+
43	L19	11	4.,4,4+	[58:4@l] 23. [25:20.] | 6.@n 25.@r [52:4@n]
44	L13	13	23+,23+@s,231@s	23@s 23+@s [42:7ρ] | [13:28] 15+ 7ρ@n
45	L18	10	22.@s,22.,12.	4 [23:23.] 22 | [54:28] 24ρ [9:21.]
46	L20	5	16+,6+,36+	34ρ [50:23σ] [5:21.] | r 15.@s 18
47	L19	7	4@n,4+@n,4+	36+ 8+ [16:14ρ@s] | [58:4@l] 23. [25:20.]
48	L17	7	6.@s,6,6.	7ρ@n 21. 20ρ | r 10 7
49	L20	20	21.,11,11.	25.@r [41:23] [30:/] | y+
50	L20	3	23σ,6,23ρ	15σ 34ρ | [5:21.] [46:6+] r
51	L14	13	6.,6,6.@s	23σ 4@s 24ρ | [21:15] 6. [27:10]
52	L19	14	4@l,4+@n,4@n	[43:4] 6.@n 25.@r | 16 1 7ρ
53	L12	16	16.,.,20.@s	4@s 3 6+ | 24 [60:24.] 15.
54	L18	11	28σ,28,128	[23:23.] 22 [45:22.] | 24ρ [9:21.] [28:23σ]
55	L21	9	15+@n,15+,15+@s	7+ 6ρ 4@n | 18 x. [24:14+]
56	L16	12	18,1.,18@s	4@n 24. 14ρ | 3 [31:6ρ@s] x.
57	L17	22	6.@s,6,6.	6 6 18 | 10 [4:21.]
58	L19	8	4.@l,4,4@l	8+ [16:14ρ@s] [47:4+@n] | 23. [25:20.] [43:4]
59	L16	6	72,42	[22:6.] 29 7+@n | 28ρ 2 4@n
60	L12	18	24.,12.,24	6+ [53:.] 24 | 15. 10@n 24.

The reading (bracketed [item:label] = positions to audit):
L12: 3 6ρ [1:23.] 24+ 8σ 4@n 21. [35:7ρ] 6 6. 14+ 6σ 4@s 3 6+ [53:.] 24 [60:24.] 15. 10@n 24.
L13: 2 0ρ@n [33:14+] 28@s 4@l [7:4@s] 24+ 6ρ 6. 23@s 23+@s [42:7ρ] [44:23+@s] [13:28] 15+ 7ρ@n 21 23σ 18@n
L14: [29:4@n] [26:21.] [40:23.] 20 4 6@n 16. 24. r 23σ 4@s 24ρ [51:6.] [21:15] 6. [27:10] 15+@n 23ρ 24
L15: 20+ [37:23+] 10 6. 15+@r 24. [18:28] 21. 6 7 15+ 23 7ρ [19:23+@s] [32:6.] 26 6@s 6ρ 8+
L16: [39:27ρ@s] 20+ [22:6.] 29 7+@n [59:42] 28ρ 2 4@n 24. 14ρ [56:18] 3 [31:6ρ@s] x. [17:28] 24ρ 23
L17: [38:28] 6ρ 23 7ρ@n 21. 20ρ [48:6.] r 10 7 24 6 6 r [36:10] x. 16. 6. 6 6 18 [57:6.] 10 [4:21.]
L18: 15ρ@2 28 4 15ρ@2 23ρ [20:15ρ] 4 [23:23.] 22 [45:22.] [54:28] 24ρ [9:21.] [28:23σ] 7ρ [15:4@n] [2:7+@n]
L19: 24 [3:4] [10:25ρ@s] 36+ 8+ [16:14ρ@s] [47:4+@n] [58:4@l] 23. [25:20.] [43:4] 6.@n 25.@r [52:4@n] 16 1 7ρ [11:20.]
L20: 15σ 34ρ [50:23σ] [5:21.] [46:6+] r 15.@s 18 3 [8:6ρ] x. y 17ρ@s 6ρ@n 6. 8ρ@l 25.@r [41:23] [30:/] [49:11.] y+
L21: [12:55.] 23. 15. 12+ 12. 7+ 6ρ 4@n [55:15+] 18 x. [24:14+] [34:10] {bul} [6:4@s] 24+ x+ [14:29ρ] /.


Write the answer TSV (header + exactly 60 rows) to /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/lookalike/audit/f52r_b_audit_reread.tsv and reply only "done 60 rows".
