# RUN2-NXALN -- known-plaintext alignment of fr.16142 c510-516 (atlas clusters) against Dupuy 521 221R-226R

LANE-RUN2 wave 2, account 1 worker, 4 Oct 2026, 03:18-03:4x UTC (`date -u`). Brief: `.claude/briefs/runs/2026-10-04-acct1-run2-wave1.md`
(RUN2-NXALN). Pre-registration `PREREG.md` (commit 2e264d01, 03:21 UTC) and its amendment 1 (commit c5608b9a, 03:27 UTC, design-matched
control) were pushed before the target was run. Intake gate re-run 03:18 UTC: `fr16142-noailles-constantinople-1571: partial (line 1) --
edition/page or full-text-search citation found within 6 lines`, exit 0.

## Verdict
**Atlas instrument: non-test at the atlas's measured noise, not a negative.** The target fails its gate (held-out accuracy 0.363 vs null
p99s 0.365 / 0.369 / 0.366), but the licensing control (design-matched, 40% cluster impurity) fails its own gate on 2 of 3 seeds, so the
pipeline cannot read this design at this noise and the target's failure says nothing about the clear copy or the key. The line-read
instrument (instrument 2) was not run (brief: "if only one instrument fits, do the atlas instrument"; box and cap).

## What was built
`tools/stream_align.py`, reached as `python3 tools/interlinear_align.py stream SYMBOLS TEXT OUT_KEY` (Usage 8; offline test
`tools/tests/test_stream_align.py`, passes in 2 s; SYSTEM.md updated): anchored, progressively grown (+300 symbols per step), banded (+-150)
hard-EM dynamic programming of a whole symbol stream against a separate clear copy, with gaps on both sides (nulls / nomenclator remainders /
split tiles on the cipher side, Dupuy's abridgements / merged tiles on the clear side), and the semi-global held-out accuracy statistic.
`nxaln.py` runs the controls, target, nulls, the gibbs pairs, `key_learned.tsv` and the rule-7 `check`.

## Numbers (results/*.json)
Statistic: train key (argmax letter per cluster, c510-c513) decodes c514-c516; decoded string aligned semi-globally to the clear text after
the train alignment's end; accuracy = identical pairs / held-out symbols. Gate: beat p99 of nulls (a) shuffled key and (c) wrong text
(fr16 Lettres de Catherine de Medicis spans; Dupuy 219-220 is not transcribed), and the max of (b) shuffled-text retraining (40-50 draws).

| run | acc | (a) p99 | (b) max (n) | (c) p99 | gate |
|---|---|---|---|---|---|
| control 41-symbol, impurity 10% | 0.834 | 0.385 | 0.423 (40) | 0.413 | PASS |
| control 41-symbol, 25% | 0.601 | 0.396 | 0.419 (40) | 0.412 | PASS |
| control 41-symbol, 40% | 0.557 | 0.396 | 0.420 (40) | 0.401 | PASS |
| control design (Tomokiyo shape, ~109 symbols), 10% | 0.756 | 0.406 | 0.446 (50) | 0.432 | PASS |
| control design, 25% | 0.667 | 0.415 | 0.449 (50) | 0.415 | PASS |
| **control design, 40%, seed 0 (licensing)** | **0.447** | 0.457 | 0.457 (40) | 0.450 | **FAIL** |
| control design, 40%, seed 1 | 0.537 | 0.433 | 0.452 (50) | 0.426 | PASS |
| control design, 40%, seed 2 | 0.430 | 0.450 | 0.461 (50) | 0.442 | FAIL |
| **target atlas (c510-513 -> c514-516)** | **0.363** | 0.365 (200) | 0.368 (40) | 0.366 (200) | **FAIL (non-test)** |

Target: 6,222 train tiles, 3,682 held-out tiles; clear stream 9,166 letters; the train path ended at letter 6,333, leaving 2,833 letters for
3,682 held-out tiles. The target's training took 7.8 s, so null (b) ran 40 draws with the gate on its maximum (PREREG). Why each null can
differ from the target on this statistic: PREREG.md (a: the key link; b: text order; c: the letter's content); all three moved with the
real key in every passing control (0.56-0.83 against nulls at 0.40-0.46).

Order of work (rule 3): the 41-symbol controls were read before the target was started; the target was started (03:31) while the
design controls were still running, but its output was read only after design 10/25/40% seed 0 had been read (03:32-03:38) and seeds
1-2 (03:43). The design control at 40% fails on the pre-registered seed whatever the target scored.

## Where the 40% comes from, and what it means
RUN2-NXATL's c262 cluster->label purity is 0.593 (about 40% impurity). That figure mixes the clustering's error with the c262 reconciler's
own naming error (readers split 31% on c262), so the atlas's true impurity may be lower; nothing here measures it. The design curve
crosses the gate between 25% (0.667, pass) and 40% (1 of 3 seeds pass): a cleaner sign inventory (the person's sorter pass on the
120 clusters, TRANSCRIPTION.md) that brings impurity to about 25% or below would make the same pipeline a real test.

## Learned key
`key_learned.tsv`: per cluster, the train-alignment value, count, share, the gibbs value, agreement, grade, and the c262 provisional name.
Every value is grade **M** (the gate failed). Comparison with key.tsv (Tomokiyo, published) through the provisional c262 letter labels is
the last line of the file; it is descriptive only and key.tsv was not edited. Results, both consistent with the aligner not having
found the key: stream vs gibbs (`tools/gibbs_align.py`, 156 line-sized pairs cut from the stream path, 60 sweeps, max chunk 2) agree on
13 of 98 clusters gibbs keyed; stream value vs the c262 provisional letter label agrees on 9 of 66 labelled clusters (1 of 15 among the
labels with support >= 3 and purity >= 0.6). The decoded held-out text is not a reading (rule 10).

## Not done
Instrument 2 (line reads c510 -> c516 + c515 L01-L20): not run. The c262 known-answer route through this aligner: not run.
Subagent calls: 0. Requests: none (all inputs on disk).
