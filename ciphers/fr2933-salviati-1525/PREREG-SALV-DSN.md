# PREREG-SALV-DSN (11 Oct 2026, written before any run; worker SALV-DSN, account 1, LANE DEFAULT-A1-1840)

Job: `.claude/briefs/runs/2026-10-11-acct1-default-1840-jobs.md` "### SALV-DSN". The retry rung NEAR-RUNGS named:
DSN irregular syllabary (`tools/family_run.py --family syllabary --param assign=irregular`) at 96 restarts on the
SALV-F56V split (spec `specs/fr2933-salviati-1525.json`, N=2939, K=253, 324 runs; dry-run 11 Oct 19:5x UTC).

## Attempt count (rule 3, third-attempt clause)
DSN irregular on this target, same tool, same design: (1) LANE R8 DSN, 25 Sept, err 0.05, restarts 6 (control 0.177/0.242/0.229)
and 24 (per-seed rows 0.242/0.783/0.852; target FAIL on the gated seeds); (2) bSALI, 26 Sept, err 0.064, restarts 24
(control 0.125/0.553/0.722, mean 0.467, CONTROL BELOW GATE). This run changes the restart count (24 -> 96) on a split that
differs from bSALI's by 7 tokens / 2 types. **It is the third attempt of the same family whose main change is the restart
count.** Pre-registered consequence: if the control misses the gate here, the family is logged "untested-by-this-tool
(family_run.py syllabary, assign=irregular) at this N", not refuted, and no further restart/seed tuning is proposed.

## Error level (rule 3, SALV-DIAG lesson)
Measured error of the text the spec is built from: **6.4% per sign** (bSALC pass-C model estimate; the SALV-F56V split
changed 7 boxes and was not re-measured, so 6.4% stands; NEAR-RUNGS notes f.56r's disputed boxes are one-reader settled, so
6.4% is an estimate, not a measurement). The 14.6% figure is the raw atlas pass A/B disagreement before pass C.
- Gated run: control at err=0.064 (`--measured-error 0.064`), 3 seeds, 96 restarts; target (seed 1) runs only if
  family_run.py's own gate passes (control mean >= 0.6). If not: CONTROL BELOW GATE, stop, no bracket runs.
- Bracket runs (only if the gated control passes; control-only, same settings): err=0.10 and err=0.146.
- Interpretation of a target FAIL: control-backed negative **only up to the highest err level whose control mean clears
  0.6**; at any err level where the control misses, the target result is a non-test at that error. If the control clears at
  0.064 but not at 0.146, the result reads "control-backed at the 6.4% estimate; non-test if the true error is near the
  pre-pass-C 14.6%".
- Target judge: the spec's own judge block (it16), as family_run.py runs it; a PASS would be reported as a judge PASS only
  ("worth a verifier"), never as a reading. Shuffle-target check (CLAUDE.md rule 3, ARM-C1) run only if the judge PASSes.

## Not done
No tuning of any other parameter; no second target seed; no new transcription. Target stays `partial`/open per rule 5.
