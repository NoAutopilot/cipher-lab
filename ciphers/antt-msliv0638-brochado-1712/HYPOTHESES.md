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

## D4-BROC (8 Oct 2026): letter 134 doubled-loop sign
Image pass, not a family run. Control first: m0179-r1 pos 16 (Carta 80 copy single f -> s) read as one doubled-loop sign by
both blind passes; target m0276-r1 pos 10 read the same; m0275-r1 pos 8 read 55 (two digits) by both. Known-answer gate
G1 0.939/0.939 (gate 0.85), G2/G3 pass. Standing: `ff -> s`, grade M, 1 witness (PREREG-D4-BROC.md). m0275-r1 pos 31 and
m0276-r2 pos 16 match no known code (untested-by-this-tool beyond the image; LM run next).

## D4-BROLM (8 Oct 2026): LM-context rescoring of letter 134's 26 open tokens
Instrument: pt18 letter 4-gram Viterbi + key prior (PREREG-D4-BROLM.md, scripts/23_d4brolm_lm_rescore.py). Control first:
600 appendix windows at letter 134's own mask load (26/70), truth = Deciffrada letter. pt18: open-slot top-1 0.307 (gate 0.40;
shuffled null 0.112), keyed-override precision 0.214 (gate 0.60; decoder 0.782 vs prior-only 0.827). pt17: 0.322 / 0.206.
CONTROL BELOW GATE both gates, both corpora: target not run. Standing: non-test at this N (untested-by-this-tool), no value
changed; m0275-r1 pos 31 and m0276-r2 pos 16 -> no-key-material.
