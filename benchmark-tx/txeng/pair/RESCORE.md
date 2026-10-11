# TXE-C pair re-read -- RESCORE (11 Oct 2026, 18:0x UTC by date -u)

**Measurement correction: box-to-position map fixed (off by one), not a new gate look.** BOXMAP-RESCORE (others), account-3 parent (session_0198Cv8ypBfBVfRToKVWx33M); script-only, no model call. Method, tables and the shifted-position list: `benchmark-tx/txeng/RESCORE.md`.

Not re-run (reads). `pair/dev_tune/box_pos.tsv` equals the old map's 333 dev 1:1 boxes, so 51 dev positions had a shifted box, but neither of the run's two changed positions (fixed 1 / broken 1) is among them. **FAIL unchanged.** The 51 selected eval positions (written, never read) were selected through the same join; a rebuilt per-unit map is `benchmark-tx/txeng/rescore_boxmapLA/box_pos_1to1_eval_heldout.tsv`.
