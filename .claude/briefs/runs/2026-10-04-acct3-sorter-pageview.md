# SORTER-PAGEVIEW (account 3 worker) -- 4 Oct 2026 (account-3 orchestrator). START ONLY AFTER SORTER-NUDGE's ROOM done line
# (session_01VfJtieRPNJefEXz8ws4A61; same template file). If NUDGE is still live, wait via one send_later, never edit in parallel.
Owner's ask (4 Oct, Longlee larger view, tile f101v_L32_49): the neighbour lines above and below show as trimmed slices with separator
lines, which cut through ascenders/descenders; "can we just show the full graphic? I want to see clearly what's up above and below to tell
if it's a good or bad cut and then put the item in a pile."
Cause: each line is a separately deskewed strip (tools/sorter_recut.py shear); the larger view stacks the middle band (22-78%) of the
neighbour strips. Fix: show the ORIGINAL page region around the tile, continuous, with the tile's box drawn on it.
1. Build side (shared, tools/sorter_recut.py + the two targets' recut.py/build.sh): emit, per tile, its box in REGION coordinates (inverse
   of the shear: region y = strip y - HALF + trace(x) per column; give the 4 corners or a polygon, since a sheared box is a parallelogram)
   and publish a downscaled copy of the region image (e.g. long side <= 4000 px, JPEG, under the artifact size limits) as a supporting file.
   Offline test that a tile's region box contains its own ink (round-trip on the fixtures + one real tile per target).
2. tools/sign_sorter/template.html larger view: a "Whole page" view, DEFAULT ON when region data exists (toggle back to "Line strips"):
   the region image cropped around the tile (zoom slider = window size; default about 3 lines above and below), the tile's box drawn with
   the same corner brackets, no separators, no trimming. Keep the SORTER-NUDGE "Fix the cut" editing working in this view (edit the box on
   the page image; convert back to strip coordinates on save, or store region coords and let tools/sorter_apply_recuts.py handle both).
   Pages without region data keep the current view unchanged.
3. Browser test test_pageview.js + run_all.sh green with both real pages as EXTRA_PAGE; phone width check (no horizontal page scroll).
4. Rebuild + republish Longlee (https://claude.ai/artifact/CJoBEX8sy858LwSG868prC) and Pisany f.75 (https://claude.ai/artifact/VdudJ5ppAreb4Srd1HnWtR)
   same URLs, db kept: count the "moves" collection before and after publish; must be unchanged.
Model Opus 5.5. Cap USD 8, box 60 min (80% stop rule). ROOM claim/done via tools/room.py. Report: what the owner sees now, tests, URLs.
