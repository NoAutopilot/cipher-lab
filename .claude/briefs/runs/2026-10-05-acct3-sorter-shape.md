# SORTER-SHAPE (written by account 3, 5 Oct 2026, for account 4). Opus 5.5. Cap $8, box 90 min. Public repo (tools only).

Owner, 5 Oct 2026, on Longlee "Fix the cut": the box is a sheared parallelogram (it follows the slanted line trace), and
on a wide looped sign it cannot cover the sign without clipping in the neighbour's ink. He asked for more control than
a box. Add two controls to tools/sign_sorter/template.html's "Fix the cut" panel, keeping the existing box edit:
1. Corner handles: each of the 4 corners moves on its own (a free quadrilateral), not only edges of a parallelogram.
2. "Erase stray ink" brush: paint over ink inside the box that belongs to a neighbour; the painted area is masked to
   paper colour in the tile. Undo per stroke; brush size slider; phone works (touch).
Save as recuts/*.json with {sid, page, quad:[[x,y]x4], mask:[polyline strokes with radius], old, at}; keep the old
{x,y,w,h} form readable. tools/sorter_apply_recuts.py cuts the quad (perspective-warp to an upright tile) and applies
the mask; tools/sign_sorter_apply.py passes them through. Offline tests in tools/tests/ + a browser test in
tools/sign_sorter/browser_tests/ (corner drag, brush stroke, undo, save shape). Rebuild Longlee and Pisany on the new
template at the same URLs (owner choices kept), and post the links in a ROOM done line for the account-3 orchestrator.
Update SYSTEM.md if a new tool name appears. Do not touch any target's readings.
