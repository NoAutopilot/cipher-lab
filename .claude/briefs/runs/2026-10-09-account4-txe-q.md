# TXE-Q: the confirm item, read once with today's pipeline (LANE TX-ENGINEER round 3, Amendment 2 guard 2; account 4, Opus 5.5; cap 12, box 120 min)

Read `.claude/briefs/runs/2026-10-09-account4-txe-COMMON.md` first, then `benchmark-tx/PREREG-txeng-3.md` (the "Decision"
section: the crop step did not clear a second unit, no instrument moved eval, and the confirm item is scored ONCE with
today's pipeline whatever that pipeline is) and TRANSCRIPTION.md "The pipeline". Why this job exists: Amendment 2 guard 2
asks for the campaign's headline to be a number on a leaf the lane never tuned on, built by another account:
BENCHMARK-TX.tsv row `spinelli-c1519-confirm` (split=confirm; Beinecke GEN MSS 109 Filza 163, Tommaso Spinelli, Barcelona
c.1519; a different hand from every dev/eval item; built by TX-CONFIRM-SET, commit 74934b71, with a sha256). Nobody in
this lane has opened it. You open its folder ONLY as this brief says.

## Order of operations (binding)
1. Read the BENCHMARK-TX.tsv row for `spinelli-c1519-confirm` and the item's `crops` / `lines` / `outputs` / `notes` cells, and
   the folder's README or NOTES ONLY for: where the crops are, which sheet/brief the folder's own blind passes used (if any),
   the line ids. Do NOT open `benchmark-tx/spinelli-c1519-confirm.truth.tsv` (or whatever the truth cell names), any
   existing pass output under benchmark-tx/outputs/spinelli-c1519-confirm/, any decode, key-applied reading or gloss.
   Write `benchmark-tx/txeng/confirm/PREREG.md` naming the crops, the sheet, the brief, the call grouping, the two reader
   subagents, the reconciliation protocol, and this gate: the pipeline's reconciled read is scored ONCE with
   `tools/tx_bench.py OUT.tsv --bench BENCHMARK-TX.tsv --item spinelli-c1519-confirm` (plus `--paired` against the item's
   existing best output if `outputs` names one -- open that file only at scoring time). Push PREREG before any read.
2. Crops: if the folder already has line crops from `tools/iiif_lines.py`, use them; if any line's debug overlay or
   `--check-boxes` shows a slope, re-cut that line with `--follow-slope` (the one crop rule round 2 adopted). If the folder
   has only a page image, cut with `tools/iiif_lines.py --image ... --band-extent 0.1 --mask-neighbours --overlap-note
   --debug` and check the overlay. Paste the commands.
3. Two blind Opus 5.5 passes (value-blind, the folder's own sign sheet and blind brief if it has them; else the sheet the
   benchmark row's `notes` names; one call per 20-40 crops), then `tools/reconcile_passes.py passA passB --crops`, the
   disagreements and uncertain.tsv settled by one Sonnet third-reader call from the crops with the agreed neighbours as
   landmarks (the folder protocol of nevers-birago; TXE-K showed a stronger adjudicator does not help). Commit each pass
   and the reconciliation before scoring. No relabel map exists for this hand; none is invented.
4. Score ONCE: `benchmark-tx/outputs/spinelli-c1519-confirm/passZ_pipeline.tsv` through tx_bench as in 1; also each single
   pass (reported, not a second look at the pipeline). Then `tools/tx_taxonomy.py` on the pipeline read for the class
   breakdown. Write `benchmark-tx/txeng/confirm/RESULTS.md`: the one headline line, the single-pass lines, the taxonomy
   classes, call count, cost note. The register's "Eval looks" line gains "confirm item: 1 look (TXE-Q)".

## Report
Results-log row in research/TX-IDEAS-2026-10-09.md (id CONFIRM; rebase before editing). No tool change expected; if a
crop option is needed, add it to iiif_lines.py with a test. Vision calls: 2 passes x 1-3 calls + 1 adjudication; cap 12;
stop before a call that crosses 80% of cap or box. Report in a short paragraph (first line: the headline err_true with its
CI, the two single-pass figures, and the paired line if any) and stop. Never describe the number as a result for the
hand beyond this leaf.
