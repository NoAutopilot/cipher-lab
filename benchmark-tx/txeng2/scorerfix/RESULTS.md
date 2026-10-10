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
