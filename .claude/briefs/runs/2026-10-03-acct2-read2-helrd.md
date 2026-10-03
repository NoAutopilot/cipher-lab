# READ2-HELRD: rule-7 fresh re-derivation of the hellen-frederick-1752 R1953 reading (3 Oct 2026, written by LANE-READ2, account 2)

Why: CLAUDE.md rule 7 -- before a reading moves on, a fresh session that has seen only the spec and the key re-derives it with the
target's decode script and `--check`; a re-derivation that differs by more than the M-graded tokens sends it back. The reading:
ciphers/hellen-frederick-1752/key_r4369/reading_R1953.txt (READ2-HEL, ddb945a9; H 152 S 304 M 16 U 374).

Model: Sonnet. Cap USD 3; box 30 min from your claim, whichever first. Disk-only.

Start: `python3 tools/room.py --start` (detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`); `date -u`; claim with
`python3 tools/room.py "READ2-HELRD (account 2 worker, for LANE-READ2)" 'claim: hellen-frederick-1752 rule-7 re-derivation of R1953 (spec + key only); box ends <HH:MM> UTC'`.
Read ONLY: this brief, CLAUDE.md rules 4 and 7, `specs/hellen-frederick-1752.json`, `ciphers/hellen-frederick-1752/ciphertext_R1953.txt`,
`ciphers/hellen-frederick-1752/key_r4369/key.tsv`, `key_r4369/decode.json`, and `tools/decode_key.py --help`. Do NOT read the folder's
NOTES.md, HYPOTHESES.md, `reading_R1953*` or `build_keys.py` before step 2 is written down.

1. Write your own short script (`key_r4369/rederive_helrd.py`) that maps each R1953 token through key.tsv per decode.json's stated rules,
   from the spec and key alone, and writes `key_r4369/rederive_helrd.txt` (one output per token, U for an unkeyed code).
2. Run `python3 tools/decode_key.py ciphers/hellen-frederick-1752/key_r4369 --check` and paste its output.
3. Only now open `reading_R1953_tokens.tsv` and diff token by token against your output: count agreements and differences, list every
   difference with its grade in the committed reading. Verdict: PASS if every difference falls on an M-graded token (or none), else SEND
   BACK with the list.
Write the result as a short section "## READ2-HELRD rule-7 re-derivation (3-4 Oct 2026)" at the end of the folder's NOTES.md (append only).
No novelty words; no decoding beyond the key. Never call AskUserQuestion. End: commit by explicit path, `python3 tools/file_shrink_guard.py
<paths>`, `python3 tools/room.py --push <paths>`, confirm on origin/main, one done line for LANE-READ2 (account 2) with agreements /
differences / verdict, "cost: see the lane ledger".
