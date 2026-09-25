OX-PAGT transcription (Sonnet, cap $6 as a stall alarm, 2 subagents for the passes). Parent: LANE OX orchestrator, session_01BE3g8tWbS4T24KXMpShHt4. COMMON: .claude/briefs/runs/2026-09-25-lane-ox-COMMON.md applies in full; .claude/briefs/transcription.md.
Target: ciphers/clairambault1225-paget-1714: two nomenclator-cipher letters signed Paget, Genoa, 8 April and 28 August 1714, BnF Clairambault 1225 f.60-66 (7 canvases already on disk, images/manifest.json; OX-PAG's NOTES.md section). No fetching unless a crop at native resolution is essential (Gallica, one request at a time, post "Gallica slot OX").
Steps:
1. Crop lines (tools/iiif_lines.py on the ark, or local crops from the on-disk images; check the debug overlay).
2. Two blind passes by two subagents: every token in reading order, clear French words as words, cipher groups as numbers/signs exactly as written, line refs. tools/reconcile_passes.py; 60% agreement gate; settle disagreements from the crops. Output ciphertext.tsv (letter, line, position, token, clear/cipher flag, grade) and cleartext context per letter.
3. Stats in NOTES.md: cipher tokens per letter, distinct codes, number range, repeats, and whether the two letters share codes (same key). Plus the nomenclator's likely shape (codes for names vs syllables vs letters) from the ranges only.
No decoding. Files: ciphers/clairambault1225-paget-1714/**, ROOM.md.
