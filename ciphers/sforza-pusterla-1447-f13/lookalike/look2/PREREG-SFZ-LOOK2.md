# PREREG-SFZ-LOOK2 (11 Oct 2026, written 19:2x UTC by date -u, before any re-read)

Worker SFZ-LOOK2 (account 1, Opus), LANE DEFAULT-A1-1840, brief .claude/briefs/runs/2026-10-11-acct1-default-1840-jobs.md.
Same instrument and rules as S8 (SFZ-LOOK, NOTES.md S8), on the next four A-C confusion pairs of f.13:
So/go (7), 8/g (5), h/h- (4), a/ze (3). In the 4-unit key every pair's two members carry different values
(So a / go r, 8 v / g t, h c / h- l, a a / ze s), so each settlement can change a decoded letter.

- Adapter: `python3 lookalike/build.py --look2` (reference = pass D, reader A = pass A, pass B record only). Outputs
  lookalike/look2/{tiles_target,tiles_all,agreement,passC,confusion_f13}.tsv. Targets 19 (So/go 7, 8/g 5, h/h- 4,
  a/ze 3); controls 16 (A = D at conf H; up to 3 per label, seed 7: a 3, g 3, go 3, h 3, h- 3, 8 1; no So or ze tile has
  A = D at H, so those two labels have no control -- stated, not filled from another pair).
- Windows: tools/lookalike_pass.py windows on images/level/ (scratch manifest, s2 at x=1600, as S8), --per 6, shape
  descriptions from pusterla_labels.md; controls interleaved in shuffled order, same prompt, value-blind (no key values).
- One value-blind Sonnet re-read call per montage batch; answers in lookalike/look2/reread_sonnet.tsv.
- Control gate: the re-read gives the A = D label at conf H/M on >= 0.80 of the 16 control tiles; else non-test, no
  label changes. Per-pair control rates are reported beside the blended one (rule 3, unbalanced classes).
- Reconcile: tools/lookalike_pass.py reconcile (2-of-3: a firm H/M re-read matching A or D settles; else UNSETTLED,
  keeps D, goes to focus.tsv). Pass E = pass D with the changes. Residual = unsettled/354 (agreement, not error).
- If any label changes: lattice_decode.py --passE on it16dip and it15; report rank /201, margin over shuffle max,
  judge (FAIL as FAIL). g1p.py --check is re-run only as a no-change confirmation (f.13 is not a key unit).
- No reading is claimed whatever the result; the target stays partial (rule 5).
