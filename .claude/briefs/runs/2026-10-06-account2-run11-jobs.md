# LANE LANE-RUN11-account-2 jobs (account 2) -- 6 Oct 2026 09:2x UTC, lane orchestrator session_01FnWn17w8RS2VEFyTf3Nejv

Lane brief: .claude/briefs/default-lane.md (cap 60, box 09:11-19:11 UTC 6 Oct). WORK-QUEUE row LANE-RUN11-account-2: same tier as
RUN9/RUN10 -- RUN10's named next steps for this split (STATUS.md "LANE LANE-RUN10-account-2 handoff", "Open for the next i-r lane"),
then tools/next_steps.py runnable rows (S, M) and `parallel` actions. Folders i-r (account 1 a-h, account 4 s-z). VERIFY-BACKLOG.tsv
has no i-r row (09:1x UTC). Off limits: Birago (incl. nevers-birago-fr3251-1572), Armstrong, Debosnys; riksarkivet-r4282-1628.
Gate 0a: SESSION-SWEEP-account-2 row still `claimed`, its TSV (2026-10-05) on disk; RUN7-RUN10 proceeded past it the same way.
Every worker: Opus 5.5 (Sonnet only where stated), one job, then stop. Each job first checks that its named step is still undone (a
dated NOTES.md section may already have run it); if so, stop and report rather than inventing work.

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim
  line with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE LANE-RUN11-account-2".
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
  found; do not classify novelty (verifier jobs excepted, where the brief says).
- Stop at the cap or at 80% of the box, whichever first; do not start a unit that would cross 80% of either. A stop with work half
  done writes what was done and what remains into the folder's files. An Opus session floor is about 1.5; caps below assume it.
- Vision work: crop step mandatory and pasted (`tools/iiif_lines.py --image FILE --out DIR` or the --ark/--canvas form); give
  subagents only crop paths, one page/leaf per call, never a full-page image. Price: ~1.5 per Sonnet subagent pass, reconciliation = 1 unit.
  Thumbnail/contact-sheet triage by the worker's own eye at low resolution is allowed for locating pages.
- Sorters: any sorter meant for the owner must PASS `python3 tools/sorter_preflight.py` and have 5+ random tiles opened against the line
  image; it is handed to the account-3 orchestrator (ROOM flag line) to publish. Never publish an artifact or edit ASKS.md yourself.
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE LANE-RUN11-account-2",
  then a five-line final report.

## Wave 1 (spawned 09:2x UTC 6 Oct). Intake gate output (09:1x UTC) pasted per job.

### R11-JANS26TX -- na-janssens-java-1811, invnr 26 scans 10-11 (second signed copy of dispatch No.1) two-pass transcription vs leaf 188 (cap 5, box 70 min)
Intake gate: `na-janssens-java-1811: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
RUN10 (R10-JANS26..D) found invnr 26 scans 10-11 to be a second signed copy of No.1's cipher (5 extra leading codes, no gloss). Fetch
the two scans once at native IIIF resolution (service.archief.nl, <= 20 requests, >= 1.8 s), cut line crops with tools/iiif_lines.py
(paste the command), two blind Sonnet passes (one page per call, crops only) + your reconciliation (4 units at ~1.5 each incl. floor).
Then align the copy group by group against leaf 188's ciphertext.tsv (script, committed): count agreements, list every disagreement
with both readings, and say which side the image supports where leaf 188's own grade is M or a digit is doubtful. A copy that settles
a leaf-188 digit is a transcription correction (corrections.tsv, decode --check exit 0, flag for a verifier); no new key values unless
the copy carries something leaf 188 lacks. Pre-register the agreement statistic and a shuffled-order control (the control must be able
to differ: alignment agreement depends on order) before scoring. Update Remaining gaps / Escalation, gaps_check.

### R11-SURY -- na-suriname-map-1781, dot-level zoom of the inv. 373 0692-0693 y-family tokens (m vs n) against the map's y = d (cap 3, box 50 min)
Intake gate: `na-suriname-map-1781: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
The Verdict's cheapest next (R10-SURV): the y-family tokens in passes/inv373_0693_r10/ (m 12 / n 9 by the interlinear gloss) -- zoom
each at native resolution (crops already in passes/inv373_0693_r10/crops or recut with tools/iiif_lines.py; paste the command) and
record whether a dot/stroke feature separates the m-glossed from the n-glossed tokens. Pre-register the feature and the test (feature
vs gloss agreement, label-permutation control) before scoring. Then say what the result means for the map key's y = d (M): settle,
leave M, or flag a conflict (rule 4: record witnesses, no majority vote). Any key change: decode --check exit 0 and a verifier flag.

### R11-ROELL13 -- roell-vandedem-1809, the States General's received copy of Van Dedem's 9 Feb 1793 despatch (NA 1.01.02, Levantse lias 1793) (cap 3, box 50 min)
Intake gate: `roell-vandedem-1809: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
NOTES.md tail cheapest next (1): find the NA 1.01.02 inventory number for the Levant/Turkish lias of 1793 (NA item pages /
drupal-settings-json, <= 40 requests to nationaalarchief.nl + service.archief.nl, >= 1.8 s), locate the 9 Feb 1793 Van Dedem
despatch by bisection, and say whether the received copy is enciphered and whether its form matches DECODE R1469/R1470 (pages, opening,
"Monsieur", groups). If it is a cipher original, record scan numbers and a 1-line description; do not decode. Update the Verdict.

### R11-RJMLA -- rah-juan-manuel-1521, look-alike pass on the f.194 (88) + f.199 (114) split symbol tokens (cap 5, box 60 min)
Intake gate: `rah-juan-manuel-1521: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Remaining gaps item 2 / Escalation retry: the two passes split over the 10% line, so per CLAUDE.md Usage 6 run tools/lookalike_pass.py
(read its --help) on the disagreements marked ~ in ciphertext_f194_reconciled.tsv and ciphertext_f199_reconciled.tsv, crops only
(paste the crop command), then write what machines still split into the sorter's focus.tsv for the owner (do not publish; flag the
account-3 orchestrator if the sorter needs a rebuild, sorter_preflight PASS first). The 2-of-3 residual is agreement, not accuracy:
report it as such, never as reader error. Do not rerun test 1 (it waits on ASKS 138). Update Remaining gaps / Escalation, gaps_check.

### R11-MORNER -- ra-morner-welin, Esplunda inventory (Google Books Kok4AAAAIAAJ) snippet queries around volume 153 (Sonnet 5.5, cap 1.5, box 30 min)
Intake gate: `ra-morner-welin: open (line 3) -- edition/page or full-text-search citation found within 6 lines`.
NOTES.md "## Next step (NO-CRACKS)": Books API (`&country=US&key=$GOOGLE_BOOKS_KEY`, never print the key) snippet queries inside
volume Kok4AAAAIAAJ (`volumes/Kok4AAAAIAAJ` + `q=` searchInfo, or `volumes?q=...` restricted by id), <= 30 calls, >= 1.5 s: settle
whether "Welin - Ostergren" is a surname range and whether any volume notes chiffer/chiffrerade/nyckel/kryptering. Record each query
and snippet in a TSV; the copy order stays in REQUEST.md. Update the While waiting / Next step section and the Verdict line.

### R11-CLIN2380 -- pro3055-clinton-1779, 2380 cipher columns vs its period decipherment on the 1778 book key (cap 5.5, box 70 min)
Intake gate: run `python3 tools/intake_gate_check.py pro3055-clinton-1779` and paste it; stop if nonzero.
RUN10 open item (4): the same method as R10-CLIN3868/B (read those NOTES sections and their PREREG files first): 2380's cipher cells
checked one by one against the period decipherment (Tomokiyo: f.134-) on the 1778 key. Locate the 2380 cipher and decipherment images
already on disk (images/manifest.json) or fetch once; crop (paste the command); one blind Sonnet pass per page + your reconciliation;
PREREG (key-consistent count vs shuffled-plaintext control) committed and pushed before scoring. Record any cipher/decipherment
conflict by witness (rule 4), no majority. Stop before a page that would cross 80% of cap or box; write what remains.

