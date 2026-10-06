# LANE LANE-RUN11-account-2 jobs (account 2) -- 6 Oct 2026 09:1x UTC, lane orchestrator session_01FnWn17w8RS2VEFyTf3Nejv

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

## Wave 1 (spawned 09:1x UTC 6 Oct). Intake gate output (09:1x UTC) pasted per job.

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

## Wave 2 (spawned 09:3x UTC 6 Oct). Wave 1 all done (6 D/D-, workers 17.67). Intake gates as wave 1 (all PASS lines, 09:1x UTC); rubin-1953 and rayburn-2004 below.

### R11-CLIN2380B -- pro3055-clinton-1779, 2380 cipher pp.121-122 (Images 759-760) vs the period decipherment (cap 5, box 70 min)
Continue R11-CLIN2380 (read its NOTES section and PREREG c5d45b736 first) on pp.121-122 exactly as it did p.120: crop (paste the command),
one blind Sonnet pass per page + reconciliation, a PREREG for these pages committed and pushed before scoring, key-consistent count vs
shuffled-plaintext control per page. Record cipher/decipherment conflicts by witness (rule 4). Do not edit AUDIT.md (a verifier,
R11-CLINV3, is working on p.120 there now). Stop before a page that would cross 80% of cap or box.

### R11-CLINV3 -- verifier, pro3055-clinton-1779 R11-CLIN2380 p.120 (cap 2.5, box 40 min)
Verifier, separate from the solver. Check: PREREG c5d45b736 predates the scoring commit 0addfb26e; the gate re-scores (224/258 vs
shuffled max 32); and the three flags of the R11-CLIN2380 ROOM line: (a) the cipher/decipherment conflict after "with us" (cipher
1-7 i + 1-27 -16/-6 "a[m]", the decipherment omits it), (b) the doubled-figure rule L-PP = letter at P twice (6-77, 2-77, 5-22) and
whether it explains GAPS9's 2-99/2-44/6-77, (c) the line-9 OFICERS count -- each by eye from the crops against the 1778 key. Write an
AUDIT.md section (no change to N-class unless the evidence requires; depth fields only if they change) and correct any over-claim in
NOTES.md. Touch AUDIT.md and your own NOTES section only.

### R11-SURTV -- na-suriname-map-1781, the map's tall-v y glyph vs the inv. 373 letter's y-family (cap 3, box 50 min)
R11-SURY's named next (its NOTES section): compare the map's tall-v y glyph (pp.2039/2061 per R11-SURY) with the letter's y-family
tokens by eye from crops (paste the crop command), pre-registered feature list and a permutation control that can differ, to say
whether the map's y (= d, M) and the letter's y-family (m/n by gloss) are the same sign at all. No key change without a passing gate;
any change: decode --check exit 0 and a verifier flag. Update Remaining gaps / Escalation, gaps_check.

### R11-RUBBAU -- rubin-1953, was the Bauer *Unsolved!* print check ever run? (Sonnet 5.5, cap 1.5, box 30 min)
Intake gate: run `python3 tools/intake_gate_check.py rubin-1953` and paste it. R9-RUBIN4's next (NOTES "## Next step (R9-RUBIN4)"):
grep this folder (NOTES, AUDIT, spec, print-check files) and ROOM.md for an actual read of Bauer, *Unsolved!* (2017), Rubin chapter,
for a published transcription or reading. If not run: Google Books API (`&country=US&key=$GOOGLE_BOOKS_KEY`, never print it) and
be-api/IA full-text snippet searches for the Rubin chapter (<= 20 calls, >= 1.5 s), record what is and is not shown; correct the spec's
cheap_test_done note if it mislabels test 2. Report found / not found; do not classify novelty.

### R11-RAYWB -- rayburn-2004, the Wayback retry of the 2006 post and image (Sonnet 5.5, cap 1, box 20 min)
Intake gate: `rayburn-2004: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Escalation "[ ] retry": one CDX query and at most two capture fetches (web.archive.org, `if_` form, >= 1.5 s), record the capture
timestamps and whether the image is byte-identical to the file on disk (sha1). Mark the retry row [x] or [retired]; gaps_check.

### R11-JANSLM -- na-janssens-java-1811, leaf 188 unkeyed codes: held-out fill test (cap 3.5, box 50 min)
RUN10 open item (1, second half): before filling any unkeyed code, test the instrument. PREREG first (committed, pushed): mask a
random 20% of leaf 188's keyed (C) codes, fill them from context with a French word/character LM built from tools/data's French
corpus (era-matched if one exists; say which), and score recovery against a shuffled-context control that can differ; gate stated
in advance. Only if the gate passes, list candidate values for the unkeyed codes as M with their scores (no key.tsv change, no reading
change; a verifier decides). If it fails, log "untestable by this method at this N" in HYPOTHESES.md (rule 3) and stop. AUDIT.md
section 4's Collet crib values stay "found, not applied" unless the gate passes and they agree.

## Wave 3 (spawned 09:5x UTC 6 Oct). Wave 2 all done (5 D, 1 D-), workers so far 30.07. Intake gates as wave 1 (PASS lines, 09:1x UTC).

### R11-CLIN2380C -- pro3055-clinton-1779, 2380 cipher p.122 (Image 760) vs the period decipherment (cap 4.5, box 60 min)
Continue R11-CLIN2380B (its NOTES section, PREREG 4aa284973): p.122's six column crops are already cut. One blind Sonnet pass +
reconciliation, a p.122 PREREG committed and pushed before scoring, key-consistent count vs shuffled-plaintext control; apply the
verified doubled-figure rule (R11-CLINV3) only as a separately reported variant. Conflicts by witness (rule 4). Do not edit AUDIT.md
(R11-CLINV4 is auditing p.121 there now).

### R11-CLINV4 -- verifier, pro3055-clinton-1779 R11-CLIN2380B p.121 (cap 2, box 35 min)
Verifier, separate from the solver: PREREG 4aa284973 predates the p.121 scoring commit; the gate re-scores (406/420 vs control max 45,
and the reported variants); the conflict "cipher lacks 'with the 650 Recruits and Artillery from Europe'" checked by eye on the cipher
crops and the decipherment image, recorded by witness. AUDIT.md section + correct any over-claim in NOTES.md; touch nothing else.

### R11-SURWT -- na-suriname-map-1781, pre-registered word test y = m|n vs y = d on the 2039/2061 readings (cap 3, box 50 min)
The Verdict's cheapest next (R11-SURTV): PREREG first (committed, pushed): decode every 2039/2061 word containing y under y=d, y=m,
y=n (other signs as the current key), score each variant by a Dutch dictionary/LM from tools/data (say which corpus and era) against
a control that can differ (y substituted by random letters at the same positions, many draws). Gate stated in advance. A PASS for one
value is a candidate for a verifier (no key change here); a tie or FAIL leaves y at M with the conflict as logged. gaps_check.

### R11-SURSWP -- na-suriname-map-1781, sampled sweep of the rest of NA 1.05.03 inv. 373 for further glossed cipher (cap 3.5, box 60 min)
R11-SURTV's second next: inv. 373 outside 0600-0796 (0001-0599, 0800-1028), thumbnails at ~600 px via service.archief.nl IIIF,
<= 120 requests, >= 1.8 s, one at a time; 0800-1028 first (after the 29 Oct letter), then 0001-0599, at 1 in 4, contact sheets by
your own eye, a positive control (scan 0693) on every sheet. Record scan numbers of any cipher, gloss or key and stop at 120 requests
with the covered ranges written down. No reading. Append your own NOTES section only (R11-SURWT edits the same folder: rebase first).

### R11-RJMSIB -- rah-juan-manuel-1521, Escalation "[ ] siblings": symbol-shape and table fit against the Sanchez records (cap 3, box 45 min)
Escalation's planned step: compare this folder's alphabet.tsv / sorter tiles with ciphers/rah-salazar-soria-sanchez-1524-28 and
Bourdeau's sanchez1522 (cite, MIT; sparse clone only that target) for shared symbol shapes and nomenclator table fit. Pre-register a
shape-overlap statistic with a control (an unrelated Spanish 1520s cipher alphabet on disk, or shuffled tiles) that can differ.
Report overlap both ways; no key or reading change. Mark the siblings row [x] with the result; gaps_check.

## Wave 4 (spawned 10:1x UTC 6 Oct). Wave 3 all done (3 D, 2 D- at 1.01x), workers so far 42.82; lane ~46.7. Last wave (cap headroom).

### R11-RJMKEY -- rah-juan-manuel-1521, Tomokiyo's published Juan Manuel letter alphabet -> key TSV -> held-out rerun (cap 4, box 50 min)
Intake gate: `rah-juan-manuel-1521: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
The Verdict's cheapest next (R11-RJMSIB): fetch cryptiana.web.fc2.com/code/JuanManuel.png once (descriptive UA), transcribe the table
into key_tomokiyo_alpha.tsv (source column: Tomokiyo, Cryptiana, URL, fetch date; key = `published`, credited; rule 8), compare sign by
sign with alphabet.tsv (agreements/conflicts listed by witness, rule 4). Then a PREREG (committed, pushed) for scripts/test1.py's
held-out branch run with the published table in place of the in-house alphabet, gate unchanged from test 1, plus a shuffled-key control
that can differ; report both numbers. Note in NOTES.md that a published key means a published decipherment may exist (rule 1 risk) and
flag for a verifier; do not classify novelty. A PASS licenses no reading change here (verifier first); gaps_check.

### R11-CLINV5 -- verifier, pro3055-clinton-1779 R11-CLIN2380C p.122 (cap 2, box 35 min)
As R11-CLINV4 did for p.121: PREREG e2861d54e predates the p.122 scoring commit; the gate re-scores (242/252 vs control max 32;
variants 247); the conflicts (move/movements, Chesapeak/Chesipeak, infavor/o f division, the P.S. lacking the Europe clause) checked
by eye, recorded by witness. AUDIT.md section + correct any over-claim; touch nothing else.

