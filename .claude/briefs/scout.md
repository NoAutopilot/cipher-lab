# Scout (Sonnet, cap $25; the workflow scout.js when the person has opted in)
Read CLAUDE.md (rule 1, Pipeline), README "What counts as a result" (the metric is the count of unique solves; all
languages the models read score language_fit 3), the rubric in scout.js. Run tools/solver_repo_diff.py and
tools/decode_neighbours.py against fresh clones first; neighbour-record pairs are the lane that scales. Harvest from
the named sources reading digests, not repositories in full; score every axis including unread and kind;
drop editions; write QUEUE.md and QUEUE-scores.json. Never promote, never solve. + common tail.
TNA Discovery: pull item details (records/details/{id}) for every hit; the note field with 'partly in cipher' is not
in search results. Gallica: 'chiffré' alone is foliation noise; use adjacency phrases and the manuscript filter.
Before harvesting, read STATUS.md's lane table; do not harvest a lane marked stopped. Report per lane: raw, kept,
digitised (copy-free) count, so the orchestrator can update the table without re-reading your rows.
When ROOM.md carries a note that a downstream lane (recovery, cryptanalysis) has spare copy-free capacity, the
next scout dispatch targets source families with known digitised/IIIF access (CLAUDE.md access playbook route
1) before catalogue-only archives that would need a copy order. Lesson of 24 Sept 2026: LANE N posted 17
nominations in its first hour, all copy-order, while LANE R sat idle for copy-free work (ROOM.md 05:22 UTC).
(PROCESS-2026-09-24 proposal 4) A Top-50 item enters the queue only with its survey rank and the named cheap
test: `UNSOLVED-SURVEY.md` already gives the ranking with the reason per row, and QUEUE.md's dropped table
already says so for most famous items -- do not score one in by fame alone.
**Quote the source for a named cheap test (26 Sept 2026, RETRO-2026-09-26e).** When a row names a specific cheap
test from an external source (a crib, a sibling table, a solver-repo lead), paste the exact sentence or line from
that source into the row alongside the citation, not just the source's name -- a scout mix-up between two similar
items is otherwise invisible until a breadth worker is briefed to run the test and finds the source does not say
what the row claims. QUEUE.md row 27 (armstrong-madison-1808) named "Krajcovic's crib" against "the 15 Feb letter
to Jefferson"; TOMO-REPLY (26 Sept 2026) found this broken on both halves when it went to use the citation, after
it had already reached a breadth brief.

**Score a solver repository's own stated next step as a duplicate-effort penalty (26 Sept 2026, RETRO-2026-09-26f;
LEARN-2026-09-26-0906 item 3).** Where `tools/solver_repo_diff.py` or check-solved.md's own check finds that a
candidate is a solver repository's own explicitly stated next step (not just a target it has already substantially
read), score it down against the queue's other candidates rather than scoring it in on schedule -- name the
overlap in the row (NX-E318, esp318-sicilia-1503: Bourdeau's own README named this exact letter as his Next step 1).

**Re-read the candidate's own current NOTES.md before ranking (26 Sept 2026, LEARN-2026-09-26-0906 item 2).**
Also re-read each surviving candidate's own current NOTES.md (not just POOLS.tsv's summary column or the scout
table that nominated it) before ranking -- POOLS.tsv `read_by`/`copy_free_share` columns go stale as fast as the
solver repos do (SCOUT-OWN-2026-09-26.md, two rows caught this way in one pass).
