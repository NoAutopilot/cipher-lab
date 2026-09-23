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
