# Sign sorter, Birago 1572 short runs (NEVBIR-LOOKALIKE, 2 Oct 2026)

For the owner, when he has time. Nothing waits on it. It covers the two short 1572 runs, no.73 (f.144r, 90 signs) and
no.85 (f.168r + f.168v head, 121 signs): 211 tiles from the PUBLIC Gallica region images already on disk (BnF fr.3251,
ark btv1b9060248g, canvases 146, 171, 172), cut into one strip per line in `pages/`. Piles start from the reconciled
labels after the look-alike pass (`harvest/lookalike/<run>_passD.tsv`). No sign values appear anywhere in this folder.

Build (the account-3 orchestrator publishes it; workers do not):

    python3 harvest/lookalike_reconcile.py        # passD + the focus questions (already committed)
    python3 sorter/build_inputs.py                # signs.tsv, labels.tsv, focus.tsv, pages/
    python3 ../../tools/sign_sorter.py --signs sorter/signs.tsv --labels sorter/labels.tsv --pages sorter/pages \
      --focus sorter/focus.tsv --title "Birago 1572 Sign Sorter" \
      --lede "Nevers-Birago 1572, no.73 f.144r and no.85 f.168: the tiles two machine readers and a look-alike pass could not settle are in the box at the top." \
      --out <scratch>/birago-1572-sign-sorter.html

(run from `ciphers/nevers-birago-fr3251-1572`; 46 piles, 211 tiles, about 1.7 MB; built and rendered headless with no
script errors on 2 Oct 2026.) Publish with capabilities {"db": {}}, as for `ciphers/debosnys-1883/sorter/README.md`.

**"Check these first" box (`focus.tsv`, 13 tiles).** These are the tiles the look-alike pass left unsettled. Seven of
them are on f.168 and ask the same question: T24 or T83? Both earlier readers said T24; the look-alike reader said T83
at M, describing "two halves facing away, one bar through both". On f.178r/f.179r (GAPS4) a value-blind third reader
settled 19 of 21 splits between these two labels to T83. The owner's answer on these seven decides which f.168 sequence
gets tested (NOTES.md, NEVBIR-LOOKALIKE).

**Tile boxes are approximate.** Signs were boxed from a column ink profile, fitted to each passage's sign count
(`build_inputs.py` docstring). Where two signs touch, or one sign is in two pieces, a tile can be one position off.
Use "Click shows context" to see the tile on its line. A badly cut tile goes to BAD-CUT, not into a pile.

Export and apply, the same way as for Debosnys: `ArtifactData list` for piles/moves/newpiles, then
`tools/sign_sorter_apply.py --labels sorter/labels.tsv --db DIR --out sorter/settled_labels.tsv --summary sorter/summary.json`.
Then rebuild passD from settled_labels.tsv and re-run `decode_control.py` (NOTES.md has the commands).
