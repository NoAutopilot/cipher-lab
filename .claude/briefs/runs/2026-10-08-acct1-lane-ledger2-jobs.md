# LANE LEDGER incarnation 2 worker jobs (account 1, session_018DE9C1ZwPUGX7qbyQbQgQb; written 8 Oct 2026 20:5x UTC)

Lane brief .claude/briefs/lane-ledger.md (+ lane-common-blast.md). Continues the **Next** list of the "LANE LEDGER handoff (session_01BhFrvFs46QaEbT8aTNPN8V
...)" in STATUS.md. Every ROOM line ends "for LANE LEDGER (account 1)".

Intake gates (pasted 20:5x UTC): `eckert-1864: partial (line 3) -- edition/page or full-text-search citation found within 6 lines` (exit 0);
`eckert-1862: partial (line 3) -- edition/page or full-text-search citation found within 6 lines` (exit 0). Objects 5952 (mssEC 25) and 10074 (mssEC 18)
are Eckert Papers ledgers inside those check-solved verdicts; the prior-work step below is the item-level check.

**Common to every worker** -- exactly the "Common to every worker" block of .claude/briefs/runs/2026-10-08-acct1-lane-ledger-jobs.md (read it: CLAUDE.md,
prior-work-step.md by hand with one pasted line per check, `date -u`, ROOM claim/halfway/done via tools/room.py, push every two units, 80% stop, rule 10
wording, no AskUserQuestion, no credentials, file_shrink_guard before the final push, gaps_check after NOTES), with its **hdl.huntington.org token** rule AND the
wave-2 addition (after posting `take`, fetch ROOM again; if another `take` without `release` is newer than the last release and earlier than yours, wait for its
release). Images to scratch, never committed. Solvers: report what was found and where it was not found; do not classify novelty.
Before decoding, **diff each row's pointer, date and addressee against every filed `###` header in ciphertext*.txt and status.json** (a duplicate is recorded,
not decoded). Next free IDs: `grep -o "E1[0-9][0-9]" ciphers/eckert-1864/NOTES.md | sort -u | tail -1` after a fetch; the offsets below avoid collisions.

---

## FIX-FM1 (Sonnet 5.5; cap $2, box 45 min, no network): carry the first-audit corrections into the readings (rule 7 + rule 10 propagation)
1. ciphers/eckert-1864/AUDIT.md "## AUDIT (FV-FM1)" s.3 and the AUD2-LEDGER-3 section: E160 ("pledge pebble inch" = six 3-inch [x2], "gloryth" = 17th),
   E163 ("weasler" = steamer, "offal" H), E164 ("poney" = 9). Apply to ciphertext.txt/reading.md through the book's decode path (key.md row or the entry's
   grading, whichever the audit names; never hand-edit a reading), regenerate with `python3 ciphers/eckert-1864/decode.py --check` (exit 0).
2. FV-LS5-B and AUD2-LEDGER-2 corrections for E143/E145 (AUDIT.md sections "## AUDIT (FV-LS5-B)" and "AUDIT 2 (AUD2-LEDGER-2)": e.g. History=Hill): apply
   any not yet in the reading, same way.
3. Propagate: status.json rows and the SO prompt files (second-opinions/PROMPT-chatgpt-e160.md, -e163.md, -e164.md, -e143.md, -e145.md if they exist) carry the
   corrected words; SECOND-OPINIONS-QUEUE.tsv rows unchanged unless a prompt path changed. Note E164 is N2 after AUD2-LEDGER-3 and E103 N2 after AUD2-LEDGER-1:
   if their SO rows are not yet marked withdrawn, mark them (`withdrawn` in the status column, reason in the last column).
4. NOTES.md "## FIX-FM1 (8 Oct 2026, account 1, for LANE LEDGER)": each change, token grade before/after, decode --check output. depth_check on the touched
   status.json rows.

## FV-FM2 (Opus 5.5, first verifier, separate from FM-R1; cap $6.5, box 90 min): E165, E167, E168, E169 (Fort Monroe, mssEC 25)
Exactly "## FV-FM1" of .claude/briefs/runs/2026-10-08-acct1-lane-ledger-jobs.md (wave 4) for these four entries (NOTES "## FM-R1"). Heading
"## AUDIT (FV-FM2)". Extra: E165/E168/E169 are key-supplement telegrams (a key-change message: check Plum / Eckert's own published accounts and
Tomokiyo civilwar pages for the same supplement); E169 Mint/Mogul = Steedman vs key.md McPherson is logged in HYPOTHESES.md -- settle by dated witness
or leave both graded M (rule 4). On N3+ D2+ add WORK-QUEUE `AUD2-LEDGER-4` (account-3, Opus 5.5, cap 2.5 per entry) and name it in ROOM for the
account-3 VERIFY lane. hdl at most 40 requests under the token. Unit ~1.5 per entry; stop before an entry that would cross 80%.

## FM-R2a, FM-R2b (Sonnet 5.5, readers; cap $6.5 each, box 120 min each): Fort Monroe 1864 No. 1 rows 11-30 of clean-fm.tsv
Method: exactly "## FM-R1" (wave 3 of the jobs file above) plus: (i) before choosing the book, re-run FM-PRE's share scorer from HEAD code on your rows
(MS18-PRE found entries-fm.tsv best_book did not reproduce on 20 rows) and paste the three shares; (ii) these are mostly SENT from Fort Monroe (Butler's
HQ): Butler's Private and Official Correspondence vols III-V and OR I/33, 36, 40, 42 by date + addressee first (step 0, before any decoding); (iii) a row
whose decode is in print is filed with volume/page and not sent to a verifier.
- FM-R2a (10): 5806/1 5779/1 5787/2 5840/0 5747/2 5838/0 5820/0 5823/0 5838/2 5600/0 -- IDs E170 onward (No. 1), N2-HA onward (No. 2).
- FM-R2b (10): 5824/2 5635/0 5799/1 5584/0 5748/1 5831/0 5589/2 5643/0 5784/0 5805/2 -- IDs E185 onward (No. 1), N2-JA onward (No. 2).
Shared pages (5838/0+5838/2, 5823/0 vs FM-R1's 5823/1, 5584/0 vs FM-R1's 5584/1, 5780 pair): read only your own entry; a continuation goes to ROOM.
Unit ~0.55 per entry. NOTES "## FM-R2a (8 Oct 2026, account 1, for LANE LEDGER)" / "## FM-R2b ...", Remaining gaps / Escalation, gaps_check, decode --check.

## MS18-R1 (Sonnet 5.5, reader; cap $7, box 130 min): mssEC 18 (obj 10074) first 12 1864 No. 1 rows of ms18/clean-ms18.tsv
Rows: 9696/0 9819/2 9836/0 9830/2 9875/2 9769/0 9823/2 9730/1 9751/0 9923/3 9703/0 9923/2. Page text on disk in ciphers/eckert-1864/sources/mssEC18/.
Method: the FM-R1/LS5 reader method (step 0 own transcription; Grant Papers/Basler Google Books query; OR/ORN by date + addressee; book by share AND
header label, matched control = the other books + a meaning-shuffled copy of the chosen book; crops via tools/iiif_lines.py --image; decoded-text phrase
pass). mssEC 18 is a SENT ledger parallel to mssEC 19: diff each row against mssEC 19 (sources/mssEC19) and every filed ID first. IDs E200 onward (No. 1).
9923/2 + 9923/3 are one page: read both, check whether one continues the other. Unit ~0.55 per entry. NOTES "## MS18-R1 (8 Oct 2026, account 1, for LANE
LEDGER)", Remaining gaps / Escalation, gaps_check, decode --check.

## E62-9660 (Sonnet 5.5; cap $3, box 70 min): eckert-1862 -- the 10-entry book test on object 9660, then the last 7 printed residue entries
1. ciphers/eckert-1862/NOTES.md "## Remaining gaps (K8472 ...)": the same pre-registered 10-entry book test K8472 ran (NOTES "## K8472"), with entries picked
   from 9660's own pages (dates spread; >= 8 code-shaped words; not clear in own transcription). hdl at most 40 requests under the token. Verdict per K8472's
   rule; if a book in hand reads it, list the readable 1862-63 entries for the next incarnation (do not read them).
2. Then, offline: E62-ALN's remaining 7 printed residue entries (OR vols 9/7/8; NOTES "## E62-ALN" Remaining gaps) with print/or_align.py, as E62-ALN did;
   conflicts to HYPOTHESES.md, never key.md (rule 4); residue C/M/I counts before/after.
NOTES "## E62-9660 (8 Oct 2026, account 1, for LANE LEDGER)", Remaining gaps / Escalation updated, gaps_check after.
