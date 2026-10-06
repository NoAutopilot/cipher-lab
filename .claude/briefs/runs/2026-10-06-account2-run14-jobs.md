# LANE LANE-RUN14-account-2 jobs (account 2) -- 6 Oct 2026 15:2x UTC, lane orchestrator session_01R1TEeQiCq7JbrL8FURHPGn

Lane brief: .claude/briefs/default-lane.md (cap 60, box 15:10 UTC 6 Oct - 01:10 UTC 7 Oct). WORK-QUEUE row LANE-RUN14-account-2: RUN13's
named next steps for this split (STATUS.md "LANE LANE-RUN13-account-2 handoff", "Open for the next i-r lane"), then tools/next_steps.py
runnable rows (S, M) and `parallel` actions (plain next_steps, not --hot-only). Folders i-r (account 1 a-h, account 4 s-z). The row's
verifier-propagation flags (august-van-saksen a-h, manteuffel s-z) are other splits; lodewijk's AUDIT.md is current (R13-LVNV2).
malsburg-hessen-1636 is `found-solved` (line 1): its key_crossmatch is left for the owner-account orchestrator, not taken here.
Off limits: Birago (incl. nevers-birago-fr3251-1572), Armstrong, Debosnys; riksarkivet-r4282-1628.
Gate 0a: SESSION-SWEEP-account-2 row still `claimed` (since 5 Oct 23:10, > 90 min), its TSV on disk; RUN7-RUN13 proceeded the same way.
No live claim (< 6 h, no done) on any wave-1 folder in the last 600 ROOM lines; no overlap with the account-1 RUN11 or account-4 job files.
Every worker: Opus 5.5 (Sonnet 5.5 only where stated), one job, then stop. Each job first checks that its named step is still undone
(a dated NOTES.md section may already have run it); if so, stop and report rather than inventing work.

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim
  line with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE LANE-RUN14-account-2".
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
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE LANE-RUN14-account-2",
  then a five-line final report.

## Wave 1 (spawned 15:1x UTC 6 Oct). Intake gate output (15:1x UTC) pasted per job.

### R14-SUR746 -- na-suriname-map-1781: inv. 373 scan 0746 glossed cipher, transcribe and align (Opus; cap 5.5, box 90 min)
Intake: `na-suriname-map-1781: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`
Same method as R13-SUR702 and R13-SUR730 (their NOTES sections, PREREGs and scripts; reuse them, do not rewrite): scan 0746 is two pages
(left about 19 gloss+cipher pairs with a few plain lines, right about 6 pairs, "Actum aan boord van 's Lands Fregat van oorlog de Valk ...
24 October 1781", two signatures). Fetch 0746 once at ~2000 px from service.archief.nl, crop one gloss+cipher pair per crop with
tools/iiif_lines.py (paste the command), PREREG committed first, one blind Sonnet pass per page on the crops (no values given) + your
reconciliation with the gloss in view, then align sign-for-letter and score against the pooled 0693+0702+0730 sign table vs a
shuffled-gloss control that can vary. Report both numbers; conflicts.tsv rows for rule-4 conflicts (the y-family m|n question); list any
gloss word naming a map sheet, legend letter or fortress work (crib candidates for 2039 -- list, do not test). Do not touch 0758.
Units: 2 passes + 1 reconciliation + 1 scoring at ~1.2.

### R14-RJMZ -- rah-juan-manuel-1521: eye check of the 9 remaining Z + group places on f.34 (Opus; cap 2.5, box 50 min)
Intake: `rah-juan-manuel-1521: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`
NOTES.md Remaining gaps (R13-RJMV2), first gap: L24 "Z um" (possibly jum = otra, a table code), L04 "Jul", L23 "Jump", L03/L29 "Z bay",
L07 "Z suf", L26 "Z log"/"Z bo", L29 "Z geb". Look at each on the f.34 crops already on disk (no refetch unless the crops lack the place;
then one DECODE login at most, per R13-RJMV2's route). For any place where the image shows one J-initial group that is a table code, add a
row to lookalike/f34_exceptions.tsv (M grade, R12-RJMV's licence) and run decode9501_la.py --check (exit 0). Re-run the two judge calls and
the 20-seed shuffled control only if a token changed. Flag the reading change for a verifier. Do not touch R9526 files.

### R14-ROYCRIB -- intercepted-royalist-1646: crib loop of the unglossed Evelyn figures over f.10 (Opus; cap 3, box 60 min)
Intake: `intercepted-royalist-1646: partial (line 4) -- edition/page or full-text-search citation found within 6 lines`
Escalation Verdict: "the unglossed figures beside glossed ones on Evelyn pp.178-179 (216, 418, 19, 147) as a crib loop over f.10, ~$2".
PREREG committed first: for each unglossed figure, the candidate meanings allowed (from the glossed neighbours' key structure and the
letter's context), the scoring (consistency of the candidate with f.10's key129 rendering and the surrounding decoded words), and a
control that can vary (the same loop with the figures' positions shuffled, or random figures from the same range). Report each figure's
best candidate beside the control; grade any value C only if the print itself fixes it, else S with the control or M. HYPOTHESES.md row.
Do not post-hoc widen the candidate list after scoring.

### R14-KAL11 -- kaliningrad-2015: wordcode family at restarts 6, seeds 1-5 (Opus; cap 2.5, box 50 min)
Intake: `kaliningrad-2015: open (line 1) -- edition/page or full-text-search citation found within 6 lines`
NOTES.md R13-KAL10 named step: re-run `tools/family_run.py --family wordcode` (with the `--param bnd=` R13-KAL10 used) at restarts 6, seeds
1-5, gate 0.6 unchanged, PREREG (HYPOTHESES.md row) committed first, the matched control first; if the control mean meets the gate, run the
target and the shuffled-target decode beside it. Both numbers in HYPOTHESES.md. This is attempt 2 of this instrument on this hypothesis
(restart count is the one knob): if the control is below gate again, log "untested-by-this-tool at this N" and say in NOTES.md that a third
attempt needs a different instrument (rule 3). ~5 min CPU per run; CPU only, no hosts.

### R14-OLDF -- na-oldenbarnevelt-2442-1605: crop re-look at the 14 M/I-graded B/C1 tokens (Opus; cap 3.5, box 60 min)
Intake: `na-oldenbarnevelt-2442-1605: open (line 1) -- edition/page or full-text-search citation found within 6 lines`
Section 17 Verdict step (f): crops of the 14 M/I-graded B/C1 tokens (windows 0 and 3 first: B28-B37, C1 21-44), cut from the on-disk
images with tools/iiif_lines.py or a per-token crop (paste the command), one blind Sonnet pass on those crops only (values not given),
then your reconciliation. Change a sign only where the image settles it; then re-judge per window under R13-OLDSEG's PREREG cut (same
judge, same controls) and report each window beside its real_p05 and null. If no sign changes, do not re-judge (section 17 says so).
Units: 1 pass + 1 reconciliation + 1 scoring.

### R14-LVN10C -- lodewijk-van-nassau-1573-74: stale key.tsv reading regen, then 4610 p3 per-token crops, two blind reads (Opus; cap 7, box 90 min)
Intake: `lodewijk-van-nassau-1573-74: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`
(1) NOTES.md (R13-LVNFIX/R13-LVNV2): decode.json's key.tsv reading (reading_4616.txt / reading_4616_tokens.tsv) failed --check before
R13; regenerate it with tools/decode_key.py (decode.json) and confirm --check exit 0 on it and on decode_4616_full.json; say whether
any figure in AUDIT.md depends on that reading (it should not; the full config is the audited one). (2) The different instrument named
for 4610 p3 after R13-LVN10B retired whole-line blind passes (rule 3): per-token crops cut at each M row's position on the 300-dpi p3
render (sha1 a41b5df838e49cefb71e30cdfbe0803f3947d591; re-fetch the WVO PDF once only if not on disk), two blind Sonnet reads in crop
batches, against a fresh PREREG with the SAME gate (lvn10/PREREG.md control rows, >= 0.90 per pass; settle only when A == B), committed
first. If PASS, apply via lvn10/apply.py, decode --check, flag the reading change for a verifier; if FAIL, apply nothing and log it.
Units: 4 batch calls x ~1.5 + 1 scoring; stop before a unit that crosses 80% of the cap.
