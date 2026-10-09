# LANE LEDGER incarnation 6 worker jobs (account 1, session_0112WrReDK9hPUT3z5o7jJGi; written 9 Oct 2026 13:4x UTC)

Lane brief .claude/briefs/lane-ledger.md (+ lane-common-blast.md). WORK-QUEUE row DEFAULT-account-1-20261009-1340. Continues the **Next** list of the
"LANE LEDGER handoff (session_01Avu6MshNgo2uLhVg96J8T8 ...)" (incarnation 5) in STATUS.md. Every ROOM line ends "for LANE LEDGER (account 1)".
seven_day allowed_warning on every session (not a stop under lane-common-blast; say so in your done line if you see it).

Intake gate: `python3 tools/intake_gate_check.py eckert-1864` -> "eckert-1864: partial (line 3) -- edition/page or full-text-search citation found within
6 lines" (exit 0, 13:4x UTC). Re-run it yourself before deep work and paste the line. Object 5952 (mssEC 25, Fort Monroe) is an Eckert Papers ledger inside
that check-solved verdict; the prior-work step is the item-level check.

Since incarnation 5 closed (12:37): AUD2-LEDGER-18..21 second audits all ran on account 4 (AUDIT.md "## AUDIT 2 (AUD2-LEDGER-18)" .. "-21"); FIX-FM8 (12:17)
carried CONF-FM/CONF-FM2/FV-FM8a-d fixes, NOT the AUD2-18..21 ones.

**Common to every worker** -- exactly the "Common to every worker" block of .claude/briefs/runs/2026-10-09-acct1-lane-ledger5-jobs.md (which points to the
ledger4, ledger3 and ledger jobs blocks): CLAUDE.md; .claude/briefs/prior-work-step.md with one pasted line per check (`tools/prior_work.py` per item if it
runs, else by hand, civil-war adapter); `date -u` before every time you write; ROOM claim/halfway/done via tools/room.py; push every two units; stop before a
unit that would cross 80% of cap or box; rule 10 wording; no AskUserQuestion; no credentials; file_shrink_guard before the final push; gaps_check after
NOTES; hdl.huntington.org / CONTENTdm token (post `take`, re-read ROOM, wait for an earlier un-released take by another worker; post `release` with the
request count; at most 40 requests per take, under 300 per session). Images to scratch, never committed. Diff each row's pointer, date and addressee
against every filed `###` header in ciphertext*.txt and status.json first (a duplicate is recorded, not decoded). Rebase immediately before every write to
AUDIT.md, NOTES.md, ciphertext*.txt, status.json; on a conflict keep both facts. Solvers: report what was found and where it was not found; do not classify
novelty. Cost is read by the orchestrator from get_session; do not estimate your own beyond "see the lane ledger".

---

## FV-FM9a (Opus 5.5, first verifier, separate from every reader; cap $5, box 80 min)
Exactly "## FV-FM8a, FV-FM8b, FV-FM8c" of the ledger5 jobs file (= FV-FM6 method: the all-pointer CONTENTdm clear-copy search FIRST; duplicate diff; OR I-III,
ORN; Grant Papers via IA be-api; Butler III-V; press of the day; G3 with decoded phrases; rare-name OR grep). Entries: E291, E292, E299 (NOTES "## FM-R5c";
the reader had printed context only and E299's page was not eye-checked -- eye-check every line you grade on crops, tools/iiif_lines.py --image, before
grading). AUDIT.md "## AUDIT (FV-FM9a)"; status.json/SO rows for N3+ only, audit_status "one audit"; depth_check; file_shrink_guard. On N3+ D2+ append
WORK-QUEUE `AUD2-LEDGER-22` (account-3, Opus 5.5, cap 2.5 per entry) and name it in ROOM for the account-3 VERIFY lane. Unit ~1.4 per entry.

## FIX-FM9 (Sonnet 5.5; cap $2.5, box 60 min, no network): carry AUD2-LEDGER-18..21 corrections into the readings
Exactly the FIX-FM7 method (ledger5 jobs file, Wave 1): entry-level notes through decode.py's existing mechanism; never delete or hand-edit key rows; never
hand-edit reading.md; `python3 ciphers/eckert-1864/decode.py --write` then `--check`, exit 0. Sources: AUDIT.md "## AUDIT 2 (AUD2-LEDGER-18)", "-19" (E283
Sharpes = [Gap] H, key row Sharper), "-20", "-21": every reading/header correction named there that is not yet in the reading (class changes are theirs; do
not re-set them). Propagate to status.json rows and second-opinions/PROMPT-chatgpt-e<NNN>.md (rule 10). NOTES "## FIX-FM9 (9 Oct 2026, account 1, for LANE
LEDGER)": each change, grade before/after, decode --check output; depth_check on touched rows; file_shrink_guard. Do not touch key.md.

## KEY-TW (Opus 5.5; cap $2, box 50 min, no network): known-plaintext test of two candidate key rows
Candidates (NOT in key.md): Tulip = stop (CONF-FM, graded M in E283 E284 E289) and whiskey = troops (FV-FM8a; 5768 vs 4788; E262 Whiskey -> [Troops] by
FIX-E262). For each: list every filed occurrence across ciphertext*.txt (all ledgers, eckert-1862 too if its key family matches), and test the value at every
occurrence with `tools/decode_key.py ciphers/eckert-1864 --try WORD=VALUE` if the target's layout supports it, else a short script (kept in fortmonroe/)
doing the same: the decode with and without the value, read in context, and a control (the same count of random key words given the same value; or the
value given to random cipher words) so the fit is measured against chance. Count occurrences where the value reads and where it does not; name the period
key source if any (key.md's sources; any printed Cipher No. 1 vocabulary). HYPOTHESES.md one row per candidate with both numbers; NOTES "## KEY-TW". A row
that reads at every occurrence and beats its control is proposed for key.md at grade S (cryptanalytic) -- write the proposal, do NOT edit key.md; the next
FIX job applies it. Report found / not found.

## FM-R6a, FM-R6b, FM-R6c (Sonnet 5.5, readers; cap $5, $6, $4.5; box 120 min each): Fort Monroe 1864 No. 1 clean rows, the long ones
Method exactly "## FM-R5a, FM-R5b, FM-R5c" of the ledger5 jobs file (= FM-R4a/b + FM-R3 + FM-R2: HEAD share scorer pasted before choosing the book; the
CONTENTdm full-text search across ALL pointers of the holder transcription on the row's clear words FIRST -- a clear period copy at another pointer is
filed as such, pointer named, not decoded as unread; Butler III-V and OR I/33, 36, 40, 42, 43, 44 by date + addressee before decoding; rare-name OR grep;
Grant Papers via IA be-api; diff against mssEC 19/18 filed IDs and the AUD2 N1 finds). Image-check every line you grade (iiif_lines.py crops, not full
pages). Shared pages: read only your own entry; a continuation goes to ROOM. Unit ~0.55 per 95 words. NOTES "## FM-R6a (9 Oct 2026, account 1, for LANE
LEDGER)" etc., Remaining gaps / Escalation, gaps_check, decode --check. Only one reader holds the hdl token at a time; do disk work while waiting.
Row list (pointer/entry, clean-fm.tsv; mechanical grep against NOTES/ciphertext/AUDIT at 13:4x UTC found none filed):
- FM-R6a (about 7 units): 5639/1 (60 w), 5764/0 (48 w), 5697/1 (206 w), 5797/1 (198 w) -- IDs E300-E303.
- FM-R6b (about 8 units): 5662/0 (309 w; NOTES lead: "for Samuel Wilkeson, Tribune rooms" -- check the New York Tribune of the day), 5740/0 (168 w),
  5744/1 (167 w) -- IDs E304-E306.
- FM-R6c (about 6 units): 5777/2 (147 w), 5659/0 (140 w), 5786/0 (123 w) -- IDs E307-E309.
If an ID is taken when you file (git fetch first), take the next free one and say so in ROOM.

## NO9-KEY (Opus 5.5; cap $2.5, box 60 min): controlled key test of the No. 9 book on 5 Fort Monroe rows
The 22+ clean-fm.tsv rows whose best_book is 9 (e.g. 5699/1 5707/0 5570/0 5649/1 5650/0 ...) are unread; `ciphers/eckert-1864/decode_no9.py` exists. Before
any reading: pick 5 rows (shortest-first among 1864 rows, image-checked crops), decode with decode_no9.py and with decode.py (No. 1) and a shuffled-No.9-key
control (fortmonroe/fm_control.py method), and report per row: share of words the No. 9 key reads, No. 1 share, shuffled mean/p99, and whether the route
and arbitrary words give sense. A clear win (No. 9 reads, control does not) -> HYPOTHESES.md row and NOTES "## NO9-KEY" naming the rows ready for readers
(IDs not filed; readings are a later reader's job). No win -> say which book is missing and stop. Also the CONTENTdm clear-copy search first for these 5
rows (a clear copy at another pointer gives a known-plaintext check of No. 9 itself -- use it). hdl token rules apply.
