# PREREG D07-NOXT: c262 tiles placed under the owner's piles (widened atlas-pile -> key.tsv bridge)

Written 7 Oct 2026 by the D07-NOXT worker (LANE DEFAULT-account-1-20261007-0042, account 1), pushed before any count below is computed.
Script: `bridge_ownerpiles.py` (this folder). Disk only, no requests, no subagent unless step 0 leaves tiles a script cannot place.

## Construction (not a test)
0. Each c262 tile (run2/nxatl/sequences.tsv, leaf c262; 403 tiles) gets an owner pile: its atlas cluster mapped through the owner's 18
   merges (`summary.json` "merges", one hop). Tiles whose cluster the owner split (k006, k072, k087 -> -b/-c/-d) stay at the parent id
   and are listed (no tile features on disk to place them by script). The owner sorted only c510-516 tiles; c262 tiles were never in
   the sorter, so this is placement by cluster, not by the owner's eye.
1. Re-run `run2/nxatl/c262_align.py`'s hard-EM Needleman-Wunsch unchanged (GAP 2, 15 iterations, proportional start) with the owner
   pile as the cluster id, against `witness/c262rc_recon.tsv`; output `results/d07noxt_provisional_owner.tsv` and the tile alignment.
2. A pile is **bridged** under the same filter as basin.py step 2 / keytie.py `scored_piles`: majority label a letter label (not W:, N,
   D), purity >= 0.40, support >= 3, pile present in all six locked basin keys and not merged away by any locked run's own `extra`.

## Primary number (reported with its control, gate stated in advance)
B_after = number of bridged piles. B_before = 17 (N8-NOX / keytie). Control: the same EM with owner-pile ids permuted among the c262
tiles (counts kept; c262_align.py's own `--shuffle` null), seeds 1-20, same filter -> B_null. The widening is counted real only if
B_after > max(B_null) and B_after > 17; otherwise "the merge-placement does not widen the bridge beyond chance".

## Secondary (gate copied from PREREG-KEYTIE.md, reported only if the primary passes)
keytie's H (count-based basin consensus letter in the pile's provisional letter set) on the widened bridge, with keytie's controls
unchanged in form: (a) 10000 permutations of the letter sets across bridged piles (seed 20261004), (b) the 924 non-locking 6-subsets
(with keytie's degeneracy check), (c) the shuffled-Dupuy six, seeds 1-10. PASS iff H > p99(a), H > p99(b), H > max(c).
Also reported: H on the 17 old piles recomputed under the owner mapping, to show what the widening alone adds.

## Conflicts (listed, never resolved by majority)
(i) owner piles formed by a merge whose member clusters carried different provisional letters in run2/nxatl; (ii) bridged piles whose
runner-up label is a different key letter with >= 1/3 of the pile's support. Every value stays grade M; key.tsv is not changed.
