# Onboarding

For a new person joining the project, and for the first session of any agent they run. Read this, then
`CLAUDE.md`, then `STATUS.md`. Twenty minutes, and you are current.

## What this project is

We read old ciphered letters nobody has read. The bottleneck is access, not cryptanalysis: two well-funded
AI projects swept everything already online this month, so our lane is the paper still sitting in archives.
`README.md` under "What counts as a result" defines the three kinds of result we want, and every board card
carries one: **recovery** (a key found in another box opens an unread text), **cryptanalysis** (reading
without a key), **contribution** (a correction, a mapping or a verified negative handed to the people who
hold or study the material).

## Read in this order

| File | What it is |
|---|---|
| `CLAUDE.md` | The ten rules, the pipeline, the usage and access playbooks. Binding on every agent. |
| `STATUS.md` | The human board. Starts with a handoff note saying exactly where things stand. |
| `ROOM.md` | The shared channel. One line per signal. Read the last 30 before you act. |
| `QUEUE.md` | The ranked queue of candidate targets, with a kind per row. |
| `LEDGER.md` | One row per worker: role, model, cost, outcome. How we learn what works. |
| `.claude/briefs/` | Role templates. A worker brief is a copy of one of these with the target filled in. |
| `BUDGETS.md` | Everyone's plan limits, so the team can see who has headroom. |
| `ASKS.md` | Everything blocked on a human, from any project. Add a row when you are blocked. |
| `HANDOFF-WEEK.md` | The current week's agenda, if one is running. |

The board is published at https://noautopilot.github.io/cipher-lab/ and rebuilt by
`python3 tools/build_dashboard.py` from `status.json`. `status.json` is the source; `STATUS.md` and the board
must always agree with it.

## Your first session

1. Clone the repository and read the three files above.
2. Add your row to `BUDGETS.md` and commit it.
3. Set your own environment variables (see below). They are per person and per environment; nobody else's
   settings reach you.
4. Pick work from `QUEUE.md` or the board. **Claim it in `ROOM.md` before you start.**

## The rules people actually break

- **Never call anything new, unpublished, first or previously unread.** A solver reports "read at grade H"
  and "not found in the sources I named". Only a separate verifier, after a logged search, assigns a novelty
  class. This is rule 10, and it exists because we got it wrong on 20 September.
- **Never put a copy order, payment or quote request in front of the owner until a check-solved sweep has
  set that target to stage 2.** Three items in our own queue turned out to have been printed in clear since
  the 1800s. The sweep costs a few dollars and has already paid for itself twice.
- **Claim before you start, push often.** Three workers inside one account collided on the queue file on
  20 September. With several people it is worse. One line in `ROOM.md` prevents it.
- **Never echo a credential.** No unfiltered `env`, no verbose curl on a call that carries one. Two workers
  did this on 20 September and two passwords had to be rotated.
- **Absolute dates everywhere.** "21 September 2026", never "yesterday".

## What you set up yourself

Environment variables, in your own Claude Code environment settings. The service logins are shared accounts:
get them from the owner through a password manager, never from this repository and never pasted into a chat.

| Variable | For |
|---|---|
| `DECODE_USER`, `DECODE_PASS` | de-crypt.org, the cipher record database |
| `IA_USER`, `IA_PASS` | archive.org. `IA_USER` must be the account email address |
| `JSTOR_USER`, `JSTOR_PASS` | scholarship checks for verifier sessions |
| `GOOGLE_BOOKS_KEY` | Google Books API. Calls also need `&country=US` |

Also paste this into your environment's setup script, or headless Chromium will not trust the container's
proxy and every browser fetch will fail:

```
apt-get update -qq || true
apt-get install -y -qq libnss3-tools || true
mkdir -p $HOME/.pki/nssdb
[ -f $HOME/.pki/nssdb/cert9.db ] || certutil -N -d sql:$HOME/.pki/nssdb --empty-password || true
certutil -d sql:$HOME/.pki/nssdb -A -t "C,," -n ccr-agent-proxy -i /root/.ccr/agent-proxy-ca.crt || true
```

## Working alongside other people's agents

Everyone has full access; there are no fixed lanes. That makes the claim rule the only thing keeping two
agents off one target. A claim looks like this, appended to `ROOM.md`:

```
2026-09-21 09:00 | the owner / solver: hamilton-1650 | claim: transcribing the NRS sheets, expect 2h
```

Release it with a `done` line. If you see someone else's claim on what you wanted, take the next thing.
Rebase before you write to any shared file (`QUEUE.md`, `QUEUE-scores.json`, `status.json`, `STATUS.md`,
`ROOM.md`) and keep both sides of a conflicting row rather than overwriting someone.
