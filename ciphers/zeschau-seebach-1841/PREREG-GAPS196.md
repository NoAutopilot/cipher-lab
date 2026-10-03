# Pre-registration addendum: GAPS196 crib test on R5007 (written 3 Oct 2026 18:53 UTC, before the R5007 right page was transcribed and before any statistic)

Same question, statistics, control, positive control and gate as `PREREG-GAPS185.md`, unchanged, with R5007 (13 June
1842) in place of R5006. Only the inputs and N change:

- Target stream: `transcription/r5007p2l_ciphertext.txt` (left cipher page, 603 digits, GAPS190) followed by
  `transcription/r5007p2r_ciphertext.txt` (right cipher page, GAPS196), concatenated in page/line order. The
  catchword "53386" at the foot of the left page is not counted (it repeats the first five digits of the right page).
  N = whatever the reconciled transcription holds; the phase rule (higher pair IC) is unchanged.
- Shuffled-digit control: 2,000 draws of the same R5007 digits. Positive control: 200 contiguous R5005 windows of
  length N (not 692), each against the rest of R5005 with its own 200-draw null; power < 0.8 -> "untestable at this N".
- Seed 196. Output `crib_test_r5007.json` via `crib_test.py --target r5007` (`--check` regenerates it); the R5006
  default run and `crib_test.json` are untouched.
- Gate: T1 p < 0.01 -> consistent with the same syllabary as R5005 (no token read). T2, T3 reported as in GAPS185.
  If the run happens without the right page (budget), it is labelled "R5007 left page only" and N is stated.
- Also reported, descriptive only (not a gate): T1 with R5006 as the reference instead of R5005.
Grades as GAPS185: pins stay I (Bourdeau's values), at most M when applied; no reading.
