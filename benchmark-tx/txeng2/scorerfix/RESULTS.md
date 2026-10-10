# TOOL-SCORER-FIX: tools/tx_bench.py corrected (TXE2-SCORERFIX, 10 Oct 2026)

Worker TXE2-SCORERFIX (account 4, Opus) for LANE TX-ENGINEER-2 incarnation 3. PREREG benchmark-tx/PREREG-txeng2-17.md
section TOOL-SCORER-FIX; brief row TXE2-SCORERFIX in .claude/briefs/runs/2026-10-10-account4-txe2-round17.md; source
research/SO-TX-TRANSCRIPTION-2026-10-10.md ("Reproduced scorer behavior", "Reproduction snippet"). Run 00:37-00:4x UTC
10 Oct 2026 by date -u. Disk only, no network requests beyond git.

**Corrected audit: HELD pending PREREG-18 SCAN-103** (the PREREG-17 order change of 00:3x UTC, and the lane's message to this
worker at 00:36 UTC). No S2 or DV1b output was scored with the fixed scorer, no truth was opened by this job beyond the
`--legacy` regression test (which reproduces figures already on file, byte for byte, and prints nothing new), and no reader or
crop was run. The audit is a separate short job; `run_audit.sh` (below) is ready for it.

## Diff summary (tools/tx_bench.py, built on TOOL-2RATE's 00:18 change, which is kept)
The default is the corrected scorer; `--legacy` runs the pre-fix CLI unchanged (`_main_legacy`, the 00:18 code with only the
calls pinned to `missing='skip', abstain=False` and the position-level `paired_positions`).
1. **Fixed manifest.** An item is selected as before (the output touches one of its lines); then every truth line is scored.
   A missing line's scored positions count as deleted (confusion `<line missing>`, reported as "lines missing M (K signs counted
   deleted)"). An output or --paired base line id not in a selected item's truth fails validation, exit 2.
   `--coverage-diagnostic` keeps the old partial coverage under its own printed label.
2. **Paired** runs per mask on the SAME rows as the rate (as measured; flagged excluded = `drop_flagged` under
   --exclude-flagged). The headline is per-line unit-cost edit totals (S+D+I) paired by line: lines improved / worsened / tied,
   exact sign test. The sign-level position McNemar (fixed/broken) is printed beside it.
3. Therefore **an insertion repair counts** (review case: base A X B, output A B, truth A B gives lines improved 1; positions 0/0).
4. **--exclude-flagged = truth-verifier flags only.** Reader abstentions (UNKNOWN, NONE, a trailing `?`) never match, so they
   are wrong in the full-output measure. `accepted-token error` and `coverage` are printed on their own line.
5. **Standard SER** = (S+D+I)/N under unit-cost Levenshtein is printed beside err_true from the 0.75-indel alignment. N is the
   mask's scored positions on complete reference lines; excluded positions align but are not charged. When several --paired
   outputs are ordered differently by the two measures, a `ranking sensitivity` line names the pairs.
6. **--strict**: exact ref_sign match (visual identity), printed beside the value-compatible truth-set score.
7. **No Wilson interval** on any new-mode rate (all carry insertions). `--ci`: a 1,000-resample line-level bootstrap of standard
   SER (seed 20261010), and under --paired of the SER difference output - base, conditional on the item's lines.
8. Per-item reporting is unchanged. A **macro mean** (unweighted over items) is printed when several items are scored.
9. **--legacy** reproduces every figure on file to the digit (test_fix9).

Side effect for archived scripts: `tx_bench.score_item` now defaults to `missing='delete', abstain=True`, and `tx_bench.paired`
returns the old position keys plus line keys (with missing lines and abstentions charged). `position_errors` and `align`
defaults are unchanged (reconcile_passes.py, tx_weighted_vote.py unaffected). A script under benchmark-tx/txeng2/ that
re-derives an old figure through `score_item` or `paired` should pass `missing='skip', abstain=False` / use
`paired_positions`, or run the CLI with `--legacy`.

## Tests (tools/tests/test_tx_bench.py; written first)
The review's three asserts, inverted to the fixed behaviour, plus one test per item (test_fix1..9):
- On the pre-fix code (sha256 19640dae856f7779cd301a4539db8a4ab6c28e1d20793002403f4ff418f62434), all 10 new tests **FAIL**
  (`tests_old_code.txt`). test_fix9 fails only because `--legacy` did not exist yet.
- On the fixed code, the whole file **PASSES 16/16** (`tests_new_code.txt`; `python3 tools/tests/test_tx_bench.py` prints `ok`).
- The pre-existing tests whose assertions are on the old text format or the Wilson interval (test_scoring's interval,
  test_exclude_flagged's and test_two_rate's text lines) now run with `--legacy`. test_two_rate also asserts the 2RATE
  decomposition in the corrected scorer's flagged-excluded line.
- test_fix9: `--legacy` on the S2 arguments (six outputs, --item vivonne1573-f103r-confirm2 --exclude-flagged --paired
  committed.tsv) and on the DV1b arguments (three outputs, --item vivonne1573-f102r-dev, same switches). With the 2RATE
  suffix stripped, the output equals benchmark-tx/txeng2/s2score/tx_bench_S2.txt and viv102base/tx_bench_out.txt byte for byte.
- `python3 tools/system_map_check.py`: ok (202 names). `tools/tool_shelf.py --check`: no tx_bench row flagged. Its remaining
  complaints (families/columnar_homophonic.py, two iiif_lines option rows) were there before this job.
- `tools/file_shrink_guard.py` on the four touched files: ok.

## Corrected-audit inputs, prepared, not scored
`run_audit.sh [S2TRUTH_ITEM]` does one run per item and mask set: the six S2 outputs vs committed, plain and
--exclude-flagged, with --strict; the three DV1b passes against the WITHDRAWN dev truth (vs its committed) and against dev2 (vs
dev2's committed). It first checks the input hashes. Checked at 00:4x UTC: s2score/SHA256SUMS.prescore 7/7 OK (six outputs +
the confirm2 truth file, hash only), and the viv102base SHA256SUMS_pass[ZAB] lines for passZ/A/B_dv1 3/3 OK.

## Commits and hashes (sha256)
- 6896cf0e7: the fix, tests, shelf + SYSTEM rows, test output files
  - tools/tx_bench.py 239ba8e0c423f22f4e5a8c8fc23beef12e81e92d96b09400837a2404d0c94b3c
  - tools/tests/test_tx_bench.py 994406e86da552b2d9f11f697d9f61914458c125e20aba0ce113bad567106996
  - tools/data/tool_shelf.tsv 506ab6f6bc55e83ee36e5fdca8d50c2d7d0591a830546c9b1132315164b32cd2 (row `tx_bench.py --coverage-diagnostic`)
  - SYSTEM.md b11a33c528936e67cb0a812c5a959cd37e02e4963d4d8263a95cd67ae7530fcb (same row)
- 752f2c90c: run_audit.sh (S2 prescore path corrected before any run)

Openings of eval truth: 0 (the corrected audit is held; the --legacy regression test reproduces figures on file)

Verdict: measured: scorer corrected (review faults 10/10 FAIL old, 16/16 PASS new, --legacy byte-identical to both score files
on record); corrected audit S2 HELD pending PREREG-18 SCAN-103 / DV1b HELD with it (the lane's order).

## Corrected audit (CA-S2; run by LANE TX-ENGINEER-2 incarnation 4, session_01GukpgU1yBAfju3zg6g8ayG, 01:12:46 UTC 10 Oct 2026 by date -u; PREREG-txeng2-19 CA-S2 / PREREG-txeng2-20; one run of run_audit.sh on the EXISTING truths)
Inputs verified first: s2score/SHA256SUMS.prescore 7/7 OK (sha_check_S2.txt), viv102base passZ/A/B_dv1 3/3 OK (sha_check_DV1b.txt).
Scorer tools/tx_bench.py at 6896cf0e7. No reader, no crop, no truth file opened by eye. **A corrected audit of the one S2 look
(22:22:57 UTC 9 Oct) and of DV1b, never a second look: eval looks stay 0, S2 looks stay 1.** Openings: 1 (confirm2) + 1 (dev2).
SCAN-103 reported NOT BEST at 01:0x (registered 6655, fair margin 0.0267; best 6500, 0.0357): this run is the scorer-correction
half of the decision rule on the truth of record; the re-anchor half (a NEW truth at 6500, one re-score) is RE103 (PREREG-20,
WORK-QUEUE TX-RE103), reported beside when it lands.

### S2 (vivonne1573-f103r-confirm2, the existing truth; S2_flagged.txt, S2_plain.txt)
| output | mask | figure of record (err_true, 0.75-indel) | standard SER (S+D+I)/N, unit cost | S / D / I | position / insertion (F48) | strict (= agreement with the committed reader's sign, see note) | line-level paired vs committed: improved / worsened / tied, p; edits base -> output | position McNemar fixed / broken |
|---|---|---|---|---|---|---|---|---|
| passZ_S2b | flagged-excluded, 500 | **0.150 (75/500)** reproduced | **0.134 (67/500)** | 37 / 19 / 11 | 54/500 = 0.108; 21/1,907 = 0.011 | 0.130 (65/500) | 0 / 23 / 13, p < 0.0001; 16 -> 67 | 1 / 39 |
| passZ_S2b | as measured, 1,068 | **0.296 (316/1068)** reproduced | **0.288 (308/1068)** | 243 / 54 / 11 | -- | 0.127 (136/1068) | 1 / 29 / 6, p < 0.0001; 236 -> 308 | 7 / 66 |
| passA_S2 | flagged-excluded | 0.148 (74/500) | 0.130 (65/500) | 36 / 22 / 7 | 56/500 = 0.112; 18/1,890 = 0.009 | 0.132 | 0 / 24 / 12; 16 -> 65 | -- |
| passB_S2 | flagged-excluded | 0.154 (77/500) | 0.138 (69/500) | 39 / 20 / 10 | 57/500 = 0.114; 20/1,900 = 0.011 | 0.134 | 0 / 24 / 12; 16 -> 69 | -- |
| passA_S2 / passB_S2 | as measured | 0.292 / 0.302 | 0.284 / 0.295 | 237/59/7 ; 248/57/10 | -- | 0.127 / 0.143 | 1/29/6 ; 1/28/7 | 7/65 ; 9/76 |
| builder passA / passB (N5-VIVK) | flagged-excluded | 0.048 / 0.074 | 0.048 / 0.072 | 16/8/0 ; 28/7/1 | 0.048 + 0; 0.068 + 0.002 | 0.016 / 0.050 | 0/6/30 p 0.031 ; 0/13/23 p 0.0002 | -- |
| builder passA / passB | as measured | 0.232 / 0.246 | 0.232 / 0.246 | 231/17/0 ; 251/11/1 | -- | 0.016 / 0.046 | 0/8/28 p 0.008 ; 0/17/19 | 0/-- ; 2/-- |
| committed | flagged-excluded / as measured | 0.032 (16/500) / 0.221 (236/1068) | 0.032 / 0.221 | 16/0/0 ; 236/0/0 | -- | 0.000 / 0.000 (by construction) | tied 36 | -- |
Lines missing: 0 for every file (the missing-line fault of the review did not touch S2: every truth line is covered). Reader
abstentions: 0 (accepted-token error = position errors over covered positions: passZ_S2b 33/479 = 0.069 flagged-excluded,
239/1,012 = 0.236 as measured; coverage 0.958 / 0.948, the uncovered positions being the deletions). No ranking-sensitivity line
was printed: the 0.75-indel alignment and unit-cost SER order the six files the same way under both masks.

What moved and why. (1) The figures of record (0.150 / 0.296) reproduce to the digit under the corrected scorer's err_true; the
standard unit-cost SER sits below them (0.134 / 0.288) because the unit-cost alignment pairs 11 of the 21 inserted tokens with
substitutions (I 11, S 37 against the 0.75-indel path's inserted 21, wrong 33): a scoring-convention difference of 8 edits on 500,
not a reading difference. (2) The paired test is now on the rate's own population and at the line level: against the committed
stream the pipeline worsens 23 of 36 lines and improves none under the flagged-excluded mask (edits 16 -> 67) -- the rule-3
cannot-differ shape made visible (the committed reading is the stream the truth was aligned to), so the paired line draws
nothing about the pipeline, as the S2 line already said; the position McNemar beside reads 1 fixed / 39 broken on the 500
(the old paired() reported 7 / 66 on 1,068 -- that cell was the as-measured population, F55). (3) `--strict` on this item is NOT a
visual-ID score: confirm2's ref_sign is the committed reader's sign (its own value error 0.032 / 0.221), so strict = agreement
with that reader (0.130 / 0.127), lower than the value-level figure because the fresh readers often agree with the committed
reader where both differ from the clerk's letter; it is reported for completeness and is not a figure of record (F53: a frozen
visual atlas, not a reader's labels, is the visual reference). (4) Nothing here moves the S2 sentence: the frozen pipeline reads
this hand at 0.150 on the 500 unflagged positions and 0.296 on all 1,068, value-level, under the corrected scorer as under the
old; both above 5%.

### DV1b (f.102r passes against dev2, the truth of record, and against the WITHDRAWN dev truth; DV1b_*.txt)
| output | truth | mask | err_true of record | standard SER | S / D / I | position / insertion | strict |
|---|---|---|---|---|---|---|---|
| passZ_dv1 | dev2 | flagged-excluded, 679 | **0.124 (84/679)** reproduced | **0.118 (80/679)** | 35 / 9 / 36 | 43/679 = 0.063; 41/1,827 = 0.022 | 0.124 |
| passA_dv1 / passB_dv1 | dev2 | flagged-excluded | 0.143 / 0.096 | 0.141 / 0.087 | 53/13/30 ; 24/8/27 | 0.096 + 0.018 ; 0.046 + 0.019 | 0.138 / 0.094 |
| passZ_dv1 / A / B | dev2 | as measured, 1,234 | 0.276 / 0.287 / 0.259 | 0.273 / 0.287 / 0.255 | 275/26/36 ; 292/32/30 ; 261/26/27 | -- | 0.143 / 0.167 / 0.119 |
| passZ_dv1 / A / B | dev (WITHDRAWN) | flagged-excluded, 403 | 0.199 / 0.208 / 0.161 (superseded figures) | 0.186 / 0.206 / 0.144 | 33/6/36 ; 46/7/30 ; 26/5/27 | -- | -- |
Lines missing 0 everywhere; against dev2's committed every pass worsens 24-26 lines and improves none (the same cannot-differ
shape); pass B stays the best single pass on this leaf under every measure (0.096 / 0.087).
