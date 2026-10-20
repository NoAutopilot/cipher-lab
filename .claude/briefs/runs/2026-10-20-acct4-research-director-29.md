# Research director, wave 29 (20 Oct 2026, 02:1x UTC by date -u): Sherwood correctness check after the digit re-read

Common tail: .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a dollar
figure for yourself, `tools/experiment_log.py --check`, `python3 tools/dup_check.py sherwood-cossit-1781` pasted). Solver job: report
what was found and where it was not found; no novelty class (rule 10). AUDIT.md is the verifier's; do not edit it.

## JOB SHERWOOD-CELLS (account 4; Opus 5.5; cap USD 3; box 35 minutes; hosts: archive.org (11280377bsb page images for pp.33, 53, 165, 166, 225, 360, 366, 412 only, one at a time, 1.5 s apart); Price: vision calls: 4 x USD 0.5 + 1 reconciliation = 2.5)

ciphers/sherwood-cossit-1781 (partial, N3/D2, H/C/S 72.7%). SHERWOOD-REREAD (NOTES.md "## Digit re-read", tx2/changes.tsv) applied three
image-confirmed digit corrections (360-33, 165-13, 53-35) whose new Entick cells come from the OCR grid only (Tan, "interj", Chalkcutter:
graded M), and found two S known answers that both blind passes read differently from ciphertext.tsv (p346_L09 412-33 -> 412-35;
p345_L10 225-17 -> 225-19). This job is a correctness check on a counted reading, not a depth push.
1. Entick side: cut line crops (`tools/iiif_lines.py --image <page file> --out ...`, paste the command; never a whole page to a reader) of
   both columns at the cited lines for p.360 l.33, p.165 l.13, p.53 l.35, and for p.412 l.33 and l.35, p.225 l.17 and l.19, and read the
   headwords blind (the reader sees crops and line numbers, no cipher, no sketch). Use the same line-count rule decode_entick.py uses
   (book/ grid; the 18 Oct column-rule fix). Write book/entries_image.tsv rows for each cell read.
2. Cipher side, for the two doubted S groups only: one taller crop each (the mrows/crop_slips.py way, paste the command) and one blind
   forced-choice read between the two digit strings (33 vs 35; 17 vs 19).
3. Re-decode (`decode_entick.py`, chooser unchanged) and regrade by the existing rules. If either S row's digit is confirmed changed and its
   new word differs, the row drops from S (rule 4a: depth is lowered on any revision) and NOTES.md says so plainly; flag it in ROOM.md for
   a verifier. `decode_entick.py --check` passing; paste tools/judge_plaintext.py output. New grade counts and H/C/S share.
4. NOTES.md "## Cell check (SHERWOOD-CELLS, 20 Oct 2026)" with the six research-director questions; gaps_check passes.
Report: the five cells' headwords, the two S rows' verdicts, grade counts before/after, five lines.
