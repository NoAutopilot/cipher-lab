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

## Code 24: h vs e (V-BRO24, 9 Oct 2026)
Verifier-style key-value check, separate from the solver BRO-123. Every witness below is the same series and direction as
letter 134 (Brochado, London, to the Utrecht plenipotentiaries; appendix entries 1712 to Carta 123 of 7 Nov 1713; letter
134 is 22 Oct 1713, between Carta 110 and Carta 123). No witness from another sender, recipient or period.

| value | witnesses (leaf / entry, context in the gloss) | how read | n |
|---|---|---|---|
| e | m0284 Carta 71 (grand[e] patranha), m0284 Passage 3a (est[e] velhaco), m0285 Passage 4a, m0286 Carta 74 x2 (esp[e]ro, d[e]stes), m0287 Carta 79 x2 (est[e] v[e]lhaco), m0289 Carta 92 (velhaco [e]stá), m0290 Carta 93 ([e]stá), m0290 Passage 2a x2 (s[e]u, n[e]sse), m0291 Passage 3a (princip[e] de Hanover), m0294 Carta 110 (est[e] velhaco) | gloss, masked DP alignment + key-decoded context (code24_attest.tsv) | 13 |
| e | m0253-m0254 body copy of Carta 123 | BRO-123 masked alignment (carta123_attest.tsv), 9 C + 3 M | 12 |
| a | m0287 Carta 79 (Caminho p[a]ra; 'pera' would read e) | gloss | 1 |
| a | Carta 123 body copy | BRO-123, M | 1 |
| h | m0284 Passage 2a ("Se lhe fôr de mim"; the cipher decodes s e d ? s o e s d e, not the gloss letter for letter) | DP placement only | 1 |
| ? | m0286 Carta 74 pos 52, m0289 Carta 92 pos 37, m0290 Passage 2a pos 91 | no stable placement | 3 |

Why key.tsv held h at n=2: scripts/03_align_pairs.py counts a code run only when its span has exactly as many letters as
tokens; 16 of the 18 appendix uses of 24 sat in runs that failed that test (the key totals 381 tallied uses out of about
1,500 cipher tokens). A tally bug, not a homophone. Glyph: 24 on m0290 Carta 93 line 1 and on letter 134 m0275 line 3
(images/broc/m0275_L03.jpg, `55.12.7.3.19.14.x.24.12.y`) is the same two-digit form, distinct from 21 on the same Carta 93 line.
Standing: `24 -> e`, grade C (25 of 31 tagged uses e, 0.81; key builder rule C at >= 0.65 and n >= 2), same date and
direction as letter 134, so C applies in letter 134. The single h witness is logged here and not settled by count alone:
its gloss does not match its cipher letter for letter, so it is not an equal-strength period reading of 24.

## BRO-CT (9 Oct 2026, account 2; for LANE FAMILY-A2m): crossed-t `t` = letter 134 m0276-r2 pos 16, value l?
| hypothesis | instrument | control | target | result |
|---|---|---|---|---|
| letter 134's unkeyed sign is the appendix crossed-t (3 witnesses, gloss l) | 2 blind Sonnet looks, 3 t + 4 decoys shuffled (PREREG-BROCT.md, b9250bc79) | decoys in each look | look A: same = T1, T2 (T3 unsure), no decoy; look B: same = T1, T2, T3 + decoy D3 (slashed f, s) | NOT SUPPORTED (gate: >=2 t and no decoy in both looks) |
| t = l at all 4 occurrences | decode_key.py --try t=l, lm pt18 (broct_try.txt) | tool's own null (positions p95 -14.9, value class 9.4) | statistic -18.7 bits vs runner-up M | reject (non-blind); t=m undecided (+9.4 over NULL, below rule); avalanche top for t is M, not accepted |
Standing: no value for letter 134 pos 16; key.tsv unchanged. The appendix t still reads l by gloss in all three appendix contexts ("pelo qual" x2, "velhacos"); the LM pooling of those with letter 134 ("...tal[?]ento...") does not favour l, and the LM-context instrument failed its own known-answer control on this volume (D4-BROLM), so the --try verdict is weak either way.
