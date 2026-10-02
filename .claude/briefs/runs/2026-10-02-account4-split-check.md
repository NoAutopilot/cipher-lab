# SPLIT-<target>: check the glued-digit hits of one target against the page image and fix them through corrections.tsv

Written 2 Oct 2026 02:4x UTC (clock read) by the account-4 parent (session_01SEzoee67SivPooFpTkxMme), on account-3's
nomination (ROOM.md 00:52, 01:26 UTC 2 Oct). The session's prompt names the target, the hit count, the cap and the
vision-call count. Role field: `SPLIT-<target> (account-4)`. Model: Fable 5.1 (Opus 5.5 if Fable fails). Box: 60 min.

## What the hits are

`ciphers/_triage/split-check-1-Oct-2026.tsv` (columns: target, job, key_range, token, n, status, positions, exceptions,
splits, decoded) lists, per target, the tokens `tools/decode_key.py --split-check` found outside the key or above its
confident range, with every way of splitting each into two or three key codes. CLAUDE.md Usage 8: "Mercy, 1 Oct 2026:
65, 52, 48, 72 against a 2-34 key were two digits written together; it cannot see in-range glued pairs such as 2 6, so
the image still decides."

## Steps

1. `python3 tools/room.py --start`; last 30 ROOM.md lines; stop with `blocked` if another account claims the target
   in the last six hours; claim line. `python3 tools/intake_gate_check.py <target>` must exit 0 (every target in this
   wave passed it on 2 Oct 2026; paste the line).
2. Read the target's rows from the TSV. Group them by page/leaf and position. Rank: unkeyed tokens with exactly one
   valid split first, then tokens with several splits, then in-range doubtful tokens the TSV lists.
3. For each hit, cut a small crop around the position from the image on disk (`tools/iiif_lines.py --image ... --out
   ...` for whole lines, or a PIL crop of the token with 2-3 tokens of context either side); one subagent call per
   page's crops (never a whole leaf), asking only "is this one group or two (or three), and what digits" -- blind to the
   decode. At most the vision calls the prompt names; stop before the call that would cross 80 pct of cap or box, push
   what you hold, and say which hits were not reached.
4. A confirmed split goes into the folder's `corrections.tsv` (create it if absent, in the shape the folder's decode
   config or `tools/decode_key.py --help` expects; read how other folders do it: `grep -l corrections.tsv ciphers/*/
   decode.json`) with the position, the original token, the corrected tokens, the grade (M from one read, H if the crop
   is unambiguous and your own look agrees) and `SPLIT-<target> 2 Oct 2026` as the source. Never edit ciphertext.txt
   itself (CLAUDE.md Layout: as transcribed, never silently repaired). Then `python3 tools/decode_key.py ciphers/<target>
   --check` exits 0 and the per-token grade counts before/after are written down.
5. NOTES.md: a dated section "## SPLIT-<target> (2 Oct 2026, account-4)" with hits checked / confirmed splits / kept as
   one token / not reached, the grade counts before and after, and the judge line if the folder has a spec (rule 7).
   If the target has a "## Remaining gaps" section, update it in place (`python3 tools/gaps_check.py <target>` pasted).
   Status word unchanged (rule 5). If the target has a PROGRESS.tsv row and a count there moved, update that row from
   the file on disk and name the file in its `source` cell.
6. Commit by explicit path, rebase, `python3 tools/restricted_guard.py --outgoing`, `python3 tools/file_shrink_guard.py
   <files>`, push to main; done line with the counts and the vision calls used. Stop.

Rules 2, 4, 7, 10 bind. The common tail of `.claude/briefs/README.md` applies in full.
