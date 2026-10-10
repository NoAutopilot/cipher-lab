# LANE LEDGER-14 worker jobs (account 1, session_01ULpLhABprtUpNKbH7M5kdF; written 10 Oct 2026 09:4x UTC by date -u)

Lane brief .claude/briefs/lane-ledger.md (+ lane-common-blast.md). WORK-QUEUE row DEFAULT-account-1-20261010-0939. Blast refill after LANE LEDGER-12 closed
(09:20, "backlog spent"). **Scope: eckert-1864 mssEC 18/19 only (`ciphers/eckert-1864/`, `ms18/`). LANE LEDGER-13 (live, account 1) keeps Fort Monroe
mssEC 25 (`fortmonroe/`) and IDs E440-E599: do not touch either.** Every ROOM line ends "for LANE LEDGER-14 (account 1)". seven_day allowed_warning has been
on since 9 Oct (not a stop under lane-common-blast; say so in your done line if you see it).

Intake gate: `python3 tools/intake_gate_check.py eckert-1864` -> "eckert-1864: partial (line 3) -- edition/page or full-text-search citation found within
6 lines" (exit 0, 09:43 UTC 10 Oct). Re-run it yourself before deep work and paste the line.

**Common to every worker** -- exactly the "Common to every worker" block of .claude/briefs/runs/2026-10-10-acct1-lane-ledger13-jobs.md (and what it points
back to: hdl.huntington.org / CONTENTdm token shared with LANE LEDGER-13 and every other session -- post `take`, re-read ROOM, wait for any earlier
un-released take; `release` with the request count; <= 40 requests per take, < 300 per session; on a dropped connection one retry after 25 s, then stop that
take; prior-work step pasted before the first priced step; rebase before every push to shared files; report what was found and where it was not found, do
not classify novelty; one IA whole-collection be-api phrase query and a re-read of your own print-check output before writing "not located"), **except the
Step-0 ruling, which is replaced for these rows by the RULING below.**

**RULING for this lane (mssEC 18/19 rows not yet filed).** STEP0-KEYCTL (NOTES "## STEP0-KEYCTL", 05cdfed6c) showed the ordered step-0 test fails a
meaning-shuffled-key control on mssEC 18/19 exactly as BOOK-FM65 showed on mssEC 25: the holder transcription of a row is its cipher copy, so step-0 (a)
hits under shuffled keys as often as under the book (0 of 80 recorded hits are book-only). A step-0 hit is therefore a non-test (rule 3) and not a reason to
leave a row unfiled. LANE LEDGER-13's wave-2 ruling applies here: a row is NOT filed only if (i) a holder clear copy exists at another pointer (CONTENTdm
CISOSEARCHALL on rare plain words, all pointers), (ii) it is located in print (vol/page, read on the page image or a be-api snippet), (iii) it is plain with
no code word, or no book reads a clause, or it is too short for a clause above the authentication distance. Every other row is filed with its reading. Paste
step0_ordered (a)/(b) for the row as information only. This lane does NOT re-grade or re-audit any already-filed STEP0-RULE entry (that ruling is the VERIFY
lane's / owner-account orchestrator's).

Per row: re-grep the pointer/entry in ciphertext*.txt and NOTES.md first (skip any filed meanwhile); read the earlier reader's NOTES line for it (its decode
and step-0 figures are there, not re-derived if they reproduce); one CISOSEARCHALL holder query on a rare plain word (control 9678 once per take); decode
under the book (No. 1 `decode.py`, No. 2 `decode_no2.py`; check the header/time word fits); print check by date + both correspondents (the cached OR set
the earlier readers used, Grant Papers via be-api without identifier, Butler Corr. where Butler is a party, the press of the day by phrase); then file or
record. Filing: ciphertext.txt / ciphertext-no2.txt in the existing header format, `decode.py --write` then `--check` (and the other two `--check`), exit 0.
Per-row line in NOTES: "filed E<n> (not located: sources by date) / in print (vol/page) / holder clear copy (pointer) / plain / too short / no clause".
No audits (first verifiers are wave 2). NOTES Remaining gaps / Escalation; `tools/gaps_check.py eckert-1864`; `tools/depth_check.py` if it runs on the
folder; `tools/file_shrink_guard.py` on every touched file before the final push. Unit ~0.25 per row.

---

# Wave 1

## L14-A (Sonnet 5.5, reader; cap $2.5, box 100 min): 8 No. 1 rows held by MS18-R9/R10
Rows: 9835/1 9877/1 9793/0 9826/0 9806/2 9777/1 (MS18-R9 step-0 hits), 9823/3 9865/1 (MS18-R10). IDs E600-E609. NOTES "## L14-A (10 Oct 2026, account 1,
for LANE LEDGER-14)".

## L14-B (Sonnet 5.5, reader; cap $2.5, box 100 min): 8 No. 1 rows held by MS18-R10/R11
Rows: 9787/1 9733/1 9883/0 9802/1 9874/2 9779/0 (MS18-R10), 9743/1 9686/2 (MS18-R11). IDs E610-E619. NOTES "## L14-B (10 Oct 2026, account 1, for LANE
LEDGER-14)".

## L14-C (Sonnet 5.5, reader; cap $2.5, box 100 min): 5 No. 1 rows held by MS18-R11 and 4 No. 2 rows held by N2R-6
Rows: 9869/4 9764/1 9897/1 9862/0 9885/3 (No. 1, IDs E620-E629); 9848/0 9811/0 9688/0 9850/2 (No. 2, N2R-6's step-0 hits; IDs N2-SA onward; N2R-6 named
Grant/Sheridan among their (c) words -- check OR I/43 and I/46 by date first). NOTES "## L14-C (10 Oct 2026, account 1, for LANE LEDGER-14)".

The three readers never hold the hdl token at the same time as each other or a LEDGER-13 worker.

Held for wave 2: first verifiers (Opus, separate sessions, ~1.4/entry, CLAUDE.md verifier template + depth per the acct3 depth bar) on every row wave 1 files
"not located"; AUD2-LEDGER14-<n> WORK-QUEUE rows (account-3 tag) for N3+ D2+; a FIX job on the audits' s.5.

(09:4x UTC 10 Oct by date -u: wave 1 spawned with source_url: L14-A session_01EjyUGmdtU5rKhYXogNeNsb, L14-B session_019KG1CDAcmR826HphyHC8P9, L14-C session_017A3ak76bcEddQEQhfQ2g4Z.)

---

# Wave 2 (written 10 Oct 2026 10:3x UTC by date -u; lane workers 5.61 by get_session)
Wave 1 by get_session: L14-A 1.93 (E600-E604 filed, all not located; 9793/0 9806/2 in print; 9835/1 no clause), L14-B 1.91 (E610-E617 filed; E611 E612 not
located; E610 E613-E617 filed with print citations, which the RULING says should have stayed unfiled -- a verifier confirms N1 or not), L14-C 1.77 (E620 E621
N2-SA filed, not located; 6 in print, unfiled). All filed rows are transcription-conditional (leaves mostly not opened).

Verifier method for all three jobs: exactly "## FV-MS18r" of .claude/briefs/runs/2026-10-10-acct1-lane-ledger12-jobs.md (and what it points back to: the
CLAUDE.md verifier template, depth per .claude/briefs/runs/2026-10-08-acct3-depth-bar.md, G3 re-search with decoded phrases, one IA whole-collection phrase
query on Grant Papers and Butler Correspondence before "not located", leaf eye-check of the filed lines on the IIIF image under the hdl token), **except that
the Step-0 ruling is NOT used**: per this lane's RULING (top of file) a step-0 hit is information only and never by itself a reason for N1. AUDIT.md
"## AUDIT (FV-L14a)" etc.; AUD2-LEDGER14-<n> WORK-QUEUE rows only at N3+ D2+ (account-3 tag), named in ROOM. s.5 corrections are written for a FIX job;
do not apply them. Verifiers never hold the hdl token at the same time as each other or a LEDGER-13 worker.

## FV-L14a (Opus 5.5, first verifier, separate from every reader; cap $7.5, box 110 min): E600 E601 E602 E603 E604 (not located; reader NOTES "## L14-A")
## FV-L14b (Opus 5.5, first verifier; cap $7.5, box 110 min): E611 E612 (reader "## L14-B"), E620 E621 N2-SA (reader "## L14-C")
## FV-L14c (Opus 5.5, first verifier, N1 confirm; cap $3.5, box 80 min): E610 E613 E614 E615 E616 E617 (reader "## L14-B" print citations; E617 date conflict
open): exactly "## FV-MS18p" of the ledger10 jobs file (IA page image or be-api snippet, word-for-word diff against the derived reading block, leaf eye-check),
step 0 information only. A citation that does not hold moves the entry to the full verifier search above within the cap, else names it for wave 3.

Held for wave 3: FIX-L14 (Sonnet, apply the three audits' s.5 through decode.py's entry-note mechanism); readers' unfiled print rows need nothing.
