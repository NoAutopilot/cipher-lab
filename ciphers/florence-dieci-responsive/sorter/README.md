# Sign sorter, Florence Dieci c.127 (SORTER-FLORENCE, 3 Oct 2026)

For the owner, whenever there is time; nothing waits on it. Not yet published: the account-3 orchestrator publishes it, with capabilities
{"db": {}}, as for `../birago-fr3252-1571-72/sorter/README.md` (same build pattern).

It covers ASFi, Dieci di Balìa, Responsive filza 8 c.127 (DECODE R3766, 26 Dec 1430), the A2-FLO3 pilot stretch only:
the leaf's cipher lines 6-9 (crops `images/c127/c127b1_L01..L04_s1/s2`, here pages `c127_L01..L04`), 120 tiles cut from
`images/IMG_R3766_I23025_P.jpg`. Piles start from A2-FLO3's reconciliation (`passes/c127b1_recon.tsv`) of the two blind
passes (`passes/c127b1_passA.tsv`, `_passB.tsv`); the labels are the provisional ASCII names of `../c127_signs.md` plus
the reconciler's two additions `o/` (small o with the division mark, always together) and `s` (c-shaped form with a
tail). No sign values appear anywhere in this folder. Clear words written among the cipher are not tiles. The rest of
the leaf (~20 more cipher lines) is not here: it has no machine passes yet; add it the same way once it has.

**Before publishing:** the page embeds the strips. The R3766 scan came from DECODE (the record's own image route, see
NOTES.md Job 1); no RESTRICTED.md covers it and none was found in the folder, but the orchestrator checks the image's
terms before the page goes out (`tools/sign_sorter.py` docstring: never feed it restricted material).

Build (run from `ciphers/florence-dieci-responsive`):

    python3 sorter/build_inputs.py                # signs.tsv, labels.tsv, focus.tsv, pages/
    python3 ../../tools/sign_sorter.py --signs sorter/signs.tsv --labels sorter/labels.tsv --pages sorter/pages \
      --focus sorter/focus.tsv --title "Florence c.127 Sign Sorter" \
      --lede "Dieci di Balia, Responsive filza 8 c.127 (26 Dec 1430), cipher lines 6-9: the tiles two machine readers split on are in the box at the top." \
      --out <scratch>/florence-c127-sign-sorter.html

(27 piles, 120 tiles, 0 skipped, about 1.1 MB; built and rendered headless with no script errors on 3 Oct 2026.)

**"Check these first" box (`focus.tsv`, 15 tiles).** Every tile where the two passes did not both write the
reconciler's label, with both readings and the reconciler's (`·` = that pass wrote no sign there): the alpha/O and
alpha/x splits, t/4, z/2, q/F, p/D, the two `s` tiles, the lone `-` strokes the reconciler added, and `o/` where one pass
saw only the division mark. Disagreements in the s1/s2 overlap (signs read twice) are not tiles. A2-FLO3 counted 23
split positions of 134 on the raw passes; the box is smaller because the recon merged `o /` and dropped overlap signs.

**Tile boxes are approximate, and no eye checked them** (the brief allowed no image reads). The strip's ink threshold
is 90 (the paper is dark); signs are placed by a column ink profile inside each segment's own x range and fitted to
the recon's sign count; where a segment also holds clear words, the signs are taken as the last (or first) n x 75 px of
ink. Line 2 has faint stretches, so several of its tiles are halves of wider blobs and can be a position off; tiles
next to a clear word are the next most likely to be off. Use "Click shows context"; a badly cut tile goes to BAD-CUT,
not into a pile.

Export and apply, the same way as for Birago: `ArtifactData list` for piles/moves/newpiles, then
`tools/sign_sorter_apply.py --labels sorter/labels.tsv --db DIR --out sorter/settled_labels.tsv --summary sorter/summary.json`.
Then the full-leaf c.127 transcription against the settled labels (NOTES.md Verdict, ~$8).
