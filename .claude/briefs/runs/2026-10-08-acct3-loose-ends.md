# Loose ends and success propagation (account-3 orchestrator, 8 Oct 2026 04:0x UTC). default-lane common tail; Opus 5.5
# orchestrating, Sonnet triage subagents (max 4 at once).
Why (owner, 8 Oct 04:00 UTC: "why do I have to spot it? what other unlocks have I not spotted?"): na-oldenbarnevelt-2442-1605
NOTES.md section 1 recorded on 25 Sept that leaves 4, 5 and 7 "carry heavy cipher that reads as a different correspondence" and
that scans 9-11 were never fetched. That sentence never became a step: it sat in a body section, not in "## Remaining gaps" /
"## Escalation", so tools/gaps_check.py passed, tools/next_steps.py never listed it, and the 3 Oct solve of blocks B/C1 (key ours)
never triggered a look at the rest of its own volume. Two system gaps: (1) observations in prose never reach the step registers;
(2) a success never propagates to its siblings. A raw grep at 03:58 UTC found 374 such phrases in 165 NOTES.md files (unfiltered,
much of it noise). These two jobs turn both gaps into tools and run them once over the whole repository.

## LOOSE-ENDS (account 2), cap $18, box 150 min
1. Tool (CLAUDE.md 8a; --help; offline test in tools/tests/ with a MUST-CATCH case built from the 2442 section-1 sentence and a
   MUST-NOT-FLAG case: a line already carried in that folder's Escalation): `tools/loose_ends.py` scans ciphers/*/NOTES.md,
   AUDIT.md, HYPOTHESES.md for (a) unpursued-material phrases (not fetched, never read/opened/decoded, different correspondence,
   further/other cipher leaves/letters, carries cipher, unread sibling, out of scope for this, "next:" in a body section, scans
   N-M not fetched, unread blocks), and (b) structural signals: image files in a folder's images/ or images/manifest.json that no
   transcription/ciphertext/crops file references (image on disk, never transcribed). For each hit it marks tracked = yes when the
   same material is named in the folder's Escalation/Remaining gaps, NEXT-STEPS.tsv, an open WORK-QUEUE.tsv row, or a ROOM claim in
   the last 7 days. Output LOOSE-ENDS.tsv (folder, status, file:line, snippet, kind, tracked). Add it to SYSTEM.md (system_map_check).
2. Run it; keep untracked hits only. 3. Triage: Sonnet subagents on batches of ~25 hits (~$0.6 per batch, priced per call; plus one
   reconciliation unit): for each hit -- real unlock or noise; what material; cheapest next step with its matched control; cost;
   P(a new COUNTED document: N3+, D2+, two audits, per .claude/briefs/runs/2026-10-08-acct3-depth-bar.md); outside blocker? 4. Write
   LOOSE-ENDS-2026-10-08.md: ranked by expected counted documents per dollar, top 20 with one line each. For each of the top 20, add
   the step to that folder's "## Escalation" as "[ ] <step>; ~$<cost>; source: loose-ends 8 Oct" so gaps_check and next_steps see it
   (rebase first; file_shrink_guard on every touched file). Queue nothing; the orchestrator queues. Do not decode anything.

## SUCCESS-SIBS (account 1), cap $10, box 90 min
For every document that is counted or at one audit with N3+ (status.json results; the board's counted() rule in
tools/build_dashboard.py), list its siblings from the repository's own files only (no network): other leaves/blocks of the same
volume or file, same sender, same recipient, same key or key family (KEY-OFFICES.tsv), same design (KEY-DESIGN.tsv; e.g.
vowels-as-digits in clear Spanish), same archive series. Mark each sibling read / unread / not-in-repo, and whether a cheap step
exists. Write SIBLINGS-2026-10-08.tsv and a "## Siblings (8 Oct 2026)" section in each folder's NOTES.md (append only). Then add a
check to tools/gaps_check.py: a target whose status.json row is N3+ must carry a "## Siblings" section (offline test both ways), so
every future success is propagated by construction. Do not decode; report the top 10 unread-sibling steps by expected yield.
