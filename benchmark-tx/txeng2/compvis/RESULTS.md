# COMP-VIS: F53 visual-ID companion scores on the Spinelli and gunther outputs (lane incarnation 4, 10 Oct 2026)

Run by LANE TX-ENGINEER-2 incarnation 4 (session_01GukpgU1yBAfju3zg6g8ayG) in its own session, 01:0x UTC 10 Oct 2026 by date -u
(run_times.txt), under PREREG-txeng2-19 COMP-VIS (pushed 4cc8017d9 before the run). Read-free: scorer runs only (tools/tx_bench.py
at 6896cf0e7, `--strict` = exact ref_sign match = visual identity; the default = the value-compatible truth set). Inputs hashed
first (SHA256SUMS.prescore). Each file scored ALONE (a first multi-file invocation without --paired merged the files into one
output -- the tool's multi-part convention -- and was discarded; the per-file runs below replaced it, run_times.txt has both
times). Openings: the same two items as ../f55/ in the same session (counted there). No gate, no look; a companion figure only.

| item | output | mask | value-level (the figure of record) | visual-ID (--strict) | credit in the value score |
|---|---|---|---|---|---|
| Spinelli (fold map) | passZ_v5 (the base) | flagged-excluded, 191 | 0.047 (9/191) | **0.068 (13/191)** | +4 positions |
| | passZ_v5 | as measured, 193 | 0.057 (11/193) | 0.078 (15/193) | +4 |
| | passA_v5 | flagged-excluded | 0.079 (15/191) | 0.089 (17/191) | +2 |
| | passB_v5 | flagged-excluded | 0.037 (7/191) | 0.058 (11/191) | +4 |
| | passZ_pipeline (the old base) | flagged-excluded | 0.079 (15/191) | 0.084 (16/191) | +1 |
| | committed | flagged-excluded | 0.016 (3/191) | 0.000 (0/191) | ref_sign IS the committed sign: 0 by construction |
| gunther | passZ_gv2 (the base) | flagged-excluded, 305 | 0.020 (6/305) | **0.020 (6/305)** | 0 |
| | passZ_gv2 | as measured, 317 | 0.051 (16/317) | 0.032 (10/317) | -6: six as-measured 'errors' are align-conflict rows where the output matches the committed sign (ref_sign) but not the key's value set; all flagged, so absent under the mask |
| | passA | flagged-excluded | 0.020 (6/305) | 0.020 (6/305) | 0 |
| | passB | flagged-excluded | 0.020 (6/305) | 0.020 (6/305) | 0 |
| | passZ_pipeline | flagged-excluded | 0.016 (5/305) | 0.016 (5/305) | 0 |
| | committed | flagged-excluded | 0.000 (0/305) | 0.000 (0/305) | 0 by construction |

Reading. On Spinelli the value score credits 4 of the base's 13 visual misreads through a shared key value (a homophone or
allograph read as another cell of the same letter): the visual-ID figure for the Spinelli base is 0.068, not 0.047, under the
same mask -- the pool count (6 position errors) is value-level and stays as declared; the visual figure is reported BESIDE it from
now (Amendment 9 (27)). On gunther the two figures coincide under the mask (0.020): the committed sign and the key's value set
agree at every unflagged position, so no homophone credit is in play there. The strict score depends on ref_sign being the
visual identity: on both items ref_sign is the committed reader's atlas code, so 'visual identity' here means 'the same atlas
code the committed reader gave', and the committed output scores 0 strict by construction (the F53 caveat: a frozen atlas, not
a reader's labels, is the visual reference the oracle diagnostic will build).
