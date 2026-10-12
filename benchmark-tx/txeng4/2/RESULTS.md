# TXE4-2 DINT-PIC results: a machine-cut picture of each Dinteville sign, from f.130r, for the readers of f.128r (12 Oct 2026, 01:24-01:4x UTC by date -u)

Worker TXE4-2 (account 3, Fable 5.1, session_01MB4qh15ETboWcbSJxybVRL) for the account-3 parent (session_0198Cv8ypBfBVfRToKVWx33M);
brief `.claude/briefs/runs/2026-10-11-acct3-txe4-2.md` (93b7bb321). PREREG `benchmark-tx/PREREG-txeng4-2.md` pushed 908527f4 (01:29 UTC)
before any read or score; its Addendum carries the pasted shift-check rows and the purity gate. Item dint-f128-print (dev, 85 scored, no
flags file). Tile source f.130r only (12 qualifying crops, both blind Sonnet passes, labels mapped through dint128_label_map.tsv).
Prerequisite TXE4-0 REPAIR (6f84c5af) in place: every join ran through tools/box_token_align.py and tools/join_check.py.
**No reader call was made and no new output was scored:** the registered purity gate failed before the sheets were built, so the
declared reading for that case applies. Truth opened only by tools/tx_bench.py, twice, on the two COMMITTED baseline passes (step 1).
No eval item touched (LOOKS.tsv: no row). No truth or flag edited. No network: 0 requests to any host. Nothing published.

## Verdict: NON-TEST ('f.130 tiles not verifiably placed' and 'fewer than 15 labels pictured'), as declared. A null on the pipeline, not on the picture.

| purity gate part (PREREG, word for word) | value | holds |
|---|---|---|
| (i) among the labelled boxes at kept (agreed) positions in round 2, the share with op 1:1 >= 0.80 | 131 / 216 = 0.606 (1:2 51, 2:1 10, unsure 24) | no |
| (ii) at least 15 of the 27 labels have >= 2 kept tiles (1:1 at the same position in both rounds) | 9 of 27 (34 tiles: y 5, v 5, sq 4, 0 3, a 3, # 2, 1 2, f 2, m 2; singletons 4, w, -:-) | no |
| (iii) the shift check PASSes (join_check --steered, TXE4-0's bound) | PASS: share at 0 0.298 vs null p95 0.084; share at +-1 0.146 under bound 0.182; B1 holds on all 5 placed lines | yes |

The fill rule (step 2g) is registered for part (ii) only and cannot repair part (i), so it was not run. P and S were not built, T was
not read. The registered gate (mean(T) >= 1.25 x mean(P), gap > spread, mean(S) >= mean(P) + spread) is therefore unevaluated.

## Numbers that exist (both masks identical: dint-f128-print has no flags file, --exclude-flagged gives the same 85 positions)

Step 1, the committed baseline passes re-derived with the committed score.py (full consoles in scores/; truth-value lines kept off the
worker's screen), unit-cost edits = tx_bench's standard-SER numerator:

| output | mapped: edits (S D I), err_true (k/85), Wilson 95% | raw: edits, err_true | strict (mapped / raw) | line bootstrap 95% (mapped) |
|---|---|---|---|---|
| baseline pass A (A2-DIN, 3 Oct) | 21 (13 2 6), 0.247 (21/85), 0.161-0.355 (bootstrap) | 30, 0.353 (30/85) | 0.247 / 0.353 | 0.161-0.355 |
| baseline pass B | 16 (11 0 5), 0.188 (16/85) | 26, 0.306 (26/85) | 0.188 / 0.306 | in scores/baseline_B.mapped.txt |

Both figures on file (0.353/0.306 raw, 0.247/0.188 mapped) reproduce exactly. The planner's "23 and 21 position errors" are not
tx_bench's figures: its unit-cost edits are 21 and 16 mapped (30 and 26 raw); the planner's cross-pass overlap counts were not
re-derived (they need per-position truth values on screen, which R3 keeps off it). norm.py (build_dint128's pass normaliser repeated on
top of build_dint128.rd) is byte-identical to the committed outputs on both committed passes.

Tile pipeline (read-free; every file in tiles/ with its sha256 in SHA256SUMS.prescore):

| step | result |
|---|---|
| segmentation (glyph_atlas segment, default mode, --median-h pool 31 px) | 11 crops pooled; f130_L02_s1 came out EMPTY under the pool (the tool's line finder needs peaks >= 0.7 x 4 x 31 = 86 px apart; the crop's rows are 84 px apart) and was segmented alone at its own 29 px (declared in the PREREG Addendum before any join); 1,128 boxes, 95 marks |
| middle row + overlap dedupe (middle_row.py) | 379 boxes on the 8 lines (L02 32, L04 31, L05 34, L07 64, L08 66, L09 60, L10 61, L11 31) |
| line reads (reconcile_passes --method nw --keep-dots) | pass A 419 tokens, pass B 418; agreed 358 (83.4%); alternatives 50 |
| round 1 (width only, --count-tol 0.10) | L02 (32 boxes vs 37 tokens), L09 (60 vs 68), L10 (61 vs 70) skipped: box counts 12-14% UNDER the token counts; 5 lines aligned, 178 1:1 boxes at agreed positions (21 labels) |
| round 2 (kNN top-3 from those 178, --loo) | 250 rows: 1:1 157, unsure 25, 1:2 56, 2:1 12; 131 1:1 at agreed positions |
| shift check, in sample (box_token_align --check-bound) | n 182: at 0 76, -1 3, +1 7, +-2 16, none 80 -> PASS (0.418 vs p95 0.100; +-1 0.055 under 0.170) |
| shift check, leave-one-out (join_check --steered, BINDING) | n 178: at 0 53, -1 12, +1 14, +-2 19, none 80 -> PASS (0.298 vs p95 0.084; +-1 0.146 under 0.182) |

Reading of the tile numbers: the join is not SHIFTED (the bound holds with margin, on every placed line) but it is COARSE: 61 of the
216 boxes at agreed positions cover two tokens or share one, because the default connected-component segmentation joins touching
signs of this cursive hand and drops its dots (the passes count '.' as a sign; the segmenter's speck filter removes it), so three of
eight lines fall outside the 10% box-count tolerance and the surviving 1:1 tiles cover only 9 labels. The kNN labels themselves are
weak at 178 training tiles (44% of placed check tiles match no read sign within +-2), which is what keeps the leave-one-out share at
0.30 -- enough to pass the bound, not enough to pin tiles for 15 labels.

## Post-registration, read-free exploration (NOT a result; it prices the next step)
The segmenter's existing joining-hand option was tried at two values with the identical pipeline (run_tiles.sh; tiles_x13/,
tiles_x20/; SHA256SUMS.explore):
- `--split-wide 1.3`: every line OVER the tolerance (boxes 45/47/45/92/94/88/84/43 against tokens 37/33/36/71/71/68/70/33, +22-42%):
  nothing aligned.
- `--split-wide 2.0`: box counts within 2 of the default run (only L04 31->32, L11 31->33), the same three lines skipped, 128/219 =
  0.584 1:1, 9 labels with >= 2 tiles, and the binding leave-one-out shift check now FAILs on B1 for f130_L08 (+1 10 > 0 9).
So the box deficit is not wide boxes: it is joined pairs at normal width plus dropped dots, which this option does not reach. The
exploration stopped there (two values, no further knob).

## Access and cost
No subagent was spawned: access_log.py and usage.py are copied in (R8) and were not run; there is no reader transcript. Hosts: 0
requests. Tool patches (R7: the shared tools were not edited -- tools/box_token_align.py carried another TXE4 session's commit within
the hour and TXE4-1 is briefed to land the same options): box_token_align.py.patch (--keep-pos, --tokens-out, --count-tol) and
glyph_atlas.py.patch (--from-tokens, --row-text, --shuffle-rows), tested offline by test_patches.py against scratch copies (both OK).
Units done: U0 PREREG, U1 baseline, U2 patches + tests, U3 tile pipeline; U4-U11 not started (gate failed). Running estimate at the
stop: Fable floor 9.5 + 0.5 = about USD 10.0 (the parent's get_session is the figure). Elapsed 01:24 to about 01:4x UTC.

## For the owner, in three plain sentences
We could not test whether a picture of the Dinteville signs helps the readers, because the machine could not cut a clean enough set
of sign pictures from the sister letter f.130: the cutter joins touching signs and drops the dots of this running hand, so only 9 of
the 27 signs got two or more trustworthy pictures (the rule asked for 15), even though the pictures it did place were not shifted
against the readers' own positions (the TXE4-0 join check passed with margin). So nothing is known yet about the picture versus the
word list on this hand, and no reader time was spent on a sheet that would have shown a third of the alphabet. The sheet idea stays
open for this hand; the blocker is the sign cutter on a joined hand, not the join or the readers.

## Next step and its cost (not run)
1. A cutter for the joined hand before any sheet: segment the 12 f.130 crops with `glyph_atlas.py segment --cursive` (the joined-hand
   mode built for Vivonne 1573, never run on Dinteville) and, separately, keep the dots (lower the speck filter for '.'), each judged
   read-free by the registered box-count tolerance and purity gate (i)/(ii) alone -- about USD 4, 20 minutes, Fable, no reader.
2. Only if a cutter reaches >= 0.80 1:1 and >= 15 labels: the registered P/S/T reads exactly as PREREG-txeng4-2 (six Sonnet calls,
   about USD 2.1 + the Fable floor, about USD 12), under the same gate. The brief's own next step (re-read f.130 with P, about USD 6;
   a fr.3619 sheet from f.89/f.98v/f.113, about USD 5) waits on that.
3. Tool side, for whoever lands (a)-(c) on the shared tools: the two patches here apply cleanly to 6f84c5af; the atlas row-text
   column uses a TrueType font so the brief's Greek and symbol glyph names survive (cv2.putText drops them).

| file | sha256 (16) |
|---|---|
| tiles/TILES.tsv (34 rows, never used by a reader) | in SHA256SUMS.prescore |
| tiles/r2_map.tsv, r2_map.tsv.joincheck.json (PASS) | in SHA256SUMS.prescore |
| scores/baseline_A.mapped.txt, baseline_B.mapped.txt (+ raw) | committed with this file |

Openings of eval truth: 0. dev truth openings: 4 tx_bench calls (A and B, mapped and raw), all on committed baseline outputs.
