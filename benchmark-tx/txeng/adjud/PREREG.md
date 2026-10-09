# PREREG TXE-K: stronger-model adjudicator of A/B reader splits (M19; LANE TX-ENGINEER, account 4; 9 Oct 2026, 07:5x UTC by date -u)

Pushed BEFORE any read. Binds with benchmark-tx/PREREG-txeng-2.md (units, blindness, Amendment: gate p < 0.01).

## Items (dev_tune, f178v L01-12): 36
Built by `tools/tx_adjudicate.py items` from harvest/f178v/passC_agreement.tsv (L01-10) and passC_L11-23_agreement.tsv (L11-12;
the brief named only the first, which stops at L10): one item = a maximal run of consecutive non-'agree' rows in a line
(44 rows -> 36 items: a split plus its adjacent gap row is one item, e.g. T29 vs "T24 then T88"; L11 31-32, A "T96 T95" vs
B "T95 T96", is one order item). `harvest/f178v/passC_disagreements.tsv` holds only L03 B25 X_S, already inside item 7.
Deviation from the brief, fixed now: agreed positions with merged_conf M/L (about 75 more) are NOT items -- both readers
gave the same cell, so there are not two candidates to adjudicate. Count 36, below the brief's "roughly 40-70".
The Sonnet-adjudicator baseline = passC's merged choice on each item (`sonnet` column of items_dev_tune.tsv).

## Packet (`tx_adjudicate.py packet`, seed 20261009)
Per item: a window of the native f182 source image (the image the harvest crops are cut from; the same pixels upscaled 2x),
+-4 median sign widths around the stretch, the line's band; a dark-blue bracket above and below the stretch. Box position
from the label-blind box<->position map (benchmark-tx/txeng/compare/box_pos.tsv). Deviation: the position is marked by the
bracket rather than by an ordinal ("between the 4th and 6th"), since a stretch can hold one or two signs; no value or code is
drawn. Options 1/2 = A's and B's cell sequences in seeded random order (key.tsv, never given to a reader); X_ labels shown as
"a mark matching no cell". 5 items per sheet image, 18 items per call: 2 calls per arm, plus sign_sheet_blind_1572.png.
Answer: 1, 2, a third cell (sequence), or ?.

## Arms
Fable subagent (`model: fable`) and one Opus 5.5 subagent (`model: opus`), identical call text, value-blind. Raw reads
committed and pushed before any score.

## Resolve (fixed now)
L = benchmark-tx/txeng/units/labels_dev_tune.tsv. An answer equal to passC's choice keeps L's own label there (L carries
later relabels, e.g. T50 -> X_CE); a different answer replaces L's item positions with the chosen sequence; ? keeps L.
Outputs: benchmark-tx/outputs/birago1572-no87/passS_adj_fable_dev_tune.tsv, passS_adj_opus_dev_tune.tsv.

## Gate (fixed now)
Per arm: `tools/tx_bench.py OUT --bench BENCHMARK-TX.tsv --item birago1572-no87 --paired benchmark-tx/txeng/units/labels_dev_tune.tsv`,
fixed > broken AND p < 0.01. Met -> eval_heldout once for that arm (the one eval look). Not met -> FAIL, no eval.
Secondary (not gating): item accuracy per arm and for the Sonnet adjudicator (`tx_adjudicate.py score`: an item's choice applied
alone to L is right when its line error count reaches the minimum of the two offered options); abstentions counted apart.
Prediction: with at most ~14 L errors on dev, few of them on item positions, p < 0.01 needs >= 7 fixed and 0 broken; a pass is
unlikely and a FAIL is the expected outcome unless the items hold most of L's errors.
Verdict wording if both fail: "adjudication by a stronger model does not beat the Sonnet third reader on this hand".
