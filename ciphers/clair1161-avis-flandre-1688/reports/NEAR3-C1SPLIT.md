## NEAR3-C1SPLIT (4 Oct 2026)

Account 2 worker for LANE-NEAR3. Brief `.claude/briefs/runs/2026-10-04-ytbiz-near3-wave1.md`. Claim 01:15 UTC; runs 01:20-01:31 UTC
(container clock). Disk only, no network, no subagent calls. Two crop looks by this worker: the c186R block's 16 line crops
stacked, and a 53-snippet grid of the c185R `S`. Pre-registration `split/PREREG_split.md`, commit e6b33c38, pushed
before any run. Script `split/split.py`; occurrence assignment `split/assign.tsv`; rows `split/results.tsv`;
keys `split/<run>_key.tsv`. ciphertext.tsv, key.tsv and the reading are untouched.

**How each occurrence was assigned.**
- q/ls: pass B separates them. The 9 c185R occurrences reconciled as `q` where pass B read `ls` (7 q|ls, 1 S|ls, 1 p|ls in
  tx/c185R_rec/disagreements.tsv; L21's two columns are offset by one) became `qL`. The other 20 `q` are unchanged.
- S: neither pass separates them in the block (both write `S`). Assigned by eye from the stacked block crops: 7 open
  5-like -> `S5` (L03, L04 x2, L05, L06 3rd, L07 3rd, L08 2nd). 7 looped g-like stay `S`; the L07 2nd is graded M.
  The c185R snippet grid shows both shapes on c185R too, e.g. "+ S 4 S a" on L02, one of each. But the snippets were
  cut at x-positions estimated from token index. They were not reliable enough to label all 53 occurrences. So the S
  split was tested on the block only, and the 53 c185R `S` stay merged.

**Recipe.** Each run used homophonic_anneal.solve on the 924-sign stream: fr16 order 3, restarts 32, iters 40000,
seed 1, blind. The merged rerun reproduces key.tsv's anneal exactly: score -2281.4, gloss 0.5941, the
same as READ2-C1161 and READ2-C1161B. So the baseline is the current key's own recipe.

| run | K | anneal score | gloss match (c186R block) | c185R judge | new symbol's letter |
|---|---|---|---|---|---|
| merged (baseline) | 49 | -2281.4 | **0.5941** | **-1.155** | - |
| **qls split** (9 q -> qL) | 50 | -2360.7 | 0.3059 | -1.217 | qL = i, same as q (ls = e) |
| placebo-qls 1-5 (w, o, e, 9, p; 9 c185R occurrences each) | 50 | -2396.8, -2380.7, -2329.9, -2272.2, -2330.4 | 0.247, 0.165, 0.435, 0.582, 0.259; **p80 0.4353** | -1.222, -1.215, -1.157, -1.157, -1.169; **p80 -1.157** | - |
| **S split** (7 block S -> S5) | 50 | -2278.6 | 0.5824 | -1.143 | S5 = u, same as S |
| placebo-S 1-5 (+, 7, 4, th, qb; 7 block occurrences each) | 50 | -2343.8, -2314.9, -2368.1, -2322.6, -2324.3 | 0.112, 0.318, 0.200, 0.177, 0.271; **p80 0.2706** | -1.186, -1.200, -1.186, -1.228, -1.183; **p80 -1.186** | - |

(p80 = the 4th smallest of 5, as pre-registered.) judge thresholds on c185R: null_p99 -1.70, real_p05 -0.949 (N=704); every row FAILs the judge.

**Against the pre-registration.**
- q/ls: **FAIL**. The gloss match is 0.306, against 0.594 merged and 0.435 placebo p80. The c185R judge is -1.217,
  against -1.155 merged and -1.157 placebo p80. The split loses on both statistics, against both the baseline and the
  placebo.
- S: **FAIL**. The gloss match is 0.582, against 0.594 merged: it loses to merged by 0.012, though it beats placebo p80
  0.271. The c185R judge is -1.143, which beats merged -1.155 and placebo p80 -1.186. The gate needs both statistics,
  so the split fails.

**What else the runs show (not the gate).**
- In both real splits the anneal gave the new symbol the same letter as its parent: qL = q = i, and S5 = S = u. With
  one free letter more, the decipherment did not want to separate either pair.
- The S split stays close to the merged optimum: anneal score -2278.6 vs -2281.4, gloss 0.582 vs 0.594. Every S
  placebo falls far from it: scores -2315 to -2368, gloss 0.11-0.32. So treating the two S shapes as one sign is
  consistent with the key; a split of the same size elsewhere breaks it.
- The seed-1 anneal is sensitive to any change in the stream. 9 of 10 placebos and the qls split ended in a worse
  local optimum. That makes a single-seed comparison a coarse instrument. The pre-registration fixed seed 1, and no
  other seeds were run.

**Recommendation for the pooled re-anneal job: keep both pairs merged.** For q/ls this follows reconciliation's
choice, which was q. For the S shapes, keep one sign `S`. When c186L, c187L/R and c188L are transcribed, still record
the 5-like vs looped shape per occurrence (for example `S` plus a shape note). Then a pooled split test can be rerun at
higher N without another crop look. On c185R the shape is not recorded per occurrence. Recording it would need a
per-sign crop look, which this job did not do.

Report what was found and where it was not found: no outside source was searched; novelty is not classified here.
