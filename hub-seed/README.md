# Hub

The layer above the projects. It holds what every project inherits, a registry of what exists, and the
shell tools for moving between them.

```
idea ──> hub ──┬─> existing project ──> its own repo, its own sub-orchestrator
               └─> new project ──> bootstrap (requirements, tools, secrets) ──> new repo
```

**The one rule that makes this work: the brain is the files, not the session.** A session that runs for days
re-reads its whole history every turn, and on 17 to 21 September 2026 that cost $2,042 against $330 for every
worker combined. So state lives in git, sessions are disposable, and any agent that reads a project's
`STATUS.md` is current within a minute.

| File | What it is |
|---|---|
| `PROJECTS.md` | The registry. Every project, its repository, owner, status and where it is stuck. |
| `CONVENTIONS.md` | What every project inherits. A project's own conventions file adds domain rules on top. |
| `NEW-PROJECT.md` | The bootstrap brief. Turns "I have an idea" into a working project in one session. |
| `ASSIGNMENTS.md` | The work queue between accounts. Written by one, pulled by another. Nothing dispatches. |
| `BUDGETS.md` | One row per account. The only way limits are visible across accounts. |
| `briefs/` | Role templates that are not domain-specific. |
| `shell/` | `estate`, `asks`, `go`, `hubnew`. `projects.ps1` for Windows PowerShell, `projects.sh` for macOS and Linux. |

## Reaching across accounts

You cannot. No account sees another account's sessions, rate limits or artifacts. That is a hard wall, not a
configuration problem. Everything here is built around it: agents **write** their state to git and to their
project's `ASKS.md`, because nobody can **read** their sessions. The estate view is an aggregation of what
people wrote, never a window into where they are working.

The practical shape: one orchestrator per person, running on their own plan, reading shared state. A thin
control plane on an API key if you want something that works while everyone is asleep. All heavy work stays
on subscriptions, because that is the capacity you have already bought.
