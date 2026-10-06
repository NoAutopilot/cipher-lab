# LANE LANE-RUN12-account-4 jobs (account 4) -- 6 Oct 2026 15:5x UTC, lane orchestrator session_015RRYU6gqkKX94u2a6B7hh4

Lane brief: .claude/briefs/default-lane.md (cap 60, box 15:35 UTC 6 Oct - 01:35 UTC 7 Oct). WORK-QUEUE row LANE-RUN12-account-4 (split s-z,
then any a-h row the live account-1 lane LANE-RUN11-account-1 has not claimed in ROOM.md). Gate 0a: no SESSION-SWEEP-account-4 row.
Verifier flags: manteuffel needs no carry-over (867 le Feldmarechal is not in the audited ciphertext; decode --check C 202 M 98 U 123 matches
R9-MANTV); august-van-saksen carried by R11A-AVSV; lodewijk held by RUN14-account-2. VERIFY-BACKLOG.tsv: high rows are fr16142 Noailles
(a-h, worked by account 1 today), others Birago (off limits) or nla-heinrich (i-r, account 2). s-z: RUN11-account-4 found the runnable rows
spent; only manteuffel's untried sibling-series step remains. a-h rows below had no ROOM.md line in the last 900 lines at 15:4x UTC.
Gallica: manifest probe 15:4x UTC timed out (000) -- jobs below do not depend on Gallica; any job that finds it needs Gallica stops and says so.
Off limits: Birago, Armstrong, Debosnys; anything in a private repository.
Every worker: one job, then stop. Each job first checks its named step is still undone (NEXT-STEPS.tsv lags the folders): if a dated NOTES.md
section already ran it, take the folder's own Verdict "cheapest next" instead if it fits this job's cap and box and is not a machine
transcription pass the TRANSCRIPTION.md / CLAUDE.md Usage 6 sorter rule hands to the owner; otherwise stop and report.

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim
  line with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE LANE-RUN12-account-4".
  If --start fails to push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
- Read the folder's NOTES.md tail (Remaining gaps / Escalation / latest dated sections), HYPOTHESES.md and AUDIT.md section list first.
- Good-citizen rule and the CLAUDE.md host table for every request (one request per host at a time, >= 1.5 s apart; stop a host on
  429/403/challenge, one retry after a pause at most). Report request counts per host.
- Rule 3: any gate is pre-registered (a PREREG file committed and pushed before the scored run), with a matched control that can vary on
  the statistic tested (same N, symbol count, design, language, era); report both numbers. Rule 4 grades with counts. Rule 7:
  `tools/decode_key.py <folder> --check` (or the folder's own decode script --check) exit 0 before push if the reading or key changed. A
  reading change after AUDIT.md: say so in NOTES.md and flag in ROOM for a verifier.
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
- No private-repository access in these sessions: if a step needs one, stop and say so in ROOM.
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE LANE-RUN12-account-4",
  then a five-line final report.

## Wave 1 (spawned 15:5x UTC 6 Oct). Intake gate output (15:4x UTC) pasted per job.

### R12D-MANTSIB -- sachsstaatsarchiv-manteuffel-1712, sibling series Loc. 694/03, /04, /06 opened (Opus; cap 3.5, box 60 min)
Intake gate: `sachsstaatsarchiv-manteuffel-1712: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Escalation item "[ ] siblings: Loc. 694/03, /04, /06 (1706-10, same Manteuffel series) carry digitisat links; not opened" (NOTES.md ~l.356,
l.1389). Open each sibling's digitisat (the same Sächsisches Staatsarchiv viewer/route the 694/08-09 frames.tsv used; record frame counts in
images/<loc>/frames.tsv, fetch once), then a stride sample of frames per sibling (stride sized to fit the box; thumbnails by script, a
vision unit only on candidates) to inventory frames with code groups, and among them the *glossed* ones (interlinear period decipherment)
and the code range (letter range vs nomenclator range >400). Goal: find glossed nomenclator-range leaves that could license the 49 M / 23 U
codes of f.410 under the per-unit merge rule. No transcription in this job; write an inventory TSV + NOTES section + updated Escalation.
Units: ~4 sibling listings + ~3 vision units at ~1.5 = cap 3.5.

### R12D-GRA -- fr2980-gramont, settle f.18r L11-L21 z/zb and d/n6 split slots by eye and re-score (Opus; cap 3, box 50 min)
Intake gate: `fr2980-gramont: partial (line 3) -- edition/page or full-text-search citation found within 6 lines`.
Verdict cheapest next (N9-GRA4, 5 Oct): settle the 16 z/zb and 11 d/n6 split slots of fr.3040 f.18r L11-L21 by eye and re-score against
Le Grand III under N9-GRA4's gate. Crops must be on disk (Gallica is down): if they are not, stop and report. Pre-register the re-score (same
gate, same control as N9-GRA4) before settling; settle each slot from per-slot crops (one subagent call per line's slots, crop paths only,
blind to the Le Grand text), then re-score. Key/reading change -> decode --check, NOTES, ROOM verifier flag. BnF item.
Units: ~11 lines grouped into ~3 calls at ~1.5 => cap 3 tight; stop before a unit that crosses 80%.

### R12D-VILL -- fr7129-villeroy-bongars-1604, f.268 decode restricted to key v3's high-confidence cells (Opus; cap 2.5, box 45 min)
Intake gate: `fr7129-villeroy-bongars-1604: blocked (line 3) -- already terminal, nothing to gate` (status blocked; this is the folder's own
"While waiting" step 2, which waits on nobody; f.260 at full size is not on disk and Gallica is down, so step 1 is not this job).
Decode f.268 (images/keys/ native captures on disk; use the existing transcription if one is committed, else stop -- no new machine
transcription pass) with only key v3's cells attested 2+ times / confirmed (the NOTES list: s=i, p=i, o=e, r=e, m=u, b=u, e=p, 26=en ...),
everything else `[MARK]`. Grade per rule 4 with counts; judge per rule 7 (`tools/judge_plaintext.py` with an era-matched French corpus if one
exists, plus shuffled-key controls at the same coverage). Report the reading honestly graded; do not change status unless rule 5 allows.
Disk only. Units: 1 script + 1 judge run => cap 2.5.

### R12D-FAIR -- fair-game-2010, crib/word-constrained solve with matched control at N=67 (Opus; cap 3, box 50 min)
Intake gate: `fair-game-2010: open (line 3) -- edition/page or full-text-search citation found within 6 lines`.
NOTES next (rule 3 third-attempt clause: a different instrument, not more anneal restarts). Reconcile first which ciphertext (spec vs
Rossignol vs image order, NOTES l.102) is used, and say so. Instrument: a word/crib-constrained search (dictionary-constrained or crib
"Democracy only works if you do your part" family placements, NOTES l.86) under the marker-scheme hypothesis the folder names. Do not copy
code from aaymeloglu/unsolved-ciphers (no licence): cite it and write our own. Matched control: synthetic English text of N=67 under the
same scheme, seeds >=3, gate pre-registered; target only if the control clears (family_run.py discipline; HYPOTHESES.md both numbers).
Disk only. Cap 3.

### R12D-ERBA -- erba-2006, spec test 2 (re-segmentation word-length profile with controls) (Opus; cap 2, box 40 min)
Intake gate: `erba-2006: open (line 3) -- edition/page or full-text-search citation found within 6 lines`.
specs/erba-2006.json cheap_tests_in_order[1]: re-segment the confirmed digraph sequence on `xs` and compare its word-length profile with an
unsegmented and a randomly segmented control (and an Italian-text control under the same digraph design at the same N, era-matched corpus
from tools/data if one exists). Pre-register the statistic and gate. Write both numbers into the spec's cheap_test_done and NOTES.md.
Disk only. Cap 2.

### R12D-CYLOB -- cylob-c1995, Rotering 2015 partial transcription -> ciphertext.tsv + one grid-page image check (Opus; cap 2.5, box 45 min)
Intake gate: `cylob-c1995: open (line 3) -- edition/page or full-text-search citation found within 6 lines`.
NOTES next: fetch Rotering's 2015 PDF again (NOTES l.104 gives its sha256; one request to the share named there; if it no longer answers,
stop and log), turn its transcribed pages into ciphertext.tsv (source and date in the header, transcription conventions recorded), and check
one grid page against the scan on disk (rule 2; crop step mandatory, one vision unit). No solve in this job. Credit Rotering (rule 8).
Units: 1 fetch + script + 1 vision unit => cap 2.5.

## Wave 2 (spawned 16:0x UTC 6 Oct). Intake gate output (16:0x UTC) pasted per job. Gallica still unprobed-green: no job depends on it.

### R12D-HDKV -- hessen-daenemark-1672, rule-7 fresh re-derivation + clear-pages question (VERIFIER, Opus; cap 3, box 50 min)
Intake gate: `hessen-daenemark-1672: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Verdict cheapest next (GAPS199): a separate verifier re-derivation of the reading (rule 7: from the spec/ciphertext and key only,
`tools/decode_key.py ciphers/hessen-daenemark-1672 --check`, plus an independent re-derivation script or decode.json run in a scratch copy;
report any token that differs beyond the M-graded ones), then the clear-pages question: is the interlinear/margin glossing hand period or
modern (ink, hand, spelling against the dated 1672 text; the same method as manteuffel GAPS158, grade M, say what was compared). You are a
verifier, not a solver: do not decode beyond the key, do not change key values. Write a dated AUDIT.md section (re-derivation result, hand
verdict, depth per rule 4a with `tools/depth_check.py` if the result changes anything) and update status.json depth fields only if your
re-grade changes them. Disk only unless an image is missing. Units: 1 script + 1-2 vision units at ~1.5 => cap 3.

### R12D-GOLD -- goldbar-1933, premise-check read of the Bin Tao v. Citibank docket (Opus; cap 1.8, box 30 min)
Intake gate: `goldbar-1933: open (line 3) -- edition/page or full-text-search citation found within 6 lines`.
NO-CRACKS next (NOTES l.123): read the docket (dockets.justia.com, 9th Cir. 09-56992, from Kim's comment 15) for any reading of the bars the
claimant filed. Fetch once (descriptive UA, or browser tool if challenged; one retry max), record what the docket lists and whether any filed
document carries a reading; do not purchase PACER documents. Report found / not found with the URLs. Status unchanged unless rule 5 allows.

### R12D-GRAZB -- fr2980-gramont, blind f.30 zb vs fr.3040 barred-z sort (Opus; cap 3, box 50 min)
Intake gate: `fr2980-gramont: partial (line 3) -- edition/page or full-text-search citation found within 6 lines`.
R12D-GRA's named next (NOTES latest section): zb -> R in 25/27 fr.3040 occurrences while key.tsv has zb NULL. Pre-register a blind shape
sort: mixed per-token crops of f.30 zb, fr.3040 barred z (K2) and plain z, shuffled, one Sonnet subagent call (crop paths only, labels
hidden), plus a decoy-control set of known-distinct signs; gate = sort recovers the decoys and states whether f.30 zb and fr.3040 barred z
are one sign. Crops must come from images on disk (Gallica is down): if a needed leaf is not on disk, stop and report. Key change only if
the gate licenses it (then decode --check, NOTES, ROOM verifier flag). BnF item. Units: crop script + 1 sort call + reconciliation => cap 3.

### R12D-CYL3 -- cylob-c1995, spec cheap test 3 (fixed discrete alphabet structural check) with matched control (Opus; cap 2.5, box 45 min)
Intake gate: `cylob-c1995: open (line 3) -- edition/page or full-text-search citation found within 6 lines`.
specs/cylob-c1995.json cheap_tests_in_order[2] on R12D-CYLOB's ciphertext.tsv (190 rows / 167 signs, Rotering pp.1-20). Pre-register the
statistic (e.g. sign-inventory growth curve / type-token saturation and repeat structure vs (a) a synthetic English text enciphered with a
fixed homophonic alphabet of the same inventory size and N, (b) a random/no-alphabet null at the same N); gate pre-registered; both numbers
in the spec's cheap_test_done and NOTES.md; test 4 only if a later worker is briefed. Disk only. Cap 2.5.

### R12D-ERBA3 -- erba-2006, modern Italian corpus (era-matched) + spec test 3 letter-like design (Opus; cap 3, box 55 min)
Intake gate: `erba-2006: open (line 3) -- edition/page or full-text-search citation found within 6 lines`.
R12D-ERBA found the it19 corpus is the wrong era for a 2006 note. Step 1 (~12 min, V6-PTCORP pattern): build tools/data/<it-modern> from
public-domain/openly licensed late-20th-century Italian prose (record sources + licence in a README; LOFO per-fold false-negative spread per
rule 3 if a judge is used). Step 2: specs/erba-2006.json test 3 (letter-like design) with its control drawn from the new corpus at the same
N and design, pre-registered; rerun test 2's design-L statistic on the new corpus control too and report whether the era caveat moves it.
Both numbers into cheap_test_done. Shared asset: name the corpus in SYSTEM.md (tools/system_map_check.py). Cap 3.
