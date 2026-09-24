LANE R4 WORKER O -- fr3151 SEURE 1558 f75L: fix the segmentation, then box-keyed passes of the page (Sonnet, cap $8; disk first).
Target: ciphers/fr3151-seure-1558. Common rules: .claude/briefs/runs/2026-09-24-lane-r4-common.md. Read NOTES.md "Capture and passes
(LANE R4 K)": one line passed at 51.7% because the binding-gutter shadow and faint bleed-through were segmented as boxes (662 of 1177
boxes are noise) and three box pairs overlapped one sign.
1. Re-segment f75L inside a gutter-free region (crop off the gutter band and the top-margin bleed-through; raise the ink threshold or
   minimum box area; merge overlapping boxes) with tools/glyph_atlas.py options (add an option with a test if one is missing). Target:
   under 20% noise boxes. Recluster, relabel from the contact sheets (add the "W" double-loop as a code), classify, strips. Commit.
2. Gate test on three lines first (line 9 and two others): pass A by you, pass B by one Sonnet subagent blind; compare by (line, box id).
   Under 80% -> report and stop. At or over 80% -> continue line by line through the cipher block of f75L (commit every two lines),
   settle disagreements from the strips, write ciphertext_f75L.tsv (as fr2933-salviati-1525's ciphertext_f54r.tsv), report tokens, types.
3. At 70% of cap, stop adding lines; settle and write what is done.
No fetches unless a strip needs native resolution the disk lacks (gallica.bnf.fr IIIF only, <= 6 requests). No solving. NOTES.md section
"Re-segmentation and passes f75L (24 Sept 2026, LANE R4 O)". ROOM done: agreement, lines done, tokens.
