# Sign sorter, Rayburn sheet (R9-RAYSORT, account 2, 6 Oct 2026)

For the owner. Built, not published: the account-3 orchestrator publishes it (capabilities {"db": {}}, as for
`ciphers/debosnys-1883/sorter/README.md`) and files the ASKS row. Why: R8-RAY2's two blind passes agreed on only 47.1%
of aligned positions (pass2/), over the 10% line, so by CLAUDE.md Usage 6 / TRANSCRIPTION.md the next transcription
step is a person settling the alphabet, not a third machine pass, and spec test 3 waits on it.

What is in it: `images/Rayburn-Cryptogram.jpg` (Schneier's 2006 850px file, byte-identical; no new request). 80 tiles =
pass2/reconciled.tsv's 80 tokens: rows main01-main10 (5,7,3,7,7,5,7,8,7,8 = 64) and the left and right margin columns
(8 + 8). Starting piles are the reconciled sign labels, case-sensitive (58 piles); families group a capital with its
small letter, and the margin signs in one `margin` family. `?-dot` (right 8) is renamed `hook-dot` (a pile id starting
with '?' would read as unsorted). No sign values or plaintext anywhere in this folder.

Cut (`build_inputs.py`, no network, no vision model, about 0.2 s): ink below grey 170 -> 8-connected components; the
rectangle round rows 1-2 (drawn later by a family member, per Schneier's post) dropped as thin pieces on its path; each
component put on the nearest row base line (two points per row read off the component overlay) and merged with the
components it overlaps in x, so a tile is the sign with its own underline or strike and any small sign written just
under it (k+r, A+m, R+H, a+v: a component starting within 12 px below a sign of the row above goes with that sign).
Margin components are merged in 2-D. Left out, as in R8-RAY2's N: the vertical note word beside right 2 ("Append"/
"Approved") and the circled mark below the grid. The script stops if any line's box count differs from the reconciled
count; it matched on all 12 lines without forcing. Pages are one strip per line (`pages/<line>.png`, the box union plus
8 px), so the context view shows the line itself; margin strips are tall columns.

Build: `sh ciphers/rayburn-2004/sorter/build.sh [out dir]` from the repo root -> `rayburn_sorter.html` (569 KB).

"Check these first" (`focus.tsv`, 40 tiles): every reconciled position where blind pass A (ciphertext.tsv) and blind
pass B (R8-RAY2) differ, hand-aligned from pass2/passA.tsv, passB.tsv and disagreements.tsv (`SPLITS` in the script),
each question saying what each reader saw. 7 of them are the white-out-adjacent margin tokens (copy_condition.tsv).

Preflight (pasted, R9-RAYSORT, 6 Oct 2026):
```
PASS template: ok, Fix the cut present, marker 2026-10-06.1
PASS answerable: 40 focus tiles, 58 named piles of 58, 0 unanswerable
PASS right line: 80 tiles; 0 tile(s) off the cipher lines, 12 of 12 listed lines have tiles; shape: 0 wide (>2.5x median 45 px), 0 strip-height boxes, 0 ink outside 3-60% of 80 measured; 0 = 0.0% (limit 5%) [list: ciphers/rayburn-2004/sorter/cipher_lines.tsv]
PASS contact sheet: 24 tiles beside their line strips -> ciphers/rayburn-2004/sorter/rayburn_sorter.preflight.png (seed 20261006; eye it before publishing)
preflight: PASS
```
Tile check (lane rule, 5+ random tiles against the line image): the contact sheet's 24 tiles eyed (every box on its own
sign, underline included); then 8 more drawn at random (random.Random(1006)) back onto the original full image and
opened: main07_03 k+r, left_08 *, main04_07 e, main08_08 D, left_02 %, main04_04 E, right_02 &/8, main06_05 Y -- all 8
on the sign their label names, the strip crops pixel-identical to the original (0 of 8 differ). Limits: main04_04 E's
box ends before the far right of its underline; main02_05 w's box takes in a short stretch of the rectangle's bottom edge.

Apply after the owner's pass: `ArtifactData list` for piles/moves/newpiles, then
`python3 tools/sign_sorter_apply.py --labels sorter/labels.tsv --db DIR --out sorter/settled_labels.tsv --summary sorter/summary.json`
(from the target folder). A settled label is a shape decision (grade I), not a value; it sets K (case-folded or not)
and the margin identities for spec test 3's matched control.
