# PREREG-ERR-SIM -- error-matched synthetic control for ink 63 (RESEARCH.md experiment 1)

Written 17 Oct 2026 01:2x UTC (date -u), before any scored synthetic run. Worker ERR-SIM (account 4), brief
`.claude/briefs/runs/2026-10-17-acct4-research-director-2.md` JOB ERR-SIM. Disk only. Nothing here edits key.tsv,
reading_piece63.tsv, AUDIT.md or any committed reading.

## AD recount (step 2, run before this file was written; not a scored run)
`tools/depth_stats.py --tokens tx/err_sim/tokens63.tsv --key key.tsv --cipher-class 'len<=3' --shuffle classes --corpus
tools/data/fr16 --seeds 8100-8119` (tokens63.tsv = reading_piece63.tsv split one row per token by tx/err_sim/tokens63.py;
AUDIT 7 names no class, len<=3 takes every key code and no brace label). Output tx/err_sim/depth63/summary.json:
- R (fr16) 2.116, V 18, 32 distinct cipher codes, H_design 133.4 bits, H_lib 6458.1 bits (every M/U token of the item charged).
- Tool's item-wide AD = 1.5 x 6591.5 / 2.116 = **4671.6** letters (R 3.4: 2908.0). This charges all 3472 M/U liberties of the whole
  15,762-token item against one clause, so no all-H run can reach it on any item of this size (12,290 H tokens in all): as a bar for an
  all-H run it cannot fail differently from the target (rule 3, non-test shape). Reported, not used as the gate.
- **Governing bar for an all-H run (no liberty inside it): AD_design = 1.5 x H_design / R = 1.5 x 133.4 / 2.116 = 94.6 letters**
  (DV-MERCY2's convention, corpus R; liberties are zero inside an all-H run). Sensitivity at R 3.4: **58.9**. The old convention
  (about 42) is reported beside.
- Target ink 63 now: primary_run (all-H) 40; m-through run 277.

## Method (fixed now)
- Plaintext: tx/dec67_norm.txt + tx/dec70_norm.txt + tx/dec_f105v..f108v_merged.txt (markup stripped: {del:..} dropped, {add:..}
  kept), folded a-z, v->u, j->i; concatenated in that order and cut (or cycled from the start if short) to 15,762 letters, split into
  ink 63's own line lengths and pages.
- Encipher with key.tsv (all 34 rows): each letter -> a code whose meaning is that letter, chosen with probability proportional to the
  code's count in reading_piece63.tsv (+1). A letter with no key code (f, p, k, w, x, y) -> an out-of-key sign (decodes U), as on the
  target.
- Readers: per-pass confusion P(read|true) learnt by `tools/key_decode_lattice.py learn-confusion --per-pass` from f.102r dev2 passes
  A and B against its truth (tx/vivlat/in_dev_A/B.tsv, benchmark-tx/vivonne1573-f102r-dev2.truth.tsv), key signs as cells. Scaling
  to an injected error e: each true sign t is misread with probability min(0.9, e x err_t / mean err), mean over the synthetic's own
  sign frequencies (keeps which signs are hard), the substitute drawn from t's off-diagonal row. Readers A and B independent.
- Reconcile as committed (tx/viv63_decode.py): agree -> that sign; differ and the pair in viv63_decode.RULES -> the rule's sign,
  unflagged; otherwise pass A's sign, flagged. Grade: sign not in key -> U; key grade M or flagged -> M; else H.
- Levels e = 0.05, 0.10, 0.14, 0.19, 0.23; seeds 1-5 each.
- Measures per run: longest all-H run in letters over the whole stream (depth_stats' primary_run, checked to give 40 on the target's
  own tokens); the longest all-H run whose letters are all correct; V_strict (tx/viv54L_stretch.py --strict vocabulary, longest
  stretch per page, max over pages).

## Controls (run first)
- C0: e = 0.0, real key, 5 seeds. Must give longest all-H run >= 94.6 in >= 3 of 5 seeds; else the pipeline is broken (or the key's
  M rows alone cap the run below AD), the job logs NON-TEST and the sweep is not run.
- C1: e = 0.0, value-shuffled key (meanings permuted over codes, grades kept) used to decode the real-key encipherment, 5 seeds. Must
  give no run of correct letters >= 94.6 (the all-H grade run is key-grade-driven and is reported, not gated; the correct-letter run
  and V_strict can differ from the target's).

## Decision
- (a) If at e = 0.14 and every level above it, fewer than 3 of 5 seeds give an all-H run >= 94.6: every ink-63 negative is a
  non-test; the crossover error (largest level where >= 3 of 5 seeds still give a run >= 94.6) becomes the transcription target; decode
  side work on ink 63 stops until a known leaf reads below it.
- (b) If >= 3 of 5 seeds give a run >= 94.6 at each of 0.14, 0.19 and 0.23: ink 63's failure (run 40) is informative and the next
  wave is key-structure (nomenclator or code groups beside the letter key, nulls, an Oct 1573 variant table).
- Mixed (passes at 0.14, fails above): reported as (a) for the measured 0.19-0.23 and (b) at 0.14; the crossover is named and the
  parent decides. The same table at the R 3.4 bar (58.9) is reported as sensitivity, not as the gate.
- Crossover reported either way.
