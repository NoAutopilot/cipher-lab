# N8-NOX2 key-tie pre-registration (LANE-NEAR8 worker N8-NOX2, account 2, 4 Oct 2026, committed before any key-tie statistic)

Brief: `.claude/briefs/runs/2026-10-04-ytbiz-near8-wave3.md`, job N8-NOX2. Script: `aln/keytie.py` (reads `results/basin_keys.json`
from N8-NOX unchanged and imports `basin.py`'s step-2 bridge rule unchanged; no re-learning). Disk only.
Why re-registered: N8-NOX step 2 used a >= 4-of-6 majority consensus; the non-locking control reached a majority on only 0-6 of the
17 bridge piles, so its ratio sat near 1.0 by small N and could not fail differently from the target (rule 3, orthogonal-control
paragraph). This file replaces that consensus with a count-based one that is defined on every scored pile for every run set.

## Scored piles (unchanged from PREREG-BASIN step 2)
The 17 piles of `run2/nxatl/cluster_provisional_names.tsv` that pass basin.py's step-2 filter (single-letter provisional label,
support >= 3, purity >= 0.40, present in all six L runs, not merged in any L run). Provisional letter set per pile as there.

## Count-based consensus (the new rule)
For a run set R and a scored pile p: each run r in R that decodes p (value >= 0) and whose own merge does not touch p (p neither
source nor target of r's merge) casts a vote for its letter weighted by its train-token count on p (`key[p][1]`). Consensus(p) =
letter with the largest summed weight; ties broken to the lowest letter index. A pile with no vote has no consensus (counted as a miss).

## Statistic
H(R) = number of the 17 scored piles where Consensus_R(p) is in p's provisional letter set (a count over a fixed denominator of 17).
Target: R = L (alt 04, 05, 06, 08, 12, 14). Reported, not gated: L + target (7 runs), and H for each L run alone.

## Controls (each checked below that it can differ from the target on H)
- (a) permutation: the 17 provisional letter sets permuted across the 17 piles (consensus fixed), 10000 draws, seed 20261004; gate p99.
  Can differ: H under a permutation depends on which letter set lands on which pile.
- (b) non-locking: the same count-based consensus over every 6-subset of NL (alt 01, 02, 03, 07, 09, 10, 11, 13, 15, 17, 18, 19;
  924 subsets), H on the same 17 piles; gate p99. Can differ: NL keys disagree with each other and with L (N8-NOX step 1: NL 6-subset
  pairwise agreement mean 0.207), and the consensus is defined on every pile with any vote, so the denominator is 17 for every subset.
  Pre-registered degeneracy check: if the 924 values of H(NL subset) take fewer than 3 distinct values, or more than 10% of subsets
  leave more than 3 of the 17 piles without a vote, control (b) is declared non-discriminating, the result is NON-TEST, not PASS/FAIL.
- (c) shuffled Dupuy (reported, gated as a third condition): H of the count-based consensus of the six L merges learned against
  word-shuffled Dupuy (N8-NOX's shuf01..shuf10 keys, already on disk), 10 seeds; gate max.

**PASS iff H(L) > (a) p99 AND H(L) > (b) p99 AND H(L) > (c) max, and (b) is not degenerate.** Otherwise FAIL (or NON-TEST), all numbers
reported. A PASS licenses only "the locked basin's count-based key agrees with Tomokiyo's key (via the c262 bridge) beyond chance and
beyond non-locking and shuffled-text runs on the 17 bridge piles". Every value stays grade M either way: the bridge labels are
themselves Tomokiyo's key applied to c262 (grade M), no reading is claimed, key.tsv is not changed. Grades move only at a later decode
of a leaf not aligned to Dupuy, with its own control.
