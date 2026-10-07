# PREREG D07-NOX510: split-pile c262 tiles bounded, then c510-516 through the 19-pile bridge vs Dupuy 221R-226R

Written 7 Oct 2026 01:14-01:2x UTC by date -u, before any decode statistic was computed. Worker D07-NOX510 (LANE
DEFAULT-account-1-20261007-0042, account 1). Script: `nox510.py` (same folder). No input below is changed after scores are seen.

## Part 1 -- the 14 split-pile c262 tiles (reported, not gated)
No tile features are on disk for c262 (the glyph_atlas segment output was scratch-only) and the brief's vision allowance is for tiles a
script cannot place. Instead of guessing one placement, bound it: re-run D07-NOXT's EM + bridge filter (`bridge_ownerpiles.py`, imported
unchanged) with the 14 tiles (`d07noxt_summary.json` `split_parent_tile_ids`) placed (a) all at the parent (= D07-NOXT), (b) each parent
group sent whole to each of its split children (k006 -> k006-b/-c/k087-d; k072 -> k072-b; k087 -> k087-b/-c/-d), (c) 200 uniform random
placements over {parent + children}, Random(510). Report the distinct bridged sets (pile -> letters) that occur and how often.
If every placement gives D07-NOXT's 19-pile bridge unchanged, the placement cannot move Part 2 and the 14 tiles are recorded as
"bounded, not placed" (no eye pass). If any placement changes the bridge, Part 2's primary still uses D07-NOXT's 19-pile bridge and every
distinct variant bridge is scored the same way, reported beside it.

## Part 2 -- decode of c510-516 through the bridge (gated)
Stream: `run2/nxatl/sequences.tsv` rows for leaves c510-c516 in file order (leaf, line, pos), each tile's owner pile from
`settled_labels.tsv` `new_sign`; tiles absent from settled_labels or status bad-cut dropped. Decode: a tile whose pile is in the bridge
(`d07noxt_summary.json` `bridged_after`, values = key.tsv letters through the c262 reader labels) emits its letter set (y -> i by test0's
norm); every other tile is left unread (emits nothing). Reference: `run2/nxdup/dupuy221_226_norm.txt`, pages joined, test0 `norm()`,
starting after the first "icelle que" (the clear lead-in on c510 L01-L05 ends there; RUN2-NXATL step 3).

Statistic: R = 2*LCS(dec, ref)/(|dec|+|ref|), exact bit-parallel LCS (test0's `lcs_len`), set-aware: a token with set {e,o} matches a
reference e or o. Nulls, 200 draws each, Random(16142):
 (k) key-permuted: the 19 bridge values permuted among the 19 piles (same piles read, same counts, letters moved);
 (o) order-shuffled: the decoded token sequence shuffled (same letters, order destroyed).
Both can vary R (k changes which letters appear, o changes their order).
**Gate: PASS if R(target) > max of (k) AND > max of (o).** Else FAIL ("the 19-pile bridge does not read c510-516 toward Dupuy beyond
these nulls at this transcription"). An (o)-PASS with a (k)-FAIL is reported as order signal not attributable to the key values.

Secondary (reported; licenses per-token grades only): the LCS path (numpy DP, ties broken diagonal-first) and the number of decoded tokens
in contiguous matched runs of length >= 4 (consecutive dec tokens matched to consecutive ref letters). The same count on each (o) draw.

## Grades (rule 4)
H 0, C 0 throughout (no key source read on this leaf; Dupuy is a clear copy used only as the scoring reference, not as a crib per token).
If the gate PASSes AND the run count beats the (o) p99: tokens in runs >= 4 are S, all other decoded tokens M. Otherwise every decoded
token is M. Unread tiles are not graded (no reading). No reading is written into key.tsv or gloss.tsv; outputs go to
`results/d07nox510_*.{json,tsv}` with `nox510.py check` (rule 7) exiting 0.

Conditional on: RUN2-NXATL's segmentation (tiles != signs, ~1.05), the owner's quick-pass merges, one reconciler's c262 labels,
and D07-NOXT's bridge (thin, H 10/19).
