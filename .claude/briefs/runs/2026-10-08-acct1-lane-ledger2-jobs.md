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

---

# Wave 2 (written 8 Oct 2026 21:1x UTC)
Wave 1 by get_session: FIX-FM1 1.67, FV-FM2 5.27 (E168 N3 D3, E165 N3 weak D3, E167 N3 D2, E169 N2; AUD2-LEDGER-4 queued), FM-R2a 3.77 (E170-E179, none
located), FM-R2b 3.55 (E185-E194; E186 E188 E192 in print), MS18-R1 4.20 (E200-E209; E201 E203 E204 E205 E208 in print). E62-9660 still running.
Google Books answered 429 to every call from every worker since ~20:50 (daily quota; resets midnight Pacific = 07:00 UTC, after this box): do not call it.
Grant Papers instead: IA be-api full text inside the lending-only volumes by identifier, `papersofulyssess00NNgran` (vol. 10 Jan-May 1864, 11 Jun-Aug, 12
Aug-Nov, 13 Nov 1864-Feb 1865), as AUDIT.md's earlier sections did; log it as snippet-only (no page). Basler likewise via IA.

## FV-FM3a, FV-FM3b, FV-FM3c, FV-MS18 (Opus 5.5, first verifiers, separate sessions from the readers; cap $7 each, box 90 min each)
Exactly "## FV-FM2" above (= FV-FM1 of the wave-4 jobs file: duplicate diff first; own Huntington transcription + CONTENTdm full-text; OR I-III, ORN; Grant
Papers (route above) and Basler; Butler's Private and Official Correspondence III-V; press of the day; G3 with decoded phrases; the sender's copy in
mssEC 19/18 or the receiver's in mssEC 25 -- sources on disk), depth per .claude/briefs/runs/2026-10-08-acct3-depth-bar.md, the reader's own "Remaining
gaps" next steps for your entries are your first print leads. Where the reader read a page from the transcription only (FM-R2b: 5635 5799 5584 5748 5831
5643 5784), eye-check your entry's lines in the image (tools/iiif_lines.py --image, crops only) before grading. AUDIT.md headings "## AUDIT (FV-FM3a)" etc.;
status.json/SO rows for N3+ only, audit_status "one audit"; depth_check; file_shrink_guard. On N3+ D2+ append a WORK-QUEUE row `AUD2-LEDGER-5` (FV-FM3a),
`-6` (FV-FM3b), `-7` (FV-FM3c), `-8` (FV-MS18) (account-3, Opus 5.5, cap 2.5 per entry) and name it in ROOM for the account-3 VERIFY lane. hdl at most 40
requests each under the token (wave-2 rule). Unit ~1.4 per entry; stop before an entry that would cross 80% of cap or box.
- FV-FM3a: E170, E172, E173, E174, E177 (NOTES "## FM-R2a").
- FV-FM3b: E171, E175, E176, E178, E179 (NOTES "## FM-R2a"; E171/E175/E176 have related print named there -- decide whether it is the same telegram).
- FV-FM3c: E185, E187, E189, E190, E191 (NOTES "## FM-R2b").
- FV-MS18: E200, E202, E206, E207, E209 (NOTES "## MS18-R1").
Handed on, not briefed this wave: E193, E194 (FM-R2b); FV-FM2's decoder over-count fix for key-supplement telegrams (~0.4).

---

# Wave 3 (written 8 Oct 2026 21:3x UTC; seven_day allowed_warning on workers, keep going per lane-common-blast)
By get_session: E62-9660 2.47 (no book in hand reads 9660; no residue pair added); FV-FM3b 5.46 (E171 E175 E176 N3 D3, E178 N3 weak D2, E179 N3 D2; AUD2-LEDGER-6).

## FIX-DEC (Sonnet 5.5; cap $2, box 50 min, no network): decoder false positives + the residue --check flag
1. ciphers/eckert-1864/decode.py: FV-FM2 (AUDIT "## AUDIT (FV-FM2)": payload words of key-supplement telegrams E165/E168/E169 counted as code) and FV-FM3b
   (AUDIT "## AUDIT (FV-FM3b)": 11 named false positives, plain words/ship names that are also key.md code words). Mark them plain through the entry-level
   mechanism FIX-FM1 used (variant:/split:/plain notes in ciphertext.txt or decode.py's per-entry exceptions), never by deleting key rows; regenerate with
   `--write` then `--check` (exit 0); report H before/after per entry. Do not touch entries a live verifier holds (E170 E172 E173 E174 E177 E185 E187 E189
   E190 E191 E200 E202 E206 E207 E209 -- check ROOM for their done lines first; if done, include their listed false positives too).
2. ciphers/eckert-1862/print/residue_decode.py --check: E62-9660 flagged "residue readings are stale" with page texts matching the manifest and key/decoder
   unchanged. Find the cause (nondeterministic order, seed, timestamp, a file another job rewrote); fix in the script, rerun --check twice, both exit 0.
NOTES "## FIX-DEC (8 Oct 2026, account 1, for LANE LEDGER)" in each folder touched; status.json H counts updated for rows already there; file_shrink_guard.
