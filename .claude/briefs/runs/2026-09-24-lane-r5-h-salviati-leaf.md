LANE R5 WORKERS H1-H6 -- M35 SALVIATI: one leaf per worker with A's box-keyed method (Sonnet, cap $12 each; disk only, no fetches).
Owner's decision relayed by the parent at 20:16 UTC 24 Sept 2026: buy the remaining leaves (usage, not purchase). Common rules:
.claude/briefs/runs/2026-09-24-lane-r5-common.md. Target ciphers/fr2933-salviati-1525. Read NOTES.md "Leaves f.54v-f.57v (LANE R4 J)",
"Code+mark control curve (LANE R4 P)" and "Leaf f.55r priced, rest not bought (LANE R5)".
Your leaf is named in the spawn prompt. Jobs: H1 f.55r (boxes, strips and passA_f55r.tsv are already committed: do pass B and on only),
H2 f.55v, H3 f.56r, H4 f.56v, H5 f.57r, H6 f.57v.
Method exactly as J's f.54v: `glyphs/build.sh` to restore glyphs/crops/ if absent (atlas files must stay byte-identical; if a rebuild
differs, do NOT commit the atlas, use the committed files, and say so); `tools/glyph_atlas.py classify --page <leaf> --tsv <leaf>_boxes.tsv
--strips strips`; boxlist as f54v_boxlist_for_passes.tsv; pass A by you (passA_<leaf>.tsv), committed per six lines; pass B by ONE blind
Sonnet subagent (never opens passA*; given J's confusable-code pairs) writing passB_<leaf>.tsv to disk every six lines, you commit it;
`python3 recon_box.py passA_<leaf>.tsv passB_<leaf>.tsv recon_box_<leaf>`. Gate >= 80% base-code agreement. Pass -> settle disagreements
from the strips, write ciphertext_<leaf>.tsv (as ciphertext_f54v.tsv). Fail -> report and stop, no hand-settling.
Cost rule (RETRO f proposal 1): get_session on yourself after every six lines. If pass A alone has cost more than $6, start pass B only
if the remaining cap covers it; otherwise push and stop with a progress section, so no pass is lost at the cap.
NOTES.md section "Leaf <leaf> (24 Sept 2026, LANE R5 H<n>)". ROOM done: "for LANE R5: salviati <leaf> agreement <x>%, <tokens> sign
tokens, cost $<c>". No solving.
