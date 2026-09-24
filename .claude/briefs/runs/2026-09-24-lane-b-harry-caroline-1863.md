LANE B breadth worker: harry-caroline-1863. Sonnet (claude-sonnet-5). Cap $3.
Common rules: `.claude/briefs/runs/2026-09-24-lane-b-common.md` (read it first; it governs).

Spec: specs/harry-caroline-1863.json. Run `cheap_tests_in_order[0]` and its matched control, nothing else. Write both numbers into the spec's `cheap_test_done` (with date, method, cost). Judge any candidate plaintext with `tools/judge_plaintext.py` and paste its output. Cap $3. Report in five lines; do not run test 2; rule 10 wording; a negative's done line carries the target and control numbers side by side.

No host needed. Control: English 71-letter text with the same word-length pattern, same solver, 3 seeds; percent letters right.
