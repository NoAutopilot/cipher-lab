# malsburg-hessen-1636 -- hypothesis families

Append-only. Rows below are written by `tools/family_run.py` (CLAUDE.md rule 3: the matched CONTROL number sits beside the TARGET number in every row; a row with gate met = no reports a control that could not read its own design, and the target was not run). Prose sections may be added above this table by workers.

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 26 Sept 2026 05:34 | masc | N=352 K=95 restarts=8 corpus=composed_enhg.txt | 1 | 0.987 (0.980-1.000) | -780.425 | FAIL language: score=-1.472, null_p99=-1.618, real_p05=-0.457, real_median=-0.431, mode=both, N=352 | yes (gate 0.6) | bMAL3 masc vs de16 |
| 26 Sept 2026 05:34 | homophonic | N=352 K=95 restarts=8 corpus=composed_enhg.txt profile=target | 1-3 | 0.392 (0.318-0.511) | not run (CONTROL BELOW GATE) | - | no (gate 0.6) | bMAL3 homophonic profile=target vs de16 (nomenclator K=95) |
| 26 Sept 2026 07:02 | homophonic | N=1000 (projected N, actual target N=352) K=95 restarts=8 corpus=composed_enhg.txt profile=target | 1-3 | 0.928 (0.867-0.964) | not run (control-only) | - | yes | bMALC pooled-N control |
| 26 Sept 2026 07:03 | homophonic | N=2000 (projected N, actual target N=352) K=95 restarts=8 corpus=composed_enhg.txt profile=target | 1-3 | 0.844 (0.710-0.957) | not run (control-only) | - | yes | bMALC pooled-N control |
| 26 Sept 2026 07:03 | homophonic | N=3000 (projected N, actual target N=352) K=95 restarts=8 corpus=composed_enhg.txt profile=target | 1-3 | 0.976 (0.970-0.984) | not run (control-only) | - | yes | bMALC pooled-N control |
| 26 Sept 2026 09:34 | homophonic | N=1828 K=173 restarts=8 corpus=composed_enhg.txt profile=target | 1-3 | 0.637 (0.298-0.881) | not run (control-only) | - | yes | bMALH pooled N=1828 control-only sanity |
| 26 Sept 2026 09:34 | homophonic | N=1828 K=173 restarts=8 corpus=composed_enhg.txt profile=target | 1 | 0.637 (0.298-0.881) | -4769.700 | FAIL language: score=-1.635, null_p99=-1.66, real_p05=-0.435, real_median=-0.423, mode=both, N=1828 | yes (gate 0.6) | bMALH pooled N=1828 |
| 26 Sept 2026 09:35 | homophonic | N=1791 K=144 restarts=8 corpus=composed_enhg.txt profile=target | 1 | 0.699 (0.191-0.961) | -4654.965 | FAIL language: score=-1.628, null_p99=-1.653, real_p05=-0.434, real_median=-0.422, mode=both, N=1791 | yes (gate 0.6) | bMALH pooled N=1828 deduped off-form dropped |
| 26 Sept 2026 09:37 | homophonic | N=1828 K=173 restarts=8 corpus=composed_enhg.txt profile=target | 1 | 0.637 (0.298-0.881) | -4769.700 | FAIL language: score=-1.635, null_p99=-1.66, real_p05=-0.435, real_median=-0.423, mode=both, N=1828 | yes (gate 0.6) | bMALHfull pool N=1828 undeduped rerun |
| 26 Sept 2026 09:37 | homophonic | N=1828 K=173 restarts=8 corpus=composed_enhg.txt profile=target,shuffle_target=1 | 1 | 0.637 (0.298-0.881) | -5225.376 | FAIL language: score=-1.724, null_p99=-1.66, real_p05=-0.435, real_median=-0.423, mode=both, N=1828 | yes (gate 0.6) | bMALH pooled N=1828 shuffle-target floor |
| 26 Sept 2026 10:55 | period-key (HCPortal 519, 4 d Nr. 1219) | code-set overlap of pool vs key's 81-value numeric range, N=1828 K=173 | control: 1000 random 80-code samples from key's own 11-99(non-x10) range | control mean 0.4454 distinct / 0.7757 tokens (p95 0.4451 / 0.7850) | target 0.4451 distinct (77/173) / 0.7834 tokens (1432/1828) | not run (no judge -- key519 decode of ff.3/12 is gibberish, see NOTES.md) | DEGENERATE, not a test (key is exhaustive over its own range; control cannot differ, CLAUDE.md rule 3 bCAS/AX-5799 shape) | bMALK key519 coverage (non-test) + direct decode negative |
