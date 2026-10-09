# LANE LEDGER incarnation 9 worker jobs (account 1, session_016pcjMK9ShCpNwDUEG955mj; written 9 Oct 2026 23:5x UTC)

Lane brief .claude/briefs/lane-ledger.md (+ lane-common-blast.md). WORK-QUEUE row DEFAULT-account-1-20261009-2342. Continues the **Next** list of the
"LANE LEDGER handoff (session_01FeQWmACzMQn2r9uJttmV36 ...)" (incarnation 8) in STATUS.md. Every ROOM line ends "for LANE LEDGER (account 1)".
seven_day allowed_warning was on through incarnation 8 (not a stop under lane-common-blast; say so in your done line if you see it).

Intake gate: `python3 tools/intake_gate_check.py eckert-1864` -> "eckert-1864: partial (line 3) -- edition/page or full-text-search citation found within
6 lines" (exit 0, 23:5x UTC 9 Oct). Re-run it yourself before deep work and paste the line.

Since incarnation 8 closed (22:3x): AUD2-LEDGER-30..33 all ran on account 4 ("## AUDIT 2 (second adversarial, AUD2-LEDGER-30)" .. "-33" in AUDIT.md), every
class kept; their s.4/s.5 corrections are NOT yet in the reading (notably E358: prisoner Capt. J. G. Ryan, not J. N.; E346 context note). AUD2-LEDGER-33 found
an unread holder sibling 9258/2 (mssEC 19 p.364, 27 July 1865) for a later reader.

**Common to every worker** -- exactly the "Common to every worker" block of .claude/briefs/runs/2026-10-09-acct1-lane-ledger8-jobs.md (which points back to
the ledger7/6/5/4/3 blocks): CLAUDE.md; .claude/briefs/prior-work-step.md with one pasted line per check; `date -u` before every time you write; ROOM
claim/halfway/done via tools/room.py; push every two units; stop before a unit that would cross 80% of cap or box; rule 10 wording; no AskUserQuestion; no
credentials; file_shrink_guard before the final push; gaps_check after NOTES; hdl.huntington.org / CONTENTdm token (post `take`, re-read ROOM, wait for an
earlier un-released take by another worker; post `release` with the request count; at most 40 requests per take, under 300 per session). THREE workers in
this wave use hdl (FV-MS18j, FV-MS18k, MS18-R6): keep takes short and do disk work while waiting. Images to scratch, never committed. Rebase immediately
before every write to AUDIT.md, NOTES.md, ciphertext*.txt, reading*.md, status.json, key.md, HYPOTHESES.md, WORK-QUEUE.tsv; on a conflict keep both facts.
Solvers: report what was found and where it was not found; do not classify novelty. Cost is read by the orchestrator from get_session. Print searches use the
IA ids in ciphers/eckert-1862/ec18/or_volumes.tsv as corrected by FIX-FM16 (warofrebellion431unit = OR I/47 pt 2). Lesson carried from incarnation 8: the
reader's "not located" was wrong for 6 of 13 rows audited -- grep OR by date + addressee on page images before calling anything unlocated.

---

## FIX-FM17 (Sonnet 5.5; cap $3, box 70 min, no network)
Exactly the FIX-FM16 method (ledger8 jobs file, Wave 3; FIX-FM11 is the full statement): entry-level notes through decode.py's existing mechanism; never delete or
hand-edit key rows except as (a) below; never hand-edit reading.md; `python3 ciphers/eckert-1864/decode.py --write` then `--check`, exit 0 (also decode_no2.py,
decode_no9.py --check). Sources, in order:
(a) NOTES "## KEY-CANBY (9 Oct 2026 ...)" and its HYPOTHESES.md rule-4 record: this job MAY add to key.md exactly the condition KEY-CANBY proposes for Leghorn /
    Legend / Leopard (Canby from 11 May 1864, Hurlbut before; H key-book + C print; the rule-4 note naming the witnesses), keep the original key-book row as
    written, and re-grade E55 E323 E334 E345 accordingly. Nothing else in key.md.
(b) AUDIT.md s.5 of "## AUDIT (FV-MS18i)" (negroes/reward are clear words, not key rows Negro/Reward; E358 header with holder 7976-7978; E352-E354 E360 headers
    with OR pages).
(c) AUDIT.md s.4/s.5 of "## AUDIT 2 (second adversarial, AUD2-LEDGER-30)", "-31", "-32", "-33": every reading/header/context correction named there not yet in the
    reading (E358 Ryan J. N. -> J. G. also in FV-MS18i's text if the AUD2 asks it; E346 context note; E333/E335/E340/E347/E349/E350 header notes). Class changes are
    theirs; do not re-set them, but carry each one into status.json and the SO prompt per rule 10 if not already there.
NOTES "## FIX-FM17 (10 Oct 2026, account 1, for LANE LEDGER)": each change, grade before/after, decode --check output; depth_check; file_shrink_guard.
Units: ~4 source blocks x ~0.35.

## FV-MS18j (Opus 5.5, first verifier, separate from every reader; cap $6.5, box 100 min): E351, E355, E356
Exactly "## FV-MS18d" of the ledger8 jobs file (= FV-FM9a / FV-FM8 method: the all-pointer CONTENTdm clear-copy search FIRST, duplicate diff against the mssEC 19
received ledger, OR I-III and ORN by date + both correspondents ON PAGE IMAGES, Grant Papers via IA be-api, the press of the day, G3 with decoded phrases, rare-name
grep, eye-check every graded line on crops via tools/iiif_lines.py --image), on MS18-R5's unlocated rows (NOTES "## MS18-R5" says what the reader did and did not
search, and its "## Remaining gaps" names the cheap next steps):
- E351 (10065/2, 2 Dec 1865, to Bodle, Baltimore, for Hancock: habeas corpus for minors; book share tied No. 1/No. 2 -- test the book first and say if none reads it;
  1865 Baltimore press, Hancock's papers, OR ser. II/III vol. 8/5);
- E355 (9863/0, 7 Oct 1864, Fox: reporter Stiner at Fort Monroe; ORN by "Stiner"/"Fort Monroe" first, addressee M; NY press 7-12 Oct 1864);
- E356 (9729/2, 3 May 1864, Fox to Olcott via Horner: Boston witness, Goodman late Judge Advocate; ORN, Olcott/Navy Yard fraud cases 1864, Boston press).
Also open the unopened holder hits MS18-R5 listed (7898, 7917, 10419, 8911, 10297, 8791, 7943, 4514) by one item-info call each and say whether any is a clear copy
of E351 E355 E356 (or of E357/E359 -- if so, write it in ROOM for FV-MS18k). AUDIT.md "## AUDIT (FV-MS18j)". status.json/SO rows for N3+ only, audit_status "one
audit"; depth_check; file_shrink_guard. On N3+ D2+ append WORK-QUEUE `AUD2-LEDGER-34` (account-3 per lane-common-blast -- account 4 ran 30..33; Opus 5.5, cap 2.5
per entry; fetch first, take the next free number if taken) and name it in ROOM for the account-3/4 VERIFY lane. Fixes in AUDIT s.5 for a later FIX job.
Unit ~1.9 per entry.

## FV-MS18k (Opus 5.5, first verifier, separate from every reader; cap $4.5, box 90 min): E357, E359
Exactly "## FV-MS18j" (above), on:
- E357 (9825/1, 19 Aug 1864, Leet to Bowers at City Point: no troops joined/left Early; rumour Lee's cavalry beaten at Orange C.H.; the ledger labels it "No 2" but
  only No. 1 reads -- record the label-vs-sense conflict per rule 4, do not settle it by the share; OR I/43 pt 1 and pt 2 by 19-20 Aug 1864 and I/42 pt 2 by date on
  page images; Grant Papers 12);
- E359 (9753/1, 4 June 1864, to Lew Wallace via Sampson: 1st Md Veteran Cavalry and Battery D to Washington to Augur; OR I/37 pt 1 and I/36 pt 3 by 3-5 June on page
  images; the reader's near miss Halleck to Schoepf 4 June is a different telegram -- check whether the two are one order sent twice; "tell n/u? see B" open code).
AUDIT.md "## AUDIT (FV-MS18k)". N3+ D2+: WORK-QUEUE `AUD2-LEDGER-35` (next free if taken; account-3, Opus 5.5, cap 2.5 per entry). Unit ~1.9 per entry.

## MS18-R6 (Sonnet 5.5, reader; cap $3, box 100 min): 10 more mssEC 18 No. 1 rows
Method exactly "## MS18-R4" of the ledger8 jobs file (= "## MS18-R2" of the ledger7 file plus the print note) with incarnation 8's lesson: for every row you call
"not located", name the OR volume(s) you read BY DATE on page images, not only the cached phrase grep. Rows, in ms18/clean-ms18.tsv order after 9770/1:
9674/0 and 9886/1 (MS18-R5's spares, already decoded in ms18/ms18_r5_controls.txt -- re-run, check, file), 9676/1, 9769/1 (its pointer appears in ciphertext.txt:
check the entry number first; skip and say so if already filed), 9674/1, 10005/2, 9801/0, 10027/2, 10020/2, 9836/1 (spares 9842/1, 9907/1 if any is skipped).
For 10005/2, 10027/2, 10020/2 (May-June 1865) test the book share first and write "no book in hand" if none reads. IDs from E361 (fetch first; take the next free
one if taken). NOTES "## MS18-R6 (10 Oct 2026, account 1, for LANE LEDGER)" with a per-row line "in print (vol/page) / holder clear copy (pointer) / not located
(sources searched by date)", Remaining gaps / Escalation, gaps_check, decode --check. No audits. Unit ~0.25 per row.
