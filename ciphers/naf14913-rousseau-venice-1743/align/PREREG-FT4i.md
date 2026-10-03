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
