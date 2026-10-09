# TXE-A: compare, don't recall (LANE TX-ENGINEER round 2, instrument A; account 4, Opus 5.5; cap 10, box 120 min)

Read `.claude/briefs/runs/2026-10-09-account4-txe-COMMON.md` first, then `benchmark-tx/PREREG-txeng-2.md` "Instrument A".
Why this job exists: half of today's transcription error on Birago no.87 is the reader naming a sign from memory against a
printed sheet cell when the hand's form sits between two cells (research/TX-TAXONOMY-2026-10-09.md class 1: d T18 / s T98,
p T90 / t T53, n T76 / e, h T64 / l; 34 of pass A's 54 errors shared with B with the same wrong sign; 20 positions wrong in
every pass on disk). Line reads are 0.040 where the atlas top-1 alone is 0.162; the combination -- the reader choosing among
SHOWN candidates (the line read's sign plus the atlas's top-3) instead of recalling -- has never been scored.

## Build `tools/tx_compare.py` (subcommands build, resolve; --help; test tools/tests/test_tx_compare.py)
Inputs (all on disk, folder `ciphers/nevers-birago-fr3251-1572`): `atlas/signs.tsv` (boxes), `atlas/bitmaps.npz`,
`atlas/clusters.tsv`, `atlas/labels.json` ("signs" cluster -> code only; NEVER its "override"), page images (`atlas/crops/`
regenerable per atlas/README.md, else the harvest `src_*.jpg` through `atlas/pages.py`), the line read L
(`benchmark-tx/outputs/birago1572-no87/labels.tsv`) with merged confidence from `harvest/f178v/passC_agreement.tsv` and
`harvest/f179r/passC_agreement.tsv`, exemplar tiles from `atlas/sheet_truth/sheet.tsv` (secure tiles on non-no.87 leaves)
or, for a code it lacks, boxes of non-no.87 pages labelled by cluster.
1. Candidates: run the atlas classify holding out ALL of no.87 (README's HO form extended:
   `--holdout f178r_ --holdout f178v_ --holdout f179r_`, `--topk 3`, `--tsv benchmark-tx/txeng/compare/topk_no87_allheld.tsv`).
   Map boxes to line positions with the SAME label-blind method `atlas/no87_map.py` uses (sequence alignment of boxes to
   the line read by order and x; do not read its truth column; write your own `box_pos.tsv`: sid, line, pos, 1:1/2:1/1:2).
2. `build --unit dev_tune|eval_heldout` (lines from `benchmark-tx/txeng/units/README.md`): per position candidates =
   {L sign} + atlas top-3 codes; SHOW the position when top-1 != L sign, or top-1 share < 0.6, or L merged conf in M/L
   (an unmapped position is shown only if conf is M/L). Row = tile of the sign at 4x with one neighbour each side (box
   grown 50%) | 2 exemplar tiles per candidate, candidates numbered 1..k in a seeded random order per row. Sheets of at
   most 16 rows: `benchmark-tx/txeng/compare/<unit>/sheet_NN.png` + `sheet_NN.tsv` (row, line, pos, candidate codes in
   shown order) -- the TSV is the key and is not given to the reader. Print per unit: positions, shown, sheets.
3. Reader: one Opus 5.5 subagent call per sheet, task text: "Read only <sheet png>. For each numbered row, which numbered
   candidate (1..k) matches the boxed sign in the leftmost tile, or none? Write <path>: row, pick, conf (H/M/L), note. Do
   not open any other file." Save raw reads to `benchmark-tx/txeng/compare/<unit>/reads_NN.tsv`; commit and push the
   unit's reads before resolving or scoring.
4. `resolve --unit U` -> `benchmark-tx/outputs/birago1572-no87/passG_compare_<unit>.tsv` (line, pos, sign: the pick's
   code, else L's sign) and `benchmark-tx/txeng/compare/<unit>/topk_weighted.tsv` (line, pos, cand, score: pick H 1.0 /
   M 0.6 / L 0.3, the others sharing the rest) for the secondary lattice run.
5. Score (PREREG): dev first, `tools/tx_bench.py passG_compare_dev_tune.tsv --bench BENCHMARK-TX.tsv --item birago1572-no87
   --paired benchmark-tx/txeng/units/labels_dev_tune.tsv`. Gate fixed > broken, p < 0.05. Met -> eval_heldout once, the
   same way against labels_eval_heldout.tsv. Not met -> FAIL, no eval. Secondary, reported only:
   `tools/key_decode_lattice.py decode topk_weighted.tsv --key <harvest key, see decode.json> --lang it ... --out-prefix` at
   lam 4, scored the same way. Then `python3 tools/tx_taxonomy.py --item birago1572-no87 --pass L=... --pass G=... --boxes
   atlas/signs.tsv --box-token atlas/no87_box_token.tsv --harvest harvest --out-tsv ... --md ...` (after the reads are
   committed; this file carries truth) to say which class moved.
6. Fable arm (only if the Opus dev gate is met AND you are under 60% of cap): the eval sheets read once by a Fable subagent
   (`model: fable`), resolved and scored as a separate output `passG_compare_fable_eval.tsv`; reported beside Opus, never
   pooled. Otherwise write "Fable arm not run (<reason>)".

Offline test: a synthetic page with 3 known signs, a tiny atlas/labels, a line read that disagrees on one position: build
shows exactly that position, the key TSV holds its candidates, resolve applies a pick and keeps L on "none".
Shelf row grade from your own result (proven only on an eval PASS; else weak with both numbers). Vision calls: dev about 3,
eval about 3, Fable arm up to 3 = 6-9 x about 1.5 (Fable 2.5) within cap 10; stop before a call that crosses 80% of cap or
box. Report in a short paragraph (first line the verdict with dev and eval fixed/broken/p) and stop.
