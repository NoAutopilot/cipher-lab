# PREREG BAL167-C275 (14 Oct 2026, account 1, for LANE DEFAULT-A1-1840-14), written before any pass

Item: BnF Baluze 167 f.135r (canvas 275, ark btv1b9001489r), inside the f.127 Memoire (Louis XIII / Bouthillier to d'Avaux, St Germain,
Oct 1637; continuation canvases 266-285). The run after the clear "qui est difficile a", about 22 groups over two lines, has no word
above it and no margin gloss (BAL-LOOKS, 1600 px, by eye). Optional lower-priority line: the c283 tail (`n 42 x 66 f / 19 71 96 n 76 6 46`),
only if spend is under 60% of the cap after c275.
Crop: one native region of c275 around the two lines (openapi.bnf.fr, info.json + 1-2 region requests) -> tools/iiif_lines.py --image,
line crops under 2400 px. Images untracked (manifest + regen command only).
Passes: two blind Sonnet subagent calls (A, B) with the passes/passA_prompt.txt prompt (blind: no key values beyond the table's letter
block; interlinear writing ignored). Split = cipher tokens differing / max cipher-token count (marks included).
Gate: split <= 0.10 -> agreed transcription stands, disagreements settled from the crops and graded M; split > 0.10 -> reconcile by eye
from the crops (this worker); every token not agreed by both passes is M (trailing ?).
Decode: key.tsv (Tomokiyo's published D'Avaux table) with tools/decode_key.py as a new decode.json job; no key edit. Letter signs are M
(the hand-dependence D4-B167 found); 1-bearing numerals M. Clear words kept as w: tokens.
Report criteria (not novelty): cipher-token count and grades; whether the numeral decode gives French that joins "qui est difficile a"
before it and the clear text after it. A decode that does not join is reported as such; no re-keying. No spec exists for this target
(judge_plaintext needs a spec): if no spec, say so; no grade is raised from a judge.
Priced: 2 pass calls + 1 reconciliation unit at ~1.2 each, cap 5.
