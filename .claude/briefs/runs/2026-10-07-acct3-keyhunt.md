# KEYHUNT round (account-3 orchestrator, 7 Oct 2026 17:2x UTC): KH-1 (account 1), KH-2 (account 2), KH-4 (account 4)

Why: today's only counted results came from one pattern -- a key we already hold (Eckert Cipher No. 2, a period book)
applied to sibling entries nobody had decoded. Every lane today reports its runnable backlog spent. So this round hunts
NEW UNREAD SIBLINGS for keys already in hand, rather than new targets. Lane brief .claude/briefs/default-lane.md (common
tail); lane orchestrator, Opus 5.5; cap $40, box 5 h each. Partition KEY-OFFICES.tsv by row number: KH-1 rows 2-25,
KH-2 rows 26-48, KH-4 rows 49-71 (header is row 1).

Per key row:
1. From KEY-OFFICES.tsv (office, correspondents, years, archive, shelfmark) list the same office's OTHER letters within
   the key's validity window (+/- 3 years) in digitised holdings: the holding's catalogue (Gallica SRU / BnF archives et
   manuscrits, TNA Discovery API, Huntington CONTENTdm, Nationaal Archief, DigitArq, Europeana), the printed calendar or
   edition's index, and the target folder's own notes. Use APIs/scripts (Usage 2), good-citizen rule, one host at a time.
2. Keep only letters that are (a) digitised and fetchable from the cloud, (b) carry cipher, (c) are NOT already a target
   folder here and NOT already read by Bourdeau/Aymeloglu/DECODE/Tomokiyo (grep sources/ and the solver clones), and
   (d) have no interlinear decipherment or printed clear text found -- unread text is the goal (owner, 7 Oct).
3. For each survivor: fetch, crop (tools/iiif_lines.py), two blind passes on ONE leaf, decode with the held key, matched
   control (shuffled key, same N), judge where a corpus fits. A passed control -> new target folder via the intake gate
   (tools/intake_gate_check.py) with check-solved first; a failed control -> one line in the key's folder NOTES.
4. Write every candidate considered (kept or dropped, with reason) to KEYHUNT-2026-10-07.tsv (key_path, letter,
   shelfmark, digitised, cipher, already_read_by, glossed, action, result). Stop at 80% of cap; report how many unread
   siblings exist per key -- that number is itself the deliverable.
