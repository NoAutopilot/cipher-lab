# One-off resume prompt for the owner's ChatGPT instance (5 Oct 2026)

Written by the account-3 orchestrator after the owner's 5 Oct request: the ChatGPT instance (the earlier JSTOR /
second-opinion runner, and the Armstrong research loop of 27-28 Sept) may hold work it never reported because it ran
out of usage. This prompt has it (1) report that work back, then (2) take the second-opinion queue. Parent-owned file
(CLAUDE.md "Any session may propose an edit to a tools/*_runner_prompt.md"); self-contained, no credentials.

## Paste this

You are the cipher-lab research runner, working on the public GitHub repository NoAutopilot/cipher-lab with the
GitHub tools. Read https://github.com/NoAutopilot/cipher-lab/blob/main/CLAUDE.md rule 10 first: never call anything
in that repository "first", "new", "unpublished", "unread" or "never printed".

PART 1 -- report unfinished work (do this before anything else).
1. Look back over your own earlier conversations and tasks for this project: the Armstrong-Madison 1808 research loop
   (your last checkpoint files are in ciphers/armstrong-madison-1808/second-opinions/, latest chatgpt-checkpoint-
   2026-09-27-2026.md and chatgpt-continuity-2026-09-27.md; your pull requests #58-#63, 28 Sept), any JSTOR or
   second-opinion run, and anything else you started for cipher-lab.
2. For every piece of work that is NOT already in the repository (check main, your pull requests and branches
   second-opinion/* and jstor-run*): finish it if it needs under about 20 minutes; otherwise write down exactly where
   it stopped.
3. Create the branch chatgpt-resume/2026-10-05 from main and add ONE file,
   ciphers/armstrong-madison-1808/second-opinions/chatgpt-resume-2026-10-05.md (if the work concerns other targets,
   add one more file per target at ciphers/<target folder>/second-opinions/chatgpt-resume-2026-10-05.md). Each file:
   first lines `label: CHATGPT-RESUME`, `model: <your model>`, `date: <UTC date>`; then sections "Finished since last
   report" (findings with checkable citations: author, title, year, volume, page, URL; "unverified" on anything not
   page-cited), "Unfinished -- where it stopped" (each item: what, last step done, next step, files/links), and
   "Suggestions" (at most 3 next research steps you think have the most leverage, one line each).
4. Open a pull request titled `[CHATGPT-RESUME] unfinished work report, 5 Oct 2026` with one-line body "Leads, not
   verdicts; the repository's verifier checks every citation." Never commit to main, never merge, never edit any
   file outside those you add.

PART 2 -- second opinions (after Part 1's pull request is open).
Follow https://github.com/NoAutopilot/cipher-lab/blob/main/tools/second_opinion_runner_prompt.md section "Paste
this", steps 1-5, for as many queued rows as your usage allows (one pull request per row). Stop cleanly when usage
runs low: open the pull request for the row you finished rather than leaving a half-done row unreported.

End with a short summary: the pull request numbers, and one line on what you could not finish.
