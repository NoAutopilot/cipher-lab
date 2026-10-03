# FT4ad pre-registration (account-4, 3 Oct 2026, written 18:07 UTC by the clock, pushed before any crop is read)

Step (FT4ac's Verdict): a blind eye check of the f.206 cipher (ff.205v/207r, numbering of ciphertext.tsv, 0-indexed) at the
two boundaries where FT4ac's exact solver frees 581 next to 534 / 338, with an equal number of decoys.

Positions:
- Targets (4): g21 534 (f207r L01, last group of the line), g22 581 (f207r L02, first group), g35 338 (f207r L03, first group),
  g36 581 (f207r L03, second group).
- Decoys (4, same lines, same hand, adjacent): g20 420 (L01), g23 379 (L02), g37 279 (L03), g38 347 (L03).

Crops: cut with `tools/iiif_lines.py --image` from the on-disk line crops `images/f207r_L01_s2.jpg`, `f207r_L02_s1.jpg`,
`f207r_L03_s1.jpg` (no network), one group per crop, `--region` boxes taken from the tool's own `--groups` ink pieces,
each box extended to half the gap on each side (and to the line end / line start for g21 / g22) so a dot, stroke, clear letter
or correction in the gap shows. Blind copies `images/ft4ad/C1-C8.jpg`, shuffled by seed 20261003:
C1 g23, C2 g37, C3 g36, C4 g22, C5 g35, C6 g38, C7 g20, C8 g21.

Reader: ONE Opus 5.5 subagent vision call, given only the eight crop paths; no transcription, no key, no slip, no expected values,
not told which crops are targets or what the job is about. Per crop: digits as read, confidence (high/medium/low), alternative per
digit, and every non-digit mark (dot, stroke, letter, cancel, overwriting, extra sign) with its place (before / inside / after).

Scoring:
- CHANGED = first reading differs from the transcription in any digit or digit count; HIGH change = changed at high confidence.
- Any decoy HIGH change -> NOISY: nothing acted on, logged only.
- MARK = a non-digit sign reported at a boundary that is not the ordinary group-separator dot. A clear letter (t, s) or a
  cancel/correction/extra sign at a target boundary (after 534 / before 581 at g22; after 338 / before 581 at g36) with the
  same kind of mark absent on all 4 decoys -> outcome B (a written explanation of the one-letter boundary: the left-over s / t
  written in clear or a corrected group). Logged as I, a VERIFY flag line, no key or transcription change in this job.
- Targets read as transcribed, no non-ordinary mark at a target boundary -> outcome P1: the boundary is not explained by the
  image at this reader's resolution; the one-letter boundary stays an unencoded-letter / shifted-chunk question (I), rule 4
  conflict notes unchanged.
- A target HIGH change with decoys clean -> logged as a doubt with a second-eye request; no transcription change in this job
  (brief: key change only via a later VERIFY).
No solver re-run in this job. Cap USD 2, box 18:06-18:26 UTC, stop line 18:22.
