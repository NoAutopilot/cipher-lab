# LANE LEDGER-15 worker jobs (account 1, session_01RQiEtm2KntpSGrqttBnXU1; written 10 Oct 2026 12:4x UTC by date -u)

Lane brief .claude/briefs/lane-ledger.md (+ lane-common-blast.md). WORK-QUEUE row DEFAULT-account-1-20261010-1239. Blast refill after LANE LEDGER-13 closed
(11:35, "Fort Monroe scope spent"). **Scope: eckert-1864 Fort Monroe ledger mssEC 25 (obj 5952, `ciphers/eckert-1864/fortmonroe/`) -- LEDGER-13 handoff
"next" 1-2: first audits of the unaudited filings E441-E577, row 5855/1, N1 confirms. LANE LEDGER-14 (closing, account 1) keeps mssEC 18/19 (E600-E629,
N2-S*): do not touch those entries.** Every ROOM line ends "for LANE LEDGER-15 (account 1)". seven_day allowed_warning has been on since 9 Oct (not a stop
under lane-common-blast; say so in your done line if you see it). New entry IDs, if any: E578-E599.

Intake gate: `python3 tools/intake_gate_check.py eckert-1864` -> "eckert-1864: partial (line 3) -- edition/page or full-text-search citation found within
6 lines" (exit 0, 12:4x UTC 10 Oct). Re-run it yourself before deep work and paste the line.

**Common to every worker** -- exactly the "Common to every worker" block of .claude/briefs/runs/2026-10-10-acct1-lane-ledger13-jobs.md (and what it points
back to), including the hdl.huntington.org / CONTENTdm token shared with every other session (post `take` in ROOM, re-read ROOM, wait for any earlier
un-released take; `release` with the request count; <= 40 requests per take, < 300 per session; on a dropped connection one retry after 25 s, then stop that
take). Prior-work step (.claude/briefs/prior-work-step.md, civil-war adapter) pasted before the first priced step. **Step 0 is a non-test on mssEC 25**
(BOOK-FM65, STEP0-KEYCTL; ledger13 jobs file Wave 2 RULING): never classify N1 from a step-0 hit; N1 needs print, a holder clear copy at another pointer, or
a decipherment located. All 411 Fort Monroe page JSONs are on disk (fortmonroe/, manifest); fetch only what is missing. Rebase before every push to shared
files (status.json, AUDIT.md, NOTES.md, ciphertext*.txt, WORK-QUEUE.tsv); FIX-AUD2-L14 and LEDGER-14 workers write the same files. Lessons carried: (1) Grant
Papers vols. 13 (Nov 1864-Feb 1865) and 14 (Feb-Apr 1865) are not on IA: search them by Google Books API (`www.googleapis.com/books/v1/volumes`,
`&country=US&key=$GOOGLE_BOOKS_KEY`, never print the key; volume ids in NOTES "## FIX-FM65": mnRjmhe3QLoC / ij8fAQAAMAAJ = vol. 13, DVLPEPsH1_oC /
1D8fAQAAMAAJ = vol. 14), 1.5 s apart; FIX-FM65's two-phrase sweep is a floor, not a negative -- try two more phrases per entry, including names and numbers.
(2) OR ser. I parts on disk: `ciphers/eckert-1864/print/or_volume_map.tsv` (OR-CACHE) -- use its true labels (IA `warofrebellion431unit` is I/47 pt 2, not
I/43 pt 1); for a 1864 entry whose OR part is not on disk, fetch that part's `_djvu.txt` once from archive.org (<= 4 parts per session) and add it to the map.
(3) Verifiers diff the print against the derived reading block (E420 lesson). (4) One IA whole-collection be-api phrase query before "not located".

---

# Wave 1

## FV-L15a, FV-L15b, FV-L15c, FV-L15d (Opus 5.5, first verifiers, separate from every reader; cap $8 each, box 110 min each)
Exactly "## FV-FM65a, FV-FM65b" of .claude/briefs/runs/2026-10-10-acct1-lane-ledger13-jobs.md (FV-FM9a/FV-FM10a method: all-pointer CONTENTdm clear-copy
search FIRST, duplicate diff against every mssEC 18/19/25 entry, OR I-III and ORN by date (1865: OR I/46 pts 1-3, I/47 pts 1-2, ORN I/11-12), Grant Papers
13/14 by Google Books per lesson (1), Butler Corr. V where Butler is a party, the press of the day (a press dispatch -- E536 Tribune -- checked in the
newspaper itself: Chronicling America / IA newspapers by phrase), G3 with decoded phrases, rare-name OR grep, eye-check every graded line on crops with
tools/iiif_lines.py --image), step 0 never a reason for N1, depth per rule 4a / tools/depth_check.py / .claude/briefs/runs/2026-10-08-acct3-depth-bar.md.
Reading fixes go in AUDIT s.5 for a FIX job, not into the reading. Entries by H count (reading.md "Code-word tokens"); reader NOTES sections named in each
entry's reading.md header line ("FM65-A".."FM65-F", "FM-F1", "FM-S1".."FM-S3", "FM-R9"):
- FV-L15a: E555 E536 E568 E541 E576 E575. AUDIT.md "## AUDIT (FV-L15a)".
- FV-L15b: E545 E560 E505 E567 E525 E572 (E545: FIX-FM65 found a near-miss, different telegram, in Grant Papers 13 -- settle it). AUDIT.md "## AUDIT (FV-L15b)".
- FV-L15c: E551 E529 E513 E515 E552 E549. AUDIT.md "## AUDIT (FV-L15c)".
- FV-L15d: E539 E528 E500 E573 E557 E517. AUDIT.md "## AUDIT (FV-L15d)".
status.json/SO rows for N3+ only, audit_status "one audit"; depth_check; file_shrink_guard. On N3+ D2+ append WORK-QUEUE `AUD2-LEDGER15-<n>` (n = a..d -> 1..4;
fetch first, take the next free number if taken), **tagged account-1** (owner-account orchestrator rule, ROOM 10:28 10 Oct: accounts 3 and 4 silent), Opus
5.5, cap 2.5 per entry, box 30 per entry + 30; name it in ROOM for the orchestrator (owner account). Unit ~1.3 per entry. The four never hold the hdl token at
the same time as each other or any reader: take it in turn.

## FV-L15n (Opus 5.5, first verifier, N1 confirm; cap $3, box 70 min)
N1 confirms (FV-MS18p method of .claude/briefs/runs/2026-10-10-acct1-lane-ledger10-jobs.md: page image or snippet, word-for-word diff against the derived reading
block, leaf eye-check, step 0 information only): E537 E544 E565 (FIX-FM65 Grant Papers 13/14 hits, NOTES "## FIX-FM65"; E544's snippet cites O.R. I/46 pt 2
p.271 -- check it on disk) and E171 (OR-CACHE lead: Heine to Halleck 20 Aug 1864 vs OR I/43 pt 1 p.860, run of 10 words; NOTES "## OR-CACHE"; E171 is
already audited -- write the ruling as a short AUDIT section, change the class only if the print holds for the body, and propagate per rule 10 to status.json
and any SO row). A citation that does not hold leaves the entry for a full verifier (name it). AUDIT.md "## AUDIT (FV-L15n)". No hdl token needed unless a leaf
eye-check image is missing from disk.

## R-5855 (Sonnet 5.5, reader; cap $1, box 50 min)
Read row 5855/1 (31 words, never read; Webster to Dodge 4 Jan 1865, reply to E507 msg 2; AUD2-LEDGER13-2 lead) under Cipher No. 1 (`decode.py`; check the
header/time word fits; shuffled-key control as BOOK-FM65), print check by date + both correspondents (OR I/45 pt 2 and I/46 pt 2 by date, Grant Papers 13 by
Google Books, the 1865 OR parts on disk), holder clear-copy CISOSEARCHALL on a rare plain word (control 9678 once, under the token). File it (E578) or record
why not per the ledger14 jobs file RULING (holder clear copy / print / plain / no clause / too short). NOTES "## R-5855 (10 Oct 2026, account 1, for LANE
LEDGER-15)"; decode x3 --check exit 0; file_shrink_guard. Report what was found and where it was not found; do not classify novelty.

Held for wave 2: first verifiers on the rest of the unaudited filings (1865: E509 E511 E514 E518 E526 E527 E542 E543 E546 E548 E550 E553 E554 E558 E562 E564
E566 E569 E571 E574 E577 E506 E508 E521; 1864: E441 E472 E465 E447 E442 E474 E471 E470 E468 E443 E473 E445 E469 E466 E446 E448); a FIX job on wave 1's s.5.

(12:47 UTC 10 Oct by date -u: wave 1 spawned with source_url: FV-L15a session_01WNiDGdC52vxM1PiiB8Rcw8, FV-L15b session_01JHZ65eV5Fe3DSuTujnfSc4, FV-L15c session_01EEFyxEGFkG9NEjAqivwrCh, FV-L15d session_011HBDTUbE69JkJPExoyA9j8, FV-L15n session_01CFSNt8CD3vxPQzKNBLP61e, R-5855 session_013HSZrwAokYtQpqFJzHaaKx.)

---

# Wave 2 (written 10 Oct 2026 13:2x UTC by date -u; lane workers 20.0 done + FV-L15a/b live)
By get_session: R-5855 0.98 (5855/1 plain/no clause, not filed), FV-L15n 3.69 (E537 E544 E565 N1; E171 N3 -> N1, OR I/43 pt 1 p.860), FV-L15d 8.18 (E573 E557
N1; E539 E528 E500 E517 N3 D3; AUD2-LEDGER15-4), FV-L15c 7.14 (E551 E552 E529 E513 N1, E515 N2, E549 N3 D3; AUD2-LEDGER15-3). Lesson: of 12 entries
audited, 7 had a **holder clear copy at another Huntington pointer** (the Washington clear books, pointers ~7680-7830 and 8500-8660) or print -- found in the
first ~20 CISOSEARCHALL queries. An Opus verifier at ~1.3/entry spends most of that on entries a cheap sweep settles. So the rest go through a Sonnet sweep first.

## CLEAR-SWEEP (Sonnet 5.5; cap $4, box 120 min; hdl <= 160 requests in takes of <= 40, archive.org/be-api <= 60, googleapis <= 60)
Entries (40): 1865 E509 E511 E514 E518 E526 E527 E542 E543 E546 E548 E550 E553 E554 E558 E562 E564 E566 E569 E571 E574 E577 E506 E508 E521; 1864 E441
E472 E465 E447 E442 E474 E471 E470 E468 E443 E473 E445 E469 E466 E446 E448. Per entry, from its derived reading block in reading.md: (a) holder clear copy --
CISOSEARCHALL (documented `CISOSEARCHALL^TERM^all^and` form, sixth segment 1) on two rare plain words or names of the body plus the date, all collections the
FV-L15c/d sections used (read "## AUDIT (FV-L15c)" / "(FV-L15d)" s.1 for their exact query form and the pointer ranges that hit); for each candidate pointer one
dmGetItemInfo and a word-for-word diff of its transcription against the reading (control 9678 once per take); (b) print -- grep the OR/ORN parts on disk
(print/or_volume_map.tsv true labels) by date window +-3 days on two letters-only phrases (ms18_l14b_print.py method), one IA whole-collection be-api phrase query,
Grant Papers 13 by Google Books (lesson (1)) and Grant Papers 14 on IA (`papersofulyssess0014gran`, be-api) for 1865 entries, for 1864 entries OR ser. I parts
by date (fetch a missing part's _djvu.txt once, <= 4, add to the map). Output `ciphers/eckert-1864/fortmonroe/clear_sweep.tsv` (entry, pointer, date,
clear_copy pointer/page or -, print vol/page or -, shared run length, verdict: CLEAR / PRINT / NEAR (different message, same day) / NONE) with a control row
(E552 -> 7749 and E557 -> 7768 must hit; E549 must not). No grade change, no AUDIT edit: CLEAR/PRINT rows are N1 candidates for a confirming verifier, NONE rows go
to full first verifiers. NOTES "## CLEAR-SWEEP (10 Oct 2026, account 1, for LANE LEDGER-15)". file_shrink_guard. Report what was found and where it was not found;
do not classify novelty. Stop before starting an entry that would cross 80% of cap or box; list the unswept ones.

Held for wave 3: one N1-confirm verifier (Opus, FV-L15n method) on CLEAR/PRINT rows; full first verifiers (Opus, 6 per session) on NONE rows by H count; FIX-L15
(Sonnet) on FV-L15a/b/c/d/n s.5.
