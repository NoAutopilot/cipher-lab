# NEVBIR-<folio> (2 Oct 2026, written by account 3; runs on account 2). One job per letter; the row's note names the folio.

Model: Fable if it answers, else Opus 5.5. Cap USD 5, box 50 min. Per-unit pricing: 2 blind transcription passes +
1 reconciliation + decode/control ~ USD 1.2 each.
Target: ciphers/nevers-birago-fr3251-1572, the ONE letter named in your WORK-QUEUE row's note (folio and no.). Its Premise
check (PREMISE-NEVBIR, 2 Oct, NOTES.md) is CLEAR TO TEST; folio corrections: no.82 is f.162, no.86 is f.170.
1. `python3 tools/room.py --start`; claim the folio; `python3 tools/intake_gate_check.py nevers-birago-fr3251-1572` exit 0.
2. Fetch the leaf once (Gallica IIIF, ark and canvas rule in NOTES.md/images/manifest.json; 1.5 s between requests),
   cut line crops with `tools/iiif_lines.py --image ... --out ...` and paste the command; give subagents only crops.
   Two value-blind passes against the 51-sign sheet (one page per call), one reconciliation; record agreement.
3. Decode with the printed 1572 key + T42=m (keys/ and decode.json as used for f.178v) via `tools/decode_key.py` (a decode.json
   section or a per-letter ciphertext file), then the matched control: 200 value-shuffled keys, rank and z of the real key on
   the same statistic the f.178v run used. Report both numbers (rule 3). Judge (it16/it-period corpus as the folder uses) only
   as a secondary signal; report its line as is.
4. If the real key ranks 1/201 with a clear margin, grade tokens per rule 4 (S where the control backs it, M otherwise) and
   write the reading file; otherwise log the control-backed negative or non-test. Never call it new (rule 10); a passing
   reading is flagged in ROOM for a separate verifier.
5. NOTES.md step + finish-or-blocker sections in place; add/update a PROGRESS.tsv row "Birago 1572 f.<folio>" from the files;
   gaps_check; commit by explicit path; done line with rank, z, agreement, grades, cost note.
