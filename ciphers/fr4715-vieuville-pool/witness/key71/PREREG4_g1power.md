# Pre-registration 4: known-answer power check of gate G1 (GAPS83-fr4715-vieuville-pool, account-4)
Written 3 Oct 2026 (clock read 10:5x UTC), committed and pushed BEFORE scripts/g1_power_check.py is run.
Question: can the G1 instrument of PREREG3.md (tools/interlinear_align.py align, flat start, --floor 100 --keep-fs,
statistic A/S against Tomokiyo's table, PASS = S >= 12 and A/S >= 0.70 and A > p99 of 10,000 value permutations)
reach its own gate on input whose answer is known? If not, G1's two FAILs (GAPS-16 5/32, GAPS82 8/30) are non-tests
(CLAUDE.md rule 3: a gate the control cannot reach licenses nothing).

## Material
The 22 plain_raw gloss texts of witness/f4712_7r_pairs_img.tsv (GAPS82), unchanged. Normalization: NFKD to ASCII,
lowercase, j->i, v->u, letters only; letters with no numeric code in Tomokiyo's table (k, w, x, z) dropped.

## Conditions (20 seeds each, seeds 1-20)
- K1 clean: every letter -> a Tomokiyo numeric homophone chosen uniformly at random. The noiseless ceiling.
- K2 leaf-like: K1, then each gloss word replaced by ONE marked code (d/t/b uniform, number 1-99 uniform) with
  probability 0.15 (= 18 marked tokens / 120 gloss words measured on the img pairs file), then each unmarked token
  substituted by a uniform random code 1-99 with probability 0.10.
- K3 noisier: as K2 with substitution probability 0.20 (brackets the unmeasured transcription error, rule 3 headline).
Each synthetic pairs file goes through scripts/f4712_7r_gates.py's own numeral mapping and alignment call, imported
unchanged; A, S and the permutation p99 are computed by the same code path (G2 is not run).

## Read-out
Per condition: median, min and max of A/S; median S; G1 PASS rate over the 20 seeds.

## What each outcome means (fixed now)
- K1 PASS rate < 0.5 (or median A/S < 0.70): the aligner cannot reach the gate even on a perfect transcription.
  G1 is untestable-by-this-aligner at this N; the flat-start aligner is [retired] for this gate (rule 3 third-attempt
  clause); the GAPS-16 and GAPS82 FAILs are non-tests, not negatives. Named different instrument: fixed-key scoring --
  apply Tomokiyo's key directly to each f.7r cipher run (no alignment learned) and score letter agreement with its
  gloss by edit-distance alignment against a permuted-key control.
- K1 passes but K2 PASS rate < 0.5: the gate is reachable only on a clean, mark-free transcription; at the leaf's own
  structure it is a non-test, same consequence as above.
- K1 and K2 both pass (rate >= 0.5): the gate is reachable at leaf-like structure; the two FAILs stand as real
  FAILs of the f.7r pairing at its current transcription (still not a negative on key no.71 or the slots); the
  instrument is not retired by this check, but rule 3's third-attempt clause still bars a third reconciliation.
K3 is reported for the record and does not change the verdict.
