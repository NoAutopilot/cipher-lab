# Pre-registration: R8-ZESCH crib test on R5008 (written 6 Oct 2026 04:05 UTC by date -u, before any statistic on R5008)

Same question and statistics as `PREREG-GAPS185.md` / `PREREG-GAPS196.md` (T1 pair-profile cosine to R5005, T2 pin
coverage, T3 pin-count Spearman), with R5008 (26 Oct 1843, German) as the target. What changes is the order: the
power control is run and gated FIRST, and the target statistic is computed only if the control clears its gate.

- Target stream: `transcription/r5008_ciphertext.txt` (GAPS208: 260 digits, P1 113 + P2-left 147), lines
  concatenated in page/line order. Phase rule unchanged (higher pair IC of phase 0 vs 1), so about 130 pairs.
- Matched power control (primary, gated): 200 contiguous 260-digit windows of **R5007** (German, same hand, same
  correspondence, shown to share R5005's syllabary by GAPS196, p 0.0005), each scored by T1 against the whole of
  R5005 with its own 200-draw shuffled-digit null. This matches N (260), symbol count (two-digit codes, 100-pair
  space), design (the same syllabary) and language (German) -- a closer match than a synthetic syllabary, which
  GAPS202 showed we cannot build to the cipher's real unit inventory. Gate: share of windows with p < 0.01 >= 0.80.
  Below the gate -> "untestable at N=260", the target T1/T2 are not computed (exit 3), logged as a non-test.
- Secondary power control (reported, not gated): 200 R5005 windows of 260 digits vs the rest of R5005, as GAPS185.
- The control can vary on the statistic: windows are real cipher pair counts whose cosine to R5005 can fall to the
  shuffled null at small N; the shuffled-digit null changes the pair counts the statistic is computed on.
- If the gate is met: target T1 against 2,000 shuffled-digit draws of the same 260 digits; T1 p < 0.01 -> consistent
  with the same syllabary as R5005 (no token read). T2, T3 reported, no gate.
- Seed 8008. Output `crib_test_r5008.json` via `crib_test.py --target r5008`; `--check` regenerates it. The R5006 and
  R5007 outputs are untouched.
- Grades as GAPS185: pins stay I (Bourdeau's values); at most M when applied; no reading.

Second step (only if budget allows, pre-registered here so it cannot be shaped by the first result): a crib-anchored
key search on R5008's sentence frame. The frame (Bourdeau's target table; GAPS208's overview) gives clear text on both
sides of the cipher but no plaintext *inside* it, so a crib-anchored search has no known plaintext span to anchor on.
Before any such search a matched control is required: a synthetic 260-digit syllabary text in German built from the
held-out de19 book, same K, with only the clear-text frame known, and the search must recover >= 0.60 token
accuracy there. If no control design with a real anchor can be written within this job's cap, the step is logged
"not attempted: no in-cipher crib exists" with the reason, not run.
