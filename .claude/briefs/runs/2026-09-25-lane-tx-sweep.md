TX-SWEEP (Sonnet, stall alarm $6, at most 2 Sonnet subagents). Parent: LANE TX orchestrator, session_01UDxtM9Xv2dnPfoo5z9T6wA. Read .claude/briefs/runs/2026-09-25-lane-tx-COMMON.md first; it applies in full.

Job: triage every unswept or still-open row of the printed-ciphertext detector sections of QUEUE.md and write ONE file: .claude/briefs/runs/2026-09-25-lane-tx-triage.md. Touch nothing else except ROOM.md (claim, done).

Sections (grep QUEUE.md for the headers): "## Printed ciphertext (detector test of 23 September 2026)", "## Printed ciphertext, round 2 (24 September 2026)", "## Printed ciphertext (detector round 3, LANE S, ...)", "## Printed ciphertext (detector round 4, LANE S, ...)", "## Printed ciphertext, HathiTrust detector (LANE N, ...)". About 38 rows; about 32 never swept, 6 left open. Skip rows already closed (found-solved, dropped, a target folder at partial/solved), and say which you skipped and why in one line each.

Excluded (do not triage beyond one line "excluded: <reason>"): ciphers/thurloe-printed (LANE T's, incl. P3/P10 and Stamford P4); anything claimed in ROOM.md in the last six hours; every R5, N4, B, V2, PX, LX, OX target (grep ROOM.md and STATUS.md for the folder name).

Per row, one line or short block:
- the passage: edition, volume, page, letter, date, sender -> recipient, cipher extent (tokens if countable), cipher type as printed (numbers, letters, symbols);
- decipherment in print: does the edition print a decipherment anywhere (same page, footnote, appendix, a later volume, an errata)? Read the IA full text you already have or fetch it once (archive.org _djvu.txt; be-api fts for lending-only items; HTRC EF for HathiTrust-only volumes). Name what you read.
- key route: a sibling letter of the same correspondent and years whose decipherment is printed or on disk (grep ciphers/*/key*.tsv and NOTES.md for the correspondent), a published key, a key sheet, or none. If a sibling exists, say how many sibling ciphertext/plaintext pairs are available.
- EV per CLAUDE.md pipeline item 3: P(first cheap test moves it) x value / cost, score 0-10, one line of reasoning.
- named first step (check-solved first for any row going forward, per the intake gate).

End with a ranked table (rank, row id, passage, key route, EV, first step) and a TOP FOUR line, plus counts: rows swept, rows with a key route, rows excluded/skipped. Rule 10 wording; mark inferences as inferred. The vein is rated low to moderate; a short negative with numbers is a result.

Hosts: archive.org and be-api one at a time >=1.5 s; data.htrc.illinois.edu >=1.6 s; Google Books with key and &country=US. Fetch each volume's text once to your scratchpad, grep it; do not commit the texts. Report request counts per host.
Finish per COMMON: commit the one file by path, push with tools/room.py --push, ROOM done line naming the top four, one-paragraph reply.
