# PREREG -- R8-BAL103: where does the f.50 decode break, transcription or table? (written and pushed before any per-pass score is computed)

Worker R8-BAL103 (account 1, LANE LANE-RUN8-account-1), 6 Oct 2026, written about 03:5x UTC by `date -u`. Nothing below has been
computed yet: the per-pass decodes, line scores, permutation and synthetic controls are all run by `r8/pertest.py` after this file is
pushed. There is no plaintext of f.50 to open; "the answer" here is the per-line and per-page statistics.

## Material
- Pass A and pass B of f.50r-v as transcribed blind (R7A-BAL103): `tx/f50r_passA_long.tsv`, `tx/r7b/f50r_passB_long.tsv` (the
  L11/L12-relabelled B file), `tx/f50v_passA_long.tsv`, `tx/f50v_passB_long.tsv`. Per-line agreement share from
  `tx/r7b/rec_r/agreement.tsv`, `tx/r7b/rec_v/agreement.tsv` (32 lines).
- Key: `key_decode.tsv` as committed (Tomokiyo 1644 table + the licensed c = p). Decoding rule = `tx/r7b/judge_input.py`'s: first value
  of an a|b cell, U (sign not in table) dropped, word codes (=11 que etc.) give their word.
- Language model: `tools/judge_plaintext.py`'s NgramModel on the fr17 corpus (the spec's corpus).

## T1 -- page-level table test (does the table read f.50 at all, per pass?)
Statistic S = mean log10 4-gram probability per letter of each pass's whole-page decode (f.50r+v joined).
Controls: (a) permutation null: 200 random permutations of letter values across the key's sign cells (word codes kept), same pass,
same scoring (seed 1644); (b) matched synthetic: a fr17 window of the same letter count, enciphered with this table (a uniformly random
homophone per letter), then each sign replaced by a uniformly random other table sign at rate r = 0.15 and 0.30 (20 seeds each),
decoded and scored.
- T1 table-reads: S > permutation p99 for both passes.
- Descriptive: where S falls between the synthetic r=0.15 and r=0.30 bands gives the transcription-error level the decode "looks like".

## T2 -- per-line localisation (32 lines)
For each line: sA, sB = 4-gram score of each pass's line decode; agr = reconciler share. Reference: the synthetic control at r = 0.15
cut to the same line length (200 windows per length): a line **breaks** in a pass when its score is below that reference's p05.
A line is a **break line** when it breaks in both passes.

## Decision rule (registered)
Let HI = lines with agr >= 0.90 (passes agree on >= 90% of columns), LO = lines with agr < 0.80.
- **Table suspect** if T1 table-reads fails for either pass, OR (>= 50% of HI lines are break lines AND Spearman rho(agr, mean(sA,sB))
  over the 32 lines is not significantly positive, one-sided permutation p >= 0.05, 10,000 shuffles, seed 1644).
- **Transcription suspect** if T1 table-reads holds for both passes AND fewer than 50% of HI lines are break lines AND (rho is
  significantly positive OR break lines are more frequent in LO than in HI).
- Otherwise **undecided** (say so; not a negative either way).

## Step 3 -- re-reads of the worst lines (only if transcription suspect or undecided)
Worst 4-6 lines = break lines ranked by mean(sA,sB), lowest first (ties: lower agr first). One blind Sonnet pass per batch of their
existing line crops (`images/f50*_L*.jpg`, cut by tools/iiif_lines.py in R7A) and the key sheet only, never the decode, never told
any plaintext, told to read the ink. Settlement rule: at a column where the re-read sign equals pass A's or pass B's reading (2 of 3),
that sign is applied as a correction in `r8/corrections.tsv` (line, position, old, new, A, B, reread) at grade M unless all three agree;
a re-read that matches neither pass is logged, not applied. ciphertext.tsv keeps the old sign in `alt`; no silent repair. Then
decode_key --check and the fr17 judge, before/after reported.
If **table suspect**: no re-read; name the April 1644 table search (Tomokiyo / DECODE R2742's own documents, other April 1644
Le Tellier-Marca letters in Baluze 103) as next, not run.

## Descriptive, not gated
- Per-sign best-alternative gain: for each sign with n >= 5 on f.50 (agreed columns), the gain in page S if its value were the best
  other letter; compared with the same statistic on the r = 0.15 synthetic (max gain over signs, 20 seeds). A sign whose gain exceeds
  the synthetic's p95 max is listed as a cell to check on a sibling; never applied to key.tsv here.
- =11 que and other word-code contexts, quoted.
