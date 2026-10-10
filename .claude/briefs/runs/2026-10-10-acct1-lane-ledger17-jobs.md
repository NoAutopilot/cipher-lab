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
