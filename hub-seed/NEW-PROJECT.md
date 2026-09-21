# New project bootstrap

One session turns an idea into a working project. Run it from the hub with the idea in one sentence.
Budget about $15. Do not start doing the project's actual work; this brief ends when the project is ready
for its first real worker.

## 1. Interview, ten minutes

Ask the owner, and write the answers into the new repository's `README.md`:

- What is the goal, in one sentence?
- **What counts as a result?** Name two or three kinds and what separates them. This is the most important
  question and the one people skip. Cipher-lab's answer took two days to find and reshaped its whole queue.
- What is the bottleneck likely to be: access, compute, money, or someone's attention?
- What would make this not worth doing?
- Who else is working on this, and how would we know?

## 2. Search before building

Run the hub's convention 1 against the idea itself. Who is already doing this, how far have they got, what
is published. An honest answer here can end the project in an hour for a few dollars, which is a good
outcome.

## 3. Repository

Create it private. Write `README.md` (goal, what counts as a result), `CLAUDE.md` (inherits
`CONVENTIONS.md`, plus the domain rules the interview implied: the grading vocabulary, the status words),
and empty `STATUS.md`, `status.json`, `ROOM.md`, `ASKS.md`, `LEDGER.md`, `ONBOARDING.md`. Copy the hub's
`briefs/` and adapt. Copy `tools/build_dashboard.py` from cipher-lab and point it at the new stages.

## 4. Tools and access

List every data source the project needs. For each, test the route and write the result into the
`CLAUDE.md` access playbook: a plain API, a browser, a login, or a human. Record what failed and how, not
only what worked. Reuse what the hub already knows, for example the proxy certificate fix that headless
browsers need in cloud containers.

## 5. Secrets

**The one step that cannot be automated.** List every credential the project needs, the exact signup URL,
and the environment variable name. Put the list in `ASKS.md` addressed to the owner. Do not proceed as if
they exist.

## 6. First queue

A scout pass: harvest candidate work, score it against what counts as a result, and write the queue. The
top of the queue should include at least one item of each result kind, so the project does not become
single-track.

## 7. Register

Add the row to the hub's `PROJECTS.md`, add the project to `shell/projects.conf`, and report: what the
project is, what it needs from the owner before anyone can start, and what the first real worker should do.
