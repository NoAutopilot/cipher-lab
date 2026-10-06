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
