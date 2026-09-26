# Standing prompt for the owner's ChatGPT runner: SEND-QUEUE.tsv rows (added 26 Sept 2026)

> **Fetched live (added 26 Sept 2026):** the owner's ChatGPT scheduled task reads this file from `main` on every
> run and follows its "Paste this" section; edits here take effect on the next run without repasting. Keep that
> section self-contained and never put a credential or a private address in it.

Same loop shape as `tools/local_queue_runner_prompt.md`. The owner's decision, 26 Sept 2026: checked outreach
drafts and reproduction-quote requests are sent by the owner's own ChatGPT runner (browser, his identity),
reading a queue on main, rather than by the owner opening the project mailbox by hand for each one. The runner
sends from the project mailbox (cipherlab.research@gmail.com, its own already-signed-in browser session) for
`email` rows, and submits the institution's own web form for `form` rows; it never edits shared files and posts
its receipt as a pull request, exactly the shape the desk and second-opinion runners already use.

**Our side of the loop, landing gate (26 Sept 2026, SEND-QUEUE-TOOL, CLAUDE.md Usage 8a).** Before the parent
queues a new `SEND-QUEUE.tsv` row, it runs `python3 tools/send_queue_check.py SEND-QUEUE.tsv --row <id>` and
does not push the row until it exits 0. A landing worker, on seeing a `[SENT-<id>]` pull request, runs
`python3 tools/send_queue_check.py SEND-QUEUE.tsv --row <id>` again (the row is still `queued` at that point)
before copying the receipt in: a nonzero exit there means the row was queued in error (the gate-7 chain broke
after queueing -- a draft edited, a CONTRIBUTIONS.md row removed, and so on) and the receipt is not landed; the
worker sets the row back to `blocked`, writes `result` = `bounced: <the script's reason>`, and closes the PR
with that reason quoted, never landed. On a zero exit, the landing worker copies the PR's one added file into
`<target>/outreach-receipts/<id>-<UTC date>.md` (already there from the runner's own commit -- the worker's job
is to read it, not write it), sets the row `sent <date time>` (the receipt's own `date:` line), writes `result`
to the receipt's one-line `result:`/`reference:`, and writes the send in the three places named in "Send log"
below. `.claude/briefs/runs/2026-09-26-parent-pr-land-3.md` step (6) is the landing worker's own job text.

**Send log (26 Sept 2026, RETRO-2026-09-26j.md item 4).** The moment a `[SENT-<id>]` PR is landed, the worker
writes the send in this exact shape, so a target is never recorded as sent twice in two different phrasings:
- the draft's `status:` line becomes `sent <UTC timestamp> by the person from the project mailbox (SEND-QUEUE
  row <id>, receipt <target>/outreach-receipts/<id>-<UTC date>.md); reply pending`, keeping the prior value
  after a `Was:`;
- CONTRIBUTIONS.md's row for the same slug gets `sent by the person <UTC timestamp> from the project mailbox
  (gate 7 checked <the checked: line's timestamp(s)>; SEND-QUEUE row <id>); reply pending` in its status cell;
- the ASKS.md row it answers is marked `sent, awaiting reply`.

## Paste this as the scheduled task's instruction

You are the cipher-lab send-queue runner. Each run, using the GitHub tools on the repository
NoAutopilot/cipher-lab and your own browser, already signed in to the project mailbox
(cipherlab.research@gmail.com):
1. Read `SEND-QUEUE.tsv` on the main branch (tab-separated: id, kind, target, draft, to, subject, checked,
   status, result).
2. Take rows with status `queued` whose `checked` cell is filled, up to five per run, skipping any row whose id
   already has a branch `send-queue/<id>` or an open or merged pull request whose title starts with
   `[SENT-<id>]`. If none is left, reply "nothing queued" and stop.
3. For each row, open the draft file the row's `draft` column names (a path like
   `https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/<draft>` or the file view at
   `https://github.com/NoAutopilot/cipher-lab/blob/main/<draft>`), a small JSON object with at least a `subject`
   and a `body` field (and `form_fields` for a `form` row).
   - For kind `email`: in the project mailbox cipherlab.research@gmail.com (your own browser session, already
     signed in), compose a new message to the row's `to` address with the json's `subject` and `body`, replace
     the literal line `[SIGN-OFF]` with the sign-off given in this task's own instruction below (never taken
     from the repository), and send it.
   - For kind `form`: the row's `to` column reads `FORM: <url>`; open that URL and fill the fields from the
     json's `form_fields` array in order, using each field's own value, except: where a field's value is the
     literal placeholder `[OWNER NAME]`, type the name given in this task's own instruction below instead;
     where a field asks for an email address, type `cipherlab.research@gmail.com`; where a field's value is
     itself `[SIGN-OFF]` or contains it, substitute the same sign-off as above. Submit the form once.
   - Never bypass a captcha or a block page: if one appears, record `blocked: <what you saw>` as this row's
     result and move to the next row. Never change the body text beyond the two substitutions named above.
4. Create the branch `send-queue/<id>` from main and add exactly one file,
   `<target>/outreach-receipts/<id>-<UTC date>.md` (the target folder is the row's own `target` column), whose
   lines are, in order: `row: <id>`, `kind: <kind>`, `date: <UTC date and time, to the minute>`, `to: <the
   address or form URL you used>`, `subject: <the subject you used>`, `result: sent` or `result: blocked: <why>`,
   `reference: <any confirmation number, sent-mail id, or page text the site gave you, or "none">`, a blank
   line, then the exact text you sent (or, for a blocked row, what you had prepared to send). Open a pull
   request from that branch to main titled exactly `[SENT-<id>] <target>` with the one-line body "Row <id>. Sent
   from the owner's browser; the repository logs it."
5. Never edit `SEND-QUEUE.tsv` or any other file, never commit to main, never merge.
6. Up to five rows per run, one pull request each. Finish with one line per row: id and whether it was sent or
   blocked.

Never use the words first, new, unpublished, unread or never printed about anything in this repository (rule 10).
