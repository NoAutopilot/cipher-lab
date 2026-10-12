# TXE4-0 REPAIR -- RESULTS (12 Oct 2026, 00:1x-00:5x UTC by date -u)

Worker TXE4-0 (account 3, Sonnet, session_011uLGwLmyW1rw5K8tojeZNr), brief `.claude/briefs/runs/2026-10-11-acct3-txe4-0.md`
(commit 93ecd72da). Script-only: no reader, no vision call, no image read, no network beyond git. Units 1-4 done;
unit 5 (optional) skipped.

## Unit 1 -- the join gate (8a)

New `tools/join_check.py`: a bounded gate on `tools/box_token_align.py`'s own truth-free shift-check statistic.

- B1 (per line, >= 5 placed check tiles): matches at offset 0 beat matches at -1 and at +1. Lines under 5 placed
  tiles are 'unchecked', never failed.
- B2 (overall): matches at -1 and +1 together are at most max(0.05, p95) of placed tiles, p95 the 95th percentile
  of that same share over 20 seeded permutations of the check labels within each page.
- B3 (overall): the share at 0 exceeds that same null's p95, else UNCHECKABLE (the labels cannot see a shift at
  all -- the same shape a fully permuted check column reads as).
- Verdict: UNCHECKABLE when B3 fails; else FAIL when B1 or B2 fails; else PASS.

Writes `MAP.tsv.joincheck.json` (verdict, per-line and overall counts, null p95s, map and inputs sha256, UTC
time). `require(map_path)` refuses (exit 2) a map with no sidecar, a non-PASS sidecar, or a sha256 mismatch;
`--allow-unchecked-join REASON` is the only escape (prints and returns `UNCHECKED JOIN: REASON`).

Offline test `tools/tests/test_join_check.py`, 9 cases, all pass:

```
ok test_mc1_single_line_fails_b1
ok test_mc2_whole_page_fails_every_line
ok test_mc4_permuted_check_labels_is_uncheckable
ok test_mc5_require_refuses_missing_and_stale_sidecar
ok test_nb2_2to1_and_1to2_never_enter_pos_of
ok test_nb3_short_lines_are_unchecked_not_failed
ok test_nb4_weak_labels_do_not_fail_a_right_map
ok test_nb5_repeated_sign_offset0_counted_first
  repository check: old map FAIL (share0 0.755); label-aware map PASS (share0 0.926)
ok test_repository_no87_old_and_labelaware_maps
test_join_check: all passed
```

MC1/MC2 are this job's own construction (a synthetic line/page shaped like the f178v L06 defect but with the
shifted boxes outnumbering the correct ones, since the real L06/L07 only shift after mid-line and pass B1 --
caught by B2 instead, per the real-data check below). MC3/NB1 are the repository check, on the real no.87 files,
checked with `sorter/no87/seed.tsv`'s atlas top-1 label:

```
old map (atlas/no87_box_token.tsv): FAIL, share0 0.755
  f178v_L06: pass (shifted only after mid-line, as predicted)
  f178v_L09, L11, L13, L17, L21, f179r_L02, L03: fail (B1)
label-aware map (atlas/no87_box_token_labelaware.tsv): PASS, share0 0.926
```
Matches the brief's MC3 figures (157/24/14 of 208 old; 188/203 label-aware; leave-one-out 187/2/2) to within the
single-digit rounding a slightly different alt-sign set gives; both maps' verdicts are exactly as predicted.

`tools/box_token_align.py --check-bound` (requires `--check-labels`): runs `join_check.evaluate()` on the map it
just wrote (`--steered` detected automatically when `--check-labels` names the same file as `--topk`/
`--tile-labels`), writes the sidecar, exits 0/2/3. Default behaviour (no `--check-bound`) is unchanged; its own
CLI test is in `tools/tests/test_box_token_align.py::test_check_bound_cli_exit_codes`. All of
`test_box_token_align.py`'s existing tests still pass (default DP, labels, statuses, 1:2/2:1 handling unchanged).

`tools/tests/km_birago_map.py`: a KM PASS now also needs the neighbour-label count at or under 0.05 of the scored
(gated) 1:1 tokens -- the old map's own KM PASS (231/381 = 0.606, neighbour 75/381 = 0.197, well over 0.05) is
exactly the case this bound exists to catch (`tools/tests/RESCORE.md` section 1); the label-aware map's neighbour
share (3/373 = 0.008) and the sorter-only sensitivity map's (4/375 = 0.011) both pass it. Could not be run
end-to-end in this container (`needs opencv-python-headless scikit-image scikit-learn pillow`, the same
pre-existing gap `tools/tests/RESCORE.md` already notes for this file); the gate code was checked by
`py_compile` and by eye against the existing `KM` statistic it extends.

Real sidecar written for the committed label-aware map (steered/leave-one-out, matching the README's own
leave-one-out figure): `atlas/no87_box_token_labelaware.tsv.joincheck.json` -- PASS, n=203, share0 0.921.

## Unit 2 -- route the copies

- `tools/tx_compare.py map --label-aware [--topk --tile-labels --status --lam --check-labels]` and
  `tools/tx_pair_reread.py select --label-aware [...]`: both default (no flag) unchanged, byte-identical to the
  committed `box_pos.tsv` files (new tests `test_tx_compare.py::test_map_label_aware_is_new_and_default_is_unchanged`,
  `test_tx_pair_reread.py::test_select_label_aware_is_new_and_default_unchanged`, both pass). `--label-aware`
  routes through `tools/box_token_align.py` and, with `--check-labels`, writes a join_check sidecar.
- `benchmark-tx/txeng3/7/map_f152r.py` needed no code change: its twin `rescore/map_f152r_la.py` already runs the
  label-aware DP. Wrote its sidecar (check labels: `runs/A0a_f152r.tsv` top-1, leave-one-out): **PASS**, n=83,
  share0 0.711 (`rescore/f152r_box_token_labelaware.tsv.joincheck.json`). The old `f152r_box_token.tsv` gets no
  sidecar, as the brief asks.
- **New files** (`benchmark-tx/txeng4/0/build_box_pos_bta.py`, extending coverage to f178r for the first time):
  - `benchmark-tx/txeng/compare/box_pos_bta.tsv` (891 rows: 1:1 782, unsure 5, 2:1 76, 1:2 26, bad-cut 2). Its
    f178v/f179r rows equal `benchmark-tx/txeng/rescore_boxmapLA/box_pos.tsv` on every shared box: **0 of 891
    differ**. Its 110 f178r boxes are mapped and checked per line (all three f178r lines PASS B1 individually; the
    whole-check verdict is **PASS**, share0 0.908, so no f178r line was excluded -- BOXMAP-LA's caution that
    f178r's line assignment is itself unreliable did not materialise on this check, but the per-line gate stayed
    live and would have dropped a failing line had one appeared).
  - `benchmark-tx/txeng/pair/{dev_tune,eval_heldout}/box_pos_bta.tsv` (367 and 414 rows), both join_check PASS.
- **Defaults switched**: `tools/tx_pair_clf.py --map` and `tools/decipher_sheet.py`'s Birago box-map default, both
  from `atlas/no87_box_token.tsv` to `atlas/no87_box_token_labelaware.tsv`.
- **join_check.require() wired** into `tx_sorter_curve.py --map`, `tx_pair_clf.py --map`, `decipher_sheet.py`'s box
  map (via a new `default_box_map()` helper, independently testable without opencv), and `tx_doubt.py signals
  --box-pos`. Each gained `--allow-unchecked-join REASON`. One test per tool, all pass (listed in the done line).
  Existing synthetic test fixtures that build their own tiny map.tsv now stamp it a trivial PASS sidecar first
  (`_pass_sidecar()` helpers added to `test_tx_pair_clf.py`, `test_tx_sorter_curve.py`); this is new, intended
  behaviour (a map used to score something is now required to carry a checked join), not a regression.
  `tx_doubt.py`'s own test suite needed no fixture change (it never called `TD.main`); its new test runs the real
  `signals` subcommand against the repository's own no.87 defaults, which is what the gate actually guards in
  production.
- **Not yet wired** (named as the next step, per the brief's own fallback): `tx_tile_gate.py --box-pos`,
  `tx_taxonomy.py --box-token`, and `tx_compare.py`'s other box_pos-reading subcommands (`library`, `resolve`,
  `tiles`, `tiles-resolve`).
- **Pre-existing, unrelated environment issue found while testing**: two assertions in
  `tools/tests/test_tx_pair_clf.py` (`test_train_apply_control`, `test_x2b_dev_tune_loo_lines`) already fail in
  this container before any of this job's edits (confirmed by `git stash`): the synthetic classifier training
  never "enables" (numpy/version drift in this container, unrelated to box maps). Not fixed here (out of scope);
  flagged for whoever next touches `tx_pair_clf.py`.

## Unit 3 -- the 3 Oct start labels, re-attached by position

New `benchmark-tx/txeng4/0/unit3_start_labels.py`. The line read each sorter cut its labels from (both READMEs):
f117r from `harvest/f117/la/passD.tsv`; f144r and f168 from `harvest/lookalike/<run>_passD.tsv`. Both
`build_inputs.py` scripts zip that read's rows (in position order) against that passage's own boxes (in x order)
one to one -- the sid itself encodes the original index (`f117_L09_07` is the 7th box, which took the 7th
line-read row), so the "old (index) join" is recovered directly from each sid's own suffix with no re-derivation.
The "new (geometric) join" runs `tools/box_token_align.py` per passage, steered by each box's own atlas cluster
label (`sorter/no87/owner_map.tsv`'s geometric centroid join -> `atlas/topk/{fr3252-no77,no73,no85}.tsv`'s top-3,
by the owner_map's `atlas_page`), check labels = the same top-1, leave-one-out.

Shift check, old vs new, every strip passage (sids from `harvest/bir87align/settled_corrected.tsv`, 488 tiles
across 20 passages):

```
  f117_L01 (n=30): old 0/-1/+1 12/0/2 (PASS) -> new 0/-1/+1 14/0/0 (PASS)
  f117_L02 (n=29): old 0/-1/+1 20/0/0 (PASS) -> new 0/-1/+1 20/0/0 (PASS)
  f117_L03 (n=31): old 0/-1/+1 13/0/0 (PASS) -> new 0/-1/+1 13/0/0 (PASS)
  f117_L04 (n=29): old 0/-1/+1 22/0/0 (PASS) -> new 0/-1/+1 21/0/0 (PASS)
  f117_L05 (n=31): old 0/-1/+1 16/1/0 (PASS) -> new 0/-1/+1 16/1/0 (PASS)
  f117_L06 (n=31): old 0/-1/+1 19/0/0 (PASS) -> new 0/-1/+1 19/0/0 (PASS)
  f117_L07 (n=29): old 0/-1/+1 18/2/1 (PASS) -> new 0/-1/+1 17/0/1 (PASS)
  f117_L08 (n=28): old 0/-1/+1 23/0/0 (PASS) -> new 0/-1/+1 23/0/0 (PASS)
  f117_L09 (n=29): old 0/-1/+1 5/15/0 (FAIL) -> new 0/-1/+1 16/0/0 (PASS)
  f117_L10 (n=10): old 0/-1/+1 6/0/0 (PASS) -> new 0/-1/+1 6/0/0 (PASS)
  f144r_L03 (n=11): old 0/-1/+1 4/0/0 (PASS) -> new 0/-1/+1 4/0/0 (PASS)
  f144r_L04.1 (n=12): old 0/-1/+1 3/1/0 (UNCHECKABLE) -> new 0/-1/+1 3/0/0 (PASS)
  f144r_L04.2 (n=12): old 0/-1/+1 0/0/0 (UNCHECKABLE) -> new 0/-1/+1 2/0/0 (PASS)
  f144r_L05 (n=35): old 0/-1/+1 14/1/1 (PASS) -> new 0/-1/+1 14/0/1 (PASS)
  f144r_L06 (n=20): old 0/-1/+1 2/12/0 (UNCHECKABLE) -> new 0/-1/+1 10/0/1 (PASS)
  f168_R02 (n=34): old 0/-1/+1 14/4/3 (FAIL) -> new 0/-1/+1 16/1/0 (PASS)
  f168_R03 (n=18): old 0/-1/+1 5/0/8 (FAIL) -> new 0/-1/+1 6/0/0 (PASS)
  f168_V01 (n=13): old 0/-1/+1 0/5/0 (UNCHECKABLE) -> new 0/-1/+1 4/1/0 (PASS)
  f168_V02 (n=30): old 0/-1/+1 4/0/5 (FAIL) -> new 0/-1/+1 9/0/0 (PASS)
  f168_V03 (n=26): old 0/-1/+1 5/5/0 (FAIL) -> new 0/-1/+1 6/1/1 (PASS)
```

The old index join FAILs or is UNCHECKABLE on 9 of 20 passages (f117_L09 and five f168 passages FAIL B1 outright;
f144r_L04.1/L04.2/L06 and f168_V01 are UNCHECKABLE -- too few atlas-labelled tiles on these short passages to see
a shift at all, not a pass); the new geometric join PASSes all 20. f117_L09's fail matches the brief's named
must-catch case directly (5 beats 15 the wrong way under the old join); f144r_L06's own number here (2 vs 12 at
-1) is the same shape as the brief's cited diagnostic figure (13 vs 2) though not an exact match -- this job
re-derived the statistic from the committed files fresh rather than reusing `rescore/diagnostics.txt`'s own
(differently-scoped) count.

New files: `harvest/bir87align/start_labels_geom.tsv` (sid, strip, index_pos, index_start, geom_pos, geom_start,
op, changed) and `harvest/bir87align/settled_geom.tsv` (settled_corrected.tsv's rows with `old_sign` replaced by
the re-attached start label, `status` re-derived).

**Changed start labels**: 90 of 488 (f117 21, f144r 29, f168 40). **Kept/moved totals**: old (index-attached)
kept 274 / moved 206; new (geometry-attached) kept 322 / moved 166. **Of the boxes where A1 (old_sign) and A2
(new_sign) differ**, now counted as kept (owner label == re-attached start label): **54 of 214**. The brief
predicted "62 of 121" from TXE3-7 section 1's own count; this job's 214 is the *full* raw count of every
`old_sign != new_sign` row in `settled_corrected.tsv` across all three strips, not TXE3-7's (differently
filtered, no.87-training-specific) 121 -- the two denominators are not the same population, so the figures are
not directly comparable; this is reported as a fresh, independently-derived number, not a reproduction of
TXE3-7's. **Not re-run**: TXE3-7 itself (named next step, per the brief).

## Unit 4 -- the atlas names, rebuilt as a new file

Ran `atlas/no87_map.py --compat` (the one named truth-reading exception, temp-only, never committed) then
`atlas/name_clusters.py --map <that file> --out <temp>` -- exactly `atlas/RESCORE.md`'s own job, reproduced fresh:

```
compat -> /tmp/.../map.tsv {'1:1': 700, '2:1': 25, '1:2': 13, 'bad-cut': 2, 'unsure': 3}
302 verified tune tiles; clusters by source {'clerk': 74, 'model': 63, 'unnamed': 3}; tiles in unnamed clusters 137 of 4209
```

Byte-identical to the already-committed `atlas/rescore_boxmapLA/named/{labels.json,cluster_names.tsv}`. Diffed
against the old committed `atlas/labels.json`:

```
override counts: old 309 new 302
shared 299 changed sign 35 dropped 10 added 3
cluster codes changed: 8 ['84', '89', '94', '14', '63', '37', '2', '132']
```

Matches `atlas/RESCORE.md`'s cited figures exactly (302 overrides: 299 shared, 35 changed, 10 dropped, 3 added;
74/63/3 clusters; 8 cluster codes changed). Committed as **new files** `atlas/labels_boxmapLA.json` and
`atlas/cluster_names_boxmapLA.tsv`. `benchmark-tx/txeng4/0/build_labels_boxmapLA.py --check` regenerates and
compares (rule 7); run now:

```
build_labels_boxmapLA --check: current
```

`atlas/README.md` gained the "labels_boxmapLA.json (TXE4-0)" section (what it is, that no consumer reads it by
default, that `glyph_atlas.py classify --labels` takes it, that switching a consumer is the lane's decision, and
that it keeps TX-ATLAS-B72's dev-truth naming convention). The three unnamed clusters (14, 84, 89) stay `_` (no
model call made).

## Unit 5 (optional) -- skipped

Per the brief ("Unit 5 is optional and is the first unit dropped"): not attempted. TXE4-3 to TXE4-7's own briefs
build these machine-only inputs themselves if still needed.

## Files written

New: `tools/join_check.py`, `tools/tests/test_join_check.py`, `benchmark-tx/txeng4/0/{build_box_pos_bta.py,
unit3_start_labels.py, build_labels_boxmapLA.py, RESULTS.md}`, `benchmark-tx/txeng/compare/box_pos_bta.tsv(+.joincheck.json)`,
`benchmark-tx/txeng/pair/{dev_tune,eval_heldout}/box_pos_bta.tsv(+.joincheck.json)`,
`benchmark-tx/txeng3/7/rescore/f152r_box_token_labelaware.tsv.joincheck.json`,
`ciphers/nevers-birago-fr3251-1572/atlas/{labels_boxmapLA.json,cluster_names_boxmapLA.tsv,
no87_box_token_labelaware.tsv.joincheck.json}`, `ciphers/nevers-birago-fr3251-1572/harvest/bir87align/
{start_labels_geom.tsv,settled_geom.tsv}`.

Edited: `tools/box_token_align.py` (+`--check-bound`), `tools/tests/km_birago_map.py` (+neighbour bound),
`tools/{tx_compare,tx_pair_reread,tx_pair_clf,tx_sorter_curve,tx_doubt,decipher_sheet}.py` (+`--label-aware`/
`require()` wiring, all defaults unchanged and tested), their test files, `ciphers/nevers-birago-fr3251-1572/
atlas/README.md`, `SYSTEM.md`, `tools/data/tool_shelf.tsv`, `UPDATES.md`, `LEDGER.md`.

Unchanged (Z4): `atlas/labels.json`, `atlas/no87_box_token.tsv`, `benchmark-tx/txeng/compare/box_pos.tsv`,
`benchmark-tx/txeng/pair/*/box_pos.tsv`, `benchmark-tx/txeng3/7/f152r_box_token.tsv`, the sorters' `labels.tsv`,
`harvest/bir87align/settled_corrected.tsv`.

## Proposed to the parent (not made here, per the brief)

- CLAUDE.md 8a precedent: `tools/join_check.py` (a box-to-token join needs a bounded, sidecar-carrying gate before
  any consumer scores from it; a KM-style PASS alone licenses nothing -- the old map's own KM PASS at 75/381
  neighbour-label matches is the worked example).
- TRANSCRIPTION.md join rule: a box-to-token map is scored or cut from only through `tools/join_check.require()`
  (or an explicit, logged `--allow-unchecked-join`); `--check-bound` is run whenever a new map is built.

Host requests this session: 0 (git only, per the brief's scope).
