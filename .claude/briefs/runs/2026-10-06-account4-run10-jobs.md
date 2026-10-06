# LANE LANE-RUN10-account-4 jobs (account 4) -- 6 Oct 2026 09:4x UTC, lane orchestrator session_019b5FtNbHb8pGgZbPaFv7QV

Lane brief: .claude/briefs/default-lane.md (cap 60, box 09:36-19:36 UTC 6 Oct). WORK-QUEUE row LANE-RUN10-account-4 (split s-z): RUN9's
named next steps for s-z first (STATUS.md "LANE LANE-RUN9-account-4 handoff", "Open for the next s-z lane" 1-4), then tools/next_steps.py
runnable rows and the `parallel` action of blocked rows, cost band S and M, folders s-z only. The row's other examples (clinton, suriname,
decode-2678, eckert) are outside s-z; the manteuffel verifier on R9-MANTPC is already done (R9-MANTV, ROOM 07:05). Gate 0a: no
SESSION-SWEEP-account-4 row. VERIFY-BACKLOG.tsv: no s-z row. Off limits: Birago, Armstrong, Debosnys; bne20211-ferdinand-1478 and
destaing-gerard-1779 (account-4 standing session); anything in a private repository.
Every worker: one job, then stop. Each job first checks its named step is still undone (NEXT-STEPS.tsv lags the folders): if a dated NOTES.md
section already ran it, take the folder's own Verdict "cheapest next" instead if it fits this job's cap and box and is not a machine
transcription pass the TRANSCRIPTION.md / CLAUDE.md Usage 6 sorter rule hands to the owner; otherwise stop and report.

Every worker: one job, then stop. Each job first checks its named step is still undone (NEXT-STEPS.tsv lags the folders): if a dated NOTES.md
section already ran it, take the folder's own Verdict "cheapest next" instead if it fits this job's cap and box and is not a machine
transcription pass the TRANSCRIPTION.md / CLAUDE.md Usage 6 sorter rule hands to the owner; otherwise stop and report.

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim
  line with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE LANE-RUN10-account-4".
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
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE LANE-RUN10-account-4",
  then a five-line final report.


## Wave 1 (spawned 09:4x UTC 6 Oct). Intake gate output (09:39 UTC) pasted per job.

### R10-WVOTX -- wvo-hessen-1564 f.23, careful two-pass transcription of the ten German gloss rows (Opus; cap 6, box 80 min)
Intake gate: `wvo-hessen-1564: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
RUN9 named step 1 / folder Verdict "else" branch: the ten gloss rows of f.23 (crops_m/ German rows; R9-WVOALIGN's gloss was a reconciliation
sketch, C03/C05/C09 uncertain). Units: 2 blind Sonnet passes (one call per pass over the ten gloss-row crops only, never the full leaf; crop
step pasted -- re-cut with tools/iiif_lines.py --image if crops_m/ rows are over 2500 px) + 1 reconciliation by you against the crops = 3 units
x ~1.5. Then re-run build_pairs.py and the aligner as R9-WVOALIGN did (its PREREG gate unchanged; report pile ids vs row-shuffle p95 again)
and rebuild r9align key/decode; report C/M changes. Do NOT touch the owner's f.23 sorter or apply sorter answers (separate step). The reading
changes after AUDIT.md: say so in NOTES.md and flag a verifier in ROOM. Update Remaining gaps / Escalation; gaps_check.py pass.

### R10-WVOREPLY -- wvo-hessen-1564, WVO search for Wilhelm of Hesse -> Orange letters Oct-Dec 1564 (Sonnet; cap 1.5, box 30 min)
Folder `parallel` action. Huygens WVO (host table row: `wvo/app/brieven?...`, >= 2 s apart, descriptive UA, <= 25 requests): list letters
Hessen -> Oranje (and Oranje -> Hessen) Oct 1564-Mar 1565; for each, the detail page `brief?nr=` opmerkingen field (cipher? printed where?
digitised scans?). Write a dated "## R10-WVOREPLY" NOTES.md section: table of letters found, which paraphrase or reply to 1109 (18 Sept
1564), which carry cipher, and where scans are. Search results only: no decode, no transcription, no status change.

### R10-SIENA7C -- siena-concistoro-2308 no. 7, arbitrate J/B splits on the other nine lines (Opus; cap 3, box 50 min; disk only)
Intake gate: `siena-concistoro-2308: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
RUN9 named step 2 (R9-SIENA7B "Next step"): arbitrate the ~66 J/B split spots on L02, L04-L07, L09-L11 (L12 is cut by the crop edge: re-cut it
first from the image on disk if possible, else exclude and say so) on autocontrast 2x zooms exactly as R9-SIENA7B did for L03/L08, worker
only, no subagent; extend transcripts/no07_arbitration_R9-SIENA7B.tsv into a new R10 file. Report agent J's error over all arbitrated tokens
with Clopper-Pearson 95% bounds and say whether it is under R9-SIENA7's ~10% control crossover (i.e. whether the R9-SIENA7 negative stands
as control-backed on the whole letter). Write "## R10-SIENA7C" in NOTES.md and HYPOTHESES.md row note. No fit, no key.

### R10-SIENA15 -- siena-concistoro-2308 no. 15, R4765 key-sheet shape pass (Opus; cap 3.5, box 60 min)
Intake gate: as R10-SIENA7C. RUN9 named step 2b (R9-SIENA15 "Next step for no. 15"): one DECODE login (tools/decode_browser_login.js; scrub
the account name; images in scratchpad unless committing a key-sheet crop the folder needs) to look over R4765 and the other 1540s orator keys
of fasc. 1 for a sheet carrying the ◎, ⊔, barred-x and R families no. 15 uses. Pre-register the shape-presence criterion before looking
(PREREG file pushed). If one has them, record the sheet and its alphabet rows (crop step pasted) and name the next test; if none, no. 15
goes too-short / no-key-material in Remaining gaps. Write only "## R10-SIENA15" (do not overlap R10-SIENA7C's no. 7 files).

### R10-MANT526 -- sachsstaatsarchiv-manteuffel-1712, 0527 run-7 zoom + glossed frame 0526 transcription (Opus; cap 6.5, box 85 min)
Intake gate: `sachsstaatsarchiv-manteuffel-1712: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
RUN9 named step 3. (a) First, ~0.5: the 0527 run 7 code over "Ilgen" -- 898 or 98? one zoom by you (crop pasted); record it. (b) Frame 0526:
2 blind Sonnet passes (one call per pass, line crops via tools/iiif_lines.py --image, never the full frame) + 1 reconciliation = 3 units x
~1.5, then the per-leaf single-code gate as GAPS195 ran it for 0528 (prereg first) for 898/939/867. Codes that pass go in key.tsv at M only;
decode_key.py --check exit 0; reading change after AUDIT.md -> NOTES.md + ROOM verifier flag. 714/515 conflicts: leave to HYPOTHESES.md,
do not resolve by majority (rule 4). Update Remaining gaps / Escalation; gaps_check.py pass.

### R10-ZESBASIN -- zeschau-seebach-1841, basin-width diagnostic of the word-parse objective (Opus; cap 3, box 55 min; disk only)
Intake gate: `zeschau-seebach-1841: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
RUN9 named step 4. R9-ZESCH/ZESCH2 found the true key scores highest (J 1181.7) yet local search never reaches it (control 0.0026, 0.0146 vs
gate 0.60): the instrument is retired for local search (rule 3 third-attempt clause). This job is NOT a further search: it measures the
objective's landscape on the matched control only -- perturb the true control key by k random swaps (k = 1, 2, 4, 8, 16, 32; >= 50 draws each)
and report J vs k and the fraction of k-neighbours a single greedy pass returns to the true key. Pre-register what width would justify a
different instrument (e.g. a crib-seeded or exhaustive-near-key method) vs retiring the objective at this N. Write "## R10-ZESBASIN" and a
HYPOTHESES.md row; no target run.

### R10-SRCH -- s-z printed-source / catalogue greps (Sonnet; cap 2.5, box 50 min; archive.org / be-api / TNA Discovery API only)
Each folder's own `parallel` action; check NOTES.md first that it was not already run; write a dated "## R10-SRCH" section per folder
(searched, ids, quoted hits, "not found in <source>, searched by <method> on 6 Oct 2026"): (1) wallis-emus203-undeciphered: grep Thurloe vols
2-5 djvu text (collectionofstat02thur..05thur) for "Brasset", "Buckingham", "Townesend" and the Scotland 1651 window; (2) sp53-22-f52: re-read
Tomokiyo's live unsolved.htm and mary.htm entries for f.52 against the 24 Sept snapshots on disk (sources/cryptiana/; diff only, do not edit
sources/; an image reference like 092.jpg/093.jpg?); (3) sp77-nicholas-1659: grep CSPD 1659-60 and Cal. Clar. iv indexes (IA) for royalist
aliases/agents at St Sebastian, Aug 1659; (4) sp54-maclean-1745: TNA Discovery item-level description of SP 54/25/5 (tools/discovery_items.py).
Search results only; no decode; no status change.

## Wave 2 (spawned 10:0x UTC 6 Oct)

### R10-WVOV -- VERIFIER wvo-hessen-1564 f.23, audit 2 after R10-WVOTX (Opus; cap 3.5, box 60 min)
CLAUDE.md "Verifier brief (template)", steps 1-5, on the revised reading: R10-WVOTX (ROOM 09:54/09:55; r10tx/, gloss_r10.tsv, rebuilt key 16 C / 12 M,
decode C 142 M 115 of 257; k28 a -> b at C). First confirm R10-WVOTX's commits are on origin/main (its session may still be pushing; if not
there, wait 5 min once, then proceed with what is there and say so). Re-run its alignment and decode from the committed files (byte-identical?),
check the PREREG predates the scored run, check the control can vary on the statistic, re-check 5+ random C tiles against the gloss on the
image, then revise AUDIT.md (audit 2; N-class with the novelty search delta only, key source, depth D0-D4 with %), status.json depth fields,
and any SECOND-OPINIONS-QUEUE row (rule 10 propagation). You are not the solver: do not protect R10-WVOTX's reading.

### R10-MANTSCR -- sachsstaatsarchiv-manteuffel-1712, 867 normalisation rule + eye screen for single-code 898/939 (Opus; cap 3, box 50 min)
Folder Verdict "cheapest next" (R10-MANT526): (a) pre-register (PREREG pushed first) a spelling-variant normalisation rule general enough to
apply to every gloss in the pool, not only 867 (feld mareschal / Feldmarechal), re-run the pooled single-code gate with it and report whether
867 licenses at M and what else moves (sensitivity: do any previously licensed codes change?); (b) disk-only eye screen of the remaining
N9-MANT2 glossed frames (0514 0517 0518 0520 0521 0523 0532 0533 0535 0539 0541 0542 0544 0548; reduced frames, one look each, no
transcription) for single-code 898/939 or f.410 U codes; rank them; name the next frame to transcribe. key.tsv at M only; decode --check.

### R10-WVHMIN -- willem-van-hessen-1567, Marburg minuut clear-text transcription as crib (Opus; cap 6, box 80 min)
Folder `parallel` action: transcribe the Marburg minuut's clear text (WVO 01127.pdf pp.2-4, about 75 lines; on disk? else one WVO fetch) --
line crops via tools/iiif_lines.py --image (pasted), 2 blind Sonnet passes (one call per page per pass: 3 pages x 2 = 6 calls ~1.5 each is
over cap -- so one call per pass over all ~75 line crops if under ~80 crops, else pages 2-3 only and say so) + your reconciliation. Output a
normalised line-numbered TSV usable as a crib for the KHA original when it arrives; note any words the minuut marks for enciphering (underlining,
marginal signs). No cipher work; status stays as the folder says. Note R9-WVOX: wvo-hessen-1564 f.23 shares a key family with this folder's 1069
key -- record that cross-reference in NOTES.md, nothing more.

### R10-SIENA4777 -- siena-concistoro-2308 no. 15 vs R4777 nomenclator (Opus; cap 3, box 50 min)
R10-SIENA15's optional next: R4777 (1540s imperial-court nomenclator) partial overlap 2/4 with no. 15's sign families. Pre-register first
(PREREG pushed): shape concordance of no. 15's signs vs R4777's alphabet rows, statistic and permutation control exactly as R9-SIENA15's S2
gate. One DECODE login if the R4777 image is not on disk (scratchpad). If PASS, apply R4777's values to no. 15 at M and judge; if FAIL,
no. 15 stays too-short / no-key-material. "## R10-SIENA4777" only.

### R10-SRCH2 -- s-z catalogue / print lookups (Sonnet; cap 2.5, box 50 min)
As R10-SRCH (check each folder's NOTES.md first; R10-SRCH found all four of its items already run -- skip any already-done item quickly and
take the next): (1) taurello-roma-1527: map Sanuto vol. 46's archive.org identifier and read vol. XLII's Taurello entries named in NOTES;
(2) salvago-caraffa-1691: full-text search of Atti della Società Ligure di Storia Patria for "Caraffa" 1691 / Coisis / Coissy; (3) vanspaen-
vandergoes-1808: grep the public EAD of the NA Kabinet des Konings 1806-1810 for code books / sleutel / cijfer; (4) sp8-ehrenstein-1689: read
the remaining 29 rows of the Arcinsys Bernstorff 1688-1690 list; (5) sp78-france-1583: Discovery details of SP 78/113/56, /58 and SP 78/111/92,
/94. Search results only.

## Wave 3 (spawned 10:2x UTC 6 Oct)

### R10-MANT521 -- sachsstaatsarchiv-manteuffel-1712, glossed frame 0521 transcription + gates (Opus; cap 6, box 80 min)
R10-MANTSCR's named next frame (0521, then 0518). Same shape as R10-MANT526: 2 blind Sonnet passes (one call per pass, line crops via
tools/iiif_lines.py --image, pasted; never the full frame) + 1 reconciliation = 3 units x ~1.5; PREREG pushed first; per-leaf single-code gate
as GAPS195 / R10-MANT526, then the pooled gate with the leaf added (R10-MANTSCR's spelling rule as registered). Codes licensed go into key.tsv
at M only; decode_key.py --check exit 0; a reading change after AUDIT.md -> NOTES.md + ROOM verifier flag. Do not start 0518 unless 0521 is
done under 60% of cap and box. Remaining gaps / Escalation; gaps_check.py pass.

### R10-SIENA7N -- siena-concistoro-2308 no. 7, homophonic + nomenclator family with matched control (Opus; cap 5, box 75 min; disk only)
R9-SIENA7's named next, now licensed: R10-SIENA7C put agent J's error at 0.8-6.6% on the whole letter (under the ~10% crossover). Family: the
anchored homophonic fit (R9-SIENA7's solver, 7 C anchors fixed) extended with a nomenclator layer (a small set of multi-sign or single-sign
codes standing for frequent Italian words/names, Bourdeau's R4750 Latin-word nomenclator as the design reference). Rule 3 in order, via
tools/family_run.py if it can express this (else extend it with an option, Usage 8): matched control first -- synthetic 1420s Italian plaintext,
N=363, K=45, same anchor count, a nomenclator of the size you register, injected sign error at J's measured rate (bracket it: 0%, 3.5%, 7%) --
gate pre-registered (PREREG pushed before scoring). Control below gate -> "non-test at this N", stop. Else run the target, judge the candidate
(tools/judge_plaintext.py, say whether the Italian corpus is era-matched) and the shuffled-target decode through the same judge (ARM-C1).
No key.tsv beyond M without a verifier. HYPOTHESES.md row with both numbers. Status stays `open` unless rule 5 says otherwise.

## Wave 4 (spawned 10:4x UTC 6 Oct; last wave)

### R10-MANT518 -- sachsstaatsarchiv-manteuffel-1712, glossed frame 0518 (Opus; cap 5, box 70 min)
Exactly as R10-MANT521, for frame 0518 (R10-MANTSCR's second-ranked frame): 2 blind passes + reconciliation on line crops (pasted), PREREG
first, per-leaf gate, pooled SP gate with the leaf added. key.tsv at M only; decode --check; verifier flag on any reading change.

### R10-ZESCRIB -- zeschau-seebach-1841, crib-drag of French diplomatic formulae for a near-exact seed (Opus; cap 3.5, box 55 min; disk only)
R10-ZESBASIN's named next: the word-parse objective ranks the true key first but has no basin, so search needs a seed within ~1 swap. A
different instrument (rule 3 third-attempt clause: not local search on the same objective): drag a short list of pre-registered French
dispatch formulae (salutation/closing/date formulae of 1840s Saxon diplomatic French; list fixed in PREREG before scoring) along the pooled
R5005-R5008 digits under Bourdeau's 7 grade-I values; score each placement by consistency with the syllabary's known values and by the
objective. Matched control first: the same crib-drag on the synthetic control with its true key hidden -- does a correct placement rank in the
top k, and does seeding from it reach the true key? Gate pre-registered; control below gate -> non-test, target not run. HYPOTHESES.md row,
"## R10-ZESCRIB", gaps_check pass. No key beyond M.
