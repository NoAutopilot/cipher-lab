# LANE LEDGER incarnation 4 worker jobs (account 1, session_016gnJfRCVWfZbRVf9Bqk3bL; written 9 Oct 2026 03:4x UTC)

Lane brief .claude/briefs/lane-ledger.md (+ lane-common-blast.md). WORK-QUEUE row DEFAULT-account-1-20261009-0339. Continues the **Next** list of the
"LANE LEDGER handoff (session_01SUrPvi8LCc6ZyHcfTUCKbK ...)" in STATUS.md. Every ROOM line ends "for LANE LEDGER (account 1)".
Rate limit at writing: seven_day allowed_warning (not a stop under lane-common-blast); five_hour allowed.

Intake gate (pasted 03:4x UTC): `eckert-1864: partial (line 3) -- edition/page or full-text-search citation found within 6 lines` (exit 0).
Object 5952 (mssEC 25, Fort Monroe) is an Eckert Papers ledger inside that check-solved verdict; the prior-work step is the item-level check.

**Common to every worker** -- exactly the "Common to every worker" block of .claude/briefs/runs/2026-10-08-acct1-lane-ledger3-jobs.md (which points to
ledger-jobs.md's block plus the wave-2 hdl token re-read rule): CLAUDE.md; .claude/briefs/prior-work-step.md with one pasted line per check
(`tools/prior_work.py` per item if it runs, else the checklist by hand, civil-war adapter); `date -u`; ROOM claim/halfway/done via tools/room.py; push
every two units; 80% stop; rule 10 wording; no AskUserQuestion; no credentials; file_shrink_guard before the final push; gaps_check after NOTES;
hdl.huntington.org token (post `take`, re-read ROOM, wait for an earlier un-released take; post `release` with the request count). Images to scratch,
never committed. Diff each row's pointer, date and addressee against every filed `###` header in ciphertext*.txt and status.json first (a duplicate is
recorded, not decoded). Rebase immediately before every write to AUDIT.md, NOTES.md, ciphertext*.txt, status.json; on a conflict keep both facts.
Solvers: report what was found and where it was not found; do not classify novelty.

---

## FIX-FM5 (Sonnet 5.5; cap $2, box 50 min, no network): carry incarnation-3 audit corrections into the readings
Exactly the FIX-FM3 method (ledger3 jobs file): entry-level notes through decode.py's existing mechanism (variant:/split:/plain/positional/merge:/graded:
notes); never delete or hand-edit key rows; never hand-edit reading.md; `python3 ciphers/eckert-1864/decode.py --write` then `--check`, exit 0.
1. AUDIT.md "## AUDIT (FV-FM5a)" s.4 corrections (E210-E216).
2. "## AUDIT (FV-FM5b)" s.3: E220 signer R. C. Webster plain, E223 Baltic plain, and the rest of its section 3/4.
3. "## AUDIT (FV-FM5c)": decoder slips (plain Bermuda/Darling/Columbia/Webster/John); E235's dropped first line.
4. E193 still renders "[20] second" for "22nd" (FIX-FM4 left it): fix it.
5. "## AUDIT 2 (AUD2-LEDGER-8/-9/-10/-11)": any reading correction named that is not yet in the reading (class changes are theirs; do not re-set them).
6. Propagate (rule 10): status.json rows and second-opinions/PROMPT-chatgpt-e<NNN>.md carry the corrected words. NOTES "## FIX-FM5 (9 Oct 2026, account 1,
   for LANE LEDGER)": each change, grade before/after, decode --check output; depth_check on touched rows; file_shrink_guard.

## FV-FM6a, FV-FM6b, FV-FM6c (Opus 5.5, first verifiers, separate sessions from the readers; cap $6.5, $6.5, $5; box 90 min each)
Exactly "## FV-FM5a, FV-FM5b, FV-FM5c" of the ledger3 jobs file (= FV-FM4's method: duplicate diff; own Huntington transcription; OR I-III, ORN; Grant
Papers via IA be-api by identifier, snippet-only; Butler's Private and Official Correspondence III-V; press of the day; G3 with decoded phrases; sender's
copy in mssEC 19/18 on disk; rare-name OR grep; eye-check lines the reader did not image-check). ADDED (FV-FM5c's lesson: 4 of 5 "not located" entries had a
clear period copy at ANOTHER pointer): a CONTENTdm full-text search of the holder's own transcription across ALL pointers (CISOSEARCHALL, suppressfulltext=1,
per CLAUDE.md) on 2-3 distinctive clear words of each entry, before any other print search. Depth per .claude/briefs/runs/2026-10-08-acct3-depth-bar.md.
AUDIT.md headings "## AUDIT (FV-FM6a)" etc.; status.json/SO rows for N3+ only, audit_status "one audit"; depth_check; file_shrink_guard. On N3+ D2+ append
WORK-QUEUE `AUD2-LEDGER-12` (FV-FM6a), `-13` (FV-FM6b), `-14` (FV-FM6c) (account-3, Opus 5.5, cap 2.5 per entry) and name it in ROOM for the account-3
VERIFY lane. hdl/CONTENTdm at most 40 requests each under the token. Google Books: probe once, on 429 stop. Unit ~1.5 per entry; stop before an entry that
would cross 80% of cap or box.
- FV-FM6a: E217, E219 (NOTES "## FM-R3a"), E226, E227 (NOTES "## FM-R3b").
- FV-FM6b: E228, E229 (NOTES "## FM-R3b"), E240, E241 (NOTES "## FM-R3d").
- FV-FM6c: E242, E243, E245 (NOTES "## FM-R3d"; E244's three key conflicts in HYPOTHESES.md are context, not yours to settle).

## FM-R4a, FM-R4b (Sonnet 5.5, readers; cap $6.5 each, box 120 min each): Fort Monroe 1864 No. 1 rows after the 64 used
Method exactly "## FM-R3a, FM-R3b, FM-R3c" of the ledger3 jobs file (FM-R2 method; HEAD share scorer pasted before choosing the book; Butler III-V and OR
I/33, 36, 40, 42 by date + addressee, step 0 before decoding; rare-name OR grep; Grant Papers via be-api; diff against mssEC 19/18 filed IDs). ADDED to step
0: the CONTENTdm full-text search across ALL pointers of the holder transcription on the row's clear words (see FV-FM6 above) -- a clear period copy at
another pointer is filed as such (pointer named), not decoded as unread. Shared pages: read only your own entry; a continuation goes to ROOM. Unit ~0.55
per entry (rows over 95 words: 2 units). NOTES "## FM-R4a (9 Oct 2026, account 1, for LANE LEDGER)" etc., Remaining gaps / Escalation, gaps_check,
decode --check.
- FM-R4a (10): 5770/1 5816/0 5781/1 5789/1 5829/0 5797/0 5752/1 5594/1 5774/0 5781/0 -- IDs E250 onward (No. 1), N2-PA onward (No. 2).
- FM-R4b (10): 5787/1 5629/1 5741/0 5812/0 5610/1 5822/1 5609/2 5790/0 5742/1 5775/1 -- IDs E260 onward (No. 1), N2-QA onward (No. 2).

---

# Wave 2 (written 9 Oct 2026 04:2x UTC; seven_day allowed_warning on every session, continuing per lane-common-blast)
By get_session: FIX-FM5 1.66, FV-FM6a 6.71 (E219 E227 N3; E217 E226 N1), FV-FM6b 6.28 (E228 weak, E229 E240 N3; E241 N1 Intelligencer), FV-FM6c 5.11
(E242 E243 N3; E245 N1), FM-R4a 3.28 (E250-E258; 5594/1 = E62; E255 in print; clear copies E250 10490, E254 9913, E257 4823), FM-R4b 4.58 (E260-E269).
Wave 1 total 27.62. The all-pointer CONTENTdm search found a clear copy for 6 of 23 entries this wave: keep it first.

## FIX-FM6 (Sonnet 5.5; cap $2, box 50 min, no network): FV-FM6a/b/c reading corrections
Exactly the FIX-FM5 method above. Sources: NOTES "## FV-FM6a" reading corrections (E217 Washington, E219 webster/Chief, E226 White House/wharf, E227
William/[Steam]er); AUDIT.md "## AUDIT (FV-FM6b)" s.5 (E228 Wise, E229 Herald, E240, E241 person); "## AUDIT (FV-FM6c)" s.5 (E243 4.15, E245 Ino to be, E242).
Propagate to status.json and second-opinions/PROMPT-chatgpt-e<NNN>.md. NOTES "## FIX-FM6 (9 Oct 2026, account 1, for LANE LEDGER)"; depth_check;
file_shrink_guard.

## FV-FM7a, FV-FM7b, FV-FM7c (Opus 5.5, first verifiers; cap $7, $7, $4.5; box 90 min each)
Exactly "## FV-FM6a, FV-FM6b, FV-FM6c" above (the all-pointer CONTENTdm clear-copy search first). The reader's own "Remaining gaps" for your entries are your
first print leads. FM-R4a image-read only 1 of 9 pages: FV-FM7a eye-checks its entries' lines (tools/iiif_lines.py --image, crops only) before grading.
AUDIT.md headings "## AUDIT (FV-FM7a)" etc.; WORK-QUEUE `AUD2-LEDGER-15` (FV-FM7a), `-16` (FV-FM7b), `-17` (FV-FM7c) on N3+ D2+.
- FV-FM7a: E251, E252, E253, E256, E258 (NOTES "## FM-R4a").
- FV-FM7b: E260, E261, E262, E263, E266 (NOTES "## FM-R4b").
- FV-FM7c: E267, E268, E269 (NOTES "## FM-R4b").
Handed on, not briefed: E250 E254 E257 (reader found holder clear copies: short N1 confirms, ~0.5 each), E255 (in print), E264 E265 (printed context).
