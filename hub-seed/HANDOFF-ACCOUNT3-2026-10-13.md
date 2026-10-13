# Handoff from the account-3 parent (13 Oct 2026)

Written 05:3x UTC 13 Oct 2026 by the account-3 parent (session_0198Cv8ypBfBVfRToKVWx33M). Account 3 stands down. The
owner needs its remaining usage for other projects, so **no work runs on account 3** until he says otherwise. Nothing is
running and no check-ins are scheduled; the last state is in ROOM.md (02:2x and 05:2x UTC 12-13 Oct).

## Usage, as the owner read it (13 Oct, about 05:3x UTC)

| Account | Usage used | Use for |
|---|---|---|
| 4 | nearly none | the parent orchestrator role (this handoff) and most workers |
| 2 | 16% | workers |
| 1 (owner account) | about half | its own orchestrator as now; light work |
| 3 | 87% | nothing: reserved by the owner |

## The owner's feedback (13 Oct), and the operating rules it implies

a. **He lost track of what was happening and when.** Too many threads ran at once (a sorter template rebuild, two batches of ten
   experiments, several read-only research workflows), and updates came as long messages. Rule: at most two jobs in flight
   per orchestrator; every reply to him opens with three short lines, "Running now / Finished since last time / Waiting on
   you", each with a clock time (Pacific first); one line per job, never a wall of text.
b. **Tokens were not spent efficiently.** A small sorter change became a 30+ minute pipeline (builder running the full browser
   suite, three adversarial checkers, a fixer, a recheck). TXE4-0, a script-only repair priced at 4.5, cost 25.9 (4.3x);
   the TXE4 batch cost about 186 against an estimate of about 125. Rules: size the process to the change (a UI tweak is one
   agent plus the tests it touches, and the owner's own phone is the final check); adversarial rounds only for anything that
   changes a reading, a label file or a count; read get_session for every worker every 30 minutes and interrupt at 1.3x cap;
   do not run the session in an always-use-workflows mode for routine work.
c. **Cross-account usage was never under control.** No account sees another's usage. get_session returns
   `rate_limit_info` (status, resetsAt) for every session an account owns: at each check-in, write each account's status
   and reset time into one table (BUDGETS.md) and show it in every report as one line per account. Ask the owner for the
   other accounts' percentages when a decision depends on them.
d. **Eckert moved; most others did not.** Eckert had what the others lack: a known cipher system or codebook, a large body of
   ciphertext, clean images and plaintext that can be checked. Prefer targets with that shape.
e. **The sign sorter was not clearly useful.** research/OWNER-SORT-IMPACT-2026-10-12.md: no counted board result depends on any
   of his sorts; half were never exported or applied; the no.87 gain once credited to his sort was a machine re-read. Rules:
   ask him to sort only when the sort is the named next step on a near-solve AND a pre-registered test will consume it
   within a day; after every sort, tell him in one line what it changed. No open-ended sorter requests.
f. (not used)
g. **He wants one keystone target, hammered until it gives, that would matter to history.** See below.

## Keystone proposal (the owner decides)

**Saint-Gouard to the King, Madrid, 10 Oct 1573** (`ciphers/fr16104-vivonne-spain-1572`, BnF fr.16105 ff.190r-194r; PROGRESS row
"Vivonne ink 63"). Jean de Vivonne, French ambassador in Spain, reporting to Charles IX in the year after the Saint
Bartholomew massacre. About 15,760 cipher signs, a published key, 12,151 signs read firmly (H 11,932), text not found in print
so far. It is held at depth D1 because no clause yet reads cleanly above the authentication distance: the bottleneck is the
transcription of this hand, and one print check (Flament 1996, LOCAL-QUEUE L52) stands between it and N4. Every earlier
transcription experiment ran on this hand's sister leaves (Vivonne f.102r), so the tools and the known-answer pages are in place.
Alternatives: Mercy 1648 (92% read with our own key, one code open; the quickest count) and Armstrong to Madison 1808 (US
history, Tomokiyo asked; hard, shorthand, 0% read).

## Open items (nothing urgent; pick up only what the keystone or the owner needs)

- Sorter R12 (page lock, swipe through a pile) is built on branch `wip/acct3-sorter-swipe` (16b8e0c7b), not merged, not checked;
  the bottom bar "Back / Doesn't belong / Fits" is not built. The 27 live sorter pages are account-3 artifacts on template
  2026-10-09.7: only account 3 can update them. Pages published from account 4 are private to account 4 until shared.
- Owner sorts never applied: Armstrong shorthand (R9GrLoF1), Armstrong marks, Debosnys, Matignon (partial export committed),
  Harley 287, Birago f.117, Oldenbarnevelt 2442, Pisany f.75. Modena g/q applied to labels 12 Oct; re-key pending (~3).
- Birago f.144r: the committed owner reading still carries a pick he withdrew on 4 Oct (L04.1.7); L06.7/L06.11 may be one
  position off. Stale registers: ASKS 118 and 128 'open', sorter_families.tsv lists ASKS-118 as open, NEXT-STEPS.tsv points
  Bergh at the old page SLHhvXfh.
- TXE3/TXE4 transcription experiments: all done; none of the 21 beat the plain two-reader reading on known-answer pages.
  TXE3-10's pair classifier (6 fixed / 0 broken, p 0.031) still awaits a verifier ruling.
- Owner desk (https://claude.ai/artifact/GNMEYAR5C1ZeBHvJ9bXYxm): card bnf-quote-010032 (Clairambault 1161: confirm the
  document, decline the 150-dpi PDF). His runners: the desk runner (LOCAL-QUEUE L71-L78, two Gallica fetches), the send
  runner (SEND-QUEUE S3, S4, S7 queued since 5-9 Oct) and the JSTOR runner (232 rows) have not run lately.
- Gallica answers 403 to the cloud; it is the main blocker for accounts 1 and 2. Image fetches go through the owner's desk runner.

## Paste this into a new session on account 4

```
You are the parent orchestrator for cipher-lab on account 4 (CIPHERLAB_ACCOUNT=4), taking over from the account-3
parent, which has stood down to save that account's usage. Read CLAUDE.md, then hub-seed/HANDOFF-ACCOUNT3-2026-10-13.md
in full; its rules (a)-(e) are the owner's feedback of 13 Oct and bind you. Do not start any work on account 3.
First: run python3 tools/room.py --start, read the last 40 lines of ROOM.md, write a claim line, and ask the owner one
question: which keystone target to hammer (the handoff proposes Saint-Gouard 1573, with Mercy 1648 and Armstrong 1808
as alternatives). Until he answers, run nothing but that question. Keep at most two jobs in flight, open every reply with
Running now / Finished / Waiting on you, and read every worker's get_session cost every 30 minutes.
```
