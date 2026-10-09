# TXE-D: tile rendering sweep (LANE TX-ENGINEER round 2; ideas O1 O2 O4 M4; 9 Oct 2026, account 4, Opus 5.5)

**Verdict: FAIL at the read-free proxy gate -- no setting earns the read.** Best setting sr4 (LANCZOS 4x): atlas top-1
err_true 0.192 vs plain 0.216 on dev_tune, fixed 9 broken 1, sign test p 0.0215 > 0.01 (registered gate, PREREG-txeng-2
Amendment). No blind read was run, so no passK file exists and eval_heldout was not looked at (eval looks by this
instrument: 0).

## What was built
`tools/tx_prep.py` (`render`, `proxy`, `lines`, `settings`; `--help`), test `tools/tests/test_tx_prep.py` (offline, ok).
Settings and parameters: `python3 tools/tx_prep.py settings`; every tile's manifest carries the source box, the tile box,
the scale and the setting's parameters. combo = tight + stretch at tight's own 2x (the "sr2" of the combination is
tight's 2x, not a second one; fixed before any score).

## Proxy (read-free; never saw a truth file until the TSVs were committed in ddd9ee5ab)
    A=ciphers/nevers-birago-fr3251-1572/atlas
    python3 tools/tx_prep.py render --page ciphers/nevers-birago-fr3251-1572/harvest/f178v/src_ark_12148_btv1b9060248g_f182_1703_848_2900_3452.jpg \
        --boxes $A/signs.tsv --page-name f178v --lines 1-12 --median-h 68 --out TILES --setting plain --setting tight ... (13 settings)
    python3 tools/tx_prep.py proxy --tiles TILES --setting ... --atlas $A --out benchmark-tx/txeng/prep/proxy \
        --holdout f178r_ --holdout f178v_ --holdout f179r_
    python3 tools/tx_bench.py proxy/<S>_bench.tsv --bench BENCHMARK-TX.tsv --item birago1572-no87 --paired proxy/plain_bench.tsv

Boxes: the atlas's own 364 boxes of f178v L01-12, unchanged (box count = signs.tsv's exactly; no re-segmentation, so the
5% rule is met trivially). Each rendered tile is re-binarised (one rule for every setting, closing kernel scaled with the
tile scale), the components with >= half their pixels inside the source box make the 48x48 bitmap and the size ratios,
those rows replace the stored ones in a temporary atlas copy, and `glyph_atlas.py classify --topk 3` runs with all of
no.87 held out. Box -> position: `tx_compare.box_map` (label-blind width DP, atlas/no87_map.py costs) against the line
read; it depends on box widths only, so it is identical for every setting. Top-3 share: the k1 alignment of tx_bench,
truth in any of k1-k3 (scratch computation over tx_bench.align, read after the commit).

| setting | top-1 err_true (dev_tune, 343) | fixed / broken vs plain | p (sign test) | truth in top-3 | thin-tercile errors |
|---|---|---|---|---|---|
| plain (control) | 0.216 (74) | -- | -- | 0.866 | 28 |
| tight (O1) | 0.195 (67) | 9 / 2 | 0.0654 | 0.866 | 28 |
| gamma=0.5 (O2) | 0.233 (80) | 8 / 14 | 0.2863 | 0.845 | |
| gamma=0.7 (O2) | 0.216 (74) | 8 / 8 | 1.0000 | 0.869 | |
| stretch (O2) | 0.201 (69) | 8 / 3 | 0.2266 | 0.860 | |
| thicken=1 (O2) | 0.210 (72) | 8 / 6 | 0.7905 | 0.866 | |
| sr2 (M4) | 0.198 (68) | 8 / 2 | 0.1094 | 0.857 | |
| sr4 (M4) | 0.192 (66) | 9 / 1 | 0.0215 | 0.869 | 25 |
| combo (O1+O2+M4) | 0.195 (67) | 10 / 3 | 0.0923 | 0.860 | 26 |
| invert (O4) | 0.216 (74) | 0 / 0 | 1.0000 | 0.866 | non-test: binarised on 255 - x, identical by construction |
| channel=R/G/B, sep, false (O4) | not run | -- | -- | -- | non-test: the source is single-channel (Gallica native for f182 is mode L; the RGB line crops have R = G = B, max abs(R - B) = 0) |

err_true counts include tx_bench's 4 insertions (constant across settings: the box set is fixed). Gamma convention:
out = 255 (in/255)^(1/G), so G < 1 darkens.

Taxonomy (`tools/tx_taxonomy.py`, benchmark-tx/txeng/prep/taxonomy_proxy.md) on plain vs sr4/tight/combo: the gains sit
in the heavy and mid stroke terciles (plain 20/21 -> sr4 17/19, tight 18/16); the thin tercile, the class the
instrument was registered against (class 3), barely moves (28 -> sr4 25, tight 28, combo 26). Band-cut positions do not
improve (15 -> 16). So the upscaling gain the proxy sees is in the binariser's bitmap on ordinary strokes, not on faint
strokes.

Caveat on the proxy itself: the atlas reader binarises, so it is blind to anything a setting does below the threshold
(darkening a stroke already above it), and LANCZOS upsampling adds no information to the page, only a smoother mask.
A vision reader may respond differently; the registered gate decides that the read is not spent here.

## The read
Not run (gate not met). Reader task text: none sent. Vision calls: 0.

## Follow-ups (one line each, not started)
- sr4 at 9/1 (p 0.02) is the strongest sub-gate signal; if the lane wants it, a read-free replication on another hand's
  known-answer item (not no.87 eval) is the cheap next look, not a read.
- Colour (O4) needs a colour source: Gallica serves this manuscript single-channel; a colour scan would come from the BnF
  reproduction service, not the IIIF endpoint.

## Cost
Calls 0 vision; run 07:21-07:34 UTC by date -u; cost: see the lane's get_session.
