# PREREG-MANT0490L (9 Oct 2026, 18:5x UTC by date -u, written while the three blind passes were still running: before any pass result was read and before any score; LANE FAMILY-A2k account 2)

Leaf: HStA Dresden 10026 Loc. 694/08, film frame 0490 (fullsize 0490.jpg, re-fetched once 9 Oct 2026 18:46 UTC, HTTP 200, sha256 prefix
c60a2ad6ca891c02 = MANT-0490's file), LEFT page (paragraphs 3-5, the continuation of the dispatch whose right page MANT-0490 read) and the
vertical run in the gutter margin. Manteuffel to Flemming, mid-November 1712 (between 0489, Berl. 15 Nov, and 0496, 20 Nov). Premise as
PREREG-MANT0490 (Acta Borussica BO I: only Nr. 82, Berlin 23 Nov 1712, printed for November; no 15-20 Nov report printed or paraphrased).
Question: does key.tsv (origin/main, last key commit a768bc651) read this page's glossed code runs the way its own interlinear period gloss
reads them? A key test, not a reading.

Token count on the image before planning (worker eye, 18:47 UTC): left page about 52 code tokens in 9 code lines (L01 '207'; L02-L04
paragraph 3; L05-L09 paragraph 5); gutter run about 37 tokens in 2 lines, followed by clear words ('et a la satisfaction des deux partis
belligerents' at sight) and with no interlinear note seen at sight. About 89 for both: under ~120, so the whole left page and the gutter run
are read in this job.

Protocol = PREREG-MANT0490 exactly, with these inputs:
- codes: two blind Sonnet passes over the 10 crops f0490_08/crops/c0490L01..L09_L01.jpg and c0490G01_L01.jpg (gutter strip rotated 90 deg
  to horizontal, f0490_08/gutter_rot.jpg = 0490.jpg box 2060,1280,2240,2520), one call per pass, pass B in reverse order -> passA_L.tsv,
  passB_L.tsv; reconciled by this worker from the image where they disagree -> f0490_08/ciphertext_L.tsv, before any gloss is attached to
  codes and before any score. Disclosure: this worker has seen key.tsv's values, MANT-0490's right-page results and the left page's glosses
  at sight scale; digits are settled from the image, never from key values; doubtful ones marked low.
- gloss: ONE blind Sonnet gloss pass (gloss_L.tsv; V-BRANDT rule) over g0490L01..L09 strips plus the code crops' top edges and the gutter
  crop, used exactly as that pass wrote it (letters only; '?' letters dropped); this worker does not correct, complete or settle any gloss
  word. A crop the pass marks NONE has no gloss span.
- spans: f0490_08/gloss_spans_L.tsv (same columns as gloss_spans.tsv, page 'L'), one row per gloss note with the code tokens it sits over,
  set by physical position (the pass's x extents and this worker's eye), never by what a decode would need; a note whose codes cannot be
  placed is left out and listed. The gutter words after the numbers are main text unless the gloss pass places a note over the numbers.

Statistic S: exactly f0490_08/gloss_gate.py's, copied as f0490_08/gloss_gate_L.py (writes gate_L.out; --check), seed 490.
Name codes whose value is a whole word or name match only when the gloss spells the whole value: S is a lower bound.
Control (rule 3): key.tsv values permuted over its codes, 1000 draws, seed 490, same spans and alignment (can differ from the target).
Gate (a): deciding row = every left-page span. PASS if S > p99 AND S >= 0.5 x keyed code tokens in spans; fewer than 10 keyed tokens = too
short (neither PASS nor FAIL). A span's codes are grade C only if the deciding row PASSes; everything else M.
Reported only (no gate): left + right pooled, with MANT-0490's right-page deciding spans.
Gate (b): the unglossed gutter run(s) (if >= 15 tokens) through exactly f0474_08/judge_gate.py copied as f0490_08/judge_gate_L.py (fr18,
permuted-key, name-abbreviation rule, 52-letter blocks, power >= 0.80 from the same positive controls), seeds 490(+k), input
f0490_08/judge_L/ciphertext.tsv; run only if under 80% of the cap after gate (a). Gate (b) PASS = the gutter run grades S under key.tsv;
too-short/FAIL = M. A decode of the gutter run is reported as letters with its verdict, not as a reading.
Cross-witness (descriptive, no gate) -> f0490_08/candidates_L.tsv, never key.tsv: codes outside key.tsv; codes > 401; the held codes 321,
191, 254, 199, 42 and MANT-0494's 231-715 if present; rule-4 conflicts where a keyed code's slot disagrees with its gloss letters.
