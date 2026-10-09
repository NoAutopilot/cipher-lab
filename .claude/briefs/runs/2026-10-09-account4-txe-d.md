# TXE-D: tile rendering sweep -- white space, darkening, colour channels, super-resolution (LANE TX-ENGINEER, ideas O1 O2 O4 M4; account 4, Opus 5.5; cap 10, box 120 min)

Read `.claude/briefs/runs/2026-10-09-account4-txe-COMMON.md` first, then `benchmark-tx/PREREG-txeng-2.md` (units, blindness,
and its Amendment: gate p < 0.01), then research/TX-IDEAS-2026-10-09.md rows O1, O2, O4, M4. Why this job exists: the owner
asked (Amendment 1) that white-space deletion, darkening and colour alteration each be a tool flag measured, never assumed;
the taxonomy's class 3 (thin strokes: half of the mapped errors at a 29% base, 8.5% vs 4.2%) is the mechanism they attack.
The crops today are native resolution, about 40 px a sign, and 14% of signs are cut by the band.

## Build `tools/tx_prep.py` (--help; test tools/tests/test_tx_prep.py; disk only)
`tx_prep.py render --page IMAGE --boxes signs.tsv --page-name f178v --out DIR --setting NAME [--setting ...]`, where a setting is
one of (every one a flag with its parameters printed in the manifest it writes):
- `plain` (the tile as cut today: box grown 50%, native scale) -- the control;
- `tight` (O1): box grown by a margin measured in ink -- the smallest margin such that no ink of the box's own component is
  cut, plus 10% -- then 2x LANCZOS so the sign sits at about 80 px;
- `gamma=G` (O2) for G in 0.5, 0.7; `stretch` (1st-99th percentile); `thicken=1` (one 1-px dilation of ink after a local
  threshold; the result composited back on the paper);
- `channel=R|G|B`, `sep` (blue minus red, rescaled: ink-paper separation), `invert`, `false` (B in red, R in green, G in blue);
- `sr2`, `sr4` (LANCZOS 2x, 4x; if a learned SR model is importable offline without a download, add it as `srl` and say which);
- `combo` = tight + stretch + sr2 (one named combination, fixed now).
Also `tx_prep.py lines --crops DIR --setting S --out DIR2`: the same setting applied to whole line crops (for the one read).
Each tile/crop goes to DIR/<setting>/<sid>.png with a manifest.json (setting, parameters, source box, scale).

## Read-free proxy (the dev gate; never sees a truth file): atlas classify under each setting
The atlas classifier (`tools/glyph_atlas.py classify`, HOG on 48x48 bitmaps) is the read-free reader. For each setting, build
bitmaps from the rendered tiles of the dev_tune lines (f178v L01-12; `--strips` or re-segment the rendered strip with
`segment --median-h pool`, whichever keeps the box count within 5% of signs.tsv's for those lines -- state which) and classify
them against the family atlas holding out ALL of no.87 (`--holdout f178r_ --holdout f178v_ --holdout f179r_ --topk 3`). Score
with `tools/tx_bench.py --item birago1572-no87` after mapping boxes to positions label-blind (sequence alignment to L by order
and x, as atlas/no87_map.py does; never its truth column) -- this opens the truth file, so commit every setting's topk TSV
first. Report per setting: top-1 err_true on dev_tune, truth-in-top-3 share, paired fixed/broken vs `plain`. Registered gate for
a setting to earn the read: fixed > broken, p < 0.01 vs plain. If no setting earns it: FAIL, write the table, no read.

## The one read (only for the single best setting that passed the proxy gate)
Apply the setting to the dev_tune line crops (`tx_prep.py lines` on harvest/f178v/f178v_L01..L12_s?.jpg; tight = band from
ink extent then 2x, under the 2500 px width limit -- split a segment in two with a 100-px overlap if 2x exceeds it, and say so
in the generated crops note). ONE blind Opus 5.5 subagent pass on those crops with the unchanged
`harvest/blind_pass_brief_1572.md` + `sign_sheet_blind_1572.png` (plus a one-line crops note on scale and overlap), in two
calls as pass A used (L01-10 pattern: here L01-06 and L07-12). Raw read to `benchmark-tx/txeng/prep/passK_raw_dev.tsv`, commit,
normalise to `benchmark-tx/outputs/birago1572-no87/passK_prep_dev_tune.tsv`, score paired vs
`benchmark-tx/txeng/units/passA_dev_tune.tsv` (same reader kind on plain crops; gate fixed > broken p < 0.01) and vs
labels_dev_tune.tsv (reported). If the dev read passes: eval_heldout ONCE (f178v L13-23 + f179r L01-03, two calls), paired vs
passA_eval_heldout.tsv and labels_eval_heldout.tsv; that is this instrument's single eval look. If not: FAIL, no eval.

## Report
`benchmark-tx/txeng/prep/RESULTS.md`: the per-setting proxy table, the read's tx_bench lines, `tools/tx_taxonomy.py` on
passK vs A (which class moved; after the reads are committed), the reader task text, calls and cost. Shelf and SYSTEM rows
for tx_prep.py (grade from your own result; every setting that failed is listed as weak with its numbers). Add one row per
setting tested to the Results log of research/TX-IDEAS-2026-10-09.md (ids O1, O2, O4, M4; rebase before editing). Vision
calls: dev 2, eval 2 at most, x about 1.5; cap 10; stop before a call that crosses 80% of cap or box. Report in a short
paragraph (first line: the best setting and its proxy and read numbers) and stop.
