# Accounts

Which Claude account is which, which GitHub account it signs in as, and why a repository
sometimes does not appear. Written 22 September 2026, after a repository was invisible for an
hour because only half of a two-part permission was in place.

## The accounts

| Claude account (addresses kept out of the public repository, rule 9) | Signs in to GitHub as | Local wrapper (Windows) | Config folder |
|---|---|---|---|
| owner account | NoAutopilot (owns the repositories) | `claude` | `.claude` |
| second account (biz) | `noautopilotytbiz-beep` * | `claude-ytbiz` | `.claude-work` |
| team account | `noautopilotteam-lab` | `claude-team` | `.claude-three` |

\* Inferred from the naming, not yet confirmed by a session. The team mapping is confirmed: a
web session on that account identified itself as `noautopilotteam-lab`.

Wrapper setup and the Windows console traps are in `CLI-WINDOWS.md`. To see which account a
running session is on, type `/status`.

## Two permissions, both required

A repository is reachable only when **both** of these are true. Miss either and the repository
simply does not appear in the picker, with no error saying why.

1. **The Claude GitHub App is granted the repository.** Managed on the owning account at
   https://github.com/apps/claude/installations/select_target — either "All repositories" or an
   explicit list. This says Claude *as an application* may touch the repository.
2. **The GitHub account is a collaborator on it.** Repository → Settings → Collaborators → Add
   people → **Write**. This says *that account* may touch it.

Grant 1 is per owning account and covers every repository at once. Grant 2 is per repository,
per account, and is the one that gets forgotten.

An invitation does nothing until it is accepted from the invited account, at
`https://github.com/<owner>/<repo>/invitations`. A pending invitation shows only "Remove Access"
in the collaborator dropdown, which reads like a bug and is not one.

## When a repository does not appear

In order:

1. Type its name in the picker's search box; the list is not always complete until filtered.
2. Check which Claude account the browser is signed in as. Each holds its own GitHub connection.
3. Check grant 1 on the owning account.
4. Check grant 2, and that the invitation was accepted.

Step 4 is the usual answer.

## Scaling

`NoAutopilot` is a personal account, so access is per repository, per collaborator, forever.
Converting it to an organization would make membership the unit instead: add a person once, put
them in a team, and every repository follows. Not urgent at three accounts. Worth doing before
it is six.
