# PREREG-COL26-KEY (account 4, LANE DEFAULT-A4-0437-15, 15 Oct 2026, written 04:5x UTC before any score)

Job: COL26-KEY, `.claude/briefs/runs/2026-10-15-acct4-default-0437-jobs.md`. Script: `siblings/c50_keyrev.py` (its docstring is
the full registration; pushed with this file before its first run). Prior work: `tools/prior_work.py colbert26-lathuillerie-1644
--item-spec 'canvas=50' --step-type align --offline` exit 4 (LEAD 1-own = the COL26-C50 reading step) -> recorded CONTEXT -> exit 0.

- **Folded in:** only the 21 canvas 50 tokens VER-COL50 kept at C (rule 3 per-unit merge: canvas 50 cleared its own word-grain
  control, DA1-COL 21 vs W p95 11, P 0.0000). Canvas 51 (COL26-SIB FAIL) is not merged.
- **What the revision does:** the 21 anchors cut their c50 gloss words (both blind pairings, DA1-COL and DA1-COL2); open codes between
  anchors get a proportional chunk of the remaining letters; modal chunk per code = candidate value. Written to a new file
  `key_f23_c50rev.tsv`; key_f23.tsv, decode.json and every reading are not changed.
- **Counts as a gain only if**, on the held-out word-paired units whose instruments cleared (c3940, c47, c54, c55, c56, c63; c62
  excluded), in BOTH scorings (pass 1 / pass 2 pairings for c3940 and c47): H_after > p95 of the shuffled-pair control (candidate
  values permuted among candidate codes, 10000 draws), P_SP < 0.05, P_W < 0.05 (held-out word-pairing shuffle), hits in >= 2 held-out
  units. Before/after H (key_f23's current values for the same codes vs the candidates) reported as the gain.
- **Stage 0:** shuffled-pair power of the statistic on the held-out units with key_f23 C codes subsampled to the candidate-code
  count; power < 0.5 -> NON-TEST at this N, gate not read.
- **Merge:** PASS -> candidates at grade M in key_f23_c50rev.tsv ("per-code test owed"); no C from a unit gate. FAIL/NON-TEST ->
  candidate column only (grade '-').
