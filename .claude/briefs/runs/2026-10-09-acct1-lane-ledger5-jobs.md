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
