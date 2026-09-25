LANE R6 WORKER COMMON (parent: LANE R6 orchestrator, session_018MWpKL71WnBxA8k4ejVkBS). Written 25 Sept 2026 15:45 UTC.
Read, in order: CLAUDE.md; `.claude/briefs/runs/2026-09-24-lane-r4-common.md` (the base rules); `.claude/briefs/runs/2026-09-25-lanes-7b-COMMON.md`
(the 25 Sept addendum, which wins where they differ); this file; your job brief.
Overrides of the R4 common file:
- Hosts: the R4 list of forbidden hosts is retired. Use ONLY the hosts your job brief names, at the Access playbook's per-host limits.
  gallica.bnf.fr: this lane's two fetchers are named in their briefs; nobody else in this lane touches Gallica.
- Readings route to `for LANE V6` (verifiers), not V3/W2.
- Wall-clock box: stop and push at your $ cap or your minute box, whichever comes first. The box is also a minimum working time: do not
  stop early with the job undone while budget remains. Your own cost reading does not bind the orchestrator; it reads get_session.
- Never call AskUserQuestion (no human watches this session). If blocked, write a `flag:` ROOM line, push, and stop.
- A subagent's usage folds into your cost late: budget pass-B subagents at the cost of your own pass A.
- NOTES.md: write your section as the brief says; when the brief names a separate notes file, write there instead (several workers share
  one target folder and must not collide on NOTES.md).
- Done line (COMMON item 9): target number and control number side by side, requests per host, no cost figure.
