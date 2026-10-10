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

---

# Wave 2 (written 10 Oct 2026 08:2x UTC by date -u; lane ~18 of 60 + orchestrator)
By get_session: FV-N2g 3.49 (KA KB KC all in print: N1), FV-N1C-a 4.69 (all 8 N1 D1), FV-N1C-b 5.61 (all 9 N1), FIX-FM22 0.63, MS18-R9 1.61 (E402 E403 not located,
E404 OR I/41-4 p.389; 6 step-0 hits), MS18-R10 1.62 (E420 OR I/37-2; 8 step-0 hits). Lesson for readers: FV-N2g found the reader's own printcheck output had
the phrase hits that its NOTES verdict called "not located" -- before writing "not located", re-read your own print-check output for each row and say which
hit lines you rejected and why.

## FV-MS18r (Opus 5.5, first verifier, separate from every reader; cap $4, box 80 min): E402, E403 (not located), E404, E420 (printed, N1 confirm)
E402/E403 exactly "## FV-MS18q" of the ledger10 jobs file (Step-0 ruling first; full print search per the verifier template); E404/E420 exactly "## FV-MS18p"
(IA page image, word-for-word diff, leaf eye-check). Readers' notes: NOTES "## MS18-R9" and "## MS18-R10". WORK-QUEUE AUD2-LEDGER12-<n> for N3+ D2+ (account-3
tag), name it in ROOM. AUDIT.md "## AUDIT (FV-MS18r)"; s.5 corrections for a FIX job.

## MS18-R11 (Sonnet 5.5, reader; cap $2.5, box 90 min): the last 8 best_book 1 rows
As MS18-R9 (with the wave-2 lesson above). Rows: 9743/1 9686/2 9869/4 9730/0 9764/1 9897/1 9862/0 9885/3. IDs from E430 (fetch first; next free if taken).
NOTES "## MS18-R11 (10 Oct 2026, account 1, for LANE LEDGER-12)".

## FIX-FM23 (Sonnet 5.5; cap $2.5, box 60 min, no network)
Exactly FIX-FM20's method: apply s.5 (or the section the audit names) of "## AUDIT (FV-N2g)", "(FV-N1C-a)" and "(FV-N1C-b)": the readers' NOTES verdicts
(N2R-4/5/6, MS18-R8 rows now N1, with the audits' print citations), decoder plain-word slips through the decode scripts' entry-note mechanism, E390 Lehigh/Canby
note, N2-JB's continuation on 9758 (note only, do not file). decode x3 --write/--check exit 0; status.json/SO per rule 10; NOTES "## FIX-FM23 (10 Oct 2026,
account 1, for LANE LEDGER-12)"; depth_check; file_shrink_guard. Not N2-IC.

## S0-57XX (Sonnet 5.5; cap $1.5, box 50 min; hdl token)
LEDGER-10 next 4: fetch the page JSONs (CONTENTdm dmGetItemInfo, one take, <= 15 requests) for the entries "## AUDIT (STEP0-RULE ...)" lists as having no page
JSON on disk (the 57xx pointers / FM entries E302-E321), save them beside the others under ciphers/eckert-1864/sources/ with the manifest updated, then run
ms18/step0_ordered.py on those entries and append their rows to ms18/step0_ordered.tsv. Change no grade: post one ROOM line listing hits "for the VERIFY lane
and LANE LEDGER-12", and NOTES "## S0-57XX (10 Oct 2026, account 1, for LANE LEDGER-12)".

## HDR-NO9 (Sonnet 5.5; cap $1, box 40 min)
LEDGER-11 next 4: header crops of 9845/0 and 9862/1 (`tools/iiif_lines.py --image <leaf on disk>` or, if absent, one IIIF fetch each under the hdl token),
read the header (book label, time word) and write the No. 9 book call for each into NOTES "## NO9-L" as an addendum (decode nothing beyond the header).

(08:19 UTC 10 Oct by date -u: wave 2 spawned with source_url: FV-MS18r session_01CXQMDaCTduUo8KJmfBkFDo, MS18-R11 session_019Uiw5ZjKovLPq4Db1PKCAi, FIX-FM23
session_01X1cz8coPgpXQJyahaiGHtG, S0-57XX session_01DAazHZS5hJPjKWGu7FFmph, HDR-NO9 session_01MP9srFvpRKvXFXmsWFsUdX.)
