# BIRAGO-NUM-TOOLS step 2: seg_homophonic on the Nov 1571 numerical system -- pre-registration (3 Oct 2026, 04:40 UTC)

Written and pushed before any seg_homophonic control or target run.

**Hypothesis (design).** A prefix code: the digits 1, 5, 8 always open a two-digit unit (1x, 5x, 8x); 0, 2, 3, 4, 6, 7, 9
are single units; each unit is one letter of a homophonic table. Design string `158:letter`.

**Why this design, from structure only (no solver score used).** Of the 46 plain-digit runs longer than one digit
(`../joint/runs_digits.txt`), only 2 end in 1, 5 or 8, against a within-run digit-shuffle null of mean 13.6 (10,000
draws; p01 7, minimum 3). A digit that never ends a run is a unit opener. Under the pairs-plus-strays reading
(phase.py) 1/5/8 stand second in 148 of 476 pairs, which would end runs about as often as their frequency.

**Input.** `signs.txt`: 48 runs (`phase.runs_from`, letters dropped, marked groups / wavy sign / clear text as breaks),
985 digits, one passage per letter. Under `158:letter` it parses to 734 units, 29 types, 1 parse exception.

**Control first (rule 3).** `seg_homophonic.py control --design 158:letter --units 734 --cipher signs.txt --seeds 5
--restarts 5 --iters 150000`, held-out it16 Italian (every 10th line, model trained on the rest), at noise 0.02 and
0.05. The measured transcription error is 1.4% two-reader disagreement (BIRAGO-NUM; agreement, not accuracy) plus 1
parse exception in 734 units; 0.05 brackets both (rule 3 error-bracketing paragraph). **Gate: mean per-token accuracy
>= 0.6 at noise 0.05.** If the gate is not met: CONTROL BELOW GATE, target not run, logged as non-test.

**Target, only if the gate is met.** `solve --designs 158:letter,15:letter,1589:letter --restarts 6 --nulls 3`
(sign-shuffle nulls) and `158:letter` again with `--null-kind units --nulls 4`, model it16 all. The two comparison
designs are neighbours of the primary, reported, never chosen post hoc. **Reads** only if (a) z against the unit-shuffle
null exceeds the same z on a noise-0.05 control solved the same way, AND (b) `tools/judge_plaintext.py` (it16) PASSes
the decode. Anything else: no reading.

**Different instrument? (CLAUDE.md rule 3 third-attempt clause).** For the pairs-plus-strays hypothesis that
BIRAGO-NUM/-NUM2/-NUM3 tested, seg_homophonic is NOT a new instrument: with every digit a prefix it cuts each run in
pairs from the run start (one fixed phase), strictly weaker than phased_homophonic, and that hypothesis stays retired
for it. It IS a different instrument for a different hypothesis: a deterministic variable-length prefix parse has no
phase to lose, so it does not face the phase-flip tie that retired phased_homophonic. Bourdeau
(cyphersolver `targets/birago`) lists prefix/suffix codes among his exclusions; his test is not reproduced here, and the
run-end statistic above was not part of it as far as his NOTES show.
