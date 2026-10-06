# Baluze 170 f.228r-v sign sorter (R12A-BALS, 6 Oct 2026)

For the owner, via the account-3 orchestrator (publish with capabilities `{"db": {}}`; a worker does not publish).
Page: `out/baluze170_f228_sorter.html` (1.1 MB, 258 tiles, 41 starting piles, 124 "Check these first" questions).
Rebuild (no network, repo root): `bash ciphers/baluze167-davaux-1637/sorter170/build.sh` (writes pages/, data.json and the
page; pages/ and the data JSON are not committed, the page embeds them).

What it holds: the 13 cipher lines of BnF Baluze 170 f.228r (4 lines) and f.228v (9 lines), Chavigny to d'Avaux, Amiens
25 Aug 1640, cut one sign per tile from the five Gallica native regions already in `../images/crops/` (D1-BAL170, D1-BAL170B).
Clear words, the period after 76 on f.228v b_L05 and the end-of-line dashes are blanked to the paper tone (x-ranges in
`build_inputs.py` CIPHER, eye-set on 400 px boundary panels). Starting piles come from the reconciled sheets
`../passes/reconciled_b170f228{r,v}.tsv`: one tile per digit, the accent / diaeresis / bar of a number drawn on its last digit
(`marks.tsv`, so the tile is cut round digit + mark and 6 and 6' can be told apart on the tile itself); a letter sign is one
tile, or several pieces in the same pile when it is wider than 2.5 digits (the preflight's merged-sign line), to be joined
with Fix the cut.

Focus box (124): u4 / 4u (11), q vs 9 (6), ff (2), hook / wave / v (9), y+ (5), h (7), ll / m4 / gam / g+ (12), pieces of a
wide letter sign (10); every 6, marked or not (35: the curled top of this hand's 6 and descenders from the line above mimic an accent, D1-BAL170B);
every other column the reconciled sheets mark "?" (19); tiles no reader column lined up with (8: fragments, pen strokes).

Known faults of the starting piles (eye-checked by R12A-BALS on all 13 lines at 0.8 scale and on the 24-tile contact sheet:
22/24 contact tiles in the right pile, the two wrong ones in the regions below):
- f.228v a_L01 around "16 m4 44'" (x 1940-2240): a pen stroke from the line above crosses the signs; boxes there are fragments.
- f.228v b_L04 "u4 65' p h" (tiles 04-08): the second u4 is cut as u + 4 and the next three tiles carry their left
  neighbour's label (the 4-piece sits in 6, the 6 in 5', the 5 in p); the h after p is right again.
- f.228r b_L02 end "51 w": the w is in pieces and the starting labels of 5 and 1 may be shifted by one.
- f.228r c_L01 and f.228v a_L02 are faint lines; their tiles look grainy at the sorter's contrast.
A PASS of `tools/sorter_preflight.py` (`preflight.txt`) says the page can be answered and shows cipher signs, never that
the starting piles are right. After the sort: `tools/sign_sorter_apply.py`, then the provisional f.228 decode with key.tsv.
