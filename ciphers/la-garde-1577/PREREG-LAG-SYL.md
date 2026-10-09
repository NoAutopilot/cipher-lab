# PREREG-LAG-SYL: `syllabary` control at the measured error (9 Oct 2026, account 2, LANE FAMILY-A2d)

Written and pushed before any control or target score of this job is computed. CPU only, no network beyond git.

**Family and input.** `tools/families/syllabary.py` (LANE R8 DSN design: base code = letter, a mark on a consonant base = the
following vowel; control on the spec's row pattern with the CM3 token-level error mix `err`, split del:ins:code
0.465:0.331:0.204; recovery = token accuracy). The family already carries an error parameter (`err`), so no `noise` param is
added. Input: `specs/la-garde-1577.json`'s own ciphertext (the 239 marks-kept code^mark tokens, 27 bases, 48 types, 18.4%
marked), the same input WC-LAGARDE2's 26 Sept row used -- the syllabary design reads the marks, so the marks-stripped
`basecode_cipher.txt` (N=229, no marks) would make it degenerate to homophonic, which LAG-GAP already closed.

**Which measured error.** LAG-ERR (8 Oct) measured pairwise disagreement two ways (`lag_err.tsv`): base code (marks stripped)
0.055 pooled (A-vs-B 0.036, A-vs-L1 0.064), and literal sign (marks kept) 0.183 pooled (A-vs-B 0.107, A-vs-L1 0.219). The
brief names 0.055/0.084, the base-code figures. A syllabary reads code AND mark, so the error on the axis this family reads is
the marks-kept one; 0.055/0.084 understate it (CLAUDE.md rule 3, SALV-DIAG: a control's error must bracket the target's own
measured error on what the design reads). Runs, `tools/family_run.py specs/la-garde-1577.json --family syllabary --seeds 3
--gate 0.6 --control-only --measured-error p --param err=p`, p in:
- 0.055, 0.084 (the brief's levels, base-code measured and its bracket);
- 0.107 (marks-kept, A-vs-B, the lowest marks-kept measured figure) and 0.183 (marks-kept pooled);
- 0 (descriptive upper bound, not a gate).
Corpora: family_run's default from the spec's judge block (fr16, the two Catherine volumes), as WC-LAGARDE2.

**Read-out, fixed now.**
- Control mean below 0.60 at 0.055 (the gentlest gating level) -> syllabary is **untestable by this tool at N=239 even at the
  base-code error**, a fortiori at the marks-kept error; "untested-by-this-tool", not a negative (rule 3). Target not run.
- Control meets 0.60 at 0.055/0.084 but not at 0.107 -> still **not licensed**: the target's marks-kept error is >= 0.107, so a
  target run would sit outside the band the control backs (SALV-DIAG). Target not run; logged as untestable at the measured
  marks-kept error.
- Control meets 0.60 at 0.055, 0.084 AND 0.107 -> stop scoring; write Amendment 1 here fixing the LAG-GAP score-gap design
  (PREREG-LAG-GAP.md: target best score vs 40 matched controls and 40 shuffled targets, PASS iff T > p95(shuffles) and
  T >= p05(controls)) with its power check on held-out controls first, push it, then run. If that does not fit the cap or 80%
  of the box, stop after the amendment and name it as the next step.
- The third-attempt clause (rule 3) applies: WC-LAGARDE2 ran this family at 0.23; this run changes the error band because the
  measurement changed (LAG-ERR), not as a tuning knob. A control below gate here at <= 0.107 retires syllabary-by-this-tool on
  this text until new material (pooling) or a different instrument.
- The target stays `open` (rule 5) whatever the result. No reading is claimed by this job.

## Amendment 1 (written after the control calibration, before any target or gate score)

Control calibration (family_run rows in HYPOTHESES.md, 00:4x UTC): mean recovery 0.861 at err 0.055, 0.863 at 0.084, 0.833 at
0.107 (all gate 0.60 met), 0.264 at 0.183 (not met). Per the read-out above, the third branch applies: the control gates at
0.055, 0.084 and 0.107, so the LAG-GAP score-gap gate is run, power check first in the same batch. Fixed now:

- Script `families/lag_syl.py` (a copy of `lag_gap.py`'s design with the syllabary family on the spec's marks-kept input).
  Solver: syllabary, restarts 8, defaults otherwise (iters 120000, order 3, assign regular, use auto, gap 2).
- **Statistic: solver score per cipher token (score / N of the ciphertext solved).** Changed from LAG-GAP's raw score because
  this family's error mix inserts and deletes tokens, so control N varies (226-243 in the calibration) while the target and
  its shuffles have N=239; a raw log-likelihood would move with N, not with fit.
- Target T: the spec ciphertext, solver seed 1. (a) 40 matched controls: err 0.084 and 0.107, seeds 1-20 each (the 0.055
  level is dropped from (a) because 0.107 is the licensing level fixed above; 0.084 keeps the brief's bracket).
  (b) 40 shuffled targets (family_run --shuffle-target convention: the 239 code^mark tokens permuted over the same 15 message
  lengths; shuffle seed k, solver seed k), k = 1-40.
- **PASS iff T > p95(b) and T >= p05(a).** p95/p05 = ceil(q n)-th order statistic, as lag_gap.py.
- **Power check (decides whether the gate is a test at all):** 10 held-out controls at err 0.107, seeds 101-110, each against
  the p95 of 20 shuffles of its own ciphertext (seeds 1-20) and p05(a). Power PASS iff >= 80% of the held-out controls with
  recovery >= 0.60 pass. Power FAIL -> the gate is a non-test for this family at this N; logged "untested-by-this-gate", no
  gate swap, target result not read either way.
- Read-out: power PASS and target FAIL -> **control-backed negative for syllabary (this design, regular assignment) at N=239
  for transcription error up to 0.107**; NOT a negative over the 0.107-0.183 band, where the control itself fails (0.264), so
  the row stays conditional on the true marks-kept error being <= ~0.11 (pairwise disagreement 0.183 is an upper estimate of
  one reader's error; about half if independent). Power PASS and target PASS -> "worth a verifier" at most: run the spec
  judge on the decode, report it, grade every token S at best, claim no reading in this job, and name a shuffle-decode judge
  check (rule 3, ARM-C1) as the next step. Target stays `open` either way.
- Scores to families/lag_syl.tsv; `--report` re-prints; `--check` re-runs and diffs (rule 7).
