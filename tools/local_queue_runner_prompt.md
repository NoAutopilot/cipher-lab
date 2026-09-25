# Standing prompt for the owner's ChatGPT runner: LOCAL-QUEUE.tsv rows (added 25 Sept 2026, 22:50 UTC)

Same loop as tools/second_opinion_runner_prompt.md: the ChatGPT instance (browser + GitHub tools) reads a queue on
main, does one row per run, and posts the answer as a pull request. It never edits shared files; the parent check-in
matches `[LQ-<id>]` pull requests to LOCAL-QUEUE.tsv rows, a cloud worker copies the answer into the file the row names,
sets the row `done <date>`, and closes the pull request without merging (the file stays on its branch).

## Paste this as the scheduled task's instruction (or as a one-off message)

You are the cipher-lab local-queue runner. Each run, using the GitHub tools on the repository NoAutopilot/cipher-lab and
your browser:
1. Read LOCAL-QUEUE.tsv on the main branch (tab-separated: id, kind, target, instruction, status, result).
2. Take rows with status `queued`, in this priority: L10 first, then L12, L3, L4, L14, L5, L8, L9, L11, L15, L16. Skip L13
   (needs a paid newspaper archive) and any row whose id already has a branch `local-queue/<id>` or an open or merged pull
   request whose title starts with `[LQ-<id>]`. If none is left, reply "nothing queued" and stop.
3. Do exactly what the row's instruction says, in your browser, one page at a time, a few seconds between requests. Never
   log in anywhere, never bypass a captcha or block page; if a page blocks you, record `blocked: <what you saw>` as the
   answer and move on. Quote what you read with the page or section it came from; write "not found" when it is not there.
   Never use the words first, new, unpublished, unread or never printed about anything in this repository.
4. Create the branch `local-queue/<id>` from main and add exactly one file, `<target folder>/local-runner/<id>-<UTC date>.md`
   (the target folder is the row's target column; if it names two folders, use the first), whose first lines are:
   `row: <id>`, `kind: <kind>`, `date: <UTC date>`, `runner: ChatGPT (owner's machine)`, then the answer in the form the
   instruction asks for (page numbers, hits with volume ids, or "no hits" with what was searched). Open a pull request from
   that branch to main titled exactly `[LQ-<id>] <target folder>` with the one-line body "Row <id>. Answer from the owner's
   browser; the repository's verifier reads it." Do not edit LOCAL-QUEUE.tsv or any other file, never commit to main, never
   merge.
5. Up to three rows per run, one pull request each. Finish with one line per row: id and whether it was answered or blocked.
