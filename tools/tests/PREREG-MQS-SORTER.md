# PREREG-MQS-SORTER (written 9 Oct 2026 by MQS-SORTER, before any control below was run)

Everything here is fixed before `sign_sorter.py --oddness-audit` or `tx_bench.py` is run on the numbers it governs.

## A. `sign_sorter.py --oddness-audit` (Unit 3): is "Odd ones first" any good?

Statistic: **recall@10%** = the share of planted tiles that sit in the first 10% (at least 1 tile, `ceil(0.10 n)`) of the pile they were
planted into, when the pile is ordered by the page's own oddness score (distance from the pile's mean 24x24 grey tile, normalised: the
same function `build()` calls, factored as `oddness_scores`, so the audit measures the shipped feature, rule 7).

Known answer: Birago no.87, tiles of f.178v + f.179r (`ciphers/nevers-birago-fr3251-1572/atlas/no87_box_token.tsv`, boxes
`atlas/signs.tsv`, page images `atlas/pages.json`). **Clean pile = the line-read sign (`sign`) of a tile with op `1:1` whose printed 1572 key
value (`harvest/key_1572_sheet.tsv`) equals the clerk-sheet letter (`truth`).** That is the truth-derived label: the sign's key value
agrees with BENCHMARK-TX truth for that box, so the tile belongs in that pile. Piles with fewer than 3 clean tiles are dropped (a mean tile
of 1-2 tiles is noise; the page itself skips them for look-alike offers). Expected: about 637 of 748 tiles qualify.

Plants (5% of the clean tiles, rounded, per seed; 20 seeds 1..20):
- **random**: a tile moved from its pile to a uniformly random other pile.
- **look-alike**: a tile moved to its pile's top confusion partner's pile (largest n in `harvest/confusion_1572.tsv`, the no.87 table),
  among tiles whose pile has a partner pile that survives the 3-tile rule. Random plants are far easier than the real errors (which are
  look-alikes), so both are reported.

Null (the shuffled order): the same planted piles, each pile's tiles in a random order, 200 shuffles per seed; p95 of its recall@10%.
Why it can fail differently from the target: the shuffle changes *which* tiles sit in the first 10% of a pile and nothing else, which is
exactly the statistic. Near-ceiling check: the null's recall@10% is about 0.10-0.15 by construction, far from 0.95, so there is headroom
for a gain; the control is not matched by "more restarts alone" because the score is deterministic.

Gate (written before the run): **random plants: recall@10% >= 0.6 and above the shuffled-order p95 in at least 18 of 20 seeds.**
Look-alike plants: report the number of seeds above the shuffled p95 and the mean recall, whatever they are; no pass/fail threshold.
If the random gate fails, the option ships with shelf grade `weak` and both numbers (nothing is run on a target from it); a medoid or
`bitmaps.npz`-distance variant may then be tried and reported beside it, not instead.

## B. Scoring the owner's no.87 sort against BENCHMARK-TX (Unit 4)

Input: `ciphers/nevers-birago-fr3251-1572/sorter/no87/owner-sort-2026-10-04/settled_no87.tsv` (248 no.87 tiles; read-only).
The owner's page placed every tile by a machine nearest-pile seed and the owner moved some (`sorter/no87/README.md`), so this scores
**owner corrections on a machine seed**, not an independent blind read.

**Label-map rule** (fixed here; it must not come from the clerk sheet, whose truth BENCHMARK-TX uses, so BIR87-ALIGN's fitted per-pile
values are NOT used):
1. a **family pile** (a plain sign id such as `T45`) takes that sign's value in the printed 1572 key, `harvest/key_1572_sheet.tsv`;
2. an **owner-made new pile** (a suffixed name such as `T60-c`, `T24-b`, or `X_NEW-*`) is **unknown** (`?`), the `--new-piles-unknown`
   semantics of BIR-OWNERSORT (LEDGER.md);
3. a pile whose family has no key value is reported **unmapped**, never filled from the alignment; NOT-LETTER / BAD-CUT / ASIDE tiles
   are outside the scored set and are counted separately.
Scored with `python3 tools/tx_bench.py` on his labels under that `--label-map`, `--paired` against the committed machine labels on the
same positions; err_true with its interval for both, and paired fixed/broken **separately** for tiles the owner moved and tiles he left
in their machine-seeded pile. If the map cannot be built by this rule the `sign_sorter.py` shelf grade stays `untested` and this is said.
Shelf wording: "owner corrections on a machine seed, scored against BENCHMARK-TX", never "a blind reader's err_true"; BIR-ADJ's 98 of 108
disputed tiles cited as supporting evidence only.

## C. Blind-first (Unit 1) and the colour check (Unit 5): offline tests, no statistic

Unit 1 has no numeric control: `tools/tests/test_sign_sorter_blind.py` carries a positive control (the legacy non-blind caption does show
"reader weight"), so its "no machine string" checks can fail. Unit 5's `--cvd` check must FAIL the legacy tokens, a red/green pair, a hint
naming "red", a light-on-tint dark block and a box under 3:1 on a parchment median, and PASS the updated template (`test_sign_sorter_cvd.py`).

### A1. Addendum, written AFTER the shipped ("mean tile") order was run, before any variant was run (disclosed)

Primary run, 9 Oct 2026, same seeds: random plants mean recall@10% 0.498 (above the shuffled p95 in 20 of 20 seeds, recall >= 0.6 in
1 of 20: the gate FAILS); look-alike plants mean 0.282 (above p95 in 16 of 20). Per section A the option ships `weak` with these numbers.
The brief allows a rival ordering "reported beside it": two variants, fixed now, same plants and seeds, `--oddness-variant`:
`medoid` (distance to the pile member with the smallest summed distance to its pile mates) and `knn3` (mean distance to the 3 nearest
pile mates). Same gate text, same shuffle null. Neither replaces the page order unless it passes the section A gate; the page order is not
changed in this job either way (a variant that passes is a one-line suggestion for the lane).
