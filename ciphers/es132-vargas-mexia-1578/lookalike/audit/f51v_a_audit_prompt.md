<!-- operator note (N7-LKTOOL, 4 Oct 2026): this prompt shows the committed label sequence and whole line crops; it drew
7/7 Sonnet re-reads that echoed passC on Vivonne inks 53/54 (voided). Prefer `windows` (per-tile crops, label hidden) or
--hide-passc, and treat a re-read that agrees with passC everywhere as an echo, not a confirmation. -->
# Proofreading audit, f51v_a (value-blind)

You are proofreading 60 signs of a symbol-cipher transcription against the manuscript. The reading below is what the
transcription currently says; some of it may be wrong. For each bracketed position, look at the sign in the line crop
and pick, from the listed candidate ids, the one whose shape it is -- whether or not it is the label the reading shows;
never copy a label from the reading.
You are never told what any sign means; do not guess letters or words.

Line crops (read these images; s1 = left half, s2 = right half of one line; halves overlap a little): /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L11_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L11_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L12_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L12_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L13_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L13_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L14_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L14_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L15_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L15_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L16_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L16_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L17_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L17_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L18_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L18_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L19_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L19_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L20_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L20_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L21_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L21_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L22_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L22_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L23_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L23_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L24_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L24_s2.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L25_s1.jpg, /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/images/f51v_L25_s2.jpg
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
1	L22	9	77@n,70ρ@n,7ρ@n	[27:18] 26 7618@s | 231 101 [8:6ρ]
2	L16	2	11.,21.	11.@s | [40:28ρ] [15:12ρ@l] 1
3	L18	3	21.,11.	20 [37:24ρ] | [49:4] r+ 231
4	L21	18	6,6.@s,6.	7σ 4@n 6ρ | 1
5	L16	10	4.@l,4,4@l	r 610 21. | [32:6σ] 7. r.
6	L21	14	033.,33.	4@s 24+ 14 | 7σ 4@n 6ρ
7	L19	13	4@n,4@l,4+@n	[33:6.] 15+@n 24. | [55:4@s] 24. n.
8	L22	12	6+,6ρ,6σ	[1:7ρ@n] 231 101 | 102 362 368
9	L11	3	{y},7,y	7ρ 231+@s | 68 20ρ@r 7+@r
10	L22	5	12ρ@s,nρ@s	161 28 814 | [27:18] 26 7618@s
11	L19	6	14ρ@r	32σ 10 16. | 20+ [43:23+@m] [58:10]
12	L24	12	38,3+	15ρ@s 23. 7ρ@n | 23. 10 36+
13	L12	7	12ρ,15ρ,24ρ	231 12.@r [36:16+] | 28 35+ 21
14	L15	5	20+@r,20+	[52:7+] 20ρ@r 231 | [26:24] / 28
15	L16	4	12ρ@l	11.@s [2:21.] [40:28ρ] | 1 1+ r
16	L11	13	6.@s,6.,6	23 20. [39:24ρ] | 10 25. r
17	L20	2	70ρ@n,7ρ@n,77@n	[35:y] | 4@s 24ρ 23
18	L25	13	15ρ@s,15+@s,15ρ	35ρ 201 23ρ | 18 36+@s 6
19	L18	8	24,24.@n	r+ 231 14@n | 7σ 18@n 28
20	L12	2	24σ,24ρ,24+	[57:4@s] | 10 231 12.@r
21	L24	2	70ρ@n,7ρ@n,77@n	[47:21.] | 15+ 18 7+
22	L18	15	20ρ@r,20ρ@m	10 17σ [44:16ρ] | 21. 1
23	L20	15	1+,1,161	7ρ {bul} 16 | [31:28] [30:7ρ] 24.@n
24	L23	13	30_	29σ 10 12+ | [29:6σ] 77ρ 7ρ
25	L20	7	1,15,11⊣	24ρ 23 8ρ | 25σ 18 [28:4@l]
26	L15	6	24,24.,24.@n	20ρ@r 231 [14:20+@r] | / 28 4@n
27	L22	6	18@s,18,1.	28 814 [10:nρ@s] | 26 7618@s [1:7ρ@n]
28	L20	10	4.@l,4@l,4	[25:15] 25σ 18 | 6σ 7ρ {bul}
29	L23	14	6σ,6ρ,16σ	10 12+ [24:30_] | 77ρ 7ρ 20
30	L20	17	7σ,77ρ,7ρ	16 [23:1] [31:28] | 24.@n 24+
31	L20	16	28σ,28,128	{bul} 16 [23:1] | [30:7ρ] 24.@n 24+
32	L16	11	16σ,6σ,6ρ	610 21. [5:4@l] | 7. r. y
33	L19	10	6.,6.@s,6	20+ [43:23+@m] [58:10] | 15+@n 24. [7:4@n]
34	L13	13	10,610,10.	17ρ@s 28ρ 15. | 281 6+ r
35	L20	1	7,{y},y	 | [17:7ρ@n] 4@s 24ρ
36	L12	6	6+,16+,16+@s	10 231 12.@r | [13:12ρ] 28 35+
37	L18	2	24+,24ρ,24σ	20 | [3:21.] [49:4] r+
38	L19	17	15ρ,11ρ,17ρ	[55:4@s] 24. n. | 7
39	L11	12	24σ,24ρ,24+	r. 23 20. | [16:6.] 10 25.
40	L16	3	28σ,28ρ,25ρ	11.@s [2:21.] | [15:12ρ@l] 1 1+
41	L12	12	6+,6ρ,6σ	35+ 21 24+@n | 7σ@n 231@s 21
42	L17	17	3,3@s	h+ 25σ 10 | 3
43	L19	8	23+@m,23+@r	16. [11:14ρ@r] 20+ | [58:10] [33:6.] 15+@n
44	L18	14	16σ,16ρ@s,16ρ	28 10 17σ | [22:20ρ@m] 21. 1
45	L23	2	6ρ,6+,6σ	15ρ@s | 20@n 1 24ρ@s
46	L17	8	15+@s,15+,15+@2	23σ [60:18@n] 6. | 7+ r 24+
47	L24	1	11.,21.	 | [21:7ρ@n] 15+ 18
48	L25	3	10,610,10.	21. 15+ | 16σ 23 [56:24+]
49	L18	4	4+,4,4.	20 [37:24ρ] [3:21.] | r+ 231 14@n
50	L14	15	3@l,3,183	24+@l 6. 16ρ@n | 6+ 7618
51	L16	19	201,23,23.	24.@n 6σ 4 | 
52	L15	2	7+,74,7	12. | 20ρ@r 231 [14:20+@r]
53	L17	12	.,2+,21	7+ r 24+ | 15. h+ 25σ
54	L21	3	23.,201,23	23+ 24σ | 2. 7ρ 6
55	L19	14	14@s,4@s,20+@s	15+@n 24. [7:4@n] | 24. n. [38:11ρ]
56	L25	6	24+,24,x+	[48:10] 16σ 23 | 6 21. 4@l
57	L12	1	14@s,20+@s,4@s	 | [20:24ρ] 10 231
58	L19	9	10,10.,610	[11:14ρ@r] 20+ [43:23+@m] | [33:6.] 15+@n 24.
59	L13	9	11.,11,11.@s	231@s 6. 23σ | 17ρ@s 28ρ 15.
60	L17	6	14@n,18@n	18 7+ 23σ | 6. [46:15+@s] 7+

The reading (bracketed [item:label] = positions to audit):
L11: 7ρ 231+@s [9:y] 68 20ρ@r 7+@r 23+ 28 r. 23 20. [39:24ρ] [16:6.] 10 25. r 23 18
L12: [57:4@s] [20:24ρ] 10 231 12.@r [36:16+] [13:12ρ] 28 35+ 21 24+@n [41:6ρ] 7σ@n 231@s 21 4@r 29+
L13: 6. 10 24+ 14+@r 15. 231@s 6. 23σ [59:11] 17ρ@s 28ρ 15. [34:10] 281 6+ r 610 2
L14: 71 6σ r 610 77ρ mρ 23. 6. 37 610 10 24+@l 6. 16ρ@n [50:3] 6+ 7618
L15: 12. [52:7+] 20ρ@r 231 [14:20+@r] [26:24] / 28 4@n 18ρ 23. 1@n 6ρ 6. 15 6. 184
L16: 11.@s [2:21.] [40:28ρ] [15:12ρ@l] 1 1+ r 610 21. [5:4@l] [32:6σ] 7. r. y 4@n 24.@n 6σ 4 [51:23]
L17: 7ρ@n 15+ 18 7+ 23σ [60:18@n] 6. [46:15+@s] 7+ r 24+ [53:21] 15. h+ 25σ 10 [42:3@s] 3
L18: 20 [37:24ρ] [3:21.] [49:4] r+ 231 14@n [19:24.@n] 7σ 18@n 28 10 17σ [44:16ρ] [22:20ρ@m] 21. 1
L19: 23. 20ρ 32σ 10 16. [11:14ρ@r] 20+ [43:23+@m] [58:10] [33:6.] 15+@n 24. [7:4@n] [55:4@s] 24. n. [38:11ρ] 7
L20: [35:y] [17:7ρ@n] 4@s 24ρ 23 8ρ [25:15] 25σ 18 [28:4@l] 6σ 7ρ {bul} 16 [23:1] [31:28] [30:7ρ] 24.@n 24+
L21: 23+ 24σ [54:23] 2. 7ρ 6 15+ r. 23 201 4@s 24+ 14 [6:33.] 7σ 4@n 6ρ [4:6.] 1
L22: 29.@r 161 28 814 [10:nρ@s] [27:18] 26 7618@s [1:7ρ@n] 231 101 [8:6ρ] 102 362 368
L23: 15ρ@s [45:6ρ] 20@n 1 24ρ@s 4@n 21. 16. 12+ 29σ 10 12+ [24:30_] [29:6σ] 77ρ 7ρ 20
L24: [47:21.] [21:7ρ@n] 15+ 18 7+ 23σ 18@n 6. 15ρ@s 23. 7ρ@n [12:3+] 23. 10 36+ 8+ 1
L25: 21. 15+ [48:10] 16σ 23 [56:24+] 6 21. 4@l 35ρ 201 23ρ [18:15ρ@s] 18 36+@s 6 6 10


Write the answer TSV (header + exactly 60 rows) to /home/user/cipher-lab/ciphers/es132-vargas-mexia-1578/lookalike/audit/f51v_a_audit_reread.tsv and reply only "done 60 rows".
