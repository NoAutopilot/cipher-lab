LANE R4 WORKER I -- M35 fr2933 SALVIATI 1525 f.54r SOLVER: try the keys on file by sign shape, then a control-first anneal (Opus, cap $8;
disk only; no subagents). Target: ciphers/fr2933-salviati-1525. Common rules: .claude/briefs/runs/2026-09-24-lane-r4-common.md.
Input: ciphertext_f54r.tsv (509 rows: 370 sign tokens in 36 atlas types with superscript marks, 139 plain Italian boxes; gate 83.5%,
NOTES.md "Pass B finished and gate (24 Sept 2026, LANE R4 G)"), glyphs/atlas.png/atlas.tsv, strips/. Open strips only for named tokens.
1. Key trial by shape (the signs are invented, so a key fits when its SIGN SHAPES match, not its codes): compare the Salviati atlas with
   the sign tables already in the repo -- ciphers/dupuy452-carpi-1520 (Raince/Carpi 1520-26, glyphs/ and key.tsv),
   ciphers/decode-4450-bnf-fr20506-1525 (1525), ciphers/fr2980-gramont (1530), any Montmorency key on file (grep ciphers/*/key.tsv
   and NOTES.md for 1524-1527 papal, Florentine or French court keys), and sources/ copies of Tomokiyo's and Lasry's published
   tables for 1525-26 if on disk (no fetches). Write keytrial.tsv: key, signs matched by shape / 36, and the partial decode of
   f.54r under the best mapping. A key fits if it turns the plain-Italian frame into continuous Italian across the cipher runs.
2. Fit -> key.tsv (salviati code -> value, source key named), decode.json, tools/decode_key.py --check exits 0; grades C for values
   carried from a key on file, S if confirmed by context, M otherwise; counts.
3. No fit -> run the MATCHED CONTROL FIRST (rule 3; J7 lesson): synthesise Italian of 370 tokens with the same type count, marks and
   plain/cipher interleaving, and see whether the homophonic anneal (tools/ or ciphers/*/anneal*.py; reuse, do not write a new one)
   recovers it. Only if the control succeeds (> 60% of tokens) run the target. Report both numbers either way.
Report what was found and where it was not found; do not classify novelty. NOTES.md section "Solver (24 Sept 2026, LANE R4 I)".
Hard cap $8: check your cost after each step, push at 80%. ROOM done line: grade counts or control numbers, and "for LANE V4:
ciphers/fr2933-salviati-1525 reading ready" only if a reading exists.
