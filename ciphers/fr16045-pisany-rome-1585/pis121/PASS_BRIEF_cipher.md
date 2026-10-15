# Blind transcription pass, fr16045 canvas 252 (PIS-121, 15 Oct 2026)

You are one of two independent readers. Do not read any file in ciphers/fr16045-pisany-rome-1585 except the ones named here;
do not read key.tsv or any reading/decode file (this pass must be value-blind).

Inputs:
- Reference sheet: ciphers/fr16045-pisany-rome-1585/tx/SIGNSHEET.png (67 labelled cells S01-S67) and its shape list tx/SIGNS.md.
  S07 = S04 and S08 = S05 (same shapes): use S04 / S05.
- Line crops: /tmp/claude-0/-home-user-cipher-lab/cc3e6f93-d812-57ee-82d9-34f21d908561/scratchpad/crops/c252_L01_s1.jpg, c252_L01_s2.jpg, ... c252_L27_s2.jpg (27 manuscript lines, each in two segments;
  s2 repeats about the last 100 px of s1: start s2 after the last sign you already read from s1).

Task: for each line L01..L27, read every cipher sign left to right and write its label. Rules:
- Use the closest Sxx label. If a sign matches no cell, write ?[shape] (no spaces), e.g. ?[colon-bar]. If unsure between labels,
  write the best label with a trailing ? (e.g. S41?).
- Multi-stroke signs: prefer the compound label when the strokes sit together as in the cell (S25, S26, S57, S59, S60-S67).
- Some lines are wholly or partly ordinary French handwriting (plain words). Do not transcribe plain words: write the single token
  [clear] once for each run of plain handwriting, at its place in the line. A line that is all plain handwriting is just [clear].
- Ignore small writing squeezed above or between lines, stains, and anything at the far left/right edges that belongs to the margins.
- Read each crop image with the Read tool, one crop at a time; never open a full-page image.

Output: write one file, tab-separated, no header: L01<TAB>S12 S40 [clear] S31 ... one row per line (27 rows), to the path given
in your instructions. Then reply with only: the file path, the total sign count, the count of ? signs, and the 5 labels hardest to tell apart.
