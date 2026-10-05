# RUN6-NOXDEC pre-registration (LANE-RUN6 worker, account 1, 5 Oct 2026, committed before any decode statistic)

Brief: `.claude/briefs/runs/2026-10-05-acct1-run6-wave1.md`, job RUN6-NOXDEC. Script: `aln/decode262.py`. Disk only.

## Leaf
c262 (the NX-RECUT block, 403 atlas tiles in `run2/nxatl/sequences.tsv`). Chosen over c511 because c511 is a TRAIN leaf of the
Dupuy alignment (`nxaln.TRAIN_LEAVES` = c510-c513): the basin key was learned on it, so it is not "a leaf not aligned to Dupuy".
c262 is the only atlas leaf the basin never saw, and it carries an independent period interlinear gloss (`gloss.tsv`).

## Key and decode
Tile -> pile: the tile's k-means cluster, then the owner's 18 merges (`../summary.json` 'merges', applied once; c262 has no
per-tile settled row). Key: N8-NOX2's count-based consensus (`keytie.consensus`, unchanged) of the six locked runs L (alt 04, 05,
06, 08, 12, 14 from `results/basin_keys.json`, no re-learning) over EVERY pile, not just the 17 bridge piles. A pile with no vote,
or whose consensus value is < 0, yields nothing. Decode = letters in tile order (sequences.tsv order: line, pos).
Nothing from key.tsv, the c262 bridge labels or the gloss enters the key.

## Statistic (the one the target already uses)
`scripts/test0.py`'s statistic: difflib SequenceMatcher ratio (autojunk off) between the normalized decode and the normalized
concatenated gloss (test0.norm: lower case, u=v, i=j=y, accents folded, letters only). Call it R.

## Controls (each can differ from the target on R -- rule 3 orthogonality check)
- (a) shuffled key: the consensus key's letter values permuted across its piles, 1000 draws, seed 20261005; gate p99.
  Can differ: R depends on which letter each tile yields.
- (b) letter-order shuffle: the target decode's letters permuted (same multiset, order destroyed), 1000 draws, seed 20261005;
  gate p99. Can differ: R (a matching-block ratio) depends on order; this null keeps the decode's own letter frequencies exactly.
- (c) shuffled Dupuy: the same count-based consensus over the six L merges learned against word-shuffled Dupuy (N8-NOX's
  shuf01..shuf10 keys on disk), 10 seeds; gate max. Can differ: those keys carry French frequencies but not Dupuy's sequence.
- (d) non-locking: the same consensus over every 6-subset of the 12 non-locking runs (924); gate p99. Can differ: NL keys disagree
  with L (N8-NOX step 1, 0.207 vs 0.601).
Reported, not gated: R of each L run alone; R of c262 tiles under the bridge's provisional (Tomokiyo-key) labels where they exist
(a ceiling reference for this tile stream); the NX-RECUT reconciled transcription's 0.4548 is a different token stream, quoted only.

**PASS iff R > (a) p99 AND R > (b) p99 AND R > (c) max AND R > (d) p99.** Otherwise FAIL, all numbers reported. A PASS licenses
only "the Dupuy-learned basin key reads the unaligned c262 block toward its own period gloss beyond chance and beyond shuffled-text
and non-locking keys"; it does not grade any token above M by itself (the gloss is the period decipherment, so C grades would need a
per-token alignment, out of this brief). A FAIL is a negative on this key at this tile stream, conditional on the atlas tiling
(1.05 tiles/sign on c262) and on the owner's merges.
