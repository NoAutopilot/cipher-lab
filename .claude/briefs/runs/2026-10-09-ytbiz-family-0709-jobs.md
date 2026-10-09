# LANE FAMILY jobs (account 2, incarnation DEFAULT-account-2-20261009-0709, "FAMILY-A2g") -- 9 Oct 2026 07:2x UTC, lane orchestrator session_01JLg3wgWv5KDmveVFp6agMv

Lane brief: .claude/briefs/lane-family.md (+ lane-common-blast.md). Cap 60, box 07:10-17:10 UTC 9 Oct. Seventh incarnation: started from
STATUS.md "LANE FAMILY handoff (incarnation DEFAULT-account-2-20261009-0409)" next list items 1-5. Gate 0a: SESSION-SWEEP-account-2
stale-claimed since 5 Oct (prior incarnations proceeded). Exclusions: eckert-*, lodewijk-van-nassau-1573-74, baluze167, huntington-blathwayt,
ceppo-nevers, pro3055-clinton-1779 and fr16045-pisany (live work on accounts 1/4 within 6 h), Gallica fetches, Birago/Armstrong/Debosnys,
every folder with a ROOM claim < 6 h and no done. Register rows re-checked by check 1 at 07:2x: wallis-emus203 Thurloe vols 2-5 grep already
done (R8-SPLOOK 6 Oct); es132 f.89 rule-7 re-derivation already done (ES132-RD 8 Oct) -- neither briefed.
Intake gate 07:1x UTC (tools/intake_gate_check.py, exit 0 each): sachsstaatsarchiv-manteuffel-1712 partial, la-garde-1577 open,
hessen-daenemark-1672 partial -- "edition/page or full-text-search citation found within 6 lines".
Key livecheck 07:17 UTC: Google Books HTTP 200 (works again), OpenAlex 200, CORE 200, Semantic Scholar 429, Europeana timeout.

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim line
  with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE FAMILY-A2g (account 2)". If --start fails to push
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
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE FAMILY-A2g (account 2)",
  then a five-line final report.
- PREREG files and results: commit with `git add <paths> && git commit -m ... && git push origin HEAD:main` directly (tools/room.py "msg"
  --push <paths> commits ROOM.md only -- known tooling flag); check `git log -1 --stat` shows the PREREG landed BEFORE computing any score.
- Rule from V-BRANDT (9 Oct): a gloss used as a known answer is read BLIND (two passes) and scored per blind pass; the worker never settles
  the gloss before scoring. Commit every crop a later eye check would need (MANT-EYE63 could not run because crops stayed in scratch).
- PREREG lesson (V-MANT0136, 9 Oct): push the PREREG in its own commit with `git push origin HEAD:main` and check
  `git log origin/main -1 -- <PREREG>` shows it BEFORE scoring; a room.py rebase can fold the commit away.
- Hosts this wave: archiv.sachsen.de ("sachsen": V-MANT0454's two GETs first, then MANT-INV08B -- take/release, the second waits for the
  first's release and works from disk meanwhile); www.googleapis.com (GB-PHRASE only); everything else disk only / CPU only.

## Wave 1 (07:2x UTC 9 Oct)

### V-MANT0454 (Opus, cap 5, box 90 min; verifier, a session that has not read 0454): sachsstaatsarchiv-manteuffel-1712, Loc. 694/08 frame 0454
Handoff next 1. Claim under audit (NOTES "MANT-0454"): "694/08 0454 read under Krauske's table: 62 tokens S46 M16, gate (b) PASS at N=52 (real
-1.659 vs p95 -1.693); stretches 'rebelle', 'Rozrasewsky' x2, 'renonce a', '[a]rnold', 'abdiquer'". Use the CLAUDE.md "Verifier brief
(template)" steps 1-5 in full, with depth per .claude/briefs/runs/2026-10-08-acct3-depth-bar.md (copy the bar into your section before ruling).
Step 0 (the solver's owed lookup, done by you as part of check 4): "sachsen take", two GETs of 694/08 frames 0452 and 0453 (full-size URLs
from images/loc694-08-09/frames.tsv or mant0608's frame list; the 0454 URL pattern), "sachsen release"; save to f0454_08/ with a manifest entry;
read the letter's date line, place, sender/recipient and any code group on its first page (eye at reduced size, then line crops via
tools/iiif_lines.py --image only where a date or code needs a zoom; one Sonnet call per crop, two on doubt). Then check 4 by that date
(+-1 day): Droysen IV.1/IV.2, Acta Borussica, the Mercure historique et politique / Europäische Fama for the Rozrazewski audience and
Stanislas's abdication talk (IA full text, Google Books with country=US and the key, OpenAlex); positive control per edition. Check 5 / G3:
re-run tools/print_check.py on f0454_08/phrases.txt where MANT-0454 got Google Books 429. Ground truth: re-run f0454_08's three --check
scripts; spot-check three tokens against f0454_08/crops. Write "## AUDIT (V-MANT0454)" in AUDIT.md (N-class, depth, key source `period`
(Krauske's 1893 table is a modern archivist's table rebuilt from period glosses -- say which you rule and why), safe/unsafe sentence),
status.json row, NOTES pointer section. If N3+ D2+: the SECOND-OPINIONS-QUEUE row (CLAUDE.md) and a WORK-QUEUE row `AUD2-FAMILY-A2g-1` for
account 3. Units: 2 GETs + ~3 vision calls + searches + ruling, ~$4.5. Do not decode anything beyond re-running the committed scripts.

### MANT-INV08B (Opus, cap 6, box 100 min): sachsstaatsarchiv-manteuffel-1712, Loc. 694/08 stride-4 offset-2 frame inventory
Handoff next 2 + SIBS-PREMISE round item 6. Read NOTES "MANT-INV08" (the stride-4 pass that saw 310/592 frames) and mant0608/. Prior work
(check 1): list the frames already seen in mant0608/, frame_inventory.tsv, frame_classify_gaps207.tsv, inventory_r12dmant06.tsv and every
f0NNN_08 folder; your frame list = 694/08 frames not yet seen, starting with stride 4 offset 2 from MANT-INV08's offset. Host: wait for
V-MANT0454's "sachsen release" (work out the frame list meanwhile), then "sachsen take" and fetch at >= 2 s apart, reduced size where the
host allows (else full size, downscale locally, keep only code-bearing frames on disk under 30 MB, the rest in a manifest only). Classify each
frame by eye at reduced size (code groups yes/no, glossed y/n/partial, density, est. tokens), batched as contact sheets of <= 6 frames per vision
call (~1.5 per call). Write mant0608/inv08b.tsv and extend rank_unglossed_08.tsv with the new unglossed code-bearing frames (grade M estimates,
not transcriptions). Stop at 80% of cap or box; report frames seen / remaining. Units: ~140 frames = ~24 contact-sheet calls is too many --
stop at ~10 calls (~60 frames, ~$5) and hand the rest on. No transcription, no decode.

### MANT-NAMES136 (Opus, cap 3, box 60 min, disk only): sachsstaatsarchiv-manteuffel-1712, 694/09 0136 r01/r02/r09 as name runs
Handoff next 3 (second half). NOTES "MANT-0136" (04:17) and V-MANT0136 in AUDIT.md: r01 '44 16 12 8 33 5 35 42' (l o l h o v e l, after 'la
negociation secrete de'), r02 '39 12 7', r09 '50 15 10 17 6 29 14 30 35'; 0103 r04 repeats r01's stem 44 16 12 8. Steps: prior work (check 1:
grep the runs in HYPOTHESES.md and every f0*_09/f0*_08 decode); `tools/name_candidates.py ciphers/sachsstaatsarchiv-manteuffel-1712 --code ...`
for each run with --sender Manteuffel --recipient Flemming --date 1713-04 (read its --help: the pool is frozen before scoring; build the pool
from Droysen IV.2 / Krauske's table names / persons named in the clear parts of 0136 and 0103, saved as a file and committed BEFORE scoring), then
`tools/decode_key.py <t> --try` per top candidate (where the tool supports a letter-run candidate; if it does not, say so and report the
candidates only). Accept nothing into key.tsv; grades M at best; HYPOTHESES.md rows; NOTES "MANT-NAMES136". ~$2.5.

### LAG-CHECK (Opus, cap 1.5, box 40 min, CPU only): la-garde-1577 --check re-runs LAG-RESCORE left
Handoff next 4. Run every script LAG-RESCORE committed (NOTES "LAG-RESCORE"; lag_sylv2 / lag_wcgap or whatever names it gives) with --check;
where a script has no --check, add one that regenerates and diffs its committed output (rule 7), exit non-zero on stale. Paste outputs into
NOTES "LAG-CHECK"; update Remaining gaps/Escalation and gaps_check. If a check shows a stale committed number, report both numbers and do not
rewrite the conclusion yourself -- flag it in ROOM for the lane. ~$1.

### GB-PHRASE (Opus, cap 3, box 60 min; host www.googleapis.com only, plus IA be-api): two owed Google Books phrase checks
Google Books answered 200 at 07:17. (1) hessen-daenemark-1672: the 0062 gloss phrase search BRANDT-MARGIN could not run (NOTES "BRANDT-062",
"BRANDT-MARGIN"; dk131_brandt/ phrases) -- tools/print_check.py with the phrases file it names, Google Books rows only plus anything it
skipped. (2) sachsstaatsarchiv-manteuffel-1712 0136: the press-of-the-day check (handoff next 3, V-MANT0136's "press of the day unchecked"):
Mercure historique et politique and Europäische Fama, April-May 1713, for the news 0136 reports (NOTES "MANT-0136" 04:17 reading; AUDIT
"V-MANT0136"), by Google Books (country=US, key, filter=full where possible) and IA full text; a positive control per periodical (a 1713 item
you know is in that volume). One request at a time, >= 1.5 s; stop the host on 429. Record per check route/query/result in each folder's
NOTES ("GB-PHRASE"); a hit sharing two rare entities within +-3 days is SUBSTANCE: quote it and flag ROOM for the lane (it goes to the
verifier). No decode, no class. ~$2.5.

### VB-EAD (Sonnet, cap 2, box 45 min; host www.nationaalarchief.nl, "NA" take/release): vanbeuningen-dewitt-1657 pool, sibling cipher letters
Supply (c): KEY-OFFICES row for ciphers/vanbeuningen-dewitt-1657/key.tsv (491/517 coded tokens C); NOTES "Remaining gaps" bullet "other Van
Beuningen letters of 1656-1658 in NA 3.01.17 inv.1536-1541" and the Verdict's cheapest next. Intake gate 07:2x: found-solved, exit 0 (the
19/29 Sept letter's text is in print; this job looks for UNREAD siblings in the same key). Prior work check 1: grep NOTES/AUDIT for every inv.nr
you list. Steps: ONE request for the archive's EAD (`www.nationaalarchief.nl/onderzoeken/archief/3.01.17/download/xml`, the route NOTES line
113 used), saved to sources/na-3.01.17/2026-10-09/ (README with URL, date, sha256; it is a source snapshot, never edited). Grep it (script,
not a model read) for cijfer, gecijferd, sleutel, chiffre, geheimschrift, ontcijfer and for Beuningen across 1655-1660; write
ciphers/vanbeuningen-dewitt-1657/siblings_ead.tsv (inv.nr, date, title, matched term, digitised y/n from the `<dao>`, already-printed
pointer if NOTES names one, e.g. the 28 Oct 1657 letters Kernkamp deciphered = known). Do NOT fetch images. NOTES "VB-EAD" with the ranked
list (unread + digitised + Van Beuningen as sender first) and the next step per row. ~$1.5.

## Wave 2 (07:4x UTC 9 Oct)
Hosts this wave: sachsen -- MANT-INV08C holds it for its batch; MANT-0109 needs at most one GET (take/release around it, waits for
INV08C's release or works from disk if 0109 is already there); service.archief.nl / www.nationaalarchief.nl ("NA") VB-SCREEN only.

### MANT-0109 (Opus, cap 5.5, box 100 min): sachsstaatsarchiv-manteuffel-1712, Loc. 694/08 frame 0109 (f.80) as a reading leaf
MANT-INV08B rank 1 unglossed (mant0608/inv08b.tsv row 0109: two pages, calligraphic clerk hand, ~70-90 tokens, recurring pairs 55.44 x~14 and
7.60 x~9). Method and gates exactly as NOTES "MANT-0454" (copy its folder layout to f0109_08/; PREREG-MANT-0109.md pushed in its own commit and
checked on origin BEFORE any pass or score -- it names gate (b) (fr18 4-gram, letter values permuted over letter codes, power at this leaf's
letter count from the 0085/0136 unglossed windows; power < 0.80 = non-test, stop there and say so), the grading rule and the repeated-pair
handling). Check 2 includes the facing page and 0108/0110 if on disk. Crops via tools/iiif_lines.py --image (pasted), committed; two blind
Sonnet passes (A crop order, B reversed), one reconciliation unit. Check 5 (print_check on the decoded + clear phrases; Google Books answers
today). Units: 1 GET + 2 passes x ~2 calls + reconciliation, ~$5. Report what was found and where it was not found; do not classify novelty.

### MANT-INV08C (Opus, cap 5, box 80 min): sachsstaatsarchiv-manteuffel-1712, Loc. 694/08 offset-2 frames 0267-0499 (the 43 MANT-INV08B left)
Same method as NOTES "MANT-INV08B" (its sheets_b.py, planted controls, sheet_key, eye check at 1500 px of flagged frames); append to
mant0608/inv08b.tsv (or inv08c.tsv) and re-rank rank_unglossed_08.tsv. "sachsen take/release" around the batch. No transcription. ~$4.5.

### VB-SCREEN (Opus, cap 6, box 90 min; host service.archief.nl / www.nationaalarchief.nl, "NA" take/release): vanbeuningen-dewitt-1657 siblings
NOTES "VB-EAD" ranked inv.1537, 1539, 1541 first (autograph Van Beuningen letters to De Witt; digitised; EAD flags no cipher). Prior work
check 1 per bundle. Route (CLAUDE.md host table, Nationaal Archief row): the item page's embedded drupal-settings-json for the scan list, then
service.archief.nl IIIF at a small size (<= 400 px wide) one scan at a time, >= 1.5 s apart, <= 120 requests in all. Screen for comma- or
dot-separated digit runs: first a script (ink-density/row-profile heuristics are optional), then contact sheets of <= 12 thumbnails per
vision call (~1.5 per call), planted controls on each sheet (two known cipher leaves: images/NL-HaNA_3.01.17_1538_0208/0209 or the cipher leaf
this folder read, and two known clear leaves 0206/0207). Write vanbeuningen-dewitt-1657/siblings_screen.tsv (inv, scan, digit runs y/n,
est. groups, date if legible at thumbnail size). Stop at 80% of cap; start with inv.1537 (QUEUE HU7, 15 Mar 1656, may sit there). No
transcription. ~$5.

### SUR-PARTIAL (Opus, cap 2.5, box 50 min, CPU only): na-suriname-map-1781 partial-split power curve
NOTES "SUR-POOLPC" next (line ~3480): plant m -> Mx at 25/50/75% of m tokens at the pooled 65 lines on both scaffolds, same statistic, aligner,
draws and gate as PREREG-SUR-POOLPC; PREREG-SUR-PARTIAL.md pushed in its own commit before any draw. Report detection per level per scaffold
and what the real pooled NO SPLIT now excludes (the smallest split fraction with power >= 0.80). HYPOTHESES.md row with both numbers; NOTES
"SUR-PARTIAL"; Remaining gaps/Escalation; gaps_check. ~$2.

## Wave 3 (07:5x UTC 9 Oct)
Hosts: sachsen -- MANT-0453 only (INV08C released 07:49); IA / HathiTrust EF / Google Books -- BONNESEN only.

### MANT-0453 (Opus, cap 5, box 90 min): sachsstaatsarchiv-manteuffel-1712, Loc. 694/08 frame 0453 cipher + the letter's date (0450-0451)
V-MANT0454's next (2) and (3) (AUDIT.md "AUDIT (V-MANT0454)" line ~1229 and ~1331): 0453 right page para 3 carries code groups nobody has read;
0452/0453 have no date line. Steps: prior work (check 1: grep 0453 in the folder); "sachsen take", GET 0450 and 0451 (2 GETs; 0452/0453 are
already on disk in f0454_08/ from V-MANT0454), "sachsen release"; find the letter's head and date (eye, then line crops where needed).
Then 0453 as a reading unit by MANT-0454's method in f0453_08/: PREREG-MANT-0453.md pushed in its own commit before any pass, gate (b) with a
power control at this unit's letter count (power < 0.80 = non-test: say so and stop at the transcription); two blind Sonnet passes on committed
crops; grades; check 5. If 0453 belongs to the same letter as 0454, say so with the evidence, and add 0453's letter count to a pooled gate
(b) only if the PREREG named that pooling before scoring. ~$4.5. Report what was found and where it was not found; do not classify novelty.

### BONNESEN (Sonnet, cap 2, box 45 min; lookup): Sten Bonnesen, Studier över August II:s utrikespolitik 1712-1715, del I (Lund 1918) pp.62-77
V-MANT0454's next (1): the decisive prior-print check for 0454 (Rozrazewski sent by Stanislas to Berlin, Arnold, abdication). Find a full-text
or page-image copy: IA advancedsearch (title/creator), HathiTrust bibliographic API (Chrome UA) then HTRC Extracted Features per-page token
counts for "Rozrazewski"/"Rozražewski"/"Arnold"/"abdi*" to locate pages (EF works even for search-only volumes), Google Books (GS3SAAAAMAAJ;
country=US, key) snippet search for the 0454 phrases' entities; Lund University / LUP open copy. Positive control: a word you know is on
p.68-70 by the snippet V-MANT0454 saw. Write a NOTES section "BONNESEN" in the Manteuffel folder: per route what was reachable, which pages
mention the entities, and any quoted text (snippets verbatim). If no route reads the pages, write a LOCAL-QUEUE.tsv row (owner's browser:
HathiTrust full view or Google Books page view of pp.62-77) per tools/local_runner_brief.md format, quoting the key_livecheck line for Google
Books. Do not decode; do not change AUDIT.md (the verifier's class is changed only by a verifier). ~$1.5.

### V-MANT0109 (Opus, cap 5, box 90 min; verifier, a session that has not read 0109): sachsstaatsarchiv-manteuffel-1712, Loc. 694/08 frame 0109
Claim under audit (NOTES "MANT-0109"): "694/08 0109 (f.80) both pages read under Krauske's table: 80 tokens, S37 M43 (38 M = name-abbreviation
groups 55.44 x12, 7.60 x7); gate (b) PASS at 43 letters (real -1.392 vs p95 -1.687, p99 -1.539, 0/1000; power 18/18); reads Kraut, Kr.,
commissioners Feldm. le comte Dona / Printz / Kameke / Ilgen, le grand maitre". Same shape as V-MANT0454 (jobs file, wave 1): CLAUDE.md
verifier template steps 1-5 in full, depth per .claude/briefs/runs/2026-10-08-acct3-depth-bar.md copied into your section. Step 0: the solver's
owed lookup -- "sachsen take" (wait for MANT-0453's release; it is fetching 0450/0451), GET 0108 (and 0110 if 0108 shows no head), "sachsen
release"; read the letter's date, place and sender. Check 4 by that date: Droysen IV.1/IV.2, Acta Borussica Behördenorganisation, the
Kraut/commission affair in print (IA full text, Google Books country=US + key, OpenAlex; positive control per edition). Check 5 / G3 where
MANT-0109 got Google Books 503. Rule the 55.44 / 7.60 name groups: H/C only with a key-table row or a gloss; else M. Write "## AUDIT
(V-MANT0109)" in AUDIT.md, status.json row, NOTES pointer; if N3+ D2+, the SO row and WORK-QUEUE `AUD2-FAMILY-A2g-2` for account 3. ~$4.5.
