# R2-1 ORDER-DOSE: result (29 Sept 2026, DEB-SWARM2-R2-1, for the orchestrator)

Pre-registration: `PREREG.md`, committed f2c2160a before any real score. Scripts: `r21.py` (texts, mixed noise,
calibration, real score), `run_calib.sh` (regenerates the 12 `calib_*.jsonl`, 40 pairs x 6 designs each), `analyze.py`
(writes `result.json`). Instrument: `swarm/G-D/dcore.py` unchanged. Public copies only; CPU only; no key fitted or
scored, nothing read. Rule 10 throughout.

## Numbers (pair score; real = median of 5 seeds x 400 shuffles; "as low" = control pairs scoring <= real, of 40)

| text | N | gate: bal. acc. at decision noise | threshold | real | call | language designs as low as real (decision noise) | NULL-IID as low |
|---|---|---|---|---|---|---|---|
| a (c3, c4) | 107 + 263 | **0.85** at 15 pct (0.805 at 10, 0.782 at 20) | 4.9 | 2.84 | NULL by threshold | FR 10, EN 2, PT 7, LA 8, FR-SYLL 2 | 31 |
| b (c1, c2) folded | 125 + 643 | **0.938** at 20 pct (0.968 at 15, 0.863 at 25) | 5.5 | 2.56 | NULL | FR 1, EN 0, PT 0, LA 0, SYLL 0 | 34 |
| c (c1, c2) strokes dropped | 117 + 619 | **0.958** at 20 pct (0.97 at 15, 0.895 at 25) | 5.1 | 0.27 | NULL | FR 1, others 0 | 25 |
| raw (D's reading) | 125 + 643 | **0.955** at 20 pct (0.95 at 15, 0.91 at 25) | 5.6 | 0.96 | NULL | PT 1, others 0 | 27 |

c2-alone score (secondary): b 1.07 vs threshold 3.2 (bal. 0.94), at most 1 of 40 per design as low; c 0.37 vs 1.1
(bal. 0.89), at most 1 of 40; raw 0.66 vs 4.1 (0.915), at most 2 of 40. c4-alone (a's second member): 0.06 vs 1.5
(bal. 0.835), 0-6 of 40 per design as low. Full per-noise tables: `result.json`.

## Kill test, read against PREREG.md

- **Indel noise (the condition DIGEST-1 section 1 left open):** measured. With a quarter of the errors as
  insertions/deletions, D's battery still separates language from NULL-IID on the c1/c2 shape at 0.91-0.955 over 15-25
  pct noise, and the real c2 stays at 0-2 of 40 per design. D's margin survives the real error mix.
- **b and c (folds; strokes dropped):** both gated, both NULL with at most 1 of 40 language pairs as low. Neither
  declared folding nor removing the stroke classes brings out order in c2.
- **a (c3+c4):** the instrument passes its gate (0.85 at the decision noise), and the real text is under its threshold,
  but it fails the pre-registered "at most 5 of 40 per design" clause: 10 of 40 FR-HOMO, 7 PT-HOMO and 8 LA-HOMO pairs
  score as low as the real pair. The real score sits at about the 78th percentile of NULL-IID (31 of 40 below it).
  At N 370 the battery has too little margin to call c3+c4 null the way it calls c2.

**Kill test: NOT met** (by the letter of PREREG.md, because arm a is not NULL-clean). What does hold: on c2, the
no-order result is not an artefact of the replacement-only noise model, of the PCT/X splits, or of the stroke-class
boxes. On the cleaner verse pages the test is weaker, and that result is ambiguous, not a signal. Letter/syllable solving on c2
still has no order to work with. The dose-response question (does the order come back when the noise drops?) stays
open for c3+c4 because they are short, not because they show order.

## What drives a's 2.84 (diagnostic, not gated)

Median feature z over the 5 real seeds: bigram types seen twice or more are above shuffle on both pages (c3 +1.93, c4
+2.09); adjacent MI is at or below shuffle (c3 -0.28, c4 -1.05); the held-out transfer between c3 and c4 is at zero
(+0.27, -0.45; language controls at 15 pct have a median around +0.9 to +1.2); c4 has **more** doubled adjacent signs than its
shuffles (+1.93; language controls go the other way, about -0.7 to -0.9). Recurring pairs without transfer or MI fit
verse repetition (refrains, the couplet-end matches of H5) as well as language. Worth one line for R2-3/R2-4, which
test the verse layout directly.

## Next step named

A dose-response reading of c3+c4 needs either more clean verse-page signs (none on file) or a lower-noise c2 (R2-2);
this battery at N 370 cannot separate FR/PT/LA homophonic letters from iid writing tightly enough to decide.
