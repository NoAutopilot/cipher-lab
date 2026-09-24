LANE R4 WORKER B -- M35 fr2933 SALVIATI 1525: atlas revision and two script-assisted atlas passes of f.54r against the 80% gate
(Opus lead, Sonnet passes, cap $6; disk only, no fetches). Target: ciphers/fr2933-salviati-1525.
Common rules: .claude/briefs/runs/2026-09-24-lane-r4-common.md. Read .claude/briefs/transcription.md and NOTES.md "Glyph atlas and
atlas passes (24 Sept 2026)" (worker H: base-code agreement 62.8%; 57 of 130 disagreements are gaps; eps/e 7, h/bh 5 confusions).
1. Revise the atlas: split or merge eps/e and h/bh (and o., dl, tee/S4 if the contact sheet shows the same trouble) by eye from
   glyphs/sheet_signs_*.png; update glyphs/labels.json; rerun glyphs/build.sh; commit.
2. Remove the gap disagreements by letting the script count: classify every segmented box of f.54r against the revised atlas
   (nearest exemplar, as ciphers/dupuy452-carpi-1520/glyphs/classify.py; put any reusable part in tools/glyph_atlas.py as an
   option with a test, not a private copy) and write f54r_boxes.tsv (line, box id, bbox, script code, distance, marks above).
   Render per-line strips with box ids printed under each box.
3. Two blind Sonnet subagent passes of f.54r: each receives the strips, the atlas and the box list, and CONFIRMS or CORRECTS each
   box's code (and its mark attribute), and adds or deletes boxes only where segmentation is wrong (flagged). Commit each pass.
4. tools/reconcile_passes.py; report agreement on base codes and with marks. Gate: >= 80% on base codes. Pass -> settle
   disagreements.tsv from the image, write ciphertext_f54r.tsv, report tokens and types, then STOP (the solver is a separate brief).
   Fail -> report agreement and the confusion table, and stop.
No solving, no key trials, no other pages. NOTES.md section "Atlas revision and script-assisted passes (24 Sept 2026, LANE R4 B)".
ROOM done line ends "for LANE R4: salviati gate <pass|fail> <pct>".
