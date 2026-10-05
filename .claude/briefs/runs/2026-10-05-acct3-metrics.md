# METRICS (account 3 worker) -- 5 Oct 2026. Opus 5.5 (model floor). Cap $4, box 60 min. Owner approved 5 Oct.
Build tools/progress_metrics.py (+ offline test): from LEDGER.md and status.json compute per ISO week: (a) worker spend USD, (b) share of
workers with outcome D (vs D-, X, F), (c) count of results at D2+ added that week (status.json depth/dates), (d) USD per new D2+ result,
(e) median worker cost by role. Output a markdown table to stdout and --tsv. Handle messy rows (skip and count unparsable).
Run it, paste the table into research/PROGRESS-METRICS.md with a 3-line reading. Add one line to .claude/briefs/retrospective.md:
"Report tools/progress_metrics.py's week-on-week trend (USD per D2+ result, share D) before proposing changes." Add the tool to
SYSTEM.md (system_map_check). Commit by path, push, ROOM done line, 5-line report.
