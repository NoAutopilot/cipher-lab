# NOX-ALN pre-registration (account 3 worker, 4 Oct 2026; committed before any alignment on the settled labels is run)

Brief: `.claude/briefs/runs/2026-10-04-acct3-nox-aln.md`. Script: `aln/nox_aln.py` (imports `run2/nxaln/nxaln.py` unchanged).

## Target (same pipeline, only the symbol ids change)
RUN2-NXALN's atlas instrument exactly (train c510-513, held-out c514-516, Dupuy 221R-226R stream, `run_pipeline`, rng seed 1574,
nulls a/c 200 draws, b 40 draws gated on max), with each tile's `cluster` replaced by the owner's `new_sign` from
`settled_labels.tsv`; BAD-CUT tiles dropped; tiles absent from settled_labels.tsv keep their atlas cluster. "Before" is the
committed RUN2-NXALN result (`run2/nxaln/results/target_atlas.json`, acc 0.363), not re-run.

## Matched random-merge control (rule 3: can differ from the owner on this statistic, since it changes which piles share a symbol)
20 sets of 18 merges drawn with NOX-OWNERSORT's size-matched rule (`nearest`, 8 nearest piles by tile count, seed 20261004+set),
the owner's 36 moves and 4 bad cuts applied identically; per set the target accuracy only (no nulls). Reported: owner's
delta acc (after - before) and its rank among the 20 random deltas.

## Licensing design control
RUN2-NXALN's design control (Tomokiyo shape) at the post-sort pile count, n_clu = 108, impurity p = 0.40 (NOX-OWNERSORT: the
sort left impurity unchanged, so 40% stays the matched bracket), seeds 0, 1, 2, 50 draws. Licensing seed: 0. Also p = 0.25 seed 0
for the curve.

## Gate
After-sort target passes iff acc > null a p99, > null c p99, > null b max (as RUN2-NXALN). It counts as a test only if the
108-pile design control at p = 0.40 seed 0 passes its own gate; otherwise "non-test at this noise", not a negative.
Two-reader impurity / disagreement before vs after: quoted from NOX-OWNERSORT `nox/impurity.tsv` (same settled labels, same
200-set random-merge control); err_2reader is unchanged by a sort.

## Step 3 (refine next_targets.tsv)
Expected change to the reading, per candidate pile: number of the pile's tiles that the after-sort train alignment places on a
letter other than the pile's modal letter (aligned mass that a split could redirect), times the pile's reader-visible mix
(NOX-OWNERSORT P2). Tiles: from NOX-OWNERSORT's 40, keep those in the chosen <= 3 piles first, then by the same ranking; one-line
reason each; sids to `targets.json`. Exploratory, not a gate.
