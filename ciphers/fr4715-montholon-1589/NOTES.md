open

INTAKE-4715 unit B, 27 Sept 2026: solver-ready intake only (Layout, no reading, no decoding, no class), on the
`ciphers/nevers-birago-fr3251-1572` pattern. Built from KEY-ADJACENT.tsv row 19 and
`sources/cryptiana/web/bnf4715.htm` (local mirror, section id=no58, read in full this session; not re-fetched).

# BnF fr.4715, no.58 (f.81), Sieur de Montholon to an unnamed recipient, Tours, 8 November 1589

Francois II de Montholon, Keeper of the Seals for the Catholic League. Digits, per bnf4715.htm.

Tomokiyo, verbatim (bnf4715.htm section id=no58):

> "no.58 (f.81) Letter of Montholon, Tours, 8 November 1589. This can be read with the Vieuville-Nevers
> cipher (for which see another article). The decipherment of the beginning is given below."

The BnF catalogue itself independently confirms this item is undeciphered: archivesetmanuscrits.bnf.fr
full-text search "non dechiffre", checked 27 Sept 2026 (ark:/12148/cc577658/cd0e811), "Lettre du Sr DE
MONTHOLON. Chiffre non dechiffre. Tours, 8 nov. 1589" -- matching sender, place and date exactly.

## The gate (this job's first step)

Fetched the page's own image for no.58 (`BnFfr4715f81.png`, into `sources/cryptiana/web/img/`, manifest not
yet written for this single file -- see "Requests" below) and looked at it directly: it is a plain manuscript
scan (dense cipher digit groups with a handful of interspersed plain-French words and a two-line clear
salutation/close top and bottom), not an interlinear or annotated reading like the mantua.htm case
(INTAKE-3979). The page's own prose confirms this independently: "The decipherment of the beginning is given
below" -- only the beginning, and the printed passage itself ends "...." (an explicit ellipsis in the source,
not this worker's truncation). **Gate verdict: only the opening is deciphered, the expected case** -- this is
a genuine open target with a partial known plaintext, not a found-solved retirement.

## What's on disk

- `known_plaintext.txt`: Tomokiyo's own printed prose decipherment of the letter's opening (grade H, rule 4 --
  his reading, not ours), transcribed verbatim from the local mirror.
- `aligned_dump.txt`: the SAME opening passage, but as Tomokiyo's own group-by-group cipher/plaintext
  alignment (his page's "DUMP" block, immediately after the prose) -- also grade H. Extracted by decoding the
  page's raw bytes as cp932 (it declares `charset=SHIFT_JIS`; a plain utf-8 read replaces several of the
  page's own printed glyphs with the mojibake replacement character, U+FFFD, losing real data -- flagged here
  since a later worker re-fetching or re-reading this page should decode it the same way).
- `keys/key_vieuville_nevers.tsv`: the letter-homophone substitution table from `nevers.htm` (section
  id=BnFfr3641, image `phelippes8.png`, a clean printed/digital table, not a hand-drawn one) -- 34 sign rows,
  21 plaintext-letter values (a-z minus j, k, v, w; French convention, i covers j, u covers v), transcribed by
  direct inspection plus one independent blind Sonnet subagent read as a cross-check (agreed on every cell
  except whether "64" sits under column h or i, settled by this worker with a zoomed pixel crop -- it is
  under i). Two cells hold a non-numeric printed glyph instead of a digit (the table's own s and x columns'
  extra homophones); both were **cross-validated**, not just visually re-checked, against `aligned_dump.txt`'s
  running text, which uses the identical characters for s and x in ordinary decoded words ("hasard",
  "excomunie") -- graded AB, not left at the initial M. `tools/key_design.py` reads it `usable=yes`,
  design_family `homophonic` (accurate for the letter table alone; see the word-code caveat below).
  `tools/key_design.py --check` passes; KEY-OFFICES.tsv and KEY-DESIGN.tsv both carry rows for this key.
- `images/manifest.json`: f.81r (canvas 177) and f.81v (canvas 178), Gallica ark btv1b52509819x, fetched at
  1000px. The ark's IIIF manifest carries its own folio labels for this span ('81r'/'81v' directly, not a
  formula-derived offset -- the manifest has two INCONSISTENT offset runs elsewhere in the volume per
  `tools/gallica_folio.py`'s own warning, so the label is what was used, not either offset). Eye-checked: a
  600px fetch of canvas f177 matches Tomokiyo's own page image (same wax-seal-shaped stamp top-left, same
  text-block shape, folio number "81" visible top-right) -- confirms the labelled canvas independently of the
  label itself.

## An important caveat for any future decode: a second, undocumented code table

nevers.htm's own prose on this cipher says: "Figures with a dot over the first digit are code numbers
representing common words" -- illustrated there only for a *different* letter (Governor of Sy to Nevers, BnF
fr.3633 f.22: 16=de, 19=et, 20=est, 24=il, 25=la, 26=le, 35=ne, 36=na, 40=ou, 42=pour, 43=plus, 46=que,
48=quil?, and two-dot forms 11=villes, 76=gens de pied, 88=duc, 93=monsieur). `aligned_dump.txt` (this
letter's own alignment) uses the SAME apostrophe/dot notation extensively -- roughly a third of its tokens are
dotted -- and glosses several of them directly: '47=qui, '30=ma, '41=par, '65=comme, '16=de, '11=au, '20=est,
'48=quil, '42=pour, '19=et, '46=que, '25=la, '35=ne, '50=se, '99=vous, '28=luy, '64=catholique, '75=faire,
'52=si, '22=je, '31=me, '40=ou, '27=les, '14=ce, plus a few left unglossed by Tomokiyo himself ('97, '94,
'51, '36, '15, '13, '7, '84). Some values agree with the fr.3633 list above (16=de, 19=et, 20=est, 40=ou,
42=pour, 46=que), others do not appear there at all -- this may be a partially overlapping but not identical
table, or the fr.3633 list may itself be incomplete. **Not built into a second key TSV this session** (out of
this job's scope); a future decode pass against the rest of f.81r/f.81v will hit these dotted codes constantly
(they cover very common short words) and should not assume every unmatched digit group is a transcription
error before checking whether it is dotted in the original image.

## Requests (network log)

cryptiana.web.fc2.com: 2 requests this unit (`BnFfr4715f81.png`, `phelippes8.png`), 2 s apart, descriptive
User-Agent (out of this job's 5-request allowance across both units; unit A used 0). gallica.bnf.fr: 3 requests
(canvas f177 at 600px for the eye check, then f177 and f178 at 1000px for the manifest), through
`tools/gallica_folio.py` for the label lookup plus direct IIIF fetches, 1.5 s apart. No archive.org requests
this unit (not needed -- no printed-volume page to confirm, unlike unit A). No credentials, no AskUserQuestion.

## What remains before any class (rule 10) or any deep-work brief

- `tools/intake_gate_check.py fr4715-montholon-1589` (run before any deep-work brief, per the intake gate rule).
- Transcribe f.81r's cipher passage from the image (two blind passes), decode with
  `keys/key_vieuville_nevers.tsv`, calibrated against `known_plaintext.txt`/`aligned_dump.txt`'s printed
  opening -- this is the aligned-letters advantage the fr.3251 lane's own targets lacked (per this job's own
  brief). The dotted word-code table above is the likely main source of undecoded tokens; a future worker
  should first check whether an unmatched group is dotted in the image before treating it as an error.
  A 20-shuffled-key control (rule 3) before any claimed reading; reading to a verifier.
- f.81v and beyond: unexamined this session; the letter's full extent (how many folios) is not established.
- A full check-solved pass proper (`.claude/briefs/check-solved.md`) has not been run; this job only confirmed
  the found-solved gate (no) and the BnF catalogue's own "non dechiffre" flag, per KEY-ADJACENT.tsv row 19's
  digitised cell and this NOTES.md's own citation above.
- Once a reading exists: `tools/print_check.py` on the decoded phrases (rule 10).

## MONT-4715 (27 Sept 2026)

Per `.claude/briefs/runs/2026-09-27-parent-ytbiz-mont-4715.md`. Transcribed f.81r's cipher passage (two blind
passes), decoded with `keys/key_vieuville_nevers.tsv`, calibrated against the printed opening. **Calibration
FAILS the pre-registered gate.** Status stays `open`.

**U1 crops.** `python3 tools/iiif_lines.py --ark btv1b52509819x --canvas 177 --region 326,1285,3630,2243 --out
ciphers/fr4715-montholon-1589/images --prefix f81r --debug` (native region found by scaling the 1000px eye-check
image's text-block box by the canvas's native/1000px ratio, 4.079x, from the cached IIIF manifest
`sources/gallica-manifests/btv1b52509819x.json`, canvas 177 = 4079x5720 native). 36 lines detected, debug overlay
checked by eye (centres on every line, band edges in whitespace) -- good line detection.

**Crop legibility failure and fix.** The first attempt (`--max-width 2400`, 2 segments/line, 72 crops, prefix
`f81r_`) was given to two independent blind Sonnet subagents (one leaf, one call each, per Usage 6). **Both
independently declined to produce a transcription**, citing illegible digit shapes at that crop width -- not
primed by each other (launched in parallel, no shared context). This is the same failure shape as NEV-C3's first
gloss-reading attempt (ceppo-nevers-fr3251-1570s NOTES.md: "all illegible... 0 confident letters"), fixed there by
narrower, more zoomed crops. Diagnosed by testing crop widths directly: a 2400px-native crop upscaled 3x (7200px)
displayed no better (the display/vision pipeline downscales the long edge back down to roughly 2000px regardless of
source size, so a wide crop's real information is lost before the model sees it); a 700-900px-native crop upscaled
3x displayed near 1:1 and was clearly legible by direct inspection. Re-cut at `--max-width 900` (5 segments/line,
180 crops, prefix `f81rz_`, from the already-cached region source, no new network fetch), each segment upscaled 3x
LANCZOS (prefix `f81rzoom_`, superseding `f81rz_`), then the up-to-5 segments per folio line composited into one
vertically-stacked "sheet" per line (`f81rsheet_Lnn.jpg`, 35 files, one per folio line L02-L36) so a subagent reads
35 files instead of 175 -- stacking vertically does not reintroduce the width problem (each row keeps its own
900-native/2700-upscaled width, same ~1.35x display factor as the single-segment test). The superseded wide
(`f81r_L*.jpg`) and intermediate non-upscaled narrow (`f81rz_L*.jpg`) crops were deleted, not kept.
`images/regen_f81r_crops.sh` reproduces the final `f81rzoom_L*.jpg` set from the cached source (rule 7). Two fresh
independent blind passes were then launched on the 35 sheet images; running as of this checkpoint.

Images folder: 25 MB (under the 30 MB limit) after the wide/intermediate crops were deleted.

Network log this job: 0 new gallica.bnf.fr requests for the crop fix (region cut from the already-cached full-page
source fetched by INTAKE-4715); the U1 region fetch itself was 1 request (cached locally after).

**U2/U3 blind passes.** Two independent Sonnet subagents (`witness/pass_a.tsv`, `witness/pass_b.tsv`), each given
only the 35 `f81rsheet_Lnn.jpg` sheets and the key's sign inventory (letters only, not meanings), transcribing
L02-L36 (L02's tail and L36's head/tail carry the folio's own clear-French salutation/closing, marked
`[PLAIN:word]`; the dense middle is cipher). Both passes succeeded this time (v. the v1 failure above) but both
flagged the hand as genuinely hard even at 3x zoom: recurring 0/6, 1/7, 2/3, 3/5, 3/8, 9/g digit-shape confusions,
named independently by both passes before they saw each other's output. Pass A: 2376 sign rows. Pass B: 2217 sign
rows.

**U4 reconciliation.** `python3 tools/reconcile_passes.py witness/pass_a.tsv witness/pass_b.tsv --out-dir
witness --crops images` (NW alignment). **Pass agreement: 1487/2524 = 58.9%** pooled (per-line range roughly
41-80%, `witness/agreement.tsv`) -- moderate, consistent with both passes' own stated difficulty, not a tool or
convention error. `witness/ciphertext_draft.tsv` (2524 rows) is the agreed/majority sign per position, graded M
throughout (reconcile_passes.py's own rule: agreed-but-flagged-by-either-pass -> M; almost every row was M/L
confidence in at least one pass, so almost nothing reached H here) -- **not independently reconciled against the
source crops by a human/model arbiter this job**, budget was spent on the crop-legibility fix instead; this is
the auto-reconciled (majority/first-pass) draft, named as the next step's target below.
`witness/disagreements.tsv` (1037 rows) is where the two passes differ.

**Sign -> key_row conversion.** `scripts/signs_to_witness.py` (target-local, not promoted to tools/ this job --
see its own docstring) converts `ciphertext_draft.tsv`'s raw digit strings to `decode_witness.py`'s `key_row`
format by an **exact match** against `keys/key_vieuville_nevers.tsv`'s own sign column, not that tool's built-in
`nNN` substring lookup: the key's row 22 (bold "1", -> r) is a substring of row 3's sign "10" (-> b), which sits
earlier in the file, so decode_witness.py's own `_numeral_lookup` would silently resolve a bare "1" to "b" instead
of "r" -- flagging this here as a landmine in `tools/decode_witness.py` for whoever next uses its `nNN` convention
with a key that has any 1-digit sign sharing digits with an earlier 2-digit one. A leading zero (very common in
both passes' output, e.g. "05") is stripped before lookup when the stripped form matches a key sign (the key's
row 1, sign "5", has no "05" row -- almost certainly the passes' own formatting habit, not a real second digit).
1053 raw signs were unmatched before this normalisation, 716 after (`witness/witness_signs.tsv`, 2525 rows); the
remaining 716 are mostly 3-5 digit runs (segmentation disagreements between the passes on where one sign ends and
the next begins in the dense hand) or genuinely off-inventory pairs, left as `key_row=?` (graded I in the decode,
never guessed).

**U5 calibration.** `plain` = `known_plaintext.txt`'s printed opening, chunked into 15 rows by its own printed line
breaks (`witness/witness_opening_plain.tsv`). `python3 tools/decode_witness.py --key
keys/key_vieuville_nevers.tsv --signs witness/witness_signs.tsv --plain witness/witness_opening_plain.tsv
--shuffles 20 --seed 1 --key-rows-out witness/key_rows_calibration.tsv`:

```
full passage: real key 0.4636 (541/1167 aligned letters); 20 shuffled keys mean 0.4227 sd 0.0334 min 0.3470 max 0.4884; z 1.22; rank 2 of 21
```

Ran against the FULL `witness_signs.tsv` (all of L02-L36, not line-sliced): `decode_witness.py`'s alignment is
global over the whole passage, so signs beyond the true opening's own extent (the opening runs roughly L02-L17,
by cumulative sign count against `aligned_dump.txt`'s own 959 tokens -- see below) simply have nothing left to
match once the clerk plaintext (1167 letters) is consumed, and cannot inflate the real-key score; a `--sample-lines`
attempt to slice cleanly by folio line failed (`plain`'s own row ids, p1-p15, don't correspond to signs' Lnn ids --
tool's own line-id-matching design, not built for this shape of witness; not fixed this job, worked around by
running unsliced instead).

**Gate (pre-registered, this job's brief): z >= 2 AND >= 30 aligned letters.** n=1167 aligned letters -- **well
powered**, not the NEV lane's "calibration underpowered" shape. **z=1.22 does not clear the gate.** The real key
still beats the shuffled mean (0.4636 vs 0.4227) and ranks 2nd of 21, so there is a real, non-trivial signal in
the right direction, consistent with the key itself being correct and the shortfall being transcription noise
(58.9% raw pass agreement) rather than a wrong key -- but this is short of the pre-registered bar, so **not** a
pass, and this reading is not sent to a verifier.

**Diagnostic decode, lines L18-L36 (beyond the calibration range).** `python3 scripts/decode_rest.py
witness/witness_signs.tsv keys/key_vieuville_nevers.tsv L18 L36` (target-local script; grades H = letter
homophone from the key table, M = dotted word-code resolved from `aligned_dump.txt`'s own gloss or, failing that,
nevers.htm's fr.3633 sibling-letter list -- named M per rule 4, not guessed -- I = illegible/unmatched/unresolved
dotted code). Written to `reading.txt`. **H=1039 M=12 I=419, total=1470, 28.5% unread.** The readable majority
does not parse as French words (`reading.txt`) -- consistent with the failed calibration on the same
transcription, not a contradiction of it. **This is not a reading and is not offered to a verifier.** Lines
L02-L17 (the calibration range) are not separately re-decoded: Tomokiyo's own printed opening
(`known_plaintext.txt` / `aligned_dump.txt`, grade C) already covers that span at a higher grade than anything
this job's transcription could produce.

**print_check.py:** not run. Rule 7's "once a reading exists" does not apply -- no reading exists this job.

**Named next step, in order of expected value:** (1) a targeted reconciliation pass against the source crops on
`witness/disagreements.tsv`'s 1037 rows (not a third independent blind full-page transcription -- the two passes
already agree on the shape of the problem, recurring digit-shape confusion, not a segmentation or convention
gap) -- Usage 6's own "reconciliation is a distinct priced step" applies; this job's budget went to the
crop-legibility fix instead of a human/model arbiter pass. Raising real pass accuracy is the most direct lever on
a calibration that is well-powered (1167 letters) but short on precision (58.9% raw agreement), not scarce
material -- f.81v or a second witness letter would not fix a transcription-accuracy shortfall on f.81r itself. (2)
Once reconciled, re-run `tools/decode_witness.py` unchanged; if the gate then passes, decode the rest of f.81r
(L18-L36) properly and hand to a verifier. (3) `tools/decode_witness.py`'s `nNN` numeral lookup should get an
exact-match fix or a documented caveat (flagged above) before another target relies on that convention with a
key carrying 1-digit signs.

Requests this job: 0 new gallica.bnf.fr fetches (crops cut from the already-cached region source). Subagents: 4
(two blind-pass attempts on the too-wide crops, declined; two blind passes on the corrected crops, both
completed). No credentials, no AskUserQuestion, no novelty wording, owner not named.

## MONT-4715B (27 Sept 2026)

Per `.claude/briefs/runs/2026-09-27-parent-ytbiz-mont-4715b.md`. Targeted reconciliation of MONT-4715's
`witness/disagreements.tsv` (1,037 rows) against the source crops, then the calibration re-run unchanged.

**U0, `tools/decode_witness.py` fix.** MONT-4715 flagged `_numeral_lookup`'s `nNN` convention: it matched
the key's `sign` column by substring in file order (`if digits in r["sign"]`), so a 1-digit sign that is a
substring of an earlier 2-digit sign resolved to the wrong row (this key's row 22, sign `1` -> r, sits after
row 3, sign `10` -> b; `n1` would silently resolve to `b`). Fixed to an exact match on the stripped sign cell
(`r["sign"].strip() == digits`), with the docstring corrected to match. Added a regression case to
`tools/tests/test_decode_witness.py` reproducing this key's own row-22/row-3 shape (`n1` -> r, not b) and
changed the pre-existing `n85` fixture from a sign of `digits85` (which only worked because the old code did
a substring match) to a real sign of `85`, so that test now exercises the corrected exact-match behaviour
instead of accidentally depending on the bug. `python3 tools/tests/test_decode_witness.py`: ALL PASS (22
checks). `scripts/signs_to_witness.py` was **not** folded into `tools/decode_witness.py`: the script does
more than the nNN numeral lookup alone (the glyph map for the two special non-numeric signs, the dotted-code
marker, `[PLAIN:...]` pass-through, the leading-zero fallback, and the reconcile-output-to-signs-file column
mapping) -- not a one-function change, so it stays a target-local script per the brief's own fallback
instruction; it already did its own exact-match lookup independently of this tool, so it was unaffected by
either the bug or the fix. `witness_signs.tsv` (v1, MONT-4715's own signs file) is built entirely through
`scripts/signs_to_witness.py`, not through `decode_witness.py`'s `nNN` convention, so this fix does not
change MONT-4715's own numbers by itself -- confirmed by running the new `merge_settled_signs.py` (below)
with an empty override file and diffing its `key_row` column byte-for-byte against `witness_signs.tsv`: zero
differences.

**U1-U3 reconciliation.** `witness/disagreements.tsv`'s 1,037 rows were split into three contiguous line
ranges by row count (not line count, so the three calls are balanced): L02-L14 (350 rows), L15-L25 (359
rows), L26-L36 (328 rows). Each of three parallel Sonnet subagents (general-purpose) was given only its
range's `f81rzoom_L*_s*.jpg` crops (the zoomed segments MONT-4715 found legible, never the wide or full-leaf
crops), the disputed (line, col, pass-A reading, pass-B reading, flagged) rows for its range, and a shared
reference document (key sign inventory, the dotted-word-code convention, how "col" numbers map to the five
crop segments per line, and the required output format) -- never told which pass to prefer. Each returned
one row per input row: a chosen sign (or `?` if genuinely undecidable from the image) and a one-word reason
(`digit shape` / `dot present` / `segmentation` / `undecidable`).

Results, verified row-for-row against each range's own disagreement list before merging (no gaps, no
duplicates, no extra rows):

| range | rows | settled | left `?` |
|---|---|---|---|
| L02-L14 | 350 | 280 | 70 |
| L15-L25 | 359 | 292 | 67 |
| L26-L36 | 328 | 287 | 41 |
| **total** | **1037** | **859** | **178** |

All three workers flagged the same shape of hard case independently (same-length homophone-pair digit
disputes with no clean pixel tiebreak, e.g. 63/65, 23/24, 70/20) and left those `?` rather than guess, the
same caution the original two blind passes showed.

**U4 merge.** `scripts/merge_settled_signs.py` (new, target-local, mirrors `signs_to_witness.py`'s exact-match
sign lookup and glyph map) takes `witness/ciphertext_draft.tsv` (the position of record for every position
the two original passes already agreed on) plus the three workers' combined output
(`witness/settled_disagreements.tsv`) and the key, and writes `witness/witness_signs_v2.tsv` (v1 kept).
Sanity check: re-run with an empty override file reproduces `witness_signs.tsv`'s `key_row` column exactly
(0 differences over 2524 rows) -- confirms the reimplementation, not just the new inputs, is correct.

Of the 859 newly-settled rows: 533 resolved to a digit string matching one of this key's 35 letter-homophone
signs, 20 resolved to a confirmed dotted word-code, and 306 are a definite crop reading that still does not
match any row in this (letter-only) key -- expected, since bnf4715.htm's own printed alignment shows roughly a
third of this letter's tokens are the undocumented word-code layer, and a definite reading of a word-code with
no visible dot, or of a multi-digit group that is itself a real sign outside the 35-row letter table, is not an
error to chase further here. `witness_signs_v2.tsv`'s own `key_row='?'` count is 727 of 2524 (306 settled but
unmatched, 178 settled `?` (undecidable), 221 unresolved from positions the two original passes already
agreed on, 20 dotted, 2 illegible), down from v1's 760.

**New effective pass agreement.** Counting a position as settled once either the original two passes agreed
on it or one of U1-U3's reconcilers gave a definite (non-`?`) reading: **2,346/2,524 = 92.9%**, up from the
original two-pass raw agreement of 1,487/2,524 = 58.9%. The remaining 178 positions (7.1%) are genuinely
undecidable from the available crops per all three reconcilers, not unattempted.

**Calibration re-run, unchanged from MONT-4715 (`tools/decode_witness.py --key keys/key_vieuville_nevers.tsv
--signs witness/witness_signs_v2.tsv --plain witness/witness_opening_plain.tsv --shuffles 20 --seed 1
--key-rows-out witness/key_rows_calibration_v2.tsv`):**

```
full passage: real key 0.4773 (557/1167 aligned letters); 20 shuffled keys mean 0.4240 sd 0.0337 min 0.3505 max 0.4841; z 1.58; rank 2 of 21
```

| | agreement (aligned) | shuffled mean | sd | z | n |
|---|---|---|---|---|---|
| MONT-4715 (v1) | 0.4636 (541/1167) | 0.4227 | 0.0334 | 1.22 | 1167 |
| MONT-4715B (v2) | 0.4773 (557/1167) | 0.4240 | 0.0337 | 1.58 | 1167 |

**Pre-registered gate (z >= 2, n >= 30): still not met.** n=1167 remains well powered. Real agreement rose
(0.4636 -> 0.4773) and z improved (1.22 -> 1.58) with the pass-agreement gain (58.9% -> 92.9%), moving in the
expected direction, but the targeted crop reconciliation -- a genuinely different instrument from a third
blind pass, per CLAUDE.md rule 3's repeated-attempt paragraph -- still does not clear the bar. This is **not**
a negative on the key (the real key still beats the shuffled mean and ranks 2nd of 21, the same as before):
**key_vieuville_nevers untestable-by-this-transcription on f.81r at 92.9 pct pass agreement.**

No decode of L18-L36 or `print_check.py` this job -- the brief's "if it fails again" branch applies, not the
"if it passes" branch. Status stays `open`. No reading offered to a verifier.

**Named next step:** not a third pass at f.81r (the transcription is now settled to 92.9% and the shortfall
persists) -- either (a) f.81v (unexamined this session, per INTAKE-4715's own note that the letter's full
extent beyond f.81r is not established), which would add fresh aligned material without depending on
resolving the same 178 genuinely ambiguous positions on f.81r; or (b) a second witness letter in the same
Vieuville-Nevers cipher, if one exists -- nevers.htm names the cipher for "another article" but this job did
not check whether a second letter using this same key is cited there (the fr.3633 f.22 dotted-code witness
named in MONT-4715's own caveat section is a *different* cipher's sibling letter for the word-code layer, not
a second Vieuville-Nevers witness -- flagged here so a future worker does not conflate the two). Both are
material steps, not a further tuning of the same transcription-accuracy knob.

Requests this job: 0 new network fetches (all three subagents worked from the already-cached crop images on
disk; no gallica.bnf.fr or cryptiana.web.fc2.com requests). Subagents: 3 (the U1-U3 reconciliation calls, run
in parallel). No credentials, no AskUserQuestion, no novelty wording, owner not named. Images folder
unchanged at 25 MB (no new images fetched or cut).

## Pool (27 Sept 2026, parent 7m)

f.81v (canvas 178) is a blank leaf by direct inspection (parent 7m, 12:26 UTC): the letter is one leaf. CS-4715-POOL's check-solved pass on the twenty-two fr.4715 letters nevers.htm places in the Vieuville-Nevers cipher is in `POOL.md` (11 carry a period decipherment on the leaf per the BnF's own depouillement, 9 are open or partial, about 13,000 signs with this folder's key of record). The first pool job is MONT-KEY6 (no.6 f.24, interlinear, key recovery through tools/interlinear_align.py).

## MONT-KEY6 (27 Sept 2026)

Per `.claude/briefs/runs/2026-09-27-parent-ytbiz-mont-key6.md`: no.6 f.24r (Vieuville to the Duke of
Nevers, Sy, 3 July 1589; BnF's own depouillement "Lettre en chiffre, avec dechiffrement") is an
**interlinear** leaf -- the clerk wrote the plain-French decipherment directly above each line of cipher
digit-groups. Goal: transcribe the (group, gloss) pairs, run `tools/interlinear_align.py` to validate
`keys/key_vieuville_nevers.tsv` at grade C and recover the dotted word-code table no.58's own key lacks.
**Result: neither goal was reached this session.** The blocker is transcription accuracy on this leaf's
crop scheme, not the key or the alignment tool. Status stays `open`; nothing here is a reading, a key
validation, or a novelty claim (rule 10).

**Gloss present: yes.** `python3 tools/gallica_folio.py btv1b52509819x --folio 24` -> canvas f61 = label
'24r' (4028x6143 native). Fetched a 1000px eye-check (`images/f24/f24r_1000.jpg`, 1 gallica.bnf.fr
request after one retry on a connection reset -- the documented intermittent Gallica behaviour, single
retry per the good-citizen rule, then HTTP 200): dense interlinear hand, a line of French gloss above
every line of digit-groups, confirming the BnF's "avec dechiffrement" note directly.

**U1 crops -- tuning failure caught before it reached a subagent, then a second failure not caught
until the passes reported back.** First attempt: `--lines-per-crop 2` at the tool's own default
distance/prominence (34/477.6) to pair one gloss row with one cipher row per crop, matching the brief's
instruction to tune until the debug overlay shows one band per pair. The debug overlay *looked* right at
three spot-checks (top, middle, bottom of the page) -- but opening the raw single-width segment for band
1 before stacking showed only the gloss row "noster heur est trop", no cipher digits at all: this leaf's
ink-density profile does not alternate cleanly gloss-peak/cipher-peak the way a single-layer cipher line
does (ascenders/loops inside one row produce sub-peaks 40-60px apart, indistinguishable by height alone
from the true, highly irregular 40-170px gap between real rows), so pairing "2 consecutive raw peaks"
silently paired two sub-peaks of the *same* row for band 1. Fixed by widening to `--lines-per-crop 12`
(7 bands, generous margin, no attempt to assert an exact pair boundary the ink profile cannot reliably
give) and letting the transcribing pass self-segment lines from what it actually sees -- exactly the
right instinct (this is the second failure): the brief's own "~5-6 pairs per band" sizing estimate was
wrong by roughly 5x. Both blind passes independently report 25-35 real manuscript lines per band (except
the shorter final band), for roughly 101-215 lines total depending on the pass's own segmentation -- not
the ~37-45 a direct eyeball count of the 1000px image suggests either, so even the passes' own line counts
disagree with each other and with a plain look at the page. `images/f24/regen_f24_crops.sh` documents both
failures and the fix in its own header (rule 7); `f24t_lines_debug.jpg` and the native region source are
kept, the 35 upscaled crops (`f24zoom_L*_s*.jpg`, legibility confirmed by direct inspection before the
passes were launched) were deleted after use per the brief's own folder-size instruction (`du -sh` before
push: 4.4 MB, was 28 MB with the crops in place).

**U2 two independent blind passes** (`witness_f24/pass_a.tsv`, `pass_b.tsv`; one Sonnet subagent call
each, given all 35 crops and the letter-only sign inventory, no key values, no shared context): both
completed, both self-reported low confidence **before either was scored against the other** --
pass A: 2262 groups, 69 M / 2193 L, 0 H; pass B: 900 groups, 119 M / 781 L, 0 H. Both independently named
the same root cause: a small, dense, ambiguous cursive hand (0 vs. o, digit-shape confusions), a faint
gloss hard to align to individual groups without pixel coordinates, and uncertainty distinguishing the
dot/apostrophe word-code mark from ordinary ink. Pass A read far more (and shorter) tokens than pass B
(2262 vs. 900) -- consistent with pass B's own admission that it likely merged several true groups into
longer runs in the harder lower two-thirds of the page, rather than a real segmentation convention gap.

**U3 reconciliation -- adapted, not run as briefed.** The two passes' own "line" numbering diverges so far
(101 vs. 215) that a per-manuscript-line reconciliation (`reconcile_passes.py`'s normal long-format
alignment, matching rows by shared line id) would compare unrelated spans of text, not a real
disagreement. Adapted: both passes flattened into one continuous sequence (line=1, positions 1..N) and
aligned as a single long sequence (`reconcile_passes.py --method difflib`, one call, script only):

```
lines 1  signs A 2262  B 900  agree 349/2262 = 15.4%  (difflib)
gloss agreement (aligned columns where every pass wrote a gloss): 14/66 = 21.2%
```

Far below MONT-4715's own f.81r figure (58.9% raw, same two-blind-pass method, a *plain* cipher line, no
interlinear gloss to align) -- this leaf is harder, and both passes said so themselves before either
number existed. Given the scale of disagreement (2162 of 2262 positions differ or gap), a costed
crop-arbitration subagent call (the brief's own U3 plan) was **not** run: with the passes' own line counts
already off by more than 2x from each other, most of that 2162 would be an artifact of segmentation
drift, not real per-position corrections a crop-arbiter could fix one row at a time -- spending the
~USD 3 there would not have produced a trustworthy settled draft. Logged here as the conservative call
this session made without asking (no AskUserQuestion; a worker call, not a stopping point).

Agreement is not uniform: chunked in 200-row windows over the flattened sequence, the opening reaches
43.0% (86/200) before dropping to a 0-27% range for the rest of the leaf (`witness_f24/ciphertext_draft.tsv`,
column `why`). The two passes read the *same* opening words in the *same* order before their differing
segmentation compounds into drift further down the page.

**U4 key gate -- two runs, both reported, neither clears a meaningful bar.** `scripts/build_f24_pairs.py`
turns the reconciled draft into `tools/interlinear_align.py`'s PAIRS.tsv format: a dotted group `'47` is
shifted to `147` (its own docstring explains the +100/`--floor 100` encoding, chosen after a synthetic
round-trip test caught an earlier +1000/`--floor 1000` attempt silently misclassifying every dotted code
as kind `doubtful` instead of a word-code -- `classify_token()` only parses a 1-3 digit numeral as kind
`num`). `scripts/f24_key_gate.py` runs the alignment **with no `--prior`** (blind, so its own converged
meaning for each already-known letter-homophone sign can be checked against `keys/key_vieuville_nevers.tsv`
as an independent known-answer gate, the AX2-BRO4 shape -- not circular, since the known values are never
fed in) and controls with 20 gloss-shuffled reruns (same cipher, gloss reassigned to the wrong line,
verified no shuffle keeps any line's own gloss):

```
Opening window (first 200 flattened positions, the best-agreeing prefix, 43.0% raw agreement):
  REAL: 3/20 = 0.150 known letter-codes recovered blind
  SHUFFLED (20 seeds): mean 0.071, range 0.000-0.200
  -- real (0.150) falls WITHIN the shuffled range (one shuffle reached 0.200) -- no separation from noise.

Full leaf (all 2511 flattened positions, pseudo-lines of 20 -- real manuscript line breaks are not
trusted given U3's finding, so this is an approximation, stated as such):
  REAL: 4/28 = 0.143 known letter-codes recovered blind
  SHUFFLED (20 seeds): mean 0.048, range 0.000-0.107
  -- real (0.143) exceeds the shuffled range's own maximum (0.107): a genuine, if narrow, separation on
     this one aggregate number.
```

The control satisfies rule 3 (it can and does fail differently: 0.000-0.200 and 0.000-0.107 are real
spreads, not a tied non-test). But the aggregate full-leaf "pass" does not survive contact with the
per-code detail: of the 28 known letter-codes checked, only 4 converged to their correct value (`sign '24'
truth=e recovered=e OK`, `'25' truth=a recovered=a OK`, `'75' truth=d recovered=d OK`, `'59' truth=o
recovered=o OK` -- all four single-letter monosyllabic-context codes, plausibly recoverable by chance from
short common words); the other 24 missed, several by a lot (`'40' truth=h recovered=a`, `'90' truth=y
recovered=i`). And the actual dotted word-codes the alignment produced are not French: `'75` ->
"ditrsalvnajugn", `'95` -> "confoor", `'650` -> "dissonprons" -- alignment noise from a transcription this
session could not read reliably, not word codes. The decisive cross-check: **of the 7 dotted codes
recovered here that also appear in no.58's own printed `aligned_dump.txt` gloss (`'25`, `'28`, `'46`,
`'47`, `'50`, `'64`, `'75` -- NOTES.md's "An important caveat" section), 0 agree and 7 conflict**
(`'47`: f.24 "lendroit" vs. no.58 dump "qui"; `'64`: f.24 "gamb" vs. no.58 dump "catholique"; full list in
`keys/key_f24_recovered.tsv`'s own header). Per rule 4, a conflict between an attempted S-grade recovery
and an established C/H-grade printed witness is resolved toward the printed witness, not averaged --
this is not evidence of two genuinely different word-code tables (which per the fr.3633 sibling-letter
comparison would show *some* agreement, not 0 of 7), it is evidence this attempt's recovery is wrong.

**Verdict: the letter key is NOT validated at grade C this session, and no dotted word-code table is
recovered.** `keys/key_f24_recovered.tsv` (renamed `witness_f24/key_f24_recovered_UNVALIDATED.tsv`, moved
out of `keys/` and added to `tools/key_design.py`'s `NOT_A_KEY` skip list with a one-line reason so
`KEY-DESIGN.tsv`/`KEY-OFFICES.tsv` never present it as a usable key alongside the real
`key_vieuville_nevers.tsv`) is kept on disk, clearly marked in its own header as unvalidated, for the
record only -- not merged, not registered as a recovered key, not cited as a result. This is a
transcription-accuracy negative with a matched control (rule 3), not a design-family negative on the key
or the tool: `tools/interlinear_align.py` itself was confirmed correct on a synthetic round-trip before
use, and the known-letter gate does show a genuine (if narrow and per-code-fragile) signal above noise on
the aggregate full-leaf run -- the transcription this session could produce from these crops is simply
not accurate enough to turn that signal into a trustworthy per-code table. Consistent with MONT-4715's own
finding on f.81r (a *plainer*, single-layer cipher line, still only 58.9% raw pass agreement): this whole
pool's likely bottleneck is transcription accuracy against this hand, now confirmed worse on an
interlinear leaf than on a plain one.

**U5 not run.** The brief gated U5 (merge into `key_vieuville_nevers_plus.tsv`, re-run the no.58
calibration) on U4 producing a usable table; it did not. Merging a 0/7-conflicting, mostly-non-French
table into the key used for no.58's own calibration would risk manufacturing a spurious calibration
change, not measuring a real one -- the conservative call (no AskUserQuestion) is to skip it and say so.

**Named next step, in order of expected value:** this leaf needs a **materially different transcription
approach**, not a further pass at the same crop scheme (CLAUDE.md's "second attempt at an unchanged
approach" principle) -- specifically, per-real-manuscript-line crops with a correctly verified
gloss/cipher pairing (the tuning failure above means neither an ink-profile pairing nor a wide multi-line
band reliably tracks real line boundaries on this hand), likely priced closer to MONT-4715's own per-line
`f81rsheet_Lnn.jpg` approach (35 single-pair sheets, not 7 multi-line bands) but doubled in unit count for
the extra gloss row -- a materially larger crop/pass budget than this job's cap, named here rather than
attempted with what was left. Until then: no.6 f.24 is `open`, not `partial` (rule 5 -- no reproducible
margin over its own control was found; the full-leaf gate's narrow separation does not survive the
per-code and no.58 cross-checks above), and the pool's other open/partial rows (no.21, 27, 28, 35, 37, 39,
44, 60) should not be attempted with this same wide-band crop scheme without first fixing the line-pairing
problem documented here.

Requests this job: gallica.bnf.fr 2 (the 1000px eye-check after one retry on a connection reset, then the
one native-region fetch reused by every crop cut -- `images/f24/regen_f24_crops.sh` recuts from the cached
file with 0 further requests). Subagents: 2 (the two blind passes, run in parallel, one leaf each per
Usage 6 -- no arbitration subagent, see U3 above). No credentials, no AskUserQuestion, no novelty/solved/
first/unpublished wording. `pip install numpy pillow scipy` (local package install, not a network host)
to make `tools/iiif_lines.py` importable.

## MONT-4715C (27 Sept 2026)

Per `.claude/briefs/runs/2026-09-27-parent-ytbiz-mont-4715c.md`, run as its restart MONT-4715C2 (the first session
stopped on an API error before pushing anything). Script-only: no fetch, no subagent, no new transcription pass.
Everything below regenerates with `scripts/mont4715c.py` (u1, u2prep, classes, u3cover) plus the
`tools/decode_witness.py` and `scripts/decode_rest.py` commands quoted.

**U0, f.81v.** Viewed `images/f81v_canvas178.jpg` directly: blank -- no ink, only the facing leaf's bleed-through at
the right edge and two seal impressions. Confirms the "Pool" section's note (parent 7m, 12:26 UTC); the letter is
one leaf. One-line note added to `images/manifest.json`'s f81v entry. MONT-4715B's next step (a) is void.

**U1, transcription accuracy without the key.** Global LCS over group strings between our v2 signs
(`witness/witness_signs_v2.tsv`, L02-L17, 1,054 groups: key-row groups rendered as their key sign, dotted as
`'NN`, unmatched-definite as read, undecidable/illegible as a token that never matches) and Tomokiyo's dump
(`witness/aligned_dump_codes.txt`, 959 groups, grade H). Control: the same LCS with our group order shuffled within
each folio line, 20 shuffles (seed 1) -- an order shuffle changes an LCS, so this control can fail differently from
the target.

| L02-L17 | groups matched (real) | order-shuffled mean (sd) | z |
|---|---|---|---|
| all groups, as drawn | 380/959 = 0.396 | 0.290 (0.004) | 27.7 |
| bare (letter) groups | 376/816 = 0.461 | 0.338 (0.005) | 27.5 |
| dotted groups, dot required | 3/129 = 0.023 | 0.015 (0.007) | 1.3 |
| symbol/other | 1/14 = 0.071 | 0.014 (0.029) | 1.9 |
| all groups, dot-blind (apostrophe stripped both sides) | 448/959 = 0.467 | 0.308 (0.004) | 37.2 |
| dotted groups, dot-blind | 75/129 = 0.581 | 0.243 (0.035) | 9.7 |

(Over L02-L36 the as-drawn figure is 457/959 = 0.477 vs shuffled 0.404, z 21.1; the gain over L02-L17 is near what
chance adds with 1,470 more groups, consistent with the dump ending about L17.) The order is real -- z 28 -- but
**only about 46 pct of Tomokiyo's letter groups are recovered in order by our transcription**, against MONT-4715B's
92.9 pct "settled". Settled means the two passes and a reconciler agreed on a reading, not that the reading is what
Tomokiyo printed. Dots are almost never seen by our passes (7 dotted signs in L02-L17 vs 129 in the dump; 13.5 pct
of the dump's groups are dotted, not the "roughly a third" of the older caveat), but the digits under the dot are
read about as well as letter groups (0.58 dot-blind). Caveat: part of the 54 pct loss is segmentation (our
`123`/`773`/`231` runs vs the dump's `1 23`, `73 1`...), which a group-level LCS counts as a miss; this number is a
floor on accuracy, not an error rate. Tomokiyo's dump is itself a transcription; it is treated as the reference
here, not as the manuscript.

Per-class breakdown of our v2 signs over L02-L17 (1,054): key-row letter 753 (71.4 pct), unmatched definite 209
(19.8), undecidable 83 (7.9), dotted 7 (0.7), illegible 2 (0.2). The dump over the same passage (959): bare in key
818 (85.3), bare not in key 1 (0.1), dotted 129 (13.5), symbol/other 11 (1.1). The gap sits in our 209
unmatched-definite readings (mostly segmentation runs and undotted word-codes such as 42, 46, 27) -- the dump has
essentially none.

**U2, the ceiling of decode_witness's statistic.** `python3 scripts/mont4715c.py u2prep` writes
`witness/tomokiyo_signs_ceiling.tsv` (the dump's 959 groups, 818 resolved to a key row by exact sign match, dotted
and symbol groups '?'). Then `python3 tools/decode_witness.py --key keys/key_vieuville_nevers.tsv --signs <file>
--plain witness/witness_opening_plain.tsv --shuffles 20 --seed 1`:

| signs file | real | shuffled mean (sd) | z | rank |
|---|---|---|---|---|
| ceiling: Tomokiyo's groups through this key | 0.7009 (818/1167) | 0.3030 (0.0239) | 16.66 | 1 of 21 |
| MONT-4715B v2, full L02-L36 (as registered) | 0.4773 (557/1167) | 0.4240 (0.0337) | 1.58 | 2 of 21 |
| v2, L02-L17 only (length-matched to the opening) | 0.3805 (444/1167) | 0.2860 (0.0210) | 4.50 | 1 of 21 |

Boundary sensitivity of the length-matched run (same command, v2 sliced to L02-Lnn): L15 z 4.67, L16 4.49, L17
4.50, L18 4.27, L19 3.85, L20 3.49, L22 3.14 -- rank 1 of 21 throughout, z falling steadily as signs past the
opening are added. The ceiling is 818/818: every key-resolvable group of Tomokiyo's dump lands on its clerk letter,
so the statistic's maximum on this passage is 0.70 (the remaining 0.30 is mostly the dotted word-codes' letters, plus 11 symbol groups), not
0.48-0.50. **Two things follow.** (1) The shortfall to the ceiling is the transcription (U1: 46 pct of letter
groups in order), not a saturated statistic. (2) The z 1.58 was depressed by the scoring window, not only by
transcription error: running decode_witness over all 2,524 signs lets the 1,470 signs of L18-L36 feed the global
LCS, which lifts the shuffled floor from 0.29 to 0.42 while adding little to the real key. Over the lines the
printed opening covers, the v2 transcription scores z 4.5, rank 1 of 21, n 1,167, clearing the pre-registered z >= 2
and n >= 30 numbers. This length-matched window was not the registered run (MONT-4715 fell back to the unsliced run
because `--sample-lines` could not match p/L line ids), so it is reported beside the registered FAIL, not in place
of it: the key reads the letter positions of this passage above chance through our transcription; the registered
full-passage calibration remains z 1.58. It does not say the key is right in every cell, and it licenses no
reading.

**U3, v2 decode of L18-L36.** `python3 scripts/decode_rest.py witness/witness_signs_v2.tsv
keys/key_vieuville_nevers.tsv L18 L36` -> `witness/decode_rest_L18-L36_v2.txt` and `.stats.txt` (v1 files kept).
French word-cover: `python3 scripts/mont4715c.py u3cover <signs> 18 36` -- fraction of H+M letters inside a
maximum non-overlapping cover by words of 3-14 letters occurring at least 3 times in `tools/data/fr16` (3 files,
15,718 words; accents stripped, j->i, v->u), with I tokens breaking runs; control: 20 keys with letter values
permuted among the letter rows (seed 1), dotted-word glosses unchanged.

| | H | M | I | unread | word-cover real | letter-shuffled keys mean (sd), max | z |
|---|---|---|---|---|---|---|---|
| v1 signs (MONT-4715) | 1039 | 12 | 419 | 0.285 | 0.489 (526/1075) | 0.302 (0.091), 0.461 | 2.07 |
| v2 signs (MONT-4715B) | 1044 | 12 | 414 | 0.282 | 0.482 (520/1080) | 0.295 (0.093), 0.448 | 2.00 |
| positive control: Tomokiyo's dump (the opening, not L18-L36) | 818 | 129 as glossed | -- | -- | 0.923 (1065/1154) | 0.574 (0.093), 0.764 | 3.74 |

The v2 decode barely differs from v1 (5 more H) because the reconciliation changed few positions past L17 into key
signs. Word-cover sits about two sd above letter-shuffled keys but below the positive control's shuffled mean; the
cover statistic's floor depends on run length (the dump's unbroken runs give chance 0.57), so the two rows are not
directly comparable. No judge PASS/FAIL (no spec for this target), no reading claim. First three decoded lines,
exactly as `decode_rest.py` prints them (`_` = I, `[...]` = M from this letter's own dump gloss):

```
L18  ua_iceft_anecea_ai_[que]faia_nar_aybdemeu__auecl__a_uealuy[que]_legat_unia_unia___a      H 56  M 2  I 17
L19  habileaa_ucced_raed_r_caathali_m_____euniane_cag_cagnaia_eceluy[qui]fplu                  H 54  M 1  I 13
L20  ea_t_mia__liberae_gaau____n_radm__a__et_faa__ecla___etiua__a_a_[qui]puia_                 H 43  M 1  I 25
```

These are letter strings under the key, not a reading: rule 4 counts, H 153 / M 4 / I 55 over the three lines, no C.

**Verdict.** The chance floor and the ceiling are now both measured: through Tomokiyo's own groups this key scores
0.70 against 0.30 (z 16.7), and our v2 transcription recovers only about 46 pct of his letter groups in order, so
MONT-4715B's 92.9 pct was agreement among our readers, not accuracy. Over the lines the opening covers, the v2
transcription still carries the key above chance (z 4.5, rank 1 of 21, stable z 3.1-4.7 across window ends
L15-L22), and the registered full-passage z 1.58 was depressed mainly by scoring 1,470 signs the opening does not
cover. The key reads the letter positions; the shortfall is the transcription (segmentation and unseen dots), so a
decode of L18-L36 from this transcription stays a letter string with 28 pct unread, not a reading.

**Named next step.** Not a further reconciliation of the same 1,037 disagreements (rule 3's repeated-attempt
paragraph) and not f.81v (blank). Material with a period gloss to train and check the reader: MONT-KEY6's
interlinear no.6 f.24 and the POOL.md letters with a decipherment on the leaf, used to (a) calibrate our
transcription of this hand against a known clear text group by group (the U1 measure, where 46 pct is the number
to beat), and (b) recover the dotted word-code table, whose absence is 30 pct of this passage's letters; only then
a fresh segmentation-aware transcription of f.81r L18-L36. For `tools/decode_witness.py`: its `--sample-lines`
cannot slice a witness whose plain ids differ from its sign ids; a sign-range option (as used here by slicing the
file) would have avoided the misleading unsliced run -- suggestion only, not done here.

Requests this job: 0 network requests; 0 subagents. No credentials, no AskUserQuestion, no novelty wording.
