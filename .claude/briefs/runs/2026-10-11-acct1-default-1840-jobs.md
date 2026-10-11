# LANE DEFAULT-account-1-20261011-1840 jobs (account 1, lane orchestrator session_01GJw2dpLAYEhjSmYwRDBvs5) -- 11 Oct 2026 19:0x UTC

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 18:40 11 Oct - 04:40 UTC 12 Oct (80% line 02:40). Gate 0a:
SESSION-SWEEP-account-1 stale-claimed since 5 Oct, proceeded (as every incarnation since).
Backlog read 18:4x-19:0x UTC: VERIFY-BACKLOG.tsv high rows were Birago (off limits) plus 10 eckert-1864 rows that are N1 (text in
print); verify_backlog.py read the class only from `novelty`/`class`, so those N1 rows sat at high -- fixed this lane (77f24bb33, the
class is also read from `plaintext_novelty`/`grade`, + offline test); after the fix only Birago is high. `next_steps.py --hot-only`:
most `parallel` cells are stale on reading the folders (brochado crossed-t BRO-CT done, blathwayt BLA-TRY done, fr17 corpus exists,
bne20211 R1180 login done); Gallica 403 (probe 18:5x UTC, 1 request), so every Gallica step is out. be-api 200 (1 probe).
Exclusions: Birago, Armstrong, Debosnys; no live (< 6 h, no done) claim on any folder below (ROOM last 600 lines read 18:5x UTC).

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-09-ytbiz-family-1310-jobs.md` (read it in full), with
these substitutions: address every ROOM line "for LANE DEFAULT-A1-1840 (account 1)"; the hosts line of each job below replaces the
"No Gallica" hosts bullet there (still no Gallica, no HTRC). Halfway line: one ROOM line at half the box or half the cap, whichever
first (skip if done before). `get_session` is not available to you: say "cost not visible to this session" in the done line.
Intake gate run by the lane at 19:0x UTC for each target below: `<slug>: partial (line N) -- edition/page or full-text-search citation
found within 6 lines`, exit 0 (eckert-1864, fr4712-nevers-duchesse, thurloe-printed, wvo-hessen-1564, fr16045-pisany-rome-1585).

## Wave 1 (19:0x UTC 11 Oct)

### ECK-S65G (Opus, cap 3, box 75 min): eckert-1864, the FM-S65B Remaining gaps (NOTES.md l.6948-6963)
Hosts: archive.org be-api / IA full text, googleapis (key + country=US; one try per query, 503/429 stops the host), hdl.huntington.org
(CONTENTdm per CLAUDE.md, >= 3 s, page images at 2400 px). Units: (1) the three whole-collection be-api phrase checks for E590 (Seward),
E592 (Cammann), E593 (ponchos), ~0.1; (2) Grant Papers vol. 14 snippet sweep for E589, E591, E593, E594 and the page of the 5914/2 hit,
~0.2; (3) Sherman's family letters (Thorndike 1894) IA full-text check for E594 after a title-page/identifier check, ~0.1; (4) image
check of pages 348, 352, 364, 366, 392, 397: one 2400 px look per page, strip crops only (`tools/iiif_lines.py --image`), compare the
header and code words with the filed rows, ~0.15 each. Solver-side print check: report what was found and where it was not found; do
not classify novelty, do not edit AUDIT.md classes (a print hit goes in NOTES.md and a ROOM line for the verifier). Update FM-S65B's
Remaining gaps / Escalation by a dated replacement section; gaps_check.py.

### F4712-K71 (Opus, cap 3, box 90 min): fr4712-nevers-duchesse, key no.71 on f.10r's 37 numbers with a matched control
The Escalation's known-keys rung (V1-F4712, NOTES.md l.435): key no.71 (BnF fr.3995 f.133r, Nevers collection; f.7r of fr.4712 is its
period pair per NOTES.md l.28) on the f.10r tokens (`ciphertext_f10_digits.tsv` / the S1 segmentation used by f13_carry.py). Disk only,
no network. The no.71 alphabet is already transcribed as `ciphers/birago-fr3252-1571-72/keys/key_fr3995_no71_f133r.tsv` (24 letter
codes H, 2 M; BIRAGO-NUM-KEYEYE3) with its native crop `ciphers/birago-fr3252-1571-72/images/fr3995/read_f133r.jpg`: READ those two
files only, copy what you use into this folder (`keys/key_no71.tsv`, with provenance), and never write anything in a Birago folder.
The word columns (two-figure codes reused with a dot/overline) are only partly transcribed: say which f.10r tokens fall on unread word
codes rather than guess. PREREG-F4712-K71.md pushed before any score: the statistic (e.g. fr16 judge or dictionary-word coverage of the
letter-code decode), the matched control (same N=37, a no.71-shaped key on shuffled/fr16 plaintext, and the target decoded under
shuffled keys), gate and what counts as a non-test (rule 3: check the control can differ on the statistic; at N=37 a non-test is the
likely answer and is a result). Grade per token (rule 4), decode script with --check (rule 7). Units: key copy + PREREG 0.5, decode +
controls 1, write-up 0.5.

### THUR-NIJ (Opus, cap 2.5, box 75 min): thurloe-printed, three text/image-route gaps of THUR-REST (NOTES.md l.3837-3856)
Hosts: archive.org only (metadata, djvu text, page images through the IA image service; `IA take`/`IA release` lines). Units: (1) Nijhoff
Bijdragen X p.291: identify "Tiende deel" among the IA `bijdragenvoorva*` items dated 1848-1856 by metadata then title page (about 8
requests), and if found read p.291 against Birch I p.340, ~0.4; (2) Van Sypesteyn p.213: one leaf of `geschiedkundige00sypegoog`, strip
crops, image-check the p.351 run numerals (run 4's omission and runs 5, 7-11), ~0.4; (3) the code-94 conflict: image-check one glossed
Bamfylde run of vols 4-6 whose gloss line the OCR dropped (span list in THUR-356) for Tomokiyo's 94 = t instance, ~0.6. Correction
of record only; no code value enters a key without its own image read (rule 4 grade). Dated section + Remaining gaps/Escalation.

### WVO-DEDUP (Opus, cap 2, box 60 min): wvo-hessen-1564, the duplicate recut tiles step (NOTES.md l.1121-1135)
Disk only. Write a dated dedupe list in realign/ and a PREREG note (pushed first) that names it as a change of token stream, not of
labels; drop one copy of each of the 5 same-pile pairs; put the 2 cross-pile pairs (C06 009/010, C09 018/019; k03 vs k23) as focus
rows for the owner (sorter focus.tsv per the folder's convention, never blocking); re-run realign/ under PREREG-WVO-REALIGN with its
within-row control; report AGREE before/after against the control p95; re-look C09_01_025 once (strip crop). `--check` scripts exit 0.

### PISA-T475 (Opus, cap 2, box 60 min): fr16045-pisany-rome-1585, per-token compare of the UNSETTLED T47/T57/T45 tokens
The Verdict's cheapest next (NOTES.md l.1090: "a per-token compare of the UNSETTLED T47/T57/T45 tokens (key86 T45/T47/T49/T57 row),
disk only, ~$1"). Disk only. Read PISA-T31, UNA3-PISA and PISA-T32 first and reuse their instrument (committed crops, sheet, known-answer
tiles); PREREG before any reader call; a relabel is committed only if its re-score gate passes as in PISA-T31; f.244r and f.275r both.
Correction of record on a leaf whose plaintext is known by the copy letter.

Known-text share (owner's guardrail): THUR-NIJ, WVO-DEDUP and PISA-T475 work on leaves whose text is known, but each corrects a record
(a transcription or key cell), the guardrail's allowed case; the lane counts them separately and states the share in the close line.
