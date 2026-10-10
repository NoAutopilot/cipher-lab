# LANE LEDGER-N2 worker jobs (account 1, session_01JyTbV4HjnVsWqF3eTp8vvZ; written 10 Oct 2026 00:4x UTC by date -u)

Lane brief .claude/briefs/lane-ledger.md (+ lane-common-blast.md). WORK-QUEUE row DEFAULT-account-1-20261010-0040 (the second account-1 blast lane).
Every ROOM line ends "for LANE LEDGER-N2 (account 1)". seven_day allowed_warning was on through LANE LEDGER incarnations 8-9 (not a stop under
lane-common-blast; say so in your done line if you see it).

**Scope split.** LANE LEDGER incarnation 9 (session_016pcjMK9ShCpNwDUEG955mj) reads mssEC 18 rows whose `best_book` is 1 and files them as E-ids.
This lane takes ONLY the 1864 rows of `ciphers/eckert-1864/ms18/clean-ms18.tsv` whose `best_book` is 2 or 9 (63 + 26 unread at 00:4x). It files
under the N2- (ciphertext-no2.txt) and O9- (ciphertext-no9.txt) prefixes only, NEVER an E-id. If a row of yours reads as Cipher No. 1 and not as
its guessed book, do not file it: list it in your NOTES section as "reads No. 1 -- handed to LANE LEDGER" and post one ROOM line naming the pointer.

Intake gate: `python3 tools/intake_gate_check.py eckert-1864` -> "eckert-1864: partial (line 3) -- edition/page or full-text-search citation found within
6 lines" (exit 0, 00:4x UTC 10 Oct). Re-run it yourself before deep work and paste the line.

**Common to every worker** -- exactly the "Common to every worker" block of .claude/briefs/runs/2026-10-09-acct1-lane-ledger7-jobs.md (which points back to
the ledger6/5/4/3 blocks): CLAUDE.md; .claude/briefs/prior-work-step.md with one pasted line per check (the civil-war adapter: own work, the Huntington
transcription of the same pointer -- an entry clear in its own transcription is a step-0 skip -- OR ser. I/II/III and ORN by date + both correspondents,
same-leaf siblings in other codes, the newspaper of the day where reachable); `date -u` before every time you write; ROOM claim/halfway/done via
tools/room.py; push every two units; stop before a unit that would cross 80% of cap or box; rule 10 wording; no AskUserQuestion; no credentials;
file_shrink_guard before the final push; gaps_check after NOTES; hdl.huntington.org / CONTENTdm token SHARED WITH LANE LEDGER (post `take`, re-read ROOM,
wait for an earlier un-released take by any worker of either lane; post `release` with the request count; at most 40 requests per take, under 300 per
session). Page text is on disk in ciphers/eckert-1864/sources/mssEC18/: read it before any network request. Images to scratch, never committed; crops only
(`tools/iiif_lines.py --image`). Rebase immediately before every write to AUDIT.md, NOTES.md, ciphertext*.txt, reading*.md, status.json, key*.md,
HYPOTHESES.md, WORK-QUEUE.tsv; on a conflict keep both facts (incarnation 9's workers write the same files). Solvers: report what was found and where it
was not found; do not classify novelty. Cost is read by the orchestrator from get_session. Print searches use the IA ids in
ciphers/eckert-1862/ec18/or_volumes.tsv as corrected by FIX-FM16 (warofrebellion431unit = OR I/47 pt 2). Lessons carried: readers' "not located" was
wrong for 6 of 13 rows audited in incarnation 8 -- grep OR by date + addressee on page images, and run the all-pointer CONTENTdm clear-copy search on each
row's clear words FIRST (readers missed holder copies three times), Grant Papers via IA be-api; the decoded-text phrase pass (G3) is the filter that works.

---

# Wave 1

## N2R-1 (Sonnet 5.5, reader; cap $3.5, box 110 min): 10 mssEC 18 rows guessed Cipher No. 2
Method: "## MS18-R2" of .claude/briefs/runs/2026-10-09-acct1-lane-ledger7-jobs.md (all-pointer clear-copy search first, OR by date + addressee, rare-name
grep, Grant Papers be-api) applied to Cipher No. 2: decode with `ciphers/eckert-1864/decode_no2.py` (read how the mssEC 19 No. 2 readers filed N2-BP/N2-BQ
from mssEC 18 and N2-DA/N2-DB/N2-EA, and follow that file convention exactly); for each row also decode under No. 1 (`decode.py`'s tables) and under a
shuffled No. 2 key (same token counts, values permuted, 3 seeds) and paste the three coherence numbers side by side: the row is filed as No. 2 only if No. 2
beats both. Rows (clean-ms18.tsv, best_book 2, file order): 9879/0, 9767/1, 9690/0, 9680/1, 9905/1, 9807/0, 9782/2, 9916/2, 9690/2, 9798/0 (spares 9871/2,
9874/1). Grep each pointer/entry in ciphertext*.txt, NOTES.md, AUDIT.md first; skip and say so if filed. IDs N2-FA, N2-FB, ... (fetch first; if FA is
taken use the next free two-letter block). Then `decode_no2.py --write` and `--check` exit 0. NOTES "## N2R-1 (10 Oct 2026, account 1, for LANE
LEDGER-N2)" with a per-row line "in print (vol/page) / holder clear copy (pointer) / not located (sources searched by date) / step-0 skip / reads No. 1",
Remaining gaps / Escalation, gaps_check. No audits. Unit ~0.3 per row.

## N2R-2 (Sonnet 5.5, reader; cap $3.5, box 110 min): the next 10 rows guessed Cipher No. 2
Exactly N2R-1. Rows: 9871/2, 9874/1, 9761/1, 9913/0, 9800/2, 9871/1, 9916/1, 9722/1 (dated 1864-11-02 on p.56: check the date against the page first),
9680/0, 9725/0 (spares 9914/1, 9681/0). IDs N2-GA, N2-GB, ... NOTES "## N2R-2 (10 Oct 2026, account 1, for LANE LEDGER-N2)". Both readers write
ciphertext-no2.txt: rebase immediately before writing and keep both blocks.

## O9-BOOK (Opus 5.5, key test; cap $3.5, box 90 min, disk only unless an image is needed)
Question: which book in hand reads the 26 unread 1864 mssEC 18 rows that the share guesses as Cipher No. 9? Their s9 shares are low (0.03-0.31) because
key-no9.md is a SAMPLE table (key-no9.md header), so the guess is weak. Pre-register in HYPOTHESES.md before decoding: for each of 10 rows (9926/1,
9880/2, 9709/1, 9772/0, 9694/2, 9699/0, 9808/2, 9845/0, 9830/1, 9673/0) decode under No. 1, No. 2 and No. 9 (decode.py / decode_no2.py / decode_no9.py
tables) and under one shuffled key per book (3 seeds); call a book "reads" a row only if its coherent-word count beats every shuffled control and the
other two books; check the ledger's own header word/book label on the page text first (NOTES "Book assignment note (rule 3)": the header word decides, not
the share). Write a table row x book (count, control p95) to NOTES "## O9-BOOK (10 Oct 2026, account 1, for LANE LEDGER-N2)" and the verdict per row:
No. 9 / No. 2 / No. 1 (hand to LANE LEDGER) / none in hand. File nothing; the readers of wave 2 file. Also say, for the remaining 16 rows, which book the
header words predict. Report what was found and where it was not found.

---

# Wave 2 (written 10 Oct 2026 01:2x UTC by date -u; seven_day allowed_warning on every worker, continuing per lane-common-blast)
By get_session: N2R-1 2.41 (N2-FA..FJ; 6 in OR, 4 not located), N2R-2 3.09 (N2-GA..GJ; 4 in OR, 6 not located; 9871/1, 9871/2 no clause under any book),
O9-BOOK 3.15 (No. 9 reads 9709/1 9808/2 9673/0, 9845/0 header only; 9880/2 9772/0 read No. 1, handed to LANE LEDGER; 9926/1 "No 3", 9830/1 "No 13" none in
hand; 9694/2 conflict, 9699/0 undecided; shuffled-key bigram instrument weak, 3/10 -- the header words decide). Wave 1 8.65.

## FV-N2a, FV-N2b, FV-N2c (Opus 5.5, first verifiers, separate from every reader; cap $2.5 per entry, box 100 min)
Method exactly "## FV-MS18l" of .claude/briefs/runs/2026-10-10-acct1-lane-ledger9-jobs.md (= the FV-FM9a / FV-FM6 chain: all-pointer CONTENTdm clear-copy
search FIRST, duplicate diff across mssEC 18/19/25, OR I-III and ORN by date + both correspondents on page images, Grant Papers via IA be-api, press of the
day, G3 with decoded phrases, rare-name OR grep; eye-check of the leaf against the holder transcription; CLAUDE.md verifier template incl. rule 4a depth),
for Cipher No. 2 entries in ciphertext-no2.txt (`decode_no2.py --check`). Write "## AUDIT (FV-N2a)" etc. in AUDIT.md, status.json rows, SO rows for N3+,
and for N3+ D2+ one WORK-QUEUE row AUD2-LEDGERN2-<n> (account-3 tag; this lane is account 1, which read and first-audited) for the VERIFY lane; corrections
in s.5 for a FIX job, never edited into the reading by you. Each NOTES/AUDIT line ends "for LANE LEDGER-N2 (account 1)".
- FV-N2a (cap 7.5): N2-FA (9879/0, 30 Oct 1864, Caldwell to the Nymph: Seymour's agents, ballot-box stuffer; a same-day sibling Dana to Patrick is in print
  with different wording -- test N2 against it), N2-FB (9767/1, 26 June 1864, hospital transports, Ingalls), N2-FE (9905/1, 3 Dec 1864, Sixth Corps shipping).
- FV-N2b (cap 7.5): N2-FH (9916/2, 17 Dec 1864, vessels to Sherman at Savannah), N2-GE (9916/1, 16 Dec 1864, Halleck to Canby, Pensacola to Hilton Head;
  holder clear reply 8504 -- read it first), N2-GF (9722/1, 25 Apr 1864, Augur to Meade, Mosby near Upperville).
- FV-N2c (cap 10): N2-GH (9725/0, 27 Apr 1864, Burnside to Grant, column to Fairfax; OR I/33 Grant to Meade 27 Apr 8.30 a.m. names the move -- test N2),
  N2-GA (9874/1, 22 Oct 1864), N2-GC (9913/0, 10 Dec 1864), N2-GI (9914/1, 14 Dec 1864) -- the three Brice paymaster telegrams: read them together, look for
  the Paymaster General's printed reports and OR III/4 for each.

## N2R-3 (Sonnet 5.5, reader; cap $3.5, box 110 min): 10 more rows guessed Cipher No. 2
Exactly N2R-1, with N2R-2's day-word test beside the shuffled-key coherence (the decoded time/day word must equal the header's). Rows: 9791/1 (325 words: one
unit = 2 rows), 9839/0, 9807/1, 9888/1, 9873/3, 9813/0, 9840/0, 9774/3 (pointer 9774 has E-ids from LANE LEDGER: check the entry number), 9687/0 (spares
9848/1, 9876/1, 9691/0). IDs N2-HA, N2-HB, ... NOTES "## N2R-3 (10 Oct 2026, account 1, for LANE LEDGER-N2)".

## O9R-1 (Sonnet 5.5, reader; cap $3.5, box 110 min): 10 rows O9-BOOK assigned or predicted to Cipher No. 9
Method of N2R-1 with `decode_no9.py` and ciphertext-no9.txt (follow the O9-BA/O9-BB convention for mssEC 18 rows); key-no9.md is a SAMPLE table: unread
groups stay [?] at grade M, never guessed; the header words (label, Pagan/Pagoda place word, time word = header time) are the book test -- paste them per row,
and file a row only if they agree with No. 9 and the decoded body has at least one clause. Rows: 9709/1, 9808/2, 9673/0 (O9-BOOK verdicts), 9687/1, 9684/1,
9699/1, 9803/0, 9684/0, 9735/0, 9686/1 (header predictions). Read NOTES "## O9-BOOK" first (its decodes are in ms18/o9book.out). IDs O9-DA, O9-DB, ...
NOTES "## O9R-1 (10 Oct 2026, account 1, for LANE LEDGER-N2)". Count per row how many tokens the sample table leaves unread.

---

# Wave 3 (last planned; written 10 Oct 2026 01:5x UTC by date -u; seven_day allowed_warning on every worker)
By get_session: FV-N2a 6.38 (N2-FA FB FE N3 D3; AUD2-LEDGERN2-2), FV-N2b 5.64 (N2-GE N1 OR I/41 pt 4 p.869; N2-FH GF N3 D3; AUD2-LEDGERN2-1), FV-N2c 7.20
(N2-GH N1 Grant Papers 10; GA N3 D3, GC GI N3 D2; AUD2-LEDGERN2-3), N2R-3 2.17 (N2-HA..HI, 6 printed, HB HC HF not located), O9R-1 3.45 (O9-DA..DK all No. 9 by
header words; 4 printed, 7 not located; H 57 M 20; judge FAIL -1.094). Workers 33.49 + orchestrator ~3.5. Remaining under cap ~23: caps below sum 17.

## FIX-N2a (Sonnet 5.5; cap $2.5, box 60 min, no network)
Exactly the FIX-FM16/FIX-FM18 method (ledger8/ledger9 jobs files; FIX-FM11 is the full statement) for Cipher No. 2: apply s.5 of "## AUDIT (FV-N2a)", "(FV-N2b)",
"(FV-N2c)" to ciphertext-no2.txt through decode_no2.py's existing entry-note mechanism (the missed name Felix McCloskey, Fifth Corps and the Dana signature
in N2-FA; FB/FE fixes; "walch" omitted from the N2-FH transcription after the leaf; plain words collecting/business, Relay House; Pharoah Brooks = December 2
as each audit words it); never hand-edit reading-no2.md; `decode_no2.py --write` then `--check`, exit 0 (also decode.py, decode_no9.py --check). Carry each
change into status.json and the SO prompt rows per rule 10. NOTES "## FIX-N2a (10 Oct 2026, account 1, for LANE LEDGER-N2)": change, grade before/after,
check output; depth_check; file_shrink_guard.

## FV-N2d (Opus 5.5, first verifier; cap $7.5, box 100 min): N2-HB (9839/0), N2-HC (9807/1), N2-HF (9813/0)
Exactly "## FV-N2a" of Wave 2. Read NOTES "## N2R-3" first. WORK-QUEUE row AUD2-LEDGERN2-4 for N3+ D2+ (account-3 tag).

## FV-O9a (Opus 5.5, first verifier; cap $7, box 100 min): O9-DC (9673/0), O9-DE (9684/1), O9-DH + O9-DI (9684/0, two telegrams on one pointer)
Exactly "## FV-N2a" for Cipher No. 9 entries (ciphertext-no9.txt, `decode_no9.py --check`); key-no9.md is a SAMPLE table and the book call rests on header
words (label, Pagan/Pagoda, time word): re-test the book call yourself on the leaf before grading anything; unread groups stay M; rule 4a depth honestly
(short entries, H 5-7 each). Read NOTES "## O9-BOOK" and "## O9R-1" first. WORK-QUEUE row AUD2-LEDGERN2-5 for N3+ D2+ (account-3 tag). The other not-located
O9 rows (DA DD DF) are left for the next incarnation.
