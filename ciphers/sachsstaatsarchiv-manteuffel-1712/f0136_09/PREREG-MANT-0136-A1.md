# PREREG-MANT-0136-A1 (MANT-R07, 9 Oct 2026, LANE FAMILY-A2f account 2): amendment to PREREG-MANT-0136.md, gate (a) input widened

Written and committed BEFORE any amended gloss pass is read or any amended score computed. Everything in PREREG-MANT-0136.md stands
except what is stated here.

Why: MANT-0136's worker eye (NOTES "MANT-0136 (9 Oct 2026, 04:17...)", "Worker eye (NOT scored...)") saw faint period gloss letters
under r07 (34..30) and under r08 16 31 13 that both blind gloss passes missed. That eye note is NOT a known answer and is not shown to
any reader.

Input (the only change): gate (a) is scored on spans over r07 (all 19 tokens) and r08 (all 14 tokens; positions 1-3 now inside the
read, positions 4-14 as before). Readers: two new blind Sonnet gloss passes (A1A in crop order, A1B in reversed order) that see only
the crop paths below -- no key, no prior gloss file, no ciphertext.tsv, no worker-eye note, no NOTES. Each reader reports, per crop,
the code numbers it sees in order and the small letter(s) under each code ('-' none, '?' unreadable). Per pass, the worker builds
gloss_A1A.tsv / gloss_A1B.tsv with one span per line (r07, r08): gloss = that reader's letters in code order across the crops of the
line (overlap duplicates removed by the reader's own code positions), '-' and '?' dropped; codes = the reconciled ciphertext.tsv
tokens of the line (r07 1-19, r08 1-14). The worker does NOT settle or edit the gloss letters. A line on which a reader reports no
letters gives no span for that pass (listed).

Crops: tighter, higher-contrast strips cut from the committed f0136_09/crops/f0136_L12.jpg and f0136_L13.jpg (adjacent boxes,
y 2532-2650 and 2650-2779 of 0136.jpg), stitched, autocontrast cutoff 1%, three overlapping horizontal thirds per line, 2.5x
upscale: f0136_09/make_crops_a1.py -> f0136_09/crops_a1/ (committed, manifest.json).

Statistic, alignment, control, seeds and gate: UNCHANGED (gloss_gate.py: S = codes whose key.tsv value matches the next gloss
letters under the DP alignment; control key.tsv values permuted over codes, 1000 draws, seed 8; PASS iff S > p99 AND S >= 0.5 x
keyed codes in spans). Scored per pass: gate_A1A.out, gate_A1B.out. (a)-A1 PASSES only if both PASS. Old numbers (gate_A.out,
gate_B.out: A 9/13 PASS, B 8/13 PASS) are reported beside the new ones, not replaced.

Grades: grade_0136.py --a1 reads gate_A1A/A1B and gloss_A1A/A1B instead of A/B and writes grades_A1.tsv (grades.tsv unchanged);
same rule-4 rules. Gate (b) (judge_gate.out) is NOT re-run: its unglossed token set was fixed by the original spans; under --a1 the
newly glossed r07 tokens are graded by the gloss rules, and the remaining unglossed tokens keep (b)'s original result -- disclosed,
not a new gate. No key.tsv change. Candidate values from a gloss under a code whose key value differs (e.g. 20, 120, 66) go to
HYPOTHESES.md as rule-4 slots only.
