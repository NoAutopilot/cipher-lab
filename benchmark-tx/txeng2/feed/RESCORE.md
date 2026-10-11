# TXE2-FEED -- RESCORE (11 Oct 2026, 18:0x UTC by date -u)

**Measurement correction: box-to-position map fixed (off by one), not a new gate look** (S4 product, no gate). BOXMAP-RESCORE
(others), account-3 parent (session_0198Cv8ypBfBVfRToKVWx33M); read-free, no model call, nothing published.

The eval_heldout (no.87) feed names each sorter tile by the atlas box `--tile-map benchmark-tx/txeng/compare/box_pos.tsv` puts at its
position: the width-DP join that is one token off on f178v L13, L17, L21 and f179r L01-L03 (`benchmark-tx/txeng/RESCORE.md`). Re-built
with only the tile map changed:

    sh benchmark-tx/txeng2/feed/rescore_boxmapLA/build_la.sh      # (with the old tile map the same command reproduces the committed
                                                                  #  eval_heldout_feed/focus/feed_signals byte for byte)

The focus positions and questions do not change (the focus tier is latt + vote4, read-based). **3 of the 11 focus tiles named the
neighbouring sign's box** and would have shown the owner the wrong tile:

| position | question | tile before | **tile after** |
|---|---|---|---|
| f178v L13.20 | T18 or T92 or T98? (descender) | f178v_13_020 | **f178v_13_019** |
| f178v L21.21 | T26 / T45 / T66 / T76 / T86? (loop) | f178v_21_021 | **f178v_21_022** |
| f178v L13.7 | T70 or T84? (reads split) | f178v_13_007 | **f178v_13_006** |

Corrected files: `rescore_boxmapLA/eval_heldout_{feed,focus,feed_signals,tiles}.tsv`. f152r and Spinelli have no box map and are
unaffected. **Conclusion:** the feed's content and its predicted decisions to 2% are unchanged; any sorter page built from the committed
eval_heldout_tiles.tsv should use the corrected file (L13.20 is also the T98 tile TXE3-10's discriminator missed only because of the
same shift).
