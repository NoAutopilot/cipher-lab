# LANE LEDGER incarnation 8 worker jobs (account 1, session_01FeQWmACzMQn2r9uJttmV36; written 9 Oct 2026 20:4x UTC)

Lane brief .claude/briefs/lane-ledger.md (+ lane-common-blast.md). WORK-QUEUE row DEFAULT-account-1-20261009-2039. Continues the **Next** list of the
"LANE LEDGER handoff (session_01PkXfi2qevAQ4DhSpGJHhVb ...)" (incarnation 7) in STATUS.md. Every ROOM line ends "for LANE LEDGER (account 1)".
seven_day allowed_warning is on (not a stop under lane-common-blast; say so in your done line if you see it).

Intake gate: `python3 tools/intake_gate_check.py eckert-1864` -> "eckert-1864: partial (line 3) -- edition/page or full-text-search citation found within
6 lines" (exit 0, 20:44 UTC). Re-run it yourself before deep work and paste the line.

Since incarnation 7 closed (20:04): AUD2-LEDGER-26..29 all ran on account 4 (AUDIT.md "## AUDIT 2 (AUD2-LEDGER-26)" .. "-29"); FIX-FM13 carried FV-MS18b/c
s.5 only, NOT the AUD2-26..29 corrections.

**Common to every worker** -- exactly the "Common to every worker" block of .claude/briefs/runs/2026-10-09-acct1-lane-ledger7-jobs.md (which points back to
the ledger6/5/4/3 blocks): CLAUDE.md; .claude/briefs/prior-work-step.md with one pasted line per check; `date -u` before every time you write; ROOM
claim/halfway/done via tools/room.py; push every two units; stop before a unit that would cross 80% of cap or box; rule 10 wording; no AskUserQuestion; no
credentials; file_shrink_guard before the final push; gaps_check after NOTES; hdl.huntington.org / CONTENTdm token (post `take`, re-read ROOM, wait for an
earlier un-released take by another worker; post `release` with the request count; at most 40 requests per take, under 300 per session). THREE workers in
this wave use hdl (FV-MS18d, FV-MS18e, MS18-R4): keep takes short and do disk work while waiting. Images to scratch, never committed. Rebase immediately
before every write to AUDIT.md, NOTES.md, ciphertext*.txt, reading*.md, status.json, WORK-QUEUE.tsv; on a conflict keep both facts. Solvers: report what was
found and where it was not found; do not classify novelty. Cost is read by the orchestrator from get_session. Print searches use the IA ids in
ciphers/eckert-1862/ec18/or_volumes.tsv (MS18-R2's reader missed 5 of 7 prints on a wrong id).

---

## FV-MS18d (Opus 5.5, first verifier, separate from every reader; cap $8, box 110 min): E333, E334, E335, E340
Exactly "## FV-FM9a" of the ledger6 jobs file (= FV-FM8/FV-FM6 method: the all-pointer CONTENTdm clear-copy search FIRST, duplicate diff against the mssEC 19
received ledger, OR I-III and ORN by date + both correspondents, Grant Papers via IA be-api, Butler III-V, press of the day, G3 with decoded phrases, rare-name OR
grep, eye-check every graded line on crops, tools/iiif_lines.py --image) as FV-MS18b used it, with the sources NOTES "## MS18-R3" says the reader searched and
did not search (E333 Dix / L. C. Turner, Havana spies: Dix papers, NY press 26-30 May 1864, OR ser. II; E334 Rosecrans/Hurlbut May 1864: OR I/34 pt 4 and
I/39 pt 2; E335 Ordnance, Wise to Mason, Cairo: ORN ser. I vol. 26, OR ser. III vol. 4; E340 1 Oct 1865 Sampson / Alberger: 1865 Washington press). The reader
saw period glosses/numerals over code words on E333 and E335: grade them as the leaf's own evidence and say which tokens they settle. AUDIT.md
"## AUDIT (FV-MS18d)". status.json/SO rows for N3+ only, audit_status "one audit"; depth_check; file_shrink_guard. On N3+ D2+ append WORK-QUEUE
`AUD2-LEDGER-30` (account-3, per lane-common-blast; Opus 5.5, cap 2.5 per entry; fetch first, take the next free number if taken)
and name it in ROOM for the account-3/4 VERIFY lane. Fixes in AUDIT s.5 for a later FIX job. Unit ~1.9 per entry.

## FV-MS18e (Opus 5.5, first verifier; cap $3.5, box 75 min): N1 confirms of E331, E332, E336, E337, E338, E339
The reader (MS18-R3) placed each in print from OCR page heads: OR I/47 pt 3 p.560; I/37 pt 2 p.576; I/41 pt 4 pp.390, 420, 438; I/43 pt 1 p.62. For each, find
the printed message on the IA page image (leaf named, not the OCR head), diff it word for word against the reading (date, hour, sender, addressee, body),
and classify N0/N1 per rule 10 with key source `period`; if the print differs in substance, say so and do not force N1. Run the all-pointer CONTENTdm
clear-copy search on each (one CISOSEARCHALL per entry on a rare word; holder copies outrank print as N0 evidence). Depth per rule 4a from the decode's
counts. AUDIT.md "## AUDIT (FV-MS18e)"; no status.json/SO rows for N1; fixes in s.5. Unit ~0.5 per entry.

## FIX-FM14 (Sonnet 5.5; cap $2.5, box 60 min, no network): AUD2-LEDGER-26..29 corrections
Exactly the FIX-FM13 method (ledger7 jobs file, Wave 4; FIX-FM11 is the full statement): entry-level notes through decode.py's existing mechanism; never delete
or hand-edit key rows; never hand-edit reading.md; `python3 ciphers/eckert-1864/decode.py --write` then `--check`, exit 0. Sources: AUDIT.md "## AUDIT 2
(AUD2-LEDGER-26)" (E318), "-27" (E319-E321), "-28" (E325), "-29" (E326): every reading/header correction named there not yet in the reading (class changes
are theirs; do not re-set them, but carry each one into status.json `audit_status`/class fields and the SO prompt per rule 10 if not already there). Do not
touch key.md (KEY-LAV is testing lavender / Tulip). NOTES "## FIX-FM14 (9 Oct 2026, account 1, for LANE LEDGER)": each change, grade before/after, decode
--check output; depth_check; file_shrink_guard.

## KEY-LAV (Opus 5.5; cap $1.5, box 45 min, no network)
Two key questions from the incarnation-7 handoff, the KEY-TW method (ledger6 jobs file "## KEY-TW"): (a) lavender = Washburn (FV-MS18c proposed it from print,
AUDIT "## AUDIT (FV-MS18c)"): grep every filed occurrence of `lavender` in ciphertext*.txt, test the value in each context against a control of random key
names from key.md's name section (same count of contexts), blind verdicts committed before unmask as KEY-BLIND did; (b) Tulip: key.md carries Tulip = Open H
(p.22) and Tulip = Period S (KEY-TW); write the context condition that tells them apart (position at a sentence end vs before a noun/verb, from every filed
occurrence including E319) and check it reads all occurrences. HYPOTHESES.md one row each; NOTES "## KEY-LAV (9 Oct 2026, account 1, for LANE LEDGER)" with
the proposed key.md wording; do not edit key.md (the next FIX job applies it).

## MS18-R4 (Sonnet 5.5, reader; cap $4.5, box 110 min): 10 more mssEC 18 No. 1 rows
Method exactly "## MS18-R2" of the ledger7 jobs file plus the print note above. Rows: seven earlier rows of ms18/clean-ms18.tsv that no filed entry names by
pointer/entry (check each against ciphertext.txt headers first: 9866/3 may be E82's own entry; 10002/2 may be NOTES line 1524's printed 10002 entry -- if so,
skip it and say so): 9892/1, 9835/0, 10002/2, 9827/1, 9866/3, 9825/2, 9820/1; then the next in file order after 10056/2: 9811/2, 9779/1, 9843/1, 9895/2
(stop at ten read). IDs from E341 (fetch first; take the next free one if taken). NOTES "## MS18-R4 (9 Oct 2026, account 1, for LANE LEDGER)" with a per-row
line "in print / holder clear copy / not located (sources searched)", Remaining gaps / Escalation, gaps_check, decode --check. No audits. Unit ~0.4 per row.

---

# Wave 2 (written 9 Oct 2026 21:1x UTC; seven_day allowed_warning, continuing per lane-common-blast; lane ~17 of 60 at writing)
By get_session: FV-MS18d 7.16 (E334 N1 OR I/34 pt 4 p.64; E333 E335 E340 N3 D3; AUD2-LEDGER-30), FV-MS18e 3.40 (E331 E332 E336-E339 N1 on page images), FIX-FM14
0.77, KEY-LAV 2.15 (lavender = Washburne 3/3 vs 0/3; Tulip rule 11/11 + 108/108; E287 misdecode), MS18-R4 2.04 (E341-E350: 4 printed, 6 not located). Wave 1 15.52.

## FIX-FM15 (Sonnet 5.5; cap $3, box 60 min, no network)
Exactly the FIX-FM14 method (above). Sources: AUDIT.md s.5 of "## AUDIT (FV-MS18d)" (E333-E335 E340: decoder errors black/Colored/Ordnance/Frances, headers with
print/holder pointers ORN I/21 pp.302-303, holder 4505, 8004/8825; E334 Legend = Hurlbut vs print Canby: a second witness for the HYPOTHESES.md conflict row
FIX-FM13 opened for E323 -- add it there, rule 4, never settle by majority) and "## AUDIT (FV-MS18e)" (eight decoder overrides, E331 E332 E336-E339 headers with
the OR page and IA leaf). NOTES "## KEY-LAV": this job MAY add to key.md exactly the rows/wording KEY-LAV proposes there (lavender = Washburne at the grade it
proposes; the Tulip Open/Period context rule as a note on the two existing rows and in decode.py's existing per-entry/context mechanism), and fix E287
("tuliped fire") accordingly; nothing else in key.md. Propagate to status.json and SO prompts (rule 10). decode.py / decode_no2.py / decode_no9.py --check exit 0;
depth_check; file_shrink_guard; NOTES "## FIX-FM15 (9 Oct 2026, account 1, for LANE LEDGER)".

## FV-MS18f, FV-MS18g (Opus 5.5, first verifiers, separate from every reader; cap $6.5 each, box 100 min each)
Exactly "## FV-MS18d" (wave 1 above) on MS18-R4's six "not located" rows (NOTES "## MS18-R4" names what the reader did and did not search -- Navy and Grant Papers
were unsearched; the OR print miss rate is real, so grep OR I/37-43 by date + addressee on the or_volumes.tsv IA ids before calling a row unlocated).
- FV-MS18f: E343 (Sheridan via McCaine, 26 Aug 1864; sender unseen), E345 (Hurlbut / Memphis, 19 Aug 1864; M Hurlbut/Europe), E346 (Stanton to Murray, Halifax
  agent Keith, 13 Aug 1864; the book share did not establish No. 1 -- test it first and say if another book reads it better). AUDIT.md "## AUDIT (FV-MS18f)".
- FV-MS18g: E347 (W. P. Smith via Sampson, Grant to Monocacy, 5 Aug 1864), E349 (Meigs to Donaldson, 16 Sept 1864), E350 (Brackett, Planters House, 10 Nov 1864).
  AUDIT.md "## AUDIT (FV-MS18g)".
On N3+ D2+ append WORK-QUEUE `AUD2-LEDGER-31` (FV-MS18f) / `AUD2-LEDGER-32` (FV-MS18g) (account-3, Opus 5.5, cap 2.5 per entry; fetch first, take the next free
number if taken). Unit ~1.9 per entry.

## FV-MS18h (Opus 5.5, first verifier; cap $2.5, box 60 min): N1 confirms of E341, E342, E344, E348
Exactly "## FV-MS18e" (wave 1 above). The reader's print: E341 OR I/39 pt 3 p.703; E342 I/39 pt 2 p.343; E344 I/39 pt 3 p.274 (paragraph 1 only: paragraph 2,
the Eckert-office note about copies to Lamb, is U/M and unprinted -- classify the entry as a whole honestly, and say whether paragraph 2 alone carries an N3
question); E348 I/37 pt 2 (8 July 1864; find the page). AUDIT.md "## AUDIT (FV-MS18h)". If E344 paragraph 2 is N3+ D2+, it rides AUD2-LEDGER-32 or the next free number.

## MS18-R5 (Sonnet 5.5, reader; cap $3, box 100 min): 10 more mssEC 18 No. 1 rows
Method exactly "## MS18-R4" (wave 1). Rows (next in clean-ms18.tsv order after 9895/2, none in a ciphertext.txt header at 21:1x): 10065/2 (2 Dec 1865 -- HEAD
share first; "no book in hand" if none reads), 9821/1, 10004/1, 9791/0, 9863/0, 9729/2, 9825/1, 10043/1, 9753/1, 9770/1 (spare: 9674/0, 9886/1). IDs from E351.
NOTES "## MS18-R5 (9 Oct 2026, account 1, for LANE LEDGER)". No audits. Unit ~0.25 per row.
