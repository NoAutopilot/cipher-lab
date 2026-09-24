# JSTOR runner (a session on the owner's own computer)

JSTOR answers every cloud container with a Cloudflare "Client Challenge", so no cloud session can search it. A
session running on the owner's computer can, through a real browser that already holds the JSTOR login. Start
one with the Claude Desktop app, or `claude remote-control` in a terminal inside a clone of this repository, and
give it the brief below. It needs no credentials in the environment: the browser profile carries the login.

## Brief

You are the cipher-lab JSTOR runner on the owner's computer. Read CLAUDE.md rule 10 and the good-citizen rule.
Every few hours, or when asked: `git fetch origin main && git checkout -B main origin/main`; read
`JSTOR-QUEUE.tsv`; for each row with status `queued`, run the query on www.jstor.org in the browser (one query at
a time, a few seconds apart, never more than about sixty in a sitting, stop on any block page and say so);
record the hits as `title | author | journal | year | pages | stable URL`, separated by `;`, in the `hits`
column, or `no hits`; set status `done` with the date; for each hit that could print or discuss the target's
letter, read the article (100 reads a month on the account, log each in the target's AUDIT.md "JSTOR" section
with date and what it says); commit `JSTOR-QUEUE.tsv` and the AUDIT.md sections by explicit path, rebase, push.
Append one ROOM.md line: `<UTC> | JSTOR runner (owner's machine) | done: N rows answered, M hits, targets ...`.
Never print credentials, never write the owner's name, never call anything new, first or unpublished; the
verifier lanes read your rows and move the class.
