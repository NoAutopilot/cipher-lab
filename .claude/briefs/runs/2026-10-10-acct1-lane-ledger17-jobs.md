# LANE LEDGER-17 worker jobs (account 1, session_012RUntsXtDcM9uQywtGBBXs; written 10 Oct 2026 16:4x UTC by date -u)

Lane brief .claude/briefs/lane-ledger.md (+ lane-common-blast.md). WORK-QUEUE row DEFAULT-account-1-20261010-1640. Blast refill after LANE LEDGER-16
(closed 15:5x). **Scope: eckert-1864 Fort Monroe residue (mssEC 25, obj 5952, `ciphers/eckert-1864/fortmonroe/`) -- the 22 short 1865 rows no session ever
read, the 11 undated entries -- plus FIX jobs on the LEDGER-16 audits' s.5 and the OR-CACHE gap (LEDGER-14 next 2).** Every ROOM line ends "for LANE
LEDGER-17 (account 1)". seven_day allowed_warning has been on since 9 Oct (not a stop under lane-common-blast; say so in your done line if you see it).
New entry IDs: **E578-E599** (free at 16:44: highest used E577 in the E5xx block, E600-E621 LEDGER-14's), then E622 onward. Fetch and grep before using one.

Intake gate: `python3 tools/intake_gate_check.py eckert-1864` -> "eckert-1864: partial (line 3) -- edition/page or full-text-search citation found within
6 lines" (exit 0, 16:45 UTC 10 Oct). Re-run it yourself before deep work and paste the line.

**Common to every worker** -- exactly the "Common to every worker" block of .claude/briefs/runs/2026-10-10-acct1-lane-ledger16-jobs.md (and what it points
back to): host tokens in ROOM for hdl.huntington.org / CONTENTdm, be-api.us.archive.org, archive.org and googleapis (post `take`, re-read ROOM, wait for any
earlier un-released take by ANY session -- AUD2-LEDGER16-1 and -5 are live on the same hosts; `release` with the request count; <= 40 requests per take, < 300
per session; on a dropped connection one retry after 25 s, then stop that take); prior-work step (.claude/briefs/prior-work-step.md, civil-war adapter) pasted
before the first priced step; step 0 is a non-test on mssEC 25 (never "not filed" or N1 from a step-0 hit); the Wave 2 RULING of
.claude/briefs/runs/2026-10-10-acct1-lane-ledger13-jobs.md (a Fort Monroe row is NOT filed only for (i) a holder clear copy at another pointer, (ii) print
located at vol/page, (iii) plain, no book reads a clause, or too short for a clause above the authentication distance); all 411 Fort Monroe page JSONs on disk;
rebase before every push to shared files (status.json, AUDIT.md, NOTES.md, ciphertext*.txt, WORK-QUEUE.tsv); the lessons there, especially (5) three FRESH
holder queries per row (Washington clear books ~7680-7830 and 8500-8660) and (8) the `washington#1` header slip. Readers: report what was found and where it
was not found; do not classify novelty.

---

# Wave 1

## FM-S65A, FM-S65B (Sonnet 5.5, readers; cap $3.5 each, box 110 min each): the 22 short 1865 Fort Monroe rows, never read
prefilter-fm-final.tsv `final_verdict` clean-offline (offline pre-filter clean, < 40 words, Huntington full-text layer never run). LEDGER-13 read the 1864
short rows (FM-S1..S3) and the >= 40-word 1865 rows (FM65-A..F); these 22 pointer/entry pairs appear nowhere in reading.md, NOTES.md, AUDIT.md or the
fortmonroe/*.txt|*.tsv files (grep at 16:4x). Book: Cipher No. 1 (BOOK-FM65: No. 1 reads Jan-Mar 1865 Fort Monroe rows); decode under No. 2 as well where
best_book is 2, and test No. 1 first where it is 9. Method exactly "## FM65-A, FM65-B, FM65-C" of the ledger13 jobs file under its Wave 2 RULING: per row one
CONTENTdm CISOSEARCHALL holder query on a rare plain word (all pointers; positive control 9678 once per take) plus two fresh ones before decoding; after decoding
the print check (OR I/46 pts 1-3 and I/47 pts 1-2 by date + addressee, ORN I/11-12, Butler Corr. V, Grant Papers 14 via be-api `papersofulyssess0014gran`, vol.
13 via the Google Books API ids mnRjmhe3QLoC / ij8fAQAAMAAJ, O'Brien 1910 `telegraphinginba00obri` for O'Brien / Wilmington rows, the press of the day by
phrase), re-reading your own print-check output before "not located". A short row may carry no clause above the authentication distance: record "too short to
read a clause" rather than force it, and file only rows that carry one. File each row the ruling files in ciphertext.txt (existing header format; decode.py
--write then --check; decode_no2 / decode_no9 --check). Shuffled-key control: paste the decode of each filed row under one meaning-shuffled copy of No. 1 (seed
as BOOK-FM65's --shuf) beside the book decode, and say whether the clause survives it. NOTES "## FM-S65A (10 Oct 2026, account 1, for LANE LEDGER-17)" /
"## FM-S65B (...)" with the per-row line "filed E<n> / in print (vol/page) / holder clear copy (pointer) / plain / too short / no book in hand"; Remaining
gaps / Escalation; gaps_check; depth_check; file_shrink_guard. No audits. Unit ~0.25 per row; stop starting a row at 80% of cap and name the rest. The two
never hold one host's token at the same time.
- FM-S65A (11): 5845/2 5857/2 5858/2 5862/0 5862/2 5872/0 5872/1 (best_book 2) 5872/2 5874/1 5883/2 5892/0 -- IDs E578-E588.
- FM-S65B (11): 5892/1 5893/1 5896/0 5896/1 5908/0 5910/1 5914/2 5928/2 (best_book 9) 5936/2 5941/2 (best_book 9) 5942/1 -- IDs E589-E599.

## FM-UND (Sonnet 5.5; cap $2.5, box 90 min): the 11 undated Fort Monroe entries
prefilter-fm-final.tsv rows whose header carried no date (FM-PRE: "11 undated entries unexamined"): 5568/0 (print-likely+clear-sibling, 34 w), 5575/0
(print-likely+clear-sibling, 19 w), 5616/0 (clear-sibling, 97 w), 5656/0 (print-likely, 357 w), 5658/0 (print-likely, 233 w), 5689/0 (print-likely, 253 w),
5759/0 (print-likely, 91 w), 5842/0 (print-likely, 48 w), 5902/0 (print-likely, 66 w), 5914/0 (print-likely, 73 w), 5951/0 (clear-sibling, 12 w). Most are
known text by the pre-filter's own flags (light guardrail: do not read what is in print or has a clear copy). Per row: (1) place the date from the neighbouring
entries on the same and adjacent pages (page JSONs on disk) and the text's own references; (2) confirm the flag: the clear sibling's pointer, or the printed
page (vol/page, read on the page or a be-api snippet) -- the pre-filter's "print-likely" is an OR-coverage-by-date guess, NOT a located print; (3) only a row
whose flag does not hold (no clear copy, no print located) is read with the book its date implies (method as FM-S65A) and filed under the ruling, IDs E622
onward. NOTES "## FM-UND (10 Oct 2026, account 1, for LANE LEDGER-17)" with a table pointer | date placed (and how) | flag confirmed (where) | action;
Remaining gaps / Escalation; gaps_check; file_shrink_guard. Unit ~0.2 per row confirmed, ~0.3 per row read.

## FIX-L17a (Sonnet 5.5; cap $2, box 60 min, no network)
Exactly "## FIX-L16" of the ledger16 jobs file (FIX-L15's entry-note mechanism; never hand-edit reading*.md; extend `fixl16b_apply.py` or write an idempotent
`fixl17a_apply.py`), applying s.5 of AUDIT.md "## AUDIT (FV-L16b)" (E518 E527 E526 E546 E553 E554, incl. E546 washington#1), "## AUDIT (FV-L16c)" for E564 E574
E558 E569 only (incl. E569 washington#1), "## AUDIT (FV-L16d)" (E441 E472 E442 E473 E469 E466), and the three second-audit sections "## AUDIT 2 ...
AUD2-LEDGER16-2", "-3", "-4" (whatever they changed: depth, dates, senders). Do NOT touch FV-L16a's six (E509 E511 E514 E521 E508 E506) nor E447 E471 E474: their
second audits (AUD2-LEDGER16-1, -5) are live; FIX-L17b takes them. Check each fix is not already applied. decode x3 --write/--check exit 0; status.json depth
fields match the second audits; NOTES "## FIX-L17a (10 Oct 2026, account 1, for LANE LEDGER-17)"; depth_check; gaps_check; file_shrink_guard on every touched file.

## OR-CACHE2 (Sonnet 5.5; cap $3.5, box 100 min): the 22 ser. I vols 32-49 parts still not on disk (LEDGER-14 next 2)
NOTES "## OR-CACHE (10 Oct 2026, account 1, for LANE LEDGER-14)" lists the parts missing from `print/` and the method (title-page check of every IA id into
print/or_volume_map.tsv first -- `warofrebellion431unit` was I/47 pt 2, not I/43 pt 1). Fetch each missing part's _djvu.txt once (archive.org token; title page
verified before use; one id per part), then re-grep every eckert-1864 entry at N3 (status.json / AUDIT.md) whose date falls in a fetched part's span, by
rare names, places and decoded phrases (the OR-CACHE grep script, extended, not a private copy). A hit is a lead for a verifier: NOTES "## OR-CACHE2 (10 Oct
2026, account 1, for LANE LEDGER-17)" with parts fetched (id, title page line), entries grepped per part, and each hit as entry | vol/page | the printed line |
same message / related / unrelated; change no grade or status. ROOM flag naming the lead entries. Remaining gaps / Escalation; file_shrink_guard. Unit ~0.1 per
part fetched + ~1 for the grep.

Held for wave 2: FIX-L17b on FV-L16a's six + E447 E471 E474 after AUD2-LEDGER16-1 and -5 post done (Sonnet ~1.5); first verifiers (Opus, ~1.4/entry, sets of
5-6) on what FM-S65A/B and FM-UND file; verifier on any OR-CACHE2 lead.

(16:46 UTC 10 Oct by date -u: wave 1 spawned with source_url: FM-S65A session_01WDfyAjcGSadPWfNfb8HznQ, FM-S65B session_01VH54ZLoF8vbYjJi1WexTyb, FM-UND session_011zrx8sfAw6GegrqRCCHfvL, FIX-L17a session_01WAdCUNcVhMoWCkyVpoDvvT, OR-CACHE2 session_01EkWBz2ENJQ9KF6KGCDQyEK.)

---

# Wave 2 (written 10 Oct 2026 17:2x UTC by date -u; lane ~10.3 workers + orchestrator of 60)
By get_session: FIX-L17a 1.31 (16 entries fixed, fixl17a_apply.py), OR-CACHE2 1.67 (20 parts fetched, 210 N3 entries grepped, no lead), FM-UND 2.13 (E622 = 5616/0,
E623 = 5656/0 tel 1 filed; 5 clear copies, 4 print; gaps: E622 head, 5658/0 tel 2), FM-S65A 2.68 (E581 E582 E583 E585 E586 E587 filed; E582 E583 E586 thin);
FM-S65B live. AUD2-LEDGER16-1 and -5 posted done (17:02, 17:15).

## FV-L17a (Opus 5.5, first verifier, separate from every reader; cap $8, box 120 min)
Exactly "## FV-L16a, FV-L16b, FV-L16c, FV-L16d" of the ledger16 jobs file (all-pointer CONTENTdm clear-copy search FIRST with three FRESH queries per entry, not
the reader's; duplicate diff against mssEC 18/19/25; OR I/46 pts 1-3 and I/47 pts 1-2 by date, ORN I/11-12, Grant Papers 13 (Google Books ids) and 14 (be-api),
Butler Corr. V where Butler is a party, O'Brien 1910 for Wilmington / Army of the James, the press of the day for press-shaped text, G3 with decoded phrases,
eye-check every graded line on crops with tools/iiif_lines.py --image; step 0 never a reason for N1; depth per rule 4a / tools/depth_check.py /
.claude/briefs/runs/2026-10-08-acct3-depth-bar.md; diff any print against the derived reading block; reading fixes in AUDIT s.5, not the reading) on FM-S65A's
six filings, by H count: E581 E585 E587, then the thin E582 E583 E586 (too short for a clause -> say D0/D1 and spend little). Read NOTES "## FM-S65A" first,
including its shuffled-key control lines. AUDIT.md "## AUDIT (FV-L17a)". status.json/SO rows for N3+ only, audit_status "one audit"; depth_check;
file_shrink_guard. On N3+ D2+ append WORK-QUEUE `AUD2-LEDGER17-1` (fetch first; next free number if taken), tagged account-1, Opus 5.5, cap 2.5 per entry, box 30
per entry + 30; name it in ROOM for the orchestrator (owner account). Stop starting a new entry at 80% of cap and name the rest.

## FIX-L17b (Sonnet 5.5; cap $2, box 60 min, no network)
Exactly "## FIX-L17a" above, applying s.5 of AUDIT.md "## AUDIT (FV-L16a)" (E509 E511 E514 E521 E508 E506), "## AUDIT (FV-L16e)" for E447 E471 E474 only, and the
two second-audit sections "## AUDIT 2 (second adversarial, AUD2-LEDGER16-1)" and "## AUDIT 2 (second adversarial, AUD2-LEDGER16-5)" (whatever they changed:
depth, dates, senders, readings -- e.g. E474 "Frances fever" = Francis). Extend fixl17a_apply.py or write an idempotent fixl17b_apply.py. Check each fix is not
already applied. The key.md Topsy/Francis rows FIX-L17a held: leave key.md unedited, note it again under "## FIX-L17b" if these sections touch it. decode x3
--write/--check exit 0; status.json depth fields match the second audits; NOTES "## FIX-L17b (10 Oct 2026, account 1, for LANE LEDGER-17)"; depth_check;
gaps_check; file_shrink_guard on every touched file.

## FM-UND2 (Sonnet 5.5, reader; cap $1.5, box 50 min)
FM-UND's two read gaps (NOTES "## FM-UND" Remaining gaps 1-2), method as FM-S65A: (1) E622's head -- page 5614 from l.20 ("Washington Apr 20 1864") and page
5615, under No. 1, joined to E622 as one entry (same telegram; ciphertext.txt E622 extended, not a second ID, unless the head proves a separate telegram:
then E625); holder queries (three fresh, all pointers) and print check on the head's clause first; (2) 5658/0 telegram 2 (O'Brien to Eckert, Jamestown 9 May
1864 3.30 AM): the No. 1 decode is in fortmonroe/fmund.out; holder queries were run by FM-UND (none); run the print check by phrase (OR I/36 pt 2 by date 9 May,
Butler Corr. IV, be-api whole-collection), then file it as E624 under the Wave 2 RULING with the shuffled-key control line. NOTES "## FM-UND2 (10 Oct 2026,
account 1, for LANE LEDGER-17)"; update FM-UND's Remaining gaps lines to "done (FM-UND2)"; gaps_check; decode x3 --check; file_shrink_guard.

Held for wave 3: FV-L17b on FM-S65B's filings + E622 (with head) E623 E624, sized when FM-S65B posts done.

(17:21 UTC 10 Oct by date -u: wave 2 spawned with source_url: FV-L17a session_01J7yoXmAxN65SLSbfnCXPus, FIX-L17b session_01SoM9HipRUetCFV6coErchv, FM-UND2 session_01JtRM4ojs8yDrQtzZKVqypd.)

---

# Wave 3 (written 10 Oct 2026 17:5x UTC by date -u; lane ~20.3 workers + ~3 orchestrator of 60)
By get_session: FM-S65B 3.50 (E589-E594 filed; 5896/1 clear copy 8561 + OR I/47 pt 2 p.213, 5914/2 Grant Papers 14; be-api checks for E590 E592 E593 and the
Grant Papers 14 sweep not run, 502/503/429), FV-L17a 5.40 (E582 N1 OR I/47 pt 2 p.18, E587 N1 OR I/46 pt 2 p.198, E585 N3 D3, E581 N3 D2, E583 E586 D1;
AUD2-LEDGER17-1 queued for E585 E581), FIX-L17b 1.31 (nine entries), FM-UND2 2.31 (E622 head joined, list in print OR I/33 p.915, relay not located; E624 =
5658/0 tel 2, thin). FM-S65B's flag (clear copy 8561 covers E550) is already on file: E550 N1 by 8561 since FV-L15m.

## FV-L17b, FV-L17c (Opus 5.5, first verifiers, separate from every reader; FV-L17b cap $8, box 120 min; FV-L17c cap $6, box 100 min)
Exactly "## FV-L17a" (Wave 2), with FV-L17a's lesson: Grant Papers vol. 13 DOES reach Jan 1865 (FM-S65A said it ends Dec 1864) -- run it by Google Books API
for every 1865 entry. Read the reader's NOTES section first, including its shuffled-key control lines and its Remaining gaps (re-run what it could not).
- FV-L17b (FM-S65B's six, NOTES "## FM-S65B"), by H count: E589 E590 E591 E592 E593 E594 (order by reading.md "Code-word tokens"); FM-S65B's unrun be-api checks
  for E590 E592 E593 and the Grant Papers 14 sweep first. AUDIT.md "## AUDIT (FV-L17b)". AUD2 row `AUD2-LEDGER17-2` on N3+ D2+.
- FV-L17c (FM-UND / FM-UND2, NOTES "## FM-UND", "## FM-UND2"): E622 (Apr 1864, long: the vessel list is printed OR I/33 p.915 -- decide whether the printed
  list makes the entry N1/N2 or only a part of it, and diff the numerals), E623 (5656/0 tel 1, May 1864, Butler Corr. IV and OR I/36 by date), E624 (thin: D0/D1,
  spend little). 1864 sources: OR ser. I parts in print/or_volume_map.tsv (OR-CACHE2 put vols 32-49 on disk), Butler Corr. IV, Plum. AUDIT.md "## AUDIT
  (FV-L17c)". AUD2 row `AUD2-LEDGER17-3` on N3+ D2+.
Both: WORK-QUEUE rows tagged account-1, Opus 5.5, cap 2.5 per entry, box 30 per entry + 30 (fetch first; next free number if taken); name them in ROOM for the
orchestrator (owner account). Never hold one host's token at the same time as each other. Stop starting a new entry at 80% of cap and name the rest.

Held for wave 4: FIX-L17c (Sonnet, ~1.5, no network) on s.5 of FV-L17a, FV-L17b, FV-L17c -- including the unfile/N1 header notes for E582 E587 and the
not-filed recommendation for E583 E586 (RULING iii) -- for entries not under a live AUD2 row.
