# LANE DEFAULT-account-4-20261005-2253 jobs (account 4) -- 5 Oct 2026 23:4x UTC, lane orchestrator session_01QTy8YG4RDcjZUdZs3b9xUg

Lane brief: .claude/briefs/default-lane.md (cap 60, box 23:35 UTC 5 Oct - 09:35 UTC 6 Oct). Backlog per the WORK-QUEUE row note
(re-pointed 23:3x by the account-3 orchestrator) and the spawn prompt: private-repo targets (Ferdinand 1478, hamilton-1650,
bowes-walsingham-1583, riksarkivet-r4282-1628) go to the account-4 standing session (this lane's sessions have no private-repo
access); then the d'Estaing Holker lead; ONE sorter fix-up job; ZOOM-ASKS.tsv "refetch, no owner" rows not held by accounts 1-2
(account 1 holds folders a-l from its jobs file, account 2 m-z). Off limits: Birago, Armstrong, Debosnys; never edit
tools/sign_sorter/template.html (the standing session's SORTER-SHAPE job). Every worker: Opus 5.5, one job, then stop.

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim
  line with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE DEFAULT-account-4-20261005-2253".
  If --start fails to push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
- Read the folder's NOTES.md tail (Remaining gaps / Escalation / latest dated sections) before acting. If a dated section already did
  your named step, stop and report (do not substitute other deep work).
- Good-citizen rule and the CLAUDE.md host table for every request (one request per host at a time, >= 1.5 s apart; stop a host on
  429/403/challenge, one retry after a pause at most). Report request counts per host. DECODE: one browser login per session
  (`tools/decode_browser_login.js`), scrub the account name from any saved page.
- Transcription/vision: crop first, as a command whose output you paste (`tools/iiif_lines.py --image FILE --out DIR` or the
  `--ark/--canvas` form); never hand a full page or leaf to a subagent; one page/line-set per subagent call; price per pass.
- Images: keep the folder under 30 MB; images/manifest.json entry for every fetched file.
- Grades per rule 4 (H/C/S/M/I); rule 7 `--check` before push where a decode script exists; a `partial` target keeps "## Remaining
  gaps" / "## Escalation" current and passes `python3 tools/gaps_check.py <target>`. Tick or update the matching Escalation line.
- Report what was found and where it was not found; do not classify novelty.
- Rebase before writing shared files (status.json, PROGRESS.tsv, HUMAN-TX-ASKS.tsv, ZOOM-ASKS.tsv, ROOM.md); keep both facts on
  conflict. Run `python3 tools/file_shrink_guard.py <every file you touched>` before the final push; push with
  `python3 tools/room.py --push <paths>`.
- Words: never "solved", "cracked", "novel", "first", "new" for anything this project did; rule 10 wording only. Never name the
  owner; never print credentials (test presence with `test -n`). Never call AskUserQuestion.
- Stop at the cap or at 80% of the box, whichever first; do not start a unit that would cross 80% of either. A stop with work half
  done writes what was done and what remains into the folder's files.
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE
  DEFAULT-account-4-20261005-2253", then a five-line final report.

Intake gate (pasted 5 Oct 2026 23:4x UTC, `python3 tools/intake_gate_check.py <t>`):
```
destaing-gerard-1779: open (line 1) -- edition/page or full-text-search citation found within 6 lines
harley-287-1587: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
vanbeuningen-dewitt-1657: found-solved (line 1) -- edition/page or full-text-search citation found within 6 lines
huntington-blathwayt-madrid-1728: partial (line 3) -- edition/page or full-text-search citation found within 6 lines
hessen-daenemark-1672: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
fr3621-dinteville-1592: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
```

### A4-SORTFIX -- owner sorter pages, fix before they reach the owner (cap 8, box 90 min; ~8 pages x ~0.8 + 1)
One job, not a series. Inputs: ROOM.md flags 2026-10-05 22:52 and 22:57 (account-3 orchestrator); HUMAN-TX-ASKS.tsv ranks 1-14;
tools/sign_sorter.py / sign_sorter_apply.py / sorter_recut.py docs; SYSTEM.md sorter rows.
1. fr3621-dinteville-1592 (rank 1): the published page (artifact RxURcDEas5VU11B95kVoJo) is the f.23r (fr.3623) sorter; its 21
   "Check these first" tiles ask "which sheet label?" but all row-4 tiles sit in one UNREAD pile with no 0 / 0' / o / v / v' / D piles,
   so the owner cannot place them. Find the right sorter (f.128/f.130 per NOTES.md and the look/ folder), seed named piles from the
   f.130 sheet labels (or give each check-first tile a pick-one-of-N question), rebuild with tools/sign_sorter.py on the CURRENT
   template (do not edit template.html), and test it in headless Chromium (tools/browser_fetch.js --shot): a check-first tile can be
   placed into a named pile. Republish to the same artifact URL if this account is a writer (Artifact action read first); if not,
   publish a separate artifact and put its link in HUMAN-TX-ASKS.tsv rank 1 and the folder's sorter/README.md.
2. Every other sorter link in HUMAN-TX-ASKS.tsv ranks 2-14 (skip Birago/Ceppo/Armstrong/Debosnys; skip bne20211-ferdinand-1478,
   the standing session's FER1478-SORTER): open each (Artifact read), check (a) the link is the sorter the row describes,
   (b) check-first tiles can be placed (named piles exist or a question is offered), (c) the page carries "Fix the cut" (SORTER-NUDGE,
   4 Oct). Write one table into HUMAN-TX-ASKS.tsv's header comment or a sibling file `HUMAN-TX-ASKS-sortercheck.tsv` (target, link,
   a/b/c, action taken).
3. Rebuild on the current template (so "Fix the cut" is there) every page that lacks it -- Florence (U2VPJbNVAm5S5u4ThNTbU1), Juan
   Manuel (YC3XqFjy3UbbbmGdF6Kkp9), Lancosme (FDkHh2hqX826r9fdxwXFAF), and the others step 2 finds -- keeping choices the owner already
   saved (read the page's db first; never wipe a saved choice). First check ROOM.md for the standing session's SORTER-SHAPE done line:
   if SORTER-SHAPE is still running, rebuild anyway on the template as committed and note in the table that a second republish follows
   SORTER-SHAPE. Same URL where this account is a writer; otherwise a separate artifact, with the link updated in HUMAN-TX-ASKS.tsv.
   Stop at the cap: list unrebuilt pages in the table.
Not this job: any transcription, any template.html edit, any target's reading.

### A4-DHOLK -- destaing-gerard-1779, the Holker lead for the Gerard-d'Estaing key (cap 5, box 75 min; search ~3 + key test ~1 + 1)
NOTES.md sections "Clements scan on hand" (64:15 covering letter: d'Estaing hopes Gerard left Holker "le Chiffre qui sert a sa
Correspondance avec moi") and DEST-COLLATE (collation.tsv, 216 groups, three copies). Step 1, search (logged per family, searched or
unreachable): LoC Manuscript Division Holker papers (John Holker / Jean Holker; loc.gov JSON API `?fo=json`, finding aid, digitised
reels if any), William L. Clements Library finding aids for Holker or Gerard (clements.umich.edu 403s the cloud: try the Wayback CDX
route, then log), AAE Correspondance politique Etats-Unis (Doniol's citations of "Etats-Unis, t. ..." volumes and any printed table of
French consular ciphers), Meng's Gerard despatches (despatchesinstru00fran) and Doniol IV for "chiffre"/"Holker", HathiTrust bib API
for Holker papers editions, Google Books API (`&country=US`), Europeana/DPLA keys for Holker items, DECODE catalogue snapshot
(sources/decode/*.tsv) for any French 1778-80 naval or consular nomenclator. Step 2, only if a key (or a fragment of one, or a sibling
cipher letter of the same correspondence with its decipherment) is found: test it on collation.tsv's agreed groups with a matched
random-key control (known_key_test.py is the pattern), report both numbers. No key found -> write a "## Holker lead (A4-DHOLK, date)"
section naming each source, what it holds, and the owner-side or archive request that would settle it (REQUEST.md row if an archive
copy order is the route; ASKS.md only per CLAUDE.md rules).

### A4-RFHAR -- harley-287-1587, DECODE full-size crops and the f.88r two-pass read (cap 6, box 75 min; 2 passes x ~2 + 1 recon + fetch)
NOTES.md Verdict "cheapest next": a two-pass blind sign-by-sign transcription of f.88r (R8492) from DECODE full-size crops, one login,
crop step pasted, scored against the gloss-confirmed core values only (#,+,7,8=c,A,D,G,H,U,z,d,y). Fetch R8492 full size (and, in
the same login, the ff.70r-72v / 96r / 97r records' full-size images if served -- fetch and manifest only, no transcription of them).
Pre-register the score (gloss-confirmed core values, a shuffled control) in the folder before the passes. Keep under 30 MB.

### A4-RFVB -- vanbeuningen-dewitt-1657, native-resolution re-read of the code-40/11 positions (cap 5, box 75 min)
NOTES.md image-check line: never re-read on native-resolution line crops (31 code-40 and 17 code-11 positions, 9 [MARK], L63,
L37 pos.10, L44-L46). Route: service.archief.nl IIIF full-resolution (host table: read the item page's drupal-settings-json, then
info.json), else the local 0210/0211 leaves with `tools/iiif_lines.py --image`. One blind pass on the code-40 and code-11 positions
plus L37 pos.10, scored against the registered predictions 40 = a / 11 = n only as a reading, not as a gate unless pre-registered
with a control first. Then `align.py --build` / `decode_key.py --check` if any token changes. (The cheaper NA 3.01.17 EAD step in the
Verdict may be done first if still undone, ~$2, one request.)

### A4-RFHUN -- huntington-blathwayt-madrid-1728, native image check of 849 on BLA188 and the 7/3 distinctions (cap 4, box 60 min)
NOTES.md image-check line. Huntington CONTENTdm native image (host table: CISOSEARCHALL route, dmGetItemInfo; IIIF/getimage at full
size), crop the 849 group on BLA188 and every 7-vs-3 position the glossed pages leave in doubt, one blind pass, compare with the
gloss and key.tsv; regrade affected tokens and `--check`. Also, if still undone and cheap: the Verdict's TNA Discovery API search for
Paretti in SP 94/36 (~$0.5).

### A4-RFHDK -- hessen-daenemark-1672, f.4 crops re-cut and the doubtful tokens re-read (cap 5, box 75 min)
NOTES.md image-check line: crops f4_top.jpg / f4_mid.jpg cited in Cheap test 1 are not on disk; doubtful tokens "6d", "bb", "96" in the
f.4 runs and the 625/774/775 "section counter" exclusion need re-reading on the native image. Re-fetch f.4 (DECODE 4692 full-size route
from A2-HDK, `--guess-fullsize`, or the HStAM route the folder used), cut lines with `tools/iiif_lines.py` (paste the command and the
debug overlay check), one blind pass on the named tokens, record in the folder; the full two-pass transcription (~$11) is NOT this job.
