# LANE LANE-RUN8-account-1 jobs (account 1) -- 6 Oct 2026 03:4x UTC, lane orchestrator session_013d5MxPPQvWPv3KmmcKVUHA

Lane brief: .claude/briefs/default-lane.md (cap 60, box 03:44-13:44 UTC 6 Oct). WORK-QUEUE row LANE-RUN8-account-1: RUN7's own named next
steps for folders a-h first, then tools/next_steps.py runnable rows (cost band S/M), ranked by PROGRESS.tsv closeness to a counted N3+/D2+
result, BnF tie-breaker. VERIFY-BACKLOG.tsv: nothing actionable in a-h (fr16142 counted by RUN7; Birago off limits). Off limits: Birago
(incl. ceppo-nevers, nevers-birago, birago-*), Armstrong, Debosnys, the account-4 private-repo targets (bne20211-ferdinand, destaing-gerard,
bowes-walsingham, hamilton-1650). outreach/huntington-eckert-followup-2026-10.md is under an OUT-CHECK by account 3: no worker edits it.
Every worker: Opus 5.5, one job, then stop. Each solver job first checks that its named step is still undone (NEXT-STEPS.tsv lags the
folders): if a dated NOTES.md section already ran it, take the folder's own Verdict "cheapest next" instead if it fits this job's cap and
box and is not a campaign; otherwise stop and report. Caps sized per CLAUDE.md Usage 6: (subagent passes + 1 reconciliation) x ~1.5 per
pass, plus ~1.5 Opus session floor.
Intake gate (tools/intake_gate_check.py, 6 Oct 03:43 UTC): baluze103-letellier-marca-1644, eckert-1864, eckert-1862,
huntington-blathwayt-madrid-1728, colbert26-lathuillerie-1644, fr16045-pisany-rome-1585, hellen-frederick-1752, fr16104-vivonne-spain-1572
all exit 0 ("edition/page or full-text-search citation found within 6 lines").

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim
  line with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE LANE-RUN8-account-1".
  If --start fails to push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
- Read the folder's NOTES.md tail (Remaining gaps / Escalation / latest dated sections) and AUDIT.md section list before acting.
- Good-citizen rule and the CLAUDE.md host table for every request (one request per host at a time, >= 1.5 s apart; stop a host on
  429/403/challenge). Report request counts per host.
- Rebase before writing shared files (status.json, PROGRESS.tsv, SECOND-OPINIONS-QUEUE.tsv, JSTOR-QUEUE.tsv, ROOM.md); keep both facts
  on conflict. Run `python3 tools/file_shrink_guard.py <every file you touched>` before the final push; push with
  `python3 tools/room.py --push <paths>`.
- Words: never "solved", "cracked", "novel", "first", "new" for anything this project did; rule 10 wording only. Never name the
  owner; never print credentials (test presence with `test -n`). Never call AskUserQuestion. No depth/N-class edits (verifier's job).
- Stop at the cap or at 80% of the box, whichever first; do not start a unit that would cross 80% of either. A stop with work half
  done writes what was done and what remains into the folder's files.
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE
  LANE-RUN8-account-1", then a five-line final report.

## Solver jobs (solver template .claude/briefs/solver.md; report what was found and where it was not found; do not classify novelty;
## rule 4 grades; rule 7 --check before push; pre-register any gate (PREREG file pushed before the answer is opened); a partial
## target keeps Remaining gaps / Escalation and passes `python3 tools/gaps_check.py <target>`; crops via tools/iiif_lines.py pasted
## before the first subagent call, never a full-page image to a subagent)

### R8-BAL103 -- baluze103-letellier-marca-1644, where does the f.50 decode break: transcription or table? (cap 4, box 60 min)
RUN7: f.50r-v decoded with Tomokiyo's 1644 table H 451 M 165 U 14 of 630; table calibrated PASS on f.171r vs f.172r; fr17 judge still
FAILs f.50 (-1.537 vs real_p05 -0.852). Verdict cheapest next: decode each f.50 blind pass separately and test transcription vs table.
Job: (1) decode pass A and pass B separately with the same key; per line, mark where each breaks into non-French. (2) Pre-register a test
(e.g. lines where both passes agree but decode is garbage => table suspect; lines where passes disagree and decode breaks => transcription
suspect), push the PREREG, then run it. (3) For the worst 4-6 break lines only, cut line crops (tools/iiif_lines.py) and one blind Opus/
Sonnet re-read per crop batch; apply only reads that the pre-registered rule settles (corrections TSV, never silently repair
ciphertext). Re-decode, --check, re-run the fr17 judge, report before/after. If table is the suspect, say so and name the April 1644 table
search as next (do not run it).

### R8-ECK64 -- eckert-1864, image-check the thirteen O9-E..Q entries (cap 4.5, box 65 min)
R7B-ECK64B decoded 13 more pp.1-20 entries H 113 from volunteer text only. Job: fetch the mssEC 19 page images for those entries
(Huntington CONTENTdm per the host notes; one request at a time >= 1.5 s), line crops, one blind read per page batch, tabulate volunteer
transcription vs image per code word; corrections TSV + re-decode with decode_no9.py --check; report changes and the H/M counts before/
after. If time remains under 80% of the box, continue "(9)"-marked entries past page 20 only from images already fetched. Do not edit
outreach/ files.

### R8-ECK62 -- eckert-1862, the 1865 cipher book for the 14 cross-entry code words (cap 3, box 50 min)
R7C-ECK62C: 14 code words outside every key on disk agree across two telegrams Dec 1864-Jul 1865. Job: locate the 1865 cipher book
among the Huntington mssEC key books (catalogue/CONTENTdm; the folder's NOTES.md manifests first, then dmGetItemInfo), fetch only the
pages needed, look up the 14 words; per word: found (value, page, grade H) / not found. Carry found values into the key with source lines
and re-run the folder's --check scripts. If no 1865 book is digitised, log the search (URLs, counts) and stop.

### R8-HUNT -- huntington-blathwayt-madrid-1728, finish the 7-form census (cap 2.5, box 45 min)
R7B-HUNT settled the descending glyph = the hand's 7 (gate 11/11 vs 1/25); 13 columns + BLA191 p5 L11 pos3 (et->es flip) remain. Job:
apply the same pre-registered glyph rule to the 13 remaining columns from crops already on disk (fetch only what is missing, hdl.huntington
.org one at a time), settle what the rule settles, re-decode, --check, report targets C/M/U before/after and the BLA191 p5 L11 pos3 call.

### R8-COL26 -- colbert26-lathuillerie-1644, canvas 62-63 numerals + gloss (cap 4.5, box 65 min)
Verdict cheapest next: canvas 62-63 (La Haye, Jan-Feb 1648) numerals + gloss from line crops (tools/iiif_lines.py --image
images/crops/canvas62_full.jpg / canvas63_full.jpg), two blind passes + one reconciliation, same per-canvas key_f23 C test as earlier
canvases. Pre-register the C test before opening the reconciled pairs. Key unchanged unless the pre-registered gate licenses a value.

### R8-PIS -- fr16045-pisany-rome-1585, f.275v L17-L20 interlinear gloss as a C witness (cap 3, box 50 min)
kp86j FAILed and retired kp86d for these lines (D2-PIS275). Job: crop the later-hand interlinear gloss over L17-L20, two blind reads of the
gloss (word level), reconcile, then align gloss to cipher sign by sign (tools/interlinear_align.py if the shape fits); grade C only where
gloss and cipher align without repair; report C/M counts and any sign values the gloss implies that conflict with the current key (rule
4: log a conflict, do not settle by majority).

## Wave 2 (04:0x UTC). Wave 1 lesson: every Opus crop job cost ~3-6 regardless of brief size (3 of 6 over cap); caps below carry a ~3
## Opus session floor. Intake gate 04:03 UTC: hellen-frederick-1752, decode-2678-bnf-colbert127-gravel-1665, fr3151-seure-1558,
## costabili-modena-1491, antt-linhares-chave, baluze103-letellier-marca-1644 all exit 0. august-van-saksen skipped (waits on Dresden).

### R8-HEL -- hellen-frederick-1752, the 0/8 pass over keyed 801-1796 tokens (cap 3.5, box 45 min)
Verdict cheapest next: the 0/8 pass over keyed 801-1796 tokens on the R7A-HEL53 crops (already on disk; no DECODE login needed). Pre-register
the 0/8 decision rule (which reading the key context licenses), push it, then run; corrections TSV (never silently repair), re-decode,
--check, report H/S/M/U before/after. No depth edits.

### R8-G2678 -- decode-2678-bnf-colbert127-gravel-1665, canvases 355-356 + crib test (cap 3.5, box 50 min)
NOTES.md next: re-view canvases 355-356 of btv1b10035540v at native resolution (facing page, docket, slip) with tools/gallica_folio.py and
tools/iiif_lines.py, then a crib test of the three enciphered names against the 1664-65 Regensburg pensioners named in Gravel's printed
dispatches. Pre-register the crib test (candidate list fixed from the print before testing; control = shuffled/unrelated name list).
Gallica one request at a time >= 2 s.

### R8-SEURE -- fr3151-seure-1558, null-tolerant nom_test with its own 10%-null control (cap 3.5, box 45 min)
Verdict cheapest next: null-tolerant nom_test setting with its own 10%-null matched control first; run R1/R2 on the target only if the
control passes its gate (tools/family_run.py discipline: control first, CONTROL BELOW GATE stops). Both numbers into HYPOTHESES.md.

### R8-COST -- costabili-modena-1491, group crops of R1166 P4 with W as its own label (cap 4, box 50 min)
Verdict cheapest next: group crops of R1166 P4 with W as its own label (~2.5), then (only if under 80% of cap and box) short-span boxes
of the R1163/R1165 slips. Crops via tools/iiif_lines.py from images on disk; blind reads per crop batch; corrections TSV; --check.

### R8-LIN -- antt-linhares-chave, Part II test of 829011 as written (cap 3.5, box 45 min)
Verdict cheapest next: the Part II test of 829011 as written (~2). Read the folder's spec of Part II before acting; pre-register, push,
run; token stays M unless the registered gate licenses a reading. Do not re-run the retired column-count instruments.

### R8-BAL103B -- baluze103-letellier-marca-1644, look-alike pass on f.50 (cap 4, box 50 min)
R8-BAL103 (r8/PREREG.md): transcription suspect, not table; its 2-of-3 re-read made the judge worse (m->mm reader bias). Job:
tools/lookalike_pass.py on the f.50 passes for the named confusable pairs (m/mm and any others in r8/), re-decode, fr17 judge before/after.
What machines still split goes to a sign-sorter focus.tsv (do not publish a sorter; if one is built it must PASS tools/sorter_preflight.py
and is handed to the account-3 orchestrator). The 2-of-3 residual is agreement, not accuracy (LESSONS.md "Look-alike pass").
