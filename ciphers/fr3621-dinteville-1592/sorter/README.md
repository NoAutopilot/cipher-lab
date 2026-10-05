# Sign sorter, Dinteville f.23r (DIN-SORTER, 3 Oct 2026)

**What the owner does (two sentences).** Open the published sorter and drag each tile of the seven cipher rows into the
pile of the sign it is (merging piles that are one sign, splitting 0 / 0' / o and v / v' / D where they differ, BAD-CUT
for a badly cut tile), starting with the "Check these first" box. Nothing waits on a deadline; when done, a session
exports the piles and applies them (below), and the f.23r passes are then read against the settled alphabet.

Not yet published: the account-3 orchestrator publishes it, with capabilities {"db": {}}, as for
`../../birago-fr3252-1571-72/sorter/README.md` (same build pattern). Built by script only, no vision call.

It covers BnF fr.3623 f.23r, a Dinteville cipher slip with an interlinear Italian decipherment (DIN-3623): 303 tiles in
seven cipher rows R1-R7 (39, 45, 43, 56, 52, 42, 26), cut from the native Gallica region already on disk
(`f3623/src_ark_12148_btv1b525245007_f55_560_1780_2950_1560.jpg`, ark btv1b525245007, canvas 55). The brief said six cipher
lines; the row profile finds seven cipher rows (the shorter R7 below a gap), as DIN-23P's own selection sheet counted.
Cipher rows are told from gloss rows by script (dense ink columns) and the assignment is checked against the DIN-23P
pilot strips, which match R4 and the gloss row above it (`build_inputs.py` docstring). No sign values appear anywhere in
this folder, only sheet labels.

Build (run from `ciphers/fr3621-dinteville-1592`):

    python3 sorter/build_inputs.py                # signs.tsv, labels.tsv, focus.tsv, pages/, rows.json
    python3 ../../tools/sign_sorter.py --signs sorter/signs.tsv --labels sorter/labels.tsv --pages sorter/pages \
      --focus sorter/focus.tsv --auto-clusters 6 --title "Dinteville f.23r Sign Sorter" \
      --lede "Dinteville cipher slip with an Italian gloss, BnF fr.3623 f.23r: the tiles two machine readers split on in row 4 are in the box at the top; every other row starts unread, grouped by shape." \
      --out <scratch>/din-f23r-sign-sorter.html

(14 piles, 303 tiles, 0 skipped, 17 provisional shape clusters, about 2.3 MB; rendered headless on 3 Oct 2026 with 325
image elements and no script errors; `tools/tests/test_sign_sorter.py` and `test_sign_sorter_apply.py` ALL PASS.)

**Seeds.** Only R4 has machine reads (DIN-23P passes A and B, `f3623/pilot/passA.txt`, `passB.txt`). The 35 positions
where A and B agree are seeded with that label (a 7, 0 6, y/c/0' 3 each, ...); the 21 where they split are UNREAD and in
the "Check these first" box (`focus.tsv`, both readings quoted: mostly + vs t, c vs 9, z vs Z, 0 vs 0'). The other six
rows start UNREAD, grouped by `--auto-clusters`. A and B are joined on their segment overlap and aligned with the pilot's
own functions; pass A's 'plus' is normalised to '+' first.

**Tile boxes are approximate.** Signs were boxed from a column ink profile over each row's core (+-30 px of a line tracked
along the -0.055 slope). R4 gave 45 raw blobs and was fitted to the 56 aligned A/B positions by halving the widest blobs,
so an R4 seed can sit one tile off its sign (the 56 include positions only one pass saw); treat R4 seeds as suggestions.
The other rows are not fitted to any count, so touching signs can share a tile (expect more signs than tiles). Use
"Click shows context" to see the tile on its row; a bad cut goes to BAD-CUT, not into a pile. The boxes were not checked
by eye (the brief allowed no vision call).

Export and apply, as for Birago: `ArtifactData list` for piles/moves/newpiles, then
`tools/sign_sorter_apply.py --labels sorter/labels.tsv --db DIR --out sorter/settled_labels.tsv --summary sorter/summary.json`.
Then the f.23r passes run against the settled labels and the 6-line (7-row) alignment follows (NOTES.md Remaining gaps).


Published 3 Oct 2026 ~10:47 UTC by the account-3 orchestrator (private Artifact, capabilities {"db": {}}): https://claude.ai/artifact/RxURcDEas5VU11B95kVoJo (ASKS 112).

**Rebuilt 5 Oct 2026 (A4-SORTFIX, account 4): https://claude.ai/artifact/JXsSNDyRLhZT8AGoCMHmyD** (private Artifact, capabilities
{"db": {}}). The first page's 21 check-first tiles asked "which sheet label?" but only 14 piles existed (no 0', v', o, D, t, Z ...),
so they could not be placed (ROOM.md 5 Oct 22:52 flag). `sorter/add_cards.py` adds one grey **name card** per missing label -- every
f.130 sheet label (f130/inventory.tsv) and every label a check-first reader offered: 1 m f w v' p z D al T h o div r . NEW:e-hook
NEW:N-like 3 Z t -- and rewrites focus.tsv as focus_cards.tsv ("readers split 9 / 0'. Tap the 9 pile or the 0' pile ..."). Build:

    python3 sorter/add_cards.py
    python3 ../../tools/sign_sorter.py --signs sorter/signs_cards.tsv --labels sorter/labels_cards.tsv --pages sorter/pages \
      --focus sorter/focus_cards.tsv --auto-clusters 6 --title "Dinteville f.23r Sign Sorter" --focus-note "..." --lede "..." --out <scratch>/din-f23r-sign-sorter.html

(34 piles, 323 tiles = 303 signs + 20 cards, 2.5 MB; headless Chromium: R4.2 moved into the 0' pile, no page errors.) Sids of the 303
signs are unchanged. **A name card is not a sign: drop every `card_` sid from the applied output** (`sign_sorter_apply.py` writes it like
any tile). The old page (RxURcDEas5VU11B95kVoJo) belongs to another account and could not be read from account 4, so it was not replaced.
