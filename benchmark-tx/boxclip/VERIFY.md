# BOXCLIP -- independent verification (12 Oct 2026)

A separate verifier (account-3 parent's workflow wf_197a8cee-e85, read-only) re-implemented the pre-registered method from
PREREG-BOXCLIP.md and recomputed every gate line from the raw label files, signs.tsv and the page images.

- **Verdict: FAIL, confirmed.** Its own re-implementation agrees on 64 of 64 flags and 64 of 64 grown boxes (outside_frac
  within 0.0005). Pooled recall 0.419 (18/43), false alarms 0.381 (8/21), balanced accuracy 0.519 vs the small-box rule
  0.552, exact permutation p 0.4956 pooled and 0.5280 within sorter (the builder's Monte Carlo 0.4970 / 0.5312), median IoU
  gain -0.017. Per page reported honestly (Modena: recall 0.857 but false alarms 0.800; Matignon: nothing flagged).
- **Leakage:** none. The method never reads the owner's boxes or the labels.
- **Labels:** exact. Modena 21 re-cuts / 10 other tiles; Matignon 22 re-cuts / 11 checked-not-re-cut (5 tiles both checked
  and re-cut count as re-cuts).
- **Order:** the pre-registration commit (8479630e1) precedes the results commit; the FROZEN hashes match at every later
  commit. The scorer was imported once before the pre-registration commit (a .pyc 33 s earlier), so it cannot be proven
  that nothing was computed then; on a FAIL on every line this could only have helped a pass.
- **Brief's literal rule:** with neighbour-tile ink counted as outside (the brief's wording, not the builder's extra
  subtraction), it still FAILs on every line (recall 0.488, false alarms 0.381, margin +0.002, p 0.29 / 0.25).
- **Why nothing on Matignon:** its tiles were cut from each sign's own ink, so outside ink is zero on all 33 labelled
  boxes once neighbouring tiles are excluded; the owner's added area lies partly under the next tile (median 33%). The
  neighbour-off reading (11/22 re-cuts vs 0/11 checked) was seen after the verdict and is a lead only; a fresh test would
  need re-registration on labels not yet seen.

Fixed by the parent after verification (same day):
1. The offline test did not guard the edge-contact condition or the "edge-crossing components only" grown box (two
   mutations passed every test). `test_only_touching_components_count` now kills both mutations (checked by applying each
   mutation and re-running the test).
2. The 33 Matignon labels were on disk only. The owner's partial Matignon answers are now committed at
   `ciphers/matignon-mayenne-1586/sorter/owner_db_2026-10-12_partial/` (exported 11-12 Oct by the account-3 parent from the
   live page N4PavgZFLNG9eTc9wwrvXk: 64 moves, 16 checked, 22 recuts), so `run_boxclip.py --check` reproduces on a fresh
   checkout (rule 7).
