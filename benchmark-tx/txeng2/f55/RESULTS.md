# F55-REDERIVE: the four baseline-change paired cells re-derived under drop_flagged with the fixed scorer (lane incarnation 4, 10 Oct 2026)

Run by LANE TX-ENGINEER-2 incarnation 4 (session_01GukpgU1yBAfju3zg6g8ayG) in its own session, 01:0x UTC 10 Oct 2026 by date -u
(run_times.txt), under PREREG-txeng2-19 F55-REDERIVE (pushed 4cc8017d9 before the run; PREREG sha256
f4bd96a7af4803767e14c11ddeb0a0265c73f55b64a7a62af4a9bb63af604996). Read-free: scorer runs only; no reader, no crop, no truth file
opened by eye. Inputs hashed first (SHA256SUMS.prescore); scorer tools/tx_bench.py at 6896cf0e7 (TOOL-SCORER-FIX). Commands as
the PREREG fixed them; one .txt per cell. Openings of eval truth: 2 (Spinelli, gunther; read-free re-scores, counted in the
openings ledger). No gate verdict rests on any cell (eval looks 0); every cell is a baseline change, never a gain.

| cell | files | mask | OLD cell (pre-fix paired(), flags ignored) | position McNemar under drop_flagged (fixed scorer) | line-level edit totals (the S1 endpoint, F56): improved / worsened / tied, sign test p; unit-cost edits base -> output |
|---|---|---|---|---|---|
| B1 | Spinelli passZ_v4 vs passZ_pipeline, collapse_map | flagged-excluded, 191 | fixed 8 / broken 2 | fixed 8 / broken 2, p 0.1094 (base wrong 12 -> 6) | 4 / 2 / 4, p 0.6875; 14 -> 9 over 191 |
| B2 | Spinelli passZ_v5 vs passZ_v4, collapse_map | flagged-excluded, 191 | fixed 2 / broken 4 | fixed 2 / broken 4, p 0.6875 (6 -> 8) | 3 / 3 / 4, p 1.0; 9 -> 11 |
| fold | Spinelli passZ_v5 vs passZ_v4, collapse_map_fold | flagged-excluded, 191 | fixed 4 / broken 4 | fixed 4 / broken 4, p 1.0 (6 -> 6) | 4 / 3 / 3, p 1.0; 9 -> 9 |
| B3b | gunther passZ_gv2 vs passZ_pipeline | flagged-excluded, 305 | fixed 6 / broken 6 | **fixed 4 / broken 4**, p 1.0 (5 -> 5) | 2 / 3 / 20, p 1.0; 5 -> 6 |

As measured (all scored positions) the McNemar cells equal the old ones (B1 8/2 on 193; B2 2/4; fold 4/4; B3b 6/6 on 317): the
old paired() was in fact computed on the as-measured population, so the Spinelli cells happen to coincide under both masks (its two
flagged positions carry no fixed/broken event), while gunther's two flagged positions each carried one fixed and one broken event
-- the B3b cell of record becomes 4 / 4 under the flagged-excluded mask (Amendment 9 (1) said 6 / 6; p 1.0 either way; the pool
count 6 is unchanged, it is the position-error count). Line level: no baseline change improves more lines than it worsens at any
p below 0.68; B1 is the only one with a net gain (14 -> 9 edits on 191, 4 lines improved / 2 worsened).

Note on the pool counts versus the SER: Amendment 9 quotes Spinelli under the fold as "8/193, 6/191" -- those are position
(wrong) counts; the fixed scorer's standard SER on the same files is 11/193 = 0.057 / 9/191 = 0.047 because passZ_v5 also carries
3 line insertions (S 6 D 0 I 3 on 191). The pool counts positions (the paired gate excludes insertions, F47/F48); the headline SER
includes them. Both are value-level (F53; the visual-ID companion is in ../compvis/).

Tool note (recorded for the audit script): without --paired, tx_bench loads several positional outputs as ONE merged output
(the multi-part convention); per-file scores without --paired need one invocation per file. run_audit.sh passes --paired, so its
six S2 files are scored separately (groups per file), as intended.
