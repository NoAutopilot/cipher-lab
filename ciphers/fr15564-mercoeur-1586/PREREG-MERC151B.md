# PREREG-MERC151B (3 Oct 2026, committed before any score below is computed)

Worker MERC151B (account 2, LANE-A2PUSH3). Target: fr15564-mercoeur-1586, f.151 (canvas f164, ark btv1b9064027v).

## 1. Transcription
Second blind read of the six MERC151 crops (`images/f151_L0{1,2,3}_s{1,2}.jpg`), one Opus subagent call, no sight of
`f151_read1.tsv`; `tools/reconcile_passes.py` read1 vs read2; disagreements settled from the crops only. err_2reader =
share of aligned sign positions where the two reads differ (substitution + indel over the longer read), recorded as
agreement, not accuracy (TRANSCRIPTION.md).

## 2. Rule-3 control (control ONLY; the target is not run in this job)
`tools/family_run.py specs/fr15564-mercoeur-1586.json --family homophonic --control-only --seeds 3 --restarts 8
--gate 0.6` on the reconciled read (N, K and span lengths from it), corpus = spec judge language `fr` (tools/data/fr16,
Catherine de Medicis letters, era-matched to 1586), `--param profile=target`. Two rows: noise=0 and noise = err_2reader
rounded up to the next 0.05 (bracketing the measured disagreement, SALV-DIAG clause). Gate 0.6 (the tool's default).
Verdict rule: if the noise-matched control mean >= 0.6, the target run is the named next step; if not, f.151 is
too-short for the homophonic family at this N (rule 5 blocker wording), the clean row stated beside it.

## 3. Lasry key-application test (separate, disk only)
Cells: `lasry_cells_f151.tsv` (this commit) -- each f.151 label -> the set of key LETTERS whose printed glyph the key
file describes with that shape; nomenclator and 'ff' excluded. Tool: `tools/partial_key_test.py --cells
lasry_cells_f151.tsv --draft <reconciled draft> --lang fr --keys 500 --within 10 --width 400 --min-run 4 --seed 342
--key-seed 3420`, then the same with `--shuffle-target 1`. Statistic: order gain (beam 4-gram log10/letter in real
order minus within-run-shuffled order); control: 500 value-permuted keys (sets permuted within frequency bins of 3).
PASS only if the real gain > the permuted-key p95 AND the shuffled-target run does not also pass. A FAIL is
conditional on description-matching of glyphs (no atlas) and on a 2-reader draft; it says nothing about f.151 under a
properly matched key. If fewer than 2 runs of >= 4 keyed signs exist, the test is logged as a non-test (too few runs).
