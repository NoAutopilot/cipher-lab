# LANE LANE-RUN9-account-2 jobs (account 2) -- 6 Oct 2026 05:1x UTC, lane orchestrator session_01A1YMVHYC29a1P95MRiYJHg

Lane brief: .claude/briefs/default-lane.md (cap 60, box 05:13-15:13 UTC 6 Oct). WORK-QUEUE row 246: RUN9, same tier as RUN8 --
tools/next_steps.py runnable rows (S, M) and `parallel` actions, first RUN8's own named next steps for this split (STATUS.md "LANE
LANE-RUN8-account-2 handoff", "Open for the next i-r lane"). Folders i-r (account 1 a-h, account 4 s-z). VERIFY-BACKLOG.tsv has no
i-r row needing a verifier (05:14 UTC). Off limits: Birago (incl. nevers-birago-fr3251-1572), Armstrong, Debosnys; riksarkivet-r4282-1628.
Every worker: Opus 5.5 (Sonnet for the check-solved job), one job, then stop. Each job first checks that its named step is still undone
(a dated NOTES.md section may already have run it); if so, stop and report rather than inventing work. Gate 0a: SESSION-SWEEP-account-2
row still `claimed`, but its TSV (2026-10-05) is on disk; RUN7/RUN8 proceeded past it the same way.

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim
  line with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE LANE-RUN9-account-2".
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
  owner; never print credentials (test presence with `test -n`). Never call AskUserQuestion. Report what was found and where it was not
  found; do not classify novelty.
- Stop at the cap or at 80% of the box, whichever first; do not start a unit that would cross 80% of either. A stop with work half
  done writes what was done and what remains into the folder's files. An Opus session floor is about 1.5; caps below assume it.
- Vision work: crop step mandatory and pasted (`tools/iiif_lines.py --image FILE --out DIR` or the --ark/--canvas form); give
  subagents only crop paths, one page/leaf per call, never a full-page image. Price: ~1.5 per Sonnet subagent pass, reconciliation = 1 unit.
- Sorters (lane rule since RUN7): any sorter meant for the owner must PASS `python3 tools/sorter_preflight.py` and have 5+ random tiles
  opened against the line image before it is handed on; it is handed to the account-3 orchestrator (ROOM flag line) to publish. Never
  publish an artifact or edit ASKS.md yourself.
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE LANE-RUN9-account-2",
  then a five-line final report.


## Wave 1 (spawned 05:2x UTC 6 Oct). Intake gate output (05:15 UTC) pasted per job.

### R9-NLACS -- nla-heinrich-braunschweig-1519, check-solved on the Grein key sheets (Sonnet, cap 3, box 45 min)
Intake gate: `nla-heinrich-braunschweig-1519: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
RUN8 named step (R8-NLA2, NOTES.md tail): NLA BU L 1 Nr. 548 and 562 each carry a 19th-c. archivist's key table and deciphered word list
(Dr. Grein, 1858/1860). Follow .claude/briefs/check-solved.md (six sources + Premise check) with this specific question: does the archival
decipherment, and any printing of it (Schaumburg / Braunschweig historical-society journals, Zeitschrift des Historischen Vereins fuer
Niedersachsen, Braunschweigisches Jahrbuch, Havemann, Merkel on Heinrich d. J., Grein's own publications), make this target `found-solved`
under rule 5, or does it stay `open` with a period key in hand (then the decode is a `period`-key check, grade H, not cryptanalysis)?
Do not decode. Write the verdict and the search log (sources, queries, hits, date) into NOTES.md; change the status line only if the
check-solved brief's own rules call it; flag in ROOM what the next job should be (e.g. the ~4.5 transcription + key-apply check already
costed in NOTES.md). No vision work.

### R9-RAYSORT -- rayburn-2004, owner sign sorter (cap 3.5, box 60 min; no vision subagent)
Intake gate: `rayburn-2004: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
RUN8 named step: the two blind passes reconciled at 47.1% agreement (pass2/), over the 10% line, so per TRANSCRIPTION.md and CLAUDE.md
Usage 6 the next step is the owner's sign sorter, not test 3 and not a third machine pass. Build a sorter with tools/sign_sorter.py (read
its --help, sorter README conventions from a recent folder, e.g. ciphers/matignon-mayenne-1586/sorter/) from the image and line crops on
disk, with the pass-split signs in focus.tsv. Then `python3 tools/sorter_preflight.py` must PASS (paste output) and you open 5+ random
tiles against the line image and list them. Only if both pass: one ROOM flag "rayburn sorter preflight PASS, ready for the account-3
orchestrator to publish (db capability), path ..."; update NOTES.md Remaining gaps (test 3 now waiting-on the sorter). Never publish or
edit ASKS.md. If preflight fails after one fix attempt, write why in sorter/README.md and stop.

### R9-RJMSORT -- rah-juan-manuel-1521, hand on the RUN1-SEG letter-alphabet sorter (cap 3, box 50 min; no vision subagent)
Intake gate: `rah-juan-manuel-1521: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
NOTES.md Remaining gaps: "Letter alphabet held out -- sorter/index.html built (RUN1-SEG: 1,781 tiles, 79 piles, 3 named), not yet published
or sorted -- account 3 publishes it". The Verdict's "label-anchored f.199 pass" is a machine pass on an unsettled inventory, which the
sorter rule hands to the owner first. Job: check whether the sorter was ever handed on (grep ROOM.md/ASKS.md for rah-juan-manuel sorter);
if not, rebuild it with sorter/build.sh against the current tools/sign_sorter.py template (the template changed 6 Oct, commit 09b452df4),
run `python3 tools/sorter_preflight.py` (must PASS, paste output), open 5+ random tiles against the line images and list them. Only if both
pass: one ROOM flag for the account-3 orchestrator to publish (db capability), path given; NOTES.md gap 1 becomes waiting-on that handoff;
pass tools/gaps_check.py. If it fails after one fix attempt, write why in sorter/README.md and stop.

### R9-ROUS4 -- naf14913-rousseau-venice-1743, re-registered count-vector gate with a same-class planted known-answer (cap 2.5, box 45 min)
Intake gate: `naf14913-rousseau-venice-1743: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
RUN8 named step (R8-ROUS3, NOTES.md ~l.1600-1620, PREREG 0ec1ce048): the gate's known-answer licence was 0/3 (de/et/se) so 605=republique
and 739 were NON-INFORMATIVE. Next ~1: a re-registered run whose known-answer controls are of the same class as the tested candidates
(long content words, comparable occurrence counts on the slip-backed pairs), so the licence can actually be met. Commit and push a PREREG
before the scored run; the control must be able to fail differently from the target (rule 3). Report both numbers. Do not change key 501
(a separate verifier job, R9-ROUSV, is reviewing it this wave); no key change unless the registered gate licenses it; then
decode --check.

### R9-ROUSV -- naf14913-rousseau-venice-1743, verifier on the 501 grade flag (cap 2, box 40 min)
Intake gate: as R9-ROUS4. You are a verifier, not the solver; do not protect the solver's conclusions. R8-ROUS3 logged (M, unregistered)
that code 501, graded C = "et" from the slips, has a count vector (1,1,0,2) matching "un", not "et" (0,1,0,2). Check every slip-backed
occurrence of 501 against the slip images/transcriptions on disk and the plain context: is C "et" supported at each occurrence, or is it
a data conflict (rule 4: two witnesses disagree -> record each, grade M where unsupported)? Correct key/grades only as rule 4 allows, then
decode --check; carry any change into AUDIT.md and any SECOND-OPINIONS-QUEUE.tsv row for this target (rule 10 propagation). Write a short
dated section in AUDIT.md or NOTES.md. Do not run new cryptanalysis.

### R9-OBRED3 -- oldenbarnevelt-brederode-1605, full-size read of the remaining in-window DECODE keys (cap 3.5, box 60 min)
Intake gate: `oldenbarnevelt-brederode-1605: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
RUN8 named step (R8-OBRED2, decode_keys_palatine_hessian.tsv, commit 256bcaf78): 89 numeral-tagged in-window keys unread at 200 px; next
"full-size Marburg 4 d 1219 + 5 Munich records ~3". One DECODE browser login for the session (tools/decode_browser_login.js, CLAUDE.md
DECODE row; --guess-fullsize per A2-HDK), fetch full size for those records, and for each record read whether the key is a numeral
nomenclator whose correspondents, date and code range could fit the Oldenbarnevelt-Brederode 1605 cipher (compare with the target's own
code range and the frequency facts in NOTES.md). Crop before any vision call (one record per call). Fit test only if a key is shown to
fit by those criteria, with a control. Scrub the account name from any saved page. Update the TSV and NOTES.md. Report requests per host.

## Wave 2 (written 05:2x UTC 6 Oct; spawned as wave-1 slots free). Intake gate output (05:15 UTC) pasted per job.

### R9-KARL4 -- ra-karlxi-fullmakt-1677, page read of the German 1680 Actes Vollmacht section (cap 2.5, box 45 min)
Intake gate: `ra-karlxi-fullmakt-1677: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Verdict cheapest next (R8-KARL3): page read of the plenipotentiaries' Vollmachten section in the German 1680 Actes (IA bub_gb_mUtFAAAAcAAJ /
11211619bsb, open scans, no loan) for the Swedish full power of 1677, ~$1. Locate the section from the item's _djvu.txt / page numbers
first (script), then fetch only those page images (one per vision call, crop or downscale under 2500 px). Report whether a Swedish
Vollmacht text is printed (page, leaf, quoted opening), and compare it with the target's transcription per NOTES.md. Update Remaining
gaps / Escalation; status changes only per rule 5 and the check-solved brief.

### R9-KONS2 -- konstanz-talleyrand-sieyes-1798, Guyot 1911 full-text search (cap 2, box 30 min)
Intake gate: `konstanz-talleyrand-sieyes-1798: open (line 3) -- edition/page or full-text-search citation found within 6 lines`.
Next (R8-KONS): Guyot, *Le Directoire et la paix de l'Europe* (1911), full text on IA / Gallica / Google Books (country=US) for a Sieyes
letter or report of 17 Jul 1798 (29 messidor an VI), "Constance"/"Konstanz", with a positive control phrase from the same volume. Script
the grep; quote hits with page. Write a dated NOTES.md section (found / not found where); status unchanged unless a printed text of the
letter is found (then say so and flag for check-solved; do not classify).

### R9-ROELL6 -- roell-vandedem-1809, January run of NA 2.01.xx inv. 92 (cap 3.5, box 60 min)
Intake gate: `roell-vandedem-1809: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Verdict cheapest next: the January run of inv. 92 (scans ~100-174, letters sent ahead to Vienna before 31 Jan 1809; <= 45 requests) or the
legation archive 1.02.20's 1809 letter-book. Take inv. 92 January first (same route, service.archief.nl IIIF at 1000 px, >= 1.8 s apart);
stop at 45 requests. Unit = one scan opened and read (~0.05); report minutes to Van Dedem and any cipher. If time remains under 80% of
box and cap, look up whether 1.02.20's 1809 letter-book is digitised (one item page, drupal-settings availability flag) and record it.

### R9-LQROWS -- three LOCAL-QUEUE.tsv rows for host-blocked reads (Sonnet, cap 1.5, box 30 min)
No deep work; intake gate not required. Run `python3 tools/key_livecheck.py` first (paste its summary line). File three LOCAL-QUEUE.tsv
rows in the existing format (read the header, L56/L57 and tools/local_queue_runner_prompt.md for the row shapes; next free L-number;
fetch+rebase immediately before writing):
(a) ciphers/lope-hurtado-1522: viewer-capture of BNE MSS/20212/27 (14 leaves, five Lope Hurtado letters 1522-26 partly cipher; BNE
    Digital is Cloudflare-blocked from the cloud) -- the L57 shape; give the BNE Digital card URL from NOTES.md.
(b) ciphers/ra-vellingk-1713: page read of HRSH (Historiska handlingar) vol. 6 pp. 223 ff., Vellingk letters, full view on HathiTrust and
    Google Books owgPAAAAYAAJ (snippet "Wellingk ... Sparre ... Chiffre"); ask for page images or a transcription of any passage naming a
    cipher/Chiffre and the letter dates. Both hosts' page views are blocked from the cloud (CLAUDE.md host table).
(c) ciphers/ra-celsing-sillen-1755 + ciphers/ra-celsing-dohsson-1779: catalogue-lookup on the Riksarkivet Sok-API / sok.riksarkivet.se
    (data.riksarkivet.se answers HTTP 000 from the cloud, re-tested 05:2x UTC 6 Oct): digitisation flag for the Celsing dispatches in
    Diplomatica Turcica 1746-1770 and Sillen's dag- och brefbocker, and every record under SE/RA/721512 (Biby), quoted flag + URL each.
Then add one line under each folder's NOTES.md "While waiting"/Escalation naming the L-row. Push with tools/room.py --push.

### R9-ROUSV2 -- naf14913-rousseau-venice-1743, verifier on the 605 = republique key entry (cap 2, box 40 min)
Intake gate: `naf14913-rousseau-venice-1743: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
You are a verifier, not the solver. R9-ROUS4 (commit 66ffa091a, PREREG c962e56e5) entered 605 = republique into key.tsv at grade C from a
count-vector gate (p 0.036/0.034, same-class planted known-answer). Check: (1) the PREREG was committed before the scored run (git log
order) and the run followed it; (2) the known-answer control could fail differently from the target (rule 3) and the licence was met;
(3) a count-vector gate licenses grade C (known plaintext) or only S (cryptanalytic with a control) under rule 4 -- C requires the
plaintext from a slip/clear source at that occurrence; regrade if needed; (4) decode --check exit 0; (5) carry any change into AUDIT.md and
any SECOND-OPINIONS-QUEUE.tsv row for this target (rule 10 propagation). Write a short dated verifier section. No new cryptanalysis.

### R9-NLATX -- nla-heinrich-braunschweig-1519, numeral-group transcription + Grein sheet-key apply check (cap 6.5, box 80 min)
Intake gate: `nla-heinrich-braunschweig-1519: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
R9-NLACS (commit 5de199eb4): no printing located; the target stays open with a period key in hand. NOTES.md's costed next step: transcribe the
numeral groups only (about 18 groups on Nr. 548 aufn 0003, about 12 on Nr. 562 aufn 0003; ~10 + ~8 lines). Units: crop step first
(`tools/iiif_lines.py --image ciphers/nla-heinrich-braunschweig-1519/images/<file> --out .../images/crops`, paste the command), then one blind
Sonnet pass per letter on line crops only (2 units) and one reconciliation from the crops (1 unit), ~1.5 each = ~4.5 + session floor.
Transcribe each sheet's key table into key.tsv (one per letter: key_548.tsv, key_562.tsv or a decode.json layout), apply with
tools/decode_key.py (grade H for every group the sheet's key reads; I for repairs, M for uncertain), diff against the sheet's own deciphered
word list, and report agreements/disagreements with counts. Add a decode --check script per rule 7. Run tools/judge_plaintext.py only if a
spec with a Low German judge exists (else say none). Status stays `open` or moves per rule 5 only with the counts written; flag in ROOM for a
verifier (N-class and depth are the verifier's). Report what was found and where it was not found; do not classify novelty.

## Wave 3 (written 05:4x UTC 6 Oct; spawned as wave-2 slots free).

### R9-RUBIN4 -- rubin-1953, Block C as Morse-like / binary with a matched control (cap 3.5, box 50 min)
Intake gate: `rubin-1953: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Next (R8-RUBIN3): transcription reconciled against every witness; test Block C as Morse-like or binary (0/1 as dot/dash or bits, x/'.' as
separators) against an English decoder, with a matched control of the same length and symbol design (synthetic English encoded the same
way, several seeds), ~$2. Pre-register (PREREG committed and pushed before the scored run): the encodings tried (enumerate them; count
them), the scoring (tools/judge_plaintext.py or an n-gram score), the gate, and the multiple-comparison correction across encodings.
Also score shuffled Block C through the same pipeline (rule 3: a shuffled-target PASS voids the gate). Report target, control and shuffle
numbers per encoding. A negative is a control-backed negative only if the control reads at the target's length; otherwise "non-test".
Update spec cheap_test_done if the spec names this test. No reading claimed unless the gate passes and the shuffle fails.

### R9-SURKEY -- na-suriname-map-1781, known-keys escalation step: NA 1.05.03 key-sheet search + design_prior (cap 2.5, box 45 min)
Intake gate: `na-suriname-map-1781: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Escalation "known-keys" is [ ] (1 Oct 2026): KEY-OFFICES.tsv has no Suriname/WIC/Wollant row and no tools/design_prior.py run is recorded;
"Planned: an NA catalogue search of 1.05.03 (Societeit van Suriname) for 1781 'cijfer'/'sleutel' items" plus Wollant's papers and Governor
Texier's 1781 correspondence. Do: (1) run tools/design_prior.py for this target and paste the output into NOTES.md; (2) search the
Nationaal Archief catalogue (www.nationaalarchief.nl search / service.archief.nl per the CLAUDE.md host table; NOT data.nationaalarchief.nl)
for 1.05.03 and the 4.VEL / Wollant context with cijfer, cyfer, sleutel, chiffre, geheimschrift, 1780-1782; record each hit's inventory
number, description, and digitisation flag (drupal-settings availability, never the boilerplate); (3) if a digitised key-sheet candidate
exists, fetch only its index thumbnail/first scan and say whether it is a key. No decode. Update the Escalation known-keys line and
Remaining gaps; pass tools/gaps_check.py. <= 40 requests to nationaalarchief hosts, >= 1.5 s apart.

### R9-NLAV -- nla-heinrich-braunschweig-1519, VERIFIER (CLAUDE.md "Verifier brief (template)") on the Grein period-key reading (cap 4, box 60 min)
Claim under audit (R9-NLATX, commit c99076a0e): the in-line cipher words of NLA BU L 1 Nr. 548 (letter to Countess Anna, 1519) and Nr. 562
(K. Schepper, Trier 8 Aug 1522) read with the 1858/1860 archivist key sheets: 548 18/18 words agree with the sheet's list (H 84, M 17
numbers), 562 11/12 (H 83, M 6; lant vs land). You are not the solver. Steps 1-5 of the template, plus: (a) circularity -- the
reconciliation was key-aware; check that H tokens are only those the blind pass and the reconciliation agree on and that the "agreement
with Grein's list" figure is not driven by M tokens settled toward the list; recompute the agreement on H-only tokens; (b) key source is
`period` (archivist's sheet of 1858/1860; say whether that is a period key under rule 10 or an archival modern decipherment, and grade
accordingly); (c) rule-5 status call: is the target `found-solved` (the decipherment of this very item already exists in the archive,
N0-style) and record it with the evidence -- the status line and status.json follow your call; (d) depth per rule 4a: the cipher tokens
are single words inside clear Low German letters -- state % of cipher tokens H/C/S and D-level with tools/depth_check.py; (e) the R9-NLACS
search log (8 queries) is the solver-side log; extend it (Niedersachsen journals, Schaumburg history, Heinrich d. J. biographies, Grein's
own publications, Google Books country=US, IA fts, OpenAlex/S2 with keys). Write AUDIT.md, status.json fields, any SECOND-OPINIONS row if
N3+. Do not decode afresh; do not touch other targets.

### R9-ROELL7 -- roell-vandedem-1809, NA inv. 996 (Hogendorp at Vienna 1809) read for the Feb 1809 letter (cap 3.5, box 60 min)
Intake gate: `roell-vandedem-1809: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
R9-ROELL6's cheapest next: inv. 996 (Van Hogendorp at Vienna 1809, digitised per EAD). Same route (service.archief.nl IIIF at 1000 px,
>= 1.8 s apart, <= 45 requests; one scan = one unit ~0.05). Look for a letter to/from Van Dedem or a cipher letter/key of Jan-Mar 1809
matching the target's description in NOTES.md; record scan numbers read and what each holds. No decode unless a key sheet is found (then
describe it and stop for a fit-test brief).

## Wave 4 (written 06:0x UTC 6 Oct; spawned as wave-3 slots free).

### R9-KAL6 -- kaliningrad-2015, paired soft/hard move-set anneal for the S3' unit (cap 7, box 80 min)
Intake gate: `kaliningrad-2015: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
The different instrument named by A2P4-KAL4 and carried by A2P4-KAL5 / RUN4-KAL ("paired soft/hard move set or two-stage solve, ~$6"): the
S3' soft unit's control did not converge (0.723) with the existing anneal; restarts alone are retired (rule 3 third-attempt clause). Build
the paired move (swap a soft/hard letter pair as one move, e.g. n<->N) or the two-stage solve as an option on the shared solver in tools/
(never a private copy; offline test in tools/tests/), pre-register (PREREG committed and pushed before any scored run), run the matched
control FIRST at the target's N, K and soft-letter rate (tools/family_run.py order: control below gate -> stop, log "control below gate",
no target run), then the target only if the control passes. Judge Russian decodes against the held-out distribution (p01 about -1.05 at N
about 1000) as well as real_p05 (A2P4-KAL5/RUN4-KAL: real_p05 alone is "judge cannot decide"), and score the shuffled target through the
same pipeline. Report control, target and shuffle numbers. Unit = one control or target run; size the run count from the per-run time you
measure on the first control run and stop before a run that would cross 80% of cap or box. HYPOTHESES.md row with both numbers.

### R9-NAKEY -- oldenbarnevelt-brederode-1605 NA States-side key hunt + rumpf-vandebie-heinsius-1716-19 NA re-probe (cap 2.5, box 45 min)
Intake gates: `oldenbarnevelt-brederode-1605: open (line 1) -- ...within 6 lines`; `rumpf-vandebie-heinsius-1716-19: open (line 1) --
...within 6 lines`. (1) oldenbarnevelt-brederode "Next cheap step" (NOTES ~l.686): the NA 1.01.02 (States-General) / 3.01.14
(Oldenbarnevelt) archive hunt for a States-side cipher key of 1600-1610 (see the folder's "Key hunt" section for what was already tried).
Search the NA catalogue (www.nationaalarchief.nl / service.archief.nl EAD per the CLAUDE.md host table, NOT data.nationaalarchief.nl) for
cijfer, cyfer, chiffre, sleutel, geheimschrift in those two archives; record inventory numbers, descriptions and digitisation flags
(drupal-settings availability). If a digitised key of the window exists, fetch only its first scan and say whether it is a numeral
nomenclator whose range could fit (no fit test). (2) rumpf "While waiting": re-probe NA 3.01.19 inv. 2030 and 2044 item pages
(drupal-settings availability, 2 requests) and record the flag. <= 40 requests to nationaalarchief hosts, >= 1.5 s apart. Update both
NOTES.md files.
