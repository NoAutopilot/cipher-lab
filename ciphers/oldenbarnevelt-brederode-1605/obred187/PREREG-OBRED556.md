# PREREG-OBRED556 (15 Oct 2026, 07:0x UTC by date -u; written before any scan 555-557 is fetched or any number computed)

Question: is the numeral block on NL-HaNA 1.01.02 inv. 6019 scan 556 (about Oct 1619, found by OBRED-6019B) in the same code list
as no. 92 (Heidelberg, 21 Feb 1605) and the scan-187 postscript (Stettin, 17 Oct 1604)?
Known before writing this: OBRED-6019B's single provisional read at 1200 px (32 groups, all M), which lists by eye
578 605 457 13 289 797 798 433 461 385 50 73 193 458 67? 390 415 202 109 593 594 430 100 169 110 241 337 120 380.
Several of these (289 433 461 241 337 110 578) are visible in no. 92 / 187. This gate is built so that an overlap of that size can fail.
The provisional read is NOT an input: the inputs are the two blind passes below.

Inputs (frozen):
- V556 = distinct numeral values in `ciphertext_556.tsv` (the reconciled two-pass transcription of the numeral groups on scans 555-557;
  all grades; clear words and glosses excluded). n556 = token count. Sensitivity row: H-read tokens only (reported, not gating).
- R = V92 | V187, the distinct values of no. 92 (`obred187/overlap.py` v92()) and of `ciphertext_187.tsv` (v187(), all grades); 130 values.
- Statistic S = |V556 & R|.

Controls (10,000 draws each, numpy seed 556), each a shuffled/replaced code that can differ from the target on S:
- C1 uniform: n556 values iid uniform on 1..M, M = max(max V556, max R); S of the distinct set against R.
- C2 band-matched: each 556 token replaced by a uniform value in its own hundred band (1-99, 100-199, ...); S against R.
- p = (1 + #{S_null >= S_obs}) / (1 + 10,000).
- Negatives, as PREREG-OBRED187: N1 Lodewijk 7206 (sign column), N2 Jan van Nassau 5551 (numerals); 10,000 subsamples of n556 tokens
  (without replacement; with replacement if shorter); S against R; mean and 95th percentile.
- Power (positive control, CLAUDE.md rule 3 last paragraph: subsampled to the target's own N): 10,000 subsamples of n556 tokens from
  187's tokens, S against V92 only, scored against a C1 run against V92 at the same n (its p99). Power = share of subsamples whose S
  exceeds that p99. If power < 0.50, a miss is logged "untestable at n556", never a negative.

Decision rule: "overlap clears its control" iff p < 0.01 under BOTH C1 and C2 AND S_obs > the 95th percentile of BOTH negatives.
If it clears: "consistent with one code list shared by no. 92, the 1604 postscript and the 1619 scan-556 block", grade M, never a reading.
If not and power >= 0.50: "no evidence of shared values beyond range and histogram at n556". If not and power < 0.50: untestable at n556.

Glosses (descriptive, no gate): the interlinear/marginal glosses are read once (Opus) and checked once (Sonnet), graded C only where
both agree on the gloss and it sits unambiguously over one group. Reported per glossed group: value, gloss, whether the value is in R,
and whether a glossed proper name falls in no. 92's name band 588-751 (OBRED-DP G2). No key.tsv edit; a glossed pair enters any key
only through the folder's own path with a passing control (rule 3, per-unit merge).

Script: `obred187/overlap556.py` (`--check` re-runs and fails if `obred187/overlap556.json` is stale). No decode, no key.
