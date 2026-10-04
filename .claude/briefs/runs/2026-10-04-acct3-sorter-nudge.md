# SORTER-NUDGE (account 3 worker) -- 4 Oct 2026 19:5x UTC (account-3 orchestrator)
Owner's ask (4 Oct, on the Longlee sorter's larger view, tile f101v_L03_04 in pile split-rare): "If you give me the ability, I can nudge the
'bad cut' to be good cuts." Build that in the shared sign sorter. Owner steer stands: sorting is optional, so keep this small and solid.
1. tools/sign_sorter/template.html, larger view (showCtx/drawLine): a "Fix the cut" button toggles edit mode. In edit mode the bracket box
   on the line canvas becomes editable: drag any edge or the whole box (pointer events, mouse AND touch, no page scroll while dragging),
   plus small nudge buttons (left edge -/+, right edge -/+, top -/+, bottom -/+, 2 source px per tap) for phones. "Save cut" writes db
   collection "recuts", doc id = tile id: {x, y, w, h} in the SOURCE line-image pixel coordinates the tile already uses (x,y,w,h of `it`),
   plus at, old box. "Cancel" restores. A saved recut: the tile shows a small "recut" badge, the bracket draws at the new box, the tile
   thumbnail in piles is redrawn from the line image at the new box (canvas) so the owner sees the fixed sign; it stays in its pile.
   If the tile was marked BAD-CUT, saving a recut offers "put it back in <home pile>" (one tap). Undo covers a recut.
   "Split here" is out of scope (one tile = one box); say so in the help text: for a box holding two signs, fix it to the first sign and
   mark the second with "Bad cut" as now.
2. tools/sign_sorter_apply.py: export recuts to recuts.tsv (tile, page, old x y w h, new x y w h, at); new tools/sorter_apply_recuts.py
   re-crops those tiles from the page/line images into the folder's tile dir (keeping the old crop as <id>.orig.jpg) and updates signs.tsv;
   --help and an offline test in tools/tests/.
3. Browser test tools/sign_sorter/browser_tests/test_recut.js (desktop drag, phone nudge buttons, save -> db doc, badge, undo, BAD-CUT
   tile put back), added to run_all.sh; all 16 tests pass on the fixtures AND with the Longlee page as EXTRA_PAGE. Update SYSTEM.md
   (tools/system_map_check.py) and the sorter README.
4. Rebuild and republish only the two open sorter pages, keeping their URLs and db: Longlee
   (ciphers/fr16106-vivonne-longlee-1579/sorter, https://claude.ai/artifact/CJoBEX8sy858LwSG868prC) and Pisany f.75
   (ciphers/fr16045-pisany-rome-1585/sorter, https://claude.ai/artifact/VdudJ5ppAreb4Srd1HnWtR) via their build.sh, capabilities {"db":{}}
   carried. The owner may be mid-sort on Longlee: the db persists across republish; before publishing, read the "moves" collection count
   and confirm it is unchanged after (nothing lost). Do not touch other sorter pages.
Model Opus 5.5. Cap USD 8, box 60 min (stop before starting a step that would cross 80% of either). ROOM claim/done via tools/room.py.
Report in a short paragraph: what the owner can now do, test results, and the two URLs.
