# Conventions

Every project inherits these. A project's own conventions file says "inherits the hub" and then adds its
domain rules: what its evidence looks like, what its grades mean, what its statuses are called.

These are the shape. The content is the project's.

## 1. Check it is not already done, before you start

Before any campaign, establish that the thing is still open, in the project's own terms, and write the check
into the target's notes with the date and the exact queries. A search negative means nothing beyond the
sources and the method it names.

*Worked example: cipher-lab runs six independent blind searchers and a reconciler. Four of its queue items
turned out to have been published in clear since the 1800s, found for a few dollars each.*

## 2. Nothing is new until a verifier says so

The agent that produces a result may never call it new, first, unpublished or previously unknown. It reports
what it found and where it did not find it. A **separate** session, working from the result and trying to
disprove it, assigns a novelty class after a logged search. External wording follows the class, not the
excitement.

*This rule exists because on 20 September 2026 a reading was reported as four unpublished items. Two of the
four had been in print since 1864 and 1891, one of them in the very source the solver had searched.*

## 3. No negative without a control

A failure means nothing unless the same method, on the same day, succeeded on something comparable. State
the control or do not state the negative.

## 4. Grade every claim per unit

Whatever a project's unit is, each one carries where it came from: a primary source, a known-good
comparison, an inference, or uncertainty. A result with no grades is an opinion.

## 5. Absolute dates, always

"21 September 2026", never "yesterday" or "recently". Agents read these files months later with no idea
when they were written.

## 6. Reproducible results

Any claimed result has a script that regenerates it from the inputs, and a check mode that fails if the
stored output is stale.

## 7. Credit

Name who did what and when, including other people's prior work and other projects' tools. Cite the
licence when you vendor someone's code or data.

## 8. Personal data stays out

Repositories are shared and may be public. Log a request by date and counterparty, never with a name,
address, payment detail or credential.

## 9. Money and outward-facing actions go to a human

No purchase, subscription, order, payment, email to a third party, or publication happens without the
owner. An agent drafts it and puts a row in `ASKS.md`.

## 10. Tokens are the budget

Tier the model to the job: the cheap model for searching, harvesting, sweeping and first passes; the
strongest only for reconciliation, verification and orchestration. Scripts read, models judge: never have a
model read a whole volume to find one thing. Fetch once and keep a manifest. Every brief carries a usage cap
and the worker stops at it. A worker does one job, pushes, reports, and stops.

## 11. Claim before you start

Append a claim to the project's `ROOM.md` before beginning, and a done line when you stop. A claim with no
activity for six hours may be taken by someone else, who says so in the same file. Rebase immediately before
writing to any shared file, and when a row conflicts keep both facts.

## 12. Blockers go in `ASKS.md`

Anything that needs a human goes in the project's asks file, not only into a report. A blocker that lives
in a session transcript is invisible to everyone, because no account can see another account's sessions.

## 13. Credentials

Read them from the environment, never from the repository or a chat message. Never run an unfiltered
environment dump, and never run a verbose network trace on a call that carries one. If a credential reaches
a transcript, say so at once and rotate it.

## 14. The improvement loop

Every project keeps `LEDGER.md`: one row per worker with role, model, cost and outcome. A retrospective
reads it weekly and proposes concrete changes to the briefs and conventions, citing the rows that motivate
them. Lessons that are not domain-specific are promoted here, so the next project starts smarter.

## Standard files

Every project repository has: `README.md`, `CLAUDE.md` (inherits this), `STATUS.md` (human board, with a
handoff note at the top), `status.json` (the same state as data), `ROOM.md`, `ASKS.md`, `LEDGER.md`,
`ONBOARDING.md`, `.claude/briefs/`, and `docs/index.html` published by GitHub Pages so the team can see the
board without an account.
