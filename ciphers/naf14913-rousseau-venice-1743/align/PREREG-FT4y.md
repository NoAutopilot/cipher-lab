# FT4y pre-registration (account-4, 3 Oct 2026, written ~16:3x UTC by the clock, pushed before any vision call)

Step (FT4x's Verdict): a blind eye re-check of the positions FT4x's post hoc readout implicates in the f.266r S1 + f.252r exact
pooled conflict (253 plus one of 369/213/248), with an equal number of decoy positions.

Positions (0-indexed group numbers as in ciphertext_f252r.txt and the S1 numbering of FT4s/FT4x):
- f.252r targets: g1 (253, flagged alt 233), g5 (369), g6 (213), g7 (248). Decoys: g0 (527), g2 (447), g3 (188), g4 (767).
- f.266r S1 targets: g39 (213), g40 (248), g46 (369). Decoys: g35 (718), g42 (63), g48 (180).
7 targets, 7 decoys.

Crops: `images/ft4y/p<leaf>_<group>_L01.jpg`, cut with `tools/iiif_lines.py --image` from the on-disk f.252r source region
(src_f517_698_2951_3956_2620.jpg) and the FT4q f.266r line crops (L05_s1, L05_s2, L06_s1), boxes from the tool's own `--groups`
ink pieces; one group per crop (neighbouring digits excluded, faint gloss strokes above the f.252r groups may show).
Blind copies renamed by seed 20261003 shuffle (A1-A8 = f.252r, B1-B6 = f.266r):
A1 g5, A2 g6, A3 g3, A4 g1, A5 g2, A6 g7, A7 g4, A8 g0; B1 g48, B2 g39, B3 g40, B4 g42, B5 g35, B6 g46.

Readers: 2 vision calls total, one Opus 5.5 subagent per leaf, given only its crop paths; no transcription, no expected values,
no key, no gloss, told nothing about which crops are targets. Each crop: digits as read, confidence (high/medium/low), any
alternative reading per digit, any mark (stroke, dot, cancel).

Scoring rule:
- A position is CHANGED when the reader's first reading differs from the committed transcription in any digit (or digit count).
  A HIGH change is a changed position read at high confidence.
- Decoy error rate = changed decoys / 7. If any decoy is a HIGH change, the reader is not reliable at this resolution:
  outcome NOISY, no target change is acted on (logged only).
- Decisive outcome (registered): decoys 0 HIGH changes AND a target is a HIGH change -> that target's digit is corrected in the
  transcription file (old reading kept as the alternative, grade the token M until a second eye), and the FT4x exact pooled test
  (align/ft4x_pool.py, same blocks S1 + f.252r, same pins, controls (s)/(g) seed 3 n 40 FIRST, same gate: both shares <= 2/40)
  is re-run ONCE with the corrected transcription. A target changed at medium/low is logged as a doubt, not corrected.
- If every target reads as transcribed (P1): the conflict is not a misread at these positions (at this reader's resolution);
  logged as a rule-4 conflict between f.252r's gloss and S1 under the C key (paraphrase, polyvalence, or M split), no key change.
- Key change only if the re-run gate PASSes and FT4x's registered uniqueness readout names a C candidate; then a VERIFY flag
  line in ROOM.md, never a status change.
What a changed digit means: a transcription error at that position (both earlier blind passes and this one being fallible
readers); it does not by itself mean any key value is right or wrong.
Cap USD 3, box 16:18-16:48 UTC, stop line 16:42.
