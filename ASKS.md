# Asks

Anything blocked on a human, from any project, any account. An agent that gets blocked writes a row here,
because nobody can see into another account's sessions. Clear a row by changing its status to `done` with
the date; do not delete it.

Status: `open`, `done`, `dropped` (with a reason), `waiting` (with who and since when).

| # | Raised | Project | What is needed | Exact action | Who can do it | Status |
|---|---|---|---|---|---|---|
| 1 | 20 Sept | cipher-lab | DECODE login rejected, password also leaked into a transcript; rotated password (set ~21 Sept) tested once and also rejected ("Incorrect user name or password") — blocks record 8725 (intercepted-royalist-1646 f.104), R413 (boswell-1628), R4930 (randolph-sussex-1569 key fit) | Re-check the de-crypt.org account (username spelling, account lock, password entry) and update `DECODE_USER`/`DECODE_PASS` again if needed; do not have workers retry against the live account meanwhile (lockout risk) | Ryan | open |
| 2 | 20 Sept | cipher-lab | archive.org login rejected. Updated 21 Sept: `IA_USER` is now an email-format value and the password was rotated, but login still fails with `account_not_found` -- archive.org has no account under that email at all (not a format problem this time) | Confirm which archive.org account IA_USER/IA_PASS should reach (mistyped email, a different registered email, or an account that is sign-in-with-Google only and has no xauthn password login) and update the variables to match; do not resubmit the same pair again without checking first (lockout risk) | Ryan | open |
| 3 | 20 Sept | cipher-lab | Spink lot 1184: does it include a pocket dictionary? (Sale day is 23 Sept; the 19 catalogue photographs are already saved in `ciphers/wellington-maitland-1812/images/`, so only the question lapses, not the images) | One email before the 23 Sept sale, contact on the lot page | Ryan, or a teammate if authorised | open |
| 4 | 20 Sept | cipher-lab | Stair 1710 scans, about $20 | Order four TIFFs per `ciphers/stair-townshend-1710/REQUEST.md` | Ryan (payment) | open |
| 5 | 20 Sept | cipher-lab | NLS MS 20769 quote and five-leaf sample | Copy enquiry per `ciphers/nls-20769/REQUEST.md` | Ryan, or a teammate if authorised | open |
| 6 | 20 Sept | cipher-lab | British Library quote for Add MS 32093 f.423 | Imaging Services enquiry per `ciphers/monck-1660/REQUEST.md` | Ryan, or a teammate if authorised | open |
| 7 | 21 Sept | cipher-lab | Whitworth 1707: is one unread clause worth a Kew order? | A decision, then the order if yes | Ryan | open |
| 8 | 21 Sept | cipher-lab | Board is published to a private artifact; the team cannot see it | Enable GitHub Pages, main branch, `/docs` folder | Ryan (repo settings) | open |
| 9 | 21 Sept | cipher-lab | Teammates need repository access | Add collaborators with write access | Ryan (repo settings) | open |
| 10 | 23 Sept | cipher-lab | The noautopilotytbiz account's cloud environment (`env_01EKcbReEPpDXpAoLWEYLGv8`) has none of the seven credential variables set: `DECODE_USER`, `DECODE_PASS`, `IA_USER`, `IA_PASS`, `GOOGLE_BOOKS_KEY`, `JSTOR_USER`, `JSTOR_PASS` are all unset there (checked with `test -n` only, 23 Sept 2026). Blocks ASSIGNMENTS row 2 (Google Books print checks for Cobham 1588 and Rupert 1645) and any verifier JSTOR check run from this account | Add the same seven variables to that environment in the claude.ai environment settings, at least `GOOGLE_BOOKS_KEY` (working) and `JSTOR_USER`/`JSTOR_PASS`; DECODE and IA only once rows 1 and 2 are resolved | Ryan (environment settings) | open |
