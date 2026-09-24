LANE R4 WORKER G -- M35 SALVIATI f.54r: finish pass B, gate, settle (Sonnet pass, Sonnet lead, cap $4; disk only).
Target: ciphers/fr2933-salviati-1525. Common rules: .claude/briefs/runs/2026-09-24-lane-r4-common.md. Read NOTES.md "LANE R4 B stopped;
partial gate measure" and the atlas files (glyphs/atlas.tsv, glyphs/atlas.png). Worker B was stopped at 2.3x its cap.
1. Finish pass B BLIND to passA2.tsv (do not open passA2.tsv until step 2): from line 8 pos 14 to the last box of
   f54r_boxlist_for_passes.tsv, confirm or correct each box's code and marks from strips/, in exactly passB2.tsv's columns and actions.
   Append to passB2.tsv line by line; commit and push after every two lines.
2. Compare by (line, pos), excluding boxes both read '_', as the NOTES section did; write recon_box/agreement.tsv (per line) and
   recon_box/disagreements.tsv. Gate: >= 80% on base codes over the whole page.
3. Pass -> settle each disagreement from its strip (one row each: chosen code, reason), write ciphertext_f54r.tsv (line, pos, code,
   marks, grade A/B/settled) and report tokens and types. Fail -> report and stop.
No solving, no key trials, no other pages. NOTES.md section "Pass B finished and gate (24 Sept 2026, LANE R4 G)". Cap is hard: check
your cost after each two lines; at $4 push and stop. ROOM done line ends "for LANE R4: salviati gate <pass|fail> <pct>".
