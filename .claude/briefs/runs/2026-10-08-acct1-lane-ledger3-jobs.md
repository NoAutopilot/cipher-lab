# LANE LEDGER incarnation 3 worker jobs (account 1, session_01SUrPvi8LCc6ZyHcfTUCKbK; written 8 Oct 2026 23:4x UTC)

Lane brief .claude/briefs/lane-ledger.md (+ lane-common-blast.md). WORK-QUEUE row DEFAULT-account-1-20261008-2340. Continues the **Next** list of the
"LANE LEDGER handoff (session_018DE9C1ZwPUGX7qbyQbQgQb ...)" in STATUS.md. Every ROOM line ends "for LANE LEDGER (account 1)".
Rate limit at writing: seven_day allowed_warning (not a stop under lane-common-blast); five_hour allowed.

Intake gates (pasted 23:4x UTC): `eckert-1864: partial (line 3) -- edition/page or full-text-search citation found within 6 lines` (exit 0);
`eckert-1862: partial (line 3) -- edition/page or full-text-search citation found within 6 lines` (exit 0). Object 5952 (mssEC 25) is an Eckert Papers
ledger inside that check-solved verdict; the prior-work step is the item-level check.

**Common to every worker** -- exactly the "Common to every worker" block of .claude/briefs/runs/2026-10-08-acct1-lane-ledger-jobs.md (CLAUDE.md;
.claude/briefs/prior-work-step.md with one pasted line per check -- `tools/prior_work.py` now exists (8 Oct, warn-first): run it per item if it runs, else
the checklist by hand, civil-war adapter; `date -u`; ROOM claim/halfway/done via tools/room.py; push every two units; 80% stop; rule 10 wording; no
AskUserQuestion; no credentials; file_shrink_guard before the final push; gaps_check after NOTES), with its **hdl.huntington.org token** rule AND the
wave-2 addition of .claude/briefs/runs/2026-10-08-acct1-lane-ledger2-jobs.md (after posting `take`, fetch ROOM again; if another `take` without
`release` is newer than the last release and earlier than yours, wait for its release). Images to scratch, never committed. Before decoding, diff each
row's pointer, date and addressee against every filed `###` header in ciphertext*.txt and status.json (a duplicate is recorded, not decoded).
**Live account-3 claims on eckert-1864 at writing:** AUD3-E96 and AUD-SIG-E146 (verifiers). Do not edit E96 or E146 rows; rebase immediately before
every write to AUDIT.md, NOTES.md, ciphertext.txt, status.json; on a conflict keep both facts.
Solvers: report what was found and where it was not found; do not classify novelty.

---

## FIX-FM3 (Sonnet 5.5; cap $2, box 50 min, no network): carry the wave-2/3 first- and second-audit corrections into the readings
Exactly the method of "## FIX-FM1" in the ledger2 jobs file (entry-level notes through decode.py's existing mechanism -- variant:/split:/plain/positional
notes; never delete or hand-edit key rows; never hand-edit reading.md; `python3 ciphers/eckert-1864/decode.py --write` then `--check`, exit 0).
1. AUDIT.md "## AUDIT (FV-FM3a)" s.3: E170 Babcock signer, E173 Kress, E177 Webster/Dodge, E174 identities.
2. "## AUDIT (FV-FM3c)": its grade fixes (E185-E191) and reading fixes.
3. "## AUDIT (FV-MS18)": its four key corrections -- as `variant:` notes on the entries, NOT key.md edits (rule 4: a conflict goes to HYPOTHESES.md).
4. NOTES "## FIX-DEC" leftovers: E171 tail "Washington" and E177 header/signature (positional notes).
5. "## AUDIT 2 (AUD2-LEDGER-4/-5/-6/-7)": any reading correction they name that is not yet in the reading (class changes are already theirs; do not re-set them).
6. Propagate (rule 10): status.json rows and second-opinions/PROMPT-chatgpt-e<NNN>.md files carry the corrected words; an entry now N0-N2 whose SO row is
   still queued is marked `withdrawn` with the reason. NOTES "## FIX-FM3 (8-9 Oct 2026, account 1, for LANE LEDGER)": each change, grade before/after,
   decode --check output; depth_check on touched status.json rows; file_shrink_guard.

## FV-FM4 (Opus 5.5, first verifier, separate from FM-R2b; cap $4, box 75 min): E193, E194 (Fort Monroe, mssEC 25; NOTES "## FM-R2b")
Exactly "## FV-FM3a ... FV-MS18" of the ledger2 jobs file (wave 2): duplicate diff; own Huntington transcription + CONTENTdm full text; OR I-III, ORN;
Grant Papers via IA be-api by identifier (`papersofulyssess00NNgran`, snippet-only); Butler's Private and Official Correspondence III-V (E193 is
Butler's 5,700 sick prisoners for exchange, Sept 1864 -- the Butler/Ould exchange correspondence in OR II/7 is the first lead); press of the day; G3
with decoded phrases; the sender's copy in mssEC 19/18 on disk. FM-R2b read 5784 from the transcription only: eye-check your entries' lines in the
image (tools/iiif_lines.py --image, crops only) before grading. Depth per .claude/briefs/runs/2026-10-08-acct3-depth-bar.md. AUDIT.md heading
"## AUDIT (FV-FM4)"; status.json/SO rows for N3+ only, audit_status "one audit"; depth_check; file_shrink_guard. On N3+ D2+ append a WORK-QUEUE row
`AUD2-LEDGER-8` (account-3, Opus 5.5, cap 2.5 per entry) and name it in ROOM for the account-3 VERIFY lane. hdl at most 30 requests under the token.
Google Books: probe once; on 429 stop that host. Unit ~1.5 per entry.

## FM-R3a, FM-R3b, FM-R3c (Sonnet 5.5, readers; cap $6.5 each, box 120 min each): Fort Monroe 1864 No. 1 rows 31-60 of clean-fm.tsv
Method: exactly "## FM-R2a, FM-R2b" of the ledger2 jobs file (which is FM-R1's method plus: re-run FM-PRE's share scorer from HEAD on your rows and paste
the three shares before choosing the book; Butler's Private and Official Correspondence III-V and OR I/33, 36, 40, 42 by date + addressee first, step 0
before any decoding; a row whose decode is in print is filed with volume/page and not sent to a verifier). Additions from FV-FM3c (E190 printed word for
word, missed by its reader): in the print pass, also full-text grep OR I/42 pt 3 and I/40 pt 2-3 (and the OR volume for your row's month) on the RARE
NAMES and numbers in the decode, not only on phrases. Grant Papers via IA be-api by identifier, not Google Books (Google Books: one probe; on 429 stop).
Diff every row against mssEC 19/18 filed IDs first (FM rows received at Fort Monroe from Washington may be filed already as the sent copy).
- FM-R3a (10): 5637/2 5649/2 5767/2 5607/1 5703/1 5734/0 5743/1 5770/0 5768/0 5780/1 -- IDs E210 onward (No. 1), N2-KA onward (No. 2).
- FM-R3b (10): 5811/2 5587/1 5747/1 5823/2 5701/1 5626/0 5748/0 5808/1 5814/1 5833/0 -- IDs E220 onward (No. 1), N2-LA onward (No. 2).
- FM-R3c (8 + 2 leads): 5839/2 5734/2 5736/1 5760/0 5683/0 5831/2 5670/1 5729/1 (the last five are long, 140-176 words: price them at 2 units each and
  stop before one that crosses 80%) -- IDs E230 onward (No. 1), N2-MA onward (No. 2). Leads from FV-FM3b/AUD2-LEDGER-6 (AUDIT.md l.5451, l.5835): 5837/1
  (Fox to Rodgers 17 Dec 1864, printed ORN I/11 pp.197-198, = mssEC 19 p.247 pointer 9141 -- check whether 9141 is already filed; if not, file the pair
  at grade C as known plaintext, a key test, not a reading) and 5837/0 (Sheldon 17 Dec, printed OR I/44 p.739: record as in print). 5839/1 = E77, skip.
Shared pages (5747/1 vs FM-R2a's 5747/2; 5748/0 vs FM-R2b's 5748/1; 5734/0 + 5734/2 split across R3a/R3c; 5780/1 vs FM-R1's 5780/0; 5823/2; 5808/1;
5831/2; 5784): read only your own entry; a continuation goes to ROOM. Unit ~0.55 per entry. NOTES "## FM-R3a (9 Oct 2026, account 1, for LANE LEDGER)"
etc., Remaining gaps / Escalation, gaps_check, decode --check.

---

# Wave 2 (written 9 Oct 2026 00:0x UTC)
By get_session: FIX-FM3 2.14 (corrections applied E167-E209; per-entry note types added to decode.py; decode --check 0).

## FM-R3d (Sonnet 5.5, reader; cap $6.5, box 120 min): six long Fort Monroe 1864 No. 1 rows (95-135 words)
Rows: 5784/1 5663/1 5682/0 5826/1 5796/0 5769/0. Method exactly "## FM-R3a, FM-R3b, FM-R3c" above (including the rare-name OR grep and the mssEC 19/18
duplicate diff). Long rows: price 2 units (~1.1) each; stop before a row that would cross 80% of cap or box. 5784/1 shares a page with FM-R2b's 5784/0
(E193, under FV-FM4): read only your own entry. IDs E240 onward (No. 1), N2-NA onward (No. 2). NOTES "## FM-R3d (9 Oct 2026, account 1, for LANE LEDGER)",
Remaining gaps / Escalation, gaps_check, decode --check.

---

# Wave 3 (written 9 Oct 2026 00:2x UTC; seven_day allowed_warning on every session, continuing per lane-common-blast)
By get_session: FV-FM4 5.52 (E193 N3 weak D2, E194 N3 weak D3; AUD2-LEDGER-8 queued; reading fixes for a FIX job), FM-R3a 3.77 (E210-E219; E215 E218 in
print, E211 plaintext on the leaf), FM-R3b 3.48 (E220 E222-E229, none located), FM-R3c 3.22 (E230-E239; E231-E233 E238 E239 in print), FM-R3d 3.00
(E240-E245; E244 in print, three key conflicts logged).

## FIX-FM4 (Sonnet 5.5; cap $1.5, box 40 min, no network): FV-FM4's reading fixes
AUDIT.md "## AUDIT (FV-FM4)": E193 Webster / R. C. plain, "22nd", E194 Hawley plain -- exactly the FIX-FM3 method (entry-level notes, decode.py
--write then --check exit 0, propagate to status.json and second-opinions/PROMPT-chatgpt-e193.md / -e194.md). NOTES "## FIX-FM4 (9 Oct 2026, account 1, for
LANE LEDGER)"; depth_check; file_shrink_guard.

## FV-FM5a, FV-FM5b, FV-FM5c (Opus 5.5, first verifiers, separate sessions from the readers; cap $6.5 each, box 90 min each)
Exactly "## FV-FM4" above (wave 1: duplicate diff; own Huntington transcription + CONTENTdm full text; OR I-III, ORN; Grant Papers via IA be-api by
identifier, snippet-only; Butler's Private and Official Correspondence III-V; press of the day; G3 with decoded phrases; the sender's copy in mssEC 19/18 on
disk; the rare-name OR grep FV-FM3c's E190 lesson added; eye-check lines the reader did not image-check). The reader's own "Remaining gaps" for your entries
are your first print leads. AUDIT.md headings "## AUDIT (FV-FM5a)" etc.; status.json/SO rows for N3+ only, audit_status "one audit"; depth_check;
file_shrink_guard. On N3+ D2+ append WORK-QUEUE `AUD2-LEDGER-9` (FV-FM5a), `-10` (FV-FM5b), `-11` (FV-FM5c) (account-3, Opus 5.5, cap 2.5 per entry) and
name it in ROOM for the account-3 VERIFY lane. hdl at most 30 requests each under the token (wave-2 rule); be-api answered 502 to readers this hour --
one retry after a pause, then log it unreachable. Unit ~1.3 per entry; stop before an entry that would cross 80% of cap or box.
- FV-FM5a: E210, E212, E213, E214, E216 (NOTES "## FM-R3a"). E211 (plaintext on the leaf) is not audited; E217, E219 handed on.
- FV-FM5b: E220, E222, E223, E224, E225 (NOTES "## FM-R3b"; E222/E224/E225 have printed context named there -- decide whether it is the same telegram).
- FV-FM5c: E230, E234, E235, E236, E237 (NOTES "## FM-R3c"; FM-R3c eye-checked only 4 of 9 pages -- eye-check your entries' lines first).
Handed on, not briefed this wave: E217, E219, E226-E229, E240-E243, E245 (first audit, ~1.3 each).
