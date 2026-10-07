# PREREG NZ-UNT27 (account 4), 7 Oct 2026, written before any blind pass ran and before the worker viewed the crops

Target: Hs 2398 opening 27 (media e0f9d823, native 4900x3064): the left figure's tablet (symbol columns) and the right figure's
scroll. R13-UNTOP's named side-step: a third sign context for symA after the opening-27 top inscription (0 symA, R13-UNTOP).
Crops: `tools/iiif_lines.py --image o27.jpg --region 1820,1100,200,580` (left tablet, R9-UNTB2 box) and `--region 2700,960,680,700`
(right scroll, R9-UNTB2 box), one crop per ink line; the worker checks the debug overlay and may widen a box only to include clipped
ink (logged), before any pass.
Control crop: opening 11 inscription line 4 (same box as PREREG-R13-UNTOP: `--image images/hs2398_opening11_inscription_leaf.jpg
--region 250,1020,1950,220`), holding bUNT8's symA at L4 tok5 and tok7.

Blind passes: two independent Sonnet subagents, each given only the neutrally lettered crops (control placed among them at a
position not first or last), no prior transcription, no Herzog, no NOTES.md, same instruction text as R13-UNTOP (ASCII letter/digit
for ordinary forms, else `SIGN:<description>`, list every unusual sign).

Gate 1 (sorter rule): tools/reconcile_passes.py on the two passes over the tablet + scroll lines after the same fixed
normalize step as R13-UNTOP (r13-untop/normalize.py, extended only by new class labels, applied identically to both passes).
Disagreement > 10% of aligned columns: stop after the passes plus one reconciliation unit; no third machine pass; name the sorter step.

Gate 2 (symA in a third context), identical to PREREG-R13-UNTOP: a tablet/scroll position counts as symA-like only if BOTH passes
flag a non-ordinary sign there whose description includes a hooked or looped top joined to a stem with a descender below the
baseline. Control (can fail): a pass that does not flag at crop-control at least one of the two symA positions as non-ordinary
(or describe the hook/loop+descender build there) cannot license "no symA on tablet/scroll"; its negative is a non-test.
Reported: symA-like count per pass, joint count, control hit/miss per pass. Worker's own eye recorded separately, never counted.
Herzog 1929 (p. 50, fol. 27 a) prints no text for these sheets ("ebensowenig auflösen", R13-UNTOP); no collation step.
Cap $3 (2 passes x ~1.5 would cross it with the Opus floor, so each pass is one call on all crops; reconciliation by the worker).
