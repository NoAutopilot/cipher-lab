# PREREG WVO-DEDUP -- f.23 re-alignment with the duplicate recut tiles dropped (written and pushed before any scored run)

Worker WVO-DEDUP, account 1, for LANE DEFAULT-A1-1840, 11 Oct 2026 (18:5x UTC by date -u). Brief:
.claude/briefs/runs/2026-10-11-acct1-default-1840-jobs.md, section WVO-DEDUP. Gap: NOTES.md "Remaining gaps (11 Oct 2026)", first row.

**What changes: the token stream, not the labels.** No settled label, pile, key rule or gloss letter is edited. The 7 overlapping
recut pairs found by the 11 Oct overlap scan (sorter/signs_recut.tsv, IoU 0.60-0.88) are two tiles cut over one written sign.
- The 5 same-pile pairs -- C03 018/019 (k23), C04 022/023 (k13), C06 023/024 (k13-d), C07 023/024 (k13), C09 031/033 (k03) --
  lose one copy each from the stream. Rule fixed now: drop the later tile in x order (the higher idx in r9align/tile_order.tsv).
  Both copies carry the same settled sign, so which copy goes does not change the label sequence.
- The 2 cross-pile pairs -- C06 009/010 (k03 / k23) and C09 018/019 (k23 / k03) -- stay in the stream unchanged (both copies)
  in the scored run, because choosing a copy is choosing a label, which is the owner's call. They go to sorter/focus.tsv as
  focus rows, never blocking.
- List: realign/dedupe_2026-10-11.tsv (pair, sids, piles, IoU, action). Output: realign/dedup/ (realign/ itself, which
  d2wvo/famwvoh/d4wvo scripts read, is left as WVO-REALIGN wrote it).

**Pipeline and gate: PREREG-WVO-REALIGN unchanged.** `realign/run.py` with a `--drop LIST --out DIR` option and nothing else
changed: same aligner parameters (`--code-prefix @ --seg-bonus 0 --keep-fs --null-cost -1.0`), same key rule (C: top letter >= 2
times on >= 2 rows and >= 0.6 of aligned occurrences), same derangement shuffle (1000, seed 1564) on CONSISTENT, same within-row
label permutation control (300 draws, seed 1564, full pipeline per draw) on the deduplicated stream. Primary statistic AGREE (C
tiles whose key value equals the aligned gloss letter). Gate: real AGREE > control p95 -> gain over chance shown on the corrected
stream; else "gain not shown". The control can differ from the target on AGREE (permuting labels within a row scatters each sign's
aligned letters), as in PREREG-WVO-REALIGN.

**Before/after (reported, not gated):** before 160/257 C-agree (realign/figures.json, control p95 9). After: N/252. Expected
direction (a prediction, not a result): the doubled m/i under "zweimahl" in C06 and C07 go; C_conflict + C_unaligned fall by some
of the non-agreeing pair copies the 11 Oct note counted (C04_022, C09_033 in conflict; C06_023, C07_023, C09_031 unaligned among the
same-pile pairs; the dropped copy is not always the counted one, and the re-alignment can shift neighbours). No figure is chosen after the run.

**C09_01_025 (gloss i over a k03 tile):** one re-look after the run at a strip crop of the gloss row above it (r10tx crops or a
crop cut with tools/iiif_lines.py --image), one look, letter shape reported (grade M), no key change.
