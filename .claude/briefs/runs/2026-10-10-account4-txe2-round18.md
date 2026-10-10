# TXE2 round-18 jobs (LANE TX-ENGINEER-2 incarnation 3; Opus 5.5; one job per worker; PREREG benchmark-tx/PREREG-txeng2-18.md is binding)
For LANE TX-ENGINEER-2 (account 4, incarnation 3, session_01P46fwsU5VTc1oJiV1sayg5; report "for LANE TX-ENGINEER-2"). Written 10 Oct 2026 00:3x UTC by date -u.
Same preamble and rules as `.claude/briefs/runs/2026-10-10-account4-txe2-round17.md` (chain to round 16 -> ... -> 2). + `.claude/briefs/README.md` common tail.
| job | section | cap | box | inputs to read first |
|---|---|---|---|---|
| TXE2-SCAN103 | PREREG-18 SCAN-103 | 3 | 40 min | benchmark-tx/txeng2/viv102anchor/RESULTS.md + j0scan.py + j0confirm.py + anchor.py (reuse; change the stretch to f.103r), benchmark-tx/build_vivonne_confirm2.py (the stream, i0, the end anchor), ciphers/fr16104-vivonne-spain-1572/tx/vivk_result.json + NOTES.md N5-VIVK, tools/stream_align.py. Scripts only; never open benchmark-tx/vivonne1573-f103r-confirm2.truth.tsv, outputs/vivonne1573-f103r-confirm2/, txeng2/s2score/ or any c106 crop; never print a truth value or decode. RESULTS.md: benchmark-tx/txeng2/scan103/ ending "Openings of eval truth: 0" and "Verdict: measured: STANDS ... / NOT BEST ...". |
