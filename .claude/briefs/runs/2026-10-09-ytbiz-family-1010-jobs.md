# LANE FAMILY jobs (account 2, incarnation DEFAULT-account-2-20261009-1010, "FAMILY-A2h") -- 9 Oct 2026 10:2x UTC, lane orchestrator session_01374AXg57FqWBwpvk29CTLT

Lane brief: .claude/briefs/lane-family.md (+ lane-common-blast.md). Cap 60, box 10:10-20:10 UTC 9 Oct. Eighth incarnation: started from
STATUS.md "LANE FAMILY handoff (incarnation DEFAULT-account-2-20261009-0709)" next list. Gate 0a: SESSION-SWEEP-account-2 stale-claimed since
5 Oct (prior incarnations proceeded). Exclusions: eckert-*, lodewijk-van-nassau-1573-74, baluze167, huntington-blathwayt, ceppo-nevers,
pro3055-clinton-1779, fr16045-pisany, birago-*, hellen-frederick-1752 (UNA-HELLEN/VERIFY-HELLEN), ra-karlxi (KARL-REQ), Gallica fetches,
Armstrong/Debosnys, every folder with a ROOM claim < 6 h and no done. FAM-POOL (research/FAMILY-POOLS-2026-10-08.md) and KEYHUNT-2026-10-07
already ran supply (c)/(d) for this lane's families; not repeated.
Intake gate 10:1x UTC (tools/intake_gate_check.py, exit 0 each): vanbeuningen-dewitt-1657 found-solved, sachsstaatsarchiv-manteuffel-1712 partial,
heinsius-vanhaersolte-1703 open -- "edition/page or full-text-search citation found within 6 lines".
Key livecheck 10:1x UTC: CORE 200; no changes since last probe (09:25).

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim line
  with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE FAMILY-A2h (account 2)". If --start fails to push
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
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE FAMILY-A2h (account 2)",
  then a five-line final report.
- PREREG files and results: commit with `git add <paths> && git commit -m ... && git push origin HEAD:main` directly (tools/room.py "msg"
  --push <paths> commits ROOM.md only -- known tooling flag); check `git log -1 --stat` shows the PREREG landed BEFORE computing any score.
- Rule from V-BRANDT (9 Oct): a gloss used as a known answer is read BLIND (two passes) and scored per blind pass; the worker never settles
  the gloss before scoring. Commit every crop a later eye check would need (MANT-EYE63 could not run because crops stayed in scratch).
- PREREG lesson (V-MANT0136, 9 Oct): push the PREREG in its own commit with `git push origin HEAD:main` and check
  `git log origin/main -1 -- <PREREG>` shows it BEFORE scoring; a room.py rebase can fold the commit away.
- Hosts this wave: resources.huygens.knaw.nl ("huygens": VB-0086 step 0 first, then HEIN-SR -- take/release, the second waits for the
  first's release); archive.org ("IA": MANT-ABBO, then RIK-COVER -- take/release); everything else disk only / CPU only.


## Wave 1 (10:2x UTC 9 Oct)

### VB-0086 (Opus, cap 7, box 120 min): vanbeuningen-dewitt-1657, does the 1656 letter 0086 share the 1657 key?
Handoff next 1 and 5. Known-text work by design: inv.1537 0086 (Van Beuningen to De Witt, 10 Dec 1656) is printed in clear in Fruin/Japikse,
Brieven aan Johan de Witt I (1919) pp.365-366, cipher stretches letter-spaced; it is used ONLY as a key source. Read NOTES "VB-EAD", "VB-SCREEN",
"VB-1537" (the 0079 ungated observation: 172/185/225/213 match key.tsv), key.tsv, align.py, decode.json, AUDIT.md section list.
Step 0 (huygens take/release, ~10 requests): the Brieven aan JdW "Brievenlijst" route VB-1537 used (`toc/index_html`, correspondent=Beuningen,
van_aan=van, date windows) for 1657-1658, and list which inv.1539/1541 letters are printed in Deel 1-2 (by date; NA scan dates from the METS
already fetched, or the 1539/1541 item pages, <= 4 NA requests). Write `edition_check_1539_1541.tsv` (date, printed y/n, volume/pages). No screen.
Step 1: pp.365-366 page images (huygens `pages.json` route; save under images/, manifest). Crop 0086's cipher lines from
images/screen_1537/NL-HaNA_3.01.17_1537_0086.jpg (1500 px; if digits are not legible, ONE fetch of 0086 at native via the IIIF path in
NOTES "VB-SCREEN", NA take/release) with `tools/iiif_lines.py --image ... --out images/crops_0086 --debug` (paste the command). Two blind Sonnet
passes per half page over line crops (groups only, gloss not shown to the pass where avoidable; read the interlinear gloss separately and blind,
V-BRANDT rule), reconcile with tools/reconcile_passes.py.
Step 2 (PREREG-VB0086.md pushed first, own commit): pair each group with its printed word by position inside the letter-spaced stretches
(tools/interlinear_align.py if the stretch/word segmentation is ambiguous). Statistic: share of groups that key.tsv holds whose 1657 value equals
the printed word (normalised spelling); control: the same share under 1,000 permutations of key.tsv's values among its codes (this CAN differ:
it changes values, the statistic is value agreement); gate: real > permutation p99. Also report codes absent from key.tsv with their printed
word (grade C from print) as candidate second contexts -- write them to `key_1656_candidates.tsv`, never into key.tsv.
Units: ~10 huygens + 4 vision calls + 1 reconciliation + CPU, ~$6. Report agreement, p99, how many single-context 1657 codes get a second
context. Do not decode any unprinted leaf. Words: this is a key test on a printed letter (rule 10: the text is known, say so).

### MANT-ABBO (Sonnet, cap 2, box 60 min, IA take/release): sachsstaatsarchiv-manteuffel-1712, Acta Borussica prior-print grep
Handoff next 2 first half (V-MANT0109's flag: 0109 was printed in Acta Borussica Behördenorganisation I Nr. 64). Before any further reading on
694/08: list every 694/08 leaf the lane might read next with its date/sender/recipient from mant0608/inv08b.tsv, inv08c.tsv, rank_unglossed_08.tsv
(at least 0108-0110, 0176, 0282, 0323, 0348, 0382, 0387, 0398, 0447, 0474, 0494, 0499 and the f0NNN_08 folders' leaves). Find the Acta Borussica
Behördenorganisation volumes covering 1712-1713 on IA (I = diebehrdenorgan01posngoog; search advancedsearch for II and others; note which are
not on IA) and fetch each `_djvu.txt` ONCE to scratch (IA take/release, >= 1.5 s). Grep by date (day + month, French and German forms, +-2 days),
Manteuffel, Flemming, and the 2-3 distinctive clear words of each leaf from the inventory notes; positive control: 0109's Nr. 64 pp.204-207 must hit.
Write mant0608/abbo_check.tsv (leaf, date, volume, hit y/n, Nr./page, snippet) and a NOTES section; mark any leaf printed as "printed: AB BO <vol>
Nr. <n>" in rank_unglossed_08.tsv's note column (no regrade). Check 4 only; no image fetch, no decode.

### HEIN-SR (Sonnet, cap 1.5, box 60 min, huygens: wait for VB-0086's "huygens release"): heinsius-vanhaersolte-1703, small_runs over the rest of Deel 2
NOTES "## While waiting" / "## Next step" (D2-HEIN): run `small_runs.py` (read its --help and the D2-HEIN section) over the Deel 2 pages A2P4 and
D2-HEIN did not read (page list from deel2_letters_r11a.tsv and deel2_ocr/ vs the full Deel 2 page range), fetching each OCR page once
(huygens, >= 2.1 s, <= 120 requests; stop at that budget and record the last page). Positive control: pages of letters 341 and 1017 must be flagged.
Write small_runs_HEINSR.tsv, a NOTES section, update Remaining gaps/Escalation and pass gaps_check. Any new run found: page, letter no., sender, date,
snippet -- no reading.

### RIK-COVER (Sonnet, cap 1.2, box 45 min, IA take/release after MANT-ABBO's release or disk first): riksarkivet-r4282-1628, R4120 cover names in clear text
NOTES "FAM-4333L" side check (line ~1508): grep R4282/R4284's clear phrases on disk and the AOSB ser. I Bd 3/4 and ser. II Bd 1 Camerarius letters
(IA `_djvu.txt` already identified in NOTES "IA-DESK-ALT"; fetch each once) for R4120's cover names and "ficta" countries (Achilles, Areopagitae,
Quirites, Leodius, Anastasius, Tryphon, Hannibal, Paulus, Sigismundus, Norwegia, Piccardia, Biscaia, ... -- full list from the FAM-4333L section or the
R4120 PDF transcription on disk). Positive control: one name known to occur in the AOSB text. Write rik_cover_hits.tsv + NOTES section; status unchanged
unless a hit ties R4120 to the Camerarius 1626-28 letters (then say so as a lead, grade nothing).

## Wave 2 (drafted 10:3x UTC 9 Oct; spawned as slots free)

### MANT-CUC (Opus, cap 7, box 120 min, sachsen take/release): sachsstaatsarchiv-manteuffel-1712, clear-under-code leaves as a gloss-free key check
Handoff next 2 second half; NOTES Remaining gaps bullet "694/08 clear-under-code leaves 0323, 0282, 0348, 0398 (+0499, 0284/0410)" and the
MANT-INV08C inventory rows (mant0608/inv08c.tsv). These are draft/instruction pages (mostly Flemming's hand, the other direction of the correspondence)
with CLEAR words underlined and the code runs written ABOVE them: the clear word is the known answer, no gloss reading involved. Check 1: grep
HYPOTHESES.md/NOTES for any earlier key check on these leaves (MANT-INV08 named 0284+0410 at ~$2; confirm it never ran). Fetch (sachsen take/release,
>= 2 s) 0323 and 0348 first (largest), then 0282 and 0410 only if the cap allows; save under f0323_08/ etc. with manifest entries. Crops: code-run
lines only (`tools/iiif_lines.py --image ... --out ... --debug`, pasted); per leaf ONE Sonnet call for pass A and ONE for pass B over that leaf's
code crops (digits only, the clear word under each run NOT shown -- crop the code line above the underline), plus one call reading the clear words
(blind, separately); reconcile with tools/reconcile_passes.py. PREREG-MANTCUC.md (own commit, pushed, checked on origin) before scoring: statistic =
share of codes whose key.tsv value equals the corresponding letter/syllable/word of the clear word under the run (exact rule for multi-code words:
concatenated key values == clear word after normalisation); control = 1,000 permutations of key.tsv values among codes (changes values, so it can
differ); gate = real > p99. Report per leaf and pooled; codes absent from key.tsv or disagreeing go to `cuc_candidates.tsv` (grade C from the
clear word, never into key.tsv). Units: 2-4 GETs + 3 calls per leaf (A, B, clear) x 2-4 leaves + 1 reconciliation, ~$1.5 per call; stop before
starting a leaf that would cross 80% of cap. No decode of any unglossed leaf.

### LIN-VIEYRA (Sonnet, cap 1.5, box 50 min): antt-linhares-chave, new material for the two M dictionary counts (cagar p.83 col 2, justa p.241 col 3)
NOTES Remaining gaps bullets for 283219 "cagar" and 3241315 "justa" and the A1B-LIN-ROWS diagnosis (~line 1250): three instruments retired on the
949 px IA derivative; the named next step is new material. Find (no counting): (1) whether archive.org newpocketdiction00viey has a higher-resolution
original (the item's files list: `_jp2.zip` / `_orig_jp2.tar`; the IIIF/BookReader full-size of leaves 95 and 255 -- one metadata request, then
at most 2 page fetches at the largest size served; record the pixel width vs 949); (2) a second independent scan of Vieyra, A New Pocket Dictionary
of the Portuguese and English Languages, London 1809, Part I: IA advancedsearch (title/creator, other identifiers), Google Books API
(country=US, key, filter=full), HathiTrust bibliographic API by OCLC (Chrome UA) -- list each copy with edition year, identifier, view and whether
pp.83 and 241 are reachable. Fetch the two pages from at most one second copy. Write `vieyra_copies.tsv` and a NOTES section; update the two gap
bullets' "next" with what was found; gaps_check. No count, no regrade (a later job counts under a fresh PREREG).

Wave 1 results (10:4x): VB-0086 PASS 216/225 vs p99 0.249 (1656 shares the 1657 key); Brieven aan JdW I prints every Van Beuningen letter
to De Witt 7 Jan 1657 - 7 Aug 1658 and none Sep-Dec 1658. MANT-ABBO: 0108/0109 and 0382 printed (AB BO I Nr.64, Nr.72); 5 date-only.
HEIN-SR: Deel 2 pp.7-131 no cipher run. RIK-COVER: no cover names in R4282/R4284 clear text.

### VB-SCREEN2 (Opus, cap 3.5, box 75 min, NA take/release): vanbeuningen-dewitt-1657, inv.1540/1541 letters after 7 Aug 1658 (unprinted window)
The edition prints nothing from Van Beuningen to De Witt after 7 Aug 1658 (edition_check_1539_1541.tsv, VB-0086). Check 1: NOTES VB-SCREEN/VB-0086.
Steps: (1) METS of inv.1541 (and 1540 if 1541 does not carry the late-1658 letters; the 1539/1541 METS URLs VB-SCREEN fetched; <= 3 METS requests);
date the scans at 400 px from heads/endorsements (contact sheets, Sonnet subagent calls of <= 12 tiles, ~0.5 each) to find letters dated
after 7 Aug 1658 -- also note any 1657-58 letter the edition list lacks; (2) screen only those scans for comma-separated number groups closed by
colons, VB-SCREEN's method with planted controls (cipher 1538_0210/0211, clear 1538_0206/0207 from images/), tile key in a file read after the calls;
(3) eye-check every flagged scan at 1500 px (<= 6 fetches). Write siblings_screen_1541.tsv (scan, date, sender, cipher y/n/partial, est. groups,
gloss y/n, printed y/n) and a NOTES section; gaps_check. No transcription, no decode. Requests service.archief.nl <= 130, >= 1.6 s.
