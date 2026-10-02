# LIKELY-SOLVES (2 Oct 2026, written by account 3 for the account-4 parent; owner's ask)

Owner: "likely solves in a similar vein to what we've already solved (head start, or similar to our starting target) --
we have a bunch from our scout". Two phases. Phase 1 is one worker; phase 2 is one separate session per candidate
(CLAUDE.md Usage 6: batches >5 run as separate sessions, never one in-container Workflow).

## Phase 1: SHORTLIST (one worker, Fable else Opus 5.5, cap USD 6, box 60 min; scripts read, the model judges)
What has actually produced our results (status.json `results`, KEY-OFFICES.tsv, LESSONS.md): (a) a key we already hold
or a published key of the same office and decade (Tomokiyo's Nevers/Gramont/Danzay/Raince keys, our KEY-OFFICES rows);
(b) a sibling letter with a contemporary decipherment, interlinear gloss or clear copy (adjacent plaintext: WVO 74/98 ->
57/126, Szembek, Thurloe); (c) a printed clear text of the same letter (Bowes/Boyd, Gramont); (d) a sign pool of 2,000+
signs from one sender/office (CLAUDE.md Pipeline 3, pools first).
1. From QUEUE.md (all sections), QUEUE-scores.json, NEXT-STEPS.tsv (open rows), POOLS.tsv and KEY-ADJACENT.tsv /
   KEY-CROSSMATCH.tsv, list every candidate NOT already a ciphers/ folder at partial/solved/found-solved and NOT claimed
   in ROOM.md in the last 6 h, and score it on: shares office+decade with a KEY-OFFICES.tsv row (a); a sibling with a
   period decipherment named in its row or the solver repos (b); a printed edition of the letter named (c); pool size (d);
   images online (free) vs copy order needed; language with a tools/data corpus. Run `python3 tools/design_prior.py` on any
   candidate with ciphertext on disk.
2. Exclude anything the 2 Oct solver diffs (sources/solver-diffs/2026-10-02-*.tsv) show as read or closed by Bourdeau or
   Aymeloglu, and Debosnys.
3. Write ciphers/_triage/likely-solves-2026-10-02.tsv: rank, candidate, folder (or "new"), head start (a/b/c/d with the
   named key, sibling or edition), images (free/order), first cheap test, est. cost, P(first test moves it) with one line why.
   Top 15. A ROOM line with the top 10.

## Phase 2: FIRST TESTS (account-4 parent, one session per candidate, top 10 by expected value = P x value / cost)
Per candidate: `tools/intake_gate_check.py` (check-solved first if it fails -- never deep work on an unverified target),
then exactly its first cheap test WITH the matched control (rule 3; `tools/family_run.py` or a key application with a
shuffled-key control), cap USD 3-5, both numbers into the spec's cheap_test_done or NOTES.md, and the finish-or-blocker
sections at the end. A reading that clears its control is flagged in ROOM.md for a separate verifier; nobody calls it new
(rule 10). Promote to a campaign only what its first test moved (Pipeline 3a).
