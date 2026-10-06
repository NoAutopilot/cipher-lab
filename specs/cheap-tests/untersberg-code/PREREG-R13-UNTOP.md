# PREREG R13-UNTOP (account 4), 6 Oct 2026, written before any blind pass ran

Target: Hs 2398 opening 27 (media e0f9d823, native 4900x3064), the 3-line painted inscription on the R page (pencil p. 53, "27").
Crops (tools/iiif_lines.py --image o27.jpg --region 2500,60,2300,600 --lines-per-crop 1): o27_L01..L03.
Control crop: opening 11 inscription line 4 (tools/iiif_lines.py --image hs2398_opening11_inscription_leaf.jpg --region
250,1020,1950,220), which holds two confirmed symA instances (bUNT8: L4 tok5, L4 tok7).

Blind passes: two independent Sonnet subagents, each given only four neutrally named crops (A = o27 L2, B = control, C = o27 L1,
D = o27 L3; the subagent is not told which is which or that one is a control), no prior transcription, no Herzog, no NOTES.md.
Each pass labels every sign with an ASCII letter/digit when it is an ordinary letter form, else `SIGN:<description>`, and lists
every sign it judges unusual (ligature, hook, loop, mirrored or non-alphabetic form).

Gate 1 (sorter rule, TRANSCRIPTION.md / CLAUDE.md Usage 6): tools/reconcile_passes.py on the two passes over the three o27 lines.
If disagreement > 10% of aligned columns, stop after the passes plus the one reconciliation unit already priced; no third machine
pass; name the sorter step.

Gate 2 (symA in a second context). A position on o27 counts as symA-like only if BOTH passes flag a non-ordinary sign there whose
description includes a hooked or looped top joined to a stem with a descender below the baseline (bUNT8's construction).
Control (can fail): a pass whose output does not flag, at crop B, at least one of the two symA positions (the 'v'-like 5th and
'p'-like 7th tokens of that line) as non-ordinary or describe the hook/loop+descender build there, cannot license "no symA on
o27"; that pass's o27 negative is reported as a non-test. Reported: symA-like count on o27 per pass, joint count, and control
hit/miss per pass. The worker's own eye on the native crops is recorded separately and never counts toward the gate.

Collation against Herzog 1929's fol. 27 apparatus: read only after the reconciled o27 text is committed.
