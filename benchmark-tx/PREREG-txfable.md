# PREREG TX-FABLE (4 Oct 2026, 15:4x UTC, account-3 worker; pushed before any Fable call)

Owner's question: is a Fable reader meaningfully better than the Sonnet readers on our known-answer transcription items?
Brief `.claude/briefs/runs/2026-10-04-acct3-tx-fable.md`. Readers: Fable (`claude-fable-5-1`, Agent tool model `fable`),
one blind pass per item. Worker (Opus) scores only and reads no crop.

## Passes (one blind Fable pass per BENCHMARK-TX item; prompts frozen at this commit in `benchmark-tx/txfable/prompts/`,
built by `benchmark-tx/txfable/make_prompts.py`)

| item | split | pass-A brief reused | crops (same as pass A) | calls (pass-A grouping) |
|---|---|---|---|---|
| birago1572-no87 | eval | nevers-birago harvest/blind_pass_brief_1572.md + sign_sheet_blind_1572.png | harvest/f178r, f179r, f178v `*_L??_s?.jpg` (87) | 3: f178r+f179r (18), f178v L01-10 (30), L11-23 (39) |
| dint-f128-print | dev | fr3621-dinteville f128/pass_instructions.md (labels in text) | images/f128_L02-L05_s1,s2 (8) | 1 |
| ceppo-f21v-S | dev | ceppo harvest/blind_pass_brief.md + sign_sheet_blind.png | harvest/f21v/lines2x (33, re-cut by cut_folio_lines.py from the committed region) | 2: L01-06 (18), L07-11 (15) |
| ceppo-f87-S | dev | same | harvest/f87/lines2x (18, re-cut, follow=True) | 1 |
| ceppo-f36v-gloss | dev | birago-fr3252 harvest/f36/prompt_A_v36.md (sheet sign_sheet_blind.png, gloss asked) | f36/crops v36top_L01_s1-s4 (re-cut by witness_f36/cut_lines.py cut(...,850,0,120,65,2)) | 1 |

Disclosed deviations (decided before any call):
1. The task wrapper adds one line ("read only the image files listed; do not open any other file") and the absolute sheet
   path; the brief text itself is pasted unchanged.
2. Ceppo f.21v / f.87: the per-line prose layout that pass A's task text carried is not on disk (NOTES says it was in the
   task text). Reconstructed from the prose words that passes A and B both quote in their own first/last-row notes (they
   agree on every anchor); prose words only, no sign or value. f.87's L01 anchor from NOTES ("... per alcuni suoi particolari").
3. ceppo-f36v-gloss: pass A read 52 crops (whole f.36v-37r) in one call; only v36top_L01 pos 1-18 is scored, so the Fable call
   gets that line's 4 crops only (cost). This shortens the call; any fatigue effect it removes favours Fable on this item
   (18 signs, smallest weight). Disclosed, not corrected.
4. The no.87 call 1 writes two files (f178r, f179r), as pass A did per leaf.
Readers see crops + sheet only, never truth, values, decodes or other passes. The worker opens no `*.truth.tsv` until every
Fable file for that item is committed (scoring goes through tools/tx_bench.py).

## Normalisation (no edits to reader output)
Raw files land in `benchmark-tx/txfable/raw/`; `benchmark-tx/txfable/norm.py` writes `benchmark-tx/outputs/<item>/passF_fable.tsv`
with the same rules the item's build script applies to pass A (build_birago87.py, build_dint128.py, build_ceppo.py
write_out; f36v only_lines v36top_L01). A call that fails or truncates is scored as is (missing lines count).

## Gate (fixed now)
"Meaningfully better" = BOTH
(a) pooled over the five items, Fable vs the better (lower err_true) of each item's two Sonnet single passes A/B:
    sum of `tools/tx_bench.py passF --paired <better>` fixed > sum broken, and the two-sided exact sign test on
    (fixed, broken) pooled gives p < 0.05;
(b) Fable's err_true strictly lower than that better Sonnet single pass on birago1572-no87 (eval) AND on at least 3 of the
    4 dev items.
dint-f128-print is scored with `--label-map benchmark-tx/dint128_label_map.tsv` for the gate (the blind-pass inventory);
without it reported too. Informative, not the gate: Fable vs the reconciled/committed read where one is scorable
(no.87 passC; f36v recon), and cost per 100 signs (Fable job vs the Sonnet rate from TX-SHEET, USD 0.74/100 signs).
If the gate passes, RESULTS.md proposes a one-line model-rule change for the parent; this worker changes no rule.

## Order and cost
Calls in order: no87 c1-c3, dint, f21v c1-c2, f87, f36v (8 calls). Cap USD 30, box 120 min (start 15:29 UTC). After the
first call the per-call cost is measured and written in RESULTS.md; no call starts that would cross 80% of the cap (USD 24)
or of the box; what is done is scored in the brief's order.
