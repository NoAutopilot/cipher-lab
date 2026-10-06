# LANE DEFAULT-account-1-20261006-1240 jobs (account 1) -- 6 Oct 2026 12:5x UTC, lane orchestrator session_016tXAHgaAgQXB3m94TerHE6

Lane brief: .claude/briefs/default-lane.md (cap 60, box 12:40-22:40 UTC 6 Oct). Gate 0a: SESSION-SWEEP-account-1 row still `claimed`, but the
sweep session completed 22:48 5 Oct (243/251 pushed, 0 unpushed; RUN8/9/10-account-1 claims) and its TSV is on disk: proceeding, 0 exclusions.
Folders a-h (account split as RUN7-RUN10). Backlog a: VERIFY-BACKLOG high row decode-2678 audit2 (RUN10 closed 11:14, no live claim); fr16142
`counted` rows are register lag (RUN9 handoff), not a verifier job. Backlog b: the RUN10-account-1 handoff's "Open for the next a-h lane" list,
then `tools/next_steps.py --hot-only` runnable rows. Excluded: account-4 DEFAULT-1235 wave folders (fr16045, decode-1411, fr16106,
clairambault296 and its sister clairambault1225, esp318, fr4715), Birago, Armstrong, Debosnys, antt-linhares (check-solved blocked, L10),
anything owner-sorter-gated. Every worker: one job, then stop. Each job first checks its named step is still undone (NEXT-STEPS.tsv lags the
folders); if a dated NOTES.md section or ROOM done line already ran it, stop and report.

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim
  line with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE DEFAULT-account-1-20261006-1240".
  If --start fails to push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
- Read the folder's NOTES.md tail (Remaining gaps / Escalation / latest dated sections), HYPOTHESES.md and AUDIT.md section list first.
- Good-citizen rule and the CLAUDE.md host table for every request (one request per host at a time, >= 1.5 s apart; stop a host on
  429/403/challenge, one retry after a pause at most). Report request counts per host.
- Rule 3: any gate is pre-registered (a PREREG file committed and pushed before the scored run), with a matched control that can vary on
  the statistic tested; report both numbers. Rule 4 grades with counts. Rule 7: `tools/decode_key.py <folder> --check` (or the folder's
  own decode script --check) exit 0 before push if the reading or key changed. A reading change after AUDIT.md: say so in NOTES.md and
  flag in ROOM for a verifier.
- Rebase before writing shared files (status.json, PROGRESS.tsv, ROOM.md, HYPOTHESES.md); keep both facts on conflict. Run
  `python3 tools/file_shrink_guard.py <every file you touched>` before the final push; push with `python3 tools/room.py --push <paths>`.
- Partial targets: update "## Remaining gaps" / "## Escalation" (Verdict line) and pass `python3 tools/gaps_check.py <target>`.
- Words: never "solved", "cracked", "novel", "first", "new" for anything this project did; rule 10 wording only. Never name the
  owner; never print credentials (test presence with `test -n`). Never call AskUserQuestion. Solver/lookup jobs: report what was found
  and where it was not found; do not classify novelty.
- Stop at the cap or at 80% of the box, whichever first; do not start a unit that would cross 80% of either. A stop with work half
  done writes what was done and what remains into the folder's files. An Opus session floor is about 1.5; caps below assume it.
- Vision work: crop step mandatory and pasted (`tools/iiif_lines.py --image FILE --out DIR` or the --ark/--canvas form); give
  subagents only crop paths, one page/leaf per call, never a full-page image. Price: ~1.5 per Sonnet subagent pass, reconciliation = 1 unit.
- Sorters: any sorter meant for the owner must PASS `python3 tools/sorter_preflight.py` and have 5+ random tiles opened against the line
  image before it is handed on; it is handed to the account-3 orchestrator (ROOM flag line) to publish. Never publish an artifact or edit
  ASKS.md yourself.
- No private-repository access in these sessions: if a step needs one, stop and say so in ROOM (the lane hands it to the standing session).
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE DEFAULT-account-1-20261006-1240",
  then a five-line final report.


## Wave 1 (spawned 12:5x UTC 6 Oct). Intake gate output (12:4x UTC) pasted per job.

### D1-DEC2678A2 -- decode-2678-bnf-colbert127-gravel-1665, AUDIT 2: second adversarial novelty audit (verifier, Opus; cap 3, box 50 min)
Intake gate: `decode-2678-bnf-colbert127-gravel-1665: partial (line 3) -- edition/page or full-text-search citation found within 6 lines`.
VERIFY-BACKLOG high row (audit2). You are a separate session from AUDIT 1 (R10-DEC2678V) and from every solver (R9-DEC2678*). Follow CLAUDE.md
"Verifier brief (template)" in full and Outreach gate 2: try to find the plaintext or a decipherment of Gravel to Colbert, Ratisbon 29 Jan 1665
(Mel. Colbert 127 f.349) in print -- Depping, Clément (Lettres de Colbert), Recueil des instructions (Diète/Allemagne), Haug 2015 if reachable,
the open indexes (OpenAlex, Semantic Scholar, CORE, Persée, HAL, CrossRef), Google Books (`country=US`), IA full text, DECODE record page,
Tomokiyo's pages. Queue JSTOR-QUEUE.tsv rows only if AUDIT 1's three rows do not already cover both families (i) and (ii). Log every family
searched/unreachable. Append "## AUDIT 2" to AUDIT.md with an N-class, key source (`published`, Tomokiyo), depth re-check (rule 4a, N=15 tokens),
safe/unsafe sentences; correct any over-claim. Update status.json/PROGRESS.tsv audit2 field only as the register's own convention shows. Do not decode.

### D1-SEURE -- fr3151-seure-1558, Morvilliers 1549 (fr. 3138 no. 24 fo. 66r) key rebuild from its marginal decipherment, then R1/R2 test (Opus; cap 8, box 120 min)
Intake gate: `fr3151-seure-1558: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Folder Verdict cheapest next (R10-SEURE4). Units at ~1.5 each: crops (regen via known_keys/regen_images.sh / tools/iiif_lines.py, canvas 70
cipher + margin regions; paste the command) + 2 blind Sonnet passes over the cipher-block line crops (crops only, one call per pass) +
1 reconciliation + 1 read of the marginal clear text = 4 units ~6; then alignment with tools/interlinear_align.py (or a sequence alignment of
signs to letters if the layout is continuous; say which) and the test ~1.5. If the two passes disagree on more than a tenth of signs, stop after
reconciliation (TRANSCRIPTION.md: next is the owner's sign sorter), write what you have, and do not run the test. Otherwise PREREG (statistic,
own-text power control first -- the rebuilt key must read a held-out stretch of the Morvilliers clear text from its cipher above gate -- then
R1/R2 with shuffled-key control) committed and pushed BEFORE scoring. Report both numbers. Grade per rule 4 (a rebuilt period key = H on
Morvilliers' own text, S/M on R1/R2). Write "## D1-SEURE" in NOTES.md, HYPOTHESES.md row, Remaining gaps / Escalation, gaps_check.py.

### D1-ECK62L -- eckert-1862, received-ledger pass on mssEC 04-14 by the GAPS171 method (Opus; cap 3, box 50 min)
Intake gate: `eckert-1862: partial (line 3) -- edition/page or full-text-search citation found within 6 lines`.
Folder Verdict cheapest next. Read "## GAPS171" in NOTES.md and reuse its scripts/method exactly (harvest, grep, align against the residue
entries of mssEC 15); fetch each volume once with a manifest (Usage 4). Report entries matched, grade per rule 4, residue count before/after;
decode --check if the reading changes. Stop before starting a volume that would cross 80% of cap or box; write which volumes remain.

### D1-DEC1162F -- decode-1162-modena-ambung-1492, focus sheet of the unsettled clear-text words for a person's read (Opus; cap 1.5, box 30 min; disk only)
Intake gate: `decode-1162-modena-ambung-1492: partial (line 3) -- edition/page or full-text-search citation found within 6 lines`.
Folder Verdict cheapest next (R10-DEC1162B). Build a focus sheet (one HTML page or the folder's existing sorter/focus format, whichever the
folder already uses) of the doubts_R10B.tsv rows marked stays / read-doubtful / RAISED: each with its word crop, both blind readings and the
line context. Open 5 random tiles against the line image before handing it on. Hand it to the account-3 orchestrator with a ROOM flag line
(do not publish, do not edit ASKS.md). Update Remaining gaps / Escalation; gaps_check.py.

### D1-BAL167 -- baluze167-davaux-1637, enlarge the gloss-fixed exemplar set to >= 2 per shape (Opus; cap 4, box 60 min; disk only unless crops are missing)
Intake gate: `baluze167-davaux-1637: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Folder Verdict cheapest next (NOTES.md line ~585). Read the last three dated sections first. Add exemplars only from gloss-fixed positions (a
glossed sign whose gloss letter is legible), crop step pasted, one subagent call per leaf at most. Report shapes now at >= 2 exemplars vs before,
and whether that unblocks the exemplar-sheet labeller for f.247 (do not run the labeller in this job). Remaining gaps / Escalation; gaps_check.py.

### D1-CEPPO -- ceppo-nevers-fr3251-1570s, f.36v S76/S58 gloss tiles to one blind Opus reader (Opus; cap 4, box 50 min; disk only)
Intake gate: `ceppo-nevers-fr3251-1570s: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Folder Verdict cheapest next (A1B-CEPPO-36V: two Sonnet reads gave no agreed letter). Give one Opus subagent only the a1b36v/tiles crops
(no prior readings, no key hints) and ask for a letter per tile with a confidence; compare to the two Sonnet reads. A letter counts only where
2 of 3 readers agree; otherwise the tile stays M. If any value enters the key, decode --check. Write "## D1-CEPPO" in NOTES.md, Remaining gaps /
Escalation, gaps_check.py.

## Wave 2 (spawned 13:0x UTC 6 Oct). Wave 1 lesson: an Opus session floor is ~2 for a build job and ~3.5 for a full verifier pass; caps below assume it.

### D1-SEURES -- fr3151-seure-1558, Morvilliers 1549 fo. 66r sign sorter for the owner (Opus; cap 3, box 45 min; disk only)
Intake gate: `fr3151-seure-1558: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
D1-SEURE stopped at the >0.1 pass split (err 0.778); TRANSCRIPTION.md: next is the owner's sign sorter. Build it from D1-SEURE's 22 re-cut line
crops with tools/sign_sorter.py (use the folder's or a sibling's build.sh pattern; focus box = the signs the two passes split on). Must PASS
`python3 tools/sorter_preflight.py` and have 5+ random tiles opened against the line image. Hand to the account-3 orchestrator with a ROOM flag
line (do not publish, do not edit ASKS.md). Remaining gaps / Escalation; gaps_check.py.

### D1-ECK62W -- eckert-1862, the 1865 received copies in mssEC 12-13 for the Lehigh third witness (Opus; cap 2.5, box 40 min)
Intake gate: `eckert-1862: partial (line 3) -- edition/page or full-text-search citation found within 6 lines`.
Folder Verdict cheapest next (D1-ECK62L). Reuse D1-ECK62L's harvest of mssEC 12-13 on disk if present (no refetch); method as GAPS171.
Report witnesses found, grade per rule 4, --check exit 0 if anything changes.

### D1-DEC2678S -- decode-2678-bnf-colbert127-gravel-1665, sommaire sweep of Mél. Colbert 120-125 and 131-133 for Ratisbon cipher letters (Sonnet; cap 3, box 60 min)
Intake gate: `decode-2678-bnf-colbert127-gravel-1665: partial (line 3) -- edition/page or full-text-search citation found within 6 lines`.
Folder Verdict cheapest next. Same method as the 126-130bis sweep (read that NOTES.md section first and reuse its script): Gallica OCR/sommaire
pages via the IIIF/host-table routes, good-citizen rule. List every Gravel/Ratisbon entry and whether it is marked in cipher; no decoding.
Write "## D1-DEC2678S" in NOTES.md with volumes covered and not covered; Remaining gaps / Escalation; gaps_check.py.

### D1-F16142A -- fr16142-noailles-constantinople-1571, per-token alignment with denser anchors (Opus; cap 2.5, box 40 min; disk only)
Intake gate: `fr16142-noailles-constantinople-1571: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Folder Verdict cheapest next. Read the latest dated sections and HYPOTHESES.md first; any gate pre-registered (PREREG pushed before the scored
run) with a control that can vary on the statistic; report both numbers. --check exit 0 if the reading changes; a reading change after AUDIT.md
is flagged in ROOM for a verifier. Remaining gaps / Escalation; gaps_check.py.

### D1-F16104I -- fr16104-vivonne-spain-1572, ink 53 audit (depth re-check) (Opus; cap 6, box 75 min)
Intake gate: `fr16104-vivonne-spain-1572: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Folder Verdict cheapest next (ink 53 only; ink 54 is a later job). Read how earlier ink audits in NOTES.md were done and repeat that method;
crop step pasted, one subagent call per page/leaf. Report per-token grade counts before/after and the rule 4a depth check; --check exit 0.
A reading change after AUDIT.md: flag in ROOM for a verifier. Remaining gaps / Escalation; gaps_check.py.

### D1-ES132G -- es132-vargas-mexia-1578, cabinet-noir git-log re-check, then the BL Add MS 28421 catalogue lookup (Opus; cap 2.5, box 35 min)
Intake gate: `es132-vargas-mexia-1578: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Folder Verdict cheapest next, both steps exactly as the Verdict names them (read the NOTES.md lines that define them). The BL lookup uses
searcharchives.bl.uk?format=json (host table); quote the record. No Cipher 3/4 work in this job. Remaining gaps / Escalation; gaps_check.py.

## Wave 3 (spawned 13:2x UTC 6 Oct). Last wave of this lane (lane ~36 of 60 spent at spawn).

### D1-F16104K -- fr16104-vivonne-spain-1572, ink 53 f/m/p key cells against the U labels, pre-registered key change (Opus; cap 3, box 45 min; disk only)
Intake gate: `fr16104-vivonne-spain-1572: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Folder Verdict cheapest next (D2 path named in AUDIT 4 by D1-F16104I). PREREG committed and pushed BEFORE the scored run: which key cells
may change, the statistic, a control that can vary on it (shuffled-key or wrong-cell assignment), the pass rule. Report both numbers. Apply the
change only on PASS; decode --check exit 0. The reading changes after AUDIT 4: say so in NOTES.md and flag in ROOM for a verifier (do not edit
the AUDIT depth yourself). Remaining gaps / Escalation; gaps_check.py.

### D1-ECK62S -- eckert-1862, other Lehigh uses in the sent ledgers mssEC 18-19 (Opus; cap 2, box 35 min)
Intake gate: `eckert-1862: partial (line 3) -- edition/page or full-text-search citation found within 6 lines`.
Folder Verdict cheapest next (D1-ECK62W). Disk first (mssEC 18 is on disk per GAPS206); fetch 19 once with a manifest only if absent. Report
every Lehigh occurrence with its plaintext context and whether it settles the M-graded conflict; grade per rule 4; --check exit 0.

### D1-DEC2678L -- decode-2678-bnf-colbert127-gravel-1665, look at the 14 unlooked Gravel leaves of Mél. Colbert 120-125/131-133 for figure groups (Opus; cap 4, box 55 min)
Intake gate: `decode-2678-bnf-colbert127-gravel-1665: partial (line 3) -- edition/page or full-text-search citation found within 6 lines`.
Folder Verdict cheapest next (D1-DEC2678S list in NOTES.md). 1665 leaves first. Gallica IIIF at a viewing size (not native) is enough to see
figure groups; one request per leaf, good-citizen rule. For each leaf: clear / cipher / partly cipher, with or without decipherment. No
decoding. A cipher leaf found: record its ark/canvas in NOTES.md as a named next step. Stop before a leaf that would cross 80%.

### D1-BAL170 -- baluze167-davaux-1637, Baluze 170 ff.228-230 crops and two blind passes with the court-hand exemplar sheet (Opus; cap 7, box 90 min)
Intake gate: `baluze167-davaux-1637: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Folder Verdict cheapest next (D1-BAL167's 63-exemplar sheet). Units at ~1.5: crop step pasted (tools/iiif_lines.py --ark/--canvas) + 2 blind
Sonnet passes per leaf-page over line crops (one call per page per pass, crops + the exemplar sheet only) + 1 reconciliation. If ff.228-230 is
more than 2 pages, do ff.228 first and stop before a page that would cross 80% of cap. If the passes split > 0.1, stop after reconciliation
(sorter next). Write "## D1-BAL170" in NOTES.md, Remaining gaps / Escalation, gaps_check.py.
