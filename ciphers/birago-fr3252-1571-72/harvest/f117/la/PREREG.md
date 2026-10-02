# NEVBIR-117C pre-registration (2 Oct 2026, written before the third reader runs and before any decode)

- Third reader: one value-blind Opus subagent context per half-leaf (L01-L05, L06-L10), prompts f117c_prompt_a.md /
  f117c_prompt_b.md cut from `tools/lookalike_pass.py packet` (130 tiles: 66 two-reader splits + 64 top-confusion-pair
  agreements; candidate sheet f117c_candidates.png, ids only). passC = recon_f117.tsv (the unsettled two-reader merge,
  not the one-eye settle), so the earlier one-eye settlement does not orient the reader.
- Rule (fixed): `tools/lookalike_pass.py reconcile` 2-of-3 -- a firm (H/M, not SPLIT) re-read matching reader A or B
  settles the tile with that label; anything else stays UNSETTLED with the passC label and goes to focus.tsv.
  Unsettled '?' tiles are then filled from recon_f117_final.tsv (the one-eye settle) for the decode only, and counted.
- Test: run_tests.sh at ERR = 0.25 (the TWO-READER error, unchanged; the 2-of-3 residual is never used as the power
  error, LESSONS.md "Look-alike pass"), same maps (printed, T42m, clerkvar) plus T88q; report rank/z/power side by side
  with the NEVBIR-3252-B table.
