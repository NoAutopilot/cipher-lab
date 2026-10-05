# RULES-SLIM (account 3 worker) -- 5 Oct 2026. Opus. Cap $8, box 90 min. Owner approved 5 Oct ~9:30 pm PDT.
Goal: cut per-session token load. CLAUDE.md (119 KB) loads into every session; agents need rules, not incident stories.
Deliverables (NOT swapped in by you; the owner approves first):
1. RULEBOOK-FULL.md = the current CLAUDE.md verbatim, plus at top a one-paragraph note: "human-readable full rulebook; CLAUDE.md is the
   slim agent copy; every rule change edits both (rule R0)". Give every rule/clause a stable id (R1, R3.a, R3.b ..., OUT-7, USAGE-6.c, ...)
   as an inline tag, e.g. `[R3.c]`, without changing wording otherwise.
2. CLAUDE-SLIM.md (target <= 15 KB): same ids, each rule as one or two imperative lines + the tool that enforces it + a pointer
   "story: RULEBOOK-FULL.md#R3.c". Keep verbatim anything operational an agent needs mid-task: credential handling, never-lists,
   status vocabulary, grade letters, N/D classes, outreach gates, git rules, access-playbook host table (may move to docs/HOSTS.md
   with a one-line pointer), personal-data rules. Drop narratives, dates of incidents, cost anecdotes.
   First line R0: "Every rule change edits CLAUDE.md AND RULEBOOK-FULL.md in the same commit; tools/rules_sync_check.py enforces it."
3. tools/rules_sync_check.py (+ tools/tests/test_rules_sync_check.py, offline): every id in one file exists in the other; exits 1 on
   drift; --help. Docstring: catches a rule added to one file only; must NOT block edits to wording inside an existing id.
4. RULES-SLIM-REPORT.md (short, for the owner): sizes before/after, approx tokens saved per session, any rule you were unsure how to
   compress (listed, kept verbose), and how to swap: `git mv CLAUDE-SLIM.md CLAUDE.md` after approval (the parent does it).
Do not edit CLAUDE.md itself. Do not drop any rule. Commit by explicit path, push, ROOM done line, 5-line report.
