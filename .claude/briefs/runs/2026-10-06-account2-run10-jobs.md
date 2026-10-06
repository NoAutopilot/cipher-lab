# LANE LANE-RUN10-account-2 jobs (account 2) -- 6 Oct 2026 07:2x UTC, lane orchestrator session_01Fnnf2KFqUKZG3cpVKRD9tL

Lane brief: .claude/briefs/default-lane.md (cap 60, box 07:12-17:12 UTC 6 Oct). WORK-QUEUE row LANE-RUN10-account-2: RUN10, same tier as
RUN9 -- RUN9's named next steps for this split (STATUS.md "LANE LANE-RUN9-account-2 handoff", "Open for the next i-r lane"), then
tools/next_steps.py runnable rows (S, M) and `parallel` actions. Folders i-r (account 1 a-h, account 4 s-z). VERIFY-BACKLOG.tsv has no
i-r row needing a verifier (07:2x UTC). Off limits: Birago (incl. nevers-birago-fr3251-1572), Armstrong, Debosnys; riksarkivet-r4282-1628.
Gate 0a: SESSION-SWEEP-account-2 row still `claimed`, its TSV (2026-10-05) on disk; RUN7-RUN9 proceeded past it the same way.
Stale NEXT-STEPS cells checked and dropped (already run): naf14913 f.206r phrase search (NOTES ~l.1592), rah-juan-manuel BHO date map
(RUN3-RJM), lambeth-bacon Baconiana page check (D2-BACON), konstanz Pallain/Bailleu/Guyot (R8-KONS, R9-KONS2).
Every worker: Opus 5.5 (Sonnet only where stated), one job, then stop. Each job first checks that its named step is still undone (a
dated NOTES.md section may already have run it); if so, stop and report rather than inventing work.

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim
  line with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE LANE-RUN10-account-2".
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
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE LANE-RUN10-account-2",
  then a five-line final report.

## Wave 1 (spawned 07:2x UTC 6 Oct). Intake gate output (07:2x UTC) pasted per job.

### R10-ROELL9 -- roell-vandedem-1809, NA 1.02.20 inv. 980, Testa's 10 Feb 1809 copy to Van Dedem (cap 2.5, box 40 min)
Intake gate: `roell-vandedem-1809: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
R9-ROELL8's cheapest next (NOTES.md tail): inv. 980's 10 Feb 1809 copy to Van Dedem compared against R1469's length and form (one or two
scans), then the question whether R1469 is an incoming letter *to* the legation rather than an outgoing one. Locate the Feb 1809 run in
inv. 980 by bisection (as R9-ROELL8 did in inv. 978: item page's drupal-settings-json for the scan list, service.archief.nl IIIF at
~1000 px, <= 30 requests, >= 1.8 s apart). Read the 10 Feb item: date, addressee, address form, length, any cipher or "en chiffre" note.
Compare with R1469 (7 pages, "Monsieur", 9 Feb) and say whether inv. 980 shows R1469 to be a copy, a different letter, or nothing.
Update the Verdict line (status stays `open` unless a check-solved rule calls otherwise). No subagents needed.

### R10-SUR -- na-suriname-map-1781, (a) [sigma] reader-code split, (b) inv. 373 index triage (cap 4, box 70 min)
Intake gate: `na-suriname-map-1781: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
(a) The Verdict's cheapest next (R8-SUR3): split reader code [sigma] into two codes in ciphertext_2077_legend.tsv (script, no vision):
R7-SUR2 logged [sigma] as two look-alike signs (L11:17 vs L10:66). Do it by a committed script with the rationale, keep the original
column, rerun the decode --check (exit 0) and report any token whose grade moves (it should not move without evidence; a split that
changes a reading goes to the verifier flag). (b) RUN9's lead (R9-SURKEY): NA 1.05.03 inv. 373 (governor's 1781 letters, 1,030 scans,
digitised), unopened. Triage only: fetch the scan list, look at any index/inventory pages at the head and a sampled contact sheet (1 in 20,
<= 50 requests to service.archief.nl, >= 1.8 s), and say whether enciphered letters, a key or a cipher reference to the 1781 map appear;
record scan numbers for any hit. No reading of cipher, no subagents. Update Remaining gaps / Escalation and gaps_check.

### R10-OBREDV -- oldenbarnevelt-brederode-1605, VERIFIER of R9-OBRED4's corrections file (cap 2.5, box 40 min)
Intake gate: `oldenbarnevelt-brederode-1605: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
You are a verifier, a separate session from the solver (R9-OBRED4). RUN9 handoff item (4): apply imagecheck_1490/corrections.tsv only with
a verifier's say. Check the two entries (170 -> 179 differing; one blotted group) against the inv. 1490 scan crops already on disk (re-crop
with tools/iiif_lines.py --image from the stored scan if needed; your own eye on the crop, one look per entry, plus one look at a
same-scan 0/9 exemplar as a control). Verdict per entry: uphold / reject / undecidable, with reasons, written to the folder (AUDIT.md
section "Verifier: R9-OBRED4 corrections", or the corrections file's verdict column). Do NOT edit ciphertext.txt (never silently
repaired); state which tests on disk would change if the correction is applied. No novelty class is asked here.

### R10-OBRED98 -- oldenbarnevelt-brederode-1605, locate the 10 Aug 1598 key in NA 3.01.14 inv. 2016 (cap 3.5, box 60 min)
Intake gate: as R10-OBREDV. A concurrent verifier session (R10-OBREDV) works the corrections file in the same folder: touch only your own
new files and append your own dated NOTES.md section; rebase before push.
NOTES named next (1): NA 3.01.14 inv. 2016 (Van Aerssen to Oldenbarnevelt, 1598; "Bij de missive van 1598 augustus 10 bevindt zich een
sleutel"), 81 scans, thumbnails first. Locate the key leaf (contact sheets at low resolution, then the candidate scans at ~1400 px; <= 60
requests to service.archief.nl, >= 1.8 s). If found: store it with a manifest, describe its design (number ranges, nomenclator lists, any
three-digit names list), and run a pre-registered fit test against this folder's ciphertext only if it is a plausible design match
(PREREG first, shuffled-key control, both numbers in HYPOTHESES.md); otherwise record the design and why it does not match. Note whether
inv. 2016 also carries deciphered letters (a sibling with a period decipherment is the higher-value find). No subagents unless a key-table
transcription is needed (then crops only, one pass ~1.5).

### R10-JANS26 -- na-janssens-java-1811, invnr 26 page-through (gap 3), one 60-request session (cap 4, box 60 min)
Intake gate: `na-janssens-java-1811: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Verdict's cheapest next: the invnr 26 page-through (gap 3; sampled 1 in 8 only so far), contact sheets with the leaf-188 positive control on
every sheet, as GAPS10-GAPS16 did for invnrs 12 and 7 (same scripts, read their sections first). Looking for: dispatch No.1's cipher, its
decipherment, a plain copy, or a Paris-side translation, or any further glossed Janssens cipher leaf. One session = <= 60 requests to
service.archief.nl, >= 1.8 s apart; record which scans were paged and which remain. Any hit: fetch at 1200 px, describe, record scan
numbers; no transcription in this job. Update Remaining gaps / Escalation / Verdict and gaps_check.

Wave 1 sessions (07:20 UTC): R10-ROELL9 session_01Cagb6db2peK3oexuGJkRyQ; R10-SUR session_01Nt4mHFoFvhGfhLCgCS3TL8; R10-OBREDV
session_0193bQtSBPEJ81F2fQ8Q43R7; R10-OBRED98 session_01JQLminjbY4FrRFVuk7J2EC; R10-JANS26 session_01C9XxTVekJp3AQYSZCSp5pr.

## Wave 2 (written 07:2x UTC 6 Oct, spawned at the first check-in with free slots)

### R10-KAL7 -- kaliningrad-2015, a judge statistic the shuffle control can separate (cap 3, box 60 min; disk and CPU only)
Intake gate: `kaliningrad-2015: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
NOTES "Next steps" (R9-KAL6): ru19_soft cannot tell this target's two-stage decode from its shuffle at N 978 (-1.733 vs -1.765). Named
different instrument: a word-segmentation rate of the decode against a Russian lexicon (built from tools/data/ru19*, held out from any
corpus the decoder used), with the decode of the *shuffled* target through the same family as its control. Pre-register (PREREG committed
before scoring): the statistic, the lexicon, the gate (target above the shuffled-decode p95 over >= 20 shuffles), and a positive control
first -- a synthetic of this target's N, K and design in Russian through the same two-stage decoder must clear the gate (if it does not,
CONTROL BELOW GATE: stop, log non-test). Check the CLAUDE.md rule-3 clause: the shuffle control must be able to differ on this statistic.
Both numbers to HYPOTHESES.md (tools/family_run.py if it supports the option; otherwise the same row shape). This is the second instrument
on the S3' design; record it as such. No reading claimed beyond what the gate licenses.

### R10-CLIN3868 -- pro3055-clinton-1779, 3868 cipher columns vs its read decipherment (cap 5, box 75 min)
Intake gate: `pro3055-clinton-1779: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Verdict's cheapest next: the cell-by-cell check of the 3868 cipher columns 3-6 of p.382 and pp.383-384 (LAC reel H-1649 Images 1031-1032)
against its read decipherment, on the 1778 book key. Plan: 3 page units; crops via tools/iiif_lines.py --image (paste the command), one
blind Sonnet pass per page on crops (~1.5 each) + one reconciliation unit = ~6, so work p.382 cols 3-6 first, then 383, and stop before a
unit that would cross 80% of cap or box. Apply the key with the folder's existing scripts; report per-cell agreement with the decipherment
(grade H for key-consistent cells), any cell where the encipherer erred (Tomokiyo notes -1 letter-position slips on 2380), and update gap
3 / Verdict. Keep images/h1649 under 30 MB (crops to scratchpad unless cited).

Wave 1 results (check-in 07:37 UTC): all 5 D, workers 10.67 (get_session). Follow-ups below.

### R10-SUR693 -- na-suriname-map-1781, gap 6: inv. 373 scan 0693 cipher + interlinear pair (cap 4, box 60 min)
Intake gate: `na-suriname-map-1781: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Gap 6 (R10-SUR): fetch inv. 373 scans 0690-0696 at ~2000 px (<= 10 requests, service.archief.nl, >= 1.8 s), identify the letter (date,
sender, place). Crop the cipher lines (tools/iiif_lines.py --image, paste command), transcribe cipher + interlinear plain (one blind Sonnet
pass on crops ~1.5 + your reconciliation = 1 unit). Then the key question: is this the same sign system as the 1781 map key (inv. 86 /
key.tsv)? Compare sign inventories by script; if it is, test the pair against key.tsv per sign (agreements, conflicts) and say which of the
map's U/M signs it would settle -- no key.tsv edit in this job, write a candidate file and flag for a verifier. If budget remains below 80%,
a 1-in-3 sweep of 0600-0800 for more passages (contact sheets, <= 30 requests). Update gap 6 / Verdict, gaps_check.

### R10-JANS26B -- na-janssens-java-1811, invnr 26 page-through scans 59-191 (cap 4, box 60 min)
Intake gate: `na-janssens-java-1811: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Continue R10-JANS26 (invnr26_scans.tsv on disk): scans 59 onward, same method (contact sheets with the leaf-188 positive control), one
session of <= 60 requests; record paged/remaining. Any No.1 decipherment, plain copy, translation or further glossed cipher leaf: fetch at
1200 px, describe, scan numbers; no transcription. Update gap 3 / Verdict, gaps_check.

### R10-ROELL10 -- roell-vandedem-1809, NA inv. 990 (Van Dedem to Testa) early Feb 1809 (cap 2.5, box 40 min)
Intake gate: `roell-vandedem-1809: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
R10-ROELL9's next: R1469 may be an incoming letter to the legation. Find NA inv. 990 (check the inventory number and its description on
the item page first), bisect to late Jan - mid Feb 1809 (<= 30 requests, >= 1.8 s), and look for a 9 Feb 1809 item, a 7-page "Monsieur"
letter, or any cipher. Compare with R1469's form; update the Verdict line.

Wave 2 sessions: R10-KAL7 session_01SQZH6fzyyk2YQy7ii2tJcp (07:21); 07:38 UTC: R10-SUR693 session_01GDgp2uN23R4v4zh8GwzAqL; R10-JANS26B
session_019rGqipBasrN8CtjYxc9mv1; R10-ROELL10 session_0162ekU79BtHvtNvfvvL6XZ1; R10-CLIN3868 session_01NyhwwQnzUjyPXFiGNrJCoi.

Wave 2 results (check-in 07:56 UTC): 4 D, 1 D- (R10-SUR693 1.10x), workers 12.85; lane ~26.8 of 60 (get_session).

## Wave 3 (spawned 07:5x UTC 6 Oct)

### R10-SURV -- na-suriname-map-1781, VERIFIER of R10-SUR693's candidates_0693.tsv (cap 3, box 50 min)
Intake gate: `na-suriname-map-1781: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
You are a verifier, separate from the solver (R10-SUR693). Check passes/inv373_0693_r10/ (transcription, PREREG, scoring, candidates_0693.tsv)
against the scan crops: (1) the PREREG predates the scored run (git log times); (2) re-run the scoring script, same numbers; (3) eye-check
each candidate value's occurrences on the crops (one look per sign class, plus one control look at an already-keyed sign); (4) per candidate:
uphold (grade C, from the interlinear known plaintext) / M / reject, with reasons. Only for upheld candidates: apply to the map key the way
the folder already records key changes (key.tsv / exceptions, with a source column naming inv. 373 0692-0693), rerun the decode --check
(exit 0), and report the 2077 grade counts before/after. A reading change after AUDIT.md: write it into AUDIT.md and any SECOND-OPINIONS
row (rule 10 propagation). No novelty class asked here. Update Verdict / gaps_check.

### R10-CLINV -- pro3055-clinton-1779, VERIFIER of R10-CLIN3868 (cap 2, box 40 min)
Intake gate: `pro3055-clinton-1779: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Verifier, separate from R10-CLIN3868. Check its PREREG predates the scored run; re-run the scoring; eye-check the "digby" cells
(11-6 4-2 11-9 1-1 16-6) on the crop against the 1778 key and the p.385 copy-book "Darby"; decide: an encipherer/copyist discrepancy to
record as a data conflict (rule 4: record witnesses, do not settle by majority) and whether the reading file's word changes (if so,
propagate into AUDIT.md and SECOND-OPINIONS rows). Write an AUDIT.md section. A concurrent worker (R10-CLIN3868B) works pp.383-384 in the
same folder; touch only AUDIT.md and your own notes section.

### R10-CLIN3868B -- pro3055-clinton-1779, 3868 pp.383-384 cells (cap 4.5, box 60 min)
Intake gate: as R10-CLINV. Continue R10-CLIN3868 (read its NOTES section and PREREG first; reuse its scripts and gate): pp.383-384 (Images
1031-1032), crops by tools/iiif_lines.py --image (paste), one blind Sonnet pass per page (~1.5) + reconciliation; stop before a unit that
would cross 80% of cap/box. Same reporting. A verifier session (R10-CLINV) edits AUDIT.md concurrently: do not touch AUDIT.md.

### R10-JANS26C -- na-janssens-java-1811, invnr 26 scans 117-191 (cap 2.5, box 45 min)
Intake gate: `na-janssens-java-1811: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Finish the invnr 26 page-through (R10-JANS26/26B method, <= 60 requests). Then update gap 3: with invnr 26 done, say which page-throughs
remain anywhere (if none, the gap's verdict).

### R10-ROELL11 -- roell-vandedem-1809, the archival source of DECODE R1469/R1470 (cap 2.5, box 40 min)
Intake gate: `roell-vandedem-1809: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
R10-ROELL10's next: neither Testa/Van Dedem direction holds R1469. Find which archive file DECODE's R1469/R1470 images come from: the
DECODE record metadata (tools/decode_list.py login-free listing; record page fields: archive, shelfmark, folio, provenance notes), and the
folder's own earlier notes. Then, if it names an NA inventory number not yet read, check its item page for digitisation (drupal-settings
availability) and locate 9 Feb 1809 (<= 25 requests). Report the provenance found and whether the original is reachable. No login unless
the listing lacks the field (then one browser login per CLAUDE.md, fetch only R1469/R1470 metadata).

Wave 3 sessions (07:57 UTC): R10-SURV session_01Tg6hSrwYMSZreAqcZkkt2Z; R10-CLINV session_0174edi7AK17rH9B9j33WV82; R10-CLIN3868B
session_01PGMWyUH1k9eUUy7hNXxSpR; R10-JANS26C session_01VQVmsMnHzSQK7Uz8wdnxWM; R10-ROELL11 session_01Xw2JXwAvVqTxbK15Gi6rz4.

Wave 3 results (check-in 08:16 UTC): 2 D, 3 D- (CLINV 1.08x, CLIN3868B 1.05x, ROELL11 1.45x), workers 14.84; lane ~42.5 of 60.

## Wave 4 (spawned 08:1x UTC 6 Oct; last wave, lane reserve held for close)

### R10-ROELL12 -- roell-vandedem-1809, R1469/R1470 groups vs R2131 (Van Dedem 9 Feb 1793) and the inv. 804 clear copy (cap 2.5, box 40 min)
Intake gate: `roell-vandedem-1809: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
R10-ROELL11's inference (not established): R1469 may be Van Dedem's 9 Feb 1793 despatch, not 1809. Test it on disk first: compare R1469/R1470
code groups and layout with R2131 (same code family?) and, if this folder or a sibling holds a key for that family, whether R1469 decodes
against the inv. 804 clear copy (scans 150R-152R) -- pre-register the comparison (PREREG pushed first) with a shuffled control that can vary on
the statistic (e.g. group-overlap or crib-alignment score vs shuffled-copy alignment). If the date is wrong, say so in NOTES with the
evidence and leave the folder rename/status to the orchestrator (flag in ROOM). Report both numbers.

### R10-CLINV2 -- pro3055-clinton-1779, VERIFIER of R10-CLIN3868B's three words (cap 2, box 35 min)
Intake gate: `pro3055-clinton-1779: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Verifier, separate from R10-CLIN3868B. Check its PREREG predates the score (10e0744a4 vs 12d7b9f85/854780ec0), re-run the scoring, eye-check
the cells for "to the kings peace", "Floquet" (q in clear) and "Cord" (21-1 21-2 21-3 21-8) on the crops against the 1778 key, and decide
whether passes/p385_reading.txt's three M words change (if so: edit, --check exit 0, propagate into AUDIT.md and any SECOND-OPINIONS row).
AUDIT.md section. No novelty class.

### R10-JANS26D -- na-janssens-java-1811, invnr 26 scans 177-191, then close gap 3's page-through (cap 2, box 30 min)
Intake gate: `na-janssens-java-1811: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Last 15 scans (R10-JANS26 method, <= 20 requests). Then write gap 3's state: invnrs 12, 7, 26 paged end to end; what (if anything) is left
for the dispatch No.1 key source, and its blocker. Verdict line + gaps_check.

Wave 4 sessions (08:16 UTC): R10-ROELL12 session_01Hn3gXWzehejCLrRvER3Rr3; R10-CLINV2 session_013oWCgg2otfyQbkQsVBwV98; R10-JANS26D
session_01DJBsTw8HRnQZWvr6T7Mdih.
