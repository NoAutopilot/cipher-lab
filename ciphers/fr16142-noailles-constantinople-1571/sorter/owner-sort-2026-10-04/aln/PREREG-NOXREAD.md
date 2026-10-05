# RUN6-NOXREAD pre-registration (LANE-RUN6 worker, account 1, 5 Oct 2026, committed before any statistic)

Brief: `.claude/briefs/runs/2026-10-05-acct1-run6-wave2.md`, job RUN6-NOXREAD. Script: `aln/noxread.py`. Disk only.
Same statistic, nulls and gate as `PREREG-DECODE.md` (RUN6-NOXDEC, commit 6de3a59e); only the token stream changes.

## Stream
c262 reconciled reader signs, `witness/c262rc_recon.tsv` (NX-RECUT, 384 signs, lines L01-L10 in order), unchanged.
A '?' sign yields nothing (as in test0.py).

## Key mapped to the signs
Label -> pile: from `run2/nxatl/c262_tile_alignment.tsv` (RUN2-NXATL's tile-to-reconciled-sign alignment, built from tiles and
recon labels only, no gloss), every row with a recon_label (not '-'); the tile's cluster goes through the owner's 18 merges
(`../summary.json`), then each label takes its majority pile (ties: lexicographically smallest pile). A label with no aligned
tile, or whose pile's key value is < 0 or absent, yields nothing. The basin key is N8-NOX2's count-based consensus of the six L
runs (alt 04, 05, 06, 08, 12, 14, `results/basin_keys.json`, keytie.consensus unchanged) over every pile; a sign decodes to the
letter of its label's pile. W: signs are treated like any other label (the basin key knows piles, not words).

## Statistic
R = test0.py's difflib ratio (autojunk off), normalized decode vs normalized concatenated `gloss.tsv` (decode262.R, unchanged).

## Nulls (identical to PREREG-DECODE.md, each can move R on this stream)
(a) consensus key's letter values permuted across piles, 1000 draws, seed 20261005, gate p99; (b) decode's letters permuted,
1000 draws, same rng, gate p99; (c) shuffled-Dupuy consensus (shuf01..shuf10), gate max; (d) consensus over every 6-subset of the
12 non-locking runs (924), gate p99. Each passes through the same label -> pile map.

**PASS iff R > (a) p99 AND R > (b) p99 AND R > (c) max AND R > (d) p99.** Otherwise FAIL, all numbers reported.

## Positive reference (reported, not gated)
Tomokiyo's published key on the same stream: test0.py's decode (letter part of each id, W: words spelled, '#' o1/e2 resolved as
e2), scored with the same R and passed through nulls (a)-(b) analogues is NOT done; quoted beside: NX-RECUT's 0.4548 and its own
nulls (key-shuffle max 0.2658, gloss-order max 0.2904). This script recomputes the Tomokiyo R on the stream to confirm 0.4548.

Grades: all tokens M whatever the verdict (the gloss is the period decipherment; C would need a per-token alignment, out of brief).
A PASS licenses only "the Dupuy-learned basin key, mapped to the reader signs, reads c262 toward its period gloss beyond the four
nulls". A FAIL with the Tomokiyo reference well above the nulls is a negative on this key on this stream, conditional on the
label -> pile map (one reconciler's labels, RUN2-NXATL's unchecked alignment) and the owner's merges.
