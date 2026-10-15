# PREREG-MONL-ADH (15 Oct 2026, account 1, for LANE DEFAULT-A1-0447-15)

Written and pushed before any W:adhuc alignment or sort was computed. Brief: .claude/briefs/runs/2026-10-15-acct1-default-0447-jobs.md, MONL-ADH
(MONL-L11's Verdict: "the pre-registered W:adhuc re-run, then a value-blind sort of the L11-L15 K11|K62, K37, K04|K12 tiles").

## Part 1: W:adhuc re-run

**Hypothesis.** The five c268 signs L11:6-10 (K66 K49 ?h_bar K35 K15, both passes) are one clear-looking word "adhuc" written inside
the cipher, a W: token like L01:16-17 W:mihil + W:Cur (MONL-ALIGN), not five cipher letters. MONL-L11 noticed the letter look before
the clear text was opened but kept the ids; the re-run below is the transcription change, made after the clear text was seen, so it
is gated.

**Manipulation.** In the token stream of ciphertext_c268.tsv as committed (L01-L15, 525 tokens), replace L11:6-10 by one token
`W:adhuc` at L11:6 (no table value: in align_c268.py it takes 0-14 clear letters at -0.1 per letter, like W:mihil). Nothing else changes.

**Statistic.** align_c268.py's confirm share of keyed tokens (confirm / keyed) on L01-L15 against clear_f140.tsv, i/y fold on, as
committed. Baseline (committed, MONL-L11): 357/504 = 0.7083. Gain = share(W:adhuc) - 0.7083.

**Matched control (can differ from the target by construction).** Removing four contradicting keyed tokens raises the share mechanically,
so the gain is compared with the same operation applied elsewhere: every other window of 5 consecutive tokens within one line of
c268 L11-L15 (same band, same clear-text quality) that does not overlap L11:6-10 and holds no W: token is collapsed into one
`W:window` token the same way, and its gain is computed. Null = the distribution of those gains.

**Keep condition (all three):**
1. the W:adhuc gain is above the null's 95th percentile and no more than 5% of null windows reach it;
2. the shuffled-clear control (200 draws, seed 140, align_c268.py's own) on the W:adhuc stream: 0/200 at or above the real share;
3. the W:adhuc chunk is non-empty.
If kept: score_c268.py writes L11:6 as W:adhuc (pass_a column `K66+K49+?h_bar+K35+K15`, relabel tag `monl-adh`, conf M), L11:7-10
are dropped (positions after are not renumbered), and the committed outputs are regenerated. A FILLS entry in align_c268.py is added
**only if** the chunk is exactly one or more whole clear words; grade **M** (one occurrence; the W: reading was proposed after the
clear text was seen). Otherwise no FILLS entry (the token stays U).
If not kept: no transcription change; the result is logged in NOTES.md as a negative for this hypothesis at this N.

Script: `adh_run.py` (writes results_adh.json; `--check` exits 1 when stale).

## Part 2: value-blind sort of L11-L15 K11|K62, K37, K04|K12 tiles

Method and rules exactly as sort/vb/PREREG-MONL-VB.md (which follows sort/PREREG-MONL-SORT.md): tiles cut from the MONL-L11 line crops
(regen_monll11.sh), candidate cells shown as key-sheet ids only (no value, no reading, no clear text, no current label, no machine label,
no decode), <= 12 windows per blind call, two independent sorts (B with rows reversed), the PREREG-MONL-SORT controls (c172 K04 x4,
gloss-confirmed K14 x3) mixed in.
- Cells offered: K11 and K62 for every L11-L15 token currently K11 or K62; K37 with its look-alike cells as chosen from the key sheet by
  shape before any sort (named in sort/adh/cells.txt, pushed with the tiles before the sorts are read); K04 and K12 for every L11-L15
  token currently K04 or K12.
- Relabel only where both sorts give the same other cell and neither is conf L. 2+ of 7 controls moved by both sorts = relabel nothing.
- A relabel set is kept only if, after it, align_c268.py's L01-L15 shuffled-clear control stays 0/200 at or above the real share.
- Then `align_c268.py --check`, `score_c268.py --check`, `decode_key.py . --check`.
Budget stop: no unit (blind call ~0.5, own look ~0.3) that would cross 3.2 of the cap of 4; if the budget runs out before both sorts,
nothing is relabelled.

## Addendum (06:1x UTC 15 Oct 2026, before any tile was cut or any sort run; part 1 result already computed, part 2 untouched)
Part 1 ran first (results_adh.json: keep false). Part 2 scope narrowed for the budget: all 37 L11-L15 K04/K12/K11/K62/K37 tokens + 7
controls = 44 tiles would need 8 blind calls at <= 12 tiles, twice the brief's 2-4. Sorted instead: the 12 lead tokens MONL-L11 named
(K62 facing m: L13:10, L15:9, L15:12, L15:18; K37 facing p: L13:7, L13:16, L13:20, L13:23; K04 facing n: L11:14, L11:23, L13:14, L15:4)
plus both K11 tokens (L11:12, L13:3) = 14, plus the 7 controls = 21 tiles, 2 calls per sort, 4 calls in all. The selection is by the
alignment (contradiction leads), the sort itself stays value-blind. Pairs as in sort/adh/cells.txt (K37|K43 chosen by shape from the key
sheet). All other rules of part 2 unchanged; the 23 unsorted tokens keep their labels.
