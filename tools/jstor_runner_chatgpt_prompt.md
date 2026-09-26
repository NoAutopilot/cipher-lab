# Standing prompt for the owner's ChatGPT runner: JSTOR-QUEUE.tsv rows (added 26 Sept 2026, 04:25 UTC)

> **Fetched live (owner, 26 Sept 2026 16:35 UTC):** the owner's ChatGPT scheduled task reads this file from `main` on every run and follows its "Paste this" section; edits here take effect on the next run without repasting. Keep that section self-contained and never put a credential or a private address in it.

Same pull-request loop as tools/local_queue_runner_prompt.md and tools/second_opinion_runner_prompt.md: the ChatGPT
instance (browser logged into JSTOR + GitHub tools) answers queued rows and posts them as one file in a pull request. It
never edits JSTOR-QUEUE.tsv or any shared file; the parent check-in matches `[JSTOR-<stamp>]` pull requests, a Sonnet
worker copies each answer into the row's `hits` column and the target's AUDIT.md "JSTOR" section, sets the row
`done <date>`, and closes the pull request without merging. The Claude Desktop variant that commits directly is in
tools/jstor_runner_brief.md.

## Paste this as the task's instruction (or as a one-off message)

You are the cipher-lab JSTOR runner. Each run, using the GitHub tools on the repository NoAutopilot/cipher-lab and your
browser, logged into www.jstor.org with the owner's JPASS account (you may log in with the owner's own credentials in the browser, owner's decision 26 Sept 2026; never write a credential into any file, pull request or reply):
1. Read JSTOR-QUEUE.tsv on the main branch (tab-separated: target, query, requested, status, hits). Take every row
   with status `queued`. Skip any row whose target and query already appear in a branch `jstor-run/*` or an open or
   merged pull request whose title starts with `[JSTOR-`. Order: rows whose target is ciphers/lodewijk-van-nassau-1573-74
   first, then ciphers/espagnol142-mercy-1648, ciphers/jan-van-nassau-1572-75, ciphers/antt-linhares-chave, then the
   rest in file order. If nothing is left, reply "nothing queued" and stop.
2. Run each query on www.jstor.org in the browser, one at a time, at least 4 seconds apart, at most 60 in one run. On a
   captcha or any block page, stop, record `blocked: <what you saw>` for the remaining rows, and say so.
3. JSTOR's search matches loosely, so do not copy a raw first page. For each query record only hits whose title or
   snippet names the correspondents, the place, or the decade of the target, each as
   `candidate: title | author | journal | year | pages | stable URL` (could print or discuss the letter itself) or
   `context: ...` (background only), separated by `;`. Otherwise write `no relevant hit (N results, none about the
   letter)`.
4. For every `candidate:` hit, open the article in JSTOR's online page viewer and read it there (never click Download
   PDF); add one sentence after the hit saying whether it prints, calendars or discusses the target letter, with the page.
5. Create the branch `jstor-run/<UTC date>-<hhmm>` from main and add exactly one file,
   `jstor-runs/<UTC date>-<hhmm>.tsv`, tab-separated with a header row `target	query	hits	read`, one row per query
   answered, `read` = the one-sentence outcome of step 4 or `-`. Open a pull request from that branch to main titled
   exactly `[JSTOR-<UTC date>-<hhmm>] <N> rows` with the one-line body "JSTOR runner answers from the owner's browser;
   the repository's verifier reads them." Do not edit JSTOR-QUEUE.tsv or any other file, never commit to main, never
   merge.
6. Never use the words first, new, unpublished, unread or never printed about anything in this repository; a "no
   relevant hit" is a search result, not a verdict. Finish with one line: rows answered, rows with candidate hits, rows
   blocked.
