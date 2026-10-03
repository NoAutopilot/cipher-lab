# FT4i pre-registration (account-4, 3 Oct 2026, written ~07:02 UTC, pushed before any real one-edit score)

Instrument: `align/one_edit.py` (docstring is the full definition; not changed after this commit). Different from the
retired strict-consistency instrument (gate_pair.py / f249_diag.py / f213_diag.py): exactly ONE edit is allowed per pair.

- Model: exact coverage of the slip's letters (as already committed in slip_f214r.txt / slip_f250.txt, expansions at I)
  by the passage's groups in order; free groups 1..12 letters; every repeated code one identical chunk at all its
  occurrences; no pins (the ten f.206 C values are not imposed). One edit: W = one group occurrence released
  (0..12 letters: misread digit / one polyvalent use / extra group at length 0) or D = one inserted group of 1..12
  letters (a dropped group). MAXLEN 12 as FT4c/FT4e/FT4h.
- Solver: exact CP-SAT model (ortools 9.15). Sanity before gate, already run (no one-edit score): E0 f216v True (2.1 s),
  f213 False (0.3 s), f249 False (4.2 s), matching FT4c (fits) and the f213/f249 diagnostics (proved infeasible).
  One timing draw of control (g) per pair was run to size the limit (f213 resolved in 25 s, f249 timed out at 30 s).
- Statistic E: 1 if a fit with <= 1 edit exists. Real pair: 60 s limit, 4 workers; timeout counts 0.
- Controls (can differ: E depends on both sides' order): (s) the slip's words shuffled, real passage; (g) the passage's
  group order shuffled, real slip. n 40 each, seed 3, 15 s per draw single-worker, timeouts counted E = 1 (high,
  conservative); the resolved-draw share is printed beside it as descriptive.
- Gate per pair: PASS if E_real = 1 AND each control's E=1 share <= 0.05 (at n 40: at most 2 of 40).
  E_real = 1 with a share above 0.05: NON-INFORMATIVE (one edit is enough to fit wrong pairings too).
  E_real = 0: FAIL for the one-edit model only (the pair needs >= 2 edits); never a negative for the f.206 key.
- On E_real = 1 the script lists every single edit (W at group i / D before group i) that gives a fit (descriptive).
- Key rule: nothing enters or moves in key.tsv this step whatever the result (no pinned key statistic is registered).
- Run order: f213 then f249: `python3 one_edit.py --pair f213`, `python3 one_edit.py --pair f249`. Stop before a run that
  would cross 80 pct of the 40-minute box (box 06:55-07:35 UTC).

## Amendment FT4j (account-4, 3 Oct 2026, ~07:31 UTC by the clock, pushed before any re-run)
Timeout change only: the controls are re-run with `--limit 60` (60 s per draw instead of 15 s); nothing else changes
(same script, n 40, seed 3, same gate and rule). Side effect of the script's own scaling, stated here: the real E0/E
calls get 3 x limit = 180 s and the single-edit enumeration 60 s per edit; both resolved under 36 s at 15 s, so their
results cannot change. Run order f213 then f249, serialized (one run at a time on the 4-CPU container).

## Amendment FT4l (account-4, 3 Oct 2026, ~09:31 UTC by the clock, pushed before any registered draw is re-scored)
Third instrument on these gates; it changes HOW a draw is solved, not the statistic, the draws or the gate.
- Solver: `align/one_edit_seg.py --dec`. (i) An equivalent smaller CP-SAT model: variables only for repeated-code
  occurrences; each run of f free groups is one gap constraint [f - wf + dd, 12(f + dd)]. (ii) E by decomposition: one
  exact subproblem per edit class (wildcard in a free run, drop in a free run, each repeated occurrence released; the
  position inside a free run does not change feasibility), 10 s each, single worker, Pool(4), early exit on the first fit.
  Draw E = 1 if any class fits, 0 if every class is proved infeasible, unresolved if none fits and any class timed out.
- Validation (run before this commit, no registered draw scored): f216v real E = 1 (2 s); f213 real E = 1 (11 s) with
  exactly one of 107 classes fitting, W at group 73 (the second 368), as FT4i/FT4j; 0 timeouts (`align/real_f213_dec_classes.out`).
  Sizing on UNREGISTERED draws (seed 99, f249): two draws that timed out at 60 s under one_edit.py resolved here
  (129 and 132 classes, 0 fits, 0 timeouts, 131 s and 90 s wall). No seed-3 draw was run with this solver before the push.
- Draws: the registered ones (seed 3, n 40, (s) then (g) as one_edit.main()). Every draw of a control being re-scored is
  re-solved (per-draw identities of the old timeouts were not stored). f213 (s) stands as FT4j (0/40, all resolved).
- Gate: unchanged (PREREG-FT4i): per pair PASS iff E_real = 1 AND each control's E=1 share <= 0.05, unresolved draws
  counted E = 1. Share > 0.05 with any RESOLVED fits > 2 of 40: NON-INFORMATIVE in the real sense (one edit fits wrong
  pairings). Share > 0.05 from unresolved draws only: NON-INFORMATIVE (power), and by rule 3 (third instrument) the
  one-edit gate is then logged [retired] for this solver on that pair; next would be new material, not a fourth solver.
- Run order and box: f213 (g) draws 0-19 then 20-39 (foreground, commit and push after each half), then f249 if the box
  allows (s, g, halves). Stop before a half that would cross 80 pct of the 45-min box (09:20-10:05 UTC; line 09:56).
  A pair not completed is reported as not scored, with its draw count, never as a partial gate.
- Key rule: nothing enters or moves in key.tsv this step whatever the result.
