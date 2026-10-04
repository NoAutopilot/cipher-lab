# DEPTH-REGRADE -- verifier re-grade of every counted result to depth D0-D4 (4 Oct 2026, account 3; owner approved)

Model Opus 5.5. Cap USD 12; box 90 min. Per-unit: 23 results x ~0.4 (one reading file + AUDIT.md section each, no web) + 1 reconciliation
unit = ~10; stop before starting a result that would cross 80% of cap or box and list the rest as "ungraded (legacy)".
Common rules: `.claude/briefs/README.md` common tail (room.py start/claim/push, no dollar figures, no AskUserQuestion).
Claim: `python3 tools/room.py "DEPTH-REGRADE (account 3 verifier)" 'claim: depth re-grade of counted status.json results; box ends <HH:MM> UTC'`.

You are a verifier (CLAUDE.md rule 4a, verifier template step 3a). Do not decode, do not change any key, ciphertext or reading.
1. `python3 tools/depth_check.py` lists the 23 legacy counted results ("ungraded (legacy)"). For each, open the reading the result
   links (the folder's reading file, reading_tokens.tsv or the AUDIT.md section named in `fields_source`) and its grade counts.
2. Assign depth per rule 4a: depth_pct = share of cipher tokens (excluding cleartext and nulls) graded H/C/S; depth_unread
   {names_codes, other}; D2+ needs one true, specific sentence about the content that you write from the reading alone
   (`depth_sentence`); D3 needs >=80% and an external check or AD + matched control already on file; D4 needs every cipher-letter token
   H/C/S, listed name/code residue only, a non-statistical external check on file (period key/table, period gloss, known-answer copy,
   independently confirmed fact) and a rule-7 re-derivation on file. Name the check from the folder's own files (`depth_check`). When
   evidence for a level is not on file, grade the level below -- never the hopeful one.
3. Write into status.json on each result: `depth`, `depth_pct`, `depth_key_pct` (if computable, else omit), `depth_unread`,
   `depth_sentence` (D2+), `depth_check`, `depth_by` (your session id), `depth_date` "4 Oct 2026", `decode_status` (D0-1 Non-decrypted,
   D2-3 Partially decrypted, D4 Decrypted). Append a 3-5 line "## Depth (DEPTH-REGRADE, 4 Oct 2026)" section to each folder's AUDIT.md
   (append only). Results at D0/D1: also correct any outward sentence in status.json `line`/`headline` and STATUS.md that calls them a
   reading or solve (rule 10 propagation), and say "class without a reading" instead.
4. Also grade the two counted today by LANE-A3V: hellen-frederick-1752 R1953 and birago-fr3252-1571-72 f.117r (check status.json has
   their result entries; if not, add them from AUDIT.md -- kind recovery, key period / published, claim_scope recovered-passages,
   two audits -- then grade).
5. `python3 tools/depth_check.py` must exit 0; paste its last line. Rebase immediately before editing status.json (shared file; keep both
   sides on conflict). Commit by explicit path, `tools/file_shrink_guard.py`, `tools/room.py --push`. Done line: counts by depth, the
   unique-solve number before (23) and after, and every result that fell below D2 by name.
