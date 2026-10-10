# LANE LEDGER incarnation 10 worker jobs (account 1, session_01JzEqWLccccneXKJs7AmR6N; written 10 Oct 2026 03:4x UTC by date -u)

Lane brief .claude/briefs/lane-ledger.md (+ lane-common-blast.md). WORK-QUEUE row DEFAULT-account-1-20261010-0339. Continues BOTH predecessors' next lists:
STATUS.md "LANE LEDGER handoff ... incarnation 9" and "LANE LEDGER-N2 handoff". Every ROOM line ends "for LANE LEDGER-10 (account 1)". seven_day
allowed_warning has been on since 9 Oct (not a stop under lane-common-blast; say so in your done line if you see it).

Intake gate: `python3 tools/intake_gate_check.py eckert-1864` -> "eckert-1864: partial (line 3) -- edition/page or full-text-search citation found within
6 lines" (exit 0, 03:4x UTC 10 Oct). Re-run it yourself before deep work and paste the line.

**Common to every worker** -- exactly the "Common to every worker" block of .claude/briefs/runs/2026-10-10-acct1-lane-ledger-n2-jobs.md (which points back to
the ledger7/6/5/4/3 blocks), with the hdl.huntington.org / CONTENTdm token now shared across THIS lane and the account-4 AUD2 verifiers (post `take`,
re-read ROOM, wait for any earlier un-released take; `release` with the request count; <= 40 requests per take, < 300 per session; the host dropped
connections under load at 02:4x 10 Oct -- on a dropped connection, one retry after 25 s, then stop that take).

**New lesson, carried into every reader and verifier (AUD2-LEDGER-38, 02:40 10 Oct; D2V-E74, 8 Oct):** E378 and E381 were lowered N3 -> N1 at second
audit because the Huntington's OWN public transcription of the entry's page already carries the clear body (the clerk wrote the decipherment, or the
cataloguer transcribed a clear copy); the first audit missed it. Step 0 is therefore explicit and comes first for every entry: open the page JSON on disk
(ciphers/eckert-1864/sources/mssEC18/p<pointer>.json, mssEC19/ likewise; fetch with CONTENTdm dmGetItemInfo only if absent) and diff its transcription
text against the decoded body. If the transcription carries the body in clear (>= half the decoded content words, in order), the entry is a step-0 item:
readers file nothing and say "clear in holder transcription"; verifiers classify N1 (key `period`, text known) and D at most what the key adds. Paste the
overlap figure (content words shared / decoded content words) per entry.

---

# Wave 1

## FIX-FM20 (Sonnet 5.5; cap $3, box 75 min, no network)
Exactly the FIX-FM16/18/19 method (ledger8/ledger9 jobs files; FIX-FM11 is the full statement). Apply, through each decode script's existing entry-note
mechanism (never hand-edit reading*.md): s.5 of "## AUDIT (FV-MS18n)" and "(FV-MS18o)" (E375 watch plain; E378 Princess = schooner C, SecWar H; E371
Ferry/Terry M; headers with holder pointers); the s.4 corrections of AUDIT 2 sections AUD2-LEDGER-34, -35, -36, -37, -38 (E378, E381 now N1 D1 -- carry
that into NOTES/reading headers; SO rows already withdrawn); s.5 of "## AUDIT (FV-N2d)" and "(FV-O9a)" for ciphertext-no2.txt / -no9.txt (incl. the O9-DA
lead: holder 4551 answers it -- note only). Then decode.py, decode_no2.py, decode_no9.py `--write` where needed and `--check` (all exit 0). Carry each
change into status.json and SO rows per rule 10. NOTES "## FIX-FM20 (10 Oct 2026, account 1, for LANE LEDGER-10)": change, grade before/after, check
output; depth_check; file_shrink_guard.

## HTX-SWEEP (Sonnet 5.5; cap $3, box 75 min, disk only, no network)
The step-0 test above, run retroactively on every eckert-1864 entry from mssEC 18 or mssEC 19 that holds a first or second audit at N3 (E-ids E300 onward,
every N2-* and O9-* at N3, plus E346 which AUD2-LEDGER-38 flagged). Script it (one script under ciphers/eckert-1864/ms18/htx_sweep.py: entry -> pointer
-> page JSON on disk -> transcription text; content-word overlap with the decoded body, stop-words removed, both normalised per CLAUDE.md rule 3 PX-BRODEC:
one case, abbreviations expanded where the reading expands them). Control: the same overlap for each entry against a RANDOM other page's transcription
(20 draws) -- report entry overlap vs control p95. Write ms18/htx_sweep.tsv (entry, pointer, overlap, control p95, flag). Flag = overlap > control p95 and
>= 0.5. Do NOT change any grade: post one ROOM line listing flagged entries "for the account-4 VERIFY lane and LANE LEDGER-10", and a NOTES section
"## HTX-SWEEP (10 Oct 2026, account 1, for LANE LEDGER-10)". If a page JSON is missing, list it (the orchestrator gives it to a fetch job).

## FV-O9b (Opus 5.5, first verifier, separate from every reader; cap $6.5, box 100 min): O9-DA, O9-DD, O9-DF
Exactly "## FV-O9a" of the ledger-n2 jobs file, step 0 above first; O9-DA: read holder 4551 first (FV-O9a lead). WORK-QUEUE row AUD2-LEDGER10-1 for N3+ D2+
(account-4 tag: account 3 has been silent since 9 Oct 02:03; account 4 is running the VERIFY stage).

## FV-MS18p (Opus 5.5, first verifier; cap $4.5, box 90 min): N1 confirms E372 E373 E376 E377 E380, and E379
Exactly "## FV-MS18m" of the ledger9 jobs file (IA page image, word-for-word diff, leaf eye-check of these entries' lines), step 0 above first. Cites: E372 OR
I/45 pt 2 p.82; E373 I/39 pt 3 p.482; E376 I/48 pt 2 p.505; E377 I/37 pt 2 p.63; E380 I/34 pt 3 p.480. E379: the quoted Burbridge dispatch is printed I/39 pt 1
p.20; the relay itself was not located -- classify the relay frame honestly (may be N3 for the relay frame alone, with depth for what the frame adds).
AUDIT.md "## AUDIT (FV-MS18p)"; status.json/SO/AUD2 row only if something reaches N3 D2 (then AUD2-LEDGER10-2, account-4 tag).

## MS18-R8 (Sonnet 5.5, reader; cap $3.5, box 110 min): 10 more mssEC 18 No. 1 rows
Method exactly "## MS18-R7" of the ledger9 jobs file (= MS18-R6), step 0 above first for every row. Rows: 10003/2 (printed OR I/49 pt 2 per MS18-R7: confirm,
file), 10048/1 (Sept 1865: book share test first; "no book in hand" if none reads), 9885/1, 9887/0, 9841/0, 10055/0 (pointer in ciphertext.txt: check the
entry number, skip if filed), 9694/1, 9903/1, then the next clean-ms18.tsv best_book 1 rows in file order after 9903/1 until 10 are read; also 9880/2 and 9772/0
(LANE LEDGER-N2 handed these over: they read No. 1). IDs from E382 (fetch first; next free if taken). NOTES "## MS18-R8 (10 Oct 2026, account 1, for LANE
LEDGER-10)"; Remaining gaps / Escalation; gaps_check; decode.py --check. No audits. Unit ~0.25 per row.

## N2R-4 (Sonnet 5.5, reader; cap $3.5, box 110 min): 10 unread rows guessed Cipher No. 2
Exactly "## N2R-1" of the ledger-n2 jobs file with N2R-2's day-word test, step 0 above first. Rows: 9701/0 9850/1 9755/0 9898/2 9759/0 9685/1 9906/0 9739/2
9782/0 9880/0. IDs N2-IA, N2-IB, ... (fetch first; next free block if taken). If a row reads No. 1, do not file: name it in NOTES and ROOM "reads No. 1 --
for MS18 readers of LANE LEDGER-10". NOTES "## N2R-4 (10 Oct 2026, account 1, for LANE LEDGER-10)". MS18-R8 and N2R-4 both use the hdl token: take/release.
