# TXE3-5 BOXES results: do the owner's corrected boxes lower err_true? (account 3; Fable worker session_014KPMCN7x6L5GsRgRFKMCLr; 05:47-06:1x UTC 11 Oct 2026 by date -u)

PREREG: benchmark-tx/PREREG-txeng3-5.md (committed f3e32015 before any arm was classified). Scripts here: build_arms.py (arms + one
classify call), score_arms.py (scores.tsv), proxy.py (proxy.txt). Tool added: `tools/glyph_atlas.py classify --boxes BOXES.tsv
[--boxes-median-h PX]` (external boxes re-cut into the atlas's fitted feature space; offline test in tools/tests/test_glyph_atlas.py).
The oracle pages and answers were read only; nothing was written to them; nothing published; no reader or vision call anywhere.

## Overlap found
All three oracle hands overlap a benchmark item with truth, but only one has a tile pipeline:
- **Birago no.87 f178v L01-L12** = birago1572-no87 (eval), 343 scored positions on these lines. The Birago 1572 family atlas exists, but
  these 12 lines are the atlas's own tune lines (cluster names and per-tile overrides were set from them), so absolute figures are
  optimistic; the paired machine-vs-owner difference under one atlas is the endpoint.
- **Vivonne f102r** 12 lines = vivonne1573-f102r-dev/-dev2 (dev; 302 / 447 scored on these lines): no atlas for the hand -> proxy.
- **La Luzerne p.1** L01-L11 = luzerne108a-p1 (dev; 64 scored groups): a digit hand, truth at the group level, no atlas -> proxy.

## Birago: full pipeline, boxes the only change (scores.tsv; tx_bench --item birago1572-no87 --coverage-diagnostic, 12 of 27 lines)
Arms from the 343 tiles of the owner's page (oracle1/boxes/boxes_recut_all.tsv); the 3 kind=mark tiles left out of every scored sequence
(with them in: machine 0.315, owner 0.300); classify --boxes --topk 3 --boxes-median-h 68 (the atlas's f178v median); sign = k1.

| arm | err_true as measured (Wilson 95%) | flagged excluded | S / D / I | lines better / worse / tied vs machine | edits vs machine |
|---|---|---|---|---|---|
| machine (343 boxes) | 0.309 (106/343) 0.262-0.360 | 0.299 (101/338) 0.253-0.350 | 68 / 26 / 12 | -- | 0 |
| **owner** (11 trashed + 3 re-cut) | **0.297 (102/343) 0.251-0.348** | **0.287 (97/338) 0.241-0.337** | 61 / 33 / 8 | 5 / 1 / 6, sign p 0.22 | **-4** |
| owner, trash only | 0.294 (101/343) 0.249-0.345 | 0.284 (96/338) 0.239-0.334 | 60 / 33 / 8 | 5 / 0 / 7, p 0.06 | -5 |
| owner, re-cuts only | 0.309 (106/343) 0.262-0.360 | 0.299 (101/338) 0.253-0.350 | 68 / 26 / 12 | 1 / 1 / 10 | 0 |
| control, 20 seeds (same edits on size-matched random boxes) | mean 0.326, min 0.321, max 0.332 | mean 0.316 | -- | best seed 2 / 6 | +4 to +8, mean +5.65 (sd 1.19) |

Gate (PREREG): owner < machine: yes (-4 edits, -0.012). Owner's improvement beats the control at 20/20 seeds (every seed is WORSE than
the machine; one-sided p < 0.05): yes. Control mean not below machine: yes (it is above). **PASS, small.** The whole gain is the 11
trashed page-edge shadows (trash-only -5); the 3 re-cuts net 0 (one box fixed, one broken: L05_b015 T13 -> `_`, L10_b031 `_` -> T86,
L11_b029 T52 -> T83). The classifier had read the 11 shadows as `_` (8) or T95 (3); removing them turns line-end substitutions into
deletions (S 68 -> 61, D 26 -> 33, I 12 -> 8), which is why 11 removed boxes buy only 4-5 edits. The Wilson intervals of machine and
owner overlap almost entirely: at N = 343 a 1.2-point difference is a direction with a matched control, not a settled size.

Beside: the committed line reads on the same 12 lines score 0.055 (passC) and 0.035 (labels), so this atlas-on-these-boxes pipeline is
at 0.30, about 6x worse -- the machine boxes also miss signs (340 sign boxes for 354 positions; 26 deletions), and the strip-level
binarisation of the oracle crops is not the page-level one the atlas was built from. The 0.309 is not comparable to TX-ATLAS-B72's
0.162 (different boxes, different held-out lines); the comparison here is arm against arm only.

## Vivonne and Luzerne: no pipeline, the proxy (proxy.txt)
1. **Cut-error share in the existing reads on exactly the oracle lines**: Vivonne dev (12 lines, 302 scored): committed S 120 D 0 I 0,
   passA S 117 D 4 I 0, passB S 123 D 2 I 0, passZ_dv1 S 130 D 3 I 14 (cuts 17/147 = 12%); Luzerne (64 groups): every output S 6 D 0
   I 0. On both hands the line readers' errors are almost all substitutions, so a box correction has little cut error to remove there.
2. **Count proxy** (machine vs owner box count per line against the line's unit count; owner edits = not-letter + aside + Vivonne's 17
   merge-absorbed boxes; BAD-CUT kept as a machine box by the owner's own rule; 200 random-deletion controls of the same size):
   - Vivonne: machine 541 boxes vs 610 truth positions, every line UNDER (signed -69); the owner's 18 removals take it further (-87);
     sum|boxes-ref| 71 -> 87; control mean 87.2 (min 87). The 11 merges are pen-unit boxes over shapes the blind one-or-several pass
     read as mostly several signs (joined/README.md: 9 of 16 likely several), so by construction they lower the box count below the
     sign count.
   - Luzerne: machine 445 boxes vs 346 digits in the committed read, every line OVER (+99); the owner's 31 trashes bring it to +68,
     sum|boxes-ref| 99 -> 68; control mean 68.7 (min 68).
   **Both proxies are non-tests by CLAUDE.md rule 3's "control cannot vary" shape**: when every line sits on the same side of the
   reference, any deletion of k boxes moves the count statistic by exactly k whichever boxes are chosen, so the random control equals
   the owner by construction (176/200 and 157/200 seeds at or below the owner only through the few lines that cross zero). They say
   that the machine undercuts Vivonne and overcuts Luzerne, not whether the owner's choices were the right ones. Position-level
   checking (do his re-cuts sit where readers made cut errors) needs a box-to-truth alignment on these hands that does not exist.
3. **The 11 Vivonne merges**: Vivonne has dev truth but no tile pipeline, so no err_true; through the count proxy they move the box
   count 17 further below the truth position count, consistent with the blind pass's "several signs in one box" and with the owner's
   stated convention (pen units). Whether the reference should count pen units or sign units is the box-check team's call.

## For the owner, in three sentences
On the one page where we could test it end to end (Birago no.87, 12 lines), your box corrections made the machine reading slightly
better, and every one of 20 random edits of the same size made it worse, so the direction is real but the size is small: 4 fewer
errors in 343 signs, all from the 11 page-edge shadows you threw out, none from the 3 re-cuts. The shadows were already being read
as "unknown" by the classifier, which is why removing them helped less than 11 boxes might suggest. On Vivonne and La Luzerne we
could only count boxes: the machine cuts too few boxes on Vivonne and too many on La Luzerne, and your merges follow your pen-unit
rule, which gives fewer boxes than there are signs -- that convention question, not accuracy, is what those pages decide.

## Next step and cost
A real test on Vivonne needs a tile pipeline for the Saint-Gouard hand: segment all 37 f.102r lines, cluster, name clusters from the
25 non-oracle lines' dev truth by a label-blind width DP (no87_map.py's shape) and classify the 12 oracle lines with machine vs owner
boxes, same arms and control as here: about USD 6-8, 60-75 min, one Opus/Fable worker, no reader call. Cheaper and first: make the
segmenter route last-of-line dark edge boxes to the owner's step 2 as a question (the shadow rule in answers/shadow/README.md is NOT
validated as a filter; as a question it costs nothing) -- about USD 1. Not worth re-running: the Birago re-cut arm (3 boxes, net 0).

## Numbers of record
Openings of eval truth: tx_bench on birago1572-no87 (eval, the 12 tune lines) 26 times by script, declared in the PREREG; no frozen
confirm item read. Classify calls: 1 (7,990 boxes). Subagent calls: 0. Network: none. Cost: the worker cannot read its own cost
(get_session shows no cost field here); the parent fills the LEDGER cost from its get_session.
