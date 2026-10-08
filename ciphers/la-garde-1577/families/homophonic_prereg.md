# R15-LAGHOM pre-registration: `homophonic` through tools/family_run.py (6 Oct 2026, account 2, LANE-RUN15-account-2)

Written and pushed before any scored run (CLAUDE.md rule 3).

- Cipher: `families/basecode_cipher.txt` (A2-LAG3 base codes, marks stripped, MARK dropped), N=229, K=26, `--tokens space`.
- Spec `specs/la-garde-1577.json`; corpus = the spec's own fr16 judge corpora (two Catherine de Medicis Lettres volumes,
  as A2-LAG3); family `homophonic`, `--param profile=target` (control matches the target's sign-count profile).
- Restarts 8; control seeds 1-3 (`--seeds 3 --seed 1`); gate: control mean recovery >= 0.60 (the tool's default, as every
  prior row on this target). `--measured-error 0.23` on every run.
- Run A (scored, gating): `--param noise=0.23`, control first; target only if gate met (tool enforces, exit 3 otherwise).
  If gated: the same command with `--shuffle-target 1` beside it, and both decodes judged by tools/judge_plaintext.py
  (family_run.py runs the spec's judge). A target judge PASS counts only if the shuffled decode FAILs (ARM-C1).
- Run B (curve, not gating): `--param noise=0.10 --control-only`, same seeds. Marked non-test by the tool (below the
  measured error); reported for the curve only.
- If run A's control mean < 0.60: CONTROL BELOW GATE -> logged "untestable by this family at this N/error", stop.
  No reading is claimed from any statistic; a target decode with a judge PASS would still need a verifier.

## Amendment 1 (8 Oct 2026, 22:4x UTC, LAG-HOM, account 2, LANE FAMILY-A2c) -- written and pushed before any scored run

Reason: LAG-ERR (8 Oct 2026, `lag_err.tsv`) measured the marks-stripped base-code pass-to-pass disagreement, the reduction
`basecode_cipher.txt` is built with, at **0.055 pooled (95% Wilson 0.036-0.084)**; the 0.23 above was the marks-kept figure.
The error level changes; nothing else does. Cipher, N=229, K=26, `--tokens space`, spec corpora, family `homophonic`,
`--param profile=target`, restarts 8, seeds 1-3, **gate 0.60 on the control mean (unchanged)**.

- Run C (scored, gating): `--param noise=0.055 --measured-error 0.055`, control first; target only if the gate is met
  (tool enforces, exit 3 otherwise). If gated: the same command with `--shuffle-target 1` beside it; both decodes judged by the
  spec's judge. A target judge PASS counts only if the shuffled decode FAILs (ARM-C1).
- Run D (upper bracket, rule 3 SALV-DIAG): the same command at `--param noise=0.084 --measured-error 0.084`. If D's control
  mean < 0.60, the family is a non-test at the upper CI bound and any run C target result is stated as conditional on the
  true error being near 0.055, not across the interval.
- Interpretation fixed in advance: gate met at C and D, target judge FAIL with the shuffled decode also FAIL = a
  control-backed negative for `homophonic` (K=26, profile=target) at N=229 on the base codes, conditional on the transcription
  (rule 2) and on the dropped free `[mark]` tokens (LAG-ERR: about 2-3% uncertain). A target PASS with shuffled FAIL goes to
  the lane for a separate verifier; no reading is claimed by this job. Control below gate at C = untestable by this family at
  this N and error (third-attempt clause: the homophonic/masc ladder closes for this instrument).

## Amendment 2 (8 Oct 2026, 22:4x UTC, LAG-HOM) -- descriptive judge-power check, written before it is computed

Runs C, D and the shuffled run are done (rows in HYPOTHESES.md, 22:40-22:42 UTC): both controls gated (0.699, 0.667), target
judge FAIL -1.208, shuffled decode FAIL -1.254, real_p05 -0.96. The gate above is control *recovery*; the target verdict is the
*judge*. A judge FAIL licenses a negative only if the same judge PASSes the solver's own control decodes at the recovery the
gate accepts (rule 3: the control must be able to read where the target does not, on the same statistic). Check, no new gate,
nothing in Amendment 1 changed: `families/lag_hom_judgepower.py` re-creates the noise-0.055 and noise-0.084 control decodes
for seeds 1-3 (same `make_control`/`solve` calls and seeds as family_run.py) plus seeds 4-9 at 0.055 for more points, and
scores each decode with the same spec judge. Read-out fixed now:
- judge PASS on most (>= half) control decodes with recovery >= 0.60 -> the target FAIL is a control-backed negative for this
  family at N=229 on the base codes (conditional on the transcription, rule 2).
- judge PASS on fewer than half of them -> the judge cannot see a decode at the gated recovery; the target FAIL is
  "judge cannot decide at this N", not a negative, and the gap says so.
