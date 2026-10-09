# LANE FAMILY jobs (account 2, incarnation DEFAULT-account-2-20261009-1310, "FAMILY-A2i") -- 9 Oct 2026 13:2x UTC, lane orchestrator session_01Xvms7TJ6c589BD817Fkatp

Lane brief: .claude/briefs/lane-family.md (+ lane-common-blast.md). Cap 60, box 13:10-23:10 UTC 9 Oct. Ninth incarnation: started from
STATUS.md "LANE FAMILY handoff (incarnation DEFAULT-account-2-20261009-1010)" next list items 1, 2 and 5. Gate 0a: SESSION-SWEEP-account-2
stale-claimed since 5 Oct (prior incarnations proceeded). Exclusions: eckert-*, lodewijk-van-nassau-1573-74, jan-van-nassau-1572-75 and
the other folders of account 4's LANE DEFAULT-1051 (craven-rupert-1648, fr4735-monluc, sforza-pusterla), baluze167, huntington-blathwayt,
ceppo-nevers, pro3055-clinton-1779, fr16045-pisany, birago-*, hellen-frederick-1752, ra-karlxi, Gallica fetches, Armstrong/Debosnys, every folder
with a ROOM claim < 6 h and no done. Not taken: handoff next 4 (antt-linhares-chave labeller re-calibration) -- LIN-COUNT logged the instrument
[retired] at 1897 px after a pre-registered calibration FAIL; a re-calibration with a re-cut gate on the same instrument and material is the
rule 3 third-attempt shape, so it waits for a person's count or a different instrument.
Register rows re-checked by check 1 (13:2x): antt-msliv0638 "eye-check m0200 + m0277/m0278 crib" already ran (R11A-BRO, 6 Oct; gate FAIL) --
replaced by its next not-attempted gap (body leaves m0250-m0269 + m0178); wvo-hessen-1564 WVO search already ran (R7-WVOH).
Intake gate 13:2x UTC (tools/intake_gate_check.py, exit 0 each): sachsstaatsarchiv-manteuffel-1712 partial, antt-msliv0638-brochado-1712 partial,
heinsius-vanhaersolte-1703 open -- "edition/page or full-text-search citation found within 6 lines".
Key livecheck: last probe 12:27 UTC (room.py --start summary: 9 present, 5 working); no ASKS/LOCAL-QUEUE row is planned this wave.

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim line
  with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE FAMILY-A2i (account 2)". If --start fails to push
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
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE FAMILY-A2i (account 2)",
  then a five-line final report.
- PREREG files and results: commit with `git add <paths> && git commit -m ... && git push origin HEAD:main` directly (tools/room.py "msg"
  --push <paths> commits ROOM.md only -- known tooling flag); check `git log -1 --stat` shows the PREREG landed BEFORE computing any score.
- Rule from V-BRANDT (9 Oct): a gloss used as a known answer is read BLIND (two passes) and scored per blind pass; the worker never settles
  the gloss before scoring. Commit every crop a later eye check would need (MANT-EYE63 could not run because crops stayed in scratch).
- PREREG lesson (V-MANT0136, 9 Oct): push the PREREG in its own commit with `git push origin HEAD:main` and check
  `git log origin/main -1 -- <PREREG>` shows it BEFORE scoring; a room.py rebase can fold the commit away.
- Hosts this wave: www.archiv.sachsen.de ("sachsen": MANT-0177 first, then MANT-CUC3 -- take/release; the second works from disk until the first posts its release); digitarq.arquivos.pt ("digitarq": BRO-SWEEP only, >= 3 s, <= 40 requests); resources.huygens.knaw.nl ("huygens": HEIN-SR2 only).



## Wave 1 (13:2x UTC 9 Oct)

### MANT-0177 (Opus, cap 4, box 90 min, sachsen take/release FIRST): sachsstaatsarchiv-manteuffel-1712, 0176 fix then 0177 continuation
Handoff next 1. (a) Owed fix from AUDIT.md V-MANT0176 section 8(c) (~line 1539): in 0176's transcription set r04 pos 7 to punctuation (a comma, not
a code) and r01 pos 3 to 26 (three eyes agree); re-run the folder's 0176 --check scripts and gate (b) exactly as MANT-0176 ran it (fr18 permuted-key
with power control at the new N); report old/new numbers; the gate is not re-cut. Do not edit AUDIT.md (a verifier's file) beyond appending a one-line
"fix applied <commit>" note under section 8(c). (b) 694/08 0177 (frame after 0176; Manteuffel, Berl. 2 Juil 1712, the letter's end per V-MANT0176
8(d)): check 1 (grep NOTES/inventories for 0177; abbo_check.tsv already covers AB BO I); fetch 0177 ONCE at native (sachsen take/release, >= 2 s,
the frames.tsv URL; manifest entry), crop code runs only (`tools/iiif_lines.py --image ... --out f0177_08/crops --debug`, pasted), two blind Sonnet
passes (one call per pass over the crops, code digits only), reconciliation (one more unit), decode with key.tsv (decode_key.py or the folder's 0176
script pattern, --check), gate (b) as for 0176 (power control at the run's own N; too-short if power < 0.8 -- say so, no reading claimed then).
Grades per rule 4. Report the run count, tokens, gate numbers and grade counts; whether 'le vieux' or the 0176 names recur. Commit crops. Units:
1 GET + 2 vision calls + 1 reconciliation + CPU, ~$3.5. Report what was found and where it was not found; do not classify novelty.
Print check 5 after decode: Berner (1901) and Bonnesen (1918) by date + names (IA be-api, take/release "IA") -- searched/unreachable per source.

### MANT-CUC3 (Opus, cap 4.5, box 90 min, sachsen: wait for MANT-0177's "sachsen release"; disk prep meanwhile): 694/08 0398 + 0499 clear-under-code
Handoff next 2 first half; MANT-CUC2's named next. PREREG-MANTCUC.md UNCHANGED (statistic, permutation control, gate real > p99 -- reuse; do not
re-write it). Inventory rows mant0608/inv08c.tsv lines 29 (0398: stamp 318, Flemming to Manteuffel, Greifswald 15 Oct 1712, clear words underlined
with codes above) and 47 (0499: stamp 400, one run 110.?.28.26.2.5.95 under 'la Treve'). Check 1: confirm neither leaf was scored before (NOTES
MANT-CUC/MANT-CUC2, cuc_candidates.tsv). Fetch both ONCE at native (sachsen take/release, >= 2 s; manifest); crops of the code lines only, the clear word
NOT in the crop (`tools/iiif_lines.py --image ... --debug`, pasted); per leaf one Sonnet call pass A, one pass B (digits only), one blind call for the
clear words; reconcile (tools/reconcile_passes.py); score per leaf and pooled with the 5 earlier leaves (report both the 2-leaf and the 7-leaf pool);
codes absent or disagreeing -> cuc_candidates.tsv (grade C from the clear word, never key.tsv). Units: 2 GETs + 6 vision calls + 1 reconciliation,
~1.5 per call when Opus reconciles, Sonnet calls ~0.5 -> ~$4. Stop before starting 0499 if 0398 has used 80% of the cap. No decode of unglossed leaves.

### BRO-SWEEP (Sonnet, cap 3, box 75 min, digitarq take/release): antt-msliv0638-brochado-1712, body leaves m0250-m0269 + m0178 at full resolution
NOTES Remaining gaps bullet "Body leaves m0250-m0269" and Escalation siblings ("Planned: a full-resolution sweep of m0250-m0269"). Read body_leaves.tsv,
the PX-BROBODY2 and R11A-BRO sections and tools/digitarq_fetch.py --help first. Fetch the 21 leaves ONCE with `tools/digitarq_fetch.py ... --full`
(>= 3 s apart, <= 40 requests total, manifest in images/; keep the folder under 30 MB -- keep full JPEGs only of leaves with cipher, a 1000 px copy of the
rest). Screen each leaf for code runs (number/letter groups set apart from the Portuguese prose, the m0275 kind) by Sonnet subagent calls over
1000-1200 px downsized leaves, <= 4 leaves per call, with planted controls in each call (m0275 or m0179 = cipher, m0200 = clear; tile key in a file read
AFTER the calls); eye-check every flagged leaf at full size yourself. Record every leaf in body_leaves.tsv (leaf, page no., letter/date head if visible,
cipher y/n/partial, est. tokens, gloss y/n). If a run is found: line crops committed under images/crops_mNNNN/ and its location in NOTES; NO
transcription, NO decode (a later job). Update the Remaining gaps bullet and Escalation siblings line; gaps_check. ~$2.5.

### HEIN-SR2 (Sonnet, cap 1.5, box 60 min, huygens take/release): heinsius-vanhaersolte-1703, small_runs over Deel 2 pp.132-251
NOTES "HEIN-SR" section and the Remaining gaps bullet "Deel 2 printed pp.132-600". Same tool and settings HEIN-SR used (small_runs.py --fetch, >= 2.1 s,
<= 120 requests; stop at the budget and record the last page); positive control as HEIN-SR (letters 341 and 1017's pages flagged from disk, no refetch).
Append rows to small_runs_HEINSR.tsv (or a _2 file), NOTES section, update the gap bullet's page range and the Verdict, gaps_check. Any run found:
page, letter no., sender, date, snippet -- no reading.
