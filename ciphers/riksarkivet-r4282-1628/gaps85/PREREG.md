# GAPS85 pre-registration (3 Oct 2026, account-4), written and committed before any run

Hypothesis: R4282 is enciphered with the key the R4284 key-test leaf demonstrates (clear word over cipher word, one
sign per letter, a few homophones), so the sign -> letter key built from the GAPS79 reconciled strip makes R4282's
sign stream read as Latin.

Key (built by `crib_key_v2.py`): pairs only from strip words whose sign count equals the clear word's letter count
(no truncation; bRIK truncated mismatched pairs). Sign -> majority clear letter (ties: alphabetical). Letters i/j and
u/v merged. Two label rules fixed now, from the transcriptions, not tuned:
- kt2 sign 1 is `L` (Bourdeau's own capital in "Ltsico"; passA lower-cased it), R4282 keeps L and l apart.
- the strip's flat-topped s label (kt2 c3, kt4 c3, the s/5 shape split GAPS79 recorded) maps to R4282's `5`; every
  other strip `s` stays `s` (absent from R4282, so uncovered). Secondary arm without this rule reported, not gated.

Arms (gated): A1 = passC_reconciled.tsv; A2 = passC_variant_kt3_onesign.tsv (kt3 word 2 as one sign).
Target stream: tx2/ciphertext_reconciled.tsv (GAPS38, 1,090 signs), per line.

Statistic S: mean log-probability per adjacent covered sign pair (both signs in the key, same line) of the decoded
letter bigram under an add-one smoothed 24-letter bigram model of tools/data/la17 (all files).

Control (can differ on S's own axis): shuffled pair assignment -- the clear letters of all aligned pairs permuted
across the pairs (the same signs, the same letter multiset, coverage identical), key rebuilt, S recomputed;
2,000 permutations, seed 85. p = share of permutations with S >= real.
Gate per arm: PASS if p < 0.05. Both arms reported; a PASS in only one arm is reported as that arm only.

Positive control (licenses a negative): 5 la17 passages of 1,090 letters (seeds 1-5, from the same files),
enciphered letter -> majority sign of the A1 key (letters with no sign -> a placeholder sign outside the key,
uncovered), then 3.4% random sign substitution (GAPS38 err_2reader); same statistic, same 2,000-permutation test.
Control passes if p < 0.05 in at least 4 of 5. If it fails, the target result is a non-test, not a negative.

Grades (rule 4): a decoded letter is C only where the sign's value comes from the strip's own clear words; any
reading claim needs PASS; no PASS -> no reading, no grades beyond "C-valued sign map", read 0 signs.
