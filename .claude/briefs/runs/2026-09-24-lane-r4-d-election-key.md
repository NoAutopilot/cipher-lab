LANE R4 WORKER D -- M36 fr5761 1519 ELECTION KEY: glyph atlas of the alphabet signs, two atlas passes of f.104 (fol.50v), key.tsv
as a dataset (Sonnet lead and passes, cap $5; disk only, no fetches). Target: ciphers/fr5761-election-1519.
Common rules: .claude/briefs/runs/2026-09-24-lane-r4-common.md. Read .claude/briefs/transcription.md and NOTES.md "Key transcription,
progress" (worker G: natives f104-f110 on disk, one word-description pass key_passB.tsv, no atlas; interrupted at 1.9x cap).
key_passB.tsv was made without an atlas: do not reuse it as a pass; it may be kept as a check only after reconciliation.
1. Atlas: tools/glyph_atlas.py over the sign regions of images/canvas104-110 (all seven leaves, so later pages share one code book);
   decide merges and splits yourself from the contact sheet; codes K1..Kn; glyphs/atlas.png, atlas.tsv, labels.json, build.sh.
   Commit and push.
2. Crops of f104 by line (tools/iiif_lines.py local-image mode if one exists, else add it as an option with a test -- LANE R4 A
   may be adding it at the same time: git pull first and reuse). Two blind Sonnet subagent passes of f104: each row = correspondent
   heading, section (alphabet / nulls / names / other), plain value as written, atlas code(s) for the cipher sign. Commit each pass.
3. tools/reconcile_passes.py; gate >= 80% on the sign column. Pass -> settle disagreements.tsv from the image, write key.tsv
   (correspondent, plain, sign_code, grade H for key-leaf values, pass agreement) and a one-line count in NOTES.md. Fail -> report
   the agreement and the confusion pairs, stop.
4. Only if 3 passed and budget remains (< 70% of cap spent): grep QUEUE.md and sources/ (Bourdeau catalogue text on disk) for 1519
   letters of the named envoys (Orval, Bonnivet, Guillard, Cordier, La Motheaugroing, Langeac, La Vernade, Salviati, Robertet,
   La Guiche, Moltzau, Tavannes, Bordeaux) and write the hits as one TSV (leads.tsv). No fetches for them.
No decoding of letters, no other folios' passes. NOTES.md section "Atlas and key f.104 (24 Sept 2026, LANE R4 D)".
ROOM done line ends "for LANE R4: M36 key f104 <pass|fail> <pct>".
