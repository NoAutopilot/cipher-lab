# HARNESS-2 pre-registration (written 29 Sept 2026, 07:2x UTC, before any new number was computed)

Task: DIGEST-1 "Round-2 prompts", prerequisite paragraph. Add to `score.py` (1) the refit null, (2) B's
cross-language check, (3) the c1+c2a <-> c2b fold bar; rerun the self-test; write a second FROZEN line.

## Bar v2 (what `score.py --claim` will test)

A claim is two key files, one fitted on each side of a declared pair, plus the fitting command.
Pairs: `c1c2` (fit c1 -> test c2, fit c2 -> test c1: the frozen pair) or `fold` (fit c1+c2a -> test c2b,
fit c2b -> test c1+c2a). On ONE statistic S of the eleven, in BOTH directions of the pair:

1. frozen conditions unchanged: `beats_all` and `beats_all_strat` (1000 shuffles each), `coverage_test >= 0.50`,
   `read_letters >= 60`;
2. **refit null**: at least 50 refits, each the same fitting command run on the fit text with its sign order
   shuffled BY THE HARNESS (all signs of the fit text permuted, line lengths kept, seed = refit index), each refit
   key scored held-out on the same test text; the key's raw S must be strictly above the refit p99 (order statistic
   ceil(0.99 n) of n refits, which is the refit maximum for n < 100);
3. **cross-language** (the ten language statistics; not applicable to `vocab`, which is not a language claim):
   z_S = (key's S - refit mean) / refit sd; the claimed language's z must exceed the z of the SAME statistic type
   (quad or dict) in each of the other four languages by at least 1.0.

Precomputed refits (`--refit-keys`) are accepted only when the fitter cannot be run by the harness; the output
marks them `refit_source: precomputed` (the shuffle is then the group's, not the harness's).

## Known-answer controls (run first) and kill test

- K1 planted FR-HOMO key (sealed answer), refit null = the harness climber (`selftest_climb.py` method) on the
  shuffled fit text, 50 refits per direction: must PASS bar v2 on fr_quad on both pairs.
- K2 a random permutation of the planted key: must FAIL.
- K3 group B's two order-shuffled refits that cleared beats_all under both frozen nulls on the fold
  (`G-B/refit/refit_c1+c2a_15.tsv` on en_quad, `refit_c1+c2a_34.tsv` on fr_dict; also 15 on es_dict): must FAIL
  in the direction they were fitted (c1+c2a -> c2b) on condition 2 or 3 -- not merely for want of a reverse key.
  Null: B's own fitter (fit_key.py, unchanged method) on shuffled c1+c2a, the 39 sibling refits plus 11 more = 50.
- K4 the climber fitted on NULL (both pairs): must FAIL.
- K5 (reachability, reported, not a kill): the climber fitted on FR-HOMO and FR-HOMO-N15 on both pairs.

**Kill test:** if K1 fails, or any of K2, K3 (in its fitted direction), K4 passes, bar v2 is not frozen: no second
FROZEN line is written and the failure is reported. If K5 shows no fitted key reaches bar v2 even on clean FR-HOMO,
that is reported beside the FROZEN line as a limit of the bar, not hidden.
