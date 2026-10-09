You are a third, VALUE-BLIND reader settling the places where two earlier blind readers of a cipher transcription disagree. You match hand-drawn signs by SHAPE only; you do not know, and must not try to work out, what any sign means. Read ONLY the files listed here; do not open, list or search any other file or directory.

Sign sheet: /tmp/claude-0/-home-user-cipher-lab/98b5b21b-1a0b-59d7-9254-31bf1ab2c1c8/scratchpad/adj/adj_ceppo_opus_a/sign_sheet_blind.png

Crops (in order):
/tmp/claude-0/-home-user-cipher-lab/98b5b21b-1a0b-59d7-9254-31bf1ab2c1c8/scratchpad/adj/adj_ceppo_opus_a/v36top_L01_s1.jpg
/tmp/claude-0/-home-user-cipher-lab/98b5b21b-1a0b-59d7-9254-31bf1ab2c1c8/scratchpad/adj/adj_ceppo_opus_a/v36top_L01_s2.jpg

Crops: the one line L01 in two OVERLAPPING segments s1 (left) and s2 (right); the last signs of s1 reappear at the start of s2 and are ONE sign each. The small letters above the signs are a later annotation: ignore them; read only the large cipher signs of the main line.

Disagreement sheet: /tmp/claude-0/-home-user-cipher-lab/98b5b21b-1a0b-59d7-9254-31bf1ab2c1c8/scratchpad/adj/adj_ceppo_opus_a/adjudicate_in.tsv

Each row of the sheet is one disputed position: passage (= line) and pos (position in the line counting the agreed signs), context_before / context_after (the agreed neighbouring signs, as labels, so you can find the place on the line crop by counting), candA / candB (what each earlier reader wrote there; "(none)" = that reader saw no sign there), their confidence and notes. For each row look at the crop and decide which reading the ink supports.

Answer with a cell of the sheet (S10..S97) or one of X_THETA2, X_POUND, X_NEW (describe it in the note). Write NONE if there is no separate sign at that position (one reader split one sign in two or saw a sign that is not there); write ? only if the ink cannot decide at all. You may give a cell neither reader wrote if the ink clearly shows it.

Output: write exactly one TSV file /tmp/claude-0/-home-user-cipher-lab/98b5b21b-1a0b-59d7-9254-31bf1ab2c1c8/scratchpad/adj/adj_ceppo_opus_a/adjudicate_out.tsv with the header
passage	pos	sign_id	conf	note
and one row per sheet row (same passage and pos), conf H/M/L, note = a few words on the shape and which candidate you rejected. No other output file. Then report in two sentences: rows settled, how many to candA / candB / other / NONE / ?. Do not decode, do not guess meanings.
