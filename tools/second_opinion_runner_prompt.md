# Standing prompt for an outside model's scheduled task (ChatGPT with the GitHub plugin)

Set up once by the owner as a scheduled task in ChatGPT (every 6 hours is enough). The task reads the queue below,
answers one prompt per run, and posts the answer back as a pull request. Nobody pastes anything by hand.
Our side: lane orchestrators append a row to `SECOND-OPINIONS-QUEUE.tsv` (label, folder, prompt path, date,
`queued`) whenever a reading reaches N3 and its `PROMPT-chatgpt.md` is written; the parent check-in lists open
pull requests, matches `[SO-...]` titles to rows, marks them `posted` with the PR number, and hands each to the
verification lane in ROOM.md. Labels are `SO-<TARGET>` and appear in the branch, the PR title and the file header.

## Paste this as the scheduled task's instruction

You are the cipher-lab second-opinion runner. Each run, using the GitHub tools on the repository
NoAutopilot/cipher-lab:
1. Read the file SECOND-OPINIONS-QUEUE.tsv on the main branch. It is tab-separated with columns label, folder,
   prompt, added, status, pr.
2. For each row in order, check whether a branch named second-opinion/<label> or an open or merged pull request
   whose title starts with [<label>] already exists. Skip those. Take the first row whose status is `queued` and
   has neither. If there is none, reply "nothing queued" and stop; do not write anything.
3. Read the file named in that row's prompt column and follow it exactly: research the question adversarially
   (prior print, prior decipherment, errors, leads, confidence), with checkable citations (author, title, year,
   volume, page, URL) and "unverified" on anything you cannot page-cite. Never use the words first, new,
   unpublished, unread or never printed about our reading.
4. Create the branch second-opinion/<label> from main, add exactly one file at
   <folder>/second-opinions/chatgpt-<UTC date>.md whose first lines are the header the prompt specifies (label,
   model, date, prompt), and open a pull request from that branch to main titled exactly as the prompt says
   (it begins with [<label>]). Write in the PR body one line: "Label <label>. Leads, not verdicts; the
   repository's verifier checks every citation." Do not edit SECOND-OPINIONS-QUEUE.tsv, do not touch any other
   file, never commit to main, never merge.
5. One row per run. Finish with a one-line summary naming the label and the PR number.

## Our side of the loop (24 Sept 2026, owner's request: show the state on the board)

The queue's `status` column drives a chip on the board next to each reading (`tools/build_dashboard.py`, matched by
folder and the label's folio or item token):

- `queued` (grey circle): the prompt is written, no pull request yet.
- `posted` (blue envelope), `pr` = the pull request number: the runner's file arrived. The parent check-in sets this when
  it sees an open `[SO-<label>]` pull request, and hands the file to a verifier in ROOM.md ("for LANE V4: second opinion
  <label> to check, PR #n").
- `checked` (green tick), `outcome` = one short phrase the verifier writes after checking every citation in the file
  against the source, e.g. "no prior print found; two citation errors corrected in AUDIT.md" or "prior print found,
  reclassed N1". The verifier appends its findings to the target's AUDIT.md ("Second opinion <label>, checked <date>")
  and corrects the folder; only AUDIT.md changes a class. The pull request is then closed without merging (the file is
  kept on its branch, and the verifier copies it into the folder under second-opinions/ with the label in the header).
- `withdrawn (<reason>)`: the reading was reclassed below N3 before the runner reached it.

The wording is "second opinion checked", never "verified" or "confirmed": rule 10 keeps verdicts with the verifier, and
an outside model's "not found" is a search result, like ours.
