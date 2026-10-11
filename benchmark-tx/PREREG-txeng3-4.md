# PREREG TXE3-4 CALIB (account 3, worker session_01U7rBmn7MS5LJn9JMzfoFgP, 11 Oct 2026 05:5x UTC by date -u; pushed BEFORE any score)

One of ten TXE3 transcription experiments the account-3 parent launched on 11 Oct 2026. Cap USD 15, box 2 h (05:47-07:47 UTC,
80% line 07:23). No new model passes, no network, no subagent reads: committed outputs and committed truth only. Never scores a
frozen confirm item (spinelli-c1519-confirm, vivonne1573-f103r-confirm2, -confirm2-w): their on-file figures may be QUOTED from
RESULTS files as a spot check, labelled "from file, not rescored". Never edits a *.truth.tsv or BENCHMARK-TX.tsv. Oracle pages
(benchmark-tx/txeng2/oracle1/) are not opened. Scripts and outputs in benchmark-tx/txeng3/4/.

## Question
Most unread letters carry only a two-reader disagreement (err_2reader: Florence c.127 0.17, Birago 1571 f.36/f.47 0.33,
Debosnys 0.28, Birago 1572 f.144r 0.24, f.168 0.13, f.117r 0.134). Agreement is not accuracy (LESSONS.md "Look-alike pass").
Does err_2reader predict err_true across the benchmark leaves well enough to put an err_true RANGE on an unread letter?

## Hypothesis
H1: across benchmark leaves, err_true (single pass, and the reconciliation) rises with err_2reader of the same pass pair;
the ratio err_true / err_2reader has a usable spread (10th-90th percentile of per-leaf ratios within a factor of about 3).
H0: the pairing carries no information beyond its mean (the shuffled-label control reproduces the observed association).

## Data (fixed before any score; every pair is two blind passes already on disk)
Primary set, ONE pair per leaf (the folder's passA/passB), reconciliation named where one exists that is not the truth source:
| leaf (item) | split | readers | pair | reconciliation |
|---|---|---|---|---|
| birago1572-no87 | eval | Sonnet | passA, passB | passC |
| birago1572-f152r | eval | Opus | passA, passB | passZ_pipeline |
| bir1591-f23r-gloss | eval | Opus | passA, passB | passZ_pipeline |
| gunther8246-p2 | eval | Opus | passA, passB | passZ_pipeline |
| ceppo-f36v-gloss (16 signs) | dev | Sonnet | passA, passB | passD (=recon) |
| ceppo-f21v-S | dev | Sonnet | passA, passB | none (passC is the truth source, scores 0 by construction) |
| ceppo-f87-S | dev | Sonnet | passA, passB | none (same) |
| dint-f128-print | dev | Sonnet | passA, passB | passX21_sonnet_reconcile |
| dint-f98v-gloss | dev | Opus | passA, passB | passZ_pipeline |
| dint-f113-gloss | dev | Opus | passA, passB | passZ_pipeline |
| dint-f89-gloss | dev | Opus | passA, passB | passZ_pipeline |
| luzerne108a-p1 (digits) | dev | Sonnet | passA, passB | passZ_pipeline (= passB byte for byte) |
| vivonne1573-f102r-dev2 | dev | Sonnet | passA, passB | none independent (committed is the alignment reference) |
Secondary pairs (same leaves, further independent pairs; enter the all-pairs analysis with a per-leaf cluster bootstrap, never
the primary fit): no.87 passX21_opus_r1/r2 (+ passX21_opus_reconcile, 12 dev_tune lines); f36v passX21b_sonnet_A/B,
passX21b_opus_r1/r2 (+ reconciles); f87 passX21_opus_r1/r2 (+ reconcile); dint-f128 passX21_opus_r1/r2, passX21b_opus_r1/r2
(+ reconciles); vivonne f102r passA_sv/B_sv (+passZ_sv), passA_tl/B_tl (+passZ_tl), passA_dv1/B_dv1 (+passZ_dv1, from the
dev folder, scored on the dev2 truth). Duplicate files (same signs) found by fingerprint are counted once: X21/X21b sonnet A/B
on f87 and dint-f128 ARE the folder passes; vivonne dev and dev2 share passA/passB.
Truth variants (-kp, -kp2, -jk, vivonne -dev) are the same leaf under another mask: sensitivity rows only, never extra points.
Hands: Birago 1572 clerk (no.87, f152r); Dinteville office (f128, f98v, f113, f89); Dinteville 1591 (bir1591); Ceppo-Nevers
(f36v, f21v, f87); Vivonne clerk; Oranje secretary (gunther); La Luzerne (digits).

## Statistics (per pair, all by script, benchmark-tx/txeng3/4/calib.py, importing tools/tx_bench.py and tools/reconcile_passes.py)
- err_2reader = 1 - (agreeing columns / alignment columns) of the two passes over the truth item's lines, Needleman-Wunsch as
  tools/reconcile_passes.py nw (the convention behind every figure on file). Also err_2reader on scored truth positions only
  (both passes aligned to the reference; disagree = different aligned sign), as a secondary.
- err_true of each pass and of the reconciliation: tools/tx_bench.score_item, 0.75-indel alignment (the project's err_true),
  as measured AND flagged-excluded (drop_flagged), Wilson 95% on each; standard SER beside.
- hidden error: on scored positions, share of a pass's errors at which the other pass reads the SAME (wrong) sign
  (hidden_A, hidden_B), and share of the reconciliation's errors at which the two passes agreed (hidden_recon).
- ratio r = err_true / err_2reader per pair, for single pass (mean of A and B) and for the reconciliation.

## Endpoint and fit
Primary endpoint: the association between err_2reader (x) and err_true (y; single-pass mean, and reconciliation where one
exists) over the 13 primary leaves, as Spearman rho and the through-origin ratio fit y = k x (k = median per-leaf ratio;
least-squares k beside), with 1,000-resample bootstraps (a) over LINES within each leaf (recompute x and y per leaf, refit) and
(b) over LEAVES (cluster bootstrap: the spread a new hand faces). Per-leaf ratios, per-hand and per-reader-model (Sonnet vs
Opus) spread are reported in full (rule 3 fold-count lesson). An intercept model y = c + d x is fitted beside; the form used
for the unread-letter table is chosen on DEV leaves only by leave-one-leaf-out MAE, then the 4 EVAL leaves are predicted from
the dev-only fit and reported against their true err_true (tune on dev, report on eval). After that report, the all-leaves
fit is the one tabulated for unread letters, labelled as such.

## Control (CLAUDE.md rule 3) and proof it can vary
Shuffled-label control: permute the err_2reader values across leaves (1,000 permutations), breaking the pairing between a
leaf's pass pair and its own truth, and recompute Spearman rho and the LOO MAE each time. The statistic (rho, LOO MAE) depends
on which x is paired with which y, so the permuted value differs from the observed one by construction unless the y values
are all equal (they are not: 0.01-0.45 on file); the control CAN collapse to rho about 0, and can also fail to collapse if
the observed association is itself noise. Reported: observed rho, permutation p (share of permutations with rho >= observed),
and the LOO MAE of the ratio predictor against the constant-mean predictor (the null predictor that uses no x).

## Gate (declared)
The fit "holds" and the estimator goes into tools/tx_bench.py as --estimate-from-2reader only if ALL of:
1. permutation p < 0.05 for Spearman rho (single-pass endpoint) on the 13 primary leaves;
2. LOO MAE of the ratio predictor < LOO MAE of the constant-mean predictor on the primary leaves;
3. at least 3 of the 4 eval leaves' true err_true lie inside the dev-only fit's leaf-bootstrap 95% band;
4. the 10th-90th percentile per-leaf ratio spread is within a factor of 3 (else the fit may be reported but the tool option
   prints only the full min-max range and says "range only, N leaves").
If any of 1-3 fails: a null, logged in RESULTS.md ("err_2reader does not license an err_true estimate at this N / these
hands"), no tool option, and the unread-letter table is still delivered as the min-max band of per-leaf ratios with the
statement that it is not a calibrated estimate.

## Deliverables
benchmark-tx/txeng3/4/RESULTS.md: per-pair table (err_2reader, err_true A/B/recon as measured and flagged-excluded with
Wilson 95%, hidden shares, ratios), the fit with both bootstraps, the control, the dev->eval report, the unread-letter table
(err_true range implied by each letter's err_2reader on file) and the err_2reader a letter needs to imply err_true <= 0.05;
three plain sentences for the owner; next step with cost. calib_pairs.tsv (every pair), calib_leaves.tsv (primary leaves).
If the gate passes: tx_bench.py --estimate-from-2reader X [--calib TSV] reading tools/data/tx_2reader_calib.tsv, with an
offline test in tools/tests/test_tx_bench.py and a tool_shelf.tsv / SYSTEM.md row.

## Stop rule
Stop before any unit that would cross 80% of the cap (USD 12) or box (07:23 UTC). Units: PREREG (this file); calib.py +
first full run (~15 min); bootstraps and control (~10 min CPU); RESULTS.md; tool option + test (only on gate pass); LEDGER
row + ROOM done. No follow-ups.
