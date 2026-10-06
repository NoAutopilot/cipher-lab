# LANE LANE-RUN13-account-2 jobs (account 2) -- 6 Oct 2026 13:1x UTC, lane orchestrator session_015WZUp6HMWrwUG6YxwSbq34

Lane brief: .claude/briefs/default-lane.md (cap 60, box 13:11-23:11 UTC 6 Oct). WORK-QUEUE row LANE-RUN13-account-2: RUN12's named
next steps for this split (STATUS.md "LANE LANE-RUN12-account-2 handoff", "Open for the next i-r lane"; verifier propagation flags
first), then tools/next_steps.py runnable rows (S, M) and `parallel` actions (plain next_steps, not --hot-only). Folders i-r
(account 1 a-h, account 4 s-z). wvo-hessen and sachsstaatsarchiv-manteuffel are s-z (account 4's split), not taken here.
VERIFY-BACKLOG.tsv i-r row: nla-heinrich-braunschweig-1519 audit2 (low) -- not run: N0, Outreach gate 2 applies only above N1.
Off limits: Birago (incl. nevers-birago-fr3251-1572), Armstrong, Debosnys; riksarkivet-r4282-1628.
Gate 0a: SESSION-SWEEP-account-2 row still `claimed` (since 5 Oct 23:10, > 90 min), its TSV on disk; RUN7-RUN12 proceeded the same way.
No live claim (< 6 h, no done) on any wave-1 folder in the last 600 ROOM lines; no overlap with the DEFAULT-account-1-1240 or
DEFAULT-account-4-1235 job files.
Every worker: Opus 5.5 (Sonnet 5.5 only where stated), one job, then stop. Each job first checks that its named step is still undone
(a dated NOTES.md section may already have run it); if so, stop and report rather than inventing work.

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim
  line with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE LANE-RUN13-account-2".
  If --start fails to push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
- Read the folder's NOTES.md tail (Remaining gaps / Escalation / latest dated sections), HYPOTHESES.md and AUDIT.md section list first.
- Good-citizen rule and the CLAUDE.md host table for every request (one request per host at a time, >= 1.5 s apart; stop a host on
  429/403/challenge, one retry after a pause at most). Report request counts per host.
- Rule 3: any gate is pre-registered (a PREREG file committed and pushed before the scored run), with a matched control that can vary on
  the statistic tested; report both numbers. Rule 4 grades with counts. Rule 7: `tools/decode_key.py <folder> --check` (or the folder's
  own decode script --check) exit 0 before push if the reading or key changed. A reading change after AUDIT.md: say so in NOTES.md and
  flag in ROOM for a verifier.
- Rebase before writing shared files (status.json, PROGRESS.tsv, ROOM.md, HYPOTHESES.md, NOTES.md of a folder another job also touches);
  keep both facts on conflict. Run `python3 tools/file_shrink_guard.py <every file you touched>` before the final push; push with
  `python3 tools/room.py --push <paths>`.
- Partial targets: update "## Remaining gaps" / "## Escalation" (Verdict line) and pass `python3 tools/gaps_check.py <target>`.
- Words: never "solved", "cracked", "novel", "first", "new" for anything this project did; rule 10 wording only. Never name the
  owner; never print credentials (test presence with `test -n`). Never call AskUserQuestion. Report what was found and where it was not
  found; do not classify novelty (verifier jobs excepted, where the brief says).
- Stop at the cap or at 80% of the box, whichever first; do not start a unit that would cross 80% of either. A stop with work half
  done writes what was done and what remains into the folder's files. An Opus session floor is about 1.5; caps below assume it.
- Vision work: crop step mandatory and pasted (`tools/iiif_lines.py --image FILE --out DIR` or the --ark/--canvas form); give
  subagents only crop paths, one page/leaf per call (or the stated crop batch), never a full-page image. Price: ~1.5 per Sonnet
  subagent pass, reconciliation = 1 unit. Thumbnail/contact-sheet triage by the worker's own eye at low resolution is allowed.
- Sorters: any sorter meant for the owner must PASS `python3 tools/sorter_preflight.py` and have 5+ random tiles opened against the line
  image; it is handed to the account-3 orchestrator (ROOM flag line) to publish. Never publish an artifact or edit ASKS.md yourself.
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE LANE-RUN13-account-2",
  then a five-line final report.

## Wave 1 (spawned 13:2x UTC 6 Oct). Intake gate output (13:16 UTC) pasted per job.

### R13-LVNV -- VERIFIER, lodewijk-van-nassau-1573-74: carry R12-LVN16C into AUDIT.md (Opus; cap 2.5, box 50 min)
Intake: `lodewijk-van-nassau-1573-74: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`
You are a verifier, a session separate from every solver. Claim under audit: NOTES.md "R12-LVN16C" -- R12-LVNV2's six 4616 H-row
corrections applied (lvn16/corrections_lvnv2.tsv, commit 46885e4fb): 4616 C 250->249, M 12->13, four letters 2359/4047 (58.3%).
1. Re-run `python3 ciphers/lodewijk-van-nassau-1573-74/lvn16/apply.py --check` and `tools/decode_key.py` with decode_4616_full.json
   `--check`; confirm the six rows match AUDIT.md "R12-LVNV2" exactly and the counts in NOTES.md.
2. Carry the applied state into AUDIT.md (counts, depth figures, safe sentence if any figure in it moved) and into any
   SECOND-OPINIONS-QUEUE.tsv row for this target (rule 10 propagation); status.json depth fields only if `tools/depth_check.py` says
   they moved. No novelty search is needed unless a plaintext word in a safe sentence changed; say which.
3. Eye check (the NOTES next step, ~$1, only if 1-2 leave budget under 2.0): ~30 random uncontested 3/7/8/9 H rows of 4616 on the
   300-dpi crops (lvn16/), report how many look wrong; correct nothing yourself -- list them in AUDIT.md for a solver.
Do not decode beyond --check, do not touch 4610/4611 (R13-LVN10B runs in parallel there).

### R13-RJMV -- VERIFIER, rah-juan-manuel-1521: audit R12-RJM9501 (Opus; cap 2.5, box 50 min)
Intake: `rah-juan-manuel-1521: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`
Verifier, separate from every solver. Claim under audit: NOTES.md "R9501 f.34: two blind passes and a trial decode with Tomokiyo's
published key (R12-RJM9501)": S 309, M 113, U 331 of 753; judge FAIL es1600/es17c with the shuffled-order decode close behind.
1. Confirm which leaf was read: the worker's session summary said "f.40" while its brief, ROOM line and NOTES say f.34. Check the
   image sha1 in images/manifest.json and the crop source against DECODE R9501's page list; say which leaf.
2. Re-derive the trial decode (the folder's own script, --check) and confirm grades follow R12-RJMV's licence (S only for A Z R 4 F,
   M for other labels and every split, nothing H or C). Count any grade outside that licence.
3. Re-run the two judge calls and the shuffled-order control; compute the shuffled spread over >= 5 seeds (the worker ran one seed) and
   say whether "judge cannot decide" holds.
4. Carry the R9501 result into AUDIT.md (the reading changed after AUDIT.md) and any SECOND-OPINIONS-QUEUE.tsv row; correct any
   over-claim. No N-class change unless the evidence requires it.

### R13-LVN10B -- lodewijk-van-nassau-1573-74: 4610 p3 two blind passes in two crop batches (Opus; cap 7, box 80 min)
Intake: `lodewijk-van-nassau-1573-74: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`
NOTES.md "R12-LVN10" named this: pass B4 was truncated past crop 11 (an incomplete pass, a defect), so re-run both blind passes of
4610 p3 split into two calls of 11 crops each per pass (4 Sonnet calls), naming the hand's hooked 1 vs 2 and 5 vs 3 / 8 vs 3 in the
prompt, against the SAME PREREG gate (lvn10/PREREG.md: 230 H control rows, >= 0.90 per pass; settle only when A == B). Write a short
PREREG addendum (pass layout and prompt change only, gate unchanged) committed and pushed before any read. Re-fetch the WVO PDF once
(resources.huygens.knaw.nl/media/wvo/images/04000-04999/04610.pdf), render p3 at 300 dpi, check the sha1 against
a41b5df838e49cefb71e30cdfbe0803f3947d591, re-cut with the exact iiif_lines.py command in R12-LVN10 and paste it. 4 calls x ~1.5 + 1
scoring unit. This is attempt 2 of this instrument on 4610 (a defect repair): if the control FAILs again, log it, apply nothing, and
write in Remaining gaps that a third attempt needs a different instrument (rule 3 third-attempt clause). If PASS, apply via
lvn10/apply.py, decode --check, flag the reading change for a verifier. Do not touch 4616 or AUDIT.md (R13-LVNV runs there).

### R13-OLDSEG -- na-oldenbarnevelt-2442-1605: per-segment es1600 judge of B/C1 (Opus; cap 3, box 50 min)
Intake: `na-oldenbarnevelt-2442-1605: open (line 1) -- edition/page or full-text-search citation found within 6 lines`
NOTES.md section 16 Verdict step (e): split the B/C1 reading (N=634) into 4 windows of ~160 letters; pre-register (PREREG committed
first) the window cut, the judge (tools/judge_plaintext.py on es1600) and a matched control: real es1600 held-out windows of the same
length (real_p05 at that N, >= 200 windows) and shuffled-decode windows. Report each window's score beside its own real_p05 and
null, and whether the FAIL concentrates in the low-confidence lines (OLD-PASS2 disagreements, the 36 uncertain words). Check first that
the control can vary on the statistic (a window score can differ from the control's). No corpus building (the corpus knob is closed).

### R13-KAL10 -- kaliningrad-2015: one different design family with its own matched control (Opus; cap 4, box 70 min)
Intake: `kaliningrad-2015: open (line 1) -- edition/page or full-text-search citation found within 6 lines`
NOTES.md "Next steps (R12-KAL9)": the light homophonic family is spent on every scheme tried; the next test is a different design family
(nomenclator/code groups or transposition). Run `python3 tools/design_prior.py` on the ciphertext first and paste its ranking; pick the
single highest-ranked family not yet logged in HYPOTHESES.md, and run it through `tools/family_run.py` if the family is supported there,
else a short script with the control built at the target's N, symbol count and language (rule 3: control first, gate pre-registered,
stop if CONTROL BELOW GATE). One family only; log both numbers in HYPOTHESES.md. If no family is runnable inside the cap, write which
one and why in NOTES.md and stop.

### R13-SURSWP4 -- na-suriname-map-1781: inv. 373 offset sweep remainder (Opus; cap 3.5, box 70 min)
Intake: `na-suriname-map-1781: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`
Finish the inv. 373 1-in-4 offset sweep at n = 2 mod 4 over 0270-0598 (~82 scans) and 0614-0798 (~47 scans), same method and positive
control on every sheet as R12-SURSWP3 (its section and script). ~130 IIIF requests on service.archief.nl (>= 1.5 s apart). If any
scan shows glossed cipher, list it with its scan number and stop the sweep there for a solver. Update the Verdict and gaps_check.

## Wave 2 (spawned 13:3x UTC 6 Oct). Intake gate output (13:18 UTC) pasted per job.

### R13-WEB -- intercepted-royalist-1646 and malsburg-hessen-1636: check-solved "Open web and blog comment threads" step (Sonnet; cap 2, box 45 min)
Intake: `intercepted-royalist-1646: partial (line 4) has an edition citation but no logged open-web and blog-comment check ...`;
`malsburg-hessen-1636: found-solved (line 1) has an edition citation but no logged open-web and blog-comment check ...`.
Both targets' cheapest next steps (royalist: Evelyn pp.178-179 crib loop over f.10; malsburg: three clear-page direct reads) are deep work
the intake gate blocks. Run only the Required step "Open web and blog comment threads" of .claude/briefs/check-solved.md for each:
(a) four plain web searches, (b) site searches of Cipherbrain, Cryptiana blog/Tomokiyo pages, Cipher Mysteries, (c) open plausible hits
and read their comment threads. Log every query and hit under "## Web and blog check (R13-WEB, 6 Oct 2026)" at the end of each NOTES.md.
Do not change either status line unless a hit shows a published decipherment or plaintext of the item (then say so in ROOM as a flag, and
leave the status change to a verifier). Then re-run `tools/intake_gate_check.py` on both and paste the output in your done line.

### R13-CATOKLM -- catokwacopa-1875 (pollaky gap 3): phrase-level LM search on the unread lines with a matched synthetic control (Opus; cap 5, box 80 min)
Intake: `catokwacopa-1875: blocked (line 3) -- already terminal, nothing to gate` (the named step is internal; R12-CATOK23 retired the
unigram exact-fit instrument for the 5 unread lines). NOTES.md Verdict: "the line-23/unread-lines phrase-level LM search with a matched
synthetic control (QUEUE.md row 18), ~$5". Pre-register (PREREG committed first): the instrument (a word-bigram or char n-gram LM over
period English, era-matched if tools/data has one -- check `tools/data/en/README.md` on the `en` corpus's reliability and say which you use),
the candidate space, the gate, and a synthetic control: plant real period phrases of the same letter-word shapes under the same cipher
design and require the instrument to recover them at a stated rate before the target is scored. Control first; if CONTROL BELOW GATE,
stop and log "untestable by this instrument at this N". Report both numbers; HYPOTHESES.md row; update the pollaky-1865-1875 gap 3 line
to point at your section. Do not file LOCAL-QUEUE rows (name the bna-search row in NOTES for the orchestrator).

### R13-RAYCDX -- rayburn-2004: one Wayback CDX query for the earliest Schneier post capture (Sonnet; cap 1, box 25 min)
Intake: `rayburn-2004: open (line 1) -- edition/page or full-text-search citation found within 6 lines`
NOTES.md's retry row (R11-RAYWB, CDX reset twice): one CDX query for schneier.com/blog/archives/2006/01/handwritten_rea.html, one retry
after a pause at most; if a capture exists, fetch the earliest with the `if_` suffix and compare its image to the one on disk as the
NOTES step describes. Log the result; if the host blocks again, mark the step [retired-for-host] with the date and stop.
