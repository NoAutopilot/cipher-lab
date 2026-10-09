# LANE LEDGER incarnation 5 worker jobs (account 1, session_01Avu6MshNgo2uLhVg96J8T8; written 9 Oct 2026 10:5x UTC)

Lane brief .claude/briefs/lane-ledger.md (+ lane-common-blast.md). WORK-QUEUE row DEFAULT-account-1-20261009-1040. Continues the **Next** list of the
"LANE LEDGER handoff (session_016gnJfRCVWfZbRVf9Bqk3bL ...)" (incarnation 4) in STATUS.md. Every ROOM line ends "for LANE LEDGER (account 1)".

Intake gate: eckert-1864 partial, edition/page citation found (exit 0, incarnation 4, re-run by each worker before deep work). Object 5952 (mssEC 25,
Fort Monroe) is an Eckert Papers ledger inside that check-solved verdict; the prior-work step is the item-level check.

Since incarnation 4 closed (04:55): AUD2-LEDGER-12..17 second audits ran on account 4 (AUDIT.md "## AUDIT 2 (AUD2-LEDGER-12..17)"): E252 and E258 moved
N3 -> N1 (printed OR I/43 pt 1), E263 to N3 weak, E267 D3 with header date 15 Oct 1864. FIX-E262 (06:45) already applied E262 Whiskey -> [Troops] and
hoe man -> [Homan]: do not redo it.

**Common to every worker** -- exactly the "Common to every worker" block of .claude/briefs/runs/2026-10-09-acct1-lane-ledger4-jobs.md (which points to the
ledger3 and ledger jobs blocks): CLAUDE.md; .claude/briefs/prior-work-step.md with one pasted line per check (`tools/prior_work.py` per item if it runs,
else by hand, civil-war adapter); `date -u` before every time you write; ROOM claim/halfway/done via tools/room.py; push every two units; stop before a
unit that would cross 80% of cap or box; rule 10 wording; no AskUserQuestion; no credentials; file_shrink_guard before the final push; gaps_check after
NOTES; hdl.huntington.org / CONTENTdm token (post `take`, re-read ROOM, wait for an earlier un-released take by another worker; post `release` with the
request count; at most 40 requests per take, under 300 per session). Images to scratch, never committed. Diff each row's pointer, date and addressee
against every filed `###` header in ciphertext*.txt and status.json first (a duplicate is recorded, not decoded). Rebase immediately before every write to
AUDIT.md, NOTES.md, ciphertext*.txt, status.json; on a conflict keep both facts. Solvers: report what was found and where it was not found; do not
classify novelty. Cost is read by the orchestrator from get_session; do not estimate your own beyond "see the lane ledger".

---

## FIX-FM7 (Sonnet 5.5; cap $2.5, box 60 min, no network): carry FV-FM7 and AUD2-LEDGER-12..17 corrections into the readings
Exactly the FIX-FM5 method (ledger4 jobs file): entry-level notes through decode.py's existing mechanism (variant:/split:/plain/positional/merge:/graded:
notes); never delete or hand-edit key rows; never hand-edit reading.md; `python3 ciphers/eckert-1864/decode.py --write` then `--check`, exit 0.
1. AUDIT.md "## AUDIT (FV-FM7a)" s.6 decoder slips; E252's trailing text is a struck 1 Sept 1864 entry (Head Qrs A. P.) -- remove it from E252's reading
   by note, keep the text recorded in NOTES as a struck entry.
2. "## AUDIT (FV-FM7b)": E261 saddle plain; E266 Iron = soon and nuptial M. (E262 is done: FIX-E262.)
3. "## AUDIT (FV-FM7c)" fixes list (E267 header date 15 Oct 1864 per AUD2-LEDGER-17).
4. "## AUDIT 2 (AUD2-LEDGER-12 .. -17)": any reading correction named that is not yet in the reading (class changes are theirs; do not re-set them).
5. Propagate (rule 10): status.json rows and second-opinions/PROMPT-chatgpt-e<NNN>.md carry the corrected words. NOTES "## FIX-FM7 (9 Oct 2026, account 1,
   for LANE LEDGER)": each change, grade before/after, decode --check output; depth_check on touched rows; file_shrink_guard.

## CONF-FM (Opus 5.5, verifier, separate from every reader; cap $4.5, box 80 min): short N1 confirms + Porter known-plaintext key test
Part A (verifier, CLAUDE.md verifier template, short form): E250 (holder clear copy at pointer 10490), E254 (9913), E257 (4823) from NOTES "## FM-R4a" --
fetch the clear copy's holder transcription by CONTENTdm (dmGetItemInfo), diff it against the reading word by word, and if it is the same telegram write
"## AUDIT (CONF-FM)" with N1 per entry, the key-source field, the diff, depth (rule 4a) and the safe sentence; E255: the OR I/39 pt 3 page (archive.org
full text), N1 or N2 as the comparison shows. status.json rows for these four (text: known); no SO rows (N1). ~0.5 per entry.
Part B (key test, grade C, not a reading): pointers 5820 and 5821 of the Fort Monroe ledger (images: CONTENTdm, under the token) carry Porter's two
telegrams printed in ORN I/11 p.155 (NOTES "## FM-R4b" Remaining gaps, E265). Transcribe the two cipher entries from crops (tools/iiif_lines.py --image,
crops only), align them with the printed text, and report how many cipher words the Cipher No. 1 key (key.md, decode.py) reads to the printed word vs a
shuffled-key control (the ledger's existing controls method, e.g. fortmonroe/fm_control.py). Write HYPOTHESES.md one row with both numbers and NOTES
"## CONF-FM key test". Do not file them as unread readings; any key row the print supports and the key lacks is listed as a candidate, not written to key.md.
Order: Part A first; stop before Part B if 80% of cap is reached.

## FM-R5a, FM-R5b, FM-R5c (Sonnet 5.5, readers; cap $6.5, $8, $7; box 120 min each): Fort Monroe 1864 No. 1 / No. 2 clean rows not yet read
Method exactly "## FM-R4a, FM-R4b" of the ledger4 jobs file (= FM-R3 + FM-R2 method: HEAD share scorer pasted before choosing the book; the CONTENTdm
full-text search across ALL pointers of the holder transcription on the row's clear words FIRST -- a clear period copy at another pointer is filed as such,
pointer named, not decoded as unread; Butler III-V and OR I/33, 36, 40, 42, 43, 44 by date + addressee before decoding; rare-name OR grep; Grant Papers via
IA be-api; diff against mssEC 19/18 filed IDs and the AUD2 N1 finds). Image-check every entry's lines you grade (iiif_lines.py crops, not full pages; FM-R4a
image-read only 1 of 9 pages and its verifier had to do it). Shared pages: read only your own entry; a continuation goes to ROOM. Unit ~0.55 per entry;
rows over 95 words count 2 units. NOTES "## FM-R5a (9 Oct 2026, account 1, for LANE LEDGER)" etc., Remaining gaps / Escalation, gaps_check, decode --check.
Row list = pointer/entry-on-page of fortmonroe/entries-fm.tsv, from a mechanical grep of clean-fm.tsv 1864 rows against NOTES/ciphertext/AUDIT/jobs files
at 10:5x UTC (a row found already handled is recorded and skipped, not re-read).
- FM-R5a (10): 5801/0 5641/1 5768/2 5724/2 5645/2 5824/0 5582/1 5802/1 5829/2 5609/0 -- IDs E270 onward (No. 1), N2-RA onward (No. 2).
- FM-R5b (10, 14 units): 5785/0 5706/0 5630/0 5819/1 5804/1 5798/2 5605/2 5788/2 5724/0 5814/2 -- IDs E280 onward, N2-SA onward. (5785: AUD2-LEDGER-13
  noted 5785, 5813, 5815 carry no filed ID; 5813/5815 Porter traffic partly in ORN I/11 -- check 5785 against ORN I/11 too.)
- FM-R5c (10, 12 units): 5751/2 5722/0 5783/1 5822/0 5616/1 5624/0 5827/2 5632/0 5794/1 5609/1 -- IDs E290 onward, N2-TA onward.
Not briefed this wave: 5820/2 (Part B of CONF-FM covers its page), the long rows 5662/0 (309 words) 5697/1 5797/1 5740/0 5744/1 5777/2 5659/0 5786/0, the
22 clean rows whose best book is No. 9 (decode_no9.py), 5751/2 onward rows 40-43.

---

# Wave 2 (written 9 Oct 2026 11:1x UTC; seven_day allowed_warning on every session, continuing per lane-common-blast)
By get_session: FIX-FM7 2.18, CONF-FM 5.07 (E250 E255 E257 N1 D3; E254 NOT N1 -- 9913 is the sent cipher copy; Porter key test 46/52 vs shuffled p99 3,
candidate Tulip = stop), FM-R5a 2.22 (E270-E279), FM-R5b 3.45 (E280-E289), FM-R5c 2.87 (E290-E299). Wave 1 total 15.79.

## CONF-FM2 (Opus 5.5, verifier, separate from every reader; cap $5, box 80 min): short N1 confirms, exactly CONF-FM Part A's method
Entries whose reader found a holder clear copy at another pointer or the telegram in print: E271 (4587; also Butler IV pp.148-149), E273 (10376), E274
(4593), E276 (4493; OR I/33), E279 (10238) from NOTES "## FM-R5a"; E282 (10267-10268), E287 (OR I/42 pt 3 + Butler V p.231) from "## FM-R5b"; E290 (OR I/40
pt 2 p.85), E296 (OR I/42 pt 3 p.971) from "## FM-R5c" (check the printed page numbers on the page image, not the OCR line). Diff word by word; N1 where it is
the same telegram, otherwise say what it is (a sent cipher copy, as E254/9913, is NOT a clear copy: leave the entry for a first verifier and say so).
"## AUDIT (CONF-FM2)", status.json rows (text: known), no SO rows. Decoder slips the diff exposes go in AUDIT s.4 for a FIX job. ~0.5 per entry.

## FV-FM8a, FV-FM8b, FV-FM8c (Opus 5.5, first verifiers; cap $7 each; box 90 min each)
Exactly "## FV-FM7a, FV-FM7b, FV-FM7c" of the ledger4 jobs file (= FV-FM6 method: the all-pointer CONTENTdm clear-copy search FIRST; duplicate diff; OR
I-III, ORN; Grant Papers via IA be-api; Butler III-V; press of the day; G3 with decoded phrases; rare-name OR grep). The reader's own "Remaining gaps" for
your entries are your first print leads. FM-R5b and FM-R5c eye-checked only some pages: eye-check every line you grade (tools/iiif_lines.py --image, crops
only) before grading. AUDIT.md headings "## AUDIT (FV-FM8a)" etc.; status.json/SO rows for N3+ only, audit_status "one audit"; depth_check;
file_shrink_guard. On N3+ D2+ append WORK-QUEUE `AUD2-LEDGER-18` (FV-FM8a), `-19` (FV-FM8b), `-20` (FV-FM8c) (account-3, Opus 5.5, cap 2.5 per entry) and
name it in ROOM for the account-3 VERIFY lane. Unit ~1.3 per entry; stop before an entry that would cross 80% of cap or box.
- FV-FM8a: E254 (CONF-FM: 9913 is the sent cipher copy, not a clear copy; AUDIT "## AUDIT (CONF-FM)"), E270, E272, E275, E277 (NOTES "## FM-R5a").
- FV-FM8b: E280, E281, E283, E284, E285 (NOTES "## FM-R5b"; E283 E285 against ORN I/11 page by page).
- FV-FM8c: E293, E294, E295, E297, E298 (NOTES "## FM-R5c"; E298 against Basler, Collected Works of Lincoln vol. 8, and OR I/39 pt 3 for 16 Oct 1864).
Handed on, not briefed: E278 (FM-R5a), E286 E288 E289 (FM-R5b, pages not image-read), E291 E292 E299 (FM-R5c, printed context only).

---

# Wave 3 (written 9 Oct 2026 11:4x UTC; seven_day allowed_warning, continuing per lane-common-blast)
By get_session: CONF-FM2 3.39 (9 N1 D3), FV-FM8a 5.58 (E270 N1 OR I/42 pt 3 p.481; E254 E272 E277 N3 D3, E275 N3 D2; AUD2-LEDGER-18), FV-FM8c 6.38 (E294 E295
E297 N1 holder clear copies, E298 N1 OR I/41 pt 4; E293 N3 D2; AUD2-LEDGER-20); FV-FM8b running (AUD2-LEDGER-19 queued). Lane ~40 of 60 at writing.

## FV-FM8d (Opus 5.5, first verifier; cap $5.5, box 80 min)
Exactly "## FV-FM8a, FV-FM8b, FV-FM8c" above (Wave 2), WORK-QUEUE `AUD2-LEDGER-21` on N3+ D2+. Entries: E278 (NOTES "## FM-R5a"), E286, E288, E289 (NOTES
"## FM-R5b"; pages 5605 5724 5814 were not image-read by the reader -- eye-check every line on crops first; E289 against ORN I/11 page by page for 1 Dec 1864).

## FIX-FM8 (Sonnet 5.5; cap $2.5, box 60 min, no network) -- spawned only after FV-FM8b and FV-FM8d report
Exactly the FIX-FM7 method (Wave 1). Sources: AUDIT.md "## AUDIT (CONF-FM)" s.4 and "## AUDIT (CONF-FM2)" s.4 decoder slips (Knocks = Knox E271/E274, plain
Chicken/person/shelter/ann, weasilers = Steamers, 6.45 not 51, page fixes E287 p.107, E271 p.148, E276 p.670); "## AUDIT (FV-FM8a)" .. "(FV-FM8d)" reading
fixes (E254 contrive; E275 whimper = Transport; E298 header place Fort Monroe); FM-R5a's own slips (E273 Chickahominy, E276 in person, E279 shelter).
Candidate key rows (whiskey = troops from FV-FM8a, Tulip = stop from CONF-FM) are NOT written to key.md: list them in NOTES as candidates. Propagate to
status.json and SO prompts; NOTES "## FIX-FM8 (9 Oct 2026, account 1, for LANE LEDGER)"; decode --check exit 0; depth_check; file_shrink_guard.
