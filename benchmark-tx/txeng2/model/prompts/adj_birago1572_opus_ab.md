You are a third, VALUE-BLIND reader settling the places where two earlier blind readers of a cipher transcription disagree. You match hand-drawn signs by SHAPE only; you do not know, and must not try to work out, what any sign means. Read ONLY the files listed here; do not open, list or search any other file or directory.

Sign sheet: /tmp/claude-0/-home-user/97cda43d-712a-5015-9525-3fb5697f385a/scratchpad/r/adj_birago1572_opus_ab/sign_sheet_blind_1572.png

Crops (in order):
/tmp/claude-0/-home-user/97cda43d-712a-5015-9525-3fb5697f385a/scratchpad/r/adj_birago1572_opus_ab/f178v_L01_s1.jpg
/tmp/claude-0/-home-user/97cda43d-712a-5015-9525-3fb5697f385a/scratchpad/r/adj_birago1572_opus_ab/f178v_L01_s2.jpg
/tmp/claude-0/-home-user/97cda43d-712a-5015-9525-3fb5697f385a/scratchpad/r/adj_birago1572_opus_ab/f178v_L01_s3.jpg
/tmp/claude-0/-home-user/97cda43d-712a-5015-9525-3fb5697f385a/scratchpad/r/adj_birago1572_opus_ab/f178v_L03_s1.jpg
/tmp/claude-0/-home-user/97cda43d-712a-5015-9525-3fb5697f385a/scratchpad/r/adj_birago1572_opus_ab/f178v_L03_s2.jpg
/tmp/claude-0/-home-user/97cda43d-712a-5015-9525-3fb5697f385a/scratchpad/r/adj_birago1572_opus_ab/f178v_L03_s3.jpg
/tmp/claude-0/-home-user/97cda43d-712a-5015-9525-3fb5697f385a/scratchpad/r/adj_birago1572_opus_ab/f178v_L04_s1.jpg
/tmp/claude-0/-home-user/97cda43d-712a-5015-9525-3fb5697f385a/scratchpad/r/adj_birago1572_opus_ab/f178v_L04_s2.jpg
/tmp/claude-0/-home-user/97cda43d-712a-5015-9525-3fb5697f385a/scratchpad/r/adj_birago1572_opus_ab/f178v_L04_s3.jpg
/tmp/claude-0/-home-user/97cda43d-712a-5015-9525-3fb5697f385a/scratchpad/r/adj_birago1572_opus_ab/f178v_L05_s1.jpg
/tmp/claude-0/-home-user/97cda43d-712a-5015-9525-3fb5697f385a/scratchpad/r/adj_birago1572_opus_ab/f178v_L05_s2.jpg
/tmp/claude-0/-home-user/97cda43d-712a-5015-9525-3fb5697f385a/scratchpad/r/adj_birago1572_opus_ab/f178v_L05_s3.jpg
/tmp/claude-0/-home-user/97cda43d-712a-5015-9525-3fb5697f385a/scratchpad/r/adj_birago1572_opus_ab/f178v_L06_s1.jpg
/tmp/claude-0/-home-user/97cda43d-712a-5015-9525-3fb5697f385a/scratchpad/r/adj_birago1572_opus_ab/f178v_L06_s2.jpg
/tmp/claude-0/-home-user/97cda43d-712a-5015-9525-3fb5697f385a/scratchpad/r/adj_birago1572_opus_ab/f178v_L06_s3.jpg
/tmp/claude-0/-home-user/97cda43d-712a-5015-9525-3fb5697f385a/scratchpad/r/adj_birago1572_opus_ab/f178v_L09_s1.jpg
/tmp/claude-0/-home-user/97cda43d-712a-5015-9525-3fb5697f385a/scratchpad/r/adj_birago1572_opus_ab/f178v_L09_s2.jpg
/tmp/claude-0/-home-user/97cda43d-712a-5015-9525-3fb5697f385a/scratchpad/r/adj_birago1572_opus_ab/f178v_L09_s3.jpg
/tmp/claude-0/-home-user/97cda43d-712a-5015-9525-3fb5697f385a/scratchpad/r/adj_birago1572_opus_ab/f178v_L12_s1.jpg
/tmp/claude-0/-home-user/97cda43d-712a-5015-9525-3fb5697f385a/scratchpad/r/adj_birago1572_opus_ab/f178v_L12_s2.jpg
/tmp/claude-0/-home-user/97cda43d-712a-5015-9525-3fb5697f385a/scratchpad/r/adj_birago1572_opus_ab/f178v_L12_s3.jpg

Crops: three overlapping segments s1, s2, s3 per line of f.178v (2x; about 100 px overlap, a sign at the right edge of s1 that reappears at the left edge of s2 is ONE sign). The page is cipher throughout.

Disagreement sheet: /tmp/claude-0/-home-user/97cda43d-712a-5015-9525-3fb5697f385a/scratchpad/r/adj_birago1572_opus_ab/adjudicate_in.tsv

Each row of the sheet is one disputed position: passage (= line) and pos (position in the line counting the agreed signs), context_before / context_after (the agreed neighbouring signs, as labels, so you can find the place on the line crop by counting), candA / candB (what each earlier reader wrote there; "(none)" = that reader saw no sign there), their confidence and notes. For each row look at the crop and decide which reading the ink supports.

Answer with a cell of the sheet (T10..T98) or one of X_K, X_A, X_EQ, X_S, X_NEW (describe it in the note). Write NONE if there is no separate sign at that position (one reader split one sign in two or saw a sign that is not there); write ? only if the ink cannot decide at all. You may give a cell neither reader wrote if the ink clearly shows it.

Output: write exactly one TSV file /tmp/claude-0/-home-user/97cda43d-712a-5015-9525-3fb5697f385a/scratchpad/r/adj_birago1572_opus_ab/adjudicate_out.tsv with the header
passage	pos	sign_id	conf	note
and one row per sheet row (same passage and pos), conf H/M/L, note = a few words on the shape and which candidate you rejected. No other output file. Then report in two sentences: rows settled, how many to candA / candB / other / NONE / ?. Do not decode, do not guess meanings.
