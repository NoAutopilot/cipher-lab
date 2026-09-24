# ciphers/reddit-runaway-2021 -- NOTES

Status: found-solved (conditional: reported by the original poster; the decoded text is not held in this
repository, rule 9 -- a minor and an open police matter are involved)

## r/puzzles solve thread, confirmed 24 Sept 2026

The OP's own comments in `thread.md` (9 May 2021 and 24 Dec 2023) say "someone in r/puzzles believes they
cracked it and forwarded their findings to the authorities" / "gave them the police phone and case
numbers", without naming the thread. Found and confirmed it via the Reddit API:

- Thread: r/puzzles, id `mwhlc8`, title "Help: Coded note left by teenage runaway".
- Posted 2021-04-22 10:37 UTC (created_utc 1619133434) -- about 11 minutes *before* the r/ciphers crosspost
  already on file here (`mwhtp0`, created_utc 1619134120). Same OP account, same day, same case: the
  thread's first comment (an OP edit) is word-for-word the same "17 year old girl... move back to
  [place] from [place]" text already redacted in `thread.md`'s equivalent r/ciphers comment, which is how
  this match was confirmed (not just the title and date).
- One comment, posted roughly 7.8 hours after the OP's post, claims to have "mostly cracked it" (following
  another commenter's suggestion that it was a simple substitution) and describes the result only in
  general terms (two short lists; the poster mentions spelling mistakes made it harder). **The decoded
  words themselves are not recorded here or anywhere in this repository** (rule 9).
- The OP's later comments in that thread accept that a decipherment existed ("What's important is that
  someone was able to decode it and hopefully it helps in some small way") and gave the solver a police
  non-emergency line and case number to pass the findings on; the OP did not independently verify the
  decoded content's accuracy anywhere in the thread itself. So: **the claimed reading was accepted by the
  OP as a genuine decipherment (sufficient to act on and refer to police), not verified against
  independent knowledge of the actual message.**
- Every Reddit username, the police phone number and case number, and the city/state named in that thread
  are deliberately omitted from this file (rule 9). Its raw JSON was read once, in the scratchpad, to
  confirm the match, and was not saved to the repository.

## Search log (24 Sept 2026)

1. `GET oauth.reddit.com/r/puzzles/search?q=coded+message+runaway&restrict_sr=1&sort=relevance&raw_json=1`
   -- HTTP 200, 25 results; row 4 ("Help: Coded note left by teenage runaway", id `mwhlc8`, created_utc
   1619133434) matched on date and framing against the r/ciphers post already on file.
2. `GET oauth.reddit.com/r/puzzles/comments/mwhlc8?raw_json=1` -- HTTP 200; confirmed the match (identical
   OP wording) and the solve/acceptance/police-referral content summarized above.
- 2 requests to reddit hosts for this confirmation (job B of this run); combined with job A's 8 requests
  (see `ciphers/reddit-oldbook-1600s/thread.md`) this run used 10 of its 10-request cap, all >=1.5s apart,
  User-Agent `cipher-lab research script (contact via repository) v1`, all HTTP 200.

## Do not

- Do not decode or reproduce the pigpen/underline cipher in `thread.md` (this repository has no reading of
  it, on purpose).
- Do not fetch the r/puzzles thread `mwhlc8` again without a stated reason; this summary plus the search
  log above are sufficient to support the `found-solved` status.
