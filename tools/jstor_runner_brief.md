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

## Paste-ready instruction (24 Sept 2026; for a Claude Desktop chat with the Chrome extension, or a scheduled task every 4 hours)

```
You are the cipher-lab JSTOR runner on the owner's computer, where Chrome is logged into www.jstor.org. Read CLAUDE.md rule 10 and the good-citizen rule.
1. git fetch origin main && git checkout -B main origin/main
2. Open JSTOR-QUEUE.tsv (tab-separated: target, query, requested, status, hits). Take every row with status `queued`; do first the rows whose target is one of ciphers/fr2980-gramont, ciphers/fr20140-danzay-1557, ciphers/thurloe-printed, ciphers/lodewijk-van-nassau-1573-74, ciphers/august-van-saksen-1561-64, ciphers/eckert-1864, ciphers/huntington-blathwayt-madrid-1728 (they gate the outreach), then the rest.
3. Run each query on www.jstor.org in my Chrome (never log in yourself, never store a password), one at a time, at least 4 seconds apart, at most 60 in this sitting. On a captcha or any block page, stop, leave the rest `queued`, and say so.
4. Record the first page of hits in the hits column as `title | author | journal | year | pages | stable URL` separated by `;`, or `no hits`. Set status to `done <date>`. Keep tabs, row order and every other row unchanged.
5. For a hit that could print, calendar or discuss the letter itself, open the article IN JSTOR'S ONLINE PAGE VIEWER and read it there (a free account gives about 10 online reads a month, per the owner 24 Sept 2026; JPASS makes online reading unlimited); never click Download PDF. Spend a read only when the hit's title or snippet names the letter's sender or recipient together with its year; otherwise record the hit as `candidate, unread` in the hits column and let the verifier decide whether it is worth one of the reads and add to that target's AUDIT.md a section `## JSTOR (owner's machine, <date>)` with the citation and one sentence on what it says. Change no N-class.
6. Commit only JSTOR-QUEUE.tsv and the touched AUDIT.md files by path; git fetch origin main && git rebase FETCH_HEAD && git push origin main.
7. Append one ROOM.md line: `<UTC> | JSTOR runner (owner's machine) | done: N rows, M with hits, targets ...` (python3 tools/room.py "JSTOR runner (owner's machine)" "done: ..." if Python is available).
Never write my name or email; never call a reading new, first, unpublished or unread. Final reply: rows answered, rows with hits, targets with hits, any block page.
```

Ongoing: JSTOR has no public search API; institutions reach it through licensed discovery feeds and text-mining agreements, not open to individuals. A scheduled task on the owner's computer with the text above, every 4 hours while the machine is on, is the standing arrangement; the parent's check-in routes rows that turn `done` with hits to a verifier.

## Second job for the same session or scheduled task: the open-index rows (added 24 Sept 2026)

OpenAlex and Semantic Scholar rate-limit the cloud egress address (OpenAlex's free daily budget per IP; resets midnight UTC),
so queries a verifier could not run are handed over the same way. After the JSTOR rows: open any `outreach/*owner-queries*.md`
file with `status: ready`; run each query in its table in the owner's Chrome on https://openalex.org and
https://www.semanticscholar.org, one at a time, a few seconds apart; record per query "no relevant hit" or title, author, year
and URL of anything that prints or discusses a decipherment of the letter; write the results into the ASKS.md row the file
names (one line per query, pipes intact); set the file's first line to `status: done <date>`; commit those files by path,
rebase, push; ROOM line `<UTC> | open-index runner (owner's machine) | done: N queries, K hits`.
