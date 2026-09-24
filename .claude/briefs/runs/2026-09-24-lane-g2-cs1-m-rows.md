# LANE G2 check-solved CS1: QUEUE rows M23, M31, M32, M30, M24, M27 (Sonnet, cap $6, no Gallica, no archivesetmanuscrits)

Read .claude/briefs/check-solved.md (or the check-solved skill) and QUEUE.md "Fourth pass, 24 September 2026" (rows M22-M34, found by LANE G2
worker F; its harvest is sources/solver-diffs/2026-09-24-lane-g2-gallica4.tsv). For each row: make ciphers/<short-name>/NOTES.md with the
status word first, the six-source sweep (search engine; printed correspondence of sender and recipient on IA; calendars/state-paper series;
Cryptiana and Cipherbrain; DECODE catalogue CSV grep; both solver repositories, fresh shallow clones grepped for shelfmark and ark), the
verdict and a one-line nomination if open: `python3 tools/room.py "..." "nomination: ciphers/<t> | copy-free | <kind> | <one line>"`.
Do NOT fetch gallica.bnf.fr or archivesetmanuscrits.bnf.fr (LANE G2 has two fetchers there already): use the harvest TSV and the QUEUE row
for the catalogue text; if a verdict needs the image or the finding aid, say so and mark it for LANE G2. Update each row's verdict in QUEUE.md
(rebase first; keep other writers' facts). No transcription, no decoding.

COMMON (every LANE G2 worker, 24 Sept 2026). Parent: LANE G2 orchestrator session_015NqJ9uu5Ef3Bo6QaRiGcGp.
- Read CLAUDE.md in full, then this brief, then the target's NOTES.md sections named below; the last 30 lines of ROOM.md.
- First action: `python3 tools/room.py --start`, then a claim line with `python3 tools/room.py "<role> (<model>, cap $N, for LANE G2)" "claim: <target> -- files: ..."`.
  Last action: a `done:` line with the commit hash and a two-line result. Push with `python3 tools/room.py --push <paths>`; stage by explicit path.
- Run every long job in the FOREGROUND (never background a solver or a fetch loop; two workers went idle that way). Commit and push after each
  pass or step, so a rate-limit stop loses nothing.
- Stop at your cap (the session metadata's cost figure). At the cap, push what you have, write a 'progress' paragraph in NOTES.md, post done.
- Rule 4 grades per token, rule 7 a script that regenerates any reading (prefer tools/decode_key.py with decode.json), rule 3 matched controls for
  any negative. Rule 10: no "new", "first", "unpublished", "previously unread"; say "read at grade X" and "not found in <source>, searched <date>".
  Absolute dates; read `date -u` before writing any time.
- Good-citizen rule: one request at a time per host, >= 1.5 s apart, UA `cipher-lab research script (contact via repository)`, IIIF images only on
  gallica.bnf.fr (.texteBrut is altcha-walled), stop a host on 429/403/challenge and log it. Report requests per host in your done line.
- Keep committed images under 30 MB per folder; above that, keep a manifest and put working copies in your scratchpad.
- End: a short report paragraph in the target's NOTES.md (what was found, where it was not found); do not classify novelty.
