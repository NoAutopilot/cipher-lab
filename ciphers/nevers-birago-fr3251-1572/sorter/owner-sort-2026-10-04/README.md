# Owner sort of the Birago "settle 24 look-alike signs" page, 4 Oct 2026

Exported from https://claude.ai/artifact/DHiLGFWiqrHxQYzLrFNh6s (private) after the owner said the sort was done
(4 Oct 2026). `db/` is the page's database as saved (moves, piles, newpiles); `labels_as_published.tsv` is the pile
each tile started in, rebuilt from the published page's data; `settled_labels.tsv` and `summary.json` are
`tools/sign_sorter_apply.py --labels labels_as_published.tsv --db db --out settled_labels.tsv --summary summary.json`.

488 tiles (f.117, f.144r, f.168): kept 277, moved 203, aside 5, bad-cut 3; 52 piles before, 105 after.
The owner's piles are a third reader, not ground truth (CLAUDE.md, TRANSCRIPTION.md): a split may be a real
homophone distinction or an over-split, and must be tested before any key value rides on it.


## Corrections after export

`corrections.tsv`: tiles the owner later moved out of a pile (one row each, with date). Apply them on top of
`settled_labels.tsv` before any use; UNPLACED means "not this pile, destination not given" (grade the tile M, unread).
