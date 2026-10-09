# TXE2-LATT: widened lattice + word-level language, fixes at doubt positions only (PREREG-txeng2-2 X3, 9 Oct 2026)

LANE TX-ENGINEER-2, account 4, Opus 5.5 worker, 16:33-16:4x UTC 9 Oct 2026 by date -u. Brief
`.claude/briefs/runs/2026-10-09-account4-txe2-round2.md`. **Read-free: 0 vision calls, 0 reader calls, 0 network requests.**
No eval look (eval_heldout untouched; no eval item scored). No tool in `tools/` changed (harness scripts here only).

**Verdict: FAIL (dev).** Step 1's gate passed (lattice d 10/12); step 2's dev gate did not: best arm fixed 4, broken 5, p = 1.00
vs L_dev_tune; the registered leave-one-line-out choice the same (4/5, p = 1.00). Shuffled-key control 0/20 passes at every lam_w.

## Step 1: truth in lattice at L's 12 dev_tune errors (gate before any fix)
Lattices committed truth-free (7ed569e3e) before step 1 opened truth (bd: `run_latt2.py`, `step1.tsv`, commit after).
L = `benchmark-tx/outputs/birago1572-no87/labels.tsv`, lines f178v_L01-12: 12 wrong of 343 scored (tx_bench.position_errors;
matches the PREREG's E = 12). Truth is a set (every homophone of the clerk's letter), so "in lattice" is letter-level.

| lattice | built as | truth in lattice | cands/pos |
|---|---|---|---|
| (a) | from-passes A, B; passC skeleton; confusion_1572 spread 0.15 (TXE-E's `run_conf.lattice`) | 2/12 0.167 | 2.33 |
| (b) | (a) + atlas held-out top-3 (`txeng/compare/topk_no87_allheld.tsv`, all no.87 out of the vote; k1/k2/k3 at 0.20/0.10/0.05) | 4/12 0.333 | 3.42 |
| (c) | (a) + taxonomy pairs (`tx_pair_reread.PAIRS`, partner at 0.15 x p) | 7/12 0.583 | 3.27 |
| (d) | all | **10/12 0.833** | 5.06 |

Atlas source: the folder's `atlas/topk/no87_heldout.tsv` keeps only the eval lines out of the vote (dev lines vote on
themselves), so the all-held-out table TXE-A/TXE-O use was taken instead. Still missing in (d): L06.27 (u, T33|T49; lattice
T76 family) and L09.4 (e; lattice T96/T95/T92/T64). Step 2 ran on (d), the widest lattice >= 0.5.

## Step 2: word-level rescoring, fixes at disagree+latt only
Rule fixed in `run_word.py`'s docstring before scoring; decodes committed cf3ed13b7 before `tx_bench`. Per line, an N-best
beam (64, no recombination) under the it16dip 4-gram LM + lam 4 x log10 prior (TXE-E's objective); final hypotheses re-scored
+ lam_w x share of letters inside lexicon words >= 3 letters (`tools/segmenter.segment`, lexicon **it16dip**: PREREG names
`it16`, which is no corpus code in judge_plaintext; it16dip is the 16th-c. Italian corpus TX-DECODE/TXE-E use). Output = L
except at tx_doubt's disagree OR latt positions (`txeng/doubt/dev_tune_signals.tsv`, truth-free): 41 of 354.

`score.tsv` (tx_bench paired vs L, 343 common):
| arm | fixed | broken | p | output wrong |
|---|---|---|---|---|
| lam_w 0.5 | 4 | 5 | 1.000 | 13 |
| lam_w 1 | 4 | 5 | 1.000 | 13 |
| lam_w 2 | 3 | 4 | 1.000 | 13 |
| lam_w 4 | 3 | 4 | 1.000 | 13 |
| **LOO lam_w (registered; every line chose 0.5)** | 4 | 5 | 1.000 | 13 |
| blanket (diagnostic, every position) lam_w 0.5 / 4 | 4 / 3 | 7 / 6 | 0.55 / 0.51 | 15 |
| shuffled key x20 (control), lam_w 0.5 .. 4 | mean 1.3 | mean 11.4-11.7 | passes 0/20 each | |

## Mechanism (post-hoc `diag.py`, not a gate)
- lam_w = 0 (lattice d alone, same fix rule) gives the identical 4/5 as lam_w 0.5: **the word term adds nothing**; at lam_w 4 it
  drops one fix and one break. Over a ~30-letter line the share moves by a few letters between hypotheses, worth < 0.5 log10
  against 4-gram sums of tens, so it re-ranks almost nothing.
- Fixed: L06.18 d T98->T18, L10.4 e T76->T86, L11.29 e T60->T86 (the class-1 look-alike pairs the widening added), L11.5
  T76->T26 (tx_bench counts it fixed through its alignment; T26 is not in the truth set at that position -- noted, not re-scored).
- Broken: the three s X_CE->T50 (L04.4, L05.25, L08.10: the curled Ce s is on no sheet cell, so the key decode pays unk and
  swaps in a keyed homophone -- the same three breaks as TXE-E), L03.24 carmagnola T11->X_NEW, L11.4 l T95->T66.
- So the widened lattice does carry the truth (10/12) and the decode does take the d/s and n/e pairs, but the same fix rule
  breaks as many correct signs; doubt positions (41) include 9 of L's 12 errors and 32 correct signs, and the language model
  cannot tell an off-sheet s from a wrong one.

## Follow-up (one line, not done)
X_CE (and any off-sheet form) needs to be a keyed sign (value s) before any key-constrained decode is tried again on no.87; that
is a key-sheet change, a fresh attempt, not a re-tune of lam_w.
