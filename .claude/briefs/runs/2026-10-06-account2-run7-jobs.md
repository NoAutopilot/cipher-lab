# LANE LANE-RUN7-account-2 jobs (account 2) -- 6 Oct 2026 01:2x UTC, lane orchestrator session_01UK47b2jBbLpTagGB97jJgP

Lane brief: .claude/briefs/default-lane.md (cap 60, box 01:13-11:13 UTC 6 Oct). WORK-QUEUE row 236: the 5 Oct lanes spent the cheap
backlog; this lane takes the next tier -- tools/next_steps.py runnable rows with cost band M as well as S, ranked by closeness to a
counted result, then depth pushes toward D2 on uncounted N3+ readings. Folders m-z (account 1 takes a-l). VERIFY-BACKLOG.tsv high rows
(01:12 UTC) are fr16142 only (a-l). Off limits: Birago (incl. nevers-birago-fr3251-1572), Armstrong, Debosnys. Every worker: Opus 5.5,
one job, then stop. Each solver job first checks that its named step is still undone (NEXT-STEPS.tsv lags the folders): if a dated
NOTES.md section already ran it, take the folder's own Verdict "cheapest next" instead if it fits this job's cap and box and is not a
machine transcription pass the TRANSCRIPTION.md / CLAUDE.md Usage 6 sorter rule hands to the owner; otherwise stop and report.

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim
  line with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE LANE-RUN7-account-2".
  If --start fails to push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
- Read the folder's NOTES.md tail (Remaining gaps / Escalation / latest dated sections), HYPOTHESES.md and AUDIT.md section list first.
- Good-citizen rule and the CLAUDE.md host table for every request (one request per host at a time, >= 1.5 s apart; stop a host on
  429/403/challenge, one retry after a pause at most). Report request counts per host.
- Rule 3: any gate is pre-registered (a PREREG file committed and pushed before the scored run), with a matched control that can vary on
  the statistic tested; report both numbers. Rule 4 grades with counts. Rule 7: `tools/decode_key.py <folder> --check` exit 0 before push
  if the reading or key changed. A reading change after AUDIT.md: say so in NOTES.md and flag in ROOM for a verifier.
- Rebase before writing shared files (status.json, PROGRESS.tsv, ROOM.md, HYPOTHESES.md); keep both facts on conflict. Run
  `python3 tools/file_shrink_guard.py <every file you touched>` before the final push; push with `python3 tools/room.py --push <paths>`.
- Partial targets: update "## Remaining gaps" / "## Escalation" (Verdict line) and pass `python3 tools/gaps_check.py <target>`.
- Words: never "solved", "cracked", "novel", "first", "new" for anything this project did; rule 10 wording only. Never name the
  owner; never print credentials (test presence with `test -n`). Never call AskUserQuestion. Report what was found and where it was not
  found; do not classify novelty.
- Stop at the cap or at 80% of the box, whichever first; do not start a unit that would cross 80% of either. A stop with work half
  done writes what was done and what remains into the folder's files.
- Vision work: crop step mandatory and pasted (`tools/iiif_lines.py --image FILE --out DIR` or the --ark/--canvas form); give
  subagents only crop paths, one page/leaf per call, never a full-page image. Price: ~1.5 per Sonnet subagent pass, reconciliation = 1 unit.
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE LANE-RUN7-account-2",
  then a five-line final report.

## Wave 1 (spawned 01:2x UTC 6 Oct). Intake gate output (01:2x UTC) pasted per job.

### R7-MANTP -- sachsstaatsarchiv-manteuffel-1712, pooled single-code-gloss gate (cap 2.5, box 45 min; disk only, scripts)
Intake gate: `sachsstaatsarchiv-manteuffel-1712: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Verdict cheapest next (D2B-MANT27, 5 Oct): "a pre-registered single-code-gloss gate pooled across the glossed leaves (0502, 0527, 0528, 0501;
shuffle of gloss strings across single-code runs only, known-answer on key.tsv C names; disk only, ~$1)". Pre-register first (PREREG file
pushed): the statistic (fraction of recurring single-code codes whose glosses agree, after MANT5 normalisation), the shuffle (gloss strings
permuted across single-code runs only, pooled over the leaves, >=200 seeds), the gate (real > shuffle p95 AND N recurring >= 3), and the
per-unit rule (CLAUDE.md rule 3 per-unit merge paragraph: report each leaf's own contribution; a value attested only on a leaf that tied its
own control is held M, not merged at C). Known-answer: the key.tsv C names must come out consistent. Only on a PASS may single-code values
enter key.tsv (grade per the prereg); then decode_key --check, and report how many of f.410's / f.409v's U tokens move. This is the D1->D2
push for f.410 (status.json depth D1 66.7%): say in NOTES.md whether f.410 now has a clause above the authentication distance; the depth
itself is the verifier's (do not edit status.json depth fields). Leave 0501 and 0574/0575 alone.

### R7-THURP10 -- thurloe-printed, P10 p.620 L10 against Powell 1937 (cap 2, box 35 min)
Intake gate: `thurloe-printed: partial (line 2) -- edition/page or full-text-search citation found within 6 lines`.
Verdict cheapest next (D2B-THURP3, 5 Oct): "align P10 p.620 L10's 14 groups against Powell 1937's printed sentence (be-api snippets in
AUDIT.md) to grade them C, ~$1". Use tools/interlinear_align.py or a pre-registered hand alignment (written before the lookup); grade C only
where the printed sentence fixes the value without ambiguity, M otherwise; any conflict with key_stamford/key_butler logged with witnesses.
If the be-api snippets do not cover all 14 groups, one be-api query per missing span at most (archive.org, 1.5 s apart). Update the gap line.

### R7-SUR -- na-suriname-map-1781, single-sign blind look (cap 4.5, box 45 min; 1 vision call + worker check)
Intake gate: `na-suriname-map-1781: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Verdict cheapest next (GAPS64, 3 Oct): "one look at L08:51 / L10:30 'noo[l]e' and the [sigma] i/e split (L11:17 vs L10:66) as single-sign
crops in one blind same-hand call, ~$4, 1 vision call". Cut single-sign crops from the native images on disk (paste the crop command),
include for each target sign 3-4 same-hand reference crops of the candidate values (labelled only by index, not by value), one Sonnet call,
blind. Pre-register what each answer changes before the call. Apply only under GAPS23's rule; --check exit 0; 2077 H/C/M/U counts before and
after. Stage 9 stays blocked on LOCAL-QUEUE L36/L41; flag for VERIFY5 if any token changes.

### R7-OLDA -- na-oldenbarnevelt-2442-1605, crop-and-read pass on blocks A and C2 (cap 6, box 70 min; 2 blind passes + 1 reconciliation)
Intake gate: `na-oldenbarnevelt-2442-1605: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Verdict (after OLD-ES17A): "(a') crop-and-read pass on blocks A and C2 with the settled conventions (tools/iiif_lines.py crops first,
per-pass pricing), ~$4". Two blind passes (A in order, B reversed) on the block A and C2 crops, tools/reconcile_passes.py, one
reconciliation unit from the image; then the folder's existing key/decode route on the reconciled text with grades. If the two passes split
on more than a tenth of the signs, stop after reconciliation and log it for the owner's sorter (CLAUDE.md Usage 6) -- no third pass.
Judge only with the es17a corpus already on disk and say "unknown reliability" per the OLD-ES17A fold result.

### R7-MATSORT -- matignon-mayenne-1586, seed the owner's sign sorter for f.110 (cap 2, box 40 min; no vision)
Intake gate: `matignon-mayenne-1586: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Verdict cheapest next (D2B-MATF110, 6 Oct): "the f.110 glyphs go to the owner's sign sorter (tools/sign_sorter.py, crops images/f110/, ~$1
to seed)". Build the sorter from the crops already on disk per tools/sign_sorter.py --help and sorter/README.md conventions in other folders
(e.g. grep for an existing ciphers/*/sorter/), with a focus.tsv of the pass-split pairs. Do NOT publish an artifact and do NOT write ASKS.md
yourself: write the sorter files, then one ROOM flag line "matignon f.110 sorter ready for the owner, path ..." for the lane orchestrator,
who files the ASKS row. NEAR.md row stays; status stays partial.

### R7-ROUS -- naf14913-rousseau-venice-1743, Souchon 1915 No 2044 check (cap 1.5, box 30 min)
Intake gate: `naf14913-rousseau-venice-1743: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Verdict cheapest next: "Souchon 1915 N° 2044 (f.197r letter, 21 Dec 1743) and re-check N° 2031 text for a printed decipherment, ~$1".
Read the Souchon text already located by A3V2-ROUS2 (ALTO/Gallica or IA, whichever the folder used; fetch once) at N° 2044 and N° 2031;
report whether either prints a plain side for the f.197r / f.165r cipher passages, with page numbers. A printed plain side = a crib: note it
and the next step; do not start the crib alignment in this job.

## Wave 2 (spawned 01:4x UTC 6 Oct). Wave 1 result: 6/6 D (16.24). Intake gate output (01:4x UTC) pasted per job.

### R7-MANT463 -- sachsstaatsarchiv-manteuffel-1712, transcribe 0574/0575 (f.463) and gate (cap 5.5, box 75 min; 2 blind passes + 1 reconciliation at ~1.5 each + scripts)
Intake gate: `sachsstaatsarchiv-manteuffel-1712: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Verdict cheapest next (R7-MANTP, 6 Oct): "transcribe 0574/0575 (f.463, dense glossed; 2 blind passes + 1 reconciliation, ~$3-4) and add it to the
pooled single-code-gloss gate (pooled_mantp/pooled_gate.py)". Confirm folio labels from the frames first (D2B-MANT27's check). The D2B-MANT27 shape
exactly: crop step pasted, two blind passes (one page per call, crop paths only), reconcile_passes.py, one reconciliation unit, decode_key.py,
the per-leaf gate AND the pooled gate re-run with the leaf added (same PREREG; an addendum for the added leaf pushed before scoring). Codes enter
key.tsv only per the per-unit merge rule. Report how many f.410 / f.409v U tokens move and whether f.410 now has a clause above the
authentication distance (the depth itself is the verifier's). If the two passes split > 10% of tokens, stop after reconciliation.

### R7-OLDSORT -- na-oldenbarnevelt-2442-1605, seed the owner's sign sorter for blocks A/C2 (cap 2, box 40 min; no vision)
Intake gate: `na-oldenbarnevelt-2442-1605: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
R7-OLDA (6 Oct) split 19.0% and handed blocks A/C2 to the owner's sorter. Build it from the R7-OLDA crops on disk as R7-MATSORT did for matignon
(ciphers/matignon-mayenne-1586/sorter/: build.sh, build_inputs.py, focus.tsv of the pass-split pairs from transcription/disagreements_R7OLDA.tsv;
the 9/q, f/p, v/r, l/t, G/t pairs first). Do NOT publish and do NOT write ASKS.md; one ROOM flag line with the path for the lane orchestrator.

### Sonnet print/crib greps (model Sonnet 5; each cap 1.2, box 30 min; script-first, Usage 2; fetch once, grep, give the model the hits)
For each: first check the folder's NOTES.md for a dated section that already ran the step (NEXT-STEPS.tsv lags); if done, report and stop.
Record what was searched, hits with page/leaf, and what was not found; a hit that prints the letter's plaintext is a crib -- note it and the
next step, do not align. Do not touch keys or readings.
- R7-WVOH -- wvo-hessen-1564. Intake gate: `wvo-hessen-1564: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
  Step: a Huygens WVO search for Hessen -> Oranje letters of Oct-Dec 1564 (Wilhelm's reply to 1109, which might paraphrase the enciphered
  news), ~3 requests (host table row: >= 2 s apart, descriptive UA).
- R7-CHEST -- sp87-chesterfield-1747. Intake gate: exit 0 with `WARNING: citation reads as a reused/re-cited search, not one this worker
  independently opened`. Step: grep Coxe, *Pelham Administration* (1829, archive.org _djvu.txt) for July-Aug 1747 Waldeck/Cronstrom despatches
  to Cumberland, a crib source for the cipher passage.
- R7-NEWC -- sp87-newcastle-1743. Intake gate: `sp87-newcastle-1743: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
  Step: be-api full-text search for "Munchberg" across the HMC reports and Yorke's *Life of Hardwicke* (archive.org, no login).
- R7-DONC -- sp78-doncaster-1621. Intake gate: `sp78-doncaster-1621: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
  Step: grep CSP Venice vol. 17 (1621-1623; BHO or archive.org full text) for the Venetian ambassador's reports of Doncaster's Sept 1621
  audiences, a crib source for the item's subject.
