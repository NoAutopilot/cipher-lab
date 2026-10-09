# Orchestrator jobs, unassigned progress rows, batch 2 (account-4 orchestrator session_01PkUoxUSDziiDv1wCDtqDo4, written 9 Oct 2026 09:4x UTC by date -u)

Source: `python3 tools/progress_block.py --unassigned` at the 09:2x UTC check-in listed 18 rows in six folders with nobody on them.
Three get a worker here (the cheapest named next step in each folder's own Verdict line); the other three are recorded, not queued:
ceppo-nevers-fr3251-1570s (next step needs Gallica, 403 all of 9 Oct; re-queue with the 10 Oct Gallica probe; coverage only, no depth
gain per D2-CEP21M), fr3416-nevers-fils-1589 (next step is a person reading the f.27r L09 gloss: an owner card, which account 4 cannot
write to the desk board), debosnys-1883 (account 3's, never taken over).

Common rules (every job): read CLAUDE.md first (rules 3, 4, 5, 7, 10; Usage 6-8), then this file, then the folder's NOTES.md tail.
ROOM claim first via `python3 tools/room.py "<job_id> worker (account N, Opus)" "claim ... cap, box end" --push`; done line "for
orchestrator (account-4)". PREREG file pushed before any score or tile. `tools/prior_work.py <folder> --step-type <type>` before the
step; answer every LEAD. No key.tsv edit, no reading grade change unless the folder's own pre-registered gate passes; `decode_key.py
--check` (or the folder's decode script --check) exit 0 before the final push. `tools/gaps_check.py <folder>` passes; update the
folder's Verdict line and NEXT-STEPS "next:" with the result. file_shrink_guard on every touched path. Never AskUserQuestion, never
print credentials, never name the owner, never the words solved/cracked/novel/first/new for anything this project did. Stop at the
cap or the 80% box line, whichever first; report cost from get_session is the orchestrator's (the LEDGER row is the orchestrator's).

## UNA2-BIR3252 (account 2, Opus 5.5, cap USD 2, box 60 min)
Folder ciphers/birago-fr3252-1571-72. Step: the Verdict's cheapest next (UNA-BIR3252, 9 Oct): re-cut the 6 mislocated/edge f.36-37
rule-pair tiles with eye-set x,y (UNA-BIR3252's tiles_key.tsv names them), disk only (no Gallica: 403 on 9 Oct), then re-run the same
UNA-BIR3252 blind per-sign 4x read on those 6 tiles only, with the same known-answer tiles (KA was 5/6) and the same pre-registered
rule as UNA-BIR3252 (read its NOTES section and PREREG first; this is attempt 2 of that design -- say so in the PREREG; a third would be
closed by rule 3's third-attempt clause). Apply to passD_v4 only what the rule licenses; placement p and KA reported both ways.
Report: tiles re-cut, KA, labels changed, grades unchanged unless the gate passes. No other Birago step.

## UNA2-PISA (account 2, Opus 5.5, cap USD 2.5, box 60 min)
Folder ciphers/fr16045-pisany-rome-1585. Step: the Verdict's cheapest next (UNA-PISA, 9 Oct): the pre-registered T57->T32 relabel
re-score of the 11 f.301v/f.302v tokens UNA-PISA settled on the barred-varpi cell (una_pisa/result.tsv), CPU only. Read UNA-PISA's NOTES
section, PREREG-UNA-PISA.md and HYPOTHESES.md "UNA-PISA per-token crop compare" first. This is a transcription-label question (tx87/tx87b
carry no T32 label; UNA-PISA read two signs under one label), never a key86 value edit: write the relabel as a candidate transcription
(tx87c or an exceptions file, as the folder's decode layout allows), re-run the folder's decode --check and the judge on both pages,
and report the per-token grade changes the relabel would make, with PIS1-302's alignment witness (T57 -> n 4 of 6) and gloss conflict C4
as the independent checks. Commit the relabel only if the pre-registered gate in PREREG-UNA-PISA.md (or a new PREREG amendment pushed
before scoring) passes; otherwise log the numbers and leave the committed transcription as is. Gallica untouched.

## UNA2-BLA (account 1, Opus 5.5, cap USD 3, box 70 min)
Folder ciphers/huntington-blathwayt-madrid-1728. The Verdict line (NOTES.md "cheapest next: the known-answer re-gate of D3-BLA's L12
signs, ~$1") is stale: D3-BLA2 (8 Oct 21:43 UTC) ran that re-gate and found it UNTESTABLE at N 2 and wrote that a further attempt at the
same design on the 1200 px copies would hit rule 3's third-attempt clause; the instrument it names instead is a higher-resolution image of
BLA191 p5 L12. Job: (1) rewrite the Verdict line and the NEXT-STEPS "next:" from D3-BLA2's own text (re-gate [retired] on the 1200 px
copies, instrument named; the SP 54/19/98B copy stays the owner-side step; name the parallel action below). (2) The one untried cheap
instrument: check whether the Huntington CONTENTdm serves BLA191 p5 larger than 1200 px -- CLAUDE.md Access playbook item 1 (the
`dmGetItemInfo` record and the `getimage` / IIIF-style scale parameters), at most 6 requests to the host, 1.5 s apart, browser UA; the
folder's images/manifest.json names the pointers. If a larger size exists, fetch p5 ONLY, record it in images/manifest.json, cut L12 with
`tools/iiif_lines.py --image` (paste the command), and run the D3-BLA2 known-answer gate on L12's 9 held tokens plus the 5 known-answer
columns of that page at the new resolution (one blind Sonnet call for the strip, one reconciliation, PREREG amendment pushed first); if
the host serves nothing larger, say so with the record URL and stop at (1). Grades move only if the pre-registered gate passes.

## UNA3-BLA (account 1, Opus 5.5, cap USD 2.5, box 60 min) -- added 09:5x UTC after UNA2-BLA
Folder ciphers/huntington-blathwayt-madrid-1728. UNA2-BLA (09:48 UTC, commit 6784ae952) found the Huntington IIIF info.json serves
BLA191 p5 at 8708 px native and read L12 at 4354 px: 8 M -> C (C 138, M 14 of 172), KA 14/14. Its named next step: the same IIIF size
for the remaining 14 M-sign columns (every page that carries one; images/manifest.json lists the pointers; at most one fetch per page,
1.5 s apart, browser UA, <= 8 requests). Same protocol as UNA2-BLA: PREREG amendment pushed first (universe = the 14 M columns + the
page's known-answer columns), `tools/iiif_lines.py --image` crops (paste the command), one blind Sonnet read per page, one
reconciliation, the D3-BLA2 known-answer gate (KA must pass on each page before any M moves). key.tsv unchanged; decode_key --check 0;
gaps_check; Verdict + NEXT-STEPS + AUDIT propagation. Then, in the done line, state H/C/S % and whether `tools/depth_check.py` would
now read D3 -- do NOT change depth or status.json: a separate verifier (DV-BLA, queued by the orchestrator after this job) decides.

## KARL-REQ (account 2, Opus 5.5, cap USD 2.5, box 60 min) -- from WAIT-PASS-4's finding
Folder ciphers/ra-karlxi-fullmakt-1677. REQUEST.md still says "Gated -- do not send ... blocked on the edition search", but NOTES.md
records that NX-UNBLOCK (26 Sept 2026) settled the edition question, and no ASKS.md, SEND-QUEUE.tsv or outreach/ row exists for the
Riksarkivet copy order the folder's Verdict waits on. Job: (1) read NOTES.md (NX-UNBLOCK, R8-KARL3, R9-KARL4, the 9 Oct While-waiting
section) and REQUEST.md; (2) rewrite REQUEST.md's gate line to the current state (cleared or not, citing the NOTES section); (3) if
cleared, draft the copy order as outreach/riksarkivet-karlxi-1677.md following outreach/README.md (rule 1 AI-disclosure sentence, rule 1a
voice, subject/recipient/sign-off placeholders, the recipient address read from Riksarkivet's own contact page with the date, the
reference code SE/RA/25.3/4/II/7/B and the exact document, `status: drafted`, no `checked:` line -- the gate-7 check is a separate
session); add the CONTRIBUTIONS.md row and a `backlog` ASKS.md row (self-contained: one link, one action, what comes back); (4) if not
cleared, say in REQUEST.md and NOTES.md exactly which edition page would settle it and queue that as the next step. Never send; never
name the owner; no personal data.
