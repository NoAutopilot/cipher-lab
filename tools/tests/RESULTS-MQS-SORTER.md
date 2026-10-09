# RESULTS-MQS-SORTER (9 Oct 2026, MQS-SORTER; gates and rules are in PREREG-MQS-SORTER.md, written first)

## A. `sign_sorter.py --oddness-audit`, Birago no.87 known answer (635 clean tiles -> 622 in 35 piles of >=3; 31 planted per seed; 20 seeds)

Inputs: `python3 tools/tests/oddness_no87_inputs.py DIR`; run `python3 tools/sign_sorter.py --signs DIR/signs.tsv --labels DIR/labels.tsv --pages DIR/pages.json --oddness-audit --plants random|lookalike [--confusion ciphers/nevers-birago-fr3251-1572/harvest/confusion_1572.tsv] [--oddness-variant medoid|knn3]`.

| order | plants | mean recall@10% | seeds above shuffled p95 | seeds recall>=0.6 and above p95 | shuffled mean (null) |
|---|---|---|---|---|---|
| mean (page order) | random | 0.498 | 20/20 | 1/20 | 0.130 |
| mean (page order) | lookalike | 0.282 | 16/20 | 0/20 | 0.127 |
| medoid | random | 0.497 | 20/20 | 1/20 | 0.130 |
| medoid | lookalike | 0.26 | 14/20 | 0/20 | 0.127 |
| knn3 | random | 0.494 | 20/20 | 2/20 | 0.130 |
| knn3 | lookalike | 0.271 | 14/20 | 0/20 | 0.127 |

Gate (PREREG A): random plants recall>=0.6 and above the shuffled p95 in >=18 of 20 seeds. **FAILED for the page order (1/20) and for both variants (1/20, 2/20).**
The order is far above the shuffled order (20/20 seeds above its p95 on random plants; mean recall 0.50 against a null mean 0.13), so it is not noise; but it puts about half, not 0.6+, of planted misfits in the first 10% of a pile, and on look-alike plants (the real error kind) 0.28 (16/20 seeds above p95). Shelf grade `weak`, both numbers kept. Per-seed tables: rerun the command (about 3 s each).

## B. Owner's 4 Oct no.87 sort against BENCHMARK-TX (rule: PREREG B)

`python3 tools/tests/mqs_sorter_score_owner.py`

```json
{
 "tiles_settled": 248,
 "scored_cohort": 208,
 "left_out": {
  "no position map (f.178r)": 31,
  "bad-cut / not-letter / aside": 9,
  "plain sign with no key row (unmapped)": 0
 },
 "owner_new_piles_read_unknown": 27,
 "all": {
  "scored_positions": 200,
  "owner_wrong": 52,
  "owner_err_true": 0.26,
  "owner_ci95": [
   0.204,
   0.325
  ],
  "committed_wrong": 4,
  "committed_err_true": 0.02,
  "committed_ci95": [
   0.008,
   0.05
  ],
  "fixed": 0,
  "broken": 48,
  "sign_test_p": 0.0
 },
 "moved": {
  "scored_positions": 19,
  "owner_wrong": 7,
  "owner_err_true": 0.368,
  "owner_ci95": [
   0.191,
   0.59
  ],
  "committed_wrong": 2,
  "committed_err_true": 0.105,
  "committed_ci95": [
   0.029,
   0.314
  ],
  "fixed": 0,
  "broken": 5,
  "sign_test_p": 0.0625
 },
 "kept": {
  "scored_positions": 181,
  "owner_wrong": 45,
  "owner_err_true": 0.249,
  "owner_ci95": [
   0.191,
   0.316
  ],
  "committed_wrong": 2,
  "committed_err_true": 0.011,
  "committed_ci95": [
   0.003,
   0.039
  ],
  "fixed": 0,
  "broken": 43,
  "sign_test_p": 0.0
 },
 "diagnostic_plain_piles_only": {
  "scored_positions": 176,
  "owner_wrong": 31,
  "owner_err_true": 0.176,
  "owner_ci95": [
   0.127,
   0.239
  ],
  "committed_wrong": 2,
  "committed_err_true": 0.011
 }
}
```

Reading: owner corrections on a machine seed, scored against BENCHMARK-TX (not a blind reader's err_true). 248 settled tiles; 31 f.178r tiles have no position map and 9 are bad-cut/not-letter, leaving 208 mapped, 200 on scored benchmark positions. The registered score is err_true 0.260 (0.204-0.325) for the owner's piles against 0.020 (0.008-0.050) for the committed line reads at the same 200 positions; fixed 0, broken 48 (the 52 owner-wrong include the tiles in owner-made new piles, which the rule reads as unknown). Diagnostic only, not the registered score: leaving the 24 positions in owner-made piles out, 31 of 176 plain-pile positions are wrong (0.176, 0.127-0.239) against 2 of 176 for the committed reads. BIR-ADJ's image adjudication sided with the owner on 98 of 108 disputed tiles (nevers-birago NOTES.md): supporting evidence of a different kind (one instrument, every move graded M). Grade `weak`.
