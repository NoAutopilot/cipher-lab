# TXE2-BASE-SPIN: reader and adjudicator briefs, committed before any read (PREREG-txeng2-6 B1)

9 Oct 2026, written ~20:05 UTC by date -u. Job TXE2-BASE-SPIN (account 4, Opus 5.5) for LANE TX-ENGINEER-2.
Binding: a baseline change, never a gain (Amendment 4); no instrument; no paired "instrument" claim.

- Readers: `reader_task_v4.txt` = TXE-Q's `benchmark-tx/txeng/confirm/reader_task.txt` with only the sheet path changed
  (atlas.png -> atlas_v4.png, sha256 4ad8c048...) and "do not resize" added (the round-7 brief's wording). Diff: `reader_task_v4.diff`.
  Same committed crops (benchmark-tx/txeng/confirm/crops/, 20 files), same split as TXE-Q: ONE call per pass with all 20 crops.
  atlas_v4 keeps v3's 23 cell names (cut -f1 diff: identical), so collapse_map.tsv needs no new row.
- Two blind Opus 5.5 subagents (passA_v4, passB_v4): crops + atlas_v4 + the brief only.
- Reconcile: `tools/reconcile_passes.py passA_v4.tsv passB_v4.tsv --crops benchmark-tx/txeng/confirm/crops --out-dir
  benchmark-tx/txeng2/basespin/rec --keep-alts`; disagreements + uncertain -> ONE Sonnet adjudicator call with
  `adjud_task_v4.txt` (TXE-Q's adjud_task.txt with sheet -> atlas_v4, queue/out paths -> this folder, and "view every crop
  named by a queue row; do not resize" folded in from TXE-Q's resume message), applied mechanically -> passZ_v4.tsv.
- Score ONCE (the brief's command, --exclude-flagged, --label-map collapse_map.tsv), passZ_pipeline.tsv paired as the old
  baseline; passA_v4/passB_v4 alone beside. Nothing re-read or re-adjudicated after scoring.
