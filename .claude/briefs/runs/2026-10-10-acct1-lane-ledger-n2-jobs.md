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
