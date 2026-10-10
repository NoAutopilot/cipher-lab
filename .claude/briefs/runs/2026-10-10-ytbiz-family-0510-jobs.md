# LANE FAMILY jobs (account 2, incarnation DEFAULT-account-2-20261010-0510, "FAMILY-A2o") -- 10 Oct 2026 05:2x UTC, lane orchestrator session_01TYpGVg4dqTawYWtDfvXvGq

Lane brief: .claude/briefs/lane-family.md (+ lane-common-blast.md). Cap 60, box 05:10-15:10 UTC 10 Oct (80% 13:10). Started from STATUS.md
"LANE FAMILY handoff (incarnation DEFAULT-account-2-20261010-0209)" next list and a fresh `next_steps.py --hot-only` read at 05:1x UTC.
Supply check at 05:1x UTC: the in-scope hot rows (hessen-daenemark, la-garde, pro3055-clinton, wallis, harley-287, ormond-arran, wvo-hessen,
heinsius-vanhaersolte, na-janssens, manteuffel census, hellen R1049, lodewijk 5810) were each re-read in their dated sections: done,
retired or person/physical-access gated. rah-salazar HTRC EF API probed once by the orchestrator at 05:14 UTC: still
PrimaryUnavailableException (no retry). Gate 0a: SESSION-SWEEP-account-2 stale-claimed since 5 Oct (prior incarnations proceeded; so do we).
Exclusions: eckert-* and Huntington ledgers (LANE LEDGER-10, account 1, live), Gallica fetches, Armstrong/Debosnys/Birago, any folder with a
ROOM claim < 6 h and no done.

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-09-ytbiz-family-1310-jobs.md` (read it in full), with these
substitutions: address every ROOM line "for LANE FAMILY-A2o (account 2)"; no external host this wave (both jobs are disk only). Halfway line:
one ROOM line at half the box or half the cap, whichever first (skip if done before). Account 2 is at seven_day `allowed_warning`: continue
(blast rules) and say so in the done line.

## Wave 1 (05:2x UTC 10 Oct)

### D1411-NBAR (Opus, cap 2.5, box 75 min, disk only): decode-1411-hhsta-vienna-1600, the noise-matched gloss bar
The folder Verdict's cheapest next and the 0209 handoff next item 1. Read ONLY NOTES "## D1411-POOL" (~lines 918-954), "## D1411-P6b" (the
pass-agreement figures), "## Remaining gaps" / "## Escalation", and `d1411pool/PREREG-D1411POOL.md` + `d1411pool/score_pool.py`.
Question: the de1600 coverage gate compared decoded independent numerals (which carry reader error and possible table error) against the
leaf's own clean gloss text (bar 0.6129). Build the bar a CORRECT table could reach on THIS transcription: encode `gaps150/gloss_text.txt`
(or the gloss file D1411-POOL used -- check the path in the code) through frozen T21r into numbers, inject number errors at the measured
reader-error rate(s) (take the rates from the folder's own pass-agreement figures; pre-register a low / central / high bracket that spans
them, SALV-DIAG lesson), decode back, and score de1600 coverage with `d1411v/rescore_v.score` unchanged, many seeds, at the pooled N=308.
PREREG-D1411NBAR.md, pushed in its own commit (check `git log origin/main -1 -- <PREREG>`) BEFORE any noisy-bar number is computed, must fix:
the error model (substitution only vs substitution+split/merge; which numbers errors go to), the rates, seeds, the bar statistic (e.g. the
5th percentile of noisy-gloss coverage at the central rate), and the decision rule against the already-known pooled T21r 0.513, shuffled p99
0.458 and shifted max 0.393. Because 0.513 is already known, ALSO pre-register a check that the noisy bar stays above the noisy-shuffle
level (apply the same error injection to an order-shuffled gloss encoding and to the 23 shifted rules) -- a bar that falls to the shuffle
level licenses nothing (rule 3: the control must be able to differ). Script `d1411nbar/nbar.py` with `--check`. Outcomes: PASS (T21r inside
the noisy bar's band and above noisy controls) means "the coverage gap is explained by reader error at the measured rate" -- report it, no S
grades written (a verifier decides; end with one line asking the lane for one); FAIL or non-test as found. No new reads, no image work, no
table change. NOTES "## D1411-NBAR", Remaining gaps / Escalation / Verdict updated, gaps_check.py. Report what was found and where it was not
found; do not classify novelty.

### SORT-A2o (Sonnet, cap 2.5, box 75 min, disk only): sorter inputs for two person-gated glyph questions; one ASKS row
Two folders' Verdicts wait on a person's sign sort and nobody has built the page: (1) jan-van-nassau-1572-75, `images/jvn_gly/` X1-X7 (the
glyph after 103 "vff", 140 vs 110, and a blind check of the two 104-glyph M tokens; NOTES "## JVN-GLY" and "## Remaining gaps" only);
(2) na-oldenbarnevelt-2442-1605, the L4/L7 masked crops made by OLD-O2 (NOTES "## 24. OLD-O2" and the 0209 handoff item 2: sign
disagreements there bound the longest S stretch). ASKS row 147 is a DIFFERENT, already-published Oldenbarnevelt sorter (blocks A/C2, f.54/f.56)
-- do not touch it; read it to match its build pattern (`ciphers/na-oldenbarnevelt-2442-1605/sorter/build.sh`, sorter/README.md).
Steps: check 1 of prior-work-step.md (grep ROOM/NOTES/ASKS for a sorter already built for either set; if one exists, stop that half). For
each set: cut sign tiles from the committed crops (reuse the folder's own tile cutter / the 147 build pattern; for jvn_gly the X crops are
glyph detail crops -- tile the individual signs in them), build with `tools/sign_sorter.py` in its DEFAULT blind mode (no values, no key,
no machine labels on the page; never `--show-values`), with a focus list of the disputed tiles, and run `tools/sorter_preflight.py` (and
`tools/cvd_check.py` if the preflight does not) until PASS. Commit a `build.sh` + inputs per set (`sorter/a2o/` in each folder) so the
account-3 orchestrator can publish; do NOT publish an artifact yourself. Register the families in `tools/data/sorter_families.tsv` only if
the tool requires it for a blind build. File ONE ASKS.md row (rebase first; next free number) naming both builds, the build commands, the
focus tiles first, minutes estimate, "backlog, never blocking", and that sign_sorter_apply.py is the follow-up; one ROOM `flag:` line for the
account-3 orchestrator naming the row. Update each folder's Remaining gaps blocker to "waiting-on ASKS <n>" and its Escalation image-check
line; gaps_check.py on both. Report what was built and the preflight output; no reading, no decode.

## Wave 1 results (05:3x UTC)
D1411-NBAR (2.67 by get_session): NON-TEST at the central error rate 0.123 (noisy-bar p05 0.4935 vs noisy-shuffle p99 0.4968); the decision
turns on the reconciled error rate, which needs a person-settled sample (ASKS 120). p.7 is not opened. SORT-A2o (1.77): two blind sorter builds,
preflight PASS, ASKS 161, flagged for the account-3 orchestrator.

## Wave 2 (05:4x UTC 10 Oct)

### OBRED-0259 (Sonnet, cap 2, box 75 min, NA <= 95 requests): oldenbarnevelt-brederode-1605, inv. 6016 orders 1-259 sheet screen
The folder Verdict's cheapest next. Read ONLY NOTES "## OBRED-6016", "## Remaining gaps", "## Escalation" and the TX-KEYS lines it cites.
Same method as OBRED-6016 exactly: one METS request, then IIIF `/full/400,/0/default.jpg` for every third scan 1, 4, ..., 259 (87 requests,
>= 2.0 s apart, descriptive UA, NA take/release ROOM lines), contact sheets of ten seeded with the same two disk controls (CTRL-CIPHER inv. 2016
scan 31, CTRL-PLAIN inv. 6016 order 261); a sheet whose controls are not both called right is a non-test and is re-sheeted. Your own eye, no
subagent. Re-look at 1200 px (at most 6 requests) only where a sheet shows a numeral run, table or interlinear gloss. Output
`images/6016_screen_0001_0259.tsv`, commit any 1200 px looks. Then, disk only and from the folder's own dated sections (no new step), fill the
five Escalation rungs marked "not assessed" ([x]/[ ]/[n/a] with the section that settles each; leave [ ] with a named next step where nothing
does), refresh Remaining gaps / Verdict, gaps_check.py. NOTES "## OBRED-0259". Report what was found and where it was not found (limits as
OBRED-6016 states them); do not classify novelty.

## Wave 2 result (05:5x UTC)
OBRED-0259 (1.29): 87 scans, controls 9/9; **scan 187 (inv. 6016, archive pencil "143") = a Dutch letter signed "P. Brederode", dated 17 Oct
1604, the no. 92 sign-off formula, with a postscript of about 80 numeral groups** (images/na_101_02_6016_p0187_1200.jpg, _numerals_zoom.jpg).
Orchestrator's own look at the zoom (not a transcription, M): values 97, 108, 110, 217, 289, 337, 409, 420, 433, 440 appear in both the
187 block and no. 92's printed groups -- a possible shared code, unmeasured.

## Wave 3 (06:1x UTC 10 Oct)

### OBRED-187 (Opus worker, Sonnet subagents, cap 5, box 90 min, NA <= 8 requests, huygens <= 10): oldenbarnevelt-brederode-1605, the scan-187 postscript
Read ONLY NOTES "## OBRED-0259", the folder head (what is established about no. 92), ciphertext.txt, and "## Remaining gaps"/"## Escalation".
1. Prior work first (prior-work-step.md; paste output): is the 17 Oct 1604 Brederode letter printed? Veenendaal deel II (GS 108) and deel I/III
   via the Huygens retroboeken full-text search (`retroboeken/oldenbarnevelt`, terms "17 october 1604", "Brederode", "Stettin", and the clear
   phrase you read); the editor's preface says no. 92 is the only cipher piece in deel II, so record whether the 1604 letter is printed and if
   its postscript is omitted, marked or deciphered. Also grep the folder and DECODE notes for "1604". A printed decipherment = stop after step 3
   and say so (N0 material, key source).
2. Fetch scans 186, 187, 188 at native size from service.archief.nl IIIF (METS base as OBRED-0259; NA take/release; 3-6 requests). 186/188:
   does the letter or the code continue? Commit what is cited (JPEG, folder under 30 MB).
3. Read the clear letter of 187 (date, place -- "Stettin"?, addressee, content in two lines) by eye at native size, grade M.
4. Crop the numeral block (paste `tools/iiif_lines.py --image <187 native> --out images/p187_lines ...`), two blind Sonnet passes on line crops only
   (not told no. 92 or any value), one reconciliation unit by you on the crops -> `ciphertext_187.tsv` (line, pos, group, grade H-read/M), the
   clear insertion ("oock bestaen dat dits"?) kept as text.
5. PREREG-OBRED187.md pushed in its own commit BEFORE computing it: the overlap statistic between the set of 187 values and no. 92's printed
   values (ciphertext.txt groups only), against a control that can differ: values drawn from a model of the same range and size (e.g. uniform
   over 1..max of the two, and a resample matched to 187's own value histogram shape), 10,000 draws, p-value; plus the same statistic against
   1-2 unrelated three-digit code texts of the period on disk (e.g. a DECODE 1600s key's code range or another folder's code numbers) as a
   negative. Report numbers; a shared-code claim is only "consistent with" at M, never a reading. Run `tools/key_design.py` on the pooled values
   if its help shows a fit; no decode, no key.
6. NOTES "## OBRED-187", Remaining gaps / Escalation / Verdict, gaps_check.py. If the overlap clears its control, end with one line asking the
   lane for a design_prior / pooled-attack step (do not start it). Report what was found and where it was not found; do not classify novelty.

## Wave 3 result (06:2x UTC)
OBRED-187 (4.40): 187 = P. Brederode, Stettin, 17 Oct 1604, to the griffier of the States General (M); not printed in Veenendaal II (no.89 -> no.90);
postscript 59 groups, two blind passes 59/59 (ciphertext_187.tsv, 49 H-read, 10 M); PREREG 774b4ccb1: S = 26 shared values with no. 92 vs uniform
mean 7.42 / band-matched 8.72 (p = 0.0001 both), negatives p95 8 and 6 -> clears: consistent with one code list (M), not a reading.

## Wave 4 (06:5x UTC 10 Oct)

### OBRED-S1 (Sonnet, cap 3, box 100 min, NA <= 180 requests): inv. 6016 orders 1-259, every unlooked scan
Read ONLY NOTES "## OBRED-0259", "## OBRED-187" and the gaps. Same sheet method as OBRED-0259 (METS 1 request; IIIF `/full/400,/0/default.jpg`,
>= 2.0 s apart, NA take/release), now for the 173 scans of 1-259 not yet looked at (all orders not in images/6016_screen_0001_0259.tsv and not
186-188), 186-188 excluded. Controls on every sheet: CTRL-CIPHER (inv. 2016 scan 31), CTRL-PLAIN (order 261) AND a third, CTRL-PS = a 400 px
reduction of scan 187 itself (made locally from images/na_101_02_6016_p0187_native.jpg, no request) -- the Dutch three-digit postscript is the
shape to catch; a sheet where any control is miscalled is re-sheeted. 1200 px re-looks only where a numeral run, table or gloss shows (<= 8).
Output `images/6016_screen_s1.tsv`; for each hit: docket/date/sender by eye (M) and the 1200 px image committed. No transcription. NOTES
"## OBRED-S1", gaps updated, gaps_check. Report counts and every hit; where it was not found.

### OBRED-DP (Opus, cap 3, box 75 min, disk + huygens <= 15 requests): pooled structure of no. 92 + the 187 postscript, and a print check
Read ONLY NOTES head (no. 92 established facts), "## OBRED-187", ciphertext.txt, ciphertext_187.tsv, obred187/. No decode claims, no key.
1. Print check for a period decipherment (huygens take/release): Resolutiën der Staten-Generaal (Huygens retroboeken, the volume for 1604-1605)
   for Brederode's letters of Oct 1604 and Feb 1605 and any "cijfer"/"ontcijferd"/"dechiffr" near them; one positive control query that must hit
   (e.g. a known Brederode mission entry). Record route, queries, hits.
2. `python3 tools/design_prior.py` on the pooled tokens (paste command + top lines) and on each text alone.
3. Structure, script `obred187/structure.py` with `--check`: no. 92's code tokens as runs in clear-text context (run length, preceding/following
   clear words); 187's runs; shared bigrams/trigrams of code values across the two texts vs a shuffled-order control (order-dependent statistic,
   so the control can differ -- rule 3); value range per run length (single codes for names vs runs that may spell words/syllables); whether
   any no. 92 run's context makes a crib (a run standing where a name or number is grammatically required). Write the hypotheses about the
   design (nomenclator with name codes + a syllable/letter table?) as a ranked list with the test each needs and its matched control.
4. NOTES "## OBRED-DP", gaps updated, gaps_check. Name the next attack step and its cost; do not start it. Report what was found and where it
   was not found; do not classify novelty.

## Wave 4 results (07:0x UTC)
OBRED-S1 (1.97): inv. 6016 orders 1-259, 170 unlooked scans at 400 px, controls 51/51: no further numeral block; 111 = Brederode, Hanau 22 Sept
1603 (plain). OBRED-DP (2.52): Resolutien S.G. XIII: 39 Brederode hits (control passes), no cipher/decipherment note; design_prior excludes
letter-for-letter and pure code (multi-sign nearest); PREREG ae9dd4a8d: G2 PASS -- all 33 no. 92 values >= 600 stand alone (name band ~588-751,
p = 0.0001); G1 FAIL -- one shared ordered pair (529 433), p = 0.092; lower table 30-507 (146 tokens, 113 distinct) spells words; crib test
unfalsifiable at N = 180 -> the gap is too-short; next = more text in this code.

## Wave 5 (07:3x UTC 10 Oct)

### OBRED-S2 (Sonnet, cap 3, box 100 min, NA <= 190 requests): inv. 6016 orders 351-624, every unlooked scan
As OBRED-S1 exactly (three controls per sheet incl. CTRL-PS from scan 187; 400 px, >= 2.0 s; NA take/release; <= 8 re-looks at 1200 px), for the
182 scans of 351-624 not in images/6016_screen.tsv. Output `images/6016_screen_s2.tsv`; every hit with docket/date/sender (M) and its 1200 px
image committed. Read ONLY NOTES "## OBRED-6016", "## OBRED-S1" and the gaps. NOTES "## OBRED-S2", gaps updated, gaps_check. Then (same NA take,
<= 12 more requests): for each of inv. 6017-6024 ("Liassen Agent Brederode", 1.01.02, 1614-1637) and the 1605 Swiss-mission dossier (find its
invnr in the 1.01.02 EAD on disk or one catalogue request), record digitised y/n, METS id and scan count from the item page's embedded
drupal-settings-json (CLAUDE.md host table) -- a table `nl_brederode_lias.tsv`, no image fetches. Report counts and every hit.
