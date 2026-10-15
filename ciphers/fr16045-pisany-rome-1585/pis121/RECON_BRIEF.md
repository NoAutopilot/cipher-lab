# Reconciliation of two blind passes, fr16045 canvas 252 (PIS-121, 15 Oct 2026)

Value-blind: do not read key.tsv or any reading/decode/gloss file. Read only: this brief, ../tx/SIGNSHEET.png, ../tx/SIGNS.md,
rec/disagreements.tsv (columns line, col, A, B; "-" = that reader saw no sign there) and the crops /tmp/claude-0/-home-user-cipher-lab/cc3e6f93-d812-57ee-82d9-34f21d908561/scratchpad/crops/c252_LNN_s1.jpg / _s2.jpg.

Task: for every row of rec/disagreements.tsv, look at that line's crops and decide which reading is right at that place in the
line: A, B, or a third label, or "-" (no sign there). Work one line at a time (open that line's two crops once, settle all its rows).
Ignore plain French handwriting ([clear] runs) and small interlinear writing. Do not guess language or content.

Output: write rec/choices.tsv, tab-separated with header line, col, choice -- one row per disagreements.tsv row, choice = an Sxx
label, ?[shape], or "-". Then reply with only the path and how many rows you settled as A, as B, as other, and as "-".
