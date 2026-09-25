LANE R6 L1-L5 -- fr2933-salviati-1525: one leaf per worker, box-keyed method (Sonnet, cap $12, box 60 minutes; disk only, no fetches).
Common: 2026-09-25-lane-r6-common.md. Intake gate: pasted into your spawn prompt (it must read exit 0; if it does not, stop).
Read NOTES.md sections "Leaves f.54v-f.57v (LANE R4 J)", "Leaf f.55v (LANE R5 H2)" and "Leaf f.55r (LANE R5 H1)" -- H1's is the method that
passed at 84.8 percent for about $7.
Jobs: L1 f.55v -- pass A is complete and pass B covers lines 1-15 (passB_f55v.tsv): resume pass B at line 16 (check the last line in the file
first; append, never overwrite), then gate and settle. L2 f.56r and L3 f.56v -- pass A is complete (passA_<leaf>.tsv, H3/H4, 24 Sept): do pass
B, gate, settle. L4 f.57r and L5 f.57v -- nothing done: classify, boxlist, pass A, pass B, gate, settle.
Setup: glyphs/crops/ is untracked; if absent, pip install numpy opencv-python-headless scikit-image scikit-learn pillow and run
`sh glyphs/build.sh` ONLY to regenerate glyphs/crops/*.png; then `git checkout -- glyphs/ f54r_boxes.tsv strips/` to restore every committed
atlas file and strip it overwrote (the rebuild drifts; never commit atlas files). Check `git status` shows nothing modified before you start.
Method: `tools/glyph_atlas.py classify --out glyphs --labels glyphs/labels.json --page <leaf> --tsv <leaf>_boxes.tsv --strips strips` (only
L4/L5); boxlist as f54v_boxlist_for_passes.tsv; pass A by you, committed every six lines; pass B by ONE blind Sonnet subagent (never opens
passA*; given J's confusable pairs eps/e, h/bh, tee/S4, psi/y, w/e, o./dl/h/tee/S7/#/+, Z/L, and the plain-cursive-mis-tagged-as-sign
pattern), resumed with SendMessage in batches of about five lines, each batch written to disk and committed by you before the next;
`python3 recon_box.py passA_<leaf>.tsv passB_<leaf>.tsv recon_box_<leaf>`. Gate >= 80 percent base-code agreement. Pass -> settle every
disagreement from 5x recrops (settled.tsv with a reason per row), write ciphertext_<leaf>.tsv exactly as ciphertext_f55r.tsv. Fail -> push,
report and stop, no hand-settling.
Cost: get_session on yourself after every batch; estimate pass B at your pass A's cost; at 80 percent of cap push a progress section.
Notes: do NOT edit NOTES.md (five workers share it). Write your section to `ciphers/fr2933-salviati-1525/leafnotes/<leaf>.md` headed
"## Leaf <leaf> (25 Sept 2026, LANE R6 L<n>)"; the orchestrator merges. ROOM done: "for LANE R6: salviati <leaf> agreement <x>%,
<tokens> sign tokens". No solving.
