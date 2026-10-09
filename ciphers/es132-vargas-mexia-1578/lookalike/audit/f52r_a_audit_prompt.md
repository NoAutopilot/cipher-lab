<!-- operator note (N7-LKTOOL, 4 Oct 2026): this prompt shows the committed label sequence and whole line crops; it drew
7/7 Sonnet re-reads that echoed passC on Vivonne inks 53/54 (voided). Prefer `windows` (per-tile crops, label hidden) or
--hide-passc, and treat a re-read that agrees with passC everywhere as an echo, not a confirmation. -->
# Proofreading audit, f52r_a (value-blind)

You are proofreading 60 signs of a symbol-cipher transcription against the manuscript. The reading below is what the
transcription currently says; some of it may be wrong. For each bracketed position, look at the sign in the line crop
and pick, from the listed candidate ids, the one whose shape it is -- whether or not it is the label the reading shows;
never copy a label from the reading.
You are never told what any sign means; do not guess letters or words.

Line crops (read these images; s1 = left half, s2 = right half of one line; halves overlap a little): /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L01_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L01_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L02_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L02_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L03_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L03_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L04_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L04_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L05_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L05_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L06_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L06_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L07_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L07_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L08_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L08_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L09_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L09_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L10_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L10_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L11_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f52r_L11_s2.jpg
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
1	L09	19	4,4.@l,4@l	y@s [29:21.] [43:4+@n] | [25:6σ] 23 7@r
2	L04	4	25.,24.,26.	[8:7ρ@n] [30:4@l] 7 | [22:18] 21. 12+
3	L02	5	6σ,16ρ,16σ	[48:7σ] [31:18] 6. | [60:23] 7ρ 23+@s
4	L11	4	70ρ@n,77@n,7ρ@n	26 6 [37:10@s] | [14:15+] 26. y
5	L01	7	28σ,28,128	20+@r 24+@n 24. | 7ρ@n [16:29.] 26
6	L04	10	6.,6.@s,6	12+ 6σ 7ρ | 23 23 20+
7	L09	1	23,25,15	 | 24+ [56:7ρ] 23+
8	L04	1	70ρ@n,77@n,7ρ@n	 | [30:4@l] 7 [2:26.]
9	L10	14	6,6.,6.@s	6 4 r. | 23 23ρ 30.
10	L05	12	20+@s,14@s,4@s	20+ 24+ 21. | [57:24.] 28@s [47:35.]
11	L01	2	24+@n,x+@n,24+	20ρ@r | 1 20+@r 24+@n
12	L05	2	14@s,4@s,20+@s	20 | [49:24+] 6. [27:24ρ]
13	L04	18	70ρ@n,7ρ@n,77@n	15+ 4 1+ | [15:15+] 24. 23
14	L11	5	15+,15+@n,15+@s	6 [37:10@s] [4:7ρ@n] | 26. y 24+
15	L04	19	15+@s,15+,15+@n	4 1+ [13:7ρ@n] | 24. 23
16	L01	9	29,29.	24. [5:28] 7ρ@n | 26 6 [24:4@n]
17	L08	4	16+@s,16+,6+	16 6 23 | 2ρ 6+ (.
18	L05	18	6σ,6ρ,6+	[47:35.] [20:x.] 26 | 
19	L07	1	23,23.,12.	 | 20+ 28 23
20	L05	16	r.,x.,25.	[57:24.] 28@s [47:35.] | 26 [18:6ρ]
21	L06	15	16+,16+@s,6+	23ρ [36:30.] [42:15+] | 24@l 6 10
22	L04	5	18@s,18,1.	[30:4@l] 7 [2:26.] | 21. 12+ 6σ
23	L10	3	35ρ,35+,1835+	[28:6.] 15+@s | 24 6 7+
24	L01	12	4@n,4+@n,4@l	[16:29.] 26 6 | 24. [38:20+] 24+
25	L09	20	16σ,6ρ,6σ	[29:21.] [43:4+@n] [1:4@l] | 23 7@r 23ρ
26	L09	6	24,24.,12.	[56:7ρ] 23+ 23. | [39:8σ] [45:4@l] 12.
27	L05	5	24+,24ρ,24σ	[12:4@s] [49:24+] 6. | 6ρ 4@s 24ρ
28	L10	1	6.,6.@s,6	 | 15+@s [23:35+] 24
29	L09	17	21.,11.	6@r 24+ y@s | [43:4+@n] [1:4@l] [25:6σ]
30	L04	2	4,4.@l,4@l	[8:7ρ@n] | 7 [2:26.] [22:18]
31	L02	3	1.,18,18@s	26 [48:7σ] | 6. [3:16σ] [60:23]
32	L03	4	6+,6ρ,6σ	12. 21. [55:26] | [51:10] 25 6
33	L06	11	25ρ,25ρ@s,12ρ@s	r. 24 7ρ@n | 23ρ [36:30.] [42:15+]
34	L09	13	15,25,23	10 10 6 | 6@r 24+ y@s
35	L03	18	231,23+,13+	24ρ 12+ 20+ | 6ρ
36	L06	13	30.,30_.	7ρ@n [33:25ρ@s] 23ρ | [42:15+] [21:16+] 24@l
37	L11	3	10,10@s	26 6 | [4:7ρ@n] [14:15+] 26.
38	L01	14	20⊣,201,20+	6 [24:4@n] 24. | 24+ 4@l 8.
39	L09	7	88,38,8σ	23+ 23. [26:24.] | [45:4@l] 12. 10
40	L06	4	21.,11.	28 [50:20+] 24+ | 23σ 36+ 24+
41	L07	11	35+,1835+,35ρ	y 23 6. | 7. 6. r
42	L06	14	15+@n,15+@s,15+	[33:25ρ@s] 23ρ [36:30.] | [21:16+] 24@l 6
43	L09	18	4+,4+@n,4@n	24+ y@s [29:21.] | [1:4@l] [25:6σ] 23
44	L03	8	23+@m,23+@r	[51:10] 25 6 | 18@s 6. 15ρ
45	L09	8	4,4@l,4.@l	23. [26:24.] [39:8σ] | 12. 10 10
46	L07	15	21.,11.	7. 6. r | 12+ 6. [53:23@r]
47	L05	15	35.	[10:4@s] [57:24.] 28@s | [20:x.] 26 [18:6ρ]
48	L02	2	7σ,7ρ,7	26 | [31:18] 6. [3:16σ]
49	L05	3	24,x+,24+	20 [12:4@s] | 6. [27:24ρ] 6ρ
50	L06	2	201,20⊣,20+	28 | 24+ [40:21.] 23σ
51	L03	5	610,10,10.	21. [55:26] [32:6ρ] | 25 6 [44:23+@r]
52	L11	19	6ρ,6+,6σ	14@n 18 3 | 16 6 24
53	L07	18	23@r	[46:21.] 12+ 6. | 4@n 15+
54	L02	10	6,6.@s,6.	7ρ 23+@s [59:28] | 15+ 73 6.
55	L03	3	26,x,12σ	12. 21. | [32:6ρ] [51:10] 25
56	L09	3	77ρ,7ρ,7σ	[7:25] 24+ | 23+ 23. [26:24.]
57	L05	13	24,24.,12.	24+ 21. [10:4@s] | 28@s [47:35.] [20:x.]
58	L03	12	11.,21.	18@s 6. 15ρ | 4@n 4@s 24ρ
59	L02	9	28,128,28σ	[60:23] 7ρ 23+@s | [54:6.] 15+ 73
60	L02	6	23,201,23.	[31:18] 6. [3:16σ] | 7ρ 23+@s [59:28]

The reading (bracketed [item:label] = positions to audit):
L01: 20ρ@r [11:24+@n] 1 20+@r 24+@n 24. [5:28] 7ρ@n [16:29.] 26 6 [24:4@n] 24. [38:20+] 24+ 4@l 8. 24.
L02: 26 [48:7σ] [31:18] 6. [3:16σ] [60:23] 7ρ 23+@s [59:28] [54:6.] 15+ 73 6. 23+ 7ρ 24+ (.
L03: 12. 21. [55:26] [32:6ρ] [51:10] 25 6 [44:23+@r] 18@s 6. 15ρ [58:21.] 4@n 4@s 24ρ 12+ 20+ [35:23+] 6ρ
L04: [8:7ρ@n] [30:4@l] 7 [2:26.] [22:18] 21. 12+ 6σ 7ρ [6:6.] 23 23 20+ 7+ 15+ 4 1+ [13:7ρ@n] [15:15+] 24. 23
L05: 20 [12:4@s] [49:24+] 6. [27:24ρ] 6ρ 4@s 24ρ 20+ 24+ 21. [10:4@s] [57:24.] 28@s [47:35.] [20:x.] 26 [18:6ρ]
L06: 28 [50:20+] 24+ [40:21.] 23σ 36+ 24+ r. 24 7ρ@n [33:25ρ@s] 23ρ [36:30.] [42:15+] [21:16+] 24@l 6 10
L07: [19:23.] 20+ 28 23 7ρ 10 25. y 23 6. [41:35+] 7. 6. r [46:21.] 12+ 6. [53:23@r] 4@n 15+
L08: 16 6 23 [17:16+] 2ρ 6+ (.
L09: [7:25] 24+ [56:7ρ] 23+ 23. [26:24.] [39:8σ] [45:4@l] 12. 10 10 6 [34:25] 6@r 24+ y@s [29:21.] [43:4+@n] [1:4@l] [25:6σ] 23 7@r 23ρ
L10: [28:6.] 15+@s [23:35+] 24 6 7+ 23 21 24 25 6 4 r. [9:6.] 23 23ρ 30. 4@s 24+ 16+ 24.
L11: 26 6 [37:10@s] [4:7ρ@n] [14:15+] 26. y 24+ 16+ 6. 6. 26. 18 7ρ@n 10@l 14@n 18 3 [52:6ρ] 16 6 24 6


Write the answer TSV (header + exactly 60 rows) to /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/lookalike/audit/f52r_a_audit_reread.tsv and reply only "done 60 rows".
