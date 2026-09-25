LANE R6 L2b and L5c -- fr2933-salviati-1525: finish the last two leaves (Sonnet, disk only, NO subagents). Common: 2026-09-25-lane-r6-common.md.
Intake gate (live, 25 Sept 16:18 UTC): "fr2933-salviati-1525: open (line 1) -- edition/page or full-text-search citation found within 6 lines" (exit 0).
Setup exactly as 2026-09-25-lane-r6-l-salviati-leaf.md "Setup" (restore glyphs/crops/, never commit atlas files, git status clean before work).
Measured this round: a pass-B subagent resumed over batches cost 9.6-16.3 USD a leaf; L1c's pass C done by the worker itself on 87 rows cost
3.19 USD. So YOU do the pass yourself, no subagent.
L2b f.56r (cap $8, box 50 minutes): passA_f56r.tsv is complete; passB_f56r.tsv covers lines 1-10 (277 rows, blind, pushed 9678dfb by L2's
subagent). You are pass B for lines 11-19: NEVER open passA_f56r.tsv (or recon/ciphertext files for f56r) until pass B is complete; read
f56r_boxlist_for_passes.tsv, strips/f56r_L11..L19.jpg and 5x recrops of every low-share or confusable box from glyphs/crops/f56r.png;
append to passB_f56r.tsv in the same columns, commit every three lines. Then recon_box.py, gate >= 80 percent, settle every disagreement
from 5x recrops (settled.tsv with reasons), ciphertext_f56r.tsv as ciphertext_f55r.tsv. Gate fail -> pass C on the disagreement rows as L1c did
(its crop_passC.py and settle_passC.py are in the folder), then majority vote.
L5c f.57v (cap $5, box 40 minutes): gate failed at 261/339 = 77.0 percent; pass C on the 78 rows of recon_box_f57v/disagreements.tsv exactly as
L1c did for f.55v (crop_passC.py / settle_passC.py with the leaf changed; read the calls blind to A and B), majority vote, three-way splits
settled from the crop, ciphertext_f57v.tsv. Note pass B found long plain-Italian stretches on lines 1, 16-18, 20: say in your notes whether
they look like a clear postscript, date or signature (quote what is legible), since plain text on a cipher leaf can be a crib.
Notes to leafnotes/<leaf>.md (append a section "(25 Sept 2026, LANE R6 L2b|L5c)"), not NOTES.md. ROOM done: "for LANE R6: salviati <leaf>
<agreement or majority>, <tokens> sign tokens". No solving.
