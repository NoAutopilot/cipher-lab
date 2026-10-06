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

## Wave 2b (spawned 17:3x UTC from wave-1 results). Intake gate output (17:3x UTC) pasted per job.

### R15-LVNAPP -- lodewijk-van-nassau-1573-74: apply the 10 verifier-checked 4610 p3 control corrections (Opus; cap 2, box 40 min)
Intake: `lodewijk-van-nassau-1573-74: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`
NOTES.md "## R15-LVNCTL": lvn10/control_corrected.tsv lists 10 control values wrong on the 300-dpi image (R14-LVNEYE and R15-LVNCTL agree;
8 S / 2 M per R15-LVNCTL). Apply exactly those rows to ciphertext_4610.tsv through the folder's existing correction route (a corrections TSV +
apply script as lvn16/apply.py did, not hand edits), grades as R15-LVNCTL gives them; decode_key.py --check (or the folder's decode) exit 0 with
the regenerated reading; report token-count changes per grade. Nothing else: no re-score as a licence, [retired] marks stay. Flag in ROOM for a
verifier to carry the applied state into AUDIT.md (do not edit AUDIT.md's class). Update gap 3 / image-check text and pass gaps_check.

### R15-CLIN3537 -- pro3055-clinton-1779: 3537 key check from the VHS II printed cipher specimen (Opus; cap 2, box 40 min)
Intake: `pro3055-clinton-1779: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`
NOTES.md Remaining gaps (R15-CLINGAP): fetch the archive.org djvu text of collectionsofver02vermuoft once, parse the printed figure pairs of
pp.338-341, apply the 1778 key (passes/key_2894.tsv, check_2894_key.py logic; reuse, do not rewrite) against the printed translation pp.341-342,
with a shuffled-plaintext control (PREREG first, the match rule fixed before scoring). OCR of figures is fragile: if the djvu figures are not
parseable, look at the page images for those pages only (crop, one call per page) or stop and say so. Script only otherwise. Report both
numbers, any key entries the print adds or contradicts (grade C from the print), request counts. gaps_check passes.

### R15-LAGMI -- la-garde-1577: pre-registered Z_MI test, homophonic vs running key (Opus; cap 2, box 40 min)
Intake: `la-garde-1577: open (line 1) -- edition/page or full-text-search citation found within 6 lines`
NOTES.md R15-LAGDIG "Next cheapest step": a fresh PREREG with Z_MI as the primary statistic and NEW control seeds (none of R15-LAGDIG's), the
same designs and error bracket (0, 10, 23, 30%), power gate fixed in advance (AUC >= 0.80 vs both running-key variants at e=0.23 on the new
seeds). This is a second statistic, not a re-tune of the first: if power fails on the new seeds, log "untestable by this statistic" and stop;
only if it passes, score the target and report where it falls against both control distributions. Reuse families/ scripts. CPU only.

## Wave 3 (spawned 17:5x UTC from wave-2 results and flags). Intake gate output (17:5x UTC) pasted per job.

### R15-LVNV -- lodewijk-van-nassau-1573-74: verifier carry-over of R15-LVNAPP into AUDIT.md (Opus, verifier hat; cap 2, box 40 min)
Intake: `lodewijk-van-nassau-1573-74: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`
ROOM flag R15-LVNAPP 17:39: 10 4610 p3 control corrections applied (2e47b56ca; lvn10/corrections_lvnctl.tsv), 4610 C/H 1204->1202, M 131->133,
I 55->54, U 155->156. You are not R15-LVNAPP or R15-LVNCTL. Run decode_key --check (exit 0), confirm each applied row matches control_corrected.tsv
and its grade, spot-check 3 rows on the 300-dpi crops (lvn10/eyecrops.py), recompute the four-letter H/C/S share and depth figure, then write
an AUDIT.md "Carry-over (R15-LVNV)" section with the applied state, and carry it into status.json depth fields and any SECOND-OPINIONS-QUEUE.tsv
row for this target (CLAUDE.md rule 10 propagation). Class unchanged unless the evidence moves it (say why either way).

### R15-OLDV2 -- na-oldenbarnevelt-2442-1605: verifier carry-over of R15-OLDUV into AUDIT.md and SO-OLDEN-2442-BC1 (Opus, verifier hat; cap 2, box 40 min)
Intake: `na-oldenbarnevelt-2442-1605: open (line 1) -- edition/page or full-text-search citation found within 6 lines`
ROOM flag R15-OLDUV 17:42: B37 bvenas->buenas, B49/B76 atreven->atreuen, B55 veras->ueras via overrides.tsv (NOTES s.20, ec902d21b); judge
re-run with u/v fold on target and controls (PREREG abaf33532), windows -0.933/-0.880/-0.893/-0.968, still FAIL. You are not R15-OLDUV or R14-OLDV.
Check --check OK, the four renamings against crops, that the PREREG predates the run (git log order) and that the fold was applied to every
control as well as the target (rule 3 normalisation), re-run one judge window to confirm reproducibility. Carry into AUDIT.md (carry-over
section) and the queued SO-OLDEN-2442-BC1 prompt in SECOND-OPINIONS-QUEUE.tsv. Note w1 is 0.004 short of real_p05: say plainly whether that is
"judge cannot decide" or a FAIL under the repo's rule-3 language, without moving the gate.

### R15-SURALIAS -- na-suriname-map-1781: pre-registered reader-code alias pass, re-scored with R14-SURDP's DP (Opus; cap 2.5, box 50 min)
Intake: `na-suriname-map-1781: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`
NOTES.md Remaining gaps Verdict [R15-SURV]: PREREG first: 0702 'K' = the period sheet's k, 0758 's' = [sh-lig], 0758 'i j' = one [ij] sign (each
image-checked by R15-SURV), 0730 [other: ss-like]/[other: f-like] image-checked first (one service.archief.nl fetch, crop, paste the command);
then re-score with R14-SURDP's DP script and its shuffled-gloss control, report both numbers per scan before/after. Aliases go into the pass
transcription files through the existing scripts, not into key.tsv; key.tsv changes only if the PREREG says so and the gate passes, with --check
exit 0 and a ROOM flag for a verifier. Do not start the 2039 legend k re-read (separate job).

### R15-KAL14 -- kaliningrad-2015: columnar transposition of a Russian-transliteration substitution, matched control first (Opus; cap 2.5, box 50 min)
Intake: `kaliningrad-2015: open (line 1) -- edition/page or full-text-search citation found within 6 lines`
NOTES.md R15-KAL13 next step: a different instrument from wordcode -- columnar transposition (widths per PREREG, e.g. 2-12) applied to a
Russian-transliteration simple substitution (tools/data/ru19_lat; check its era/register note in tools/data README), scored by bigram/judge.
PREREG first: widths, key search budget, scoring, gate. Matched control: synthetic ru19_lat text, same N and K as convention B (N 1066, K 28,
or the convention the PREREG names), enciphered with the same design, solved by the same search at the same budget; target only if the
control meets the gate (family_run.py pattern; add a family module with an offline test if family_run cannot express it, no private copy).
Shuffled-target run beside the target. HYPOTHESES.md rows; CPU only. If the control cannot read at this budget, log "untestable by this
instrument at this N" and stop.

## Wave 4 (spawned 18:1x UTC from wave-3 results). Intake gate output (18:1x UTC) pasted per job.

### R15-LAGHOM -- la-garde-1577: homophonic solve through family_run.py at noise 0.23, matched control first (Opus; cap 2.5, box 50 min)
Intake: `la-garde-1577: open (line 1) -- edition/page or full-text-search citation found within 6 lines`
R15-LAGMI (Z_MI, power PASS on fresh seeds) favours homophonic over running key as a design preference (0 tokens read). Next named step:
`tools/family_run.py` --family homophonic on the base codes (N=229, K=26, fr16 corpus; profile=target as the HYPOTHESES rows used), with the
control's injected error bracketing the target's measured ~23% (rule 3: run the control at 0.23 at least; add 0.10 for the curve), gate and
seeds pre-registered (PREREG committed first), control first, target only if the control mean meets the gate, shuffled-target run beside it.
If the control is below gate: CONTROL BELOW GATE, "untestable by this family at this N/error", stop. Judge any target decode with
tools/judge_plaintext.py on the spec (and score the shuffled decode through the same judge: CLAUDE.md rule 3, ARM-C1). HYPOTHESES.md rows.
CPU only. No reading is claimed from a statistic.

### R15-SUR758 -- na-suriname-map-1781: per-token image check of 0758 's' and 'i j' (Opus; cap 2, box 40 min)
Intake: `na-suriname-map-1781: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`
R15-SURALIAS: 0758 blanket s=[sh-lig] FAILed tolerance (6/9; scan A 0.947 -> 0.936); 0758 K (1) and 'i j' (4) were non-tests. Next named step:
per-token image check of the 0758 s tokens (9) and 'i j' tokens (4) on the native crops already on disk (crop per token with neighbours, paste
the command; one blind look per token batch, your own eye or one subagent call on crop paths only), each labelled s / [sh-lig] / other and
'i j' as one sign / two. PREREG first (labels, the re-score rule: only per-token labels from the image, then R14-SURDP's DP with its
shuffled-gloss control). Report before/after per scan. Pass-file changes via the existing scripts; key.tsv only if PREREG + gate allow, with
--check and a ROOM verifier flag. Do not start the 2039 legend k re-read.

### R15-CLIN3853 -- pro3055-clinton-1779: 3853 f.406 cipher against the printed f.381 extract on the 1778 key (Opus; cap 5, box 70 min)
Intake: `pro3055-clinton-1779: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`
NOTES.md Remaining gaps line "3853 cipher, f.406" (R15-CLINGAP): fetch the frame by the image-uab.canadiana.ca route recorded in
images/h1649/manifest.json (about Image 1056; confirm the page label before cutting; one image per request, >= 1.5 s apart), cut column crops
with the folder's passes/cut_cipher_cols.py or tools/iiif_lines.py --image (paste the command), PREREG the key-consistency gate first (as
R10-CLIN3868/R11-CLIN2380 did: cells matching the printed f.381 text on the 1778 key vs shuffled-plaintext p95). Units (Usage 6): 2 blind
passes per page + 1 reconciliation at ~1.5 each; stop before starting a unit that would cross 80% of cap or box. Report where f.406 carries text
beyond the f.381 extract (grade H only from a period decipherment, else S with the gate), --check if a reading file is written, flag a verifier
in ROOM if any text is added. Reuse check_3868.py / the 2380 scripts; do not rewrite them.

## Wave 5 (spawned 18:4x UTC; last wave, lane closes when both report). Intake gate output (18:4x UTC) pasted per job.

### R15-CLIN407 -- pro3055-clinton-1779: 3853 cipher continued on p.407 (Image 1058) against the printed f.381 text (Opus; cap 4.5, box 60 min)
Intake: `pro3055-clinton-1779: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`
R15-CLIN3853 (e66b18fd2): p.406 matches the printed f.381 text 191/197 under PREREG 9cca7e5a5 and stops at "about Vermont"; the cipher continues on
p.407 (Image 1058). Same method and scripts as R15-CLIN3853 (reuse its PREREG gate shape; write a short PREREG addendum for p.407 before scoring):
fetch Image 1058 once, confirm label, cut column crops (paste the command), 2 blind passes + 1 reconciliation at ~1.5 each, stop before a unit
that would cross 80% of cap or box. Report whether p.407 carries text beyond the f.381 print; any added text is graded S with the gate (H only
with a period decipherment) and flagged in ROOM for a verifier; --check if a reading file is written. Keep the "25 vs 28 sail" witness conflict
logged, not resolved.

### R15-SURV2 -- na-suriname-map-1781: verifier on R15-SUR758's [sh-lig] class (Opus, verifier hat; cap 2, box 40 min)
Intake: `na-suriname-map-1781: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`
ROOM flag R15-SUR758 18:22: 0758 image-labelled [sh-lig] PASS 5/6 0.833 vs C1 p99 0.667 (PREREG f53d915f1; passes/inv373_0758_tok_r15/). You are
not R15-SUR758, R15-SURALIAS or R15-SURV. Re-run its re-score (must reproduce), check the PREREG predates the run (git order), eye 3 of the 6
SH tokens and the OTHER token on the crops, and decide whether a [sh-lig] key entry is licensed (pooled with R15-SURALIAS's 0730 ss-like 7/7)
and at what grade. If licensed, make the key entry through the folder's key/exceptions route with decode --check exit 0, carry it into
AUDIT.md (carry-over) and any SO row for this target; if not, say why in AUDIT.md. Class unchanged unless the evidence moves it.

## Wave 6 (19:0x UTC; one verifier for the R15-CLIN407 flag, then the lane closes)

### R15-CLINV -- pro3055-clinton-1779: verifier on R15-CLIN3853 + R15-CLIN407 (Opus, verifier hat; cap 2, box 40 min)
Intake: `pro3055-clinton-1779: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`
ROOM flag R15-CLIN407 18:51: 3853 p.407 cipher reads "all your trouble and pains" where the 1920 print of f.381 has "all your Trouble", and gloss
"give up" vs print "give"; graded S under gate PASS 189/197 (PREREG 6f7ae4ab6, f2a8ff92d); p.406 PASS 191/197 (R15-CLIN3853, e66b18fd2; "25 vs 28
sail" witness conflict). You are neither worker. Re-run both scripts with --check / reproduce the scores, confirm each PREREG predates its run
(git order), eye the cells carrying "and pains", "up" and "25" on the column crops, and decide each grade (S with the gate, M, or rejected).
Rule 4: these are witness differences between the cipher and a printed decipherment, logged as conflicts, not resolved by preference. Write
an AUDIT.md carry-over (class unchanged unless the evidence moves it; if the added words are kept, rule 10 propagation into any SO row for
this target) and correct any over-claiming sentence in NOTES.md.
