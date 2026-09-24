LANE R5 WORKER A -- M35 SALVIATI f.55r: price the code+mark capture at its first leaf (Sonnet, cap $8; disk only, no fetches).
Target: ciphers/fr2933-salviati-1525. Common rules: .claude/briefs/runs/2026-09-24-lane-r5-common.md. Read NOTES.md sections
"Leaves f.54v-f.57v (LANE R4 J)" and "Code+mark control curve (LANE R4 P)". Why: the code+mark homophonic model (cm) reads a matched
control only at ~2,800 sign tokens; f.54r-v gave 719; f.55r-f.57v would supply the rest. This worker prices one leaf before the lane buys five.
Method exactly as J's f.54v (no new method, no new scripts): `glyphs/build.sh` to restore glyphs/crops/ if absent (check byte-identity of
the committed atlas files as J did); `tools/glyph_atlas.py classify --page f55r --tsv f55r_boxes.tsv --strips strips`; boxlist for passes
as f54v_boxlist_for_passes.tsv; pass A by you (passA_f55r.tsv); pass B by ONE blind Sonnet subagent (never opens passA*; given the
confusable-code pairs J listed; writes passB_f55r.tsv to disk; you commit it); `python3 recon_box.py passA_f55r.tsv passB_f55r.tsv
recon_box_f55r`. Gate >=80% base-code agreement. Pass -> settle disagreements from the strips, write ciphertext_f55r.tsv (as
ciphertext_f54v.tsv). Fail -> report and stop, no hand-settling.
Commit and push after boxes, pass A, pass B, settling. Check your cost (get_session on yourself) after each step.
Report in ROOM done: "for LANE R5: salviati f55r agreement <x>%, <tokens> sign tokens, <types> types, cost $<c>". NOTES.md section
"Leaf f.55r (24 Sept 2026, LANE R5 A)". No solving.
