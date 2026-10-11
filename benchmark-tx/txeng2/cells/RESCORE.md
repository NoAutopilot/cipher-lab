# TXE2-CELLS -- RESCORE (11 Oct 2026, 18:0x UTC by date -u)

**Measurement correction: box-to-position map fixed (off by one), not a new gate look.** BOXMAP-RESCORE (others), account-3 parent (session_0198Cv8ypBfBVfRToKVWx33M); script-only, no model call. Method, tables and the shifted-position list: `benchmark-tx/txeng/RESCORE.md`.

Not re-run (Opus reads). Its rows were built on `txeng/pair/dev_tune/box_pos.tsv` (the old width DP). 2 of its 19 changed positions are on shifted boxes, both breaks; on the right boxes fixed 2 / broken 12 (p 0.013, wrong way). **Verdict FAIL (the wrong way) unchanged.**
