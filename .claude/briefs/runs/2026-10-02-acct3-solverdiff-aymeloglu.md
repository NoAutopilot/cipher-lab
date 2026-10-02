# SOLVERDIFF-AYMELOGLU (2 Oct 2026, written by account 3; runs on account 2 via WORK-QUEUE row tagged other)

Job: a fresh solver-repository diff. The last full diff was 24 Sept (sources/solver-diffs/); since then https://github.com/aaymeloglu/unsolved-ciphers has kept
publishing. On 1 Oct an account-4 web check found fr3625-lauriere-1593 already read in full by a third party on that
repository's issue tracker (29 Sept) while another of our workers was still transcribing it. Find every other case.

Model: Fable while it answers, else Opus 5.5 (never below). Cap USD 6, box 60 min; stop at 80% of either.

1. `python3 tools/room.py --start`; read the last 30 ROOM.md lines; claim with
   `python3 tools/room.py "SOLVERDIFF-AYMELOGLU (account 2)" "claim: solver-repo diff vs our open/partial/blocked targets, read-only except the outputs below"`.
2. Fresh shallow clone of https://github.com/aaymeloglu/unsolved-ciphers to /tmp (never commit it). Licence: NO licence: cite it, never copy code or text beyond a short quoted line.
3. Our side, by script: every ciphers/*/NOTES.md whose first-line status is open, partial or blocked; for each pull its
   shelfmarks/folios, DECODE record ids, sender, recipient, date (grep NOTES.md head, spec, AUDIT.md).
4. Their side, by script: its README, catalogue/ files, per-target folders and their notes, and its issues and PRs.
   Match on DECODE id, shelfmark+folio, and sender+recipient+year. Scripts read, the model judges only the candidate pairs
   (CLAUDE.md Usage 2).
5. For each real match, read their write-up and classify: (a) they read it (full or partial; their stated %),
   (b) they attempted and closed it, (c) same item listed only, (d) false match. Record the date they posted it.
6. Write sources/solver-diffs/2026-10-02-aymeloglu.tsv: our_folder, our_status, their_path_or_url, class, their_extent,
   their_date, evidence line. For every (a) or (b) hit: post a ROOM.md flag naming our folder and the URL, and append a
   dated section "## Solver-repo check (aymeloglu, 2 Oct 2026)" to that target's NOTES.md (end of file, nothing else edited)
   -- EXCEPT ciphers/debosnys-1883 (never touch) and these targets, which another account's pass is editing tonight
   (TSV + ROOM flag only, no NOTES edit): the status-partial folders and espagnol142-mercy-1648.
   Do not change any status line, status.json or STATUS.md: the parent does that from your flags.
7. Commit by explicit path, `python3 tools/room.py --push <paths>`, then a done line with counts per class and the
   request count per host. Report in five lines. Rule 10 wording; never "new" or "first".
