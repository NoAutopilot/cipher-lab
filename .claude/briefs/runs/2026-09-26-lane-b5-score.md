JOB bSCORE (LANE B5 reserve, Sonnet worker). One line: score QUEUE.md's scouted-but-unscored VX-*, KX-*, KT-*, PX-* rows into QUEUE-scores.json and rank them alongside the "Re-rank for LANE B5" rows, so the next breadth lane's queue exists (RETRO-2026-09-26a proposal 2).

Read first: `.claude/briefs/runs/2026-09-26-lane-b5-common.md`; RETRO-2026-09-26a.md section 2; CLAUDE.md Pipeline 3 (selection rule: pools first; expected value = P(first cheap test moves it) x value / cost; prefer a transcription on disk, a formal constraint, a corpus in tools/data, a key or sibling decipherment beside the item); QUEUE-scores.json's existing schema (read 5 entries, reuse the fields exactly); QUEUE.md "Re-rank for LANE B5".

Cap and box: $3 or 35 minutes from your first `date -u`, whichever first. Disk only, no hosts. Scripts read, models judge: extract the rows with a script (grep the ID prefixes), then judge each one.

Steps:
0. `date -u`; `python3 tools/room.py --start`; ROOM line before editing QUEUE-scores.json and QUEUE.md (shared files: fetch and rebase right before writing; keep both facts on conflict).
1. List every VX-*/KX-*/KT-*/PX-* row in QUEUE.md with no entry in QUEUE-scores.json. For each: check ciphers/ and specs/ for an existing folder/spec and NEAR.md/STATUS.md for a lane that already worked it (the re-rank's "Excluded" paragraph shows how: several apparently-unrun rows had been run by PX/LX/VX/ZX2). Drop worked rows with a one-word reason.
2. Score the rest in QUEUE-scores.json (same schema; kind cryptanalysis/recovery/contribution; P(moves), value, cost, pool yes/no, the named first cheap test and its matched control, corpus available or the era gap). Do not touch other lanes' targets (LANE AX: WVO Nassau, brochado, pro3055; GOLD3: koehler, debosnys, kaliningrad).
3. Append a QUEUE.md section "Scored backlog for LANE B6, 26 Sept 2026, <clock>" with a table of the top 12 by expected value (same columns as the B5 re-rank), marking which are pools. Push; done line naming the top three; report in five lines.
