# PREREG MERCY-GAP (17 Oct 2026, written and pushed before any gap was measured)

Worker MERCY-GAP (account 4), brief `.claude/briefs/runs/2026-10-17-acct4-research-director-2.md` "## JOB MERCY-GAP".
Question: can a pixel gap statistic, gated on known pairs, separate "glued" from "spaced" digit pairs on this writer's hand, and
which side do r20:6-7, r18:5-6 and r24:14-15 fall on? Disk only; no network, readers, vision calls, reading, key or AUDIT.md edit.

## Material
`images/f22r_canvas58.jpg` (native page, the source of `mercyimg/crops/`), rows r16-r24 at the bands in `mercyimg/crops/manifest.json`
(x 400-3350). Token order from `ciphertext.tsv`; reader groupings from `mercyimg/readA.tsv` / `readB.tsv`. Rows outside r16-r24 have
crops only for r01-r09/v01-v04 region sets from an earlier pass; the three targets and all six known clusters lie on r16-r24, so only
r16-r24 are scored.

## Instrument (`mercygap/gap.py`)
Binarize (Otsu on the band), column ink profile over the band's central text strip, ink runs separated by empty columns, runs merged
across gaps under 2 px; runs aligned in order to the row's digit sequence (each digit one run; a row whose run count does not equal its
digit count after a fixed merge/split rule is reported and its gaps are not used). Statistic g = horizontal white gap (px) between
the two digits, divided by the row's median digit run width. No parameter is tuned after the gate is read.

## Classes
- Positive (glued, written together, S by the out-of-range rule): the six clusters r16:21-22 (72), r17:10-11 (52), r17:21-22 (48),
  r20:15-16 (48), r23:1-2 (186: the 18|6 gap), r24:4-5 (65).
- Negative (ordinary between-token gaps on r16-r24): every adjacent token pair not in a positive, a target, or a reader-flagged spot
  (r19:7-8, r20:4-5, r22:2-3, r22:6-7, r22:10-11 "75", r24:20-21); at least 30 needed or the job is a non-test.
- Diagnostic (third class, declared here): the digit gap inside genuine two-digit codes (H tokens 10-34). NOTE before any number: a
  glued cluster 2|3 and a code 23 are both "digits written together", so the brief's two classes can make only the *split* side
  informative for 23-vs-2|3. A target on the glued side decides 23 vs 2|3 only if glued clusters also separate from intra-code gaps;
  that separation is reported with the same LOO rule but does not change the brief's gate.

## Gate (held out)
Threshold t = midpoint between the class means' nearest members (max positive g, min negative g style: t chosen on the training
fold as the value maximizing balanced accuracy, ties to midpoint). Leave-one-out over all positives and negatives: PASS iff every
held-out positive is on the glued side (g < t) and >= 90% of held-out negatives on the split side. Control: the same LOO with class
labels permuted (20 permutations, seed 0..19, class sizes kept); PASS of the control requires it to FAIL the same gate in >= 19 of 20.
Gate failure or control failure = non-test: logged, targets not read, stop.

## Decision (from the brief)
After a pass only: margin m = t - g (glued side positive). Smallest held-out positive margin = m0. A target with m > m0 on the glued
side, or with -m > the smallest held-out negative margin on the split side, is a lead for the verifier (DV-MERCY3), never applied here;
otherwise it stays M. Glued-side leads are further qualified by the diagnostic (glued vs intra-code). Reading, key, AUDIT.md unchanged.

## Decision
(Belief and Would-change restate the gate pushed in 3f58c1d96 before measurement; that commit's section headed "Decision" carried the
brief's rule but not this tool's five-line form, added here after the run -- the gate itself is unchanged.)
Belief: this writer leaves a visibly smaller gap inside a glued cluster than between tokens, so a pixel gap can say "spaced" for 2|3.
Would change it: LOO with every held-out known cluster on the glued side and >= 90% of negatives on the split side, and the label-shuffled control failing that gate in >= 19 of 20.
Observed: real LOO 5/6 known clusters glued side (held-out 65 at r24:4-5, g 0.714, falls split side), negatives 0.940 split side (N 168) -> FAIL; shuffled control fails 20/20 (control PASS); diagnostic: intra-code gaps median 0.178 (N 120) overlap the glued clusters (0.000-0.714) entirely.
Decision: stop -- non-test by the pre-registered gate; r20:6-7, r18:5-6, r24:14-15 not read; they stay M.
Lesson: on f.22r the glued-cluster gaps (0-0.71 digit widths) reach the low tail of between-token gaps (about 6% of 168 under 0.72, some 0.0 from touching or alignment), so six positives cannot hold a threshold under LOO; and glued 2|3 and code 23 are both "written together" (diagnostic overlap), so even a pass could only ever decide the split side.
