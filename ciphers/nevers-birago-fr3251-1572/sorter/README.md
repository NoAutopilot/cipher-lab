# Sign sorter, Birago 1572 short runs (NEVBIR-LOOKALIKE, 2 Oct 2026)

For the owner, when he has time. Nothing waits on it. Published 2 Oct 2026 by the account-3 orchestrator: https://claude.ai/artifact/QzrYKYmTB5xu4VZDaC7oba (private). It covers the two short 1572 runs, no.73 (f.144r, 90 signs) and
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

## Active sorter on the family atlas (TX-SORTER, 3 Oct 2026)

Built, not published (the account-3 orchestrator publishes). Same letters plus f.117, but tiles come from the family atlas
(`../atlas/`, TX-ATLAS-B72) instead of line strips, so a decision on one tile can move its whole atlas cluster in all
three letters, and `sign_sorter_apply.py` can write it back into `atlas/labels.json` for every sibling letter's next build.
Run from the repo root:

    A=ciphers/nevers-birago-fr3251-1572/atlas
    python3 tools/sign_sorter.py --atlas-topk $A/topk/no73.tsv $A/topk/no85.tsv $A/topk/fr3252-no77.tsv \
      --pages $A/pages.json --marks $A/marks.tsv --clusters $A/clusters.tsv --atlas $A/labels.json \
      --rank-lattice --rank-key ciphers/nevers-birago-fr3251-1572/harvest/key_1572_sheet.tsv --rank-lang it16dip \
      --title "Birago 1572 Sign Sorter" \
      --lede "Nevers-Birago 1572 family atlas: no.73 (f.144r), no.85 (f.168) and f.117. Start with the box at the top: the tiles whose answer moves the reading most. Moving one tile offers to move its whole atlas cluster, across all three letters." \
      --out <scratch>/birago-1572-sign-sorter.html

39 piles, 458 tiles (boxes whose atlas top-1 is a cipher sign), 100 atlas clusters, about 3.8 MB; publish with
capabilities {"db": {}}. The "Most useful first" box holds 20 tiles scored by `tools/key_decode_lattice.py` (reader
weight on the runner-up x plaintext letters that change when the tile is forced to it); through their clusters those
20 answers reach 71 tiles. 18 of the 20 are tiles where the lattice decode picks a different sign from the atlas top-1:
TX-DECODE found that decode raises true error on no.87 at lam=1, so the box asks the person, it does not suggest an answer.

Apply (decisions now include a `clusters` collection):

    python3 tools/sign_sorter_apply.py --atlas-topk $A/topk/no73.tsv $A/topk/no85.tsv $A/topk/fr3252-no77.tsv --db DIR --out settled_labels.tsv \
      --clusters $A/clusters.tsv --atlas-labels $A/labels.json --source "<date> sorter, no.73/no.85/f.117"

then rebuild the atlas topk (`glyph_atlas.py classify`, README in `../atlas/`) so every letter picks up the decisions.
The earlier line-strip sorter above (published 2 Oct) saves no clusters and applies exactly as before.
