# BENCHMARK.tsv -- a frozen, family-split benchmark

Written 27 Sept 2026 (BENCH-FREEZE, brief `.claude/briefs/runs/2026-09-27-parent-ytbiz-bench-freeze.md`), on the
owner's decision responding to CODEX-REVIEW-2026-09-27.md section 7: "do not treat 13/13 as an out-of-sample
success rate ... build a frozen benchmark split by correspondence/key family, keeping entire families out of
calibration."

**How to add a case.** Append a row to `BENCHMARK.tsv` (never edit an existing row in place -- a correction is a
new row whose `note` points at the old `case_id`). Give it a `truth` label (`positive`, `wrong-key`,
`wrong-period`, `synthetic`, or `transcription`) and a `split` (`dev` or `eval`) -- and check first that the
row's `family` is not already assigned to the *other* split (`python3 tools/bench_check.py` catches this). An
`eval` row's `ciphertext_path`/`key_path`/`plaintext_path` must point at files that do not change after this
freeze; if a target's transcription or key is corrected later, that correction is still tracked (rule 7), but
this benchmark's own eval row for it is superseded by a new row, not silently updated under the same paths.

**How to score a solver or a control design against it.** Run the solver/design on every `dev` row while
building it (tune, pick thresholds, adjust the control, whatever); only report a headline number computed on
`eval` rows, and never adjust anything after looking at the `eval` result. `python3 tools/bench_check.py` before
scoring (fails if a family leaked across splits, an eval path moved, or a row lacks a truth label).
`python3 tools/bench_score_baseline.py` is the worked example for `tools/key_crossmatch.py`'s own statistic.

## What is in it (26 rows, 20 families)

- **positive** (17 rows): a real repo key applied to its own ciphertext, at grade H (a period key source or
  cryptanalytic result with two audits) or M (print tier: the plaintext is already published elsewhere,
  N0/N1, so this only tests whether the statistic recognises a genuine key-to-text relation, not novelty).
  Numbers (stat, coverage, n_tokens) are copied from `KEY-CROSSMATCH-CAL.tsv`'s own "verified"/"print" tiers or
  `KEY-CROSSMATCH.tsv`'s own-text rows -- not recomputed here, per rule 7 (the source row is named in each
  case's `note`).
- **wrong-key** (4 rows): a real key from a *different* family applied to a ciphertext it was never built for
  (two are the exact pairs `tools/key_crossmatch.py`'s own `NEGATIVE_PAIRS` names; two are its own documented
  false leads, `clair1108-duvergier/key_1696.tsv` on Mercy and on Bowes, kept IN so the benchmark measures the
  gate's known failure mode, not just its easy negatives).
- **wrong-period** (2 rows): a real key from the *same* office, a different folio/version, applied to a
  ciphertext from a different folio of that same office (August of Saxony's key_74 misapplied within its own
  key_53/key_74/key_98 pool) -- the negative CLAUDE.md rule 3 actually asks for ("a control's error level must
  bracket the target's own" applies to design; this is the office-level analogue: same design, same era, wrong
  specific key).
- **synthetic** (2 rows): `tools/family_run.py --control-only` on a placeholder spec sized to a real case's own
  N and K (content is random, per the tool's own control-builder, which only uses N/K/corpus/language) --
  homophonic at Mercy's N=522/K=38 (control mean 0.965, gate 0.6 met) and masc/alphabet-substitution at Saxony's
  N=364/K=20 (control mean 0.435, gate 0.6 NOT met, high seed variance 0.077-0.975). Full rows:
  `BENCHMARK-SYNTH.md`. Nomenclator, syllabary and code-numbers design-class synthetic controls were not run
  this pass (time/cap) -- same tool, next worker, `specs/bench-synth-*.json` is the pattern to copy.
- **transcription** (1 row): the Montholon (fr4715-montholon-1589) L02-L17 image-to-token sample against
  Tomokiyo's own printed dump, with substitution/omission-insertion/segmentation/mark errors recorded
  separately (MONT-4715C2, MONT-CAL, 27 Sept 2026) -- 92.9 pct raw pass-agreement was only 0.396-0.461 in-order
  accuracy against the known answer. An interlinear leaf-pair case (a second, independent transcription
  instrument) was not added this pass; MONT-KEY6's f.24 pass-agreement numbers (15.4 pct raw, no full error-type
  breakdown) are the nearest candidate, noted here for the next worker rather than added as a partial row.

**Split.** `dev` holds 10 families (gramont, nassau, saxony, mercy, vanbeuningen, blathwayt, brienne, luzerne,
este-guise, bowes); `eval` holds 10 (oxenstierna, canada, gunther, szembek, linhares, posthius, morillo,
hessen1567, synthetic, montholon-transcription). No family appears in both (`tools/bench_check.py` enforces
this). A family that shares a key across repo folders (Nassau: lodewijk + jan-van-nassau; Brienne: clair1067 +
fr5160-letellier) is kept whole in one split even though only one folder's row is included here, since a
future row for the sibling folder must land in the same split.

Why `dev` skews toward the strongest verified pairs and `eval` toward the shorter/weaker ones: the calibration
brief (`KEY-CROSSMATCH.md`, XMATCH-CAL) built its gate from *all 18* verified pairs at once, so there was no
real out-of-sample split to draw on -- this freeze had to choose which known pairs go in each split from
scratch. `eval` deliberately includes Gunther (a real verified pair the current gate is already known to miss,
stat 3.276 vs gate 3.292) and two below-length-floor pairs (Linhares N=26, Posthius N=69) precisely because
those are the cases most likely to move if the gate or statistic ever changes -- an eval split of only "easy"
pairs would not test anything.

## Baseline (U4): `tools/key_crossmatch.py`'s existing gate, scored out of sample

```
$ python3 tools/bench_score_baseline.py
== dev ==
  positives: 11 (admitted 11) -> recall 1.000 [0.741,1.000] (Wilson 95%)
  negatives: 4 (admitted/FP 2)
  precision (TP/(TP+FP)): 0.846 [0.578,0.957]  TP=11 FP=2 FN=0 TN=2
  wrong-key: 2 cases, 2 admitted (false positive) -> FP rate 1.000 [0.342,1.000]
  wrong-period: 2 cases, 0 admitted (false positive) -> FP rate 0.000 [0.000,0.658]
== eval ==
  positives: 6 (admitted 3) -> recall 0.500 [0.188,0.812] (Wilson 95%)
  negatives: 2 (admitted/FP 0)
  precision (TP/(TP+FP)): 1.000 [0.438,1.000]  TP=3 FP=0 FN=3 TN=2
  wrong-key: 2 cases, 0 admitted (false positive) -> FP rate 0.000 [0.000,0.658]
  wrong-period: 0 cases in this split
```

**Reading it.** Dev recall is 1.000 because dev was built from the same 13-in-stratum verified pairs the gate
was fitted on (KEY-CROSSMATCH.md XMATCH-CAL) -- this number is exactly the in-sample figure the review warned
against, reproduced here on purpose so the eval number beside it is legible as the answer to the review's
question. Eval recall is 0.500 (3 of 6): the gate correctly admits Oxenstierna, Canada and Szembek, but misses
Gunther (already documented, stat just under the gate), Linhares and Posthius (both far too short for this
statistic to have power). Eval precision is 1.000 on only 2 negative cases (a wide interval, [0.438,1.000] --
not a strong claim). Dev's own precision (0.846) is dragged down by the two known Duvergier false leads, which
were kept in deliberately rather than dropped as "already adjudicated," so the benchmark's numbers show the
gate's real false-positive behaviour on a documented hard case, not just its easy ones.

**What this does and does not answer.** It answers the review's literal ask: 13/13 is not an out-of-sample
rate, and the real one (eval recall 0.500, wide interval on only 6 eval positives) is much weaker than 13/13
suggests, once whole families are held out and the shorter/weaker pairs are not filtered out of eval. It does
*not* yet answer "run the entire candidate-selection pipeline on negatives, including retries and picking the
best score" (review section 7, second paragraph) -- this benchmark scores the gate at its one fixed threshold,
not a search-with-retries process, and the 260 shuffled-null draws behind the 3.292 threshold itself (not
re-run here) are a separate, larger control already on file in `KEY-CROSSMATCH-CAL.tsv`.

## Adding a design-class synthetic control

```
python3 tools/family_run.py specs/bench-synth-<class>.json --family <family> --control-only --seeds 3 --restarts 2 \
        --out BENCHMARK-SYNTH.md --label "BENCH-FREEZE U2 design-class control (<class>, N=<n> K=<k>)"
```

Build `specs/bench-synth-<class>.json` with a `ciphertext` field containing a random token stream of the target
case's own N and K (content does not matter -- `family_run.py`'s control builder only reads N, K, the named
corpus and language) and a `judge` block naming a real corpus under `tools/data/`. `--out BENCHMARK-SYNTH.md`
keeps the row out of any real target's own `HYPOTHESES.md`.
