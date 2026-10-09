# PREREG TXE-D2: one blind read at 4x (LANE TX-ENGINEER, idea M4 read; 9 Oct 2026, written 07:5x UTC by date -u, BEFORE any read)

Brief `.claude/briefs/runs/2026-10-09-account4-txe-d2.md`; binds under `benchmark-tx/PREREG-txeng-2.md` (units, blindness,
Amendment: single-instrument gate p < 0.01). Why: TXE-D's read-free proxy put LANCZOS 4x (`sr4`) at 9 fixed / 1 broken,
p 0.0215 -- a near-miss; the proxy is the atlas HOG classifier, not the reader, so one pre-registered read asks the reader.

## Rendering (fixed)
`python3 tools/tx_prep.py lines --crops ciphers/nevers-birago-fr3251-1572/harvest/f178v --setting sr4 --segments 4
--overlap 200 --only f178v_L01_ ... --only f178v_L12_ --out <scratch>/sr4dev` -- LANCZOS 4x of the 36 dev_tune line crops,
nothing else. Each 1250 px crop becomes 5000 px, cut into four segments `<crop>_q1..q4` sharing 200 px (50 native), 144
crops in all, every one 1400 px wide (under 2500; never re-stitched).
Deviation from the brief's wording, fixed now: the brief says "four 1250-px-wide segments with a 200-px overlap"; four
1250 px pieces sharing 200 px cover only 4400 of 5000 px, so the segments are 1400 px (4 x 1400 - 3 x 200 = 5000), which
keeps the two binding parts (four segments, 200 px shared, each under 2500). `--segments` is a new option on tools/tx_prep.py
(test in tools/tests/test_tx_prep.py), not a private script.
**This changes two things at once (scale 2x -> 4x and segment count 3 -> 12 per line): a loss is not attributable to scale
alone; a win is attributable to the pair.** The crops note (`crops_note_D2.md`) is generated from the tx_prep manifest and
the source crop manifest (s overlap 425 native = 1700 px at 4x; median sign width 66 native from atlas/signs.tsv), never
typed.

## Reader (fixed)
Blind Opus 5.5 subagents, FOUR calls (L01-03, L04-06, L07-09, L10-12; 36 crops each). Task text = the unchanged
`harvest/blind_pass_brief_1572.md` + `sign_sheet_blind_1572.png`, then crops_note_D2.md, the 36 crop paths and the output
path. Nothing else; no truth, decode, atlas or other pass. Raw reads -> `benchmark-tx/txeng/prep/passK2_raw_dev_L01-03.tsv`
etc., committed and pushed before scoring. Normalised as build_birago87.py does for pass A (line = f178v_<passage>, pos,
sign_id) -> `benchmark-tx/outputs/birago1572-no87/passK2_sr4_dev_tune.tsv`. Joins: the reader de-duplicates overlaps itself
(as pass A's reader did); I report the line-length difference vs pass A per line and the reader rows whose note flags an
overlap/duplicate doubt as "ambiguous joins". No position is edited after the read.

## Gate (fixed)
`python3 tools/tx_bench.py benchmark-tx/outputs/birago1572-no87/passK2_sr4_dev_tune.tsv --bench BENCHMARK-TX.tsv --item
birago1572-no87 --paired benchmark-tx/txeng/units/passA_dev_tune.tsv`: PASS iff fixed > broken and two-sided sign test
p < 0.01. Reported, not gating: the same vs `labels_dev_tune.tsv`; per-tercile movement (thin / mid / heavy) by
`tools/tx_taxonomy.py`. Prediction (TXE-D): the thin tercile does not move; any gain sits in mid/heavy.
Met -> eval_heldout ONCE (f178v L13-23 + f179r L01-03, four calls, same rendering), paired vs passA_eval_heldout.tsv and
labels_eval_heldout.tsv; that is the instrument's single eval look. Not met -> FAIL, no eval.
Stop rule: before any call that would cross 80% of cap 7 (5.6) or of the 80-min box (08:46 UTC); eval needs the cap left.
