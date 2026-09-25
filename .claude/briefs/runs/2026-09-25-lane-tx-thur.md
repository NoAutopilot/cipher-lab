TX-THUR (Sonnet, stall alarm $5, at most 2 Sonnet subagents). Parent: LANE TX orchestrator, session_01UDxtM9Xv2dnPfoo5z9T6wA. Read .claude/briefs/runs/2026-09-25-lane-tx-COMMON.md first; it applies in full.

Target: ciphers/thurloe-printed residue. LANE T closed 24 Sept 05:20 and LANE W 10:09; the last ROOM activity on this folder is 24 Sept ~17:20 (verifier V5), over six hours: before any work, append the ROOM line "LANE TX takes thurloe-printed residue (P3 postscript, P10 p.620 line 10, the Lockhart and vol. 3 glossed letters) under the six-hour rule; P4 and every AUDIT.md verdict are not touched". Read the folder's NOTES.md handoff, s.12.6, s.17, s.18 and AUDIT.md first.

Files you may touch: ciphers/thurloe-printed/NOTES.md (new section "LANE TX residue (25 Sept 2026)" only), new files under ciphers/thurloe-printed/tx/, ROOM.md. Do not edit keys, readings, AUDIT.md, or any P4 file.

Jobs, cheapest first:
1. Four "outside the lane" letters (handoff: Lockhart from Chauny 19 June 1656, vol. 5 p.101 above P14; the three glossed large-number letters of s.12.6: Nutley, Attorney General Prideaux, Sir Benjamin Wright, vol. 3): for each, from the djvu text on disk or one IA fetch and the page image, say whether Birch prints a decipherment or gloss for every numeral group. If fully glossed: one line, found-solved in print (Birch 1742, vol., page). If some groups are unglossed: count them, and say which existing key (key_*.tsv here) covers the same correspondent or period.
2. P10 p.620 line 10's 14 unglossed groups: apply key_blake_extended.tsv (and key_montagu_extended.tsv as comparison), per-token grades, how many of the 14 read; English sense check with the surrounding printed decipherment.
3. P3's three-line postscript: s.17 left it mostly M under key_butler.tsv. One attempt only: can the sibling letters' keys added since (key_fauconberg, pool_1654) raise any M to C/S? If not, record the numbers and stop.
Each claimed reading: a script under tx/ with --check that regenerates it (rule 7), and a fresh-instance re-derivation by a subagent from the key and ciphertext only. Report what was read and where it was not found; do not classify novelty.
Finish per COMMON.
