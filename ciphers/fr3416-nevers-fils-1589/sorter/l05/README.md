# fr3416-nevers-fils-1589 L05 sign sorter (R10-NEVF2, 6 Oct 2026)

For a person's read of the eight L05 digits that two blind readers split on (NOTES.md "Remaining gaps", L05 row).
Not published by the builder; publish with the Artifact tool and capabilities {"db": {}} (account-3 orchestrator, per the ROOM flag).

- `signs.tsv` / `labels.tsv`: 95 tiles on the f43 region image. 87 are the R9-NEVF H digit boxes (`verify/l05_atlas/box_labels.tsv`,
  L02-L04 and L10), piled by their settled digit as examples of the hand; 8 are the L05 question tiles, starting in the pile of the
  committed digit (`f35r_ciphertext.tsv`). Box 28 (pos 15+16, fused in the glyph_atlas segment run) was cut in two by eye at x=2781
  (`f43_05_028a` = pos 15, `f43_05_028b` = pos 16); the person can re-cut with "Fix the cut".
- `focus.tsv`: one question per L05 position 4/5/7/13/15/16/17/20. Positions 4 and 7 ask "one looped 8, or two signs" in prose: there
  is no 0 pile because no H token on this leaf contains a 0 (the A1B-FILS-L05 class-gate finding), so the two-sign answer is "Fix the cut".
- Rebuild (byte-identical, checked 6 Oct 2026):
  `python3 tools/sign_sorter.py --signs signs.tsv --labels labels.tsv --pages pages.json --title "Nevers fils L05 Sign Sorter" --out sorter.html --lede "..." --focus focus.tsv --focus-note "..." --cipher-lines cipher_lines.tsv`
  (paths relative to this folder; the lede and focus note are as in NOTES.md "R10-NEVF2").
- `preflight.txt`: `tools/sorter_preflight.py sorter.html --cipher-lines cipher_lines.tsv`, PASS. `sorter.preflight.png` is its contact sheet.
- After the person sorts: `tools/sign_sorter_apply.py` on the db export; a tile the person moves changes nothing until a session re-grades
  the token under rule 4 (a person's read of the image is a transcription settlement, not a key value).
