# TXE2-BASE-SPIN: Spinelli confirm baseline re-read under the corrected sheet (PREREG-txeng2-6 B1)

9 Oct 2026, 19:58-20:1x UTC by date -u. Worker TXE2-BASE-SPIN (account 4, Opus 5.5) for LANE TX-ENGINEER-2 incarnation 2;
brief `.claude/briefs/runs/2026-10-09-account4-txe2-round7.md`. **A baseline change, never a gain (Amendment 4).** This job
has no instrument and makes no paired instrument claim. The old-vs-new paired line below compares the two baselines and
nothing else.

Openings of eval truth: 1 (the baseline score)

## Protocol (TXE-Q's, with the sheet as the only change)
- Reader brief `reader_task_v4.txt`: TXE-Q's `benchmark-tx/txeng/confirm/reader_task.txt`, diff `reader_task_v4.diff`:
  ```
  3c3  Sheet ...glyphs/atlas.png  ->  ...glyphs/atlas_v4.png
  7c7  (20 files; view every one).  ->  (20 files; view every one at its own size; do not resize, downscale or crop any image.)
  ```
  The "do not resize" wording is the round-7 brief's. Crops are the same committed `benchmark-tx/txeng/confirm/crops/` (20).
  The call split is the same as TXE-Q's: one call per pass with all 20 crops. atlas_v4 keeps v3's 23 cell names
  (`cut -f1` of atlas.tsv vs atlas_v4.tsv is identical), so `collapse_map.tsv` needed no new row.
- Adjudicator brief `adjud_task_v4.txt`: TXE-Q's adjud_task.txt with the sheet changed to atlas_v4, the queue and output
  paths moved to this folder, and "view every crop named by a queue row; do not resize" added (diff `adjud_task_v4.diff`).
- Reconcile: `tools/reconcile_passes.py passA_v4.tsv passB_v4.tsv --crops benchmark-tx/txeng/confirm/crops --out-dir rec
  --keep-alts`. Pair agreement was 240/254 = 94.5% (TXE-Q 93.7%): 163 agreed-H, 77 agreed-uncertain, 14 disagreements.
  That gives a queue of 91 rows in TXE-Q's format, built mechanically by `build_queue.py queue`.
- Adjudication: one Sonnet subagent. Its first hand-back viewed only p1c_L01-02 (kept as `adjud_out_first.tsv`), the same
  shortfall TXE-Q hit. The same subagent was sent back once with TXE-Q's resume wording. The final output has 90 of 91 rows
  viewed=yes; p1c_L04 col 16 was not located. Confidence: 82 M, 9 L, 0 H. The adjudicator's own hand-back said "74 M, 16 L,
  1 H"; the file says otherwise and the file is what counts. `build_queue.py apply` changed 6 positions vs the draft, giving
  254 signs. 4 rows were adjudicated NEW: NEW:circle-on-stem (p1c_L02.27, p2c_L01.17) and NEW:long-s-crossbar (p1c_L02.28,
  p1c_L06.21). This counts as one adjudication with one resume, not a second reader.
- Score once: `python3 tools/tx_bench.py benchmark-tx/outputs/spinelli-c1519-confirm/passZ_v4.tsv --bench BENCHMARK-TX.tsv
  --item spinelli-c1519-confirm --label-map benchmark-tx/txeng/confirm/collapse_map.tsv --exclude-flagged --paired
  benchmark-tx/outputs/spinelli-c1519-confirm/passZ_pipeline.tsv`, then passA_v4 and passB_v4 alone with the same flags.
  `score_detail.py` re-uses tx_bench's own truth load, label map and alignment in the same process family to list positions.
  It is not a further reading of the image. Nothing was re-read or re-adjudicated after scoring.

## Calls and tokens
| call | model | tokens | tool uses |
|---|---|---|---|
| passA_v4 (20 crops + sheet) | Opus 5.5 | 130,417 | 23 |
| passB_v4 (20 crops + sheet) | Opus 5.5 | 128,177 | 23 |
| adjudicator, first hand-back | Sonnet | 108,701 | 9 |
| adjudicator, after the one resume (cumulative figure the harness reported) | Sonnet | 141,925 | 27 |
Dollar cost: the orchestrator's get_session reading.

## Results (label-mapped; spinelli-c1519-confirm only, never a figure for the hand beyond it)
```
passZ_v4  err_true 0.057 (11/193) 95% 0.032-0.099 | wrong 8 deleted 0 inserted 3 | excluded 66
          as measured 0.057 (11/193) | flagged excluded 0.047 (9/191) 95% 0.025-0.087 [2 flagged]
          top confusions: g<-NEW:circle-on-stem x2, u<-NEW:long-s-crossbar x2, i<-EIGHT, p<-THREE, s<-JHOOK, n<-PHI
passA_v4  err_true 0.062 (12/193) 0.036-0.105 | wrong 9 deleted 0 inserted 3 | flagged excluded 0.052 (10/191) 0.029-0.094
passB_v4  err_true 0.119 (23/193) 0.081-0.172 | wrong 19 deleted 2 inserted 2 | flagged excluded 0.110 (21/191) 0.073-0.162
```
| file | position errors (wrong+deleted), as measured | flagged-excluded |
|---|---|---|
| passZ_pipeline.tsv (old baseline, TXE-Q, atlas v3) | 14/193 | **12**/191 |
| passZ_v4.tsv (new baseline, atlas_v4) | 8/193 | **6**/191 |
| passA_v4 alone | 9/193 | 7/191 |
| passB_v4 alone | 21/193 | 19/191 |

### Baseline change, old -> new (paired, 193 common positions, as measured; a baseline change, not a gain)
`paired passZ_v4.tsv vs passZ_pipeline.tsv: base wrong 14, output wrong 8; fixed 8, broken 2; sign test p = 0.1094`
- Fixed, excluding the sheet-defect positions: p1c_L01.3, p1c_L03.4, p1c_L05.20, p2c_L01.27, p2c_L02.11 (5).
- **Sheet-defect positions (Amendments 4-5), listed separately:** p1c_L01.14 old wrong -> new right; p1c_L01.15 old wrong
  -> new right; p1c_L03.25 old wrong -> new right. 3 of the 8 fixed positions are these three.
- Broken: p1c_L02.26 and p2c_L01.17. p2c_L01.17 is an adjudicated NEW:circle-on-stem.
- Wrong in both: p1c_L01.5 [flagged], p1c_L03.16 [flagged], p1c_L02.27, p1c_L06.21, p2c_L02.3, p2c_L02.7.
- Of the 6 flagged-excluded new errors, 3 are NEW: signs (p1c_L02.27, p1c_L06.21, p2c_L01.17). TXE-Q's pre-registered rule
  counts a NEW: sign at a scored position as wrong, and that rule stands. The shapes are readers' and the adjudicator's
  descriptions, with no value attached.
- Full position table: `score/positions.tsv`.

## Pool arithmetic
Eval pool = 10 + 6 + <Spinelli's new flagged-excluded position errors> + 1 = 10 + 6 + **6** + 1 = **23** (Amendment 4: 29
with Spinelli's 12). The lane makes the BENCHMARK-TX.tsv baseline-column and pool change in its own Amendment. This job did
not touch either.

## Deviations and notes
- The adjudicator's resume follows TXE-Q's precedent (one resume, the same subagent). After the resume, one row (p1c_L04.16)
  was still unviewed.
- The adjudicator's self-reported confidence counts disagree with its file (above). The file is used as written.
- The old baseline files (passA_txeq, passB_txeq, passZ_pipeline) were not opened before this job's passes, reconciliation
  and passZ_v4 were committed. passZ_pipeline was first opened by the paired score.

## Commits and sha256 (all before the score unless marked)
| commit | file | sha256 |
|---|---|---|
| a2ac3b7db | benchmark-tx/txeng2/basespin/reader_task_v4.txt | 627dc63878efa2695ae0f1c385639e72a3793cdf402fc9cde52f0c05a2195305 |
| a2ac3b7db | benchmark-tx/txeng2/basespin/adjud_task_v4.txt | 37801624b8ee7b664c7727dbf4c7a1f8a79ed44748e8da7a14f38593974a5dcc |
| (input) | ciphers/spinelli-beinecke-c1515/glyphs/atlas_v4.png | 4ad8c0484ccf65c8ea8b59e326f4d1d64c98b1605bea046c752b5a654e28b67f |
| 7dfe264b3 | benchmark-tx/outputs/spinelli-c1519-confirm/passB_v4.tsv | a813a97301280a8c14794a9d7f5f276e25afe7c40e43dbd9e719c1f6593dacf6 |
| 1aa8aebaa | benchmark-tx/outputs/spinelli-c1519-confirm/passA_v4.tsv | 45f940e84803a8ba8017267d674cae443851f728f1848a80632cae842deec6e1 |
| 0bd4581ae | benchmark-tx/txeng2/basespin/rec/*, adjud_queue.tsv | (in git) |
| 23ba58e3f | benchmark-tx/txeng2/basespin/adjud_out_first.tsv | db4fa448905fe82f6fe1e08a985530067b3cbae87b761313cc97735781a683fa |
| 618f6544f | benchmark-tx/txeng2/basespin/adjud_out.tsv | 10994c25f0a9b26d4bf74a124fe60293ab809d624b225650bffd60db97d8ec4c |
| 618f6544f | benchmark-tx/outputs/spinelli-c1519-confirm/passZ_v4.tsv | a641e2614b7e9931d22d1885d011a70fd7c3aeb1e25160e7b78534afbc756a70 |
| this commit (after the score) | score/*, score_detail.py, RESULTS.md | -- |
