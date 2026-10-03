# Sign sorter, Birago f.117r (SORTER-BIRAGO2, 3 Oct 2026)

For the owner, when he has time. Nothing waits on it. Not yet published: the account-3 orchestrator publishes it, with
capabilities {"db": {}}, as for `../nevers-birago-fr3251-1572/sorter/README.md` (same build pattern).

It covers fr.3252 f.117r (no.77, Birago to Nevers, 13 Mar 1572), the ten-line cipher block: 277 tiles from the PUBLIC
Gallica region image already on disk (BnF fr.3252, ark btv1b9060232m, canvas 118, region 4380,1400,3150,1300;
`images/f117/src_*.jpg`), cut into one strip per line in `pages/`. Piles start from the 2-of-3 labels after the look-alike
pass (`harvest/f117/la/passD.tsv`; '?' becomes UNREAD). No sign values appear anywhere in this folder, only sheet labels.
f.47r (no.30) is read twice but not settled (257 split tiles wait for a third reader, NOTES.md Escalation); add it here
the same way once it has a look-alike passD.

Build (run from `ciphers/birago-fr3252-1571-72`):

    python3 sorter/build_inputs.py                # signs.tsv, labels.tsv, focus.tsv, pages/
    python3 ../../tools/sign_sorter.py --signs sorter/signs.tsv --labels sorter/labels.tsv --pages sorter/pages \
      --focus sorter/focus.tsv --title "Birago f.117r Sign Sorter" \
      --lede "Birago to Nevers, 13 Mar 1572, BnF fr.3252 f.117r: the tiles two machine readers and a look-alike pass could not settle are in the box at the top." \
      --out <scratch>/birago-f117-sign-sorter.html

(42 piles, 277 tiles, 0 skipped, about 2.7 MB; built and rendered headless with no script errors on 3 Oct 2026.)

**"Check these first" box (`focus.tsv`, 12 tiles).** `harvest/f117/la/focus.tsv` with its ids renamed to this folder's
tile ids (`f117c_L07_13` -> `f117_L07_13`). These are the tiles the look-alike pass left unsettled: mostly the hash pair
T60/T86 (five tiles), the barred-p group T95/T51/T65, the x forms T81/T83, and three off-sheet X_NEW questions.

**Tile boxes are approximate.** Signs were boxed from a column ink profile over each line's own core rows (the lines are
skewed and the bands overlap their neighbours, so the line is tracked left to right from its manifest centre) and fitted
to the line's sign count (`build_inputs.py` docstring). Boxes were checked by eye on an overlay of all ten lines; where
two signs touch, or one sign is in two pieces, a tile can be one position off. Use "Click shows context" to see the tile
on its line. A badly cut tile goes to BAD-CUT, not into a pile.

Export and apply, the same way as for Debosnys: `ArtifactData list` for piles/moves/newpiles, then
`tools/sign_sorter_apply.py --labels sorter/labels.tsv --db DIR --out sorter/settled_labels.tsv --summary sorter/summary.json`.
Then rebuild passD from settled_labels.tsv and re-run `harvest/f117/la/run_tests_3r.sh` (NOTES.md has the commands).
