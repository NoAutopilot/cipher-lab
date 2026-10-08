# LANE FAMILY jobs (account 2, incarnation DEFAULT-account-2-20261008-1613) -- 8 Oct 2026 16:2x UTC, lane orchestrator session_01XR227ra6tFXMey23e7ENgo

Lane brief: .claude/briefs/lane-family.md (+ lane-common-blast.md). Cap 60, box 16:14 UTC 8 Oct - 02:14 UTC 9 Oct. First incarnation:
no earlier "LANE FAMILY handoff" in STATUS.md; started from LANE DEFAULT-account-2-20261008-0710's handoff and next_steps.py --hot-only.
Gate 0a clear (SESSION-SWEEP-account-2 done 5 Oct per that handoff). Exclusions: eckert-* (Huntington ledgers, other lanes), Gallica
fetches, Birago/Armstrong/Debosnys, every folder with a ROOM claim < 6 h and no done line.
Register rows re-checked by the orchestrator before briefing (prior-work check 1): STALE and dropped -- wvo-11008-certain-1572 (read and
audited 7 Oct), antt-msliv0638 m0200/m0277 (done 8 Oct), wallis-emus203 Thurloe grep (R8-SPLOOK 6 Oct), heinsius-vanhaersolte small_runs
(D2-HEIN 8 Oct), na-suriname inv. 373 (done 6 Oct). `tools/prior_work.py` does not exist yet: every job runs prior-work-step.md by hand.

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim line
  with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE FAMILY (account 2)". If --start fails to push
  from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
- Prior work (`.claude/briefs/prior-work-step.md`): run checks 1-4 by hand and paste one line per check (route, query, result) into your
  NOTES.md section BEFORE the first priced step; check 5 after any decode. A check that did not run is "unchecked". If check 1 shows the
  step already done, write one ROOM line saying so and stop.
- Read the folder's NOTES.md tail (Remaining gaps / Escalation / latest dated sections), HYPOTHESES.md and AUDIT.md section list first.
- Good-citizen rule and the CLAUDE.md host table for every request (one request per host at a time, >= 1.5 s apart; stop a host on
  429/403/challenge, one retry after a pause at most). Report request counts per host. Prefer files already on disk. No Gallica.
- Rule 3 (matched control first; a control that cannot differ from the target on the statistic is a non-test), rule 4 grading, rule 7
  (`--check` scripts). Pre-register any new gate in a PREREG-<JOB>.md pushed before the score is computed.
- Rebase before writing shared files; keep both facts on conflict. Commit only your own paths. Run
  `python3 tools/file_shrink_guard.py <every file you touched>` before the final push; push with `python3 tools/room.py --push <paths>`.
- Partial targets: update "## Remaining gaps" / "## Escalation" (Verdict line) and pass `python3 tools/gaps_check.py <target>`.
- Words: never "solved", "cracked", "novel", "first", "new" for anything this project did; rule 10 wording only. Never name the owner; never
  print credentials. Never call AskUserQuestion. Solver jobs: report what was found and where it was not found; do not classify novelty.
- Stop at the cap or at 80% of the box, whichever first; do not start a unit that would cross 80% of either. Opus session floor ~1.5.
- Vision work: crop step mandatory and pasted (`tools/iiif_lines.py --image FILE --out DIR ...`); line or strip crops only, never a full
  page image to a subagent; one page (or half page) per subagent call; ~1.5 per vision call, reconciliation one more unit.
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE FAMILY (account 2)",
  then a five-line final report.

## Wave 1 (16:2x UTC 8 Oct)
Intake gate 16:2x UTC (tools/intake_gate_check.py, each exit 0):
`sachsstaatsarchiv-manteuffel-1712: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`;
`heinsius-hermitage-1704: open (line 1) -- edition/page or full-text-search citation found within 6 lines`;
`wvo-hessen-1564: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.

### FAM-MANT15 (Opus, cap 9, box 150 min): sachsstaatsarchiv-manteuffel-1712, unglossed 694/09 frames 0015+0016, then 0052
The named next read of MANT-0609 (NOTES.md "MANT-0609" section, rank table): 694/09 0015 + 0016 (f.8 and verso, Jan 1713, ~70 code
tokens, eye-read Krauske coverage 0.98). Units: fetch the two frames once (www.archiv.sachsen.de, frames.tsv URLs, images/manifest.json);
`tools/iiif_lines.py --image` line crops; 2 blind Sonnet passes + 1 reconciliation (3 units ~4.5); `tools/decode_key.py` with key.tsv
(ciphertext rows for these frames in the folder's convention), grade per token; judge (`tools/judge_plaintext.py` with the spec's corpus --
check the spec's language/era first) WITH a shuffled-key control on the same tokens (does the real key beat shuffled keys on the 4-gram
score?). Prior-work check 2 matters here: look at 0014 and 0017 and the frames either side for a clear copy or a gloss; check 4: Krauske
1893 and NASG vols 14-19 (already grepped by A2-SAX) for this Jan 1713 report by date. Then, only if under 50% of cap and box: 694/09 0052
(one 32-group run, same pipeline, ~2.5). Write a dated NOTES section, Remaining gaps / Escalation, PROGRESS/status only as rule 5 allows.

### FAM-HERM (Sonnet, cap 3, box 60 min): heinsius-hermitage-1704, list every deciphered l'Hermitage letter in Heinsius Deel 10-19
The named next step of D2-HERM (NOTES.md tail): read the candidate pages that carry the "aan d'Alonne, die de gespatieerd gezette
gedeelten uit het cijfer heeft opgelost" formula (Deel 11 pp.202, 288, 433, 505; Deel 12 pp.400, 405; Deel 13 pp.299, 354; Deel 14 p.143;
Deel 15 p.13; Deel 16 pp.9, 112, 151, 317, 325, 414, 433; Deel 17 p.647; Deel 19 pp.240, 261, 360, 371, 377), one pages.json per volume +
one OCR page each (about 30 requests, resources.huygens.knaw.nl, >= 2.1 s apart, descriptive UA), and table each: letter no., writer,
place, date, H.A. number, footnote text quoted, which passages are spaced (deciphered). Output `deciphered_letters.tsv` and a dated NOTES
section; then say which H.A. volumes (earliest first) an archive order should add beside 946/1034/2317 so a key comparison with the 1704
letter becomes possible, and update REQUEST.md's list only (no ASKS row). No decoding. Positive control: Deel 10 p.528 (no. 1066) read by
the same route must show the formula.

### FAM-WVOH (Opus, cap 3, box 60 min): wvo-hessen-1564, reference-strip blind eye read of the 33 C tiles
The named next step (NOTES.md "Remaining gaps", D2-WVO/D4-WVO): one blind read of the 33 conflict/unaligned C tiles with a letter-form
reference strip (the k22 looped d in "worden"/"vnd" beside the k19 g in "nungen", plus h, i, s exemplars) and 10 fresh decoys, the same
PREREG gate as D2-WVO (pre-register in PREREG-FAM-WVOH.md before reading; decoys drawn from tiles whose letter is known, never shown
which); fold k11 "taush" (C07 idx 14) and C03 "voans sp" into the same read. Disk only, no host. This is a key-correction step on a
glossed leaf (known-text share): if the decoy gate fails again, log the instrument "[retired]" for this step per rule 3's third-attempt
clause only if it is the third attempt -- count the attempts in NOTES first.

### FAM-POOL (Opus, cap 4, box 75 min): pools and design priors for the next waves (supply c and d of lane-family.md), no reading
Disk only (plus at most 20 catalogue requests per host, one host at a time, if a row needs one count). (1) From KEY-OFFICES.tsv and
KEY-DESIGN.tsv, list every office/key family in this lane's scope (Dutch, German, Iberian, British/Irish, DECODE/Scandinavian, BnF with
images on disk) whose key is in hand AND which has letters on the same host not yet read (grep ciphers/*/NOTES.md, SIBLINGS-2026-10-08.tsv,
sources/wvo, sources/huygens, sources/decode listings, frame inventories). For each: the unread letters (shelfmark/record id), sign count
estimate, images on disk or host route, and the prior-work check 1 result per letter (our own work: grep the id in ciphers/, ROOM.md last
1,500 lines, WORK-QUEUE.tsv). (2) Run `python3 tools/design_prior.py` on the top unread letters that have no key in hand. (3) Rank by
expected value (P(first cheap test moves it) x value / cost; pools of 2,000+ signs and keys in hand first; BnF-on-disk wins ties). Write
`research/FAMILY-POOLS-2026-10-08.md` (table + the top 6 with a one-paragraph next step each, cost band, and whether a check-solved is owed
-- run `tools/intake_gate_check.py` on each existing folder and paste the line). Push; ROOM done line names the top 3.

Spawned 16:21 UTC: FAM-MANT15 session_01KPBKpmZqWfbkT1aviBKAhy (Opus), FAM-HERM session_012WzDikiwfPBMe8fx6Rb8MR (Sonnet), FAM-WVOH
session_01VJrv6UnrkT7hdhqsD4jAxg (Opus), FAM-POOL session_017eSeTNe93RXnLzuWvfzzwx (Opus). Wave 2 is drawn from FAM-POOL's ranked list.
