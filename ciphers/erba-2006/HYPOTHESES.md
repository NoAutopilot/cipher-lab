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
| 6 Oct 2026 | R12D-ERBA4 | letter-class (polyphonic), xs = space, word-level dictionary constraint (it21news), anneal | 100 letters / 17 words, 8 | 0.614 (gate 0.60; seeds 0.02-0.88); oracle 0.860; secondary windows 0.659 | score 33.0 vs 10 nulls max 33.4; 10/17 matched | does not move -- weak negative at the control's power (target score in the failed-search band) | PREREG-test4.md / test4_output.txt |
| 14 Oct 2026 | ERBA-SIB | letter-class (polyphonic), xs = space, word-level dictionary constraint (it21news), anneal at 4x budget; + 2013 sibling phrases (press transcription) | 120 letters / 21 words, 8 | every seed >= 0.60: min 0.817, mean 0.898 PASS; oracle 0.898; solver >= true 5/5 | score 38.9 vs 10 nulls max 41.4 (mean 31.7); 14/21 matched | does not move -- control-backed negative for this design at this N (conditional on transcriptions, case folding, xs = space) | PREREG-test4b.md / test4b_output.txt |
| 14 Oct 2026 | ERBA-CASE | letter-class (polyphonic), CASE-SENSITIVE (13 case-kept token types = 13 classes), xs = space, word-level dictionary constraint (it21news), anneal at 4x budget; + 2013 siblings (press transcription) | 120 letters / 21 words, 13 | every seed >= 0.60: seeds 0.900/0.283/0.892/0.833/0.117, min 0.117 FAIL; oracle mean 0.900; solver >= true 3/5 (misses are search) | not run | CONTROL BELOW GATE -- untestable by this instrument at K=13, N=120 at this budget (search shortfall, design identifiable per oracle) | PREREG-test4c.md / test4c_output.txt |
