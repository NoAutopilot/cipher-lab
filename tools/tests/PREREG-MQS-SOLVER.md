# PREREG MQS-SOLVER: homophonic solver settings from the Mary Stuart paper and CTTS, one matched and one mismatched control

Written 9 Oct 2026, 04:02 UTC by date -u, by MQS-SOLVER (LANE MQS, account 4), before any control cell below is run.
Brief: `.claude/briefs/runs/2026-10-09-acct3-mqs-solver.md`. Options: commit 0aa8fd5ae (`tools/homophonic_anneal.py`,
`tools/families/homophonic.py`, offline test `tools/tests/test_homophonic_mqs.py`). Results go to
`tools/tests/MQS-SOLVER-controls.tsv`, one row per cell (mean, SD, per-seed values, processed share). No target is run.

## Sources

Lasry, Biermann and Tomokiyo 2023 (Cryptologia 47:2) App. A pp.195-197 (swap and reassign moves, Figs A18-A19; score
S = sum N_g log F_g / sum N_c^2), Fig. 8 p.119 (1-2 homophones per letter, nomenclature), p.110 (2,600 mean letter
length); CTTS paper p.2 and README "Built-in Cryptanalysis" (minimum count, homophone budget, ignored h and doubles);
Kopal 2019; our digest `LESSONS-LASRY.md` s.3 items 1, 3, 5. Swap and cap ported from `tools/subst_hillclimb.py`
(23 Sept 2026, bowes-walsingham-1583).

## Known answers (no ciphers/ folder)

All controls are synthetic, cut from `tools/data/fr16`; no `ciphers/<slug>` folder is used as a known answer, so the
prior-work step (`tools/prior_work.py`) has no item to run on (stated, not skipped silently).

- Plaintext (held out): `zcat tools/data/fr16/lettresdecatheri02cathuoft_djvu.txt.gz | dd bs=1 skip=1200000 count=40000`
  (Lettres de Catherine de Médicis t.2, a letter-text stretch; the whole of t.2 is held out of the model).
- Corpus: `lettresdecatheri01cathuoft` (t.1) and `lettresindites00marg` (Marguerite de Valois), decompressed, two
  `--corpus` files. Model: the tool's default order-3 add-k, 24 letters (u/v, i/j merged), 40,000 iters.

## Design

`homophonic_anneal.py --control PLAIN --signs K --length N --control-homs LO-HI --marked 0.3:60` (make_marked_control):
the 60 most frequent word types of the stretch become marked signs m0..m59, one token per occurrence.

- Matched: K = 40 letter signs, 1-2 homophones per letter (Fig. 8). Mismatched: same text, K = 52, 1-3 per letter.
- **Deviation, pre-registered:** whole-word replacement of 60 types cannot reach 30% of tokens on this text; with q = 1
  (every occurrence marked) the probe at 04:03 gave 20.1% (N=800), 14.9% (N=1500), 12.4% (N=2600). The cells use that
  achieved share (reported per row), not 30%; raising the type count to force 30% would no longer be "about 60 signs".
- Seeds 1, 2, 3 for every cell; `--seed` sets both the control instance (homophone draws) and the solver stream.

## N rule (fixed before running)

Try N in {800, 1500, 2600} tokens (marked included). Baseline = defaults, `--restarts 8`, marked signs handled by
`--skip` (`--marked-mode skip`: deleted). Use the largest N whose baseline mean over seeds 1-3 is between 20% and 85%
letter accuracy. If none qualifies: "no headroom at these N", no gain claim, cells still reported. Ceiling check: if
the chosen baseline mean is >= 95% or the 2x-restarts cell already matches the best option, no gain is read.

## Accuracy denominator

All letter tokens of the control (marked tokens excluded, they carry no single letter); `?` (a gap or a sign left out
by `--min-count`) counts wrong. The same denominator in every cell; the processed share is reported beside each.

## Cells (3 seeds each, `--restarts 8` unless named, marked signs by `--skip` unless named)

| cell | change from baseline | expected (before running) |
|---|---|---|
| base | none | 20-85% by the N rule |
| base_r16 | `--restarts 16` (restarts-alone bar) | base + 0-5 points |
| swap | `--moves swap` | below base: swap-only fixes the start's homophone counts (frequency allotment, capless), which differ from the truth's 1-2 split |
| both | `--moves both` | within +-5 of base |
| cap2 | `--max-homophones 2` (matched: oracle upper bound, the generator uses exactly 1-2) | base + 0-10 |
| mis_base, mis_r16 | mismatched design (K=52, 1-3 per letter), baseline and 16 restarts | below the matched base |
| mis_cap2 | mismatched, `--max-homophones 2` (grades the option: the cap is wrong for 1-3 designs) | at or below mis_base |
| min3 | `--min-count 3` | below base: rare signs become `?` and count wrong; processed share < 100% |
| unknown | `--marked-mode unknown` (= `--as-unknown`, marked kept as gaps) | above base (no false joined n-grams) |
| wild | `--marked-mode wild` (families/homophonic `wild=`) | at or below base (each marked token a free letter, many extra pseudo-signs) |
| nomen | `--marked-mode nomen` (solve_nomen, word_signs = marked, vocab = corpus top-100 words of >= 2 letters) | between base and unknown |
| nc2_u1, nc2_u0 | `--norm nc2`, `--uni-weight 1` / `0` | within +-10 of base (C1161-LOLO: "nc2 rewards rare letters at this free share (D2, D3)", ciphers/clair1161-avis-flandre-1688/tx/PREREG_reanneal_lolo.md point 1) |
| nc2p_u1, nc2p_u0 | `--norm nc2paper`, `--uni-weight 1` / `0` | u0 well below base (with log-probabilities < 0, dividing by sum N_c^2 can reward concentration) |

`--drop-letters` and `--collapse-doubles` have no matched design here (the generator writes h and doubles); they are
covered by the offline tests only. `--homophone-budget` shares `--min-count`'s mechanism (search_gaps) and is tested
offline only.

## Gate per option (fixed before running)

An option "helps" only if (mean(option) - mean(base)) > max(mean(base_r16) - mean(base), 2 x SD(base)), on the same
design (mis_cap2 against mis_base, mis_r16 and SD(mis_base)). For `unknown`, its gain must also beat the best of base
(--skip), wild and nomen. An option that misses the gate ships with shelf grade `weak` and both numbers; one that
passes is `controlled-only` (one synthetic control, no target). cap2 on the matched design is an oracle bound and grades
nothing; mis_cap2 grades `--max-homophones`. min3's gate is the same; its expected loss is the price of the processed
share, reported beside it.

## Why each null can fail differently from the known answer (rule 3)

The statistic is letter accuracy on a known-answer control. The null bar is base_r16 (more restarts, same objective
and move set): it changes only the search budget. Each option changes the move set (swap, both), the state space
(cap), the stream scored (min3, unknown, wild, nomen: gaps, deleted neighbours, per-position letters change which
n-grams exist), or the objective (nc2, nc2paper); each can therefore move accuracy up or down independently of the
restarts bar, and the marked-sign cells change the n-gram statistic itself, so they can fail differently from --skip.

## Amendment 1 (9 Oct 2026, 04:06 UTC by date -u, after the N-rule baselines and before any option cell)

N-rule result, baseline (defaults, 8 restarts, marked by --skip), seeds 1-3: N=800 0.9640/0.9624/0.9687, mean 0.965
(SD 0.0033); N=1500 0.9421/0.9460/0.9640, mean 0.951 (SD 0.0117); N=2600 0.9460/0.9508/0.9451, mean 0.947 (SD 0.0031).
**No N qualifies (all above 85%, and all at or near the 95% ceiling): "no headroom at these N".** Per the rule above, no
gain claim is made for any option on the matched design. The cells are still run and reported, at N=800 (the cheapest;
all three N are at ceiling). Grades: every option ships `weak` on this evidence (no gate can pass at ceiling), with
its numbers. The mismatched design (mis_*) is read against its own gate only if mis_base's mean is between 20% and 85%;
otherwise it too is "no headroom". The grid of N is not extended in this job (the brief fixes {800, 1500, 2600}); a
lower-N or harder-design grid is a follow-up suggestion, not done here.
