# PREREG-SUR372 -- key test on NA 1.05.03 inv. 372 scan 0189 right page (SUR-372, 9 Oct 2026, account 2)

Written 21:5x UTC 9 Oct 2026 (date -u), BEFORE any blind transcription pass and before any decode or score.

## Premise (what this test is)
The letter at inv. 372 scans 0183-0195 (Paramaribo 26 July 1780, docket "Rec. Oct. p[er] Lands Cap. Oorlog Mulder")
carries a lighter interlinear plain Dutch gloss line above every cipher line (seen at 1600 px on 0183, 0189, 0195).
It is therefore N0 by construction: this is a **key test** (does each period key read the cipher into the gloss), not
a reading. Disclosure: at the 1600 px look the worker saw that the first cipher group of 0189 R line "4." spells HET
under the Nieuw sheet's E and T signs; no other token was decoded before this file was pushed.

## Unit
0189 right page, crops images/sur372/372_0189_right_native_L01..L27 (tools/iiif_lines.py, native region
pct:50,4,48,80 of the scan): about 14 cipher lines and 14 gloss lines.

## Transcription
Two blind Sonnet passes (A, B), each given only the crops and a neutral sign inventory (shape names, no values, no key,
no folder files). Each pass reads every crop: cipher signs as codes, and the gloss words as written. One reconciliation
(R) by this worker from the crops, settling A/B disagreements on cipher signs only, before any decode. Agreement rate
A vs B (cipher codes, aligned per line) reported beside every result.

## Keys
- Oud: key_period.tsv (inv. 86 scan 0002). Nieuw: key_period_nieuw.tsv (inv. 86 scan 0003, sent 2 Dec 1739).
- Reader code -> value tables fixed in score_sur372.py BEFORE the passes return, from the sheets' shape names only.
  Codes a key has no sign for decode to '?'.

## Statistics (each computed per key, on A, B and R separately)
Normalisation for all text: lowercase a-z only; ij/y/j -> i; v -> u; clear words written in clear inside a cipher line
({...}) dropped from the decode; abbreviations in the gloss left as written (both sides letters-only).
- **S1 gloss agreement (primary).** difflib.SequenceMatcher ratio between the page's decoded letter string and the
  page's gloss letter string (gloss as read by the SAME pass), lines concatenated in page order.
- **S2 Dutch judge (secondary).** tools/judge_plaintext.py with the nl18 corpus (tools/data/nl18: Dutch prose 1770-1799,
  colonial/official register -- era-matched; its own README reports a leave-one-file-out FN spread of 6-76% at N~250,
  so a judge result is of unknown reliability and cannot decide the key on its own).
- **S3 word hits.** share of decoded words (split at the pass's own '_' gaps; words of >= 2 letters) present in the nl18
  word list (types with count >= 3).
## Nulls (200 each, seed 372)
- key-shuffled: the key's sign->letter values permuted among its signs, decode, statistic.
- shuffled-target: the page's cipher tokens permuted (order only, real key), decode, statistic. For S1 this changes
  order, which the ratio measures, so the control can differ from the target (rule 3 non-test check passed by design).
## Gate
A key **reads** this page iff S1(real) > p95 of BOTH nulls on pass A AND on pass B (R reported, not gating).
S2: PASS is counted only if the shuffled-target decode does not also PASS (rule 3, ARM-C1); reported, not gating.
S3: real > p95 of both nulls, reported beside S1.
A key that fails is a negative for that key on this page only, conditional on the transcription agreement rate.
## Grades (rule 4)
If a key reads: tokens whose decoded letter matches the gloss at the SequenceMatcher-aligned position -> C (gloss is
the known plaintext); others M. (Brief's H-where-key-is-H applies to unglossed text; on a glossed page the gloss is C.)
No grade if no key reads.
