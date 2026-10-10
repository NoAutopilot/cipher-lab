# LANE LEDGER-11 worker jobs (account 1, session_01P41wJ6BbSWs1T4xnJAn52e; written 10 Oct 2026 05:4x UTC by date -u)

Lane brief .claude/briefs/lane-ledger.md (+ lane-common-blast.md). WORK-QUEUE row DEFAULT-account-1-20261010-0539 (blast 2 of 2: the second account-1 lane,
running beside LANE LEDGER-10, session_01JzEqWLccccneXKJs7AmR6N). Every ROOM line ends "for LANE LEDGER-11 (account 1)". seven_day allowed_warning has been on
since 9 Oct (not a stop under lane-common-blast; say so in your done line if you see it).

**Scope split from LANE LEDGER-10 (as LEDGER-N2 split from incarnation 9).** LEDGER-10 keeps every 1864 row of ciphers/eckert-1864/ms18/clean-ms18.tsv and
the AUD/FIX chain of its own entries. LEDGER-11 takes: (i) the 1865-dated rows of clean-ms18.tsv (any best_book guess), (ii) the No. 9 leftovers named in the
LEDGER-N2 handoff item 4, (iii) eckert-1862 (mssEC 15) cheap gaps. Before working a row, grep its pointer/entry in ciphertext*.txt, NOTES.md and ROOM.md: if
another session filed or claimed it since, skip and say so.

Intake gate (05:4x UTC 10 Oct): `eckert-1864: partial (line 3) -- edition/page or full-text-search citation found within 6 lines` (exit 0);
`eckert-1862: partial (line 3) -- edition/page or full-text-search citation found within 6 lines` (exit 0). Re-run it yourself before deep work and paste the line.

**Common to every worker** -- exactly the "Common to every worker" block of .claude/briefs/runs/2026-10-10-acct1-lane-ledger-n2-jobs.md (which points back to
the ledger7/6/5/4/3 blocks): prior-work-step.md by reference with its result pasted before the first priced step; the hdl.huntington.org / CONTENTdm token
shared across LEDGER-10, LEDGER-11 and the account-4 AUD2 verifiers (post `take`, re-read ROOM, wait for any earlier un-released take; `release` with the
request count; <= 40 requests per take, < 300 per session; on a dropped connection one retry after 25 s, then stop that take); the **Step-0 ruling** of
.claude/briefs/runs/2026-10-10-acct1-lane-ledger10-jobs.md Wave 3 (ordered LCS overlap (a) vs within-entry shuffle p95 (b), key-dependent words (c); a hit is
N1 for the body; readers file nothing for a hit and say "body in holder transcription", listing (c)). Rule 10 wording only: report what was found and where
it was not found; do not classify novelty. Push with `python3 tools/room.py --push <paths>`; file_shrink_guard on every touched file in the done line.

---

# Wave 1

## BOOK-65 (Opus 5.5, key test; cap $4, box 90 min, disk first; hdl only for a missing page JSON, under the token)
Question: which book in hand (No. 1 key.md, No. 2 key-no2.md, No. 9 key-no9.md, a SAMPLE table) reads the unread 1865 rows of clean-ms18.tsv that the share
guesses as No. 9 or No. 2? Precedents: O9-BOOK (ledger-n2 jobs file: header words decide, the shuffled-key bigram score does not), MS18-R2's X1-X10 note
(NOTES l.~3717: most 1865 rows read No. 1 by sense; X3 10058/0 Oct 1865 Van Duzer reads in no book), FV-MS18n (E375 20 Oct 1865 read No. 1), E387 (23 Sept 1865,
No. 1). Pre-register in HYPOTHESES.md before decoding (rows, books, control, decision rule). Rows (10): 10047/1 10025/1 10013/1 10059/1 10014/1 10051/0
10052/0 10012/1 10023/1 10045/0. Per row: header word / label / time word on the page text first; decode under No. 1, No. 2, No. 9 and one meaning-shuffled
copy of each (3 seeds); a book "reads" a row only if its decode carries a coherent clause (rule 4a: above the authentication distance) that no shuffled copy
and no other book gives -- state the clause. Note: an H-count control ties a shuffled key by construction (ledger-n2 lesson), so use sense / clause, not
counts. Also predict, from header words alone, the book for the other 1865 rows: 10041/3 10057/1 10047/2 10054/1 10031/1 10040/1 10062/2 10044/1 10066/2
10020/3 10058/1 10053/1 10060/1 10057/0 10017/2 10041/2 10044/0 10040/0 10006/0 10006/1 10063/1 10007/1 10061/2 10046/2 10034/2 10028/2. Write NOTES
"## BOOK-65 (10 Oct 2026, account 1, for LANE LEDGER-11)": table row x book, verdict per row (No. 1 / No. 2 / No. 9 / none in hand). File nothing.
Report what was found and where it was not found.

## MS65-R1 (Sonnet 5.5, reader; cap $3.5, box 110 min): 9 mssEC 18 1865 rows guessed No. 1
Method exactly "## MS18-R7" of .claude/briefs/runs/2026-10-10-acct1-lane-ledger9-jobs.md (= MS18-R6), with the Step-0 ruling first for every row, and the 1865
caution of MS18-R7 (test the book share first; "no book in hand" if no book reads a clause; never force). Rows: 10019/1 10060/0 10039/0 10030/2 10062/0
10008/0 10046/1 10065/1, plus 10058/0 re-tested under No. 1 by sense (LEDGER handoff inc. 9 item 5: E375 20 Oct 1865 read No. 1). IDs: the next free E-number
after the highest in ciphertext.txt (fetch first; LEDGER-10 may file E39x concurrently -- take a block starting 10 above its last, e.g. E400 if E39x is in use,
and say so). NOTES "## MS65-R1 (10 Oct 2026, account 1, for LANE LEDGER-11)" with the per-row line "in print (vol/page) / holder clear copy (pointer) / not
located (sources searched by date) / step-0 skip / no book in hand"; Remaining gaps / Escalation; gaps_check; `decode.py --write` then `--check` exit 0. No audits.
Unit ~0.3 per row. Searches for 1865: OR ser. I vols. 46-49 by date + addressee (page images via the repo's or_volumes.tsv IA ids), ser. II/III, the press of the
day; Grant Papers vols. 14-15 via be-api.

## NO9-L (Sonnet 5.5, reader; cap $3, box 100 min): the No. 9 leftovers of the LEDGER-N2 handoff (item 4)
Method exactly "## O9R-1" of the ledger-n2 jobs file (decode_no9.py, ciphertext-no9.txt, the O9-BA/O9-BB convention; key-no9.md is a SAMPLE table: unread words
stay [?], never guessed), Step-0 ruling first for every row. Rows: 9699/0 (sibling of O9-DF, reads No. 9, not filed), 9694/2 (header "9" but body conflicts:
decode under No. 1 and No. 9 and say which carries a clause), 9845/0 (header only: record), 9679/0 (No. 9 or No. 2 by time word: decide by sense), 9725/1 9762/1
9761/0 (clear openings), 9862/1 9770/2 (time word fits no book: test, "none in hand" if nothing reads). IDs O9-E* (the next free block after O9-D*; fetch first).
A row that reads No. 1 or No. 2: do not file; name it in NOTES and ROOM "reads No. N -- for LANE LEDGER-10". NOTES "## NO9-L (10 Oct 2026, account 1, for LANE
LEDGER-11)"; Remaining gaps / Escalation; gaps_check; decode_no9.py --check. No audits.

## E62-CAM (Sonnet 5.5; cap $2, box 75 min): eckert-1862 cheap gaps
ciphers/eckert-1862/NOTES.md "## Remaining gaps (E62-CHECK2)" and "(E62-STALE)": (1) Camden = Thomas (one occurrence, M): grep the ledger page texts on disk
(print/residue pages, pages_manifest.tsv) for a second Camden entry 13-15 Feb 1862 and any other Camden; (2) Merlin = Maryland vs Virginia: grep the Feb pages
for Merlin in other lines (by line and date); (3) ORN ser. I vols. 22-23 (Feb 1862, Foote / Tennessee and Cumberland rivers) and OR ser. I vol. 7's Halleck-
McClellan pages by phrase for the entries carrying Myrtle, Mary, Ingress, Humboldt (IA full text, the repo's IA ids or advancedsearch; one host at a time).
No key.md edit: a value with a second witness is proposed in NOTES with its witnesses for a later KEY job (rule 4: conflicting witnesses logged, never
majority-voted). NOTES "## E62-CAM (10 Oct 2026, account 1, for LANE LEDGER-11)"; update Remaining gaps / Escalation; gaps_check; residue_decode.py --check if
anything regenerated. Report what was found and where it was not found.

---

# Wave 2 (written 10 Oct 2026 06:3x UTC by date -u; seven_day allowed_warning on every worker)
By get_session: BOOK-65 2.64 (10014/1 No. 1; 10012/1 and the Fuller 28 May entry inside the 10023/1 segment No. 2; 8 none in hand, labels No. 3/4/5; 26 predicted),
MS65-R1 1.86 (7 step-0 skips; E400 in print; E401 not located), NO9-L 1.92 (all 9 step-0 hits, nothing filed), E62-CAM 0.91 (no second witness). Wave 1 7.33.

## FV-MS65a (Opus 5.5, first verifier, separate from every reader; cap $3.5, box 90 min): E401 (10030/2), and the N1 confirm of E400 (10039/0)
Exactly "## FV-MS18l" of .claude/briefs/runs/2026-10-10-acct1-lane-ledger9-jobs.md, Step-0 ruling first (MS65-R1 filed both, so its (a) was a miss: recompute
and paste a/b/c). E401: 14 June 1865 (Cumberland; holder 7953 = Smith-to-Emory reply on McCausland, context): OR I/46 pt 3 and ser. I vols. 47-49 by date + both
correspondents on page images, ser. II, Grant Papers 15, the press of the day, G3 with decoded phrases; leaf eye-check against the transcription (MS65-R1
image-read it). E400: N1 confirm only (IA page image, word-for-word diff of the three print locations MS65-R1 cites; ~0.6). AUDIT.md "## AUDIT (FV-MS65a)";
status.json/SO rows per rule 10; WORK-QUEUE AUD2-LEDGER11-1 for N3+ D2+ (account-4 tag). Corrections in s.5 for a FIX job.

## MS65-R2 (Sonnet 5.5, reader; cap $3.5, box 110 min): the rows BOOK-65 assigned or predicted
Method "## MS65-R1" above (for No. 1 rows) and "## N2R-4" of the ledger10 jobs file (for No. 2 rows: decode_no2.py, ciphertext-no2.txt, No. 1 and shuffled
No. 2 side by side), Step-0 ruling first for every row. Rows: 10014/1 (read No. 1 by BOOK-65: file only the Sheldon 21 May entry; the Sullivan entry in the same
segment reads in no book, record it), 10012/1 (No. 2), the Fuller 28 May entry inside the 10023/1 segment (No. 2: cut it from the segment as BOOK-65 NOTES says),
then the header-word predictions 10006/0 10040/0 10034/2 10028/2 (No. 2), 10007/1 10006/1 (No. 1 or No. 2: decode both, file under the one that carries a clause),
10040/1 (Fuller, Impress). Paste BOOK-65's table row for each. IDs: No. 1 from E402 (fetch first; next free if taken); No. 2 from N2-MA (N2-L exists as a single id; fetch first, next free block if taken).
NOTES "## MS65-R2 (10 Oct 2026, account 1, for LANE LEDGER-11)" with the per-row line; Remaining gaps / Escalation; gaps_check; decode --write/--check exit 0.
No audits. Unit ~0.3 per row.
