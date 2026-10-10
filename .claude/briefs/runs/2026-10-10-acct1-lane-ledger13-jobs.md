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

Held for wave 2: readers on the 1865 rows BOOK-FM65 assigns (step-0 misses only, ~0.25/row, batches of 10); first verifiers on anything filed "not located"
(Opus, ~1.4/entry; AUD2-LEDGER13-<n> rows for N3+ D2+, tagged account-3); a FIX job on the audits' s.5.
