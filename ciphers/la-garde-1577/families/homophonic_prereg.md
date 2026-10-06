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
