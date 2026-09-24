LANE R4 WORKER L -- M36 fr5761 1519 KEY f.104: third atlas-checked pass and a dataset close (Sonnet, cap $3; disk only; no subagents).
Target: ciphers/fr5761-election-1519. Common rules: .claude/briefs/runs/2026-09-24-lane-r4-common.md. Read NOTES.md "Pass B and key f.104
(LANE R4 H)": both passes read the same rows; they disagree in sign codes (pass A wrote UNLISTED for about half the alphabet; pass B took the
script's cluster codes).
1. Coverage first (script): for the f104 sign boxes, the share with a confident atlas code (glyphs/signs.tsv, clusters.tsv). If under 70%,
   add the missing alphabet signs as new atlas codes from the contact sheet (labels.json, build.sh), commit.
2. Pass C, blind to A and B: per row, the atlas code for the sign, UNLISTED only if no code matches after step 1. Commit.
3. Majority of A/B/C per row (script) -> key.tsv (correspondent, section, plain, sign_code, grade H where 2 of 3 agree, M otherwise), counts.
This closes the target's f104 as a dataset either way: NOTES.md "Pass C and key f.104 (24 Sept 2026, LANE R4 L)". ROOM done with counts.
