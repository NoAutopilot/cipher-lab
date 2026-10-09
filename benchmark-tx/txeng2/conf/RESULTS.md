# TXE2-CONF: calibrated sign-level confidence (PREREG-txeng2-2 X4, 9 Oct 2026)

LANE TX-ENGINEER-2, account 4, Opus 5.5 worker. **Verdict: FAIL (dev, read-free scoring).** The reader's top-3 holds the
truth at 3 of L's 12 dev_tune errors (registered gate >= 0.5), so the confidence is not usable as lattice input; used as
lattice weights anyway (as registered) it fixes 2 and breaks 9 vs L. No eval look; dev only.

**Pass.** One blind Opus 5.5 pass on dev_tune (f.178v L01-12), 3 subagent calls (L01-04, L05-08, L09-12; 12 crops each,
2x LANCZOS), the unchanged `harvest/blind_pass_brief_1572.md` + `conf_block.md` (per-sign top-3 cells with probabilities)
+ `sign_sheet_blind_1572.png`. Readers saw the crops, sheet, brief and block only. Tasks frozen and pushed before any call
(a274a2528); reads, normalised pass and every truth-free decode pushed before any score (387a9d9f1). Conduct and the
disclosed deviations are in `PREREG-notes.md`: (a) the PREREG says "3 calls, pass-A grouping" but no 3-call grouping of
dev_tune exists (pass A split L01-10 / L11-23); the call count was kept, lines split 4/4/4; (b) call 3 (L09-12) said its
probabilities follow a fixed per-grade scheme (H .85/.10/.05, M .60/.30/.10, L .40/.30/.30); calls 1-2 gave graded values
(24, 21, 3 distinct triples per call).
Output: `passX_dev_tune.tsv` (356 signs; X_ 5, ? 2), `benchmark-tx/outputs/birago1572-no87/passX_conf_dev_tune.tsv`.
Harness `run_x4.py` (norm / decode / score; rules in its docstring); numbers in `score.json`.

## (1) Calibration (343 scored dev_tune positions, X aligned to truth by tx_bench.align)

| top-1 p bin | n | accuracy | mean p |
|---|---|---|---|
| 0.0-0.4 | 0 | - | - |
| 0.4-0.6 | 10 | 0.900 | 0.460 |
| 0.6-0.8 | 145 | 0.862 | 0.660 |
| 0.8-1.0 | 188 | 0.989 | 0.879 |

ECE **0.159**; X top-1 accuracy at aligned positions 0.933. The reader is **underconfident** in every bin, and not only on the
fixed-scheme call: per call ECE 0.128 (L01-04), 0.142 (L05-08), 0.203 (L09-12). The probabilities rank signs (0.86 vs 0.99
accuracy below/above 0.8), but L's errors are not where the reader doubts: they are where it is confidently wrong.

**Truth in X's top-3 at L's 12 errors: 3/12 (0.25) -- gate >= 0.5 FAIL.** At 9 of the 12, X's top-3 is a set of look-alikes
that excludes every truth cell (e.g. truth T45|T66|T86 read T76 / T26 / T96 four times; L02:12 T36/T18/T98; L05:9
T64/T13/T38). This matches TXP-AGREE's "all-same-wrong" class: the reader errors and the confusion candidates sit in the same
wrong neighbourhood, so a top-3 widening does not reach the truth. Per-error detail: `score.json` L_err_detail.

## (2) As a DOUBT signal (for X9)

Flag = X's aligned top-1 p < 0.7 (or no X sign): **recall 7/12 (0.583) at 26.2% flagged** (90/343). Above the 15% share the
detector gate allows, so on its own it does not meet X9's bar; offered to TXE2-DOUBT as the `conf` signal (file:
`passX_dev_tune.tsv`, column p1; L positions via run_x4.x_on_L).

## (3) As lattice weights at the two-signal doubt positions (registered arm)

`key_decode_lattice.py from-passes --probs` (new option: the reader's own distribution replaces the H/M/L weight), X aligned to
L's skeleton; candidates at tx_doubt's disagree OR latt positions (41 of 354, all with an X sign), L fixed elsewhere; viterbi
lam 4, beam 64, key_1572_sheet, it16dip. Paired vs L (labels.tsv), 343 common positions:

| arm | fixed | broken | p (two-sided sign) | errors (L 12) | gate |
|---|---|---|---|---|---|
| conf (registered) | 2 | 9 | 0.065 | 19 | **FAIL** (wrong way) |
| conftop1 (X top-1 at the same 41, no LM; reported) | 2 | 8 | 0.109 | 18 | - |
| X top-1, all of dev_tune (not an arm) | 2 | 13 | 0.007 | 23 | - |
| control: 20 value-shuffled keys | mean 1.35 | mean 11.5 | 0/20 pass | | control does not pass (ok) |

X's own top-1 on dev_tune: err_true 0.079 (27/343: wrong 23, inserted 4) vs L's 12 errors -- a single Opus pass with the
probability block is worse than the reconciled baseline, as every single re-pass on this hand has been.

## Reading
Retire "reader-stated confidence as lattice input" for this hand on this evidence (first attempt; rule 3's three-attempt
clause not reached, but the failure is structural: 9/12 of the baseline's errors have no truth cell in the reader's top-3).
The p1 < 0.7 flag is a weak doubt signal (0.58 recall at 26%) and goes to X9 as one candidate signal only.

Cost: 3 Opus vision calls (subagent tokens 114k, 119k, 116k); 0 hosts; cost by the orchestrator's get_session reading.
