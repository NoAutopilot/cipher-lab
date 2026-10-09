# TXE-O: the doubt detector -- read-free signals that FIND a line read's wrong signs, for the sorter (9 Oct 2026)

LANE TX-ENGINEER, account 4, Opus 5.5; brief `.claude/briefs/runs/2026-10-09-account4-txe-o.md`; ideas M22, M14 (+ DOUBT).
Tool `tools/tx_doubt.py` (signals / measure / list), offline test `tools/tests/test_tx_doubt.py` (ok). **0 vision calls,
0 hosts.** Signal tables committed before any truth was opened: commit 3db7f2912 (`dev_tune_signals.tsv`,
`eval_heldout_signals.tsv`, the eval plain lattice `passL_lattice_eval_heldout_lam4.tsv` by `run_latt.py`, truth-free:
no learnt matrix). Truth opened only through `tools/tx_bench.py position_errors`, after that push.

**Registered gate:** recall >= 0.7 of L's wrong positions at <= 15% flagged on dev_tune, AND the same combination (chosen on
dev) recall >= 0.6 on eval_heldout read-free. **Verdict: FAIL** -- best dev combination at <= 15% is `disagree+latt`, recall
0.429 (6/14) at 10.5% flagged; on eval_heldout read-free it holds 0.600 (9/15) at 6.1%. The eval half passes, the dev half
does not. Eval here is read-free (no reader, no new read): it is not an eval look and the lane's look count stays 0.

## Signals (all truth-blind; box <-> position by `tx_compare.py map`'s committed box_pos.tsv)
show = TXE-A's rule (`tx_compare.show_decision`, now a shared function); disagree = A/B agreement status != agree
(`tx_compare.merged_conf(field='status')`); bandcut = tx_tile_gate band 'cut' on any box of the position; thin = lowest
erosion-share tercile of the page (tx_tile_gate tiles table, `tx_taxonomy.tercile_classes`); contrast = tx_contrast_sweep
uncertain; stab = TXE-J jitter stability < 0.6 (f178v only: f179r L01-03 have no table, 91 eval positions read 0);
freq (M22) = the sign's page count > expected + 2 binomial sd, expected = page letter-sign total x P(letter, it16dip
unigrams) / homophones in key_1572_sheet.tsv -- it flags 17 page/sign cells (f178v T19 T33 T42 T45 T53 T60 T92 T96 T98;
not T76), because homophones are not used equally, so it is broad (36-47% of positions); latt (M14) = plain lattice lam 4
(TXE-E inputs) chooses a sign other than L's; pair = L's sign in PREREG C's look-alike pair list (`tx_pair_reread.PAIRS`).
Note: M14 as registered in TX-IDEAS is a confidence-gated *fix*; this job measures only its read-free disagreement as a
*doubt* signal, as the brief asks.

## Per signal (recall of wrong positions / flagged share)
| signal | dev vs L (14 wrong / 343) | dev vs pass A (23) | eval vs L (15 / 376) | eval vs pass A (18) | dev share | eval share |
|---|---|---|---|---|---|---|
| show | 11/14 0.786 | 19/23 0.826 | 14/15 0.933 | 17/18 0.944 | 0.501 | 0.402 |
| disagree | 2/14 0.143 | 10/23 0.435 | 6/15 0.400 | 9/18 0.500 | 0.090 | 0.053 |
| bandcut | 5/14 0.357 | 5/23 0.217 | 5/15 0.333 | 6/18 0.333 | 0.172 | 0.168 |
| thin | 5/14 0.357 | 10/23 0.435 | 8/15 0.533 | 11/18 0.611 | 0.230 | 0.380 |
| contrast | 5/14 0.357 | 8/23 0.348 | 3/15 0.200 | 4/18 0.222 | 0.210 | 0.184 |
| stab | 1/14 0.071 | 1/23 0.043 | 1/15 0.067 | 2/18 0.111 | 0.052 | 0.027 |
| freq (M22) | 6/14 0.429 | 7/23 0.304 | 7/15 0.467 | 7/18 0.389 | 0.356 | 0.468 |
| latt (M14) | 5/14 0.357 | 12/23 0.522 | 6/15 0.400 | 7/18 0.389 | 0.055 | 0.019 |
| pair | 11/14 0.786 | 11/23 0.478 | 12/15 0.800 | 13/18 0.722 | 0.446 | 0.471 |
| n_signals >= 2 | 13/14 0.929 | 22/23 0.957 | 15/15 1.000 | 18/18 1.000 | 0.636 | 0.644 |
| n_signals >= 3 | 10/14 0.714 | 18/23 0.783 | 12/15 0.800 | 15/18 0.833 | 0.399 | 0.375 |
| n_signals >= 4 | 7/14 0.500 | 12/23 0.522 | 11/15 0.733 | 14/18 0.778 | 0.166 | 0.178 |

Earlier figures reproduced: show 11/14 (TXE-A), contrast 5/14 (TXE-I), stab 1/14 (TXE-J). bandcut reads 5/14 here vs
TXE-F's 6/14 for its non-good label (TXE-F counted every non-good flag -- bad-crop, joined, blot -- not band 'cut' only).
Pass A: 23 wrong on dev by position_errors (the PREREG's 24 counts one insertion).

## Best OR-combination of k signals (dev chooses; full tables in measure_dev_tune.md / measure_eval_heldout.md)
| k | cap | dev vs L: combination, recall, share | dev vs pass A |
|---|---|---|---|
| 1 | 0.10 / 0.15 / 0.20 | latt 5/14 0.357 at 0.055 | latt 12/23 0.522 at 0.055 |
| 2 | 0.10 | latt 5/14 0.357 at 0.055 | latt 12/23 0.522 at 0.055 |
| 2 | 0.15 / 0.20 | **disagree+latt 6/14 0.429 at 0.105** | disagree+latt 14/23 0.609 at 0.105 |
| 3 | 0.10 / 0.15 / 0.20 | as k = 2 (no third signal adds an error inside the cap) | as k = 2 |

No OR-combination of up to 3 signals reaches 0.7 at <= 20% on dev: every signal with high recall (show, pair, freq, thin)
flags 23-50% of positions, and the two narrow ones (disagree, latt) overlap little with the errors L still carries --
L is passC + relabels, so A/B disagreements were already reconciled: on dev 12 of L's 14 errors sit where A and B agreed
(on eval 9 of 15). Against pass A (before reconciliation) the same pair holds 14/23 = 0.609.

## Eval_heldout, read-free, the dev-chosen combination (not re-chosen)
| read | disagree+latt recall | flagged |
|---|---|---|
| L | 9/15 = 0.600 | 23/376 = 0.061 |
| pass A | 12/18 = 0.667 | 23/376 = 0.061 |

## Single-pass detector (what a live letter has before reconciliation)
disagree, latt and show's merged-confidence leg need two passes. Restricted to the single-pass signals (bandcut, thin,
contrast, stab, pair) against pass A's 23 dev errors: best at <= 10% / 15% is stab, 1/23 at 5.2%; at <= 20% bandcut,
5/23 at 17.2%. A single-pass read-free detector does not exist here at a useful share.

## Sorter sizing (owner; TRANSCRIPTION.md item 7, 10-20 tiles a session)
eval_heldout, disagree+latt: 25 of 402 line-read positions flagged (6.2%; 23 of the 376 scored), 3 sessions of 10 tiles or
2 of 20; it would put 9 of L's 15 wrong signs in front of the owner. The list is `sorter_eval_heldout_disagree+latt.txt`
(line, pos, sign, signals). For comparison, `show` alone: 171 positions, 18 sessions of 10 (9 of 20) for 14 of 15;
n_signals >= 4: 67 positions (about 7 sessions of 10, 4 of 20) for 11 of 15 -- but on dev n>=4 holds only 7/14 at 16.6%.

## Follow-ups (one line each, not started)
- A ranked feed (sort by a weighted sum of signals, not an OR) would let the owner stop at any session count; weights
  must be chosen on dev and the gate re-registered first.
- freq (M22) needs a homophone-usage prior (observed share per homophone on solved pages) instead of an equal split
  before it can be narrow.

Commands: `python3 tools/tx_doubt.py signals --unit <u> --latt <lattice>`; `measure --unit dev_tune --base
units/passA_dev_tune.tsv`; `measure --unit eval_heldout --base units/passA_eval_heldout.tsv --combo disagree+latt`;
`list --unit eval_heldout --combo disagree+latt`. Vision calls 0.
