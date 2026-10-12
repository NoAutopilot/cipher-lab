# LANE DEFAULT-account-1-20261012-0640 jobs (account 1, lane orchestrator session_01AhQnmdAixZkfUZroT9XWrF) -- 12 Oct 2026 06:4x UTC

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 06:40-16:40 UTC 12 Oct (80% line 14:40). Gate 0a: SESSION-SWEEP-account-1 row
stale-claimed since 5 Oct 2026; proceeded, as the 11 Oct incarnations did. Backlog read 06:4x UTC: VERIFY-BACKLOG.tsv high rows are Birago only
(off limits); its audit2 rows are N0/N1 (gate 2 does not apply; LANE DEFAULT-A2-0510 read the same). `next_steps.py --hot-only` runnable rows:
Gallica answers 403 to the manifest (06:45 UTC), which removes baluze167, fr4712, fr3985, fr5160, fr3993, colbert26, gramont, ceppo; Birago and
Armstrong are off limits; pro3055-clinton's open rows are key checks on text-known items (guardrail). Google Books API answers 200 (06:47 UTC).

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-09-ytbiz-family-1310-jobs.md` (read it in full), with these
substitutions: address every ROOM line "for LANE DEFAULT-A1-0640 (account 1)"; the hosts bullet below replaces the one there. Halfway line:
one ROOM line at half the box or half the cap, whichever first (skip if done before). `get_session` is not available to you: say
"cost not visible to this session" in the done line. Check 1 before any unit: grep the folder's NOTES.md for a later section that already
ran the unit; if it did, one ROOM line and skip that unit.
Hosts this wave: www.googleapis.com/books/v1 (ECK-GP13C only; always `&country=US&key=$GOOGLE_BOOKS_KEY`, >= 2 s, one retry after 60 s on
429/503 then stop); www.delpher.nl / resolver.kb.nl (THUR-57 only, <= 6 requests, >= 2 s); archive.org ("IA", GUALT-HMC only, <= 12 requests,
>= 1.5 s, take/release lines). PISA-244 is disk only. No Gallica.

## Wave 1 (06:5x UTC 12 Oct)

### ECK-GP13C (Sonnet, cap 1, box 25 min): eckert-1864, the rest of the Grant Papers vol. 13 pass
NOTES.md "## Remaining gaps (ECK-GP13B, 12 Oct 2026)" item 1 and "## ECK-GP13B" (the sliced query list). Intake gate (06:47 UTC, pasted):
`eckert-1864: partial (line 3) -- edition/page or full-text-search citation found within 6 lines`, exit 0. Re-run `fortmonroe/eck_s65g_gb.py`
exactly as ECK-GP13B records (keyed, `country=US`, >= 2 s) for the control E531, E590, E591, E592 and the looser E589 (`Monohansett Monroe`);
5 queries; control first -- if the control is not a hit, no target query counts. Add rows to a dated "## ECK-GP13C" section in ECK-GP13B's table
format; change no row record, AUDIT or N-class (a hit that would change one is written as a one-line next step for a verifier). Update Remaining
gaps / Escalation, `tools/gaps_check.py eckert-1864`. Report what was found and where it was not found; do not classify novelty.

### THUR-57 (Opus, cap 1.5, box 35 min): thurloe-printed, code 57 and run 8 against the italics of Bijdragen X p.293
NOTES.md "## THUR-GB" and "## Remaining gaps (THUR-GB, 12 Oct 2026)" item "Code 57 ... run 8 pos 19". Intake gate (06:47 UTC, pasted):
`thurloe-printed: partial (line 2) -- edition/page or full-text-search citation found within 6 lines`, exit 0. Units: (1) fetch the one page of
the Delpher PDF THUR-GB identified (MMKB07:000756001, pdf page 305 = p.293; if it is already on disk from THUR-GB, use it), cut strip crops
with `tools/iiif_lines.py --image <page file> --out <dir>` (paste the command), ~0.3; (2) one look at the strips that carry the print's text for
run 1 ("factien"), the postscript and run 8 pos 19 ("uijtterste"): does the 1856 print italicise (= mark as deciphered) those words, and what
letters does it give where our p.72 key reads 57 = u and 58 at run 8 pos 19, ~0.5; (3) only if the print's reading is unambiguous at a cell:
grade the alignment per rule 4 (C from the printed decipherment), and edit the key only if the same printed gloss supports the value in two
places (then rule 7: the folder's p.160/p.340 decode script with --check); otherwise record as a lead (I). Update Remaining gaps / Escalation,
`tools/gaps_check.py thurloe-printed`. Report what was found and where it was not found; do not classify novelty.

### PISA-244 (Opus, cap 3.5, box 70 min): fr16045-pisany-rome-1585, the 26 f.244r T45/T47/T57 tokens
NOTES.md "## PISA-T475" and its Remaining gaps line "f.244r T45/T47/T57 (26 tokens) never compared and not located". Intake gate (06:47 UTC,
pasted): `fr16045-pisany-rome-1585: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0. Disk only.
Units (per-unit rate ~1.0 per vision call; 2 calls + reconciliation = 3 units): (1) locate the 26 tokens by eye on the committed f.244r strip
crops (images/f244r_L0*_s1/s2.jpg; pisa_t475/locate.py's montage is the aid, its predicted x is off by a sign or more on most), writing
pisa_244/locate.tsv (line, pos, x-centre, how located) -- at most one vision call over the strips in two halves (L01-L05, L06-L09), ~1.0;
tokens you cannot place with confidence are listed "not located", not guessed; (2) PREREG-PISA-244.md pushed (own commit, checked on
origin/main) BEFORE any reader call: the UNA-PISA instrument unchanged (sheet, 5 known-answer tiles, prompt, parser, settle rule), gate GK 5/5;
(3) one blind Opus reader call on tiles cut at those centres (x +/- 60 px of the strip, as PISA-T475), reply verbatim committed, a
pisa_244/pisa_244.py score [--check] (copy the pisa_t475 scorer's shape, or better, add a `--folio` option to it) -> pisa_244/result.tsv;
(4) SETTLED relabels are candidates only: re-score under the UNA2 gates only if the cap allows a further unit, otherwise name it as the next
step. key86.tsv and grades unchanged unless a pre-registered gate PASSes. Update Remaining gaps / Escalation, `tools/gaps_check.py
fr16045-pisany-rome-1585`. Report what was found and where it was not found; do not classify novelty.

### GUALT-HMC (Opus, cap 1.5, box 40 min): bl-gualterio-1700, pair the two HMC vol. VI printed keys
NOTES.md "## Next step (D2-GUALT, 8 Oct 2026)" item (1) and the vol. VI printed-keys line (l.252); `hmc_stuart_vi_ciphers_ocr_2026-10-08.txt`
on disk. Intake gate (06:47 UTC, pasted): `bl-gualterio-1700: open (line 1) -- edition/page or full-text-search citation found within 6 lines`,
exit 0. Units: (1) locate the vol. VI introduction leaves that print "the cipher used with Cardinal Gualterio" (cant-name nomenclator + "Key to
the figure cipher used with the above cipher") and "the cipher used with the King of Sicily" in archive.org `calendarofstuart06grea`
(page numbers / leaf indices from the djvu text on disk first; IIIF or BookReader leaf images, <= 4 leaves), ~0.3; (2) strip crops with
`tools/iiif_lines.py --image <leaf file> --out <dir>` (paste the command) and one vision pass that checks the OCR's key rows against the image,
correcting digits and cant names, ~0.8; (3) write `keys/hmc6_gualterio.tsv` and `keys/hmc6_sicily.tsv` (code, meaning, kind = letter/name/
word, grade H for a value read clearly from the print, M if the image is doubtful, the leaf), with a short README line naming the source
(HMC Stuart Papers vol. VI, 1916, pages); no test against ciphertext (none on disk). Also add both keys to KEY-OFFICES.tsv / KEY-DESIGN.tsv
via `tools/key_design.py` if its --help shows an add path for a printed key. Update Remaining gaps / Escalation, `tools/gaps_check.py
bl-gualterio-1700` (open targets: only if the folder already carries those sections; otherwise a dated section with a one-line next step).
Report what was found and where it was not found; do not classify novelty.

## Wave 2 (07:1x UTC 12 Oct)
Wave 1 results (get_session): ECK-GP13C 0.80 F (googleapis 503 on the control x3); THUR-57 2.38 D- (run 1 code 57 vs print n logged as a rule 4
conflict, run 8 favours 53, p.294 postscript printed undeciphered); PISA-244 5.18 D- (24/26 located, 22 relabel candidates); GUALT-HMC 3.54 D-
(keys/hmc6_gualterio.tsv, keys/hmc6_sicily.tsv). Every Opus job ran 1.5-2.4x its cap: wave 2 caps below are sized from those rates. Gallica 403
(07:12 UTC); googleapis flapping -- no googleapis-only job this wave.

### PISA-RS244 (Opus, cap 2.5, box 45 min): fr16045-pisany-rome-1585, re-score the 22 f.244r relabel candidates
NOTES.md "## PISA-244" (its result table and next step). Intake gate as PISA-244 (exit 0). Disk and CPU only, no vision call unless a gate needs
one tile re-look (then at most one call). Units: (1) PREREG-PISA-RS244.md pushed in its own commit (checked on origin/main) BEFORE scoring: the
UNA2-PISA / PISA-T32 / UNA3-PISA gates unchanged (re-score above both p99s, controls 5/5, the class-alignment check vs the old label, the random
same-size subset null), one gate per label group (T45->T19, T47->T27, T57->T32, T57->T35; T57->T42 single token reported, not committed);
(2) score each group with the existing scorer (pis1key / pisrs / una2 scripts -- read their headers; add an option rather than a private copy);
(3) commit only the groups that PASS (grades M -> C as the earlier commits did, readings regenerated, `--check` exit 0), log FAILs as FAILs.
Update Remaining gaps / Escalation, `tools/gaps_check.py fr16045-pisany-rome-1585`. A changed count goes to a verifier as a one-line next step
(no AUDIT edits). Report what was found and where it was not found; do not classify novelty.

### THUR-PS (Opus, cap 2.5, box 45 min): thurloe-printed, the Bijdragen X p.294 postscript ct file and decode
NOTES.md "## THUR-57" and Remaining gaps item "Bijdragen X p.294 postscript (29 numerals ...)". Intake gate (06:47 UTC): exit 0, as THUR-57.
Units: (1) two blind passes of the 29 numerals from the committed crop dutch1653/crops/bijX/bijX_p294_L01.jpg (re-cut tighter with
`tools/iiif_lines.py --image <file> --out <dir>` if needed, command pasted), reconcile -> ct_bijX294.tsv (3 units at ~0.5 with the Opus
floor); (2) add it to decode_dutch.py's inputs, decode with the p.72 key, grade per rule 4 (H for key values, M doubtful), `--check` exit 0;
(3) print check on the decoded phrase with `tools/print_check.py` or archive.org be-api full text (Japikse, Brieven van De Witt I notes;
later Bijdragen volumes; Birch I) -- IA <= 15 requests, >= 1.5 s, take/release lines; googleapis only if it answers (one try). Report the
decoded text and the search log; no novelty word. Update Remaining gaps / Escalation, `tools/gaps_check.py thurloe-printed`. Report what was
found and where it was not found; do not classify novelty.

## Wave 3 (07:4x UTC 12 Oct)
Wave 2 so far: THUR-PS 2.72 D- (postscript decoded H 28 M 1 under the p.72 key, print check IA 0 hits). PISA-RS244 still running. Gallica 403,
googleapis 503 (07:40 UTC).

### THUR-IA (Opus, cap 3, box 50 min): thurloe-printed, Birch I p.340 past run 15 and the vol 4/6 Bamfylde code 94 leaves
NOTES.md "## Remaining gaps (THUR-PS, 12 Oct 2026)" items "Birch p.340 vs Bijdragen X italics after run 15" and "Code 94 conflict". Intake gate
as THUR-57 (exit 0). IA images only ("IA" take/release, <= 15 requests, >= 1.5 s). Units at ~0.8 each (Opus rate from THUR-57/THUR-PS):
(1) Birch I p.340 (leaf n369): strip crops with `tools/iiif_lines.py --image <leaf> --out <dir>` (pasted), one look: cipher groups past run 15
and whether Birch gives an English of the p.294 postscript; transcribe any groups (two passes only if more than 10 numerals), decode with the
folder's p.340 script, `--check`, compare to the Bijdragen X italics; (2) the vol 4 and vol 6 Bamfylde glossed leaves the item names: one
leaf each, strip crops, read every 94 (and 25/51 if present) with its printed gloss; a value enters the key only with two printed glosses
(rule 4: a conflict with Tomokiyo's t is logged in HYPOTHESES.md with both witnesses, never settled by majority). Stop before a unit that would
cross 80% of the cap. Update Remaining gaps / Escalation, `tools/gaps_check.py thurloe-printed`. Report what was found and where it was not
found; do not classify novelty.

## Wave 4 (08:1x UTC 12 Oct)
Wave 2/3 results: PISA-RS244 4.88 D- (T45->T19 x10, T47->T27 x3, T57->T32 x5 PASS and committed, f.244r C 281 -> 295; T57->T35, T57->T42
FAIL); THUR-IA 3.95 D- (Birch I p.340 omits the Dutch closing and the postscript; vol 4 25 = e, 51 = i by printed gloss, logged). Gallica 403;
googleapis 200 at 08:08, 503 at 08:08:5x -- still flapping, no googleapis job.

### V-PISA244 (Opus, verifier, cap 3, box 60 min): fr16045-pisany-rome-1585, check of the PISA-RS244 relabels
You are a verifier, not PISA-244's or PISA-RS244's session or any solver on this folder. Pattern: `.claude/briefs/runs/2026-10-11-ytbiz-
default-0509-jobs.md` "### V-PISA3" and AUDIT.md "## AUDIT 5 (V-PISA3 ...)". Read NOTES.md "## PISA-244" and "## PISA-RS244", pisa_244/ and
the PISA-RS244 outputs. Check: (a) both PREREG commits (b708edca3, 1316666f4) precede their score commits on origin/main (git log); (b) re-run
the re-score and every `--check`, confirm the per-group gate numbers (control 5/5, both p99s, the class-alignment check, the subset null)
and that the two FAILed groups were not committed; (c) eye-check a sample of the 18 committed relabel tiles (at most one vision call, tiles on
disk) against the key86 cells they now carry; (d) recount the f.244r and item C/H/S/M counts from the committed reading/decode outputs and
propagate to status.json and depth fields (rule 4a; `python3 tools/depth_check.py` after), carrying any change into AUDIT.md and any
SECOND-OPINIONS-QUEUE.tsv row for this folder (rule 10). Write "## AUDIT 6 (V-PISA244, 12 Oct 2026)" in AUDIT.md; no class raised unless
the reading changed in substance (then say so and why). Update the Verdict line's cheapest next; gaps_check must pass. Do not decode new
material, do not touch other targets.
