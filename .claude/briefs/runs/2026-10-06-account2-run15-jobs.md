# LANE LANE-RUN15-account-2 jobs (account 2) -- 6 Oct 2026 17:1x UTC, lane orchestrator session_01QoYotT3fsUf7tNko8gh8E4

Lane brief: .claude/briefs/default-lane.md (cap 60, box 17:12 UTC 6 Oct - 03:12 UTC 7 Oct). WORK-QUEUE row LANE-RUN15-account-2: verifier
propagation flags first (both already done: R14-OLDV 15:56 oldenbarnevelt, R11A-AVSV2 16:05 august-van-saksen), then NEXT-STEPS runnable rows,
split i-r. Jobs come from RUN14's "Open for the next i-r lane" (STATUS.md) and the --hot-only runnable i-r rows (jan-van-nassau, la-garde,
lodewijk, nevers-birago, pro3055-clinton, rah-salazar); most other runnable i-r rows were stale and are corrected by the orchestrator in
NOTES.md, not briefed. Off limits: Birago (incl. nevers-birago-fr3251-1572), Armstrong, Debosnys; riksarkivet-r4282-1628; malsburg
key_crossmatch (owner-account orchestrator's call). Gate 0a: SESSION-SWEEP-account-2 still `claimed` since 5 Oct 23:10, proceeding as RUN7-RUN14.
Gallica probe 17:1x UTC: IIIF manifest bpt6k115863g HTTP 200.
Every worker: Opus 5.5, one job, then stop. Each job first checks that its named step is still undone (a dated NOTES.md section may already
have run it); if so, correct the NOTES.md next-step line, stop and report rather than inventing work.

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim
  line with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE LANE-RUN15-account-2".
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
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE LANE-RUN15-account-2",
  then a five-line final report.

## Wave 1 (spawned 17:2x UTC 6 Oct). Intake gate output (17:1x UTC) pasted per job.

### R15-LVNCTL -- lodewijk-van-nassau-1573-74: verifier re-check of the 7 suspect 4610 p3 control rows (Opus, verifier hat; cap 2.5, box 50 min)
Intake: `lodewijk-van-nassau-1573-74: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`
You are a verifier, not R14-LVNEYE. NOTES.md "## R14-LVNEYE" says the 150-dpi control sign looks wrong on 7 of 10 rows (01 02 05 06 07 08 09)
of lvn10/aligned_d.tsv that both round-d readers agreed against. Regenerate the crops with `python3 ciphers/lodewijk-van-nassau-1573-74/lvn10/eyecrops.py`
(paste the command; WVO PDF once if not on disk). Read each of the 10 rows yourself at 300 dpi BEFORE opening R14-LVNEYE's image column (record your
read first, then compare), against same-page digit forms. Then, beyond the 10: list every other control row of aligned_d.tsv that either reader
missed, and eye-check as many as fit in the box (record count checked). Write lvn10/control_recheck.tsv (row, control, your image read, agree
with LVNEYE y/n, verdict). If >= 5 control values are wrong on the image, build lvn10/control_corrected.tsv (corrected values, each graded from
the image) and re-score round d A7/B7 against it arithmetically, reported beside the old score -- that is a re-score of an existing run for the
record, not a licence: nothing goes into key.tsv/ciphertext_4610.tsv, and the [retired] marks stay. Write the result into NOTES.md gap 3 /
Escalation image-check and AUDIT.md (a carry-over note), naming what a different instrument would need (the corrected control). gaps_check passes.

### R15-SURV -- na-suriname-map-1781: verifier on R14-SURDP2's candidates + blind look at 2039 legend entry k (Opus, verifier hat; cap 2.5, box 50 min)
Intake: `na-suriname-map-1781: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`
You are a verifier, not the solver. (a) NOTES.md "## R14-SURDP2" (per-pair DP, SAME SYSTEM on 0746/0758/0730/0702) names descriptive candidates
(about 4). Re-run its script --check / regenerate its numbers (must match), then for each candidate check on the crops on disk whether the image
supports it and whether it was pre-registered or post hoc; grade each (S at most, M, or rejected). (b) Blind look at the 2039 legend entry k
(R14-SUR2039: "sd.edbrtyen", candidate "smeederyen"): read positions 1, 2, 5, 7 from the crop yourself before reading R14-SUR2039's reading;
report whether the image allows s-m-e-e-d-e-r-y-e-n and which positions it contradicts. Nothing enters a key from this job. Write the verdicts
into AUDIT.md (carry-over section) and NOTES.md; refresh the "Verdict:" line of Remaining gaps/Escalation, whose "cheapest next" (per-pair DP)
is already done (R14-SURDP/SURDP2), with the actual next step; gaps_check passes.

### R15-KAL13 -- kaliningrad-2015: wordcode with codes on unmarked types (codes=topk:N), matched control first (Opus; cap 2.5, box 50 min)
Intake: `kaliningrad-2015: open (line 1) -- edition/page or full-text-search citation found within 6 lines`
NOTES.md "R14-KAL12" next step: marked-types-as-codes wordcode is spent at both conventions; untried: codes on unmarked types (`codes=topk:N`)
or a transposition design beyond A2-KAL2's unigram test. Run the codes=topk:N variant through tools/family_run.py (check the wordcode family
supports it; if it needs an option, add it with an offline test in tools/tests/test_wordcode.py rather than a private copy). PREREG committed
first (N choice(s) fixed before any run, at most two: e.g. topk:20 and topk:40; gate 0.6; err 0.05 band as R14-KAL12; conventions per HYPOTHESES.md),
control first, target only if control meets gate, shuffled-target run beside it (control built from the unshuffled target). Give decodes a
distinct filename (R14-KAL12 noted family_run.py's decode name omits the cipher file: pass a distinct out name or add the --cipher basename,
with a test). HYPOTHESES.md rows, NOTES.md section, next step named. CPU only, no hosts.

### R15-LAGDIG -- la-garde-1577: contact/digram test homophonic vs running key, power on the control first (Opus; cap 2.5, box 50 min)
Intake: `la-garde-1577: open (line 1) -- edition/page or full-text-search citation found within 6 lines`
NOTES.md GAPS149 "Next cheapest step": at N=229 and ~23% transcription error, a contact/digram statistic (homophonic spreads a letter's bigram
partners across signs; running key gives near-independent bigrams) with matched controls, ~$1, power unknown. PREREG first: the statistic(s),
both synthetic designs (homophonic with the target's K and sign-frequency profile; running key with a period-plausible French/Dutch text) at
N=229 and the target's measured error band (bracket it, rule 3: 0, 10, 23, 30%), seeds >= 20 each, the decision rule. Step 1 power: do the two
synthetic designs separate at N=229 at the target's error? If not (overlap beyond the prereg threshold), stop: log "untestable by this
statistic at this N/error" in HYPOTHESES.md and NOTES.md, do not score the target. Step 2 only if power passes: score the target, report
where it falls against both control distributions. Script in the folder's families/; CPU only.

### R15-KONS3 -- konstanz-talleyrand-sieyes-1798: Guyot 1911 footnotes, PAG_723-729, for a 26-29 messidor an VI Sieyes item (Opus; cap 2, box 45 min)
Intake: `konstanz-talleyrand-sieyes-1798: open (line 3) -- edition/page or full-text-search citation found within 6 lines`
NOTES.md "## Guyot 1911 full-text search (R9-KONS2)" next: read the footnotes of Gallica ark bpt6k115863g views PAG_723-729 (printed pp. ~716-722)
in full for any Sieyes letter of 26-29 messidor an VI (14-17 Jul 1798) or a date in another form ("28 messidor", "le 17"). ALTO answered 429 on
6 Oct; use the IIIF image API instead (one view at a time, >= 2 s apart; crop the footnote block with tools/iiif_lines.py --ark/--canvas, paste the
command; read the crops yourself or with one subagent call per page). Map PAG_n to canvas with tools/gallica_folio.py first. Stop Gallica on any
429/5xx (one retry after a pause). Record what the footnotes cite (AE Prusse 223 piece numbers and dates), whether any matches 17 Jul 1798, and
where it was not found. Status stays open; update the next-step line (if nothing: the Konstanz image via REQUEST.md is the remaining route).

### R15-CLINGAP -- pro3055-clinton-1779: refresh Remaining gaps / Escalation after RUN10-RUN12, name the cheapest runnable step (Opus; cap 2, box 45 min)
Intake: `pro3055-clinton-1779: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`
The "## Remaining gaps (1 Oct 2026)" and "## Escalation" Verdict predate R10-CLIN3868/3868B, R11-CLIN2380/B/C, R11-CLINV3-5 and R12-CLINVHS (3868
and 2380 cell-by-cell checks done). Rewrite each gap's current state from the dated sections (no new reading), so the Verdict names the actual
cheapest runnable step (candidates in the file: 3853 f.381 decoded extract, 4833's 22 June 1782 enclosure, the 26 Oct 1782 note, the six further
Kew copies 2962/3050/3502/3537/4152/4216). Then, if the box allows and that step is a single cheap read on images already on disk or one LAC
reel image route already recorded in the file (<= 1 unit), run it with the folder's existing scripts; otherwise stop at the refreshed Verdict.
gaps_check passes; rule 7 --check exit 0 if any reading file changed.

## Wave 2 (spawned as wave-1 slots free, 17:3x UTC onward). Intake gate output (17:2x UTC) pasted per job.

### R15-OLDUV -- na-oldenbarnevelt-2442-1605: the (n) u/v notation pass (Opus; cap 2.5, box 50 min)
Intake: `na-oldenbarnevelt-2442-1605: open (line 1) -- edition/page or full-text-search citation found within 6 lines`
NOTES.md section 19 Verdict and "## While waiting": "(n) a u/v notation pass: one naming for the shared u/v shape across B/C1, applied to the
reading and the judge input, before any further judge run (~$1.5)". (a'') waits on the owner's sorter: do not touch A/C2 sorter files.
PREREG first: the single naming rule (which letter the shared shape is written as in the reading, how the judge input normalises u/v, both
fixed before any score), and the control the re-judge uses (the same normalisation applied to the real-prose and shuffled-decode controls --
CLAUDE.md rule 3 "normalize both to one convention"). Apply via the folder's existing decode/reading scripts (exceptions or a normalisation
option, not hand edits); rule-7 --check exit 0; re-judge the four windows with the same corpus and controls as R14-OLDF2; report each window
beside its previous score. Flag the reading change in ROOM for a verifier (do not edit AUDIT.md's classification yourself; a carry-over note
naming the change is fine). Update the section Verdict / While waiting so (n) reads as done.

### R15-MREVL -- maurice-rupert-1645: Evelyn's Memoirs pp.102-113 King-to-Nicholas letters, printed cipher numbers beside decipherments (Opus; cap 2.5, box 50 min)
Intake: `maurice-rupert-1645: open (line 1) -- edition/page or full-text-search citation found within 6 lines`
NOTES.md "## While waiting" (GAPS52, 3 Oct 2026): the 9119 key form cites "Evelyn's Memoirs", pp.102-113 (Charles I to Nicholas, Oct 1645).
Identify the edition the form means (Bray's Memoirs of John Evelyn, the correspondence appendix, which edition/volume has those pages),
locate it on Internet Archive (advancedsearch + `_djvu.txt`, no login), grep pp.102-113 for cipher numbers printed beside their meanings,
and write each printed pair to keys/evelyn_pairs.tsv (number, meaning, page, edition, grade C from the print). Compare with key9119.tsv
(agree / conflict / extends). Re-run keys/key_test.py only if coverage rises well above 35/93 as the line says; otherwise report the
coverage and stop. Request counts per host. Report what was found and where it was not found.
