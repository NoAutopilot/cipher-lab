# LANE FAMILY jobs (account 2, incarnation DEFAULT-account-2-20261009-0409, "FAMILY-A2f") -- 9 Oct 2026 04:2x UTC, lane orchestrator session_01Cnc5YUqc7JgCV9R2aq8L2f

Lane brief: .claude/briefs/lane-family.md (+ lane-common-blast.md). Cap 60, box 04:09-14:09 UTC 9 Oct. Sixth incarnation: started from
STATUS.md "LANE FAMILY handoff (incarnation DEFAULT-account-2-20261009-0209)" next list items 1-5. Gate 0a: SESSION-SWEEP-account-2
stale-claimed since 5 Oct (prior incarnations proceeded). Exclusions: eckert-*, lodewijk-van-nassau-1573-74 (live lanes on accounts 1/4),
baluze167, huntington-blathwayt, ceppo-nevers, Gallica fetches, Birago/Armstrong/Debosnys, every folder with a ROOM claim < 6 h and no done.
Intake gate 04:2x UTC (tools/intake_gate_check.py, exit 0 each): hessen-daenemark-1672 partial, sachsstaatsarchiv-manteuffel-1712 partial,
wvo-11106-bergh-1572 open, la-garde-1577 open, na-suriname-map-1781 partial -- "edition/page or full-text-search citation found within 6 lines".

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim line
  with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE FAMILY-A2f (account 2)". If --start fails to push
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
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE FAMILY-A2f (account 2)",
  then a five-line final report.
- PREREG files and results: commit with `git add <paths> && git commit -m ... && git push origin HEAD:main` directly (tools/room.py "msg"
  --push <paths> commits ROOM.md only -- known tooling flag); check `git log -1 --stat` shows the PREREG landed BEFORE computing any score.
- Rule from V-BRANDT (9 Oct): a gloss used as a known answer is read BLIND (two passes) and scored per blind pass; the worker never settles
  the gloss before scoring. Commit every crop a later eye check would need (MANT-EYE63 could not run because crops stayed in scratch).
- Hosts this wave: archiv.sachsen.de ("sachsen": MANT-EYE63R then MANT-0136 -- take/release, the second waits for the first's release);
  everything else is disk only / CPU only. No other host.

## Wave 1 (04:2x UTC 9 Oct)

### BRANDT-REGRADE (Opus, cap 4, box 80 min, disk only): hessen-daenemark-1672, apply V-BRANDT's regrades + blind re-score of 0062
Handoff next 1; AUDIT.md "V-BRANDT" section; NOTES "BRANDT-GATE", "BRANDT-UP", "BRANDT-062"; dk131_brandt/. Steps: (1) apply V-BRANDT's regrades
to dk131_brandt/values_gate.tsv (46=d -> M, and any other value it named) and to BRANDT-UP's token grades (23 C -> M); regenerate the --check
outputs of grade_up.py / grade_062.py etc. so `--check` exits 0 on the regraded inputs. (2) Re-score BRANDT-062's 0062 LCS gate on two BLIND
gloss passes: PREREG-BRANDT-062B.md (amendment: same statistic, control, seeds and gate as PREREG-BRANDT-062, only the gloss input changes to
each blind pass separately, plus the regraded values_gate) committed and pushed BEFORE scoring; two blind Sonnet passes over the committed
crops62/ gloss lines (crop paths only, one leaf per call; the reader sees no gloss_*.txt or prior pass); score each pass separately; PASS on
both = C stands for the tokens BRANDT-062 called C (minus any value now M); else they are M. (3) HYPOTHESES.md rows (both numbers each pass),
NOTES section "BRANDT-REGRADE (9 Oct 2026)", Remaining gaps/Escalation, gaps_check. Units: 2 vision passes (~1.5) + CPU, ~$3.5.
One-line suggestion only (not this job): whether the Brandt pool (0020/0021/0049/0062) warrants its own folder.

### MANT-EYE63R (Opus, cap 2.5, box 60 min): sachsstaatsarchiv-manteuffel-1712, 694/09 0063 flagged-slot eye check (redo)
Handoff next 2; NOTES "MANT-0063" and "MANT-EYE63"; HYPOTHESES.md (code 84 sch vs th, six flagged slots). "sachsen take", ONE GET of 694/09
0063 (URL in images/loc694-08-09/frames.tsv), "sachsen release"; cut crops of the flagged slots with tools/iiif_lines.py --image (paste the
command) and COMMIT them under f0063_09/crops/ (resize to keep the folder under 30 MB; manifest entry). One Opus look per slot at native zoom
plus one blind Sonnet look on doubt; record each confirmed / corrected with evidence in f0063_09/eye63.tsv. If a token changes, re-run the
MANT-0063 gate script --check and report the new number beside the old (no re-registration needed for a transcription correction, but say
so). NOTES section "MANT-EYE63R (9 Oct 2026)", gaps_check. ~$1.5-2.

### MANT-0136 (Opus, cap 6, box 110 min): sachsstaatsarchiv-manteuffel-1712, 694/09 0136 ("chiffre ... celui du proces") as a reading leaf
Handoff next 2 / NOTES "MANT-0136" (identity: same Krauske system, faint gloss under one 14-code run agreeing 11-12 of 13). Wait for
MANT-EYE63R's "sachsen release" (ROOM), then "sachsen take", ONE GET of 0136 at native, release. PREREG-MANT-0136.md committed BEFORE any
score: (a) known-answer gate on the glossed run(s), blind gloss passes, as PREREG-MANT-0063 (shuffle key values across codes, n >= 1000, real >
p99); (b) for the UNGLOSSED tokens, a control that CAN differ from the target on its statistic (coverage under a permuted key cannot -- rule 3):
e.g. tools/judge_plaintext.py (fr; check the corpus era first) on the key.tsv decode vs the same decode under n >= 200 value-permuted keys, gate
real > p95 of the permuted decodes; S grade for unglossed tokens only if (a) and (b) both PASS. Crops committed (f0136_09/crops/), two blind
Sonnet passes for the code tokens + two blind gloss passes, your reconciliation one more unit. Decode with tools/decode_key.py conventions
(f0136_09/ beside f0056_09/, f0063_09/); grade per token (H/C/S/M/I counts). Prior-work check 5 (tools/print_check.py on decoded phrases) after
decode. NOTES "MANT-0136 (9 Oct 2026)", Remaining gaps/Escalation, gaps_check. Units: 4 vision passes + 1 reconciliation (~1.5 each) + CPU, ~$6;
stop before a unit that would cross 80% of cap. Report what was found and where it was not found; do not classify novelty.

### BERGH-SORT (Opus, cap 3, box 70 min, disk only): wvo-11106-bergh-1572, sorter inputs rebuilt from atlas/group_sign.tsv
Handoff next 3; NOTES BERGH-ALL2 "Suggestion" (rebuild sorter inputs from group_sign.tsv agreed group labels, sorter/build_inputs.py, a group tile
per agreed group, with the 158 split boxes (BERGH-ALL1 77 + ALL2 79) and the NEW1 box as the "Check these first" focus). Steps: extend
sorter/build_inputs.py (or add an option) to read group_sign.tsv; write labels.tsv / focus.tsv / cipher_lines.tsv; run tools/sign_sorter.py to
build the page locally and its preflight (paste the output); do NOT publish an artifact -- post a ROOM flag "BERGH sorter ready for publication"
for the account-3 orchestrator (it publishes owner sorters). Offline check of the counts (875 boxes; agreed vs split). NOTES "BERGH-SORT (9 Oct
2026)", gaps_check. CPU + at most 1 Sonnet look at the preflight image, ~$2.

### LAG-V2 (Opus, cap 3, box 70 min, disk only): la-garde-1577, v2 revised with LAG-MARKS' 7 sure settles + lag_syl13 --check + wordcode control
Handoff next 4; NOTES "LAG-MARKS", "LAG-SYL13", Remaining gaps row "wordcode at the measured error". Steps: (1) apply the 7 sure settles to
ciphertext_*_v2.tsv via build_v2.py (input change, logged), re-run lag_err.py, report the revised marks-kept error beside 0.071/0.125. (2) Run
lag_syl13.py --check (the gap LAG-SYL13 left) and fix staleness if any. (3) wordcode control-only first at the measured error:
`tools/family_run.py <spec> --family wordcode --param codes=marked --param err=<measured>` (PREREG-LAG-WC.md committed before; control first,
the target only if the control meets its gate, as family_run.py enforces). HYPOTHESES rows, NOTES "LAG-V2 (9 Oct 2026)", gaps_check. CPU, ~$2.5.

### SUR-POOLPC (Opus, cap 2.5, box 60 min, CPU only): na-suriname-map-1781, SPLIT power at the pooled N before any pooled SPLIT run
Handoff next 5; NOTES "SUR-SPLITPC" (detection 0.570/0.510 at 0745L N). Steps: (1) count m|n tokens in 0744L + 0744R + 0745L (files on disk);
(2) PREREG-SUR-POOLPC.md committed before draws: SUR-SPLITPC's planted-split scaffold at the pooled N, >= 200 synthetic draws per pass scaffold,
gate detection >= 0.80; (3) only if the gate PASSES, run the pooled SPLIT statistic on the real pooled tokens under its derangement control and
report it; if it FAILS, report the N at which detection would reach 0.80 (extrapolate from >= 3 N values) and stop. HYPOTHESES row, NOTES
"SUR-POOLPC (9 Oct 2026)", gaps_check. CPU, ~$2.

## Wave 2 (04:4x UTC 9 Oct)
Hosts: archiv.sachsen.de ("sachsen") MANT-INV08 only (MANT-0136 has already released it); BRANDT-MARGIN disk + Google Books API only.

### MANT-INV08 (Opus worker, Sonnet sheet subagents, cap 5, box 110 min): sachsstaatsarchiv-manteuffel-1712, Loc. 694/08 frame inventory for UNGLOSSED cipher frames
SIBLINGS "Next sibling round" item 6 / NOTES Remaining gaps row "Loc. 694/08 and /09 ciphered reports ... not inventoried". 694/08 has 592 frames
(images/loc694-08-09/frames.tsv); about 50 are in frame_inventory.tsv / frame_rank_gaps189.tsv / frame_classify_gaps207.tsv / frame_batch_gaps201.tsv.
Goal: the method of MANT-0609X and MANT-0609Y (NOTES sections; mant0609/ scripts: sheets of downscaled frames, film header cropped, order shuffled,
two controls of known class planted per batch) on the not-yet-seen 694/08 frames at stride 4 (about 135 frames), to list cipher frames and mark
each glossed / unglossed, est. tokens. Request budget: <= 150 GETs to sachsen at >= 1.5 s, "sachsen take"/"sachsen release" lines, fetch to scratch
at a reduced size if the host serves one, else full and downscale locally; keep only the sheets and a manifest committed (folder < 30 MB). Sonnet
sheet calls ~1 each (state count x rate in your ROOM claim), eye-check every non-"none" flag yourself at ~1000-1600 px. Prior-work check 1 first
(grep each frame in the inventories so no frame is fetched twice). Write mant0608/inventory_stride4.tsv, rank_unglossed_08.tsv, rank_glossed_08.tsv,
NOTES "MANT-INV08 (9 Oct 2026)" with the request count, Remaining gaps / Escalation image-check row updated, gaps_check. No transcription.

### BRANDT-MARGIN (Opus, cap 2, box 50 min): hessen-daenemark-1672, 0020 margin lines 1-2 blind re-read + 0062 gloss phrase search
NOTES "V-BRANDT" / "BRANDT-REGRADE" next: (1) blind re-read of the 0020 margin lines 1-2 from committed crops (dk131_brandt/cropsU or crops; no
new fetch), two blind Sonnet passes not shown values_gate.tsv or any prior pass/gloss file; compare with the worker-settled reading BRANDT-UP used;
if they differ, re-run score_up.py unchanged on each blind pass and report the numbers beside the old (no grade upgrade from this job: BRANDT-UP's
tokens stay M unless a pre-registered gate run on blind inputs passes -- write PREREG-BRANDT-MARGIN.md before scoring if you score). (2) Prior-work
check 5 on the 0062 gloss: tools/print_check.py (Google Books with country=US and the key; one try, no loop on 429) on 3-4 distinctive gloss phrases
plus one positive control; paste results. NOTES "BRANDT-MARGIN (9 Oct 2026)", gaps_check. 2 vision passes + CPU, ~$1.8.

## Wave 3 (04:5x UTC 9 Oct)
Hosts: archiv.sachsen.de ("sachsen") MANT-UNGL only (MANT-INV08 has released it; if MANT-INV08 posts a new take, wait for its release).
MANT-R07 disk only. V-MANT0136 (separate verifier) is spawned after MANT-R07's done line.

### MANT-R07 (Opus, cap 2.5, box 50 min, disk only): sachsstaatsarchiv-manteuffel-1712, 0136 r07/r08 faint gloss read blind
NOTES "MANT-0136 (9 Oct 2026, 04:17...)" "Worker eye (NOT scored...)": the worker saw faint period gloss letters under r07 (34..30) and under r08
16 31 13 that both blind passes missed. Steps: amendment PREREG-MANT-0136-A1.md (same statistic, control, seeds, gate as gate (a); only the input
widens to r07 + r08 positions 1-3) committed BEFORE any read. Cut tighter, higher-contrast crops of r07 and r08 from the committed f0136_09/crops
(local PIL/iiif_lines.py --image on the crop file; paste the command; commit the new crops), two blind Sonnet gloss passes that see only the
crop paths (no key, no prior gloss file, no worker-eye note), score each pass under gloss_gate.py extended to the widened span; regrade with
grade_0136.py (--check). Report old and new numbers side by side. No key.tsv change; 20/120/66 candidate values go to HYPOTHESES.md as rule-4
slots only. NOTES "MANT-R07 (9 Oct 2026)", gaps_check. 2 vision passes + CPU, ~$2.

### MANT-UNGL (Opus, cap 6, box 110 min): sachsstaatsarchiv-manteuffel-1712, 694/09 unglossed frames 0103, 0046, 0233 read under key.tsv
Handoff next 2; mant0609/rank_unglossed.tsv (0103 light ~20 tokens 4 runs; 0046 light ~8; 0233 same clerk hand as 0136, isolated codes). Method
exactly as MANT-0136 (PREREG-MANT-0136 design, f0136_09/ scripts): PREREG-MANT-UNGL.md committed BEFORE any score, with gate (b) per leaf AND
pooled (fr18 judge, permuted letter values, n >= 1000), and its power control re-run AT THESE LEAVES' N (subsample the 0085/0136 positive control to
each leaf's letter count -- CLAUDE.md rule 3 last paragraph: power shown at N=62 says nothing at N=8); a leaf whose N fails the power control is
"too-short", not a negative. Prior-work tool and checks 1-4 first (leaf + neighbours from the mant0609 inventories). "sachsen take", ONE GET per
frame (3), release; crops committed under f0103_09/, f0046_09/, f0233_09/; two blind Sonnet code passes per leaf (one call per leaf per pass;
0046 and 0233 may share a call if both are light), reconciliation one more unit; if a leaf shows any interlinear gloss, read it blind twice and
use it as gate (a) like 0136. Grades per token; check 5 (print_check.py) after decode. NOTES "MANT-UNGL (9 Oct 2026)", gaps_check. Units: ~5 vision
calls + 1 reconciliation (~1 each at these sizes) + CPU, ~$5. Report what was found and where it was not found; do not classify novelty.

### LAG-RESCORE (Opus, cap 3.5, box 70 min, CPU only): la-garde-1577, syllabary T re-score on the LAG-V2 spec + wordcode score-gap gate
NOTES "LAG-V2 (9 Oct 2026)" Verdict "cheapest next". (1) Syllabary: the PREREG-LAG-SYL statistic T re-scored on the revised spec (239 tok/48 types)
with the same family_run.py invocation, seeds, N, corpus; the control at the revised measured error (0.000/0.067 vs settles; also the one-reader
0.071) -- an Amendment to PREREG-LAG-SYL committed BEFORE the run. (2) Wordcode score-gap gate at err 0.071: PREREG-LAG-WC amendment (statistic =
target judge score minus the control's mean at the same N/err; gate stated before), committed BEFORE the run; check the control can differ from the
target on this statistic (rule 3). Note rule 3's third-attempt clause: if this is the third run of the same family with only one knob changed and it
fails, log the family "untested-by-this-tool at this N" and retire it, not a fourth tuning. HYPOTHESES rows with both numbers, NOTES "LAG-RESCORE
(9 Oct 2026)", Remaining gaps/Escalation, gaps_check. CPU, ~$2.5.
