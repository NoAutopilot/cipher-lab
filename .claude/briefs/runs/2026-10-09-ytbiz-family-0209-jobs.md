# LANE FAMILY jobs (account 2, incarnation DEFAULT-account-2-20261009-0209, "FAMILY-A2e") -- 9 Oct 2026 02:2x UTC, lane orchestrator session_01S9QsmhcdrX6TVitHucfaiQ

Lane brief: .claude/briefs/lane-family.md (+ lane-common-blast.md). Cap 60, box 02:09-12:09 UTC 9 Oct. Fifth incarnation: started from
STATUS.md "LANE FAMILY handoff" (DEFAULT-account-2-20261009-0009) next list items 1-5. Gate 0a: SESSION-SWEEP-account-2 stale-claimed since
5 Oct (prior incarnations proceeded). Exclusions as the 0009 jobs file: eckert-*, lodewijk-van-nassau-1573-74, baluze167, huntington-blathwayt,
ceppo-nevers, Gallica fetches, Birago/Armstrong/Debosnys, every folder with a ROOM claim < 6 h and no done line.
Intake gate 02:1x UTC (tools/intake_gate_check.py, exit 0 each): hessen-daenemark-1672 partial, sachsstaatsarchiv-manteuffel-1712 partial,
wvo-11106-bergh-1572 open, na-suriname-map-1781 partial, la-garde-1577 open -- "edition/page or full-text-search citation found within 6 lines".

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim line
  with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE FAMILY-A2e (account 2)". If --start fails to push
  from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
- Prior work (`.claude/briefs/prior-work-step.md`): run `python3 tools/prior_work.py <slug> --item-spec '...' --step-type <type> --fetch`
  first and paste its output and exit code (exit 4 = the LOOK/UNCHECKED rows it lists are owed by you, then `--record` them); then checks
  1-4 by hand where v1 does not reach, one line per check (route, query, result) in your NOTES.md section BEFORE the first priced step;
  check 5 after any decode. A check that did not run is "unchecked". If check 1 shows the step already done, one ROOM line and stop.
- Read the folder's NOTES.md tail (Remaining gaps / Escalation / latest dated sections), HYPOTHESES.md and AUDIT.md section list first.
- Good-citizen rule and the CLAUDE.md host table (one request per host at a time, >= 1.5 s apart; stop a host on 429/403/challenge, one
  retry after a pause at most). Report request counts per host. Prefer files already on disk. No Gallica.
- Shared hosts: post `<host> take` / `<host> release` ROOM lines around each batch to www.archiv.sachsen.de ("sachsen"),
  resources.huygens.knaw.nl ("huygens"), service.archief.nl / www.nationaalarchief.nl ("NA"), archive.org ("IA"); if another worker of
  this lane holds the host (a take with no release in the last 30 min), work from disk meanwhile and wait.
- Rule 3 (matched control first; a control that cannot differ from the target on the statistic is a non-test), rule 4 grading, rule 7
  (`--check` scripts). Pre-register any new gate in a PREREG-<JOB>.md pushed before the score is computed.
- Rebase before writing shared files; keep both facts on conflict. Commit only your own paths. Run
  `python3 tools/file_shrink_guard.py <every file you touched>` before the final push; push with `python3 tools/room.py --push <paths>`.
- Partial/open targets: update "## Remaining gaps" / "## Escalation" (Verdict line) and pass `python3 tools/gaps_check.py <target>`.
- Words: never "solved", "cracked", "novel", "first", "new" for anything this project did; rule 10 wording only. Never name the owner; never
  print credentials. Never call AskUserQuestion. Solver jobs: report what was found and where it was not found; do not classify novelty.
- Stop at the cap or at 80% of the box, whichever first; do not start a unit that would cross 80% of either. Opus session floor ~1.5.
- Vision work: crop step mandatory and pasted (`tools/iiif_lines.py --image FILE --out DIR ...`); line or strip crops only, never a full
  page image to a subagent; one page (or half page) per subagent call; ~1.5 per vision call, reconciliation one more unit.
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE FAMILY-A2e (account 2)",
  then a five-line final report.

- Hosts this wave: digitalisate-he.arcinsys.de ("arcinsys", BRANDT-GATE only), archiv.sachsen.de ("sachsen", MANT-0056 only),
  service.archief.nl / www.nationaalarchief.nl ("NA", SUR-0745 only), resources.huygens.knaw.nl ("huygens", BERGH-ALL1 only); LAG-MARKS
  is disk only. One worker per host; the jobs below are already split so no two share one.


## Wave 1 (02:2x UTC 9 Oct)

### BRANDT-GATE (Opus, cap 3.5, box 80 min): hessen-daenemark-1672, pre-registered agrees-count gate on 0020 + held-out 0049 letter test
Handoff next 1; NOTES "BRANDT-TX" and "HDK-BRANDT check-solved" sections; files in dk131_brandt/. BRANDT-TX's registered CONSISTENT gate FAILed
(9 vs derangement max 12) while its EXPLORATORY token agrees count separated (95 vs mean 33.2, max 49, p 0.005). This job does NOT re-run CONSISTENT
(rule 3's third-attempt clause would retire it); it registers a different statistic. Steps: (1) PREREG-BRANDT-GATE.md pushed BEFORE any score:
the agrees statistic exactly as explore_agrees.py computes it, the same pairs_0020.tsv and parameters, a fresh seed set, n >= 1000 derangements,
gate "real > control max AND p < 0.01", plus a second, independent test: the 0049 held-out letter test -- the key learned from 0020 alone
(key_0020.tsv top chunk per value, single-letter values only) applied to 0049's slip groups, scored as letters matching 0049's own one-letter
glosses, against a control that permutes key_0020's value->letter assignments (n >= 1000; gate real > p99). State both gates and what each PASS/
FAIL licenses (C grades only on PASS; on FAIL the token stays M). Check that each control can differ from the target on its statistic (rule 3).
(2) 0049: "arcinsys take", one GET at the largest size (URL pattern in dk131_inventory.tsv / NOTES "HDK-131"), scratchpad only; crop the slip's
4 lines and the left-page foot with tools/iiif_lines.py --image (paste the command; check the debug overlay; shear if lines climb, as BRANDT-TX
found), two blind Sonnet passes on the crops (group + the letter written over it), reconcile with tools/reconcile_passes.py, settle splits from
the image. Write dk131_brandt/ciphertext_0049.tsv with per-group gloss letter. (3) Score both gates; HYPOTHESES.md rows with both numbers.
(4) NOTES section "BRANDT-GATE (9 Oct 2026)", Remaining gaps/Escalation update, gaps_check. Units: 2 vision passes + 1 reconciliation (~1.5 each)
+ CPU. ~$3. If both PASS, the next step (0020 upper block + 0021, ~4) is a one-line suggestion, not this job.

### MANT-0056 (Opus, cap 5, box 100 min): sachsstaatsarchiv-manteuffel-1712, 694/09 frame 0056 as a known-answer leaf
Handoff next 2; NOTES "MANT-0609Y" (0056 heavy, glossed, p.42, Berl. 18 Fevr 1713, est. 90-110 tokens, gloss over most runs) and the Remaining
gaps row "694/09 0056 and 0063 glossed leaves". Goal: transcribe 0056's code tokens and its period gloss, then score the folder's current key
(key.tsv as decode_key.py uses it) against the gloss as a known-answer gate: per glossed token, does key.tsv give the gloss value? Pre-register
(PREREG-MANT-0056.md, pushed before the score) the statistic, a shuffle control that can differ (permute key values across codes, n >= 1000),
and the gate (real > p99); on PASS the glossed tokens are C and codes absent from key.tsv but glossed here are candidate key additions graded C,
listed in a separate key_add_0056.tsv (not merged into key.tsv by this job -- rule 3 per-unit clause: say this leaf's own control result beside
each). Method: "sachsen take", fetch 0056 once at native (URL in images/loc694-08-09/frames.tsv), tools/iiif_lines.py --image crops (paste the
command, check overlay), two blind Sonnet passes for the code tokens + one pass for the gloss words, your reconciliation as one more unit. Write
f0056_09/ (ciphertext.tsv, gloss.tsv, gate output), NOTES section "MANT-0056 (9 Oct 2026)", Remaining gaps/Escalation update, gaps_check.
Units: 3 vision passes + 1 reconciliation (~1.5 each) + CPU, ~$4.5. 0063 is NOT in this job (a one-line suggestion).

### SUR-0745 (Opus, cap 4, box 90 min): na-suriname-map-1781, NA 1.05.03 inv. 373 scan 0745 as a held-out unit, dot dropped, m-vs-n split
Handoff next 4; NOTES "SUR-0744R" and its "Next (not run, one unit per brief)" line, AUDIT.md "What 0744 right and 0745 must..." and V-SUR0744 /
V-SUR0744R. Goal: 0745 as one held-out unit under the CLASS gate exactly as SUR-0744R ran it (same scripts, same seeds policy), with the DOT gate
dropped (it had no headroom: permutation p99 at ceiling), plus a pre-registered pooled [y-fam] m-vs-n split test under a derangement control
(PREREG-SUR-0745.md pushed before scoring; check the derangement CAN change the statistic). Method: images on disk first; else "NA take", one
fetch of 0745 via service.archief.nl IIIF, two blind passes (crop step pasted), reconcile. Write the unit's files beside SUR-0744R's, NOTES section
"SUR-0745 (9 Oct 2026)", Remaining gaps/Escalation, gaps_check. Units: 2 passes + 1 reconciliation (~1.5 each) + CPU, ~$3.5.

### LAG-MARKS (Opus, cap 4, box 90 min, disk only): la-garde-1577, prior-work rows + marks-kept split cells
Handoff next 5; NOTES Remaining gaps rows "plaintext prior-work rows" and "marks-kept transcription error", Escalation [ ] image-check.
(1) FIRST the owed prior-work rows: `python3 tools/prior_work.py la-garde-1577 --step-type decode --fetch` (or the item form the last run used,
see NOTES "LAG-SYL"), do each LOOK/UNCHECKED row's one look or read and `--record` it; paste output and exit code. If a row turns up a period
gloss or printed plaintext for this letter, stop and ROOM-flag (KNOWN). (2) Settle the overline/loop cells that pass A and L1 split on
(lag_err_cells.tsv) plus the two 10/18 cells from the images on disk (crops; native zoom; one Sonnet look per cell batch + two on doubt), and
re-measure the one-reader marks-kept error. State whether it falls inside LAG-SYL's covered band (<= 0.107) or in the uncovered 0.107-0.183 band.
(3) If inside: the syllabary negative covers the target -- update HYPOTHESES/NOTES. If outside: name the next control level, do not run it.
NOTES section "LAG-MARKS (9 Oct 2026)", Remaining gaps/Escalation, gaps_check. Units: ~2 look batches + reconciliation, ~$3.

### BERGH-ALL1 (Opus, cap 8, box 140 min): wvo-11106-bergh-1572, BERGH-GRP sign-group instrument on boxes 1-~440 (first half)
Handoff next 3; NOTES "BERGH-GRP" (gate 18/19 vs pre-registered 17 PASS on a de-stacked layout; atlas/group_sign.tsv for 19 windows, 285
boxes) and the Verdict line ("the instrument on all 875 boxes with whole-line de-stacked strips, then the sorter rebuild"). This job: the same
instrument, unchanged (prompt, strip layout, model, reconciliation rule as BERGH-GRP recorded them), on the first half of the box sequence not
already in group_sign.tsv, stopping at a line boundary near box 440. Images on disk first ("huygens take" only if a fetch is unavoidable).
Crop step pasted; one strip set per subagent call; per-unit pricing from BERGH-GRP's own cost per window (state your unit count x rate before
starting and stop before a unit that would cross 80% of cap or box). Write atlas/group_sign.tsv rows (append, a `job` column BERGH-ALL1),
NOTES section "BERGH-ALL1 (9 Oct 2026)" with counts, agreement and every box the reader flagged; Remaining gaps update, gaps_check. No sorter
rebuild, no decoding. The second half is BERGH-ALL2 (next wave or next incarnation).

## Wave 2 (02:5x UTC 9 Oct)

Common-rules addition (wave 1 lesson, MANT-0056): `tools/room.py "msg" --push <paths>` committed ROOM.md only and left the named paths behind
(the 0009 orchestrator saw the same). Commit PREREG files and results with `git add <paths> && git commit && git push` directly, and check
`git log -1 --stat` shows the PREREG BEFORE computing any score.
Hosts this wave: arcinsys (BRANDT-UP only), sachsen (MANT-0063 only); the rest are disk/CPU only.

### BRANDT-UP (Opus, cap 5, box 100 min): hessen-daenemark-1672, Brandt 0020 upper block + 0021 under the gate-passed values
NOTES "BRANDT-TX" and "BRANDT-GATE"; dk131_brandt/ (values_gate.tsv: 16 values C, 8 M after BRANDT-GATE). Goal: (1) the 0020 upper block (the
3 lines continuing from L01's clear text, ~20 groups) and the right-page head block above "Es ist hier eine troupe" (~44 groups); (2) leaf 0021
(arcinsys take, one GET at the largest size; BRANDT-TX/HDK-BRANDT give the URL pattern): its cipher groups and any gloss. Crop with
tools/iiif_lines.py --image (paste the command; shear as BRANDT-TX's shear_crops.py if lines climb), two blind Sonnet passes per block,
reconcile_passes.py, settle splits from the image. Then apply only values_gate.tsv's C values (no new values inferred) and report coverage:
tokens covered by C values, and any gloss over these blocks scored against them (known-answer, not a gate unless pre-registered first and
committed with git before scoring). Grades: C only for glossed tokens; decoded-by-C-value tokens unglossed are S only if a pre-registered gate
covers them, else M. Write ciphertext_0020u.tsv / ciphertext_0021.tsv, NOTES section "BRANDT-UP (9 Oct 2026)", Remaining gaps/Escalation,
gaps_check. Units: 4 passes + 2 reconciliations (~1.5 each) + CPU, ~$4.5 (stop before a unit crossing 80%: do 0020 first, 0021 second).

### MANT-0063 (Opus, cap 4, box 90 min): sachsstaatsarchiv-manteuffel-1712, 694/09 frame 0063 as a known-answer leaf
As MANT-0056 (wave 1, NOTES "MANT-0056 (9 Oct 2026)", PREREG-MANT-0056.md design) on frame 0063 (p.44, Berl. 15 ..., est. 55-70 tokens,
moderate gloss). PREREG-MANT-0063.md committed with git BEFORE any score (check git log). "sachsen take", one fetch, crops pasted, two blind
passes + one gloss pass + reconciliation, gate, key_add_0063.tsv (not merged). NOTES section "MANT-0063 (9 Oct 2026)", gaps_check. ~$3.5.

### V-SUR0745 (Opus verifier, cap 3, box 70 min): na-suriname-map-1781, audit SUR-0745's 0745-left CLASS PASS and SPLIT no-split
Separate session from the solver. Read NOTES "SUR-0745 (9 Oct 2026)", PREREG-SUR-0745, AUDIT.md (V-SUR0744 / V-SUR0744R sections) and the
unit's files. Re-run the scoring scripts with --check and fresh seeds (as V-SUR0744R did): does CLASS hold on fresh seeds for both passes; was the
PREREG committed before the passes (git log); can the SPLIT control differ from the target; is the dot-dropped design the one AUDIT.md's "What
0744 right and 0745 must" paragraph asked for. Write a dated AUDIT.md section "V-SUR0745 (9 Oct 2026)": holds / does not hold, per gate, with
numbers; correct any over-claiming sentence. No novelty class change unless the evidence requires it (rule 10; this is a design/gate audit).
Disk only. ~$2.5.

### BERGH-ALL2 (Opus, cap 6, box 110 min): wvo-11106-bergh-1572, BERGH-GRP group instrument on lines L11-L22
As BERGH-ALL1 (NOTES "BERGH-ALL1 (9 Oct 2026)"; atlas/strips_grp.py, same prompt, model and reconciliation), on L11-L22 (the rest of the 875
boxes). Append to atlas/group_sign.tsv with job BERGH-ALL2; NOTES section with counts, A/B agreement, overlap with BERGH-GRP's windows, every
reader-flagged box. No sorter rebuild, no decoding; the sorter rebuild is a one-line suggestion. Disk only. ~$4.5.

### LAG-SYL13 (Opus, cap 2.5, box 60 min, CPU): la-garde-1577, syllabary control at marks-kept error 0.13
LAG-MARKS (NOTES "LAG-MARKS (9 Oct 2026)") left the one-reader marks-kept error at 0.071 central / 0.125 upper, undecided against LAG-SYL's
covered band (<= 0.107). Run the syllabary (regular) family control at injected error 0.13 exactly as LAG-SYL ran 0.055/0.084/0.107/0.183
(same family_run.py invocation, seeds, N, corpus; PREREG-LAG-SYL.md + Amendment 1; add an Amendment 2 for 0.13, committed with git before
running). If the control meets the LAG-SYL gate at 0.13, score the target under that gate (family_run.py runs target only after the control
reads) and log both numbers in HYPOTHESES.md; if it fails, log "control below gate at 0.13" and say what that means for the negative's
coverage. Do NOT edit the v2 marks transcription (LAG-MARKS flagged 7 sure settles that differ from v2 -- a one-line suggestion). NOTES section,
Remaining gaps, gaps_check. ~$2.

### CLIN-EYE (Opus, cap 2, box 50 min, disk only): pro3055-clinton-1779, eye check of the c5:18 underline and the c6 cells on existing crops
NOTES lines about CLIN-RG and D4-CLIN: the alignment design is retired (rule 3 third-attempt clause), so this is a transcription correction only,
not a re-gate. On the existing p.123 crops (p123_full_reconciled.tsv and the crops it cites), look at c5:18 (is there an underline?) and every c6
cell at native zoom; two Sonnet looks on doubt. Record each cell: as transcribed / corrected (with the image evidence) in the reconciled TSV's
notes column or an errata TSV, NOTES section "CLIN-EYE (9 Oct 2026)". Do not re-score either gate. gaps_check. ~$1.5.
