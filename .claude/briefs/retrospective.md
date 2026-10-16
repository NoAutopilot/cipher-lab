# Retrospective (Sonnet, fresh session weekly and after every 12 ledger rows or $60 of worker usage, cap $10)
Read LEDGER.md, LESSONS.md, CLAUDE.md, the brief templates in .claude/briefs/, STATUS.md and the git log of
the last seven days. Answer, with numbers from the ledger: cost per delivered result by role and model;
share of workers that needed a poke, over-ran, over-claimed or failed; which lessons repeat; whether the
board carried all three kinds of result; whether queue rank predicted useful work (did the top five produce
anything?). Wait-only targets at the window's end (`python3 tools/next_steps.py --wait-only`) and how long each
has been wait-only (from git log of the row); when the count is not zero this is the retrospective's first
proposal. Then propose at most five changes, each as a concrete diff to a template, CLAUDE.md, a workflow
or a tool, with the ledger rows that motivate it. Write RETRO-<date>.md at the repo root, commit and push.
Do not apply the changes: the orchestrator applies the safe ones and puts the rest to the person. The
routine's email carries the five proposals in plain words. + common tail.
Report tools/progress_metrics.py's week-on-week trend (USD per D2+ result, share D) before proposing changes.

Register first (16 Oct 2026): read RETRO-PROPOSALS.tsv and run `python3 tools/retro_check.py`; every proposal this retrospective writes
gets a row (status open, decided_on blank) in the same commit as RETRO-<date>.md; a proposal already in the register as open or
partial is not re-proposed -- it is named once as a finding with its row, and the parent's duty 0d applies or escalates it. Also run
`python3 tools/learning_metrics.py --from <window start> --to <window end> --compare learning/baseline-2026-10-09-15.json` and paste
it before the proposals, operational and solving measures apart.

Near solves (25 Sept 2026): review every NEAR.md row -- has its named next step run since the last retrospective, with its
control, and are the numbers in the row? A row that has not moved is a finding with the lane and the reason named.

## Exception review (owner, 16 Oct 2026, ASKS 171; cap USD 3, Opus, within one parent check-in, never a full retrospective)
Triggered by `python3 tools/retro_check.py` line (e): since the last retrospective or EXC row, an X (over-claim) row, a worker that
died with no repository, three or more rows at 2x their cap or more, a gate found blind, or a registered lesson broken again. The
reviewer reads only the rows the line names, their NOTES.md/ROOM.md context and the RETRO-PROPOSALS.tsv rows they touch, and writes
`learning/EXC-<date>.md` with, per row: the failure in one sentence, whether an existing rule or tool should have caught it (name it),
the smallest correction (a tool/test diff, a brief line, or "none: a one-off") and who applies it. Then appends one register row
`EXC-<date>	EXC<n>	<what>	applied|open	learning/EXC-<date>.md	<date>	<who>` to RETRO-PROPOSALS.tsv (an `applied` row clears the
trigger; an `open` row is the parent's duty 0d within 7 days). No ledger recode, no CLAUDE.md edit by the reviewer.
