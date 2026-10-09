# MQS-SHEETS: key and reading sheets, the colour check, and capitals for confirmed values (jobs A1 and A2 of LANE MQS)

Written 9 Oct 2026 (clock read 00:58 UTC) by the account-3 orchestrator's reconciling session, for workers on
**account 4**; revised 9 Oct 2026 (clock read 01:26 UTC) by the check-and-fix pass. Lane brief:
`.claude/briefs/runs/2026-10-09-acct3-mqs-lane.md`. Background and every number cited:
`research/MARY-STUART-TALK-2026-10-09.md` (sections c and f) and matrix rows M09, M10, M25, M30, M31, M47 of
`research/MARY-STUART-TALK-2026-10-09.tsv`.

**Two sessions, one brief.** The tools and the renders are split so the 80% line cannot cut the renders the owner
wants most:
- **A1, MQS-SHEETS** (units 1-5 below): Sonnet (`claude-sonnet-5`), **cap USD 7, box 120 min**. Builds and tests the tools.
- **A2, MQS-SHEETS-R** (units 6-7 below): Sonnet, **cap USD 6, box 110 min**. Starts only after A1's ROOM done line;
  renders the samples, checks every tile, writes `outreach/sheets/README.md`.
A worker does only its own job's units. A2 reads A1's done line and its PREREG before starting.

- **Goal:** the owner's item 3. Sheets in the format Tomokiyo and Lasry publish (key table; interlinear reading),
  rendered from a target folder's own graded data, so a recipient can check a reading against the manuscript from
  their own desk; sample sheets for Tomokiyo's targets and one Huntington telegram in `outreach/sheets/`.
  Layout after Lasry, Biermann and Tomokiyo 2023, Figs 5-14 and B24 (pp.112-127, 200), **described, never copied**:
  the paper is CC BY-NC-ND. Glyphs are always cut from the manuscript images on disk, never from anyone's drawn table.
- **Blind-first (TRANSCRIPTION.md; lane brief "What this lane does not do").** Every Birago 1572 family sheet (key,
  no.87, any other Birago reading) is **held**: the owner still has open blind sorts in that key family (ASKS.md row 118,
  and the two unnumbered Birago sorter rows of 2 Oct (f.168 / no.85, artifact QzrYKY...) and 3 Oct (f.117r, artifact
  HY4WNL...)). Seeing which glyph is which letter would make those sorts value-informed, and that cannot be undone. A2
  renders Birago sheets into its **scratchpad only** (they are the only per-sign box test of the tool), never into
  `outreach/sheets/` and never into the repository, and lists them in the README as held with the command that
  regenerates them.

## What exists (checked 9 Oct; build on it, do not rebuild)

- `tools/glyph_atlas.py atlas --from-truth TOKENS.tsv --per N --spread --grades CHS [--exclude-leaf PAGE]` (TX-SHEET,
  4 Oct 2026; the glyph_atlas shelf row is `proven`) already picks per-code exemplar tiles from graded, securely read
  boxes: the medoid, then farthest-point spread, after trimming the farthest share (`pick_spread`, `cmd_atlas_truth`).
  **The key sheet's exemplar row imports these** (`--variants` maps onto `--per`); do not re-implement median-exemplar
  picking.
- `tools/glyph_atlas.py classify` is the shared shape-similarity kNN with a measured accuracy (TX-ATLAS-B72, 3 Oct 2026:
  0.754 on 309 known tiles of the Birago 1572 family atlas).
- `ciphers/moray-wood-1568/no804/refsheet/build_refsheet.py` (RUN1-MOR, 4 Oct 2026): one row per class in key.tsv order,
  and a panel that puts each M/I-graded token beside its three nearest S-graded exemplars (binarised 32x32 masks, Dice
  overlap, best of +-2 px shifts); RUN3-MOR's eye check (11 of 102 boxes unusable, 10.8%) and RUN4-MOR's fix (0 of the
  11), leave-one-out top-1 0.513 vs label-shuffle p99 0.128. Aymeloglu labelled the Moray glyphs (cited only, no code
  copied).
- Other target-local sheet cutters, each read before you write: `ciphers/fr3151-seure-1558/known_keys/tournon/build_sheet.py`
  (R12A-SEUT, 6 Oct: an image-exemplar reference sheet from the leaf's own line crops, the same job as `key` here);
  `ciphers/nevers-birago-fr3251-1572/atlas/exemplar_sheets.py` (TX-ATLAS-B72: cluster exemplar sheets for one model read
  per sheet); `ciphers/nevers-birago-fr3251-1572/harvest/cut_sign_sheet.py` (HARVEST-D2) and `ciphers/fr2980-gramont/legend.py`
  (value-blind sign sheets cut from **published drawn tables** for transcription passes). The last two do a different
  job (blind reference sheets from a printed table, which this tool must never cut from) and are not superseded.
- Nothing in `tools/` renders a key or reading sheet from a folder's graded data; there is no colour check.

## Promote or build (decided)

- **Promote** RUN1-MOR's M/I-beside-S panel into `decipher_sheet.py key --mi-panel`. Its similarity: use
  `glyph_atlas classify`'s features if they work on the Moray crops; otherwise keep Dice and say why in the docstring
  (RUN4-MOR's leave-one-out 0.513 vs label-shuffle p99 0.128 is the evidence Dice carries). Never ship two rival
  shape metrics without that sentence.
- **Build** `tools/decipher_sheet.py` (key and reading modes) on `decode_key.py`'s loaders and `glyph_atlas.py`'s
  exemplar picker, and `tools/cvd_check.py`. **Extend** `tools/decode_key.py` with `--style case`.
- **Not in this job:** the `register` page (a later PILE-REGISTER job built on `tools/holder_export.py`'s rows). **Do
  not edit `tools/holder_export.py`** (the HOLDER-EXPORT fix worker claimed it at 00:40 UTC 9 Oct); import its functions
  read-only if you need its md-blocks loader for Eckert.

## Files

A1: `tools/cvd_check.py` (added), `tools/decipher_sheet.py` (added), `tools/decode_key.py` (a `render_case` function,
the `'case'` entry in `STYLES` and the `--style` choices only), `tools/tests/test_cvd_check.py`,
`tools/tests/test_decipher_sheet.py`, `tools/tests/test_decode_key_case.py`, `tools/tests/PREREG-MQS-SHEETS.md`, one header
line each in `ciphers/moray-wood-1568/no804/refsheet/build_refsheet.py` ("promoted to") and
`ciphers/fr3151-seure-1558/known_keys/tournon/build_sheet.py` ("superseded by tools/decipher_sheet.py key; kept because
its outputs are cited", only if `key` reproduces its layout from that folder's data; otherwise say why not in your
report), rows in `tools/data/tool_shelf.tsv` and `SYSTEM.md`.
A2: `outreach/sheets/` (README.md and the non-Birago sample sheets), the evidence cells of A1's tool_shelf rows,
`tools/tests/PREREG-MQS-SHEETS.md` (an appended K3 results block only).
Sheets are written to `outreach/sheets/` only: the Gramont and Eckert folders already hold 28 and 27 MB of images, near
CLAUDE.md's 30 MB-per-folder image line, and a sheet embeds its tiles.

## Units (Usage 6: stop before a unit that would cross 80% of cap or box)

Minutes are planning estimates, about 80% of the box split by each unit's dollar share. The nearest measured rows are the
five TOOLS-TOMO single-option Opus jobs of 8 Oct 2026: 11-18 min and USD 3.75-5.11 each (LEDGER.md lines 3548-3552;
ROOM.md 22:44-23:04 UTC). A Sonnet render-and-look unit is slower per dollar, so the box, not the cap, is the figure to
watch in A2.

| Job | # | Unit | USD | Min |
|---|---|---|---|---|
| A1 | 1 | `tools/cvd_check.py` + test | 0.6 | 10 |
| A1 | 2 | `decode_key.py --style case` + test; push units 1-2 and post the ROOM line below | 0.6 | 10 |
| A1 | 3 | `tools/decipher_sheet.py key` and `reading` + tests (glyph_atlas picker imported; M/I panel promoted) | 2.8 | 40 |
| A1 | 4 | PREREG, then regression tests R-K1, R-K2 and the map test KM | 1.1 | 25 |
| A1 | 5 | Header lines, registration | 0.5 | 10 |
| | | A1 total 5.6 of cap 7; 95 of box 120 | | |
| A2 | 6 | Seven renders, each one render + programmatic K3 + one tile-grid eye check (at most 60 tiles, 1 vision call, about 0.3) + a fix if needed, about 0.6 and 11 min each: five public first, then the two held | 4.2 | 77 |
| A2 | 7 | README, K3 block in the PREREG, shelf evidence | 0.4 | 8 |
| | | A2 total 4.6 of cap 6; 85 of box 110 | | |

**A1: units 1-2 first, pushed within about 30 minutes**, then one ROOM line:
`python3 tools/room.py "MQS-SHEETS worker (account 4)" "step 1 pushed: tools/cvd_check.py and decode_key.py --style case (<commit>) -- for LANE MQS (account 4)"`.
Jobs MQS-SORTER and MQS-CROSSWORD wait for this line before touching the palette or `decode_key.py`.

## Unit 1 (A1): tools/cvd_check.py

- Functions: `simulate(hex, kind, severity=1.0)` (Machado, Oliveira and Fernandes 2009 matrices for protan, deutan and
  tritan at severity 1.0, applied to linear RGB); `de2000(lab1, lab2)` (CIEDE2000, Sharma, Wu and Dalal 2005);
  `contrast(a, b)` (WCAG 2.1 relative luminance); `check(marks, bg, tints=(), text=())` returning every failing pair
  and each palette's **margin** (worst pair minus the gate).
- Gate: every pair of mark colours differs by CIEDE2000 >= 20 in normal vision and in each simulation; every mark
  reaches 3:1 against the background; every text colour 4.5:1; a tint gives the text drawn on it 4.5:1.
- **The 20 is a declared design threshold, not a sourced one.** No published CVD-palette minimum was cited, and the
  same 9 Oct pass chose it and the palettes, so the `sorter_light` palette's worst pair (20.7) passes by only 0.7.
  Pre-register it in `PREREG-MQS-SHEETS.md` with that sentence (or cite a published minimum if you find one and use
  it). Results: PASS at >= 20; **WARN, exit 2, "judgement call: under the declared gate by < 2"** for 18 <= worst < 20;
  FAIL, exit 1, below 18 or on any contrast failure. Every run prints each vision's worst pair and the margin.
- `PALETTES` constant (research note section f): `sorter_light` = ink #24211c, blue #0072B2, dark orange #B35900, grey
  #767676 on #f3f1ec; `sheets_light` = black, #0072B2, #B35900, grey #595959 on white; `dark` = #ece6dc, sky #56B4E9,
  orange #E69F00 on #1b1916. Tints yellow #F0E442 and sky #56B4E9 are fills only, and **the text on a tint is dark ink
  in both themes** (#24211c in `sorter_light`: 12.13:1 and 6.95:1; #1b1916 in `dark`: 13.26:1 and 7.60:1): each palette
  carries its tint/text pairs. The dark theme's light ink #ece6dc on those tints gives 1.07:1 and 1.86:1.
- CLI: `python3 tools/cvd_check.py --marks '#24211c,#0072B2,#B35900,#767676' --bg '#f3f1ec' [--tints ...] [--text ...]`
  and `--palette NAME`; prints the worst pair and the margin per vision; exit 0 / 2 / 1 as above.
- Test `tools/tests/test_cvd_check.py` (expected values are the 9 Oct pass's own computation):
  - must catch: legacy sorter ok #2f6b3a vs bad #b3261e FAILS (deutan 11.3, protan 8.7, each +-0.5);
  - must catch: the first proposed set (#0072B2, #E69F00, #F0E442, #CC79A7 on white) FAILS (orange vs yellow deutan
    11.6 +-0.5; #E69F00 contrast on white 2.25 +-0.02);
  - must catch: light ink #ece6dc on the yellow tint FAILS (1.07 +-0.02);
  - must not block: `sorter_light` passes (worst 20.7 +-0.5, blue vs grey protan, margin printed), `sheets_light` passes
    (22.7 +-0.5), `dark` passes with its tint/text pairs (25.5 +-0.5);
  - a synthetic palette at worst 19.5 returns exit 2, not 1;
  - if scikit-image imports, `de2000` agrees with `skimage.color.deltaE_ciede2000` within 0.01 on 20 random pairs
    (skipped otherwise).

## Unit 2 (A1): decode_key.py --style case

Per token, from the job's own records: H, C and S values in CAPITALS; M in lower case; I in lower case inside
[brackets] (so exceptions.tsv corrections, which are graded, show in brackets); U as `<code>`; NULL as `_` (the CTTS
convention). Clear-hand words (record kind `clear`) get a declared form of their own (for example `{word}`) so they never
read as H/C/S capitals: Danzay's reading already uses CAPS for clear-hand words, and the existing `words` style
(dupuy468-anhalt's) upper-cases cipher runs, so do not test against another style's string. Test
`tools/tests/test_decode_key_case.py` token by token against `reading_tokens.tsv` on
`tools/tests/decode_configs/fr20140-danzay-1557.json` and `fr2980-gramont.json`: the folded value matches and the case
matches the grade for every token; `--check` behaviour of existing styles is unchanged.

## Unit 3 (A1): tools/decipher_sheet.py

CLI:
```
python3 tools/decipher_sheet.py key ciphers/<t> [--config CONFIG] [--job NAME] [--tiles boxes|lines|none] [--variants 3] [--mi-panel] --out <dir>/<stem>-key.html [--png] [--pdf] [--check]
python3 tools/decipher_sheet.py reading ciphers/<t> [--config CONFIG] --job NAME [--lines L01-L12] [--highlight CODE[,CODE]] [--annotate notes.tsv] --out <dir>/<stem>-reading.html [--png] [--pdf] [--check]
```
- Loads config, key, exceptions and grades through `decode_key.py`'s own functions; parses no key format itself
  (Gramont key.tsv is code/value/grade/source; Danzay's is a commented sign/glyph/value table read through its test config).
- Tiles, in this order: (a) per-sign boxes (`atlas/signs.tsv` + `pages.json` + a box-to-token map such as Birago's
  `atlas/no87_box_token.tsv`); (b) line crops with a known token order (the sheet then says "token row not aligned to the
  image"); (c) none (codes in monospace). Crops only from images already committed; no network. **Birago's map covers
  f.178v and f.179r only (748 rows: 659 + 89; 714 1:1, 26 2:1, 8 1:2).** f.178r has no boxes (`no87_map.py`: its three
  lines slope across one another), so f.178r tiles fall to (b) with the "not aligned" notice; the sheet counts non-1:1
  rows apart and marks them.
- **Key sheet:** an A-Z homophone header (I/J and U/V merged; W only if keyed); under each letter every code with up to
  `--variants` exemplar crops picked by `glyph_atlas.pick_spread` from the folder's graded boxes (H/C/S only, through
  glyph_atlas's `--from-truth`/`--grades` loader), the code in small monospace, its count n and a superscript grade;
  special symbols (nulls; repeat/delete only if decode.json declares them); nomenclature by value class (persons and
  places, titles, words, syllables, function words, numbers); months and enclosure marks when present; a "keyed but not
  attested here" strip. M values in lower case with '?'; a U glyph as '?'. An "(or vice versa)" brace only where a key or
  exceptions row explicitly records an undecided swap: **`key_conflicts.tsv` in the Blathwayt folder is a per-item count
  of glossed columns that differ from the key, not a list of swapped pairs; never draw braces from it.** `--mi-panel`
  adds the promoted RUN1-MOR panel.
- **Reading sheet:** header with unit, date, sender -> recipient, place, shelfmark and leaf link; the N-class and key
  source (`ours|period|published`) from AUDIT.md/status.json; the rule-4 grade counts; the depth in rule 4a's exact
  words from status.json `depth` (D1 "fragments read", D2 "partially deciphered (about N%)", D3 "largely deciphered
  (about N%)", D4 "deciphered", with "; N name codes unidentified" when the status says so; no reading sheet at D0; "key
  identified" only for a period or published key); one editorial-conventions line (how u/v and i/j are shown; that
  capitals are H/C/S, lower case M, [brackets] inferred or corrected; where each nomenclature spelling comes from: the
  paper does the same at p.136 n.95). Per manuscript line: the line crop, a token row (each tile under its box when boxes
  exist) and a value row; nomenclature values in small capitals. Then the edited text (`--style case`) and a
  translation only if one already exists in the folder (never generated). `--highlight CODE` outlines every occurrence
  with a number badge and its own dash pattern (the Fig. 9-10 analogue). `--annotate FILE.tsv` (token index, category,
  text) makes the Fig. B24-style strip, each callout starting with its category word (OK, WRONG-KEY, DEL).
- **Colour** (research note section f): `cvd_check.PALETTES['sheets_light']` only, checked inside the test. Grades by
  form first: H and C bold capitals with a superscript letter; S capitals, solid blue #0072B2 underline; M lower case,
  dashed dark-orange #B35900 underline, trailing '?'; I lower-case italic in [brackets], dotted ink underline (no third
  hue); U `<code>` in grey #595959 monospace; NULL a middle dot. Highlights: blue, dark orange, black, each with its own
  dash pattern and a number badge. No red, no green; orange never as text on beige; text on a tint is dark ink.
- **Footer:** whose key ("Key: published by S. Tomokiyo and G. Lasry" for Gramont; "Key: S. Tomokiyo's 2026
  reconstruction" for Danzay; "Key: Tomokiyo's Nevers-Birago 1572 table" for Birago; the cipher book for Eckert), with
  the page link; the image source ("Source gallica.bnf.fr / BnF" with the ark at the leaf; for Eckert "Thomas T. Eckert
  Papers, mssEC 19, The Huntington Library, San Marino, California" and the rights statement in
  `ciphers/eckert-1864/images/README.md` "Rights"); the repository commit and the render time from `date -u`; "Layout
  after Lasry, Biermann and Tomokiyo 2023, Figs 12-14 (pp.125-127); no figure reproduced"; the grade legend.
- **Output:** self-contained HTML (tiles as JPEG data URIs, quality 70), at most 3 MB per sheet and 20 MB for the whole
  `outreach/sheets/` folder; PNG through `NODE_PATH=$(npm root -g) node tools/browser_fetch.js file://<abs path> <out.html> --shot <out.png>`
  (and `--pdf` for an A4 PDF if you want one). Each HTML embeds a sha256 of every input; `--check` re-renders and exits
  1 when stale (rule 7). Light theme for print; dark tokens defined for screens.
- **Restricted material never:** the tool refuses a folder carrying a `RESTRICTED.md` (ciphers/debosnys-1883) and any
  path under `restricted/`; run `python3 tools/restricted_guard.py --outgoing` before the push and paste its line.
- **Tile check, programmatic (`decipher_sheet.py ... --tile-report TSV`, used by K3):** per tile, crop non-empty, ink
  share above a floor (pre-register it), and, where the tile has a sign label and the key gives that label a value,
  label/value agreement with the token's value row; the report counts tiles failing each test.
- Tests `tools/tests/test_decipher_sheet.py` (offline): the value row equals decode_key's own rendering token for token on
  the Gramont and Danzay test configs; the grade-to-form mapping for every grade letter; every pair of grade classes
  differs in a non-colour property; the exemplar row's tile ids equal `glyph_atlas.pick_spread`'s for the same inputs;
  `--check` fails after a one-byte change to key.tsv; the footer carries the key source; with no boxes (and on f.178r)
  the "not aligned" notice is present; no brace is drawn from a key_conflicts-style count file (must not block: a sheet
  with no swap record has no brace); a RESTRICTED.md folder is refused; `--tile-report` flags a blank crop.

## Unit 4 (A1): regression tests and the map test (pre-register in PREREG-MQS-SHEETS.md first)

- **R-K1 and R-K2 are regression tests, not known-answer controls.** The value row is loaded through decode_key's own
  functions and compared with decode_key's own output, and R-K1's coordinates are compared with the map they were cut
  from, so they can fail only through a code bug. Keep them, named as regression tests: R-K1, every tile on Birago no.87
  is cut at the box `atlas/no87_box_token.tsv` assigns (100%) and the value row equals decode_key's no.87 reading (100%);
  R-K2, Gramont f.29r's value row equals `reading_tokens.tsv` (100%), and a key with two values swapped changes the value
  row at exactly those two codes' tokens.
- **KM, the box-to-token map test (the open risk).** `no87_box_token.tsv` comes from a label-blind width-only DP
  (`atlas/no87_map.py`), and BIR-ADJ and BIR87-ALIGN named "tile-to-position mapping" as an untested suspect, with a check
  of about USD 2 never run (nevers-birago NOTES.md lines ~2437-2440, ~2502). Test it through **this tool's own cut
  path**: cut every 1:1 tile on the held-out lines (f.178v L13-L23 and f.179r L01-L03, `split` not `tune`: the tune lines
  named the atlas clusters through this same map) and classify it with `glyph_atlas.py classify --holdout` (those lines
  kept out of the vote); compare the classifier's top-1 with the token's own `sign` label. The one earlier measurement
  sets the expectation: TX-ATLAS-B72 (NOTES.md ~2045-2070) found atlas top-1 = line-read label on 0.609 of held-out
  tokens, the kNN label matching the token's own label 225 times and a neighbour's 77 times (its 0.754 is leave-one-out
  on the tune tiles, not this statistic). Pre-register: agreement about 0.61, gate >= 0.55 **and** above the p95 of a
  null that permutes box ids within each line (20 draws, re-cut each time: the image moves with the permutation and the
  label does not, so this statistic depends on the map); report own-label vs neighbour-label counts beside it. Count the
  26 2:1 and 8 1:2 rows apart and never in the gate. If KM misses its gate, the box mode ships `weak` for Birago, every
  Birago sheet carries "tile placement unverified", and the result goes in the report as the answer to BIR-ADJ's open
  suggestion. (A key-value check of a row's `sign` label against its `truth` letter does not test the map: both are
  token properties the map does not move; BIR87-ALIGN already measured that at 0.896.)

## Unit 6 (A2): sample renders, five public then two held (one unit each; stop before a unit that would cross 80%)

Each render: `decipher_sheet.py ... --tile-report`; then **K3**: the programmatic counts on every tile, and one eye check
on a grid of at most 60 tiles (all exemplars for a key sheet up to 60, else a seeded random sample), each grid cell the
tile beside its code's key-sheet exemplar so "misplaced" has a reference (1 vision call, priced in the unit). Pre-register
in A1's PREREG: a sheet with more than 10% unusable or misplaced tiles in either count (RUN3-MOR's line) is labelled "not
fit to show" in the README and is not offered. Never send a whole sheet screenshot to a vision call (Usage 6, GOLD-4D,
AX-4612TR).
1. **Gramont**: key sheet and the **f.29r** reading (to Villandry, 20 May 1530; status.json results[11], D2).
2. **Danzay ff.35-36** (27 Jan 1557; results[13], D2): key sheet and reading through
   `tools/tests/decode_configs/fr20140-danzay-1557.json` (the folder has decode.py, not decode.json).
3. **Huntington E4**: mssEC 19 p.49 (pointer 8941; image `ciphers/eckert-1864/images/mssEC19_p8941.jpg`), Fox to
   Butler, 21 Apr 1864 (N4, D4 on the Huntington list `outreach/huntington-decipherments-list-2026-10-08.tsv`): a
   word-code reading sheet (ledger page, code word, meaning, grade H from the cipher book), its key section the code
   words this telegram uses, from key.md. The E52 sample in the earlier spec cannot be rendered (its page image is not
   committed and eckert has no decode.json); E4's page is committed.
4. **Held, scratchpad only:** the **Birago 1572** key sheet (`harvest/key_1572_sheet.tsv`, Tomokiyo's published table)
   and the **no.87** reading (the box-mode test; f.178r in line-crop mode). Run K3 on them in the scratchpad; record only
   counts in the README. Never write them into `outreach/sheets/`, never commit them, never show them to anyone.

`outreach/sheets/README.md`: one line per sheet (file, target, unit, depth wording, key source, K3 counts, commit) under
the header "Samples for the owner to look at. Nothing here is sent; any outward use passes outreach gate 7." Each held
Birago sheet gets a line "held: open owner sort in this key family (ASKS row 118 and the 2 Oct / 3 Oct Birago sorter
rows); regenerate with `<command>` once those rows are done and no Birago family sorter is open", with its K3 counts.
The account-3 parent, not you, publishes any sheet as a private Artifact for the owner.

## Unit 5 (A1) and unit 7 (A2): registration

- tool_shelf rows (A1): `decipher_sheet.py` (kind renderer, grade n/a; evidence R-K1/R-K2 as regression tests and KM
  with its null), `cvd_check.py` (kind gate, evidence the must-catch numbers and the declared-threshold sentence),
  `decode_key.py --style case` (kind renderer). A2 adds the K3 counts to the evidence cell.
- SYSTEM.md (A1): a row each for `tools/decipher_sheet.py` and `tools/cvd_check.py` (the colour gate), and `--style case`
  on decode_key.py's row.
- CLAUDE.md Usage 8 line (for the orchestrator): "`tools/decipher_sheet.py key|reading ciphers/<t>` renders a key sheet
  and a reading sheet from the folder's own graded data (exemplars by `glyph_atlas.py`'s picker; layout after Lasry,
  Biermann and Tomokiyo 2023, no figure reproduced); a reading described outside the repository goes with them, and a
  sheet in a key family with an open blind sort is held. `tools/cvd_check.py` is the colour gate for any page or figure a
  person reads: never meaning by hue alone, never red against green, text on a tint in dark ink (MQS-SHEETS, 9 Oct 2026)."
- README common-tail line: "Any page, sheet or figure made for a person passes `tools/cvd_check.py` and carries every
  state by a non-colour cue too (glyph, border, case, label); never red against green; no key-value sheet for a key family
  while a blind sort in it is open (research/MARY-STUART-TALK-2026-10-09.md section f)."

## Common rules (every MQS job; read in full before the first command)

- **First commands.** `git fetch origin && git checkout -B main origin/main`; `python3 tools/room.py --start`; `date -u`.
  Every time and date you write comes from `date -u` (rule 6). Read the last 30 lines of ROOM.md. If a claim under six
  hours old with no done line covers a file you own below, stop and write one ROOM `flag` line instead of working.
- **Claim.** `python3 tools/room.py "MQS-SHEETS worker (account 4)" "claim <HH:MM> UTC by date -u: <your files>; cap USD <7 for A1, 6 for A2>, box <120 for A1, 110 for A2> min (80% line <HH:MM>) -- for LANE MQS (account 4)"` (job A2 writes `MQS-SHEETS-R` wherever this section says `MQS-SHEETS`).
- **Your files.** Exactly the ones under "Files" below; the lane brief's file table says who owns what. Extend the
  existing script (CLAUDE.md Usage 8): an option and its functions; existing behaviour and existing tests unchanged.
  Run the tool's existing tests before your first edit and again before the push, and paste both results; a test that
  already failed before you started is named as pre-existing, not yours to fix.
- **Promotion (Usage 8).** Logic taken from a target-local script moves into the shared tool with credit in the
  docstring (the script's path, its job id and date). The original keeps working and gets one header line:
  `promoted to tools/<tool> <option> (MQS-SHEETS, 9 Oct 2026); kept because its outputs are cited` (the
  `tools/interlinear_align.py` precedent). No code from aaymeloglu/unsolved-ciphers (no licence; cite only). Bourdeau's
  code is MIT and CTTS is Apache-2.0: credit either if you adapt anything from it.
- **Usage 8a scope.** The docstring states, per option, what it is meant to catch and at least one case it must NOT
  flag, each backed by an offline test (no network in any test).
- **Rule 3.** Write every control's expected number and gate into `tools/tests/PREREG-MQS-SHEETS.md` and push that file
  BEFORE the control runs. Say in one line why each null can fail differently from the known answer for the statistic
  you compute (CLAUDE.md rule 3, the "control that cannot vary" paragraph). Check the control is not already near
  ceiling (about 95%) or matched by more restarts alone before reading any gain. A control that misses its gate ships
  the option with shelf grade `weak` and both numbers; it is not withdrawn, and nothing is run on a target from it.
- **Prior-work step** (`.claude/briefs/prior-work-step.md`). For every `ciphers/<slug>` folder you use as a known
  answer: `python3 tools/prior_work.py <slug> --step-type decode --known-answer gate:MQS-SHEETS --fetch` and paste its exit
  line. A known answer on already-read material is the point here. This is a tool job: no target is read, keyed or
  decoded beyond the named controls, and no target's status, key, reading or AUDIT.md changes.
- **Hosts.** None unless your job names one. Good-citizen rule: one request at a time, at least 1.5 s apart (2 s for
  BnF), User-Agent `cipher-lab research script (contact via repository)`, fetch once to disk with a manifest, read from
  disk after. On a 403, 429 or challenge page: stop using that host, log it in ROOM.md, never retry in a loop. No
  Gallica requests at all (HTTP 403 to cloud sessions since about 12:45 UTC on 8 Oct 2026). Report requests per host.
- **Registration (yours).** One row per tool or option in `tools/data/tool_shelf.tsv` (columns tool, kind, grade,
  use_when in the words a future brief would use, evidence = control numbers + file path, last_outcome). Paste
  `python3 tools/tool_shelf.py "<phrasing>"` for three phrasings per row, each showing your row in the top 3, and
  `python3 tools/tool_shelf.py --check` (your rows must not appear as MISSING; the 17 pre-existing MISSING rows are not
  yours). Name the tool or option on its row in `SYSTEM.md` (an added tool gets its own row, in the same commit) and
  paste `python3 tools/system_map_check.py` (exit 0). **Do not edit CLAUDE.md or `.claude/briefs/README.md`:** give the
  exact lines under "Registration" below in your final report; the lane orchestrator commits all eight jobs' lines in
  one edit at close (the TOOLS-TOMO precedent, 8 Oct 2026).
- **Commit and push.** Fetch and rebase before writing a shared file (`tools/data/tool_shelf.tsv`, `SYSTEM.md`,
  `ROOM.md`); keep both facts on a conflict. Before the final push run
  `python3 tools/file_shrink_guard.py <every file you touched>` and paste the output. Commit by explicit path only,
  ending the message with the two attribution lines YOUR session's system reminder gives (its Co-Authored-By line
  and your own Claude-Session URL; never a session URL copied from this brief, which would break the per-session
  trail rule 6 rebuilds from `git log`), through room.py's rebase-and-retry push:

  ```
  MSG="$(printf 'MQS-SHEETS: <one-line summary>\n\n<Co-Authored-By line from YOUR session's system reminder>\n<Claude-Session line from YOUR session's system reminder>\n')" \
    python3 tools/room.py --push <path1> <path2> ...
  ```

  Never `git add -A` or `git add .`, never force-push, never rewrite history. Push working increments (tests green)
  rather than one large commit at the end.
- **Words.** Rule 10 and rule 4a only: report what was found and where it was not found; never "solved", "cracked",
  "novel", "first" or "new" for anything this project did; do not classify novelty. Never name the owner in a
  committed file; never print a credential; never call AskUserQuestion.
- **Stop.** At the cap or at 80% of the box, whichever comes first, and do not start a unit that would cross 80% of
  either (Usage 6: the unit table gives each unit's dollar and minute estimates; check both before each unit). The orchestrator reads your cost every 15 minutes
  and will interrupt at the cap. Stop when the brief is met (Usage 7): follow-ups go in your report as one-line
  suggestions, never as extra work.
- **Done.** One ROOM line:
  `python3 tools/room.py "MQS-SHEETS worker (account 4)" "done (<start>-<end> UTC by date -u, brief met|stopped at cap): <option: control number vs null; shelf grade; commit> -- for LANE MQS (account 4)"`,
  then a final report of at most ten lines: per option the control and its number, the null and its number, the shelf
  grade, the three tool_shelf phrasings, requests per host, and the CLAUDE.md and README lines for the orchestrator.
