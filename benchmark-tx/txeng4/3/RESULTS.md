# TXE4-3 ATLAS-NCA -- RESULTS (12 Oct 2026, 01:20-01:5x UTC by date -u)

Worker TXE4-3 (account 3, Fable 5.1, session_01MfBjefFUCgpwKvfagrojGC), brief `.claude/briefs/runs/2026-10-11-acct3-txe4-3.md`
(93b7bb32), PREREG `benchmark-tx/PREREG-txeng4-3.md` (9eb0611aa, pushed 01:26 UTC before any map, read or score). Read-free:
no reader, no vision call, no network beyond git and one `pip install` of the three libraries glyph_atlas.py needs
(opencv-python-headless, scikit-image, scikit-learn; PyPI through the proxy, 1 install). Request counts per host: none.

**Verdict (gate word for word, eval_heldout, as measured): FAIL.** (i) A2 vs A1 paired: fixed 11, broken 10, exact p = 1.000
-- not fixed > broken at p < 0.05. (ii) A2 err_true 0.242 > A0's 0.162. (iii) every A3 seed >= A2 + 0.20: min A3 0.846 vs
0.442 -- met. "(i) and (iii) without (ii)" does not apply because (i) fails; "anything else: FAIL". Flagged-excluded does not
reverse it (A2 0.232 vs A1 0.235, same paired count). A4 (beside, gated the same way): (i) fixed 46, broken 8, p < 0.0001;
(ii) 0.144 <= 0.162; (iii) min A3 0.846 >= 0.344 -- all three met, but see the caveat under A4.

## Commits (pre-registration first)
9eb0611aa PREREG | ec779a164 unit 1 labels | 904c82d80 unit 2 tool | cc94d217d, 38bdc6bd1 unit 3 grid + frozen | 47e11ec39 A5
join check | 51e80982f unit 4 outputs + LOOKS | this commit: scores, RESULTS, LEDGER, shelf.

## Unit 1 -- machine labels (no owner, no known answer)
Line correspondence (new, truth-free; `build_labels.py` stage 1, `labels/correspondence.txt`): ordered passages to ordered
atlas rows by a monotone count DP (a row takes 0 or 1 passage, or k >= 2 only when its y-spread shows two baselines, then
split by optimal 1-D y-clustering). Step-1 width-only seed round: 936 tokens on 11 pages. Step-2 bootstrap kNN
(`--only-train-labels`, labels_empty.json, no.87 and f152r held out). Round 2 label-aware (lam 1.5, --loo), gated per page by
`tools/join_check.py --steered` with the step-2 top-1 as check labels:

```
join_check: FAIL n=87 share0=0.115 (null p95 0.071) share+-1=0.046 (bound 0.151) -> benchmark-tx/txeng4/3/labels/round2_f139v.tsv.joincheck.json
dropped ['f139v_L01', 'f139v_L02', 'f139v_L04']; recheck: PASS n=20 {'+-2': 1, '+1': 1, '-1': 1, '0': 8, 'none': 9}
join_check: PASS n=20 share0=0.400 (null p95 0.150) share+-1=0.100 (bound 0.203) -> benchmark-tx/txeng4/3/labels/round2_f139v_recheck.tsv.joincheck.json
join_check: UNCHECKABLE n=37 share0=0.000 (null p95 0.054) share+-1=0.135 (bound 0.136) -> benchmark-tx/txeng4/3/labels/round2_f144r.tsv.joincheck.json
join_check: UNCHECKABLE n=6 share0=0.333 (null p95 0.342) share+-1=0.167 (bound 0.333) -> benchmark-tx/txeng4/3/labels/round2_f162r.tsv.joincheck.json
join_check: PASS n=73 share0=0.589 (null p95 0.097) share+-1=0.027 (bound 0.110) -> benchmark-tx/txeng4/3/labels/round2_f174r.tsv.joincheck.json
join_check: FAIL n=208 share0=0.207 (null p95 0.044) share+-1=0.077 (bound 0.111) -> benchmark-tx/txeng4/3/labels/round2_f174v.tsv.joincheck.json
dropped ['f174v_L05', 'f174v_L06', 'f174v_L07']; recheck: PASS n=139 {'+-2': 11, '+1': 7, '-1': 5, '0': 43, 'none': 73}
join_check: PASS n=139 share0=0.309 (null p95 0.058) share+-1=0.086 (bound 0.123) -> benchmark-tx/txeng4/3/labels/round2_f174v_recheck.tsv.joincheck.json
join_check: FAIL n=266 share0=0.568 (null p95 0.057) share+-1=0.056 (bound 0.099) -> benchmark-tx/txeng4/3/labels/round2_f174vB.tsv.joincheck.json
dropped ['f174vB_L01']; recheck: PASS n=247 {'+-2': 7, '+1': 5, '-1': 8, '0': 151, 'none': 76}
join_check: PASS n=247 share0=0.611 (null p95 0.057) share+-1=0.053 (bound 0.097) -> benchmark-tx/txeng4/3/labels/round2_f174vB_recheck.tsv.joincheck.json
join_check: PASS n=23 share0=0.565 (null p95 0.130) share+-1=0.043 (bound 0.176) -> benchmark-tx/txeng4/3/labels/round2_f175r.tsv.joincheck.json
join_check: PASS n=45 share0=0.756 (null p95 0.089) share+-1=0.044 (bound 0.138) -> benchmark-tx/txeng4/3/labels/round2_f175v.tsv.joincheck.json
join_check: FAIL n=135 share0=0.178 (null p95 0.059) share+-1=0.059 (bound 0.111) -> benchmark-tx/txeng4/3/labels/round2_f184r.tsv.joincheck.json
dropped ['f184r_L14', 'f184r_L15']; recheck: PASS n=112 {'+-2': 2, '+1': 3, '-1': 2, '0': 24, 'none': 81}
join_check: PASS n=112 share0=0.214 (null p95 0.063) share+-1=0.045 (bound 0.118) -> benchmark-tx/txeng4/3/labels/round2_f184r_recheck.tsv.joincheck.json
join_check: PASS n=90 share0=0.544 (null p95 0.067) share+-1=0.100 (bound 0.112) -> benchmark-tx/txeng4/3/labels/round2_f184v.tsv.joincheck.json
join_check: FAIL n=116 share0=0.336 (null p95 0.061) share+-1=0.034 (bound 0.131) -> benchmark-tx/txeng4/3/labels/round2_f185r.tsv.joincheck.json
dropped ['f185r_L07', 'f185r_L09']; recheck: PASS n=93 {'+-2': 3, '+1': 1, '-1': 2, '0': 39, 'none': 48}
join_check: PASS n=93 share0=0.419 (null p95 0.077) share+-1=0.032 (bound 0.130) -> benchmark-tx/txeng4/3/labels/round2_f185r_recheck.tsv.joincheck.json
```

AGREED LABELS (1:1 at the same position in both rounds, on a line whose per-line verdict is pass): **391** -- f174r 41, f174v
61, f174vB 134, f175r 13, f175v 21, f184r 49, f184v 48, f185r 24; f139v 0 (its three dropped lines and the two-round rule),
f144r and f162r UNCHECKABLE (nothing). 42 codes, 31 with >= 5 tiles. This is about a third of the ~1,100 the brief
expected: the two-round same-position rule and the per-line gate, applied as pre-registered, drop most of the seed round.
A4's no.87 tiles: passA/passB LCS agreement 743 of 844; `verdict ('FAIL', 'PASS'); lines kept 28/29; agreed 662`.
A5's secure tokens (588 after removing f152r): join_check (unsteered, check = step-2 top-1) **PASS**, n=588,
0/-1/+1 443/5/6 (share0 0.753, null p95 0.077) -- A5 is scored, beside.

## Unit 2 -- tool (tools/glyph_atlas.py classify)
`--features hog|hog+zone+topo` (the 29 TXE3-10 zone/topology features beside HOG+PCA40), `--metric none|lda|nca --metric-dim D
--metric-seed --topo-cache`: the metric and the zone/topo scaling are fitted on the labelled VOTER tiles only (never a held or
held-out-page box); `<tsv>.metric.json` records fit_tiles, fit_pages, classes. Default path byte-identical (checked against the
committed step-2 output). Offline test `tools/tests/test_glyph_atlas_metric.py`: fit never sees the held-out page; the planted
toy separates under hog+zone+topo NCA (1.00) and LDA (1.00); hog NCA on 72 tiles over 40 unit-scaled PCA components only
beats the base distance (0.85 vs 0.72) -- a learned metric on few tiles over many noise components overfits, recorded in the
test, not hidden. tool_shelf.tsv row `glyph_atlas.py classify --features --metric`. (`tool_shelf.py --check` and
`system_map_check.py` report pre-existing STALE/MISSING rows for iiif_lines.py and tx_selfcheck.py, unrelated to this change.)

## Unit 3 -- dev grid (f178v L01-12; 343 as measured / 338 flagged-excluded scored; NCA on the 391 agreed labels)
| features | dim | k | flagged-excl err (k/n) | Wilson 95% | as measured err (k/n) | Wilson 95% | S/D/I |
|---|---|---|---|---|---|---|---|
| hog | 16 | 3 | 0.3757 (127/338) | 0.326-0.428 | 0.3848 (132/343) | 0.335-0.437 | 115/3/14 |
| hog | 16 | 5 | 0.3728 (126/338) | 0.323-0.425 | 0.3819 (131/343) | 0.332-0.434 | 114/3/14 |
| hog | 16 | 9 | 0.4053 (137/338) | 0.354-0.458 | 0.414 (142/343) | 0.363-0.467 | 125/3/14 |
| hog | 32 | 3 | 0.3491 (118/338) | 0.300-0.401 | 0.3586 (123/343) | 0.310-0.411 | 105/3/15 |
| hog | 32 | 5 | 0.3284 (111/338) | 0.281-0.380 | 0.3382 (116/343) | 0.290-0.390 | 99/3/14 |
| hog | 32 | 9 | 0.3817 (129/338) | 0.331-0.435 | 0.3907 (134/343) | 0.341-0.443 | 117/3/14 |
| hog | 64 | 3 | 0.3639 (123/338) | 0.314-0.416 | 0.3732 (128/343) | 0.324-0.426 | 111/3/14 |
| hog | 64 | 5 | 0.3462 (117/338) | 0.297-0.398 | 0.3557 (122/343) | 0.307-0.408 | 105/3/14 |
| hog | 64 | 9 | 0.3698 (125/338) | 0.320-0.422 | 0.379 (130/343) | 0.329-0.431 | 113/3/14 |
| hog+zone+topo | 16 | 3 | 0.2899 (98/338) | 0.244-0.340 | 0.3003 (103/343) | 0.254-0.351 | 86/3/14 |
| hog+zone+topo | 16 | 5 | 0.284 (96/338) | 0.239-0.334 | 0.2945 (101/343) | 0.249-0.345 | 84/3/14 |
| hog+zone+topo | 16 | 9 | 0.2959 (100/338) | 0.250-0.347 | 0.3061 (105/343) | 0.260-0.357 | 88/3/14 |
| hog+zone+topo | 32 | 3 | 0.2663 (90/338) | 0.222-0.316 | 0.277 (95/343) | 0.232-0.327 | 78/3/14 |
| hog+zone+topo | 32 | 5 | 0.2544 (86/338) | 0.211-0.303 | 0.2653 (91/343) | 0.221-0.314 | 74/3/14 |
| hog+zone+topo | 32 | 9 | 0.2929 (99/338) | 0.247-0.344 | 0.3032 (104/343) | 0.257-0.354 | 87/3/14 |
| hog+zone+topo | 64 | 3 | 0.2811 (95/338) | 0.236-0.331 | 0.2915 (100/343) | 0.246-0.342 | 83/3/14 |
| hog+zone+topo | 64 | 5 | 0.2663 (90/338) | 0.222-0.316 | 0.277 (95/343) | 0.232-0.327 | 78/3/14 |
| hog+zone+topo | 64 | 9 | 0.3077 (104/338) | 0.261-0.359 | 0.3178 (109/343) | 0.271-0.369 | 92/3/14 |

Frozen (committed 38bdc6bd1 before the eval look): **hog+zone+topo, NCA dim 32, k 5** (dev flagged-excluded
0.2544, as measured 0.2653). Every zone+topo setting beats every hog-only setting on dev.

## Unit 4 -- the one eval look (no.87 eval_heldout: f178v L13-23 + f179r L01-03; 376 as measured / 371 flagged-excluded scored)
LOOKS register: `benchmark-tx/txeng4/LOOKS.tsv` (created by this job at its dev row); TXE4 rows on birago1572-no87 now 3 (this
job's dev_tune and eval_heldout rows, and one TXE4-6 row); on birago1572-f152r 2 (this job's, TXE4-6's). TXE3 looks of 11 Oct, as the brief lists them:
TXE3-7 and TXE3-9 on the whole of no.87, TXE3-10 on no.87 eval_heldout, TXE3-7 on f152r, TXE3-3 on gunther.
Can-vary before scoring (`can_vary.json`): 412 eval boxes; A2 != A1 on 76; A2 != each null on
374-407; blanks A2 0, A1 0. The test could vary.

Outputs are per-line BOX SEQUENCES of top-1 codes (no box map; a '_' top-1 is written as '_'). D = 5 and I = 16 are the same in
every arm (boxes the segmenter missed or added), so the arms differ in S only.

| arm | as measured err (k/n) | Wilson 95% | S/D/I | strict | flagged-excl err (k/n) | Wilson 95% | S/D/I |
|---|---|---|---|---|---|---|---|
| eval_A0 | 0.2021 (76/376) | 0.165-0.246 | 55/5/16 | 0.2234 | 0.1914 (71/371) | 0.155-0.234 | 50/5/16 |
| eval_A0p | 0.1968 (74/376) | 0.160-0.240 | 53/5/16 | 0.2101 | 0.186 (69/371) | 0.150-0.229 | 48/5/16 |
| eval_A1 | 0.2447 (92/376) | 0.204-0.291 | 71/5/16 | 0.258 | 0.2345 (87/371) | 0.194-0.280 | 66/5/16 |
| eval_A2 | 0.242 (91/376) | 0.201-0.288 | 70/5/16 | 0.2527 | 0.2318 (86/371) | 0.192-0.277 | 65/5/16 |
| eval_A4 | 0.1436 (54/376) | 0.112-0.183 | 33/5/16 | 0.1516 | 0.1321 (49/371) | 0.101-0.170 | 28/5/16 |
| eval_A5 | 0.2074 (78/376) | 0.170-0.251 | 57/5/16 | 0.2287 | 0.1995 (74/371) | 0.162-0.243 | 53/5/16 |
| A3 (20 seeds) | 0.846-0.928 | | | | 0.846-0.933 | | |

- A0 here is labels.json with EVERY no.87 page held out of the vote (f178r_, f178v_, f179r_), 0.202; the brief's 0.162 of record
  (`atlas/tx_bench_atlas.txt`) kept the 12 tune lines' no.87 boxes (and their 309 truth overrides) as voters. The gate uses
  0.162 as written. A0' (labels_boxmapLA.json) 0.197, beside, never gated.
- Paired against A1 (as measured; flagged-excluded identical in sign):
  A2: lines improved/worsened/tied 4/3/7, line p 1.0000; positions fixed 11, broken 10, exact p 1.0000.
  A4: 13/1/0, line p 0.0018; fixed 46, broken 8, p 0.0000.
  A5: 10/0/4, line p 0.0020; fixed 33, broken 18, p 0.0489.
  A0: 11/2/1, line p 0.0225; fixed 42, broken 26, p 0.0681.
- Top-3 through `atlas/score_no87.py --map <temp no87_map.py --compat copy>` (370 signs; the scorer's join, no arm saw it;
  reference on file: top-1 0.103, top-3 miss 0.078): A0 atlas top-1:              err_true 0.097  (wrong+U 0.124) / atlas top-3 miss (truth not among the 3 codes' values): 0.092; A0' atlas top-1:              err_true 0.078  (wrong+U 0.111) / atlas top-3 miss (truth not among the 3 codes' values): 0.095; A1 atlas top-1:              err_true 0.216  (wrong+U 0.216) / atlas top-3 miss (truth not among the 3 codes' values): 0.154; A2 atlas top-1:              err_true 0.208  (wrong+U 0.208) / atlas top-3 miss (truth not among the 3 codes' values): 0.165; A4 atlas top-1:              err_true 0.105  (wrong+U 0.105) / atlas top-3 miss (truth not among the 3 codes' values): 0.070; A5 atlas top-1:              err_true 0.178  (wrong+U 0.178) / atlas top-3 miss (truth not among the 3 codes' values): 0.138.
- A2's top confusions: r <- T90 x5, r <- T60 x4, r <- T19 x4, m <- T85 x4 (the 'r' sign has no agreed label with >= 5 tiles).

f152r (73 scored, beside, direction only): A0 0.3288, A0' 0.3151, A1 0.2329, **A2 0.3562**, A4 0.274, A5 0.2877; A3 0.808-0.959. On f152r the learned metric reads WORSE than the plain kNN on the same labels (26 vs 17 errors of 73).

## Reading
- The learned distance (NCA) with the zone/topology features gained 0.011 on dev and 0.003 on eval over the same 391 tiles under
  HOG+PCA40 (A1), within noise (11 fixed, 10 broken), and lost on f152r. The dev grid's clear preference for zone+topo did not
  carry to eval. With 391 tiles over 42 codes the metric has little to learn from; the toy test shows the same overfitting shape.
- Reader-agreed labels from nine sibling leaves (A1/A2, about 0.24) stay well behind the known-answer-named atlas (0.162 of
  record; 0.20 with no no.87 tile voting), though ahead of TXE3-7's 445 owner or machine tiles (0.30-0.31 on no.87 after the
  rescore), with fewer tiles but a checked join.
- **A4 caveat.** A4 adds 662 no.87 A/B-agreed tiles of the SAME HAND, leave-one-line-out, and reads 0.144 -- under the 0.162
  gate and 46 fixed / 8 broken against A1. But A1 is not A4's label-volume control: A4 differs from A1 in tiles AND metric, so
  the gain cannot be credited to the metric (A2 vs A1 says the metric alone adds nothing). The honest reading is that same-hand
  reader-agreed tiles, with no known answer, name this atlas about as well as the truth-named one on the held-out lines; the
  un-run control (A4's tiles under plain HOG+PCA40) is the first next step. Not run here: not pre-registered (Usage 7).
- A5 (secure_tokens, labels.json-filtered, LCS-joined, join PASS) 0.207, fixed 33 / broken 18, p 0.049 vs A1: 588 tiles filtered
  by the known-answer atlas beat 391 unfiltered ones; its join gate passed where this job's own construction kept a third.

## Three sentences for the owner
1. The machine can put names on this family's signs with no known answer and no sorting by you, from places where the two blind
   readers agreed on other letters, but on no.87's held-out lines it gets about one sign in four wrong (0.24), against one in
   six for the atlas that was named from the clerk's answer sheet (0.16).
2. Teaching the classifier a better distance (NCA on shape and topology features) did not help: 11 fixed, 10 broken, the same
   score, and worse on the second letter; the labels, not the distance, are the limit at this size.
3. Adding the readers' agreed tiles from no.87 itself (never the line being read) brings it to 0.14, under the truth-named atlas
   -- so for a new key family the plan is: read a few leaves twice, keep what both readers agree on, join it with the checked
   aligner, and name the atlas from that; the learned distance can be left out.

## Next step (named, not run)
A4's label-volume control: the same 391 + 662 tiles under HOG+PCA40 kNN5 (metric none), leave-one-line-out, one eval look, about
USD 4. On a PASS of that pair, the brief's own next steps: the stack on gunther's second hand (TXR-6), about USD 13; A4's top-3 fed
to the key-constrained lattice (TXE3-9), about USD 4. Also: the line-correspondence step kept a third of the seed tokens; a
correspondence steered by the bootstrap labels (choose the row by leave-one-out label agreement) would be a different
instrument for the same labels, about USD 5.

## Deviations and notes
- Brief's ~1,100 agreed tokens: 391 survived the pre-registered rules (see unit 1).
- A first run of unit 1 (folder `maps/`, gitignored, never committed) read the agreement files' gap tokens and let a partial-cipher first line
  merge with the next; both fixed before any classifier arm ran. A built-in safety check denied the scratch cleanup `rm`
  (variable path); not re-issued, the folder was renamed instead.
- `tools/tx_register.py` run without `--stdout` rewrote research/TX-REGISTER.tsv in the working tree; not committed here.
- Cost: from the parent's get_session. Box: 01:20-03:20 UTC; done well inside it.
