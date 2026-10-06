# erba-2006 -- hypothesis families

Append-only. CLAUDE.md rule 3: the matched CONTROL number sits beside the TARGET number in every row. Rows so far are written
by the cheap-test scripts under `specs/cheap-tests/erba-2006/`, not by `tools/family_run.py` (no polyphonic letter-class family
exists there yet).

| date | by | hypothesis / design | N, K | control (mean, gate) | target | verdict | prereg / output |
|---|---|---|---|---|---|---|---|
| 6 Oct 2026 | R12D-ERBA | xs = word space, token = letter (word-length profile, it19) | 114, 9 | power 95.0% (gate 80%) | p=0.0039 | PASS (not specific: fi, ro also p<0.05 post hoc) | PREREG-test2.md / test2_output.txt |
| 6 Oct 2026 | R12D-ERBA | xs = word space, token = syllable (it19) | 114, 9 | power 100% | p=0.481 | FAIL, control-backed | PREREG-test2.md / test2_output.txt |
| 6 Oct 2026 | R12D-ERBA3 | xs = word space, token = letter, era rerun on it21news | 114, 9 | power 89.5% | p=0.0032 | PASS (era caveat does not move it) | PREREG-test3.md / test2_output_it21news.txt |
| 6 Oct 2026 | R12D-ERBA3 | V1 letter-class (polyphonic), xs = space, bigram anneal | 100, 8 | 0.232 (gate 0.60); oracle 0.736 | not run | CONTROL BELOW GATE -- untestable by this method at this N | PREREG-test3.md / test3_output.txt |
| 6 Oct 2026 | R12D-ERBA3 | V2 letter-class (polyphonic), xs = class, bigram anneal | 114, 9 | 0.139 (gate 0.60); oracle 0.742 | not run | CONTROL BELOW GATE -- untestable by this method at this N | PREREG-test3.md / test3_output.txt |
