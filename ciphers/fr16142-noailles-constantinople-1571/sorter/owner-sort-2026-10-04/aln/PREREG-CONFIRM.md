# NOX-CONFIRM pre-registration (account 3 worker, 4 Oct 2026; committed before any confirmation run)

Brief: `.claude/briefs/runs/2026-10-04-acct3-nox-confirm.md`. Script: `aln/confirm.py` (imports `nox_aln.py` and
`run2/nxaln/nxaln.py` unchanged). Hypothesis under test (found post hoc by NOX-ALN): on the owner's settled labels, the single
extra merge k014->k077 makes RUN2-NXALN's atlas alignment lock onto Dupuy 521 221R-226R, and this is specific to that merge.

## Note on "fresh seeds"
`sa.learn` is deterministic: the train alignment, the learned key and the held-out accuracy (0.6298) do not depend on a seed.
The seed drives the three nulls only (a key shuffles, c wrong-text offsets, b word shuffles that are each retrained). So the
fresh-seed arm re-draws every null; reproducing acc 0.6298 exactly is the rule-7 check, not evidence.

## Arm 1: fresh seeds (target)
Owner labels + k014->k077, `run_pipeline` unchanged, nulls a/c 200 draws, b 40 draws gated on max, rng seeds 20261005,
20261006, 20261007 (NOX-ALN used 1574). Locks on at a seed iff acc > a p99, > c p99 and > b max (40) at that seed.
Arm 1 passes iff all three seeds lock on.

## Arm 2: specificity control (20 nearest alternatives)
The 20 single merges listed by `python3 confirm.py list` (`results/confirm_alts.json`): k014 -> each of the 10 owner piles
nearest k077 in tile count, and each of the 10 owner piles nearest k014 in tile count -> k077 (ties by name; k014, k077 excluded).
Each replaces k014->k077 on the same owner labels, same pipeline, nulls a/c 200, b 10 draws gated on max, rng 20261004.
An alternative locks on iff acc > a p99, > c p99 and > b max (10). Using b at 10 draws (a lower max than 40) makes it easier
for an alternative to count as locking on, so the count is conservative against the hypothesis. Also reported: how many reach
acc >= 0.50, and how many beat a and c only.
Arm 2 passes iff at most 1 of 20 alternatives locks on.

## Verdict
PASS iff Arm 1 passes AND Arm 2 passes. Otherwise FAIL (the lock-on is not confirmed as specific to k014->k077), with both
numbers reported. Either way every value from the alignment stays grade M; no reading is claimed by this job.
If PASS: state what the lock-on licenses (alignment of c510-513 against Dupuy 221R-226R, held-out c514-516), and list the
position map and candidate values from `results/full_pair_k014_k077_counts.tsv` at grade M.
