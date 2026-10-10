# TOOL-2RATE: tx_bench two-rate decomposition under --exclude-flagged (TXE2-2RATE, 10 Oct 2026)

Worker TXE2-2RATE (account 4, Opus) for LANE TX-ENGINEER-2. PREREG benchmark-tx/PREREG-txeng2-16.md section TOOL-2RATE;
brief row TXE2-2RATE in .claude/briefs/runs/2026-10-10-account4-txe2-round16.md. Run 00:12-00:2x UTC 10 Oct 2026 by date -u.

## Diff summary (commit 9298c281532b15b4604ccc8f6ee7810e87c29e17)
- `tools/tx_bench.py`: `score_item` also counts `read` (the output's sign count on the covered truth lines). Under
  `--exclude-flagged` the flagged-excluded line now ends with
  `| position errors P/U = r | insertions I / read R = r` (P = wrong + deleted at unflagged positions, U = unflagged
  scored positions; I = all line insertions, R = signs read), and `--json` adds `position_errors`, `position_rate`,
  `inserted`, `read` and `insertion_rate` inside `flagged_excluded`. No existing number, field or line prefix changed;
  without `--exclude-flagged` the output is untouched. Documented in the module docstring ("Two-rate decomposition").
- `tools/tests/test_tx_bench.py`: new `test_two_rate`. Fixture: 20 positions, 10 unflagged, 1 wrong at an unflagged
  position and 2 insertions. It reads err_true 0.300 (3/10), position rate 0.100 (1/10) and insertions 2 / read 22 = 0.091.
  As-measured stays 0.150 (3/20), and the plain run carries no new text. Also fixed a failure that was already on main:
  `test_repo_bench_parses` rejected the `confirm`/`confirm2` splits that BENCHMARK-TX.tsv already carries (it failed on
  origin/main before this change). The assertion now also accepts splits starting with `confirm`. No data file was touched.
- `tools/data/tool_shelf.tsv`: row `tx_bench.py --exclude-flagged` (option, controlled-only).
- `SYSTEM.md`: the same row in the 3c shelf table, below `tx_bench.py`. `python3 tools/system_map_check.py`:
  `system_map_check: ok -- all 202 names present in SYSTEM.md`. (`tool_shelf.py --check` exits 1 here and on origin/main
  alike, for rows other than this one: families/columnar_homophonic.py missing, two stale iiif_lines.py option rows.
  I did not fix them because they are outside this brief.)

## Test output (test_output.txt)
```
tx_bench: the output covers no benchmark line   (stderr of an existing negative case in test_scoring)
ok
rc=0
```
The whole file passes: test_scoring, test_label_map, test_wilson, test_repo_bench_parses, test_exclude_flagged and test_two_rate.

## Tool check on S2 (tx_bench_S2_2rate.txt)
This run used exactly the arguments of s2score/tx_bench_S2.txt: passZ_S2b, passA_S2, passB_S2, passA, passB and committed
under benchmark-tx/outputs/vivonne1573-f103r-confirm2/, `--bench BENCHMARK-TX.tsv --item vivonne1573-f103r-confirm2
--exclude-flagged --paired committed.tsv`. Before the run, every input and the truth file matched s2score/SHA256SUMS.prescore
(7/7 OK).
Assertion: once the appended ` | position errors ...` suffix is stripped, the output is byte-identical to
s2score/tx_bench_S2.txt (`diff` empty). So every err_true, as measured and flagged excluded, every Wilson interval and
every paired count equals the S2 file by construction. Nothing was re-scored for a figure, and the S2 look count stays 1.

| output | flagged excluded | position errors / unflagged | insertions / signs read |
|---|---|---|---|
| passZ_S2b | 0.150 (75/500) | 54/500 = 0.108 | 21 / 1,907 = 0.011 |
| passA_S2 | 0.148 (74/500) | 56/500 = 0.112 | 18 / 1,890 = 0.009 |
| passB_S2 | 0.154 (77/500) | 57/500 = 0.114 | 20 / 1,900 = 0.011 |
| passA (builder) | 0.048 (24/500) | 24/500 = 0.048 | 0 / 1,968 = 0.000 |
| passB (builder) | 0.074 (37/500) | 34/500 = 0.068 | 3 / 1,998 = 0.002 |
| committed | 0.032 (16/500) | 16/500 = 0.032 | 0 / 2,033 = 0.000 |

For passZ_S2b, 54 + 21 = 75 = the flagged-excluded numerator. The decomposition equals Amendment 9 (15)'s hand figures
(54/500 = 0.108; 21 insertions / 1,907 read = 0.011).

## Hashes (sha256)
- tools/tx_bench.py 19640dae856f7779cd301a4539db8a4ab6c28e1d20793002403f4ff418f62434
- tools/tests/test_tx_bench.py 110f2f7bcef989e39cbff6e659bf1691f31734acd6802186804541e21283e579
- tools/data/tool_shelf.tsv 05bc34108c3109b1a35fb7cc52d4df2b564211eec85778fd472577dd65649a23
- SYSTEM.md 69215b12c39c5b983266a4b6f83ab8a3c8101418ae4b80289b4a664ada2e59a5
- benchmark-tx/txeng2/2rate/tx_bench_S2_2rate.txt 9262e257178156b460363c5571daa802ed6cd45ad0e497bf12fc5d7a31569b67
- benchmark-tx/txeng2/s2score/tx_bench_S2.txt (unchanged) 3bb42b60ae090db6ad46a8436b73a81075142a7cc7c335693d75a80c52f4290b

No *.truth.tsv, BENCHMARK-TX.tsv or pass file was edited.

Openings of eval truth: 1 (tool check)

Verdict: measured: tool option added; S2 decomposition passZ_S2b flagged-excluded 0.150 = position errors 54/500 = 0.108 + insertions 21 / 1,907 read = 0.011 (Amendment 9 (15) reproduced; every err_true identical to s2score by construction; S2 look count stays 1).
