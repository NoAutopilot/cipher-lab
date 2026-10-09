# PREREG TXE-M: feature-first reading protocol (LANE TX-ENGINEER, idea M24; 9 Oct 2026, 08:04 UTC by date -u; pushed BEFORE any read)

Brief `.claude/briefs/runs/2026-10-09-account4-txe-m.md`; binds `benchmark-tx/PREREG-txeng-2.md` (units, blindness, Amendment:
single-instrument gate p < 0.01, one eval look). Taxonomy class addressed: 1 (look-alike pairs) and the "errors sit in the
glyph" finding of research/TX-IDEAS-2026-10-09.md. What changes: HOW the reader decides, not what it sees.

## Material (unchanged except one output rule)
- Crops: the unchanged dev_tune line crops `ciphers/nevers-birago-fr3251-1572/harvest/f178v/f178v_L01..L12_s1..s3.jpg`
  (pass A's crops); sheet `harvest/sign_sheet_blind_1572.png`; brief `harvest/blind_pass_brief_1572.md` unchanged, plus one
  section "Features first, then the cell" (tools/tx_features.py `rule_text`): the TSV gains a `features` column written
  BEFORE sign_id, seven key=value pairs in a fixed vocabulary (desc none/short/long, asc none/short/long, bars 0/1/2,
  loops 0/1/2, dots 0/1/2+, lean left/upright/right, tail none/left/right), and the table of the 51 sheet cells' features.
- Cell features: `benchmark-tx/txeng/feature/cell_features.tsv`, derived by `tools/tx_features.py cells` from the printed
  sheet PNG only (the 9 x 110 px grid; ids read from sign_id_map_1572.json's id field, sorted; no value, no hand tile, no
  truth). Measures in the tool's docstring. Known limits, seen on the sheet before any read and NOT tuned further: the
  bar count also counts flat loop tops (as tx_pair_hints.py); desc/asc are relative to a script "body band", so a sign
  whose lower curl is wide (T76) reads desc none; the reader is told to choose by the rest of the shape where cells tie.
  One revision before the read, on the sheet alone: the body band joins wide-row runs at least half as long as the longest
  (first version called a C's bottom bar a long descender).
- Reader tasks: `reader_task_dev_c1.md` (L01-06, 18 crops), `reader_task_dev_c2.md` (L07-12, 18 crops), pass A's grouping.
  Eval (only if the dev gate is met): c1 f178v L13-L18 (18 crops), c2 f178v L19-L23 + f179r L01-L03 (24 crops), same rule.

## Reader
One blind Opus 5.5 subagent per call (`model: opus`); prompt: "Your instructions are in the file <task>. Read that file
first and follow it exactly. Besides that file, open only the images it names (the sign sheet and the crops). Write only
the TSV it names." Raw reads `reads/passU_raw_dev_c1.tsv`, `_c2.tsv` committed and pushed before any scoring; normalised
with `tools/tx_features.py norm` -> `benchmark-tx/outputs/birago1572-no87/passU_feature_dev_tune.tsv`.

## Gate (fixed now)
`python3 tools/tx_bench.py benchmark-tx/outputs/birago1572-no87/passU_feature_dev_tune.tsv --bench BENCHMARK-TX.tsv --item
birago1572-no87 --paired benchmark-tx/txeng/units/passA_dev_tune.tsv`: PASS iff fixed > broken and p < 0.01. Vs
`labels_dev_tune.tsv` (L) reported, not gating. Met -> eval_heldout read once (two calls), paired vs passA_eval_heldout.tsv
(gate fixed > broken, p < 0.01) and labels_eval_heldout.tsv reported; that is the one eval look. Not met -> FAIL, no eval.

## Secondary (read-free, after the dev reads are committed)
`tools/tx_features.py consist`: per sign, the number of written features that contradict the chosen cell's; flag at >= 2
contradictions. Reported: share of wrong signs flagged vs share of right signs flagged (wrong = tx_bench wrong/deleted
positions vs truth, derived only after commit). A useful sorter flag would hold a clearly larger share of wrong signs than
of right ones; no gate is attached (descriptive). Also `tools/tx_taxonomy.py` movement A -> U -> L.

## Calls and stops
Vision calls: dev 2, eval 2 at most. Cap 7, box 07:59-09:29 UTC; stop before a call that would cross 80% of either.
