# LANE-NEAR7 wave 1 (4 Oct 2026, written 12:2x UTC by LANE-NEAR7, account 2 / ytbiz, session_011jxC5ygqRnFKn5qTCJAPNz)

Common rules: the "Common to every job below" section of `.claude/briefs/runs/2026-10-04-ytbiz-near4-wave1.md`, with
"LANE-NEAR4" read as "LANE-NEAR7" everywhere (claims, done line addressed "for LANE-NEAR7 (account 2)").
Intake gates (pasted by LANE-NEAR7, 12:1x UTC, both rc=0):
`fr16104-vivonne-spain-1572: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`
`hellen-frederick-1752: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`

Lane goal (orchestrator's brief): move one Vivonne piece from D1 to D2 (rule 4a). Audits so far read N3 / D1 because transcription noise
(err_2reader 0.15-0.30, label splits) leaves no clause above the authentication distance (about 42 letters, AUDIT 2 4a). **The depth
verdict is not yours**: a fresh account-3 audit sets it. You produce a cleaner transcription, a re-decode under label rules you
pre-registered before re-decoding, and an honest list of the longest repair-free stretches (letters, liberties counted as AUDIT 2 counts
them). Never write D2, "deciphered" or any rule-10 word.

## Shared by both Vivonne jobs (N7-VIV53L, N7-VIV54L) -- same folder, same time
- Read NOTES.md sections N5-VIVK, N5-VIV54, N6-VIV53, N6-VIV53B, AUDIT.md AUDIT 1 and AUDIT 2 (4a and Next steps), tx/SIGNS.md, TRANSCRIPTION.md,
  and `python3 tools/lookalike_pass.py --help` (subcommands confusion, packet, reconcile, audit, audit-score).
- Isolation: files named `*<NN>L*` / `tx/lookalike<NN>/`; never edit what regenerates reading_piece53/54/63.tsv (`--check` on all three must still
  pass at your push); your re-decode writes `reading_piece<NN>_L.tsv` via a new `tx/viv<NN>L_decode.py --check`. Do not touch key.tsv or any ink 63
  file (VIV63-A1 is auditing ink 63 now). NOTES section appended at the end after `git pull --rebase` immediately before the edit.
- Step 1, PREREG-N7VIV<NN>L.md pushed BEFORE any re-read or re-decode, naming: (i) the label rules -- at least the ': :' pair read as ONE sign
  (state which key cell), the a/u, 4/+/p, z/3, S/d pairs settled only by the lookalike 2-of-3 rule, nothing settled by "what decodes better";
  (ii) the D2-candidate statistic: the longest stretches of decoded text needing no letter repair, with word division and every other liberty
  listed per stretch exactly as AUDIT 2 4a lists them (the auditor re-counts; you list); (iii) an error measure: `lookalike_pass.py audit` on
  agreed signs with plants (--plant 0.05) and audit-score, so a true-error estimate sits beside the 2-of-3 residual (the residual is agreement,
  not accuracy); (iv) the b2 gate + 200-wrong-key specificity re-run on the re-decode exactly as PREREG-N6VIV53B, rule unchanged.
- Units (state in NOTES before the first subagent call): confusion + packet are scripts; ONE Sonnet re-read call per page's flagged tiles
  (crops only, never a full page: TRANSCRIPTION.md / Usage 6), ONE audit re-read call for the whole piece, ONE reconciliation step by you, priced at
  ~USD 1.2 per call. Stop before a unit that would cross 80% of cap or box.
- If the ': :' pair or a label rule needs a key-cell decision you cannot settle from tx/SIGNS.md and the key image, it stays M and goes in your
  section as a key question; never pick the reading that decodes better.
- print_check on any new repair-free stretch >= 20 letters (phrases_<NN>L.txt). Report what was found and where it was not found; do not
  classify novelty. Done line: err_2reader before/after, 2-of-3 residual, planted-audit error estimate, H/M/U before/after, b2 and specificity
  numbers beside their controls, the three longest repair-free stretches (letters + liberties). If b2+specificity pass: "piece <NN> ready for
  audit (depth re-check)".

## N7-VIV53L -- ink 53 (fr.16104 ff.170r-171v, to Anjou, 5 Sept 1572): look-alike pass + pre-registered re-decode (Opus; cap USD 7; box 110 min)
Four cipher pages (170r, 170v, 171r, 171v): 4 tile re-read calls + 1 audit call + reconciliation = 6 units ~USD 7. Inputs: tx/f170r..f171v
_passA/_passB(_c)/_rec.tsv, images/p53 crops (regenerate from the manifest's commands if absent). Also re-check the f.170r-171r gloss rows only
if a label rule changes a glossed position (the registered gloss gate result 0.577 stands and is not re-run as a gate).

## N7-VIV54L -- ink 54 (fr.16104 f.173r-v, to the King, 7 Sept 1572): the same, two pages (Opus; cap USD 4.5; box 80 min)
Two cipher pages: 2 tile re-read calls + 1 audit call + reconciliation = 4 units ~USD 4.5. The a/u "qae" confusion (AUDIT 1) is the named target.
If b2 was never run on ink 54 (N5-VIV54 used the gloss gate), run it now under the same PREREG with its two positive controls, as N6-VIV53B did.

## N7-HELDK -- hellen-frederick-1752: R4386 (f.75) and R4388 (f.79) full-size dockets/band heads for the 1763 letters (Opus; cap USD 3; box 45 min)
NOTES N6-HEL81 and its Remaining gaps. One DECODE login (`NODE_PATH=$(npm root -g) node tools/decode_browser_login.js`, try `--guess-fullsize`),
both records' pages to scratch only (never committed), read docket, header, holder, code range and whether cells carry meanings. If either is a
filled 1763 Hellen table that fits R1045-R1048/R1060/R1061 (code range, French, a holder or date), name it and price the transcription + --key
test as the next step; do not transcribe in this job. Output `key_search/R4386-R4388.tsv` (same columns as R4381-R4408.tsv), NOTES "N7-HELDK",
gaps refresh + gaps_check OK. The codes 1-800 gap is NOT this job (R4370/R4372 retired under rule 3; its named next step is the Fagel 5177
phrase corpus). Report what was found and where it was not found. Scrub the account name from anything saved.

## Wave 2 (added 12:3x UTC by LANE-NEAR7; VIV63-A1 done 12:22, AUDIT 3 written; N7-HELDK done 12:24)

### N7-VIV63G -- ink 63: f.194r lines 5-10 + the key-questions context table (Opus; cap USD 5; box 75 min)
Units: f.194r L5-10 re-cut deskewed (`--centres`/deskew, check the overlay BEFORE any pass: N6-VIV63C lesson), 2 blind passes + 1 reconciliation
(~1.5); then NOTES' named step "ink 63 key questions": a code-context table of y, single o, c, V, e, 2, r against ink 40's decipherment alignment
(tx/key_support.py) and the ink 63 reads -- proposals only, key.tsv untouched (a key change is a separate graded step), ~3. Coordinate with
N7-VIV53L/N7-VIV54L (same folder): pull --rebase before shared edits. reading_piece63.tsv regenerated with `--check` to include L5-10. AUDIT 3
was written before this change: add a dated "Revision after AUDIT 3 (N7-VIV63G)" note under AUDIT 3 stating exactly what changed (lines, token
counts, H/M/U) without altering the class or depth, and carry it into the SO-VIV63 row of SECOND-OPINIONS-QUEUE.tsv (rule 10 propagation).
b2 + specificity re-run on the whole piece under PREREG-N6VIV63B's rule (addendum PREREG-N7VIV63G.md first). Also fix the stale "ink 53 audit 1
not-attempted" line in the last Remaining gaps (VIV53-A1 done 11:21). Report what was found and where it was not found.

### N7-HELBC -- hellen-frederick-1752: pre-registered blank-cell test of R4388 on the 1763 letters (Opus; cap USD 4; box 60 min)
NOTES N7-HELDK named it: R4388 (f.79, codes 2001-3900, names c.1762-63) fits 26-35% of 1763 tokens but 11/28 sampled tokens land on blank cells
(base ~32%; the true-key precedent R4369/R1953 ~3%). One DECODE login (images to scratch only, never committed; scrub the account name).
PREREG-N7HELBC (in NOTES or key_search/) pushed before counting: which cells are read (only the cells the ~180 distinct 1763 codes need, one
blind pass + a second blind pass on the same cells), the statistic (share of the 1763 tokens in R4388's range landing on blank cells, plus, if
cells carry meanings, the LR100 uni/bi test as READ2-HEL2), the null (blank share at random code positions in the same range; and the R4369/R1953
precedent as positive control subsampled to the same N), the pass rule. Verdict: candidate for a full transcription (~$12) or retired. Do not
transcribe the whole table. gaps refresh + gaps_check OK; NEAR row Evidence/Last-touched + near_check.

## Wave 3 (added 12:5x UTC by LANE-NEAR7)

### N7-LKTOOL -- tools/lookalike_pass.py: the per-tile window re-read as a shared subcommand (Opus; cap USD 4; box 60 min; no network)
Lesson (N7-VIV53L, N7-VIV54L, 4 Oct 2026): the tool's `packet` and `audit` prompts (id-only candidate sheet + whole line crops, passC sequence
shown) drew 7/7 Sonnet re-reads that echoed passC -- voided, about half of both jobs' spend. The working instrument was private
(ciphers/fr16104-vivonne-spain-1572/tx/viv53L_windows.py and viv54L_windows.py): per-tile windows cut at the estimated x on the stitched line, 6 per
montage, candidates in alphabetical order, the passC label hidden. Usage 8 / 8a: promote it into the shared tool as a `windows` subcommand
(options for the stitched-line x estimate and montage size; output the same <run>_tiles.tsv shape `reconcile` reads), with an offline test in
tools/tests/ (synthetic crops). Add to `packet`'s and `audit`'s --help and the prompt file a warning that the passC-visible prompt is echo-prone,
with an `--hide-passc` option if cheap. Leave the two private scripts in place (their output is cited) with a header line pointing at the tool,
as interlinear_align did. Update SYSTEM.md's row for the tool and TRANSCRIPTION.md's look-alike line in one sentence. Run tools/tests for the tool
+ system_map_check + file_shrink_guard. Do not re-run any Vivonne read. Report what changed.

## Wave 4 (added 13:2x UTC by LANE-NEAR7)

### N7-VIV54Q -- fr16104 ink 54 key question "to z" = qae (Opus; cap USD 2; box 40 min; disk + at most 2 Gallica/cryptiana requests)
NOTES gap line (N7-VIV54L): 13 occurrences of "to z" read "qae", no reader split, ink 40's alignment never gives u for z. Read Tomokiyo's key image
(henryiii_Vivonne1.png on disk, or sources/cryptiana) for the cells of u, q and any z-like homophone or "qu" sign; compare the ink 54 crops of the
13 occurrences at native resolution (crops only) against the key-image sign. Write the finding as a key question with evidence; key.tsv changes
only if the key image itself shows the cell (then grade H, regenerate reading_piece54_L with --check and say what moved). No other edits.

### N7-HEL86 -- hellen-frederick-1752: the same pre-registered blank-cell test on R4386 (Opus; cap USD 3.5; box 50 min)
NOTES N7-HELBC named it: R4386 (f.75, alphabetical one-part 1201-2200, names 1764+), 1201-2000 band, 63 codes / 121 1763 tokens; low prior. Copy
PREREG-N7HELBC's rule (statistic, null, control subsampled to N=121, pass rule) as PREREG-N7HEL86 before reading; one DECODE login, images to
scratch only, scrub the account name; 2 blind Sonnet passes over the target + null cells only + reconciliation. Verdict candidate/retired; gaps
refresh + gaps_check OK; NEAR row Evidence/Last-touched + near_check.

## Wave 5 (added 13:4x UTC by LANE-NEAR7)

### N7-VIV54R -- ink 54: the col-u row-3 sign as its own label, relabel from native crops, re-decode (Opus; cap USD 2.5; box 45 min; disk only)
N7-VIV54Q (NOTES, tx/viv54Q/to_sign_evidence.jpg): the sign after "to" (13 in ink 54, read z/R/x by the passes) is Tomokiyo's column-u row-3
Sigma/I-shaped entry, which key_tomokiyo/key.tsv omits. Push PREREG-N7VIV54R.md BEFORE any relabel: the new label name, the key cell it takes
(column u row 3 as read from henryiii_Vivonne1.png -- H only if the image shows it plainly, else M), the shape criterion that decides each
position (judged from native crops against the key-image sign and the ordinary z on the same line, decoded text never shown), and that every
position in ink 54 is judged, not only those after "to". Then relabel, add the cell to key.tsv only under that grade (note it for inks 53/63,
which you do not relabel), regenerate reading_piece54_L via viv54L_decode.py --check, re-run b2 + specificity under PREREG-N6VIV53B's rule, and
re-list the three longest repair-free stretches with liberties counted. All other decodes' --check must still pass. NOTES "N7-VIV54R", gaps refresh.
