# N8-NOX basin test pre-registration (LANE-NEAR8 worker N8-NOX, account 2, 4 Oct 2026, committed before any basin statistic)

Brief: `.claude/briefs/runs/2026-10-04-ytbiz-near8-wave2.md`, job N8-NOX. Script: `aln/basin.py` (imports `nox_aln.py`,
`confirm.py`, `run2/nxaln/nxaln.py` and `tools/stream_align.py` unchanged). Inputs: NOX-CONFIRM's 20 alternative single merges
(`results/confirm_alts.json`) and their held-out accuracies (`results/confirm_alt_*.json`), fixed before this file.
Question: NOX-CONFIRM found 8 of 20 single merges also lock onto Dupuy 521 221R-226R. Do the locked runs learn one common key
(a property of the stream), or does each lock on with its own key?

## Run sets (fixed from NOX-CONFIRM's numbers, not chosen after seeing any key)
- LOCKED (L): the six alternatives at held-out acc >= 0.50: alt 04 k014->k048, 05 k014->k017, 06 k014->k031, 08 k014->k010,
  12 k108->k077, 14 k017->k077. The target k014->k077 (0.630) is reported as a secondary 7-run figure, not gated.
- NON-LOCKING (NL): the twelve alternatives that failed the NOX-CONFIRM gate (acc 0.353-0.401): alt 01, 02, 03, 07, 09, 10,
  11, 13, 15, 17, 18, 19. The two marginal passes (alt 00, 16) are in neither set.
Each run: owner settled labels + its one merge, `sa.learn` on the train stream (c510-513) against `nx.dupuy_stream()`
(deterministic), key = `sa.decode(counts)` (argmax letter per pile, -1 if no train tokens).

## Step 1 statistic (basin)
agreement(i, j) = share of shared piles on which key_i and key_j give the same letter. Shared piles: pile names present in both
runs' inventories, not a source or target of either run's merge, decoded (not -1) in both. S(set of 6) = mean over the 15 pairs.
Secondary (reported, not gated): the same weighted by each pile's train-token count; the 7-run S with the target added.

## Step 1 nulls (each can differ from L by construction: different alignments of the same inventory family)
- N1 non-locking, same N: S over every 6-subset of NL (924 subsets); gate = p99.
- N2 shuffled Dupuy, same six merges: the words of the Dupuy 221R-226R stream are shuffled (one shuffle per seed, the same shuffle
  for all six merges of that seed), each of the six L merges is re-learned against it, S computed; seeds 1..10; gate = max.
**Step 1 PASS iff S(L) > N1 p99 AND S(L) > N2 max.** Otherwise FAIL, both numbers reported, and step 2 is not run.

## Step 2 (only if step 1 PASSes): key_learned vs key.tsv (Tomokiyo)
Bridge: the atlas piles carry no key.tsv value directly; the only bridge is `run2/nxatl/cluster_provisional_names.tsv` (each
cluster's majority c262 tile label, itself Tomokiyo's key applied to c262, grade M). Scored piles: those with a single-letter
provisional label (lowercase letter + homophone index, e.g. `n1`; `o1/e2` counts as o or e; `W:`/`N`/`D` labels and nulls
excluded), support >= 3, purity >= 0.40, present after the owner's sort under the same name and not merged away in any L run.
Consensus key: per scored pile, the letter the majority (>= 4 of 6) of L runs give; piles without a majority are dropped.
Statistic K = share of scored piles where the consensus letter equals the provisional letter.
Nulls: (a) permutation: consensus letters shuffled across the scored piles, 10000 draws, p99; (b) non-locking: the same consensus
rule (>= 4 of 6) on every 6-subset of NL, K computed on the same scored piles where that subset has a majority, p99 over 924.
**Step 2 PASS iff K > (a) p99 AND K > (b) p99.** A PASS licenses only "the locked basin's key agrees with Tomokiyo's key beyond
chance"; every value stays grade M, no reading is claimed, no key.tsv change.
