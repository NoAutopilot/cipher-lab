# PREREG-R9-MANTPC (6 Oct 2026, 06:1x UTC by date -u; LANE LANE-RUN9-account-4, account 4)

Pushed before any per-code score is computed. Nothing has been run for this test yet; R9-MANTPOOL stored only the sorted
blended S of its 1000 shuffle draws (shuffle_r9.tsv), not per-code draws, so the draws are regenerated.

**Question.** R9-MANTPOOL's blended gate PASSed (24 free codes agreeing vs shuffle mean 14.93, p95 19), so roughly 5-10 of the
24 carry signal and the rest are chance. Which of the 24 codes in r9mant/codes_r9.tsv (licence M) beat their own shuffle?

**Instrument (unchanged from R9-MANTPOOL).** r9mant/pooled_multi.py's load/align/shuffle_glosses: same 101 runs, same
normalisation, same bins, same `tools/interlinear_align.py` run_align (floor 1, 6 iterations, defaults). Fixed key = ../key.tsv
**minus the 24 rows whose source names R9-MANTPOOL** (i.e. the key as R9-MANTPOOL ran it). Driver: r9mant/per_code.py.
Reproduction check: the real alignment under that key must give the same 24 agreeing codes and chunks as codes_r9.tsv; any
difference is reported and the regenerated real numbers are used.

**Per-code statistic.** For code v: n_v = distinct runs carrying v (fixed under the shuffle, since codes do not move);
A_v = number of distinct runs carrying v's most frequent non-empty folded chunk; share = A_v / n_v.
**Null.** The same 1000 within-bin gloss shuffles as R9-MANTPOOL (seeds 9501+d, d = 0..999), same aligner and fixed key;
A_v recomputed in each draw. p_v = (1 + #{draws with A_v_shuffle >= A_v_real}) / 1001 (one-sided, ties count against).
**Matched control can vary on the statistic:** the shuffle moves gloss strings between runs, so each code's chunks and A_v change.
(Checked after scoring and reported: per-code null distributions are not degenerate.)

**Multiple comparisons.** Benjamini-Hochberg at q = 0.10 over the 24 codes. "per-code PASS" = BH-significant.

**Per-class breakdown (AX-NAMES lesson).** Class by the real agreeing chunk: letter (1 letter); word (the chunk equals a whole
gloss word in at least one of its agreeing runs); syllable (otherwise). Pass counts and mean p reported per class.

**Positive (power) control.** The 5 R9-MANTPOOL known-answer C codes (35, 33, 10, 66, 14) are unfixed in the real run and in
each of the same 1000 shuffle draws (key additionally minus those 5), and tested with the same statistic and BH at q 0.10
over those 5. Reported as recovered-by-per-code-test x/5; it says whether the test has power at letter-code n (10-15 runs). It is
not a gate for the 24 (their n is mostly 2-7), and the n of each of the 24 is reported beside its p so a low-n FAIL reads as
"untestable at this n" where the minimum achievable p is above the BH threshold.

**Actions (fixed in advance).**
- per-code PASS: key.tsv note gets "per-code PASS (R9-MANTPC, p=..., BH q 0.10)"; grade stays M (S needs a verifier).
- per-code FAIL with raw p_v < 0.10: kept at M, note "per-code FAIL (R9-MANTPC, p=..., not BH-significant)".
- per-code FAIL with raw p_v >= 0.10 (no better than chance even uncorrected): **removed from key.tsv**; the row is logged in
  HYPOTHESES.md with its p; `tools/decode_key.py . --check` regenerates and must exit 0; U count recounted.
- No code is added or re-valued by this test.
