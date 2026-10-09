# TXE-D2: one blind read at 4x (LANE TX-ENGINEER, idea M4 read; account 4, Opus 5.5; cap 7, box 80 min)

Read `.claude/briefs/runs/2026-10-09-account4-txe-COMMON.md` first, then `benchmark-tx/txeng/prep/RESULTS.md` (TXE-D: on the
read-free atlas proxy, LANCZOS 4x `sr4` was the best rendering, top-1 err 0.216 -> 0.192, fixed 9 / broken 1, p 0.02 -- a
near-miss under the p < 0.01 proxy gate, so no read was made; gains sat in the heavy and mid stroke terciles) and
`benchmark-tx/PREREG-txeng-2.md` (units, blindness, Amendment). Why this job exists: the proxy is the atlas's HOG classifier,
not the reader; the owner's question is whether the reader does better on upscaled crops, and a near-miss on the proxy
earns exactly one pre-registered read.

## Pre-registration (write `benchmark-tx/txeng/prep/PREREG-D2.md` and push it BEFORE the read)
- Rendering: `tools/tx_prep.py lines --setting sr4` on the dev_tune line crops (harvest/f178v/f178v_L01..L12_s?.jpg): LANCZOS
  4x, nothing else. A 1250-px crop becomes 5000 px, over the 2500-px reading limit (CLAUDE.md Usage 8, iiif_lines.py step 4:
  never re-stitch, keep segments under 2500): cut each 4x crop into FOUR 1250-px-wide segments with a 200-px overlap (so
  the reader sees 36 x 4 = 144 crops at 4x), name them `<crop>_q1..q4`, and generate the overlap sentence for the brief with
  `iiif_lines.py --overlap-note` (TXE-B's option) or the same arithmetic stated in the note. State in PREREG that this
  changes two things at once (scale and segment count): if the read loses, the loss is not attributable to scale alone.
- Reader: blind Opus 5.5 subagent passes with the unchanged `harvest/blind_pass_brief_1572.md` + `sign_sheet_blind_1572.png`
  plus the generated crops note (scale 4x, overlap), in FOUR calls (L01-03, L04-06, L07-09, L10-12; 36 crops each) --
  not two, because the crop count has quadrupled. Raw reads to `benchmark-tx/txeng/prep/passK2_raw_dev_*.tsv`; commit and
  push before scoring; normalise as build_birago87.py does for pass A -> `benchmark-tx/outputs/birago1572-no87/
  passK2_sr4_dev_tune.tsv` (join the q-segments per line by the overlap rule, counting a sign in two segments once; say
  how many joins were ambiguous).
- Gate (fixed now): `tools/tx_bench.py passK2_sr4_dev_tune.tsv --bench BENCHMARK-TX.tsv --item birago1572-no87 --paired
  benchmark-tx/txeng/units/passA_dev_tune.tsv`: fixed > broken, p < 0.01 (the same reader kind on plain crops); vs
  labels_dev_tune.tsv reported. Met -> eval_heldout once (f178v L13-23 + f179r L01-03, four calls), paired vs
  passA_eval_heldout.tsv and labels_eval_heldout.tsv: the single eval look. Not met -> FAIL, no eval. Report also the
  per-tercile movement (thin / mid / heavy) with `tools/tx_taxonomy.py` after the reads are committed, since TXE-D predicted
  the thin tercile would not move.

## Report
`benchmark-tx/txeng/prep/RESULTS-D2.md`: PREREG hash, the tx_bench lines, the tercile table, joins, reader task text,
calls. One Results-log row in research/TX-IDEAS-2026-10-09.md (id M4-read; rebase before editing); update M4's status.
Shelf row for `tx_prep.py` regraded from the result. Vision calls: dev 4, eval 4 at most, x about 1.5; cap 7; stop before a
call that crosses 80% of cap or box. Report in a short paragraph (first line: dev and eval fixed/broken/p vs A) and stop.
