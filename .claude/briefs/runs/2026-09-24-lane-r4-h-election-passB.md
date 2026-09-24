LANE R4 WORKER H -- M36 fr5761 1519 KEY: pass B of f.104 with the atlas, reconcile, key.tsv (Sonnet, cap $3; disk only; no subagents).
Target: ciphers/fr5761-election-1519. Common rules: .claude/briefs/runs/2026-09-24-lane-r4-common.md. Worker D was stopped at 1.7x its cap after
the atlas (glyphs/atlas.tsv, 35 codes, glyphs/atlas*.png) and pass A (key_passA_atlas.tsv, 38 rows) landed. Crops: images/f104_L*.jpg.
1. Pass B, BLIND: do not open key_passA_atlas.tsv or key_passB.tsv (the old word-description pass) until step 2. From the crops and the
   atlas, write key_passB_atlas.tsv in exactly pass A's columns (line, section, plain, sign_code, note), one row per plain value. Commit, push.
2. Compare A and B by (line, plain) on sign_code (script); write recon_key/agreement.tsv and recon_key/disagreements.tsv. Gate >= 80%.
3. Pass -> settle each disagreement from its crop (one line of reason), write key.tsv (correspondent, section, plain, sign_code, grade H,
   agreement A/B/settled) and one count line in NOTES.md. Fail -> report agreement and confusion pairs, stop.
Check your cost after each step; at $3 push and stop. NOTES.md section "Pass B and key f.104 (24 Sept 2026, LANE R4 H)". ROOM done line
ends "for LANE R4: M36 key f104 <pass|fail> <pct>".
