# cipher-lab

Working area for attacking unsolved historical ciphers. One person plus AI agents. Read `LANDSCAPE.md` for who
else is working and what is left, `LESSONS.md` for how the successful solvers work. These rules apply to every
session and every subagent, cloud or local.

## Layout

- `ciphers/<name>/` one folder per target: `ciphertext.txt` (as transcribed, never silently repaired),
  `NOTES.md` (sources, status, what is established vs inferred, failure log), `REQUEST.md` when an archive
  request is involved, scripts and keys beside them.
- `sources/` unmodified snapshots of other people's pages. Never edit.
- `tools/` shared scripts. Anything a second target could reuse goes here, not in a target folder.
- `CATALOG.md` every item from Cryptiana's list; `LANDSCAPE.md` the corrected picture.

## Conventions (non-negotiable)

1. **Search before solving.** Before any campaign on a target, establish that it is still unsolved, in this
   order: the cipher's name in a search engine; the sender's printed Lettres or Correspondance on the Internet
   Archive; the calendars and state-paper series; the comment threads of the list posts (Cryptiana blog,
   Cipherbrain); DECODE at de-crypt.org; and the two solver repositories, github.com/dbourdeau/cyphersolver
   and github.com/aaymeloglu/unsolved-ciphers. Record what was checked and the date in NOTES.md.
2. **Image over transcription.** Prefer the page image. When only a transcription exists, say so, and treat a
   negative as conditional on it.
3. **No negative without a matched control.** A solver's failure on a target means nothing unless the same
   solver reads a synthetic cipher of the same length, symbol count, design and language. Report both numbers.
4. **Grade every claimed reading per token:** H read from a key source, C from known plaintext, S cryptanalytic
   with a control, M uncertain, I inferred or repaired. Give the counts. No H or C means "cryptanalytic result".
5. **Status vocabulary** in the first lines of every NOTES.md: `open`, `partial`, `solved`, `closed-negative`,
   `found-solved`, `blocked`, `offline-only`. Nothing else.
6. **Absolute dates.** "19 Sept 2026", never "recently" or "yesterday".
7. **Reproducible readings.** Any claimed reading has a script that regenerates it from the transcription and
   the key, and exits non-zero if the committed reading is stale.
8. **Credit.** Name who solved what and when. Cite the solver repositories and Tomokiyo. Aymeloglu's repository
   has no licence: cite it, do not copy code from it. Bourdeau's code is MIT, text CC BY 4.0.
9. **Personal data stays out of the repo.** It is public. Log archive requests by date and archive, never with
   the sender's name, address or payment details.

10. **Novelty is a verifier's verdict, not a solver's.** A solver session may say "read at grade H" and "not
   found in <named source>, searched by <method> on <date>". It may not say new, unpublished, unread, first or
   never printed, and neither may the orchestrator when it reports to the person. Absence from one source is a
   search result, not a discovery. A separate verifier session, working from the plaintext and the ciphertext
   and trying to disprove novelty, assigns one class after a logged search and writes it to the target's AUDIT.md:
   N0 plaintext and decipherment of this very item already known; N1 plaintext already published anywhere (our
   reading is an independent re-decipherment); N2 plaintext known elsewhere but no prior mapping of this
   ciphertext to it found; N3 no prior plaintext or decipherment located after the logged search; N4 N3 with the
   principal editions, catalogues and project pages covered, internal or unpublished work not excluded; N5
   confirmed by the holding archive or a specialist. Wording such as "first decipherment", "previously unread",
   "newly recovered" or "unpublished plaintext" is allowed only at N4, with the qualifier "no prior decipherment
   located", or at N5. The board's stage "Novelty verified" is set only from AUDIT.md. Lesson of 20 Sept 2026:
   four Eckert 1864 readings were called "never printed" because they were absent from Official Records ser. I
   vols 32-45; the sender-specific editions (Butler Correspondence, Lincoln Collected Works, ORN) had not been
   searched and no phrase search was run after decoding.
   Precedent and worked example: ciphers/eckert-1864/AUDIT.md.


## Pipeline (who hands what to whom)

1. **Scout** (`.claude/workflows/scout.js`, or a worker with the same brief) finds candidates, checks status at
   the sources, scores them and sets `kind` (cryptanalysis, recovery, contribution; editions are dropped). It
   writes QUEUE.md. It never promotes to the board and never solves.
2. **Check-solved** (`.claude/workflows/check-solved.js`) runs blind, six sources, on any queue item before it
   goes on the board, and again whenever a catalogue row may be stale. Its verdict goes into the target's
   NOTES.md and sets stage 2, "Verified unsolved". Stage 2 is set only by a check-solved verdict, and no copy
   order, payment or quote request goes on the person's card until the target is at stage 2 (20 Sept 2026).
3. **Orchestrator** promotes to the board only after check-solved, at most a handful at a time, choosing by
   score and by the three kinds together, so the board always carries at least one recovery and one
   cryptanalysis candidate and never fills with editions.
4. **Access workers** (lookup, print check, image capture, transcription) move a target from stage 2 to stage
   7 without the person where the playbook allows, and write REQUEST.md when it does not.
5. **Solver** reads (stage 8), grades per token, reports what was found and where it was not found.
6. **Verifier** assigns the N-class (stage 9) and corrects any over-claim.
7. **Result label**: the orchestrator sets the card's kind from what actually happened (a key that opened it
   is recovery, a reading without the key is cryptanalysis, a correction or a dataset handed on is
   contribution) and writes the "Result so far" line. README "What counts as a result" is the reference.

## Collaborators

Several people work in this repository, each from their own account, with full access and no fixed lanes.
Two things make that safe, and they are not optional.

**Claim before you start.** Append a line to `ROOM.md` naming you, the role and the target before any work
begins, and a `done` line when you stop. If a live claim already covers what you wanted, take the next
thing. Nothing else stops two agents transcribing the same folio.

**A claim goes stale after six hours.** If a claim in `ROOM.md` has no `done` line and no further activity from that agent for six hours, anyone may take the target after appending a line saying so. Otherwise one idle agent parks a target indefinitely and nobody can tell, because no account can see another account's sessions.

**Anything blocked on a human goes in `ASKS.md`,** not only into a report. A blocker that lives only in a session transcript is invisible to everyone else.

**Rebase before you write to a shared file.** `QUEUE.md`, `QUEUE-scores.json`, `status.json`, `STATUS.md`
and `ROOM.md` are written by everybody. Fetch and rebase immediately before editing, and when a row
conflicts, keep both facts rather than overwriting someone else's finding.

New people and their agents start at `ONBOARDING.md`. Everyone records their own plan limits in
`BUDGETS.md`, because no account can see another account's rate limits.

## Workers

A worker session does one job, pushes, reports in a short paragraph, and stops. It never starts a new target,
a cryptanalytic attempt, or a write-up that its brief did not name. The orchestrator updates `status.json`,
`STATUS.md` and the published board after every worker report.

The room: `ROOM.md` is the second channel. A worker reads its last 30 lines before its first action and
appends one line when it learns something another worker might need, before it edits a shared file, and
when it stops (`done`). A `flag` line is an interjection: the orchestrator reads every flag before the next
assignment and answers it in the brief or in the room. Lines are signals, not reports; reports go in the
worker's final paragraph and NOTES.md. Duplicate work (two sessions auditing the same claim on 20 Sept 2026)
is what the room prevents.

Two hats, never one session: the **solver** produces readings and the search log of what it checked; the
**verifier** receives the plaintext, the ciphertext and that log, and searches to disprove novelty (rule 10).
A solver brief ends "report what was found and where it was not found; do not classify novelty". A verifier
brief lists the source families to cover (canonical editions, sender- and recipient-specific edited
correspondence, the holding archive's catalogue and blog, the transcription project's pages, Google Books,
HathiTrust, Internet Archive, GitHub cipher projects, scholarship), requires a phrase search on the decoded
text, requires a log of every family searched and every one unreachable, and ends with an N-class per item in
AUDIT.md plus corrections to any over-claiming sentence in the target's files. The orchestrator moves a target
to "Novelty verified" only from AUDIT.md, and repeats to the person only the class and its safe sentence.

**Verifier brief (template).** Used before any reading is described outside the repo as new. The verifier is
a session other than the solver's and does not protect the solver's conclusions.

```
VERIFIER: <target folder>. Claim under audit: <the sentence as the repo states it>.
1. Extract from the repo, per item: date, sender, recipient, place, plaintext as read, ciphertext,
   distinctive phrases, archive identifiers, and exactly what the solver searched (sources, identifiers,
   method, date).
2. Search independently: by date, sender+recipient, quoted phrases, ciphertext words and identifiers, in
   (a) the canonical series, its index and its supplements; (b) the sender's and the recipient's printed
   correspondence; (c) the documentary editions for the period; (d) the holding archive's catalogue,
   blog and project pages; (e) full-text search on Internet Archive, HathiTrust and Google Books;
   (f) the solver repositories and cipher blogs; (g) JSTOR / Scholar / dissertations. Log each family
   as searched or unreachable, with what was searched.
3. Classify each item N0-N5 (rule 10) with: prior plaintext (yes/no, where, earliest citation), prior
   decipherment (yes/no), evidence quality, confidence, one safe sentence, one unsafe sentence.
4. Postmortem: name the failure, the files and sentences that over-claim, and correct them.
5. Write <folder>/AUDIT.md; commit and push; report the classifications and the one-line postmortem.
Do not decode, do not touch other targets, do not print or commit credentials.
```

## Usage (tokens are the budget)

The person's plan is a fixed window of usage, not a bill. A worker that burns it stops every other session.
Every brief states a cap in dollars of usage (the session metadata's cost figure) and the worker stops at it.

1. **Tier the model to the job.** Blind searches, catalogue sweeps, harvesting, transcription passes and any
   job whose output is checked by another agent run on Sonnet (`claude-sonnet-5`). Reconciliation of passes,
   key reading, cipher reasoning and verifier verdicts run on the strongest model. The orchestrator sets the
   model when it creates the session; a worker sets it when it spawns subagents.
2. **Scripts read, models judge.** Never have a model read an Official Records volume, a 400-page dictionary
   or a 2,000-row key to find one thing. Fetch the text once, grep or parse it with a script, and give the
   model the hits. decode.py, check.py and freq.py are the pattern.
3. **Digests, not repositories.** Workers read LESSONS.md and LANDSCAPE.md, not the solver repositories in
   full. Clone a repository only to grep it for a named target.
4. **Fetch once, keep a manifest.** Images and page text go to disk with images/manifest.json on the first
   fetch; later passes read the disk.
5. **Compact outputs.** Worker results are TSV, JSON or a short markdown table with a five-line report; prose
   is for NOTES.md sections the person will read. The person has said machine-shaped files are fine.
6. **Fan-out limits.** At most four subagents at once per worker; two transcription passes, not three, unless
   the two disagree on more than a tenth of the rows.
7. **Stop when the brief is met.** A worker does not continue into follow-ups (a sweep of sister copies, an
   audit of its own) that its brief did not name; it writes the follow-up as a one-line suggestion in NOTES.md.

## Access playbook

Getting the material is most of the work. Try routes in this order and record which one worked in NOTES.md:

1. **A JSON API or plain URL with curl**, with a browser User-Agent (`-A "Mozilla/5.0"`). Gallica IIIF, TNA
   Discovery's API, the Huntington's CONTENTdm API and the Internet Archive all serve this way.
2. **A real browser.** Sites that answer curl with 403, 202, a JavaScript challenge or a Cloudflare page
   (HathiTrust, PARES, Spink, TNA Discovery record pages, Yale) usually serve headless Chromium. Use
   `NODE_PATH=$(npm root -g) node tools/browser_fetch.js URL out.html --shot out.png`, which drives the
   Chromium bundled in this environment. It fills a search box with `--type "css=text"` and waits for
   `--selector`. Read the saved HTML with `python3 tools/html2text.py` or the screenshot with the image reader.
   Known on 20 Sept 2026: in cloud containers Chromium fails every HTTPS page with `ERR_CERT_AUTHORITY_INVALID`
   because it does not trust the container's TLS-intercepting proxy CA (curl and Node do, through environment
   variables). The fix is `apt-get install -y libnss3-tools && certutil -d sql:$HOME/.pki/nssdb -A -t "C,," -n
   ccr-agent-proxy -i /root/.ccr/agent-proxy-ca.crt` once per container (the script prints this hint); a worker's
   permission policy may refuse it, in which case say so and use the APIs below. Never use `ignoreHTTPSErrors`.
   Confirmed 20 Sept 2026: the setup script now runs this fix automatically in a fresh container, and it works —
   `certutil -L` lists `ccr-agent-proxy` at session start and `tools/browser_fetch.js` renders ordinary HTTPS
   pages (e.g. archive.org) with no `ERR_CERT_AUTHORITY_INVALID`, confirming the cert problem itself is fixed.
   It does not, on its own, get past a site's own Cloudflare bot challenge: HathiTrust and manuscripts.nls.uk
   both still served a "Performing security verification" Cloudflare interstitial to the tool after the fix,
   confirmed by screenshot, unrelated to the certificate. For a Cloudflare-blocked site, try the Internet
   Archive Wayback Machine instead (`web.archive.org` is not Cloudflare-protected here): find the archived URL
   with the CDX API, `https://web.archive.org/cdx/search/cdx?url=<site>&output=json`, then fetch
   `https://web.archive.org/web/<timestamp>if_/<original-url>` with `tools/browser_fetch.js` (the `if_` suffix
   avoids the wayback toolbar frame breaking `--selector`/`--type`; a bare fetch without it can return a stub
   `upstream request failed` — retry once before concluding the capture is unreachable).
   **HathiTrust without a browser:** the site itself is Cloudflare-challenged for curl, but the Bibliographic API
   (`catalog.hathitrust.org/api/volumes/brief/recordnumber/N.json`, `oclc/N.json`; needs a full Chrome User-Agent
   string) gives volume ids, and the HTRC Extracted Features API
   (`data.htrc.illinois.edu/ef-api/volumes/HTID/pages?pos=false`) gives per-page word counts for every volume;
   `tools/htrc_ef_headwords.py` uses both to place headwords. Record numbers come from web search restricted to
   catalog.hathitrust.org, the Online Books Page, or OCLC numbers from Open Library's search API.
3. **Credentials from the environment.** Logins the person has set up are exposed as environment variables
   (`DECODE_USER` and `DECODE_PASS` for de-crypt.org). Use them through the browser tool or a curl login flow.
   Never print them, never write them to the repo.
   Google Books: the API answers unauthenticated requests with HTTP 429 after a few dozen calls. The person
   has set GOOGLE_BOOKS_KEY in the environment (20 Sept 2026): append `&key=$GOOGLE_BOOKS_KEY` to every
   `www.googleapis.com/books/v1/volumes` call. Full-text hits still need the volume to be full view; use
   `filter=full` and read pages through the volume's `accessInfo` links. Never print the key.
   Internet Archive: IA_USER and IA_PASS (set 20 Sept 2026) let a worker borrow a lending-only book for one
   hour and read its pages (the `internetarchive` Python library's `ia configure` flow, or the web login with
   a cookie jar; the loan endpoint is /services/loans/loan/ with action browse_book, then the page images
   through the BookReader endpoints). Rules: one book at a time, for a named page check, returned when done,
   never bulk; the account is for the person's own reading. Search-inside and the full-text API need no login.
   First use, 20 Sept 2026: login failed both ways -- the `internetarchive` library's `ia configure`
   (`services/xauthn/?op=login`) and archive.org's current `/login` page both require an email address, and
   IA_USER as set is not one (`account_not_found` from the API; the login page renders only an "Email
   address" field, no username field). Borrowing could not be tested; `tools/ia_borrow.py` implements the
   flow (xauthn login, loan/browse_book, BookReaderJSIA.php for page images, loan/return_loan) but its image
   step is unverified pending a corrected IA_USER.
   Retried 21 Sept 2026 after the person rotated IA_USER to an email-format value and the password: login
   still fails, same `{"success": false, "values": {"reason": "account_not_found"}}` from the xauthn API
   (HTTP 401), but now because archive.org has no account under that email at all, not a format problem.
   Not retried further this session (lockout risk on repeated failed logins). Borrowing and the image step
   remain untested; the person needs to confirm which archive.org account IA_USER/IA_PASS are meant to
   reach before another attempt (flagged in ROOM.md/ASKS.md).
   Without login: `be-api.us.archive.org/fts/v1/search?q=<term>&identifier=<id>` full-text-searches even
   lending-only items and returns snippet highlights, but its `page_num` field is not a real page locator --
   it equals the item's total `imagecount` (confirmed on two different items) -- so this route can confirm a
   term is present/absent and show the surrounding sentence, but cannot cite a page number; page images and
   raw OCR files (`_djvu.txt`, `_hocr_searchtext.txt.gz`, `_page_numbers.json`) all 403 without a valid loan.
   JSTOR: JSTOR_USER and JSTOR_PASS (set 20 Sept 2026) give 100 article reads a month for the verifier's
   scholarship checks; log the article and date in AUDIT.md and never print the credentials.
   **DECODE (de-crypt.org) login, confirmed 20 Sept 2026:** plain CSRF-protected form POST, no client-side
   password encryption despite the site's `ENCRYPTED_PASSWORD` flag (that flag is server-side hashing only;
   checked the unminified `ewcore.js` behind its source map, no JS touches the password field). GET
   `/decrypt-web/login`, read the `csrf_name`/`csrf_value` hidden-input pair, POST them plus `username` and
   `password` back to the same URL with a cookie jar (`-c`/`-b`). A failed login re-renders the same login page
   at HTTP 200 with `"IS_LOGGEDIN":false` embedded in the page's JSON, not a distinct status code or redirect
   — that string is the only reliable success/failure signal. `tools/decode_fetch.sh RECORD_ID OUT_DIR`
   implements this and then fetches `/decrypt-web/RecordsView/RECORD_ID` plus its attachments; it reads
   `DECODE_USER`/`DECODE_PASS` from the environment and never echoes them. As of that date the credentials in
   this environment were rejected ("Incorrect user name or password", confirmed by screenshot) — this is a
   working flow, not a working login; do not retry it repeatedly against the live account (risk of lockout).
   Update, 21 Sept 2026: the person rotated the password and reset `DECODE_USER`/`DECODE_PASS`; a single test
   login with the new pair was also rejected (same `IS_LOGGEDIN:false` signal). One attempt only, per the
   handling rule below — do not retry further without the person confirming the account again (ASKS.md row 1).
   Handling rule (20 Sept 2026, after two workers echoed a password into their own transcripts): never run
   `env`, `printenv`, `set`, `export -p` or `cat /proc/*/environ` unfiltered; never `curl -v`, `--trace` or
   `set -x` on a command that carries a credential; pass credentials only through `--netrc-file` (mode 600,
   deleted after), a cookie jar, or a library's own config, and test presence with `test -n`. A transcript is
   the person's private log, but a password in it must still be rotated, so say so at once in ROOM.md.
   Google Books also needs `&country=US` on every call (the API otherwise answers 403 "Cannot determine user
   location" from cloud containers).
4. **The person.** Paywalls (State Papers Online, Gale), copy orders, payments, emails to archives and dealers,
   and captchas the browser cannot pass. Write the exact request into the target's `REQUEST.md`, mark the
   target "waiting on you" in the report, and stop. Batch several asks into one REQUEST.md rather than
   stopping at the first.

Test reachability before planning: `curl -sS -o /dev/null -w "%{http_code}" <url>`; `000` means the egress
policy blocks it, in which case say so and stop, since no route above will help.

Once a series is identified as useful (a ledger, a volume, a cipher book), fetch all of it once and record the
manifest (URLs, ids, sizes) in the target folder, so later workers do not refetch. Keep committed images under
30 MB per folder; for more, keep the manifest and a sample and note where the rest can be re-fetched.


## Improvement loop

The orchestrator writes a LEDGER.md row when it archives a worker (role, model, cost, outcome code, lesson).
Briefs are copies of the templates in `.claude/briefs/`; a lesson becomes a template edit, not a note. A
retrospective session (`.claude/briefs/retrospective.md`) runs weekly on a schedule and after any worker
scored X or F, reads the ledger and the week's log, and proposes at most five concrete changes as diffs in
RETRO-<date>.md. The orchestrator applies changes that only touch briefs, tools or workflows, records them in
the ledger, and puts anything that changes the goal, the spend or the person's asks to the person with a
recommendation. Success is measured as cost per delivered result by role, share of workers that stop on
brief, over-claims caught before the person sees them, and whether the top of the queue produces results.

## Git

Commit directly to `main`. No pull requests unless asked. Stage by explicit path when several sessions share
the repo. Never rewrite history.
