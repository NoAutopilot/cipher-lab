# Which shorthand? owner page (SHORTHAND-PAGE, 5 Oct 2026, account 3)

Published https://claude.ai/artifact/DTfwuc4PoX3kjNrin5pXLs (private, db + user; board card `arm-which-shorthand`).
Armstrong's mark types R1-R7 beside five period alphabets under blind labels A-E (key: ../../NOTES.md, "Owner which-shorthand
family check"). The page is built, not committed.

| file | what |
|---|---|
| `exemplars.tsv` | three tiles per mark type: line and index on the worker's contact sheet (sorter tiles of the line ordered by run, x) |
| `tiles.py` | cuts padded one-mark tiles from `../signs.tsv` boxes on the NARA frames, neighbour ink masked |
| `cells.py` | per-letter row grid of each alphabet table (by eye from ruler overlays), `cut_cells(key)` |
| `family_template.html` | the page; `build_family_page.py` embeds tiles and cells as data URIs |

Build (repo root, disk only): `python3 ciphers/armstrong-madison-1808/sorter/family/build_family_page.py OUT.html`
Read answers: ArtifactData `list` of `picks` (doc `R1-A`: pick = cell index or -1 for nothing similar, letter) and `verdicts`
(doc `A`: same / maybe / no / cant, note). One reader's likeness judgement, not a match.
