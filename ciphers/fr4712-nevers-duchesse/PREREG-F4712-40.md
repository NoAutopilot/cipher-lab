# PREREG-F4712-40 (worker F4712-40 for LANE DEFAULT-A1-0540, account 1, 11 Oct 2026, written before the read)

Question: f.13r code 40's interlinear gloss -- main word read "Vill." (DUCH-F13 pass A, "l. Vill.") vs "Lill." (pass B). M since 3 Oct.

Instrument: ONE blind Sonnet subagent call, four tiles cut from the reconciliation zooms with tools/iiif_lines.py
(images/f13r/g40/t1..t4_L01.jpg, manifest.json). Order fixed now: t1 = code 21 (decoy, H "Berry", recon_1), t2 = code 40
(tile 40b, recon_1), t3 = code 54 line 15 (decoy, H "Lorm.", recon_2 tile 54b), t4 = code 40 (tile 40a, recon_1).
The reader gets only the four paths and "These are four abbreviated words (or short words) written in a French hand of
about 1592. Transcribe each abbreviated word letter by letter, keeping dots; give your confidence per letter where unsure."
No earlier reading, no code number, no candidate letters, no mention of V or L.

Scoring (case, dots and a trailing abbreviation stroke ignored; only letters compared):
- Gate: t1 reads "berry" and t3 reads "lorm" (exact letters). Either wrong -> NON-TEST, no vote counted.
- Vote: the first letter of the main word (after any small prefix like "l.") on t2 and t4. Both V -> third vote V
  (2 of 3 for "Vill."); both L -> third vote L (2 of 3 for "Lill."); split, or any other letter, or illegible -> TIE.
- Grade after a decided vote: M (a gloss read by eye, never H without a person). Key edit only if a key.tsv row for 40
  exists and changes; decode_key --check after any edit.
- TIE or NON-TEST: logged; the model-reader instrument is [retired] for this gloss (CLAUDE.md rule 3 third-attempt clause)
  and one backlog ASKS line goes to the owner's eye (never blocking).
- Code 93 (two different glosses, lines 2 and 13): conflict reported only, not read here.
