# PREREG SUR-SPLITPC (9 Oct 2026, 03:2x UTC by date -u; pushed BEFORE splitpc.py's draws are run; splitpc.py is pushed with it, unchanged after)
LANE FAMILY-A2e (account 2), job SUR-SPLITPC. Question (AUDIT.md "V-SUR0745" 5(i)): does SUR-0745's (b) SPLIT statistic have the power to
read LEANS n on a unit of 0745 LEFT's size when the y-family really carries n only? CPU only, no transcription, no fetch.

## Design (splitpc.py, committed with this file; score.py's functions loaded unchanged)
- Synthetic unit, per pass scaffold (A, B separately): 22 gloss lines bootstrapped (with replacement) from that pass's own 22 gloss lines;
  each gloss letter deleted with that pass's real unaligned-letter rate (A 0.086, B 0.093), else enciphered with a code drawn from the codes
  that face that letter in that pass's real DP alignment (so the reader's and the aligner's own noise come along), and followed by an inserted
  sign drawn from the pass's real unaligned signs at its real insertion rate (A 0.144, B 0.131). Size and noise matched to 0745 L.
- **H1, planted split of the size the hypothesis predicts** ("the y-family is an n sign only; m is written otherwise"): every m whose drawn
  code is [y-fam] is written with a sign `Mx` that is not in T, so before alignment the y-family faces n only (S_true = 1.0). n keeps its real
  facing distribution ([y-fam] ~61%, l, 4, ...). 200 synthetic units per scaffold.
- **H0, no split** (descriptive false-positive check): m and n both keep their real facing distributions. 50 units per scaffold.
- Each unit scored exactly as score.py (b): T with the [y-fam]={m,n} steer, S = n/(m+n) over y-family tokens aligned to gloss m|n, against
  K = 300 deranged-gloss C1 draws of that unit (fewer than score.py's 10,000 for CPU; p99.5 is the 3rd-highest of ~300, stated);
  LEANS n iff S > p99.5, LEANS m iff S < p0.5; non-test iff m+n < 10, < K/2 usable draws, or p0.5 == p99.5. Master seed 20261009.
- Before this file: one smoke synthetic H0 unit (seed 5) was built for timing and its A only was read (0.871 vs real 0.914); no SPLIT
  verdict was computed on any synthetic unit.

## Gate (per scaffold; unit verdict needs both)
Detection = share of the 200 H1 units reading LEANS n. **Detection >= 0.80 on both scaffolds**: SPLIT's NO SPLIT SHOWN on 0745 L (both
passes) is a negative with measured power against a full n-only split. **Detection < 0.80 on either**: SPLIT on 0745 L is a non-test at this
N for that alternative. H0 LEANS (either side) rate is reported, not gated. Stated limits: only the full split is planted (a partial
preference is not measured); the facing distributions come from the steered aligner, so the control inherits the steer as the target does.

## Consequences
Whatever the result: no edit to key.tsv, key_period_*.tsv, conflicts.tsv, any transcription file, token grade, score.out, or N-class.
HYPOTHESES.md row with both numbers, NOTES section, gaps_check. Rule 10: report only.
