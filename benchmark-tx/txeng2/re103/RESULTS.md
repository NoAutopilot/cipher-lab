# RE103 (TX-RE103, PREREG-txeng2-20 section RE103): STOPPED at step 3 -- build control outside SCAN-103's tolerance; no re-score

Worker TX-RE103 (account-4, Opus 5.5, session_01LpVC17SHaMND2FjAvtq9Xm), 10 Oct 2026 01:15-01:2x UTC by date -u, for LANE
TX-ENGINEER-2 (account-4). Read-free: scripts only; no truth TSV opened by eye, no flags changed, no crops, no readers.

## Step 1 -- `--start S` on build_vivonne_confirm2.py
Added as build_vivonne_f102r.py's DV1d option: the f.103r stretch alone is aligned (same DP, band 400) to dec_norm[S : S+3624]
(3624 = SCAN-103's W, scan.json; clipped at the end of dec_norm, so [6500 : 9554] here); key forcing, exclusions, flag rule,
control unchanged; TXV-VIV verdicts re-applied from the frozen confirm2.flags.tsv by (line, raw position) where align-conflict
recurs; the build also prints the selection-fair margin against SCAN-103's best-over-scan null max (0.5782, confirm.json).
`--check` on the frozen item: **ok** before and after the edit (sha256 5d228b454ef556fa1e6d23cc7dca9fa3c58f332035792e0454b9f156ad2cfe7f).

## Step 2 -- build at 6500 (output: build_s6500.out, counts and control only)
Positions 2,033; scored 1,112; excluded 921 (unaligned 277, align-uncertain 255, off-key 132, key-M S 105 / y 41 / b 5 / A 2,
letter-off-key 104). Flags on scored: align-conflict 148, clerk-split 472, any 636, none 476.
Truth sha256 would be 5ac8f5e05c5c9641a78d7ee057adfe20e94e8bd0825e8a39d2354aecd6268cef (deterministic; `--start 6500` regenerates it).

## Step 3 -- the gate: FAIL by 0.002, so STOP
| | build at 6500 | SCAN-103 confirm row (6500) | diff | tolerance |
|---|---|---|---|---|
| published-key share | 0.6069 | 0.6139 | 0.0070 | 0.005 |
| selection-fair margin | 0.0287 | 0.0357 | 0.0070 | 0.005 |
| shuffled keys mean / p95 / max | 0.426 / 0.498 / 0.557 (rank 1/201) | 0.4311 / 0.5017 / 0.5565 | | |

Per the PREREG ("else STOP and report (no re-score)"): the new item was **not** registered (no BENCHMARK-TX.tsv row), its
truth, sha256 and outputs folder were deleted after hashing, and **run_audit.sh was not run**. passZ_S2b re-score: **not run**.
Record unchanged: 0.150 on 500 / 0.296 on 1,068 (value-level).

Openings of eval truth: 0 (the re-score did not run). The look of 22:22:57 UTC 9 Oct is untouched; nothing here is a look.

## Why the two numbers differ (one script diagnostic, counts only)
The frozen control re-crops its window to the aligned span +/- 200 letters; SCAN-103's statistic scores the whole window. At
S = 6500 the free-start DP places the f.103r stretch's first aligned letter at dec_norm 6881 (last 9553, 1,673 aligned signs),
so the builder's control window is [6681 : 9554], not SCAN's [6500 : 9554]. The frozen build's aligned span started at 6855
(R = 6655 = j0 + lo, lo = start - 200), so the re-anchored alignment begins **26 letters** from the frozen one, and the control,
measured on almost the same window, reads 0.607 -- next to SCAN's registered-offset 0.6049, not its 6500 figure 0.6139.

What moved and why: measured -- the re-anchor at 6500 moves the f.103r path's start by 26 letters, and the builder's span-cropped
control does not reproduce SCAN-103's whole-window share; the scorer correction is not involved (nothing was scored).

For the lane (not acted on; a brief change is the lane's): matching SCAN-103 would need either the control on the whole window
(a different control from the frozen recipe, which the PREREG fixes as unchanged) or a tolerance stated against the builder's
own control convention. Either is a new declaration before any re-run, never a retune here.

Cost: one builder --check x3, one build, one diagnostic; no subagents, no network.

Amendment of 01:2x (PREREG-20, relabel to a declared sensitivity check): read after the stop; it keeps "the control agreement
within 0.005", so the STOP stands under it. No relabel message reached this worker before the build; the item was never
registered under either split.
