# BNF-Q7-ERR (Opus worker for LANE BNF-FOCUS, account 2 / ytbiz), 13 Oct 2026

Job: measure the digit error of f.25's reconciled transcription (`ciphers/fr3982-nevers-toscana-1592/ciphertext.tsv`) as
`PREREG-Q7-T73-ADDENDUM.md` (committed bd79853a6, before this job) defines it, nothing else: no decode, no key, no screen
run. Cap USD 3, box 60 min. Units: crops check (~0.2), ONE blind reading pass by a subagent over the line crops (~0.8),
alignment + scoring script (~0.4), your own adjudication of disagreements against the native crops (~0.8), write-up (~0.4).
Model: Opus for you; the blind pass is a subagent (Opus) that is given ONLY the crop paths and the instruction "read every
digit exactly as written, one line per crop, ? after an uncertain digit" -- never ciphertext.tsv, passA/passB, the key, or
any note of what the letter says.

Read first: CLAUDE.md rules 2, 3, 6; TRANSCRIPTION.md (agreement is not accuracy); the addendum; the folder's NOTES.md
(BNF-Q7-KEY: where the f.25 crops are and how the two passes were cut); last 30 lines of ROOM.md. Disk only: the native
image and crops from BNF-Q7-KEY are on disk; if a crop is missing, re-cut it with `tools/iiif_lines.py --image <native>`.

Steps
1. ROOM claim (tools/room.py, single quotes) with box end and cap.
2. Blind pass -> `q7test/passC_blind.tsv` (same line ids as ciphertext.tsv).
3. Align passC to ciphertext.tsv per line (difflib or edit-distance alignment; script in `q7test/err_measure.py`, --help):
   counts of matches, substitutions, insertions, deletions; disagreement share d = (S+I+D)/len(reconciled).
4. Adjudicate every disagreement yourself against the native crop: reconciled right / blind pass right / unreadable. Report
   both: the addendum's conservative e_hi (Wilson 95% upper bound on d, every disagreement counted against the reconciled
   text) AND the adjudicated error of the reconciled text with its own Wilson bound. The licence in the addendum uses the
   conservative e_hi; say so plainly. If adjudication shows reconciled-text errors, write a corrected
   `ciphertext_v2.tsv` (never overwrite ciphertext.tsv) and list each change.
5. NOTES.md section "## BNF-Q7-ERR (13 Oct 2026, account 2)": d, e_hi, adjudicated error and bound, whether the addendum's
   licence holds (e_hi <= 0.07), per-line counts. Keep `tools/gaps_check.py fr3982-nevers-toscana-1592` passing.
6. Commit by explicit path, `tools/file_shrink_guard.py` on touched files, push (`tools/room.py --push <paths>`), ROOM done
   line "for LANE BNF-FOCUS (account 2)": d, e_hi, adjudicated error, licence yes/no.

Do not decode or run screen.py target (the lane runs it if licensed). Never print credentials. Never the words solved,
cracked, novel, first, new for anything this project did. Never call AskUserQuestion. If `tools/room.py --start` fails to
push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
