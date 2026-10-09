# PREREG-LAG-WC: `wordcode` at the measured marks-kept error, matched control first (LAG-V2, 9 Oct 2026, account 2, LANE FAMILY-A2f)

Written and pushed before any wordcode score at these error levels is computed. Target: `specs/la-garde-1577.json` as rebuilt
by LAG-V2 (v2 carrying LAG-MARKS' 7 sure mark settles; 239 tokens, 48 code^mark types; base codes unchanged).

**Measured error used.** One-reader marks-kept error from `lag_marks.tsv` (LAG-MARKS, passes unchanged by LAG-V2): central
**0.071**, upper **0.125**. The revised v2 against the same settles reads 0.000 central / 0.067 upper (LAG-V2 row in
`lag_marks.tsv`), but v2 is built from those readers and shared misreadings are invisible to it, so the reader figure is the
one injected. WC-LAGARDE2's only wordcode row ran the control at 0.23 (mean 0.321, below gate).

**Runs (in this order, nothing else):**
1. `python3 tools/family_run.py specs/la-garde-1577.json --family wordcode --seeds 3 --measured-error 0.071 --param codes=marked
   --param err=0.071 --gate 0.6 --label "LAG-V2 wordcode err 0.071"` -- control first; family_run.py runs the target only if the
   3-seed control mean >= 0.60 (else CONTROL BELOW GATE, exit 3, target untouched).
2. Bracket, only if run 1's control met the gate and time remains under 80% of the box: the same command at `0.125`
   (control first, same gate). If run 1's control is below the gate, run 2 is not run (a control that fails at the central
   error cannot be rescued by a higher one).

**Read-out (fixed now):**
- Control mean < 0.60 at 0.071: wordcode is **untestable by this tool at N=239 and err 0.071** (not refuted). Since this is
  the second wordcode attempt on this target and the only knob changed is `err`, rule 3's third-attempt clause applies to
  any further attempt: the next one needs a different instrument or new material (pooling), not a third err level.
- Control mean >= 0.60: the target decode family_run.py writes is reported **descriptively only** (its judge line pasted).
  No reading, grade or coverage claim is made from it: a control-backed negative or positive for wordcode needs the
  LAG-GAP/LAG-SYL score-gap gate (target score vs shuffled targets and vs controls at the bracketing errors, power check
  on held-out controls), pre-registered as its own amendment in a separate job.
- Coverage: a wordcode statement covers the target only if a control at >= 0.125 (the upper) also meets the gate.

Recovery statistic, seeds, restarts, corpus: family_run.py defaults for wordcode (seeds 1-3, restarts 8, the spec's fr16
corpora), the same as WC-LAGARDE2 apart from err.
