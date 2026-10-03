# BIR-ROUND2 pre-registration (3 Oct 2026, 12:39 UTC, account-3 worker)

Brief `.claude/briefs/runs/2026-10-03-acct3-bir-round2.md`. Written and pushed **before** `prereg_round2.py` is run, before any
crop is cut and before any score (lattice, posnull, reader, judge). Same instrument as A1-BIR-EYE / A1-BIR-VERIFY (which passed on
f.117r and f.168), now pointed at the M tokens. Targets: f.117r (fr.3252 no.77), f.168 and f.144r (fr.3251).

## Base and candidates (`prereg_round2.py`)
- The 24 A1-BIR-VERIFY survivors (`../verify/exceptions_{f117,f168}.tsv`) are pinned to their key-implied sign.
- H positions are pinned to the top-1 sign (f.117r/f.168: top-1 prior >= 0.85, as `../verify/build_decode.py`; f.144r: committed conf).
- M positions keep the TX-DECODE lattice candidates (both readers' signs and alts, `../../{leaf}_topk.tsv`) plus the top-2
  `confusion_1572.tsv` partners of the top-1 sign (the look-alike pairs of `tools/lookalike_pass.py`) where missing, at 0.03,
  renormalised, top 5 kept.
- `tools/key_decode_lattice.py` viterbi, printed 1572 key `key_1572_sheet.tsv`, lam 4, beam 64; LM fr for f.117r, it16dip for
  f.168/f.144r (round 1's settings). Changed positions **not asked in either earlier read** are the round-2 questions
  (top-1 vs key-implied). Positions asked before (incl. f.144r's 4 dropped candidates) are not re-asked; their count is reported.
- Ambiguity-matched decoys ('mdecoy'): unchanged M positions not asked before with best-alt/top-1 ratio >= 0.3, seeded sample
  (seed 20261005), as many as the leaf's changed questions (all, if the pool is smaller). A/B order and question order seeded.

## Reader
One fresh blind Opus subagent per leaf (<= 3 calls, + at most 1 reconciliation call; cap 4). It sees only line crops (commands
pasted in RESULTS-ROUND2.md before the first call; f.117r at the original band height as A1-BIR-VERIFY; scratchpad, never the repo),
`harvest/sign_sheet_blind_1572.png` (ids only), `r2blind_<leaf>.tsv` and `r2orient_<leaf>.txt` (top-1 sequence, every question
masked). Never told of a key, a decode, earlier reads, or which candidate is which. Answers A / B / U with conf H/M/L.

## Gate per leaf (`score_round2.py`)
c = changed answered key-implied, d = mdecoy answered swap. **PASS iff c/n_c > d/n_d AND binomial P(X >= c | n_c,
p0 = (d+1)/(n_d+2)) < 0.05 AND the position-shuffled-lattice null passes on the round-2 base** (`r2posnull.py` = A1-POSNULL's
`posnull.py` with only the input lattice changed: 200 shuffles, seeds 1000-1199, PASS iff real key rank 1/201 among 200
value-shuffled keys AND real S > shuffled-S p95). A leaf with fewer than 3 changed or 3 mdecoy questions is "untestable at this
N", not a FAIL. Survivors: changed positions on a passing leaf picked key-implied at H or M -> applied at S via `exceptions_r2_<leaf>.tsv`
(on top of the 24), then `tools/decode_key.py --check` and `tools/judge_plaintext.py` per leaf. A failing leaf keeps none.

## U tokens (step 2)
List every X_* / '?' / uncovered sign per leaf with counts and line context; compare by shape description with the printed key's
word codes and nulls (`../../../../keys/key_nevers_birago_1572.tsv`, `key_1572_sheet.tsv`) and `harvest/offsheet/` fits. Report only;
no value is guessed or applied.

No reading claimed beyond S, no H/C, no novelty classed.
