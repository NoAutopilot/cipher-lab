# LANE LEDGER-13 worker jobs (account 1, session_0144M5B5m1zmnBKpUbs32YxK; written 10 Oct 2026 08:4x UTC by date -u)

Lane brief .claude/briefs/lane-ledger.md (+ lane-common-blast.md). WORK-QUEUE row DEFAULT-account-1-20261010-0840. Second account-1 blast lane beside LANE
LEDGER-12 (which keeps mssEC 18). **Scope split: this lane works only eckert-1864's Fort Monroe ledger, mssEC 25 (Huntington object 5952,
`ciphers/eckert-1864/fortmonroe/`).** Every ROOM line ends "for LANE LEDGER-13 (account 1)". seven_day allowed_warning has been on since 9 Oct (not a stop
under lane-common-blast; say so in your done line if you see it).

Intake gate: `python3 tools/intake_gate_check.py eckert-1864` -> "eckert-1864: partial (line 3) -- edition/page or full-text-search citation found within
6 lines" (exit 0, 08:43 UTC 10 Oct). Re-run it yourself before deep work and paste the line.

**Common to every worker** -- exactly the "Common to every worker" block of .claude/briefs/runs/2026-10-10-acct1-lane-ledger12-jobs.md (and what it points
back to), including the hdl.huntington.org / CONTENTdm token shared with LANE LEDGER-12 and every other session (post `take`, re-read ROOM, wait for any
earlier un-released take; `release` with the request count; <= 40 requests per take, < 300 per session; on a dropped connection one retry after 25 s, then
stop that take). Prior-work step (.claude/briefs/prior-work-step.md, civil-war adapter) pasted before the first priced step. The Step-0 ruling (ledger10 jobs
file, Wave 3) is in force: run `ciphers/eckert-1864/ms18/step0_ordered.py`'s functions first and paste (a), (b), (c) per entry; a reader files nothing for a
hit. All 411 Fort Monroe page JSONs are on disk from FM-PRE (fortmonroe/; check the manifest) -- read from disk, fetch only what is missing. Rebase before
every push to shared files (status.json, AUDIT.md, NOTES.md, ciphertext*.txt, HYPOTHESES.md); LEDGER-12's workers write the same files. Report what was
found and where it was not found; do not classify novelty (readers). Lesson carried from LEDGER-12 (FV-MS18r): before writing "not located", run one IA
whole-collection phrase query (Grant Papers volumes via be-api without identifier) and re-read your own print-check output, saying which hit lines you
rejected and why.

---

# Wave 1

## BOOK-FM65 (Opus 5.5, key test; cap $4, box 90 min, disk only; hdl only for a missing page JSON, under the token)
Question: does any book in hand (No. 1 key.md, No. 2 key-no2.md, No. 9 key-no9.md) read the 81 clean **1865** rows of fortmonroe/clean-fm.tsv (Jan 48,
Feb 15, Mar 18; 57 sent, 24 received)? FM-PRE's gap (NOTES "## Remaining gaps (FM-PRE, 8 Oct 2026)" item 2): "whether No. 1 reads them is not
established (the token share is non-selective ...)". Hints, not evidence: E84 (Sheldon 3 Jan 1865, label "No 1") reads No. 1 at H; E85 (24 Jan 1865) reads
coherently under No. 1 but nothing independent selected the book; BOOK-65 (NOTES "## BOOK-65") found mssEC 18 1865 rows split across No. 1, No. 2 and books
not in hand (leaf labels No. 3/4/5). Method exactly "## BOOK-65" of .claude/briefs/runs/2026-10-10-acct1-lane-ledger11-jobs.md: pre-register in HYPOTHESES.md
before decoding (rows, books, control, decision rule); per row header word / label / time word first; decode under No. 1, No. 2, No. 9 and a meaning-shuffled
copy of each (3 seeds); a book "reads" a row only if its decode carries a coherent clause above the authentication distance that no shuffled copy and no
other book gives -- state the clause (an H-count control ties a shuffled key by construction; use the clause). Test rows (10, spread by month): 5854/1
5856/0 5878/1 5886/0 (Jan), 5897/0 5904/1 5905/0 (Feb), 5918/0 5924/0 5936/0 (Mar). Then predict from header words / labels / time words alone the book for
the other 71 1865 rows (list them from clean-fm.tsv) and run step0_ordered.py's (a)/(b) under the predicted book for every row whose prediction is a book in
hand (disk only, no decode reading by eye). Write NOTES "## BOOK-FM65 (10 Oct 2026, account 1, for LANE LEDGER-13)": table row x book with the clause,
verdict per row (No. 1 / No. 2 / No. 9 / none in hand), the 71-row prediction table with step-0 (a)/(b), and the list of rows a reader should take (book in
hand, step-0 miss). File nothing. If a month reads in no book in hand, say "blocked, no-key-material" for that month's rows and stop there.

## FM-R9 (Sonnet 5.5, reader; cap $1.5, box 70 min): the four unread 1864 Fort Monroe clean rows
Method exactly "## FM-R7a, FM-R7b" of .claude/briefs/runs/2026-10-09-acct1-lane-ledger6-jobs.md (HEAD share scorer for No. 1 / No. 2 / No. 9 pasted; decode
under the book whose decode gives sense; a row no book reads is "no book in hand", not forced), with the Step-0 ruling first. Rows (unread at 08:4x by grep
of pointer/entry in ciphertext*.txt and NOTES.md): 5752/0 (16 June 1864, sent, 54 w; check first that it is not part of E256 = 5752/1), 5699/1 (27 May,
99 w), 5707/0 (27 May, 90 w), 5650/0 (3 May, 49 w) -- NO9-KEY found May-June rows labelled 9 read in No. 1. Re-grep each before work. IDs: E440 onward (No.
1), N2-PA onward or the next free N2 letter (No. 2), next free O9- (No. 9); fetch first. NOTES "## FM-R9 (10 Oct 2026, account 1, for LANE LEDGER-13)" with
the per-row line "in print (vol/page) / holder clear copy (pointer) / not located (sources searched by date) / step-0 skip / no book in hand"; Remaining
gaps / Escalation; gaps_check; decode x3 --check exit 0. No audits. Unit ~0.3 per row.

## FM-S1, FM-S2 (Sonnet 5.5, readers; cap $2.5 each, box 100 min each): short 1864 Fort Monroe rows (24-39 words), never read
FM-PRE left 40 1864 rows below its 40-word line unread (prefilter-fm-final.tsv `final_verdict` clean-offline: offline pre-filter clean, the Huntington
full-text layer NOT run on them). Method as FM-R9 above, plus, because the holder layer was never run: one CONTENTdm CISOSEARCHALL query per row on a rare
plain word or name of the row (all pointers, under the hdl token; positive control 9678 once per take) before decoding, and the Step-0 ruling. A short row
may give no clause above the authentication distance: record it "too short to read a clause" rather than forcing a reading, and file only rows that carry
one. Grep each row first (pointer/entry in ciphertext*.txt, NOTES.md); skip any filed meanwhile.
- FM-S1 (10): 5785/1 5799/0 5816/2 5583/2 5827/0 5647/0 5793/1 5636/2 5822/2 5731/0 -- IDs E450 onward (No. 1), next free N2/O9 otherwise.
- FM-S2 (10): 5698/0 5638/0 5632/2 5627/1 5810/1 5756/1 (best_book 2) 5720/0 5814/0 5768/3 5680/2 -- IDs E465 onward.
NOTES "## FM-S1 (10 Oct 2026, account 1, for LANE LEDGER-13)" / "## FM-S2 (...)" with the per-row line as FM-R9; Remaining gaps / Escalation; gaps_check;
decode x3 --check exit 0. No audits. Unit ~0.2 per row. FM-S1 and FM-S2 never hold the hdl token at the same time. Held for wave 2: the other 20 short rows
(5720/2 5547/1 5569/1 5546/0 5577/0 best_book 9; 5673/1 5672/1 5641/0 5804/2 5669/1 5664/2 5679/0 5830/0 5633/1 5798/1 5833/2 5828/1 5829/1 5800/2 5590/0).

(08:45 UTC 10 Oct by date -u: wave 1 spawned with source_url: BOOK-FM65 session_01L1JBbw4Zcn7kDhqDocdSUE, FM-R9 session_01NhUBdr3wGVNmw1FTEoY6vZ; 08:46 FM-S1 session_01F5CS712fjJ3AoxT2BpcgxR, FM-S2 session_01RkNbt9S8hDrkqQaH6Ud92M.)

Held for wave 2: readers on the 1865 rows BOOK-FM65 assigns (step-0 misses only, ~0.25/row, batches of 10); first verifiers on anything filed "not located"
(Opus, ~1.4/entry; AUD2-LEDGER13-<n> rows for N3+ D2+, tagged account-3); a FIX job on the audits' s.5.

---

# Wave 2 (written 10 Oct 2026 09:1x UTC by date -u; lane ~8.3 of 60 + orchestrator)
By get_session: BOOK-FM65 3.43 (No. 1 reads all 10 tested 1865 rows, Jan/Feb/Mar; No. 2/No. 9 none; the other 71 predicted No. 1), FM-R9 0.99 (4 rows, all
held as step-0 hits), FM-S1 1.82 (10 rows, none filed; 5647/0 and 5636/2 in print + holder copies, 5731/0 plain + copy 11877), FM-S2 2.10 (E465 filed; 5698/0
in print; 5627/1 copy 10266; 5680/2 key check).

**RULING for this lane (mssEC 25 only), replacing the Step-0 ruling here.** BOOK-FM65 showed (NOTES "## BOOK-FM65", step-0 under three meaning-shuffled
copies of No. 1) and FM-S2 confirmed independently: on the Fort Monroe ledger the holder transcription of a row IS its cipher copy, mostly plain words, so
step0_ordered (a) measures plain residue and hits under shuffled keys as often as under the book (61/66/64 vs 66 of 72). A step-0 hit on mssEC 25 is a
non-test (CLAUDE.md rule 3: a control that cannot fail differently). On this ledger a row is NOT filed only if: (i) a holder clear copy at another pointer
(CONTENTdm CISOSEARCHALL on plain rare words, all pointers), (ii) located in print (vol/page, read on the page image or be-api snippet), (iii) plain with no
code word, or no book reads a clause, or too short for a clause above the authentication distance. Every other row is filed with its reading, whatever step 0
says; still paste step 0 (a)/(b) and the step-0 under one meaning-shuffled copy of the book, as information. The Step-0 ruling for mssEC 18/19 is not
changed by this lane (STEP0-KEYCTL below reports on it).

**ID block (ROOM 09:1x): LEDGER-13 holds eckert-1864 E440-E599; LANE LEDGER-12 asked to use E600 onward.**

## FM-F1 (Sonnet 5.5; cap $2.5, box 80 min): file the 15 Fort Monroe rows wave 1 decoded but held as step-0 skips
The readings are already in NOTES "## FM-R9", "## FM-S1", "## FM-S2" (and their scripts). Under the ruling above, file each as a cipher entry in
ciphertext.txt in the existing header format (decode.py --write then --check; decode_no2/no9 --check), with the reader's per-row line updated to "filed
E<n>": FM-R9 5752/0 (check first it is not part of E256 = 5752/1) 5699/1 5707/0 -> E440-E442; FM-S1 5785/1 5799/0 5816/2 5583/2 5827/0 5793/1 5822/2 ->
E443-E449; FM-S2 5638/0 5632/2 5810/1 5720/0 5814/0 -> E466-E470. A row whose decode gives no clause above the authentication distance (5799/0 and 5632/2
look thin) is recorded "too short to read a clause" instead, not filed. Before filing each: one be-api whole-collection phrase query (Grant Papers, Butler
Corr., OR by IA be-api without identifier) on the readable clause, and re-read the reader's own print-check output; a hit moves the row to "in print", not
filed. Not 5647/0 5636/2 5731/0 5698/0 5627/1 5650/0 5756/1 5680/2 (clear copy / print / plain / key check). NOTES "## FM-F1 (10 Oct 2026, account 1, for
LANE LEDGER-13)"; Remaining gaps / Escalation; gaps_check; depth_check; file_shrink_guard. No hdl requests needed (readers already ran the holder queries);
if one is, take/release the token. Unit ~0.15 per row.

## FM65-A, FM65-B, FM65-C (Sonnet 5.5, readers; cap $3.5 each, box 120 min each): Fort Monroe 1865 rows, Cipher No. 1
Method as FM-R9 (wave 1) under the RULING above: book No. 1 per BOOK-FM65 (paste its verdict / prediction line for each row; decode under No. 2 as well for
5931/0, the one conflict). Per row before decoding: one CONTENTdm CISOSEARCHALL query on a rare plain word (all pointers, under the hdl token, control 9678
once per take); after decoding: the print check (OR ser. I vols. 46-47 and 51 by date + addressee via the repo's IA ids, ORN I/11-12, Butler Corr. V, Grant
Papers vols. 13-14 via be-api without identifier, the press of the day by phrase), re-reading your own print-check output before "not located". For
BOOK-FM65's ten test rows reuse its clause and do not re-derive it. File every row the ruling says to file in ciphertext.txt; decode.py --write/--check, the
other two --check. NOTES "## FM65-A (10 Oct 2026, account 1, for LANE LEDGER-13)" etc., per-row line as FM-R9; Remaining gaps / Escalation; gaps_check;
file_shrink_guard. Unit ~0.25 per row. The three never hold the hdl token at the same time (post take, re-read ROOM, wait).
- FM65-A (12): 5847/2 5849/0 5849/1 5850/1 5851/0 5851/1 5852/1 5852/2 5853/1 5854/0 5854/1 5855/2 -- IDs E500-E511.
- FM65-B (12): 5856/0 5856/1 5857/1 5858/0 5858/1 5860/1 5860/2 5861/1 5861/2 5864/1 5866/0 5866/2 -- IDs E512-E523.
- FM65-C (12): 5867/0 5868/0 5867/2 5869/1 5870/0 5871/0 5871/1 5873/1 5877/0 5877/1 5877/2 5878/1 -- IDs E524-E535.

## FM-S3 (Sonnet 5.5, reader; cap $4, box 120 min): the other 20 short 1864 rows
As FM-S1/FM-S2 under the RULING above (holder query first, then decode, then print check; file what the ruling files). Rows: 5720/2 5547/1 5569/1 5546/0
5577/0 (best_book 9: test No. 1 first, NO9-KEY found May-June 9-labelled rows read in No. 1) 5673/1 5672/1 5641/0 5804/2 5669/1 5664/2 5679/0 5830/0 5633/1
5798/1 5833/2 5828/1 5829/1 5800/2 5590/0. IDs E471-E490. NOTES "## FM-S3 (10 Oct 2026, account 1, for LANE LEDGER-13)". Unit ~0.2 per row.

## STEP0-KEYCTL (Opus 5.5; cap $3, box 70 min, disk only, no network): does the Step-0 ruling survive a meaning-shuffled-key control on mssEC 18/19?
The Step-0 ruling (ledger10 jobs file Wave 3; STEP0-RULE, AUDIT a4843c48a) was controlled by a shuffled-ORDER null and by route constructions, never by a
meaning-shuffled KEY. BOOK-FM65 found the key-shuffle control fails it on mssEC 25. Re-run ms18/step0_ordered.py's functions on (1) the 57 earlier mssEC 18/19
N3 entries STEP0-RULE scored (51 hits), (2) S0-57XX's FM entries E302-E320 (ms18/step0_ordered.tsv s057xx rows), (3) every step-0 HIT this window's readers
recorded in NOTES "## MS18-R9", "## MS18-R10", "## MS18-R11" (rows LEDGER-12 did not file) -- each under the entry's book and under 3 meaning-shuffled copies
of that book (same seeds as BOOK-FM65's --shuf). Also compute a key-only variant: (a) restricted to tokens whose rendering depends on the key (code-word
positions), against the same holder window, under the book and the 3 shuffles. Report per entry: (a) book, (a) shuffles s1-s3, key-only (a) book vs
shuffles, and whether the hit survives (book hit AND all three shuffles miss, or key-only beats every shuffle). Write NOTES "## STEP0-KEYCTL (10 Oct 2026,
account 1, for LANE LEDGER-13)" with the table and a proposed revised ruling; change NO status.json, AUDIT.md, ciphertext or grade -- the ruling belongs to
the VERIFY lane and the owner-account orchestrator. Post one ROOM flag naming them and LANE LEDGER-12 with the survivor count. Report what was found.
