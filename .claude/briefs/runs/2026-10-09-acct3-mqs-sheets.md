# MQS-SHEETS: key and reading sheets, the colour check, and capitals for confirmed values (job A of LANE MQS)

Written 9 Oct 2026 (clock read 00:58 UTC) by the account-3 orchestrator's reconciling session, for one worker on
**account 4**. Lane brief: `.claude/briefs/runs/2026-10-09-acct3-mqs-lane.md`. Background and every number cited:
`research/MARY-STUART-TALK-2026-10-09.md` (sections c and f) and matrix rows M09, M10, M25, M30, M31, M47 of
`research/MARY-STUART-TALK-2026-10-09.tsv`.

- **Model:** Sonnet (`claude-sonnet-5`). **Cap:** USD 9. **Box:** 140 min.
- **Goal:** the owner's item 3. Sheets in the format Tomokiyo and Lasry publish (key table; interlinear reading),
  rendered from a target folder's own graded data, so a recipient can check a reading against the manuscript from
  their own desk; sample sheets for Tomokiyo's three targets and one Huntington telegram in `outreach/sheets/`.
  Layout after Lasry, Biermann and Tomokiyo 2023, Figs 5-14 and B24 (pp.112-127, 200), **described, never copied**:
  the paper is CC BY-NC-ND. Glyphs are always cut from the manuscript images on disk, never from anyone's drawn table.

## Promote or build (decided)

- **Promote** `ciphers/moray-wood-1568/no804/refsheet/build_refsheet.py` (RUN1-MOR, 4 Oct 2026) into the key sheet:
  its one-row-per-class exemplar layout in key.tsv order, and its panel that puts each M/I-graded token beside its three
  nearest S-graded exemplars (binarised 32x32 masks, Dice overlap, best of +-2 px shifts). Its evidence comes with it:
  RUN3-MOR's eye check (11 of 102 boxes unusable, 10.8%) and RUN4-MOR's fix (0 of the 11), leave-one-out top-1 0.513 vs
  label-shuffle p99 0.128. Credit Aymeloglu for the Moray labels (cited only, no code copied).
- **Build** `tools/decipher_sheet.py` (nothing in tools/ renders sheets) and `tools/cvd_check.py` (no colour check
  exists). **Extend** `tools/decode_key.py` with `--style case`.
- **Not in this job:** the `register` page (deferred to a later PILE-REGISTER job built on `tools/holder_export.py`'s
  rows; holder_export.py already writes the Huntington per-item register). **Do not edit `tools/holder_export.py`**
  (the HOLDER-EXPORT fix worker claimed it at 00:40 UTC 9 Oct); import its functions read-only if you need its
  md-blocks loader for Eckert.

## Files

`tools/cvd_check.py` (added), `tools/decipher_sheet.py` (added), `tools/decode_key.py` (a `render_case` function, the
`'case'` entry in `STYLES` and the `--style` choices only), `tools/tests/test_cvd_check.py`,
`tools/tests/test_decipher_sheet.py`, `tools/tests/test_decode_key_case.py`, `tools/tests/PREREG-MQS-SHEETS.md`,
`outreach/sheets/` (README.md and the sample sheets), one header line in
`ciphers/moray-wood-1568/no804/refsheet/build_refsheet.py`, rows in `tools/data/tool_shelf.tsv` and `SYSTEM.md`.
Sheets are written to `outreach/sheets/` only: the Gramont and Eckert folders already hold 28 and 27 MB of images,
near CLAUDE.md's 30 MB-per-folder image line, and a sheet embeds its tiles.

## Units (Usage 6: per-unit estimates; stop before a unit that would cross 80% of cap or box)

| # | Unit | Estimate |
|---|---|---|
| 1 | `tools/cvd_check.py` + test | USD 0.6 |
| 2 | `decode_key.py --style case` + test; push units 1-2 and post the ROOM line below | 0.6 |
| 3 | `tools/decipher_sheet.py key` and `reading` + tests (promotion included) | 3.2 |
| 4 | PREREG, then known-answer controls K1-K2 | 0.6 |
| 5 | Renders R1-R5: each one render + one screenshot read (1 vision call) + a fix if needed, about 0.6 each | 3.0 |
| 6 | Registration | 0.4 |
| | Total 8.4 (vision calls: 5 x about 0.3 included); cap 9 | |

**Units 1-2 first, pushed within about 30 minutes**, then one ROOM line:
`python3 tools/room.py "MQS-SHEETS worker (account 4)" "step 1 pushed: tools/cvd_check.py and decode_key.py --style case (<commit>) -- for LANE MQS (account 4)"`.
Jobs MQS-SORTER and MQS-CROSSWORD wait for this line before touching the palette or `decode_key.py`.

## Unit 1: tools/cvd_check.py

- Functions: `simulate(hex, kind, severity=1.0)` (Machado, Oliveira and Fernandes 2009 matrices for protan, deutan and
  tritan at severity 1.0, applied to linear RGB); `de2000(lab1, lab2)` (CIEDE2000, Sharma, Wu and Dalal 2005);
  `contrast(a, b)` (WCAG 2.1 relative luminance); `check(marks, bg, tints=(), text=())` returning every failing pair.
- Gate: every pair of mark colours differs by CIEDE2000 >= 20 in normal vision and in each simulation; every mark
  reaches 3:1 against the background; every text colour 4.5:1; a tint gives its ink text 4.5:1.
- `PALETTES` constant (research note section f): `sorter_light` = ink #24211c, blue #0072B2, dark orange #B35900, grey
  #767676 on #f3f1ec; `sheets_light` = black, #0072B2, #B35900, grey #595959 on white; `dark` = #ece6dc, sky #56B4E9,
  orange #E69F00 on #1b1916; tints yellow #F0E442 and sky #56B4E9 (fills only).
- CLI: `python3 tools/cvd_check.py --marks '#24211c,#0072B2,#B35900,#767676' --bg '#f3f1ec' [--tints ...] [--text ...]`
  and `--palette NAME`; prints the worst pair per vision; exit 1 on any failure.
- Test `tools/tests/test_cvd_check.py` (expected values are this pass's own computation, 9 Oct 2026):
  - must catch: legacy sorter ok #2f6b3a vs bad #b3261e FAILS (deutan 11.3, protan 8.7, each +-0.5);
  - must catch: the first proposed set (#0072B2, #E69F00, #F0E442, #CC79A7 on white) FAILS (orange vs yellow deutan
    11.6 +-0.5; #E69F00 contrast on white 2.25 +-0.02);
  - must not block: `sorter_light` passes (worst 20.7 +-0.5, blue vs grey protan), `sheets_light` passes (22.7 +-0.5),
    `dark` passes (25.5 +-0.5);
  - if scikit-image imports, `de2000` agrees with `skimage.color.deltaE_ciede2000` within 0.01 on 20 random pairs
    (skipped otherwise).

## Unit 2: decode_key.py --style case

Per token, from the job's own records: H, C and S values in CAPITALS; M in lower case; I in lower case inside
[brackets] (so exceptions.tsv corrections, which are graded, show in brackets); U as `<code>`; NULL as `_` (the CTTS
convention). Clear-hand words (record kind `clear`) get a declared form of their own (for example `{word}`) so they never
read as H/C/S capitals: Danzay's reading already uses CAPS for clear-hand words, and the existing `words` style
(dupuy468-anhalt's) upper-cases cipher runs, so do not test against another style's string. Test
`tools/tests/test_decode_key_case.py` token by token against `reading_tokens.tsv` on
`tools/tests/decode_configs/fr20140-danzay-1557.json` and `fr2980-gramont.json`: the folded value matches and the case
matches the grade for every token; `--check` behaviour of existing styles is unchanged.

## Unit 3: tools/decipher_sheet.py

CLI:
```
python3 tools/decipher_sheet.py key ciphers/<t> [--config CONFIG] [--job NAME] [--tiles boxes|lines|none] [--variants 3] [--mi-panel] --out outreach/sheets/<stem>-key.html [--png] [--pdf] [--check]
python3 tools/decipher_sheet.py reading ciphers/<t> [--config CONFIG] --job NAME [--lines L01-L12] [--highlight CODE[,CODE]] [--annotate notes.tsv] --out outreach/sheets/<stem>-reading.html [--png] [--pdf] [--check]
```
- Loads config, key, exceptions and grades through `decode_key.py`'s own functions; parses no key format itself
  (Gramont key.tsv is code/value/grade/source; Danzay's is a commented sign/glyph/value table read through its test config).
- Tiles, in this order: (a) per-sign boxes (`atlas/signs.tsv` + `pages.json` + a box-to-token map such as Birago's
  `atlas/no87_box_token.tsv`); (b) line crops with a known token order (the sheet then says "token row not aligned to the
  image"); (c) none (codes in monospace). Crops only from images already committed; no network.
- **Key sheet:** an A-Z homophone header (I/J and U/V merged; W only if keyed); under each letter every code with its
  median exemplar crop (up to `--variants`), the code in small monospace, its count n and a superscript grade; special
  symbols (nulls; repeat/delete only if decode.json declares them); nomenclature by value class (persons and places,
  titles, words, syllables, function words, numbers); months and enclosure marks when present; a "keyed but not attested
  here" strip. M values in lower case with '?'; a U glyph as '?'. An "(or vice versa)" brace only where a key or
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
  dash pattern and a number badge. No red, no green; orange never as text on beige.
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
- Tests `tools/tests/test_decipher_sheet.py` (offline): the value row equals decode_key's own rendering token for token on
  the Gramont and Danzay test configs; the grade-to-form mapping for every grade letter; every pair of grade classes
  differs in a non-colour property; `--check` fails after a one-byte change to key.tsv; the footer carries the key
  source; with no boxes the "not aligned" notice is present; no brace is drawn from a key_conflicts-style count file
  (must not block: a sheet with no swap record has no brace); a RESTRICTED.md folder is refused.

## Unit 4: known-answer controls (pre-register in PREREG-MQS-SHEETS.md first)

- **K1, Birago no.87** (`ciphers/nevers-birago-fr3251-1572`, jobs f178r, f178v, f179r; `atlas/no87_box_token.tsv`,
  748 token rows): every token tile is cut from the box the map assigns to that token (coordinates equal `signs.tsv`'s
  box) for 100% of mapped tokens, and the value row equals decode_key's no.87 reading token for token (100%). Null that
  can fail differently: the same map with sids permuted within each line must fail the coordinate check on at least 90%
  of tokens.
- **K2, Gramont f.29r**: the value row equals `reading_tokens.tsv` token for token (100%). Null: a key with two values
  swapped changes the value row at exactly the tokens of those two codes, and nowhere else.
- **K3, tile quality before anything is shown**: on each rendered sheet, one screenshot read counts unusable or
  misplaced tiles; a sheet above 10% (RUN3-MOR's line) is labelled "not fit to show" in `outreach/sheets/README.md` and
  is not offered.

## Unit 5: sample renders (one unit each; stop before a unit that would cross 80%)

1. **Birago 1572** key sheet (`harvest/key_1572_sheet.tsv`, Tomokiyo's published table) and the **no.87** reading (the
   control, internal): `outreach/sheets/birago1572-key.html`, `birago1572-no87-reading.html`.
2. **Birago no.86** reading (status.json results[104], D2).
3. **Gramont**: key sheet and the **f.29r** reading (to Villandry, 20 May 1530; results[11], D2).
4. **Danzay ff.35-36** (27 Jan 1557; results[13], D2): key sheet and reading through
   `tools/tests/decode_configs/fr20140-danzay-1557.json` (the folder has decode.py, not decode.json).
5. **Huntington E4**: mssEC 19 p.49 (pointer 8941; image `ciphers/eckert-1864/images/mssEC19_p8941.jpg`), Fox to
   Butler, 21 Apr 1864 (N4, D4 on the Huntington list `outreach/huntington-decipherments-list-2026-10-08.tsv`): a
   word-code reading sheet (ledger page, code word, meaning, grade H from the cipher book), its key section the code
   words this telegram uses, from key.md. The E52 sample in the earlier spec cannot be rendered (its page image is not
   committed and eckert has no decode.json); E4's page is committed.
6. Only if under 80% of cap and box: Birago no.71 and no.90 readings (results[103], [105]).

`outreach/sheets/README.md`: one line per sheet (file, target, unit, depth wording, key source, tile-check count,
commit) under the header "Samples for the owner to look at. Nothing here is sent; any outward use passes outreach
gate 7." The account-3 parent, not you, publishes any of them as a private Artifact for the owner.

## Registration

- tool_shelf rows: `decipher_sheet.py` (kind renderer, grade n/a, evidence K1/K2 numbers), `cvd_check.py` (kind gate,
  evidence the must-catch numbers), `decode_key.py --style case` (kind renderer).
- SYSTEM.md: a row each for `tools/decipher_sheet.py` and `tools/cvd_check.py` (the colour gate), and `--style case` on
  decode_key.py's row.
- CLAUDE.md Usage 8 line (for the orchestrator): "`tools/decipher_sheet.py key|reading ciphers/<t>` renders a key sheet
  and a reading sheet from the folder's own graded data (layout after Lasry, Biermann and Tomokiyo 2023, no figure
  reproduced); a reading described outside the repository goes with them. `tools/cvd_check.py` is the colour gate for any
  page or figure a person reads: never meaning by hue alone, never red against green (MQS-SHEETS, 9 Oct 2026)."
- README common-tail line: "Any page, sheet or figure made for a person passes `tools/cvd_check.py` and carries every
  state by a non-colour cue too (glyph, border, case, label); never red against green (research/MARY-STUART-TALK-2026-10-09.md
  section f)."

## Common rules (every MQS job; read in full before the first command)

- **First commands.** `git fetch origin && git checkout -B main origin/main`; `python3 tools/room.py --start`; `date -u`.
  Every time and date you write comes from `date -u` (rule 6). Read the last 30 lines of ROOM.md. If a claim under six
  hours old with no done line covers a file you own below, stop and write one ROOM `flag` line instead of working.
- **Claim.** `python3 tools/room.py "MQS-SHEETS worker (account 4)" "claim <HH:MM> UTC by date -u: <your files>; cap USD 9, box 140 min (80% line <HH:MM>) -- for LANE MQS (account 4)"`.
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
  with the two attribution lines, through room.py's rebase-and-retry push:

  ```
  MSG="$(printf 'MQS-SHEETS: <one-line summary>\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_0198Cv8ypBfBVfRToKVWx33M\n')" \
    python3 tools/room.py --push <path1> <path2> ...
  ```

  Never `git add -A` or `git add .`, never force-push, never rewrite history. Push working increments (tests green)
  rather than one large commit at the end.
- **Words.** Rule 10 and rule 4a only: report what was found and where it was not found; never "solved", "cracked",
  "novel", "first" or "new" for anything this project did; do not classify novelty. Never name the owner in a
  committed file; never print a credential; never call AskUserQuestion.
- **Stop.** At the cap or at 80% of the box, whichever comes first, and do not start a unit that would cross 80% of
  either (Usage 6: the unit list below gives each unit's estimate). The orchestrator reads your cost every 15 minutes
  and will interrupt at the cap. Stop when the brief is met (Usage 7): follow-ups go in your report as one-line
  suggestions, never as extra work.
- **Done.** One ROOM line:
  `python3 tools/room.py "MQS-SHEETS worker (account 4)" "done (<start>-<end> UTC by date -u, brief met|stopped at cap): <option: control number vs null; shelf grade; commit> -- for LANE MQS (account 4)"`,
  then a final report of at most ten lines: per option the control and its number, the null and its number, the shelf
  grade, the three tool_shelf phrasings, requests per host, and the CLAUDE.md and README lines for the orchestrator.
