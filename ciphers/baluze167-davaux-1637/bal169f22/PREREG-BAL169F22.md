# PREREG BAL169-F22 (14 Oct 2026, account 1, for LANE DEFAULT-A1-0640-14), written before any pass

Item: BnF Baluze 169 f.22r (canvas 48, ark btv1b9001488b), letter f.21-24 signed Bouthillier, Ruel 21 May 1639 (BAL169-SWEEP),
lines 1-4 of f.22r: cipher groups mixed with clear French, no interlinear gloss at 1000 px.
Crop: one native region (openapi.bnf.fr, 1285,1140,2950,810 of 4760x6850) -> tools/iiif_lines.py --image, 4 lines x 2 segments
(images/crops/b169f22r_L01-L04_s1/s2).
Passes: two blind Sonnet subagent calls (A, B), the passes/passA_prompt.txt prompt, one call per pass over the 8 crops, no reading or key
values given except the key table image's letter block. Reconcile with tools/reconcile_passes.py; split = 1 - agree/max(signs).
Gate: split <= 0.10 -> the agreed transcription stands, with the disagreements settled from the crops; split > 0.10 -> reconcile by eye from
the crops (this worker), every token settled by eye and not agreed by both passes is graded M (trailing ?).
Decode: key.tsv (Tomokiyo's published D'Avaux table) with tools/decode_key.py as a new decode.json job; no key edit. Letter signs are M
(the hand-dependence D4-B167 found). Clear words kept as w: tokens.
Success criteria for the report (not for novelty): count of cipher tokens and their grades; whether the numeral decode gives French that
joins the clear words on both sides. A decode that does not join is reported as such; no re-keying.
Priced: 2 pass calls + 1 reconciliation unit, cap 4.5.
