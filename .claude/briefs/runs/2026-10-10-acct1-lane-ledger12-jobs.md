# LANE LEDGER-12 worker jobs (account 1, session_011R8J939oZMVV2ZyZZ2LS3W; written 10 Oct 2026 07:4x UTC by date -u)

Lane brief .claude/briefs/lane-ledger.md (+ lane-common-blast.md). WORK-QUEUE row DEFAULT-account-1-20261010-0740. Continues STATUS.md "LANE LEDGER
handoff ... incarnation 10" next items 2-5 and "LANE LEDGER-11 handoff" next items 1 and 4. Every ROOM line ends "for LANE LEDGER-12 (account 1)".
seven_day allowed_warning has been on since 9 Oct (not a stop under lane-common-blast; say so in your done line if you see it).

Intake gate: `python3 tools/intake_gate_check.py eckert-1864` -> "eckert-1864: partial (line 3) -- edition/page or full-text-search citation found within
6 lines" (exit 0, 07:44 UTC 10 Oct). Re-run it yourself before deep work and paste the line.

**Common to every worker** -- exactly the "Common to every worker" block of .claude/briefs/runs/2026-10-10-acct1-lane-ledger10-jobs.md (and what it points
back to), including the hdl.huntington.org / CONTENTdm token shared across this lane and any other session (post `take`, re-read ROOM, wait for any earlier
un-released take; `release` with the request count; <= 40 requests per take, < 300 per session; on a dropped connection one retry after 25 s, then stop that
take). Prior-work step (.claude/briefs/prior-work-step.md, civil-war adapter) pasted before the first priced step. **The Step-0 ruling of the ledger10 jobs
file, Wave 3, is in force for every reader and verifier: run `ciphers/eckert-1864/ms18/step0_ordered.py`'s functions first and paste (a), (b), (c) per entry;
a reader files nothing for a hit; a verifier classifies a hit N1 (key period, text known) with depth only from (c).** A separate session is running
FIX-N2IC-DATE (owner account) on N2-IC: do not touch N2-IC. Rebase before every push to shared files (status.json, AUDIT.md, NOTES.md, ciphertext*.txt).
Report what was found and where it was not found; do not classify novelty (readers). Every create_session carries source_url.

---

# Wave 1

## FV-N2g (Opus 5.5, first verifier, separate from every reader; cap $4.5, box 80 min): N2-KA, N2-KB, N2-KC
Exactly "## FV-N2e" of the ledger10 jobs file (= FV-N2a of the ledger-n2 jobs file), Step-0 ruling first (a hit needs only the (c) check, ~0.5). These three
were filed by N2R-6 as "not located". WORK-QUEUE row AUD2-LEDGER12-<n> (n from 1) for N3+ D2+, tagged account-3 (VERIFY lane) per lane-common-blast; name it
in ROOM. AUDIT.md "## AUDIT (FV-N2g)"; s.5 corrections listed for a FIX job, not applied by you.

## FV-N1C-a (Opus 5.5, first verifier; cap $5, box 90 min): N1 confirms E382 E388 E390 E391, N2-IE IF II IJ
Exactly "## FV-MS18p" of the ledger10 jobs file (IA page image of the printed page, word-for-word diff, leaf eye-check of the entry's lines), Step-0 ruling first.
Cites from the readers: E382 OR I/49 pt 2 p.647 (time word 8 AM vs print 7 p.m., M); E388 I/32 pt 3 p.247; E390 I/41 pt 4 p.343 by sequence (Hurlbut vs
Canby, a key question: settle it from the leaf and the print); E391 I/37 pt 2 p.18 (second Wallace message not located: classify that part honestly); N2-IE
IF II IJ: the citations in NOTES "## N2R-4". AUDIT.md "## AUDIT (FV-N1C-a)"; AUD2 row only for anything reaching N3 D2 (as FV-N2g).

## FV-N1C-b (Opus 5.5, first verifier; cap $5.5, box 90 min): N1 confirms N2-JA JB JC JD JE JF JJ, N2-KD KE
As FV-N1C-a. Citations in NOTES "## N2R-5" and "## N2R-6". AUDIT.md "## AUDIT (FV-N1C-b)".

## FIX-FM22 (Sonnet 5.5; cap $2, box 50 min, no network)
Exactly the FIX-FM20 method (ledger10 jobs file): apply s.5 of "## AUDIT (FV-MS65a)" (E400: drop "they", restore "or which was included"; E401 key-only
words Point/West Virginia/Kanawha/President shown as key-dependent) through decode.py's entry-note mechanism (never hand-edit reading*.md); decode.py
--write then --check, decode_no2.py and decode_no9.py --check (all exit 0). status.json / SO rows per rule 10. NOTES "## FIX-FM22 (10 Oct 2026, account 1, for
LANE LEDGER-12)"; depth_check; file_shrink_guard. Do not touch N2-IC (FIX-N2IC-DATE is live).

## MS18-R9 (Sonnet 5.5, reader; cap $3, box 100 min): 9 unread mssEC 18 rows, clean-ms18.tsv best_book 1
Method exactly "## MS18-R8" of the ledger10 jobs file, with the Step-0 ruling (Wave 3) in place of its wave-1 step 0. Rows (unread at 07:4x by grep of
ciphertext*.txt and NOTES.md): 9811/1 9835/1 9877/1 9877/3 9793/0 9826/0 9806/2 9882/0 9777/1. Re-grep each before work; skip any filed meanwhile. IDs from
E402 (fetch first; next free if taken). A row that reads No. 2 or No. 9: do not file, name it in NOTES and ROOM. NOTES "## MS18-R9 (10 Oct 2026, account 1,
for LANE LEDGER-12)"; Remaining gaps / Escalation; gaps_check; decode.py --check. No audits. Unit ~0.25 per row (~0.1 for a step-0 hit).

## MS18-R10 (Sonnet 5.5, reader; cap $3, box 100 min): the next 9 rows
As MS18-R9. Rows: 9823/3 9865/1 9787/1 9733/1 9883/0 9802/1 9790/1 9874/2 9779/0. IDs: start at E420 (leaves MS18-R9 room; fetch first, next free if taken).
NOTES "## MS18-R10 (10 Oct 2026, account 1, for LANE LEDGER-12)". hdl token: take/release, never at the same time as MS18-R9.

Held for wave 2: MS18-R11 (9743/1 9686/2 9869/4 9730/0 9764/1 9897/1 9862/0 9885/3, the last best_book 1 rows), the 57xx page-JSON fetch + step0 run
(LEDGER-10 next 4), 9845/0 and 9862/1 header crops (LEDGER-11 next 4), and first verifiers on whatever wave 1's readers file as not located.

(07:45 UTC 10 Oct by date -u: wave 1 spawned, all with source_url: FV-N2g session_01Hcr3JGur9Z5mPB46GTpgRY, FV-N1C-a session_01AGERdLKuMQUBqX9D5ibDNo,
FV-N1C-b session_01MoccAAFnp3RKe7DbvYURL9, FIX-FM22 session_015cZzKuwyqr5PxCW7mKeFNu, MS18-R9 session_01VaZ66G8BH227GpVMMeQaPb, MS18-R10 session_01B6PSg1GRBoBJNoujdmPLgJ.)
