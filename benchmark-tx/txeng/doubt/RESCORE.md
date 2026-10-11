# TXE-O doubt -- RESCORE (11 Oct 2026, 18:0x UTC by date -u)

**Measurement correction: box-to-position map fixed (off by one), not a new gate look.** BOXMAP-RESCORE (others), account-3 parent (session_0198Cv8ypBfBVfRToKVWx33M); script-only, no model call. Method, tables and the shifted-position list: `benchmark-tx/txeng/RESCORE.md`.

Re-run (`tx_doubt.py signals --box-pos` on the rebuilt box_pos; `benchmark-tx/txeng/rescore_boxmapLA/doubt/`). The `disagree`, `latt`, `contrast`, `freq` and `pair` columns are identical; `show`, `bandcut`, `thin`, `stab` change on 4 to 82 positions per column and unit (`show` 28 dev / 82 eval). The best combination, disagree+latt, reads no box: dev 6/12 at 10.5%, eval 9/15 at 6.1%, unchanged. **FAIL, unchanged.** `show` alone keeps eval recall 14/15 at half the flag rate (40.2% -> 20.2%).
