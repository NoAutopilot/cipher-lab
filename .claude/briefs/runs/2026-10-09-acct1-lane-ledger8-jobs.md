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
