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
