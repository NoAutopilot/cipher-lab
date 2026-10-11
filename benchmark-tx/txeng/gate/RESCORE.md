# TXE-F tile gate -- RESCORE (11 Oct 2026, 18:0x UTC by date -u)

**Measurement correction: box-to-position map fixed (off by one), not a new gate look.** BOXMAP-RESCORE (others), account-3 parent (session_0198Cv8ypBfBVfRToKVWx33M); script-only, no model call. Method, tables and the shifted-position list: `benchmark-tx/txeng/RESCORE.md`.

Re-run (`tx_tile_gate.py gate --box-pos benchmark-tx/txeng/rescore_boxmapLA/box_pos.tsv`; outputs `benchmark-tx/txeng/rescore_boxmapLA/gate/`, with the old box_pos re-run today beside them, since TX-TRUTH-VERIFY changed the truth after this run). Dev recall 0.417 at 19.2% flagged -> 0.417 at 17.2%; eval 0.333 at 18.4% -> 0.333 at 17.3%. **NOT MET, unchanged.**
