# TXE-D prep proxy (and D2) -- RESCORE (11 Oct 2026, 18:0x UTC by date -u)

**Measurement correction: box-to-position map fixed (off by one), not a new gate look.** BOXMAP-RESCORE (others), account-3 parent (session_0198Cv8ypBfBVfRToKVWx33M); script-only, no model call. Method, tables and the shifted-position list: `benchmark-tx/txeng/RESCORE.md`.

Proxy re-joined from the committed per-setting top-k (`benchmark-tx/txeng/rescore_boxmapLA/prep/rebench.py`; the old map reproduces all 10 bench files byte for byte): plain 0.216 -> 0.207, sr4 0.192 -> 0.190 (fixed 9 / broken 1, p 0.0215 -> 8 / 1, p 0.039), combo 0.187 (10 / 3). **Gate (p < 0.01) not met, unchanged.** D2 (the 4x Opus read, not re-run): 6 of 48 changed positions on shifted boxes, none of its 11 breaks; FAIL unchanged.
