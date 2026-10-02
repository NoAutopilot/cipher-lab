# antt-msliv0638-brochado-1712 -- hypotheses and data conflicts (append-only)

Opened 2 Oct 2026 (NEXT-BRO). Rule 4: two period decipherments that disagree on one code are a data conflict, recorded
with their witnesses, never settled by the more frequent value alone. Family runs (tools/family_run.py) would append below.

## Code 9 vs 9± (NEXT-BRO, 2 Oct 2026)

| code as transcribed | value | witness (leaf / entry / idx) | how read | strength |
|---|---|---|---|---|
| 9± | r | m0280 Carta 13 idx80 and idx83 (`y.11.7.9±.2.7.9±` = "a perder") | gloss, letter for letter | firm (2) |
| 9 | i | m0290 Passage 2a idx82 (`8.14.2.22.4.55.15.g.9.5.d.7.f` = "indisposicoes") | gloss, letter for letter | firm (1) |
| 9 | o | m0292 Carta 101 idx29 (entry's last tokens `2.23.10.9` do not match the gloss's "de Londres") | masked alignment only (align/align_mask_9.tsv) | weak (1) |
| 9 | ? | m0275-r1 pos 2 (letter 134, Span A pos 2) | no gloss | the candidate token |

Standing: treated as two codes. `key.tsv`: `9± -> r` grade C (unchanged), `9 -> i` grade M (added 2 Oct 2026). AX2-BRO4
Step 2 stripped the ± and reported `9 -> r` at 2/4; those two agreeing occurrences are the two 9± tokens, so that figure
does not support r for the bare glyph. What would settle it: an image comparison of the 9± glyphs on m0280 against the
bare 9 on m0290, m0292 and m0275 (folded into the planned doubled-loop image pass, NOTES.md "Remaining gaps").
