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

## Wave 2 (spawned 15:3x UTC 6 Oct; lane about 19.5 of 60 at spawn). Intake gate output (15:32 UTC) pasted per job.
Wave 1 results: SUR746 non-test (no word gaps); RJMZ jum merged (verifier flag); ROYCRIB 19/216 below control; KAL11 control-backed
negative conv A; OLDF no sign settled, 4 C1 rows on shifted crops; LVN10C control FAIL with a named crop defect.

### R14-RJMV -- VERIFIER, rah-juan-manuel-1521: carry R14-RJMZ into AUDIT.md (Opus; cap 2, box 40 min)
Intake: `rah-juan-manuel-1521: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`
Verifier, separate from every solver. Claim under audit: NOTES.md "R14-RJMZ" (467f60383): L24.22 "Z um" -> jum (otra) at M via
lookalike/f34_exceptions.tsv; Jul/Jump J-groups not codes; 6 places yogh; f.34 S 300 / M 170 / U 272 of 742; judge FAIL above all 20
shuffles. Re-run decode9501_la.py --check, look at L24.22 on the crops (and one of the 6 yogh places), confirm counts, carry into
AUDIT.md and any SECOND-OPINIONS-QUEUE.tsv row. Correct only over-claims. Do not touch R9526 files (R14-RJM9526 runs there).

### R14-RJM9526 -- rah-juan-manuel-1521: R9526 retest with f.150's clerk lines and settled splits (Opus; cap 4, box 70 min)
Intake: `rah-juan-manuel-1521: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`
Remaining gaps, R9526 line: "one Sonnet read of f.150's last 6 lines and a look-alike pass on the 85 split tokens of
ciphertext_f147_reconciled.tsv, then a fresh PREREG (same gate) on the span, ~$3". Crop step pasted; PREREG committed first, same gate
as the calibration that came out a non-test (0.491) -- say first whether the calibration can now reach its gate and stop if it cannot
(CLAUDE.md rule 3 ARM-S3 lesson). The 2-of-3 residual is agreement, not error. Do not touch f.34 files or AUDIT.md.
Units: 1 read + 1 look-alike pass + 1 scoring.

### R14-SUR758 -- na-suriname-map-1781: inv. 373 scan 0758 glossed cipher, transcribe and align (Opus; cap 3.5, box 70 min)
Intake: `na-suriname-map-1781: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`
Same method as R13-SUR730 (reuse its PREREG shape and scripts): scan 0758, about 6 cipher lines with lighter plain lines above in a
plain letter (right page lower half). PREREG committed first, one blind Sonnet pass on the crops + reconciliation + scoring against
the pooled 0693+0702+0730 sign table vs a shuffled-gloss control; ask the readers to mark word gaps (R14-SUR746 lesson: without gaps
the word-level score is a non-test). Report both numbers; conflicts.tsv for rule-4 conflicts; list crib words. Units 3 x ~1.2.

### R14-SURDP -- na-suriname-map-1781: per-pair DP alignment of 0746 (Opus; cap 3, box 60 min)
Intake: `na-suriname-map-1781: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`
R14-SUR746's named next: its PREREG score was a non-test because the readers marked no word gaps. Pre-register (committed first) a
per-pair sign-to-letter DP alignment of each 0746 gloss+cipher pair (tools/interlinear_align.py if it fits; else a short script, and
say why), scored as per-sign agreement with the pooled 0693+0702+0730 sign table against a shuffled-gloss control that can vary
(shuffle gloss lines between pairs). Report both numbers; no transcription changes, no new vision passes. CPU only.

### R14-LVN10D -- lodewijk-van-nassau-1573-74: 4610 p3 per-token crops after the speck-filter repair (Opus; cap 5, box 80 min)
Intake: `lodewijk-van-nassau-1573-74: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`
R14-LVN10C named a crop defect (the speck filter drops detached leading digits) behind its control FAIL 0.726/0.722. Repair the filter
(if it lives in a shared tool, add the option and an offline test; else fix the folder's crop script), re-cut, eye 10 random control
crops for the missing digits BEFORE any read, then a PREREG addendum (layout change only, same gate >= 0.90, settle only when A == B)
committed first and the two blind reads in crop batches. This is the defect repair of this instrument's attempt 1: if the control FAILs
again with the crops eyed clean, log it, apply nothing, and mark per-token crops [retired] for 4610 p3 (rule 3). If PASS, apply via
lvn10/apply.py, decode --check, flag for a verifier. Units: 4 batch calls x ~1.5 + 1 scoring.

### R14-KAL12 -- kaliningrad-2015: pin the wordcode RNG, then convention B (Opus; cap 3, box 60 min)
Intake: `kaliningrad-2015: open (line 1) -- edition/page or full-text-search citation found within 6 lines`
(1) R14-KAL11 found `tools/family_run.py --family wordcode` controls not seed-reproducible: pin the restart RNG to `--seed`, add an
offline test in tools/tests/ that two runs with the same seed agree, keep defaults otherwise. (2) The NOTES next step: the same design
(marked types as whole-word codes) under transcription convention B, PREREG (HYPOTHESES.md row) first, control first at the target's
convention-B N and K, gate 0.6, target + shuffled-target beside it. Both numbers in HYPOTHESES.md. CPU only.

### R14-OLDF2 -- na-oldenbarnevelt-2442-1605: re-read the 4 C1 rows that sat on shifted crops (Opus; cap 2.5, box 45 min)
Intake: `na-oldenbarnevelt-2442-1605: open (line 1) -- edition/page or full-text-search citation found within 6 lines`
R14-OLDF section 18: four reader C1 rows (incl. C1_31, C1_05) were cut on the wrong crops. Re-cut those four on the right token
positions (paste the command, eye each crop against the line image first), one blind Sonnet call on the four crops, reconcile; change
a sign only where the image settles it, then re-judge per window under R13-OLDSEG's PREREG only if a sign changed. Units 1 + 1 (+1).

## Wave 3 (spawned 15:5x UTC 6 Oct; lane about 39.5 of 60 at spawn). Intake gates as wave 2 (unchanged lines, re-run 15:5x).
Wave 2: RJMV carried RJMZ; RJM9526 calibration PASS 0.679, both alphabets below 0.24 floor but rank 1/201; SUR758 transcribed (word score
non-test); SURDP 0746 0.920 vs p99 0.556 SAME SYSTEM; LVN10D control FAIL again, per-token crops retired for 4610 p3; OLDF2 two signs
changed (verifier flag). KAL12 still running.

### R14-OLDV -- VERIFIER, na-oldenbarnevelt-2442-1605: carry R14-OLDF2 into AUDIT.md (Opus; cap 2, box 40 min)
Verifier, separate from every solver. Claim under audit: NOTES.md section 19 "R14-OLDF2" (84f4031ed): C1_29 p8r8 -> p28r8 ("pere" ->
"puere"), C1_31 s2pl3c7 -> s2ppl3c7 ("suplico" -> "supplico") via overrides.tsv; S/M/I 245/18/23; re-judge windows 0-3 all FAIL. Re-run
apply_key --check, open the two crops (T1-T5) against the line image, confirm counts and the re-judge, carry into AUDIT.md and the
SECOND-OPINIONS-QUEUE.tsv row SO-OLDEN-2442-BC1 (and its PROMPT file if it quotes either word). Correct only over-claims.

### R14-SURDP2 -- na-suriname-map-1781: per-pair DP of 0758 and the unaligned 0702/0730 lines (Opus; cap 2, box 40 min)
The Verdict's cheapest next, with R14-SURDP's script and PREREG shape (reuse, do not rewrite): a short PREREG addendum committed first
naming the lines, then the same per-pair DP vs the pooled sign table (now including 0746 if R14-SURDP pooled it; say which) against the
shuffled-gloss-line control. Report both numbers per scan. CPU only; no vision, no key edits.

### R14-SUR2039 -- na-suriname-map-1781: "Smeedery" and fortress-work glosses as cribs on 2039's legend (Opus; cap 2.5, box 50 min)
R13-SUR730 listed crib words for 4.VEL 2039's a-u "Verklaringe der Letteren": Smeedery, Affuyten/Affuyt, beslag, geschut, Fortres N.A.;
R14-SUR746/758 may have listed more (Fortificatie werken, Linie, Verstopping, boom). Using ciphertext_2039_legend.tsv and the current key
(reading_2039_legend*), pre-register (committed first) the crib list, the placement rule (legend entries whose unread/M positions have
the crib's length and are consistent with keyed letters), and a control that can vary (the same cribs placed on 2039's legend shuffled
within entries, or random Dutch words of the same lengths from the 0693-0758 glosses). Report hits beside the control; any placement
that survives is graded S at most (rule 4), entered in no key file; NOTES section + HYPOTHESES.md row. Do not edit key.tsv.

### R14-RJMTQ -- rah-juan-manuel-1521: T/Q values from pooled alignments (Opus; cap 2.5, box 50 min)
Remaining gaps: "pool the f.194, f.199, f.40 and f.147 alignments for T/Q chunk counts and score Q against K after the look-alike check,
~$2". PREREG committed first (the counts that would settle T or Q, and a shuffled-alignment control that can vary). No grade change
without the gate; any value is S at most. CPU only. Do not touch f.34 or AUDIT.md.

### R14-LVNEYE -- lodewijk-van-nassau-1573-74: eye check of the 10 control rows the 4610 p3 readers agreed against (Opus; cap 2, box 40 min)
R14-LVN10D's named next: the per-token control FAILed twice with clean crops; look at the 10 control rows where both blind readers
agreed against the control sign, on the 300-dpi crops, and say whether the control sign itself looks wrong (that would point at the
control, not the readers). List them in NOTES.md; change nothing in the key or reading; the [retired] mark stays unless the control is
shown wrong on >= 5 of 10 (then say so for the orchestrator; do not re-run).
