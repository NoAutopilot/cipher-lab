OX-HEL (Sonnet, cap $6 as a stall alarm, at most 2 subagents). Parent: LANE OX orchestrator, session_01BE3g8tWbS4T24KXMpShHt4. COMMON: .claude/briefs/runs/2026-09-25-lane-ox-COMMON.md applies in full.
Target: ciphers/hellen-frederick-1752 (W.B. von der Hellen to Frederick II, 8 ciphertexts 1752-1763; DECODE record R1953, 4 Jan 1752, KHA Prins Willem V inv.196). Read NOTES.md (csNA's search log: NA 1.10.29 Fagel inv.5206, 185 scans, "Afschriften van ontcijferde brieven", 1752-53).
Host: nationaalarchief.nl (IIIF/scan API) only; post `touching host nationaalarchief.nl` in ROOM; one request at a time, >=1.5 s; thumbnails first.
Steps:
1. Page through Fagel inv.5206's scans at low resolution (script the thumbnails; a subagent reads them in batches) for a 4 January 1752 despatch from von der Hellen (Hellen, "La Haye", Berlin-bound, to the King of Prussia), and for any other von der Hellen despatch; list every Hellen item found with scan number and date in NOTES.md.
2. Fetch the matching leaves at full resolution (images/, manifest, <30 MB) and transcribe the deciphered French text of the 4 Jan 1752 letter into plaintext_decipher.txt (two passes only if the hand is hard; say which).
3. The ciphertext side: where is R1953's ciphertext image? Check the NOTES for DECODE R1953 and the KHA; if the ciphertext is on DECODE only, write "owed: DECODE login worker (LANE DX)" in NOTES.md and do not log in. If a ciphertext image is on disk or copy-free, transcribe it (two passes, 60% gate) into ciphertext.tsv.
No key recovery in this job. Files: ciphers/hellen-frederick-1752/**, ROOM.md.
