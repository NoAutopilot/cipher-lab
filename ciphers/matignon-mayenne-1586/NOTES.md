partial
Check-solved (bCSMAT, 26 Sept 2026, superseding bMAT's line below): both 1916 Labande editions of "Correspondance de Montaigne avec le maréchal de Matignon (1582-1588)" on Internet Archive (`correspondancede00montuoft`, `correspondanc00mont`, 32 pp. each) read WHOLE (`_djvu.txt` fetched and grepped cover to cover, not one page range), grepped for 1585, 1586, Mayenne, Matignon and Forget -- neither volume contains a single 1585 or 1586 date anywhere, and neither mentions Mayenne or Forget at all (0 hits every term, both files); no printed correspondence edition of Mayenne, and no edition of the Société de l'Histoire de France's "Lettres de Henri III", found on Internet Archive at all (searched, not present, so not citable as read); Tomokiyo's `sources/cryptiana/web/henryiii.htm` read directly this session (quoted verbatim in the dated section below) still lists every leaf as undeciphered. Full query log, solver-repository HEAD commits and gate-check output in "Check-solved (bCSMAT), 26 Sept 2026" below. Net: open (no printed or prior decipherment found by any of the seven checks run this pass); status stays `partial` per rule 5 (the NEAR.md row, cryptanalytic margin over a matched control, not a check-solved finding).

Check-solved (LANE B5 worker bMAT, 26 Sept 2026, kept for record -- V7-QA5 flagged its IA search below as a single-term query on one edition; superseded by the whole-volume sweep above): Tomokiyo `sources/cryptiana/web/henryiii.htm` (on disk, grepped 26 Sept 2026) still lists every leaf in this target -- Mayenne-Forget's Cipher-1 ff.110, 123-124, 143, 150, 154, 173, 196, 201, and Matignon's Cipher-3 f.276 and fr.15571 f.179 -- as "undeciphered" (f.276 gets a fragmentary paraphrase only: "La Guiolle est en doubte du pu pour les amis de la Roussiere..."). Internet Archive full-text search (be-api fts, 26 Sept 2026) on "Correspondance de Montaigne avec le maréchal de Matignon (1582-1588)" (Labande ed., IA ids `correspondancede00montuoft`/`correspondanc00mont`, the only Matignon correspondence edition on IA whose date range covers 1585-86; the two "Correspondance de Joachim de Matignon" editions on IA are the wrong Matignon, 1516-1548) for "Bellebourg" (the place-name closing f.110's cipher per Bourdeau's transcription) returns 0 hits in either volume. aaymeloglu/unsolved-ciphers (shallow clone, grepped for matignon/mayenne/forget/15571/15572, 26 Sept 2026, then deleted): no hit outside its own tools/decode.py and an unrelated PARES jsonl row. DECODE (de-crypt.org): no fresh crawl run this job (cost); `sources/decode/records-non-decrypted-2026-09-24.tsv` and `records-decrypted-2026-09-24.tsv` (login-free RecordsList cache, 24 Sept 2026) grepped for matignon/mayenne/15571/15572, no hit. OpenAlex (`api.openalex.org/works?search=Matignon Mayenne cipher 1586`, keyed, 26 Sept 2026): 0 results. Semantic Scholar (`x-api-key` header, one query plus the one allowed retry): both 429 (rate-limited even with the key); not answered, logged as unreachable this session, not a negative. Bourdeau's own `matignon1586/NOTES.md` (dbourdeau/cyphersolver, commit fc0c9e8, 25 Sept 2026 18:14 CDT) independently records "no printed decipherment of these despatches was found (searches on the BnF catalogue and on the literature, 17 Sept 2026)". Net: open, no printed or prior decipherment found by any of these six checks; Cipher-3 (f.276, fr.15571 f.179) untouched by any transcription as of this commit.

# Forget / Mayenne / Matignon, BnF fr.15572 (+ fr.15571 f.177/f.179), 1585-86

Catalogue item: QUEUE.md G1 / row 1 of "Re-rank for LANE B5". Kind: recovery. Key already recovered and verified
by Daniel Bourdeau (dbourdeau/cyphersolver, `matignon1586/`, commit fc0c9e8, 25 Sept 2026 18:14 CDT, MIT
code / CC BY 4.0 text) against the manuscript's own contemporary decipherments: f.14v/f.15r (the f.15r clear text
is the period decipherment of f.14v's ciphered postscript), f.18-21/f.19 (f.19 is the period decipherment of
f.18), and the f.78v/79r margin decipherment. That is a period gloss in the sense of CLAUDE.md rule 4/this job's
brief, so single-valued key codes are graded H here; codes Bourdeau's own key.json still carries as ambiguous
(two or three candidate letters) are graded M by `tools/decode_key.py`'s own rule (any `a|b` value auto-downgrades),
and codes he has not resolved at all (value `+` in his key.json: 49, 76, 82, 84, 98, 33, 36, 46, 62, 54, 88, star,
hash, 104, 44, 15, 27, 68, BOX, 79, 19, 53, 23) are graded U (unkeyed).

## What was copied from Bourdeau's repository (credit line, rule 8)

Daniel Bourdeau, `dbourdeau/cyphersolver`, folder `matignon1586/`, commit `fc0c9e865d0fae67ca92d19750d2b09ab11972e0`
(2025-09-25T18:14:52-05:00 per its own commit date -- read 26 Sept 2026), CC BY 4.0 text / MIT code. Copied,
unmodified except reformatting into `tools/decode_key.py`'s `rows` ciphertext format:

- `key.json` -> `key.tsv` (87 codes; values and grades preserved, see "The key" below)
- Per-leaf transcriptions of the leaves he has read only in part: `f110_cipher.txt`, `f123r_cipher.txt`,
  `f123v_cipher.txt`, `f124r_cipher.txt`, `f124v_cipher.txt`, `cipher_f143.txt` (his f.143r), `f143v_cipher.txt`,
  `f150_cipher.txt`, `f154_cipher.txt`, `f173_cipher.txt`, `f196_cipher.txt`, `f201_cipher.txt`, `f177_cipher.txt`
  -> concatenated into `ciphertext.txt` (13,013 tokens over 12,994 real-token lines match his NOTES.md table
  exactly, folio ids prefixed per line).
- `img/BnFfr15571f179.jpg` -> `images/BnFfr15571f179.jpg` (from cryptiana.web.fc2.com via Bourdeau's repo; the
  same image Tomokiyo's `henryiii.htm` cites for Matignon's Cipher-3 -- "Also used in f.179 in BnF fr.15571 (see
  the image above, which includes some additional (variants of) symbols)"). It is **not established here** whether
  the magenta interlinear annotation on this image is a period-contemporary decipherment or Tomokiyo's own modern
  working reconstruction (the right-margin notes read like a modern glyph-legend, e.g. "χ→o", "ξ→e n→e t→r X→j",
  "∠→p", "ω→t"); reported as "Tomokiyo's cryptiana image of the leaf, magenta annotation, provenance not yet
  determined" throughout, not as a period gloss (rule 10: do not over-claim provenance not established).

Bourdeau's own key-verification and per-leaf "Coverage, measured" numbers (22 Sept 2026, his `measure.py`/beam-search
decoder against a scrambled-*key* control) are **not** reproduced here -- this job runs a different, cheaper test
(see below): the same key applied by straight substitution (`tools/decode_key.py`, no beam search, no language
model inside the decoder) against a scrambled-cipher-*order* control, scored afterward by `tools/judge_plaintext.py`.
The two tests are not directly comparable; both are reported.

## Cheap test: Cipher-1 key vs. scrambled-order control

See `specs/matignon-mayenne-1586.json` `cheap_test_done` for the full numbers and command lines. Summary:

Applied Bourdeau's Cipher-1 key (`key.tsv`, from his `key.json`) to `ciphertext.txt` (12,994 tokens, the 13 leaves
he has transcribed only in part) by straight per-token substitution -- `python3 tools/decode_key.py
ciphers/matignon-mayenne-1586` -- no beam search, no language model inside the decoder (unlike Bourdeau's own
`dec.py`/`solve.py`). Grades: **H 10,074 (77.5%)**, **M 1,648 (12.7%, ambiguous 2-3-candidate codes)**,
**U 1,272 (9.8%, unresolved in his key.json)**. Control: the identical 12,994 tokens shuffled into the same
379 lines with the same per-line token counts (3 seeds: 1, 2, 3), same key, same decoder
(`ciphers/matignon-mayenne-1586/control/seed{1,2,3}/`). Grade counts for every control seed are **identical** to
the target (H 10,074 / M 1,648 / U 1,272) -- expected, since `decode_key.py` grades a token from its own key row
alone; fraction resolved (0.9021) is the same for target and control by construction and is not the test.

Scored with `tools/judge_plaintext.py specs/matignon-mayenne-1586.json --file <reading_letters.txt> --json`
(fr16, `min_word_cover` 0.3; `reading_letters.txt` strips `[unkeyed-code]` tokens and unwraps `<word-code>`
tokens from the decoder's `spaced`-style output before folding to letters):

| | language score | vs null_p99 (-1.942) | vs real_p05 (-0.837) | word cover | judge |
|---|---|---|---|---|---|
| **target** (real order) | **-1.371** | above | below | **0.814** | FAIL |
| control seed 1 | -1.782 | above | below | 0.681 | FAIL |
| control seed 2 | -1.793 | above | below | 0.677 | FAIL |
| control seed 3 | -1.784 | above | below | 0.676 | FAIL |

Judge FAIL for target and every control (none reaches real_p05 -- expected: 1,272 unkeyed + 1,648 ambiguous
tokens of 12,994 cannot read as clean prose from a straight substitution). **But the target beats every control
seed by a large, seed-consistent margin**: language score 0.41-0.42 nats above all three (control range only
0.011 wide, so this is not seed noise), word cover +0.136-0.138 above all three. This is a reproducible margin
over a matched control (same N, same K, same design, same decoder -- CLAUDE.md rule 3/5), evidence the key and
these leaves are genuinely the same cipher, even though a straight substitution cannot resolve enough of the
ambiguous/unkeyed tokens to pass the judge outright. **Status stays `partial`, not `closed-negative`** (rule 5):
this is exactly the "beat its matched control by a reproducible margin" case, and a NEAR.md row is owed (worker
note, not written here -- workers do not edit NEAR.md; ROOM.md flags it below for the orchestrator).

Getting a PASS from here needs either Bourdeau's own beam-search decoder (which he has already run -- see
"Coverage, measured" below, not reproduced by this job) or reducing the 1,272 unkeyed / 1,648 ambiguous tokens
by further transcription and context work against the crib leaves (f.14/15, f.18/19, f.78v/79r) -- out of this
job's scope (a first cheap test only, per `.claude/briefs/breadth.md`).

## Cipher-3, fr.15571 f.179: the magenta annotation, transcribed (one pass)

`images/BnFfr15571f179.jpg` (from Bourdeau's repo, sourced from cryptiana.web.fc2.com; 680x737 px, the only copy
on file -- no higher-resolution Gallica fetch made this job, per the cap). Read directly, one pass, at 3x
upscale in 5 overlapping horizontal bands (`tools/` scratch crops, not committed -- regenerable from the image
with PIL crop+resize, not needed for the record). Written to `cipher3_f179_gloss.tsv`.

**Finding that changes the job's premise**: at this resolution and in one pass, the magenta annotation does
**not** read as a continuous interlinear plaintext decipherment (running prose beside/below each cipher line).
Instead it is overwhelmingly **single magenta letters written directly above or below individual black cipher
signs, one letter per sign** -- a glyph-to-letter value label, not a translation -- with only a handful of short
French function words written out as clustered cursive script where the annotator was confident: "front" (band 1),
"pour" (bands 2 and 4), "que"/"gue" (bands 2-3), "entre" (band 3). This pattern (per-glyph letter labels plus a
few spelled-out common words) matches how a modern researcher would annotate a page while *building* a
substitution table, not how a 16th-century clerk wrote a facing decipherment. Tomokiyo's own `henryiii.htm` text
(grepped 26 Sept 2026, see check-solved above) says of f.179: "Also used in f.179 in BnF fr.15571 (**see the
image above**, which includes some additional (variants of) symbols)" -- in a paragraph about *reconstructing*
the Cipher-3 table, consistent with this image being his own working annotation rather than a period gloss.
**Provenance of the magenta ink (period-contemporary vs. Tomokiyo's modern reconstruction) is not established
here** and should not be assumed either way without asking Tomokiyo or examining the original higher-resolution
Gallica scan for ink/hand differences from the black cipher text.

Practical consequence: this leaf cannot be "read directly, no key needed" the way the job brief assumed --
there is no committed running plaintext to align cipher groups against. What is committed
(`cipher3_f179_gloss.tsv`) is a band-level (not manuscript-line-level -- line boundaries were not verified
against the image) best-effort letter/short-word transcription of the magenta ink only, grade M throughout (a
single uncontrolled pass at low image resolution, no independent second pass). No cipher-glyph segmentation or
codebook for this hand exists on file (Cipher-1's key.json does not apply -- Cipher-3 is a different cipher
and, per Bourdeau's NOTES, possibly a different scribal hand), so the `cipher_groups` column says "not
attempted" throughout rather than guess an alignment. fr.15572 f.276 (the other Cipher-3 leaf) was not
transcribed this job (not photographed in Bourdeau's repository at any resolution; a Gallica fetch was in
scope but not needed since f.179 alone met the job's "one pass" bound).

Next step for whoever continues: a higher-resolution IIIF fetch of this leaf (if it is on Gallica) or of
Tomokiyo's original page, and a second independent pass, before trusting any word beyond "front", "pour",
"que", "entre" individually, and before assuming the magenta ink is period rather than modern.

## NEAR step (1), 26 Sept 2026 (LANE B5 worker bMAT2): read/unread split, two-context M/U rule, re-judge

Job: `.claude/briefs/runs/2026-09-26-lane-b5-matignon-mu.md`. Script (reproducible, rule 7):
`resolve_mu.py`, run from the repository root.

**Split (spans.tsv).** Bourdeau's own measure.py rule (a keyed token is READ only if it lies inside a
sense run of >= 3 lexical words / >= 10 letters, measured against his lm.pkl + corpus_words.txt and
cached in measure_cache/) cannot be reproduced here: all three are `.gitignored` in his repository and
none are present in the shallow clone at commit fc0c9e8 (confirmed absent by listing). `resolve_mu.py`
therefore reimplements the SAME MINWORDS=3/MINLETTERS=10 rule on our own straight-substitution decode,
scored against this target's own fr16 corpus (`tools/data/fr16/lettresdecatheri01cathuoft_djvu.txt.gz`,
the corpus already wired in `specs/matignon-mayenne-1586.json`'s judge block) via
`tools/judge_plaintext.py`'s `NgramModel` -- a materially different word list from his, and a stricter
decoder (we have no beam-search LM to fill an M candidate or a U gap, so every M and every U token breaks
a run, the way only his fully-unresolved `+` codes do). Reported as **a proxy split, not a reproduction**
of his measure.json numbers: this rule marks only **1,406 of 12,994 tokens (10.8%) 'read'**, well below
his 26-33% (read_of_transcribed / read_of_leaf, see "Coverage, measured" above) -- consistent with being
strictly stricter, not a contradiction of his figures. `spans.tsv`: 605 line-spans, 127 read / 478 unread.
On the unread spans: **H 8,668, M 1,648, U 1,272** (no M/U token is ever inside a 'read' span, by
construction -- both always break a run).

**Two-context M/U resolution + shuffled-context control.** For each of the 13 M codes (tested only
against their own 2-3 key.tsv candidates) and each of the 49 distinct U signs with >= 2 occurrences
(open a-z search; 14 singleton U signs cannot pass a 2-context rule and were skipped), every occurrence's
immediately adjacent H-chunks (up to the next M/U token or line end) were spliced with a candidate letter
and re-segmented with the same NgramModel; a candidate is 'confirmed' when the splice lands inside a
recognised word. A code reaches grade S at >= 2 confirmed occurrences of the SAME candidate, M at exactly
1. **Real order: 62 codes tested, S 41, M 19. Shuffled-line-order control (3 seeds, tokens shuffled within
each line): S 41 / 45 / 40, M 21 / 16 / 19.** The real count sits inside the control range on both S and M
-- **the two-context rule, as implemented, adds nothing over chance** (a control-backed negative for the
*technique itself*, CLAUDE.md rule 3): the fr16 corpus word list is dense enough (any 3+-letter run of
common French syllables/short words, count >= 2 in a single large 19th-century-edited 16th-century-letters
volume) that splicing almost any letter between two real French chunks produces *some* recognised word by
chance, so 'confirmed by >= 2 contexts' is close to a base rate here, not a chance-beating signal. **No
value is committed**: no exceptions.tsv row is written, key.tsv is untouched, and the per-code
support/candidate detail for both the real run and all 3 control seeds is in `mu_resolve_results.json`
for whoever wants to see which specific codes hit S (the numbers above are the ones that matter --
individual code results are not more trustworthy than the aggregate that failed its own control).

**Re-judge, unread spans alone.** `unread_only_reading.txt` (H-token letters only, unread spans, 9,181
letters) vs a shuffled-line-order control on the identical letter set (3 seeds) -- since no M/U value was
committed, this is necessarily the same "before" and "after" (the technique changed nothing to re-judge):

| | language score | vs null_p99 (-1.944) | vs real_p05 (-0.832) | word cover | judge |
|---|---|---|---|---|---|
| unread spans, real order | **-1.483** | above | below | **0.771** | FAIL |
| shuffled seed 1 | -1.829 | above | below | 0.656 | FAIL |
| shuffled seed 2 | -1.814 | above | below | 0.666 | FAIL |
| shuffled seed 3 | -1.812 | above | below | 0.656 | FAIL |

Same pattern as the whole-target test (previous section): judge FAIL for the unread-only text and every
control (as expected -- these spans are exactly the parts a straight substitution with no LM cannot turn
into clean prose), but the real order beats every shuffled seed by a reproducible margin (score 0.33-0.35
nats above, control range 0.017 wide; cover +0.10-0.12) -- the same "key is real, straight substitution
cannot finish the job" finding as before, now confirmed to hold on the unread-only subset specifically,
not just averaged in with the parts already inside a sense run.

**Grade counts on the unread spans (rule 4):** H 8,668 (period-verified single-valued codes, source
Bourdeau `key.json` fc0c9e8, verified by him against the period decipherments f.14v/15r, f.18-21/19,
f.78v/79r), M 1,648 (ambiguous 2-3-candidate codes, unresolved -- the two-context rule found no candidate
that beat its own shuffled-context control), U 1,272 (unkeyed, same result), S 0, C 0, I 0.

**Net for NEAR.md (orchestrator's to write, not this worker's):** step (1) of the NEAR row's next-step
list is done, negative -- the two-context rule with a shuffled-context control does not resolve any M/U
code beyond chance on this target's transcription and corpus. It does not close the target (rule 5): the
whole-target and unread-only judge tests both still show the same reproducible real-vs-scrambled-order
margin as the original bMAT job, so `partial` stands. The real path to a PASS remains what the original
job named: Bourdeau's own beam-search decoder (already run, not reproduced here) or narrowing the
1,272 unkeyed / 1,648 ambiguous tokens by further transcription/context work -- not by this cheap
context-splicing rule at this corpus density.

## Cipher-3 f.179: Gallica fetch, provenance settled, structural refinement (26 Sept 2026, LANE B5 worker bMAT3)

Job: `.claude/briefs/runs/2026-09-26-lane-b5-matignon-c3.md`. Intake gate re-run before this job:
`python3 tools/intake_gate_check.py matignon-mayenne-1586` -> exit 0, "partial -- edition/page or
full-text-search citation found within 6 lines" (unchanged from bMAT's check-solved above).

**Gallica location found.** BnF fr.15571 = `ark:/12148/btv1b90618802` (Gallica SRU query `gallica all
"français 15571"`, matched by `dc:title` "XXXII Règne de HENRI III (1585, octobre-décembre)" -- the manifest
itself carries no folio labels, every canvas is "NP"). BnF fr.15572 = `ark:/12148/btv1b9061879d` (same
method, "XXXIII Règne de HENRI III (1586, janvier-juillet)"). Physical folio 179 is IIIF canvas/resource
`f187` in the fr.15571 manifest (0-indexed sequence position 186), NOT canvas 179 -- the manuscript carries
two independent numbering layers on each leaf (an older ink number and a later correction), confirmed by
reading both numerals at native resolution at two calibration points: canvas 179 shows old-ink "171" under a
corrected "18[2-3]" (illegible last digit), canvas 184 shows old-ink "176" under corrected "185"; both fit
**old = canvas - 8** exactly (179-8=171, 184-8=176). Solving old=179 gives canvas 187, confirmed correct by
direct content match (identical dense cipher-sign grid layout, identical black inkblot, identical archive
oval stamp position to the pre-existing `BnFfr15571f179.jpg`) and by the leaf's own ink numerals reading
"179" (top right) and "191" (bottom right, a second/different number, uninterpreted) once the canvas is
rotated 180 degrees -- confirming Tomokiyo's own note on `henryiii.htm` ("The digital image of BnF for this
page is upside down") refers to the raw canvas's native scan orientation, not a defect in his own posted
image. Saved: `images/f179_gallica_native.jpg` (native-resolution IIIF fetch, region cropped to the left/
cipher leaf only, rotation=180 applied server-side; see `images/manifest.json`). fr.15572 f.276 was **not**
fetched this job -- locating and triple-confirming f.179's true canvas (three wrong guesses: 179, 180/184
region, before landing on 187) used the job's entire 15-request Gallica allowance; the ark is on file above
so the next worker can go straight to it without repeating the SRU lookup.

**Provenance of the magenta annotation: settled, modern overlay, not period.** Direct comparison of the new
native Gallica image (`images/f179_gallica_native.jpg`, no overlay of any kind) against the pre-existing
Tomokiyo composite (`images/BnFfr15571f179.jpg`) shows the raw manuscript leaf carries **only black cipher
ink**, the leaf's own ink foliation numerals ("179"/"191"), a "BIBLIOTHEQUE NATIONALE MSS" oval accession
stamp, and a wax-seal remnant from the facing/adjacent letter -- **no magenta ink of any kind is present on
the physical leaf**. Every magenta mark on Tomokiyo's composite (the per-glyph letter labels, the clustered
words "front"/"pour"/"que"/"entre", and the margin legend "χ→o", "ξ→e n→e t→r X→j", "∠→p", "ω→t") is
therefore a digital annotation he added when preparing the figure for his webpage, not a period-contemporary
gloss. Independent corroborating evidence (not needed to reach the verdict, but consistent with it): the
margin legend's "→" arrow notation for "sign maps to letter" is a modern mathematical/typographical
convention with no 16th-century precedent, and `henryiii.htm`'s own running text places this image in a
paragraph about *reconstructing* the Cipher-3 table ("Also used in f.179 ... which includes some additional
(variants of) symbols"), consistent with a working annotation built while deriving the alphabet rather than
a period clerk's marginal decipherment. This resolves the open question bMAT flagged and changes the grading
basis for any value read from these labels: **grade M throughout (a modern researcher's proposed reading,
credited to Tomokiyo, not H)** -- per the brief's own instruction and CLAUDE.md rule 4, since H requires a
period key source.

**Structural refinement of the annotation layer (partial, not fully resolved).** Re-examining the composite
at higher zoom than bMAT's original band-level pass surfaces a real ambiguity bMAT's note already gestured at
("only 'pour' and 'que' read as clustered words") that this job could not settle either way: the magenta
layer visibly contains two different kinds of marks -- (a) a handful of connected-cursive whole words
("front", "pour", "que", "entre", "gue") written in a flowing hand, and (b) isolated, individually-formed
single letters positioned above or below specific black signs elsewhere in each line. The natural reading is
that (a) are Tomokiyo's confident whole-word guesses at the plaintext (placed near, but not necessarily
spelling out sign-by-sign, the cipher group they gloss) and (b) are his actual per-sign value labels -- but
this job could not confirm which category "front" belongs to: it could be a 5-letter spelling running
exactly over the first 5 black signs of line 1 (a candidate mapping was cropped to `images/signs/` while
testing this, sign1_hook/sign2_two/sign3_six/sign4_m/sign5_w for f/r/o/n/t respectively) or an unaligned
word-level note like "pour"/"que"/"entre" clearly are. **No sign->letter value is committed to key.tsv or
any other reading file from this pass** -- both the per-sign alignment (which black sign a given isolated
magenta letter labels, above or below it, when lines run close together) and this front/word-vs-spelling
question turned out to be genuinely ambiguous at the composite's native 680x737px resolution, even against
the new higher-resolution primary-source crop, and forcing a guess would produce an unreliable key rather
than a real one (rule 3/4: no fabricated precision). `images/signs/README.md` documents this explicitly so
the crops aren't mistaken for a committed mapping.

**Net for whoever continues:** the Gallica ark and exact canvas (fr.15571 `btv1b90618802` canvas `f187`) are
now on file, saving the lookup; a native-resolution, overlay-free source image is committed
(`images/f179_gallica_native.jpg`); the provenance question is closed (modern overlay, not period -- any
future value from these labels grades M, credited to Tomokiyo); the open task is a genuine sign-by-sign
transcription pass (ideally two independent passes per the usual reconciliation rule, given how easily the
hook/loop shapes here are confused) using this image, followed by fetching fr.15572 f.276 (ark on file
above) with a fresh Gallica request budget to test any resulting partial key.

## Check-solved (bCSMAT), 26 Sept 2026

Job: `.claude/briefs/runs/2026-09-26-lane-b6-csmat.md`, following `.claude/briefs/check-solved.md`.
Why: V7-QA5 (26 Sept 01:53) flagged bMAT's IA full-text check above as a single-term query
("Bellebourg" only) on one edition -- RETRO-2026-09-26b finding 3. Per RETRO-2026-09-26b proposal 3
("the whole edition, grepped for the date... both correspondents' names and the place, every hit
read; never a single term"), this job re-runs the check as a whole-volume sweep, done independently
by this worker (not re-citing bMAT's or Bourdeau's search as its own).

Intake gate before this job (unchanged from bMAT's citation, re-run to confirm before rewriting):
`partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.

**(a) Printed correspondence of Matignon and of Mayenne, via IA advancedsearch (catalogue metadata
only, no Gallica hit this job).**

| query | host | result |
|---|---|---|
| `advancedsearch.php?q=title:(Matignon) AND mediatype:texts` | archive.org | 18 hits; only two are a Matignon *correspondence* edition covering 1585-86: `correspondancede00montuoft`/`correspondanc00mont`, Labande's 1916 "Correspondance de Montaigne avec le maréchal de Matignon (1582-1588)" (two IA scans of the same 32-page pamphlet). The two "Correspondance de Joachim de Matignon" items are the wrong Matignon (1516-1548, a different person, the marshal's grandfather). |
| `advancedsearch.php?q=title:(Mayenne) AND mediatype:texts` | archive.org | 311 hits, all noise (the Mayenne département's modern election ephemera, an unrelated cartulary, League-period pamphlets by other authors) -- no printed correspondence or lettres edition of Charles de Lorraine, duc de Mayenne, anywhere in the results |
| `advancedsearch.php?q=(title:(Mayenne) AND (title:(correspondance) OR title:(lettres)))` | archive.org | 0 hits -- confirms no dedicated Mayenne correspondence/lettres edition exists on Internet Archive |

Both Matignon-correspondence IA items fetched WHOLE (`_djvu.txt`, not a page range) and grepped
for every term named in the brief, not just the place-name bMAT used:

| file | pp. | "1585" | "1586" | "mayenne" (any case) | "matignon" | "forget" | "bellebourg" |
|---|---|---|---|---|---|---|---|
| `correspondancede00montuoft_djvu.txt` | 32 | 0 | 0 | 0 | many (title/running head) | 0 | 0 (bMAT already checked) |
| `correspondanc00mont_djvu.txt` | 32 | 0 | 0 | 0 | many (title/running head) | 0 | 0 (bMAT already checked) |

Both editions are the SAME 1916 "nouvelles lettres inédites" pamphlet (two separate IA scans),
32 pages, and **contain no 1585 or 1586 date anywhere in the OCR text at all**, and never mention
Mayenne or Forget once -- a stronger and more legible negative than the single "Bellebourg" query
bMAT ran: this edition's actual letter dates fall outside 1585-86 entirely (its own title range is
1582-1588, but the surviving letters transcribed in it evidently cluster in other years), so it was
never going to carry the Mayenne-Forget despatches or Matignon's own 1585-86 dispatches to the king
regardless of which single word was searched. No edition on Internet Archive of Matignon's own
official correspondence for 1585-86 (as opposed to his private correspondence with Montaigne) was
found.

**(b) Lettres de Henri III (Société de l'Histoire de France).**

| query | host | result |
|---|---|---|
| `advancedsearch.php?q=title:("Lettres de Henri III")` | archive.org | 0 hits |
| `advancedsearch.php?q=title:(Henri III) AND title:(lettres)` | archive.org | 6 hits, none the SHF edition (a 1622 "Lettres particulieres envoyez au roy", an 1882 book on Italian comedians at court, an 1895 Montaigne piece, an 1849 Spanish play, a 1583 "Lettres de déclaration") |
| `advancedsearch.php?q=creator:("Henri III") AND mediatype:texts` | archive.org | 1 hit, unrelated (a 19th-century Spanish play) |

The SHF's modern critical edition of *Lettres de Henri III, roi de France* (Champollion-Figeac/
Cuttoli/Michel François, 9 vols, 1959-2012) is not on Internet Archive under any of these queries --
searched, not present, not citable as read. (Per the brief's host list this job did not query
Gallica or HathiTrust for it; a HathiTrust/JSTOR route, if wanted, is a `LOCAL-QUEUE.tsv` row, not
this job's to add unasked.)

**(c) Tomokiyo, `sources/cryptiana/web/henryiii.htm`, read directly this session** (converted with
`tools/html2text.py`, grepped, not re-citing bMAT's earlier read). Verbatim, on Mayenne-Forget's
Cipher-1 (line 638 of the converted text): "Letters in this cipher are found in f.14 (deciphered in
f.15), f.18-21 (deciphered in f.19), f.78-79 (deciphered in the margin), f.91-92 (deciphered in the
margin), f.110 (undeciphered), f.123-124 (undeciphered), f.143 (undeciphered), f.150 (undeciphered),
f.154 (undeciphered), f.173 (undeciphered), f.196 (undeciphered), f.201 (undeciphered), etc." On
Matignon's Cipher-3 (line 689): "Used in f.189 (deciphered in f.190), f.276 (undeciphered), f.277-278
(deciphered in f.279-280), f.282 (deciphered in the margin). Also used in f.179 in BnF fr.15571 (see
the image above, which includes some additional (variants of) symbols)." And (line 692): "The
undeciphered text in f.276 can be read as something like 'La Guiolle est en doubte du pu pour les
amis de la Roussiere sont et grand nombre avec lu....'" All target leaves named in this job's brief
are covered by these two quotations and every one reads undeciphered as of the live page.

**(d) DECODE (de-crypt.org) listing.** No fresh crawl run this job (the good-citizen rule against
repeated crawls of the same host, and the existing cache is 2 days old, not stale enough to
distrust for a manuscript catalogue that does not change daily): `sources/decode/
records-non-decrypted-2026-09-24.tsv`, `records-non-decrypted-2026-09-24-diff.tsv` and
`records-decrypted-2026-09-24.tsv` (login-free RecordsList crawl, 24 Sept 2026) grepped
independently by this worker (not quoting bMAT's sentence) for `matignon|mayenne|15571|15572|forget`,
case-insensitive: 0 lines matched in any of the three files.

**(e) Solver repositories, fresh shallow clones this job, deleted after.**

| repo | HEAD commit | date | grep result |
|---|---|---|---|
| dbourdeau/cyphersolver | `fc0c9e865d0fae67ca92d19750d2b09ab11972e0` | 2026-09-25 18:14:52 -0500 | `matignon1586/NOTES.md` unchanged from the 25 Sept 2026 credit line already in this file: "no printed decipherment of these despatches was found (searches on the BnF catalogue and on the literature, 17 Sept 2026)"; no `matignon1586/` file marks any of the target leaves solved |
| aaymeloglu/unsolved-ciphers | `2495c45e8b94ffbc4f09a085224aa5ebce5cdf9f` | 2026-09-23 14:27:44 -0500 | only hit is `catalogue/pares-pages.jsonl` id 3625361, a Spanish PARES catalogue entry about the Duke of Mayenne's 1580s arrival in Genoa during a plague outbreak -- unrelated to this cipher (same finding as bMAT, now with the commit hash on file) |

**(f) Web search** ("solved"/"déchiffr\*"/model-solve source family per check-solved.md): "Mayenne
Forget cipher BnF fr.15572 déchiffré" and "Matignon cipher BnF fr.15571 f.179 solved deciphered
Claude GPT" return only Bourdeau's own repository/site (dbourdeau.github.io/cyphersolver, the same
source already credited) and two unrelated GitHub forks of his repository (arya1515, aryasn2026 --
forks with no new commits on this target found); no third-party claim of a solution. A third query,
`"Mayenne" cipher 1586 solves Vals AI OR "Claude Fable" OR benchmark historical cipher`, surfaces
only the unrelated Vals AI "Cyphral Distich" post (Thomas Urquhart's book cipher, a different
target) -- no model-solve announcement mentions Mayenne, Matignon or Forget.

**(g) OpenAlex and Semantic Scholar, one query each (both keys present and working this session,
unlike bMAT's 429s).**

| query | host | result |
|---|---|---|
| `works?search=Matignon Mayenne chiffre 1586` (`Authorization: Bearer $OPENALEX_KEY`) | api.openalex.org | 7 results, all general League-period historiography (e.g. "Les maréchaux de la Ligue" 2010, "Philippe II et la Ligue parisienne (1588)" 2011) -- none about this cipher or a decipherment |
| `paper/search?query=Matignon Mayenne cipher 1586 chiffre` (`x-api-key: $S2_KEY`) | api.semanticscholar.org | 0 results |

**Net.** Seven independent checks (a-g), all negative for a prior decipherment or a printed
plaintext of any of the target leaves (fr.15572 ff.110, 123-124, 143, 150, 154, 173, 196, 201;
fr.15571 f.179; fr.15572 f.276). The whole-volume IA sweep is a materially stronger negative than
bMAT's single-term query -- it rules out the entire 32-page candidate edition on every relevant term,
not just one place-name -- but does not change the verdict: `open` (check-solved sense: no printed
plaintext or prior decipherment found), status stays `partial` (rule 5: the cryptanalytic
control-margin finding above, unrelated to this check).

Request counts this job: archive.org ~11 (4 advancedsearch, 2 metadata, 3 `_djvu.txt` fetches
including one redirect retry, all ≥1.5s apart); github.com 2 (shallow clones, deleted after);
api.openalex.org 1; api.semanticscholar.org 1; de-crypt.org 0 (cache reused, no live request);
gallica.bnf.fr 0 (none, per brief).

Intake gate, re-run after this rewrite:
```
matignon-mayenne-1586: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
```

## NEAR step (1b), M/U beam (bMATBEAM), 26 Sept 2026

Job: `.claude/briefs/runs/2026-09-26-lane-b6-matbeam.md` (LANE B6, Opus). Intake gate at 03:36 UTC (lane
orchestrator) and again by this worker at 03:38 UTC: `matignon-mayenne-1586: partial (line 1) --
edition/page or full-text-search citation found within 6 lines`, exit 0. Script `mu_beam.py` (run from the
repository root; docstring gives the design). No hosts, disk and CPU only.

**Design.** Character 6-gram, interpolated Witten-Bell, trained on fr16 `lettresdecatheri01` + `lettresindites00marg`
(Lettres de Catherine de Médicis t.1 and Marguerite de Valois, same decade and register as the target; spaces
removed, j->i, v->u, w->uu, accents stripped); `lettresdecatheri02` held out entirely (held-out 2.93 bits/char).
M codes chosen per occurrence among their own key.tsv candidates by exact Viterbi per line (states recombined
on the last 5 letters, exact for this LM); U signs one global value each from 22 letters + `null` + `TOK`
(nomenclator word: resets the context), by coordinate ascent with the M choices held, alternating with the M
Viterbi until no U value changes. `null` and `TOK` each cost one average character (2.93 bits) so neither is free.
Change from the orchestrator's sketch: alternating M-Viterbi / U-ascent instead of the M beam inside every U
trial (same fixed point, a fraction of the cost); control (A) licenses it or not either way.

**Gate, stated before the first run:** control (A) mean of 3 seeds: U-sign accuracy (distinct signs,
unweighted) >= 0.60 AND M-occurrence accuracy >= frequency baseline (the candidate whose letter is commonest in
French) + 10 points.

**Round 1 (6 iterations cap, 5 restarts; `mu_beam_results_round1.json`):**

| control (A) seed | U-sign acc (signs) | U token-weighted | M acc | M freq baseline | M oracle-majority | bits/char before -> after |
|---|---|---|---|---|---|---|
| 1 | 0.619 (42) | 0.627 | 0.838 | 0.468 | 0.668 | -3.830 -> -3.111 |
| 2 | 0.568 (44) | 0.635 | 0.797 | 0.489 | 0.646 | -4.017 -> -3.230 |
| 3 | 0.605 (43) | 0.811 | 0.853 | 0.463 | 0.642 | -3.961 -> -2.957 |
| mean | **0.597** | 0.691 | 0.829 | 0.473 | 0.652 | |

Control (B), shuffled within lines: bits/char -5.914 -> -5.737, -6.078 -> -5.700, -6.003 -> -5.715.
Round 1: U gate NOT MET (0.597 < 0.60), M gate met (+35.6 points over frequency baseline, +17.7 over the
oracle per-code majority). Every restart stopped at the 6-iteration cap, unconverged, and frequent signs were
among the wrong ones (control seed 3: sign `4`, 106 tokens, wrong at a 161-bit margin) -- a search-depth fault,
so one change was declared before re-running: iterate to convergence (cap 30), 10 control restarts, and the
gate must also hold on three fresh seeds (4-6) as a replication, so the retry cannot be a seed-shop.

Correction to the round-1 diagnosis above (found after round 2): the "6 of 6 iterations, unconverged" reading was
a bug in the stopping test, not evidence about the search. `search()` compares the best value with `uval[s]`
after the trial loop has left it on the last value tried, so the test almost never reads zero and every run goes
the full ITERS (commented in the script, behaviour left as is so the JSON reproduces). Round 2 changed only
seed 1 (U 0.619 -> 0.643); seeds 2 and 3 are identical to round 1.

**Round 2 (30 iterations, 10 restarts; `mu_beam_results.json`), control (A):**

| seed | U-sign acc (signs) | U token-wtd | M acc | M freq baseline | M oracle-majority | bits/char before -> after |
|---|---|---|---|---|---|---|
| 1 | 0.643 (42) | 0.628 | 0.838 | 0.468 | 0.668 | -3.693 -> -3.110 |
| 2 | 0.568 (44) | 0.635 | 0.797 | 0.489 | 0.646 | -4.017 -> -3.230 |
| 3 | 0.605 (43) | 0.811 | 0.853 | 0.463 | 0.642 | -3.961 -> -2.957 |
| 4 (repl.) | 0.667 (42) | 0.780 | 0.855 | 0.472 | 0.653 | -3.663 -> -2.929 |
| 5 (repl.) | 0.447 (38) | 0.762 | 0.807 | 0.469 | 0.674 | -3.765 -> -3.123 |
| 6 (repl.) | 0.707 (41) | 0.816 | 0.836 | 0.432 | 0.689 | -3.607 -> -2.926 |

Gate: **met, only just** on U (0.605 on seeds 1-3, 0.607 on 4-6, one seed at 0.447). Met clearly on M
(+35.6 / +37.5 points over the frequency baseline, and +17 to +19 over the oracle per-code majority, which is
the stronger baseline). Largest margin of any WRONG U sign in control (A): 264.9 bits (seed 4).
Control (A) also shows how `TOK` behaves on clean text with a known answer: the search wrongly sends
true-letter signs to `TOK` (18-37% of U tokens across the 6 seeds; recorded per seed in the JSON as
`wrong_tok_signs`, `wrong_tok_token_share`): 11-17 signs.

**Control (B), shuffled within lines (3 seeds):** bits/char -5.914 -> -5.737, -6.078 -> -5.700, -6.003 -> -5.715
(gain +0.18 to +0.38). On shuffled text the optimiser sends **36-43 of 48 U signs to `TOK`, 99.0-99.5% of U
tokens** (`tok_signs`, `tok_token_share` in the JSON).

**Target (6 restarts):** bits/char -4.721 -> -4.239 (gain +0.48, between control (B)'s +0.18-0.38 and control
(A)'s +0.58-0.81, and the end point sits far outside control (A)'s -2.93 to -3.23). **34 of 48 U signs, 98.4% of U tokens, go to
`TOK`**, including all the frequent ones (`U` 343, `z` 296, `BOX` 137, `4` 106, `w` 83, `T` 53, `y` 41, `v` 37),
stable across all 6 restarts. That is the shuffled-text pattern of control (B), not the known-answer pattern of
control (A). Four signs (`U`, `z`, `BOX`, `4`) pass the brief's letter-of-the-rule licence (stable, margin over
264.9 bits), but their value is `TOK`, the value the optimiser picks on any text whose context does not read. So
**no U value is licensed and key.tsv / exceptions.tsv are unchanged** (the script's `licensed` flag now excludes
`TOK`/`null` for this reason). The 14 non-`TOK` U signs (13 letters and `68`->null: `36`->e, `53`->e, `37`->e, `46`->t, `101`/`104`->l,
`f3`->a, `O`->i, ...) have 1-3 occurrences each and margins of 0.5-8.1 bits (two unstable across restarts), far
below 264.9.

M per-occurrence choices on the target (S candidates only, in `m_choices` of the JSON, not committed): f c 277 / u
225; E i 294 / y 59; B i 267 / y 39; 6 n 110 / i 52 / s 45; ff n 58 / o 31; T= m 74 / mm 8; S u 38 / c 8; yy s 27
/ ss 10. The technique is control-backed on M (control (A) above), but the target's context fits the LM much worse
than any control (A) text did (-4.24 vs -2.93 to -3.23 bits/char), so the control's 0.80-0.86 accuracy cannot be
assumed to carry over; these stay candidates, not grades.

**Judge** (fr16, `lettresdecatheri01`, Lettres de Catherine de Médicis t.1, same decade; `mu_beam_reading.txt`, TOK
rendered as a space, null dropped):
```
FAIL language: score=-1.347, null_p99=-1.947, real_p05=-0.839, real_median=-0.779, mode=both, N=12484
ok   words: cover=0.812, min=0.3, real_text_median_cover=0.946
FAIL - matignon-mayenne-1586 (a PASS is a gate for a verifier, not a reading; rule 10)
```
Straight-substitution reading before this step, same judge: -1.371, cover 0.814 (FAIL). Shuffled-order controls
of the earlier cheap test, same judge: -1.782 / -1.793 / -1.784. The beam moves the score by +0.024, a small
fraction of the 0.41 target-vs-shuffle margin already on file, and stays FAIL.

**Grade counts after this step (rule 4), unchanged:** H 10,074 / S 0 / M 1,648 / U 1,272 (C 0, I 0).

**Net.** Control-backed technique: the M part works on known-answer text (+17 over oracle majority), the U part
only just meets its gate. On the target it does not help: the U solution looks like the shuffled-text null, not
the known-answer control, and the judge moves +0.024. Reading of the result (inference, not tested): most of the
target's lines do not read as French context even with H fixed (end fit -4.24 bits/char against about -3.0 for
enciphered held-out prose), so the frequent unkeyed signs (`U`, `z`, `4`, `w`, `T`, `y`) most likely are not single
letters of this alphabet. They may be nomenclator codes, nulls, word dividers or transcription artefacts, or the H
key may be wrong on part of the leaves. Suggested next step, not run: rerun the same search only on the 127 'read'
spans of spans.tsv plus their neighbours, where the context does read, and/or add a per-leaf split (some leaves may
use a different table). Status stays `partial` (rule 5).

**NEAR step (1c) (bMAT1C), 26 Sept 2026.** Committed bMATBEAM's per-occurrence M choices as grade S. Steps:
`exceptions.tsv` written (1,648 rows, one per M occurrence, `line`/`position`/`value`/`grade S`/reason
"bMATBEAM fr16 6-gram beam, known-answer control 0.83"), value taken from the target's chosen restart
(seed 8 of {7,8,9}, obj -52937.459, the same argmax rule `main()` uses to pick `res['target']`), reproduced
by rerunning `mu_beam.py`'s exact deterministic search (`search()`, same seeds) rather than trusting an
aggregate: per-sign per-value tallies from the reproduction matched `mu_beam_results.json`'s `m_choices`
exactly (0 mismatches across all 14 M signs, 1,648 occurrences) before any row was written, so this is the
same beam already control-backed in bMATBEAM, not a re-decision. No U value touched (bMATBEAM's finding
stands: the U solution reads as the shuffled-text null, not the known-answer pattern). `decode.json` now
points at `exceptions.tsv`. `tools/decode_key.py ciphers/matignon-mayenne-1586` then `--check`: exit 0,
"reading up to date".

Grade counts: before H 10,074 / S 0 / M 1,648 / U 1,272 (C 0, I 0) -> after H 10,074 / **S 1,648** / M 0 /
U 1,272 (C 0, I 0).

Judge (fr16, `lettresdecatheri01`, same spec as the earlier steps), new `reading.txt` vs a freshly-built
shuffled-line-order control (token order shuffled within each line of the same rendered reading, 3 seeds,
same letters -- not a re-decode from ciphertext, so `exceptions.tsv`'s position-keyed rows cannot be
misapplied to the wrong sign under shuffling):

```
target (S-committed reading):        FAIL language: score=-1.545, null_p99=-1.942, real_p05=-0.838, real_median=-0.781, N=14459
                                      ok   words: cover=0.714, min=0.3, real_text_median_cover=0.946
control seed 1 (shuffled-in-line):    FAIL language: score=-1.898 | words cover=0.601
control seed 2 (shuffled-in-line):    FAIL language: score=-1.896 | words cover=0.605
control seed 3 (shuffled-in-line):    FAIL language: score=-1.888 | words cover=0.604
```
Control mean -1.894 (range 0.010 wide); target beats every seed by +0.34 to +0.35 (a margin of the same
order as the +0.41/+0.136-cover margin already on file for the pre-beam straight-substitution reading), and
cover +0.11-0.11 over the control mean. Still FAIL against `real_p05` (-0.838): control-backed margin holds,
gate does not.

Note against over-reading this as progress: the target's own score got **worse**, not better, than the
pre-beam straight-substitution reading on the identical judge and rendering (-1.371 before this step vs
-1.545 now; cover 0.814 -> 0.714). Likely reason (inference, not tested): bMATBEAM's per-occurrence M
choices were optimised *jointly* with the U coordinate-ascent step (each M Viterbi pass in `mu_beam.py`'s
`search()` ran against whatever U values the alternating loop held at that point, mostly `TOK`/wrong per
bMATBEAM's own finding), not against the naive bracket-placeholder rendering `decode_key.py` uses for
unkeyed signs here; committing the M half of a jointly-fit pair while discarding the U half changes the
context each M choice was fit to. The straight-substitution reading's old M values (`v.split('|')[0]`, an
arbitrary first-candidate pick) were not "wrong" here so much as this new reading and the old one are
different heuristics neither licensed by a matched control at the *reading* level (only bMATBEAM's own
M-occurrence accuracy on control (A) is control-backed, per rule 3; the judge margin above is the
new reading's own control, and it does hold).

Grade counts (rule 4), final: H 10,074 / S 1,648 / M 0 / U 1,272 (C 0, I 0). Status stays `partial` (rule 5:
a control-backed reproducible margin, not closed-negative; a control-backed gap, since the judge gate is
still not met).

## NEAR steps (1c') and (1d) (bMAT1D), 26 Sept 2026

Job: `.claude/briefs/runs/2026-09-26-lane-b7-mat1d.md`.

**(1c') Revert bMAT1C.** `exceptions.tsv` did not exist before bMAT1C's commit (`48f340d`; confirmed with
`git show 48f340d^:.../exceptions.tsv` -> "exists on disk, but not in 48f340d^"), so the revert deletes it
and restores `decode.json`, `reading.txt`, `reading_tokens.tsv` to their `48f340d^` content (`git checkout
48f340d^ -- <paths>`; `reading_letters.txt` was untouched by bMAT1C, confirmed identical to its `48f340d^`
version, so left as is). `python3 tools/decode_key.py ciphers/matignon-mayenne-1586`: **H 10,074 / M 1,648 /
U 1,272**, matching the pre-bMAT1C counts exactly. `--check`: exit 0, "reading up to date". Re-judge
(`tools/judge_plaintext.py specs/matignon-mayenne-1586.json --file reading_letters.txt`): **FAIL
language: score=-1.371, null_p99=-1.942, real_p05=-0.837, N=12485; words: cover=0.814** -- matches the
pre-bMAT1C numbers exactly (the brief's "about -1.371 / cover 0.814"). M back to M throughout (no S).

**(1d) U signs as nomenclator code words -- which U signs sit inside a period-deciphered passage.**
Source of meanings, per the brief: Bourdeau's transcriptions of the three period decipherments, shallow
clone `dbourdeau/cyphersolver` (credit: Daniel Bourdeau, `matignon1586/`, HEAD at clone time, CC BY 4.0
text / MIT code; clone deleted after this job). Of the three named crib locations only two have a
transcribed cipher stream AND its full period plaintext both on file in his repository: `f78_cipher.txt`
+ `crib_f78.txt` (Mayenne to the King, camp, March 1586, margin-deciphered) and `f79_cipher.txt` +
`crib_f79.txt` (the same letter's continuation). The third, f.14v/f.15r, has only the cipher
(`l1415.txt`, 27 tokens) -- the repository holds just the opening phrase of f.15r's clear text as a
quotation inside `NOTES.md`, not a full transcription -- so it cannot be tested; f.18-21/f.19 likewise has
only 3 lines of cipher (`cipher_f18.txt`) against 2 lines of plaintext (`f19_plain.txt`), far short of the
"22 lines cipher / 32 lines clear" his own `NOTES.md` describes for that leaf, so this pair is too short
and its correspondence to the rest of the leaf is unverified; excluded from the test as unverified rather
than assumed. **This narrows the passage actually tested to f.78v/f.79r.**

Of the target's 48 distinct U signs, **19 occur at all inside these four crib cipher files; 17 occur
inside the one verified pair (f.78v/f.79r)**: `U`(f78:17,f79:10), `T`(f78:10,f79:1), `D2`(f78:8,f79:4),
`5`(f79:8), `4`(f78:5,f79:2), `z`(f78:3,f79:2), `BOX2`(f78:4,f79:1), `w`(f79:5), `y`(f78:4), `u`(f78:3),
`1`(f78:1,f79:1), `p`(f78:1), `2`(f78:1), `9`(f78:1), `fe`(f79:1), `me`(f78:1), `de`(f78:1) -- 96 token
occurrences in total. Two more (`BOX`, `hash`) occur only in the unverified f.18 fragment and are not
tested. The other 29 U signs do not occur in any crib file at all. Script: `align_crib.py` (this folder).

**Method.** A global monotonic DP (Needleman-Wunsch style, `align_crib.py:align_leaf`) aligns each leaf's
cipher token stream to its despaced period-plaintext letter stream: each token consumes 1 letter (scored
+2 match / -3 mismatch against its key.tsv value, only for tokens already graded H) or 0 letters (a null
code, -1), except a token whose H value is itself a known multi-letter word (e.g. `14`=que), which must
consume that word's exact letters in one step. M/U/hidden tokens score 0 either way, so the winning path
is driven entirely by the already-established H key, never by the sign under test -- this is what would
license reading a value off the path for an untested sign. Verified correct on synthetic cases (perfect
substitution, and with interspersed null codes): both recovered 100%.

**KNOWN-ANSWER CONTROL, run first, before any U value was read.** Two draws, both on codes actually
occurring in f.78v/f.79r (same design as the real test, not a different leaf or a different token count):

1. The 20 *most frequent* H codes hidden (h,d,t,o,q,e,7,m,.v.,Ze,L,4+,s,A,w-,oo,n,a,c,R -- 470 of the
   leaves' 470 H tokens are of these 35 types; these 20 account for the bulk of them). This turned out to
   strip nearly all anchoring at once (a design flaw caught before trusting the number: the real U-sign
   test never removes more than 15% of a leaf's H tokens, since all *other* H codes stay keyed). Recovered
   value (majority vote across occurrences) matched the true key.tsv value on **6 of 20**.
2. Re-drawn to match the real test's design: 20 H codes whose *combined token count* (93) is close to the
   96 tokens the real U signs occupy, leaving the other 15 H types (377 of 470 H tokens, 80%) as intact
   anchors -- the same anchor density the real U-sign test would have. Codes: 13,M,b,X,x,8,26,g,24,D,lam,
   he,3,R,c,n,a,oo,w-,H. Recovered **4 of 20** (`D`,`H`,`R`,`a` correct; `13,24,26,3,8,M,X,b,c,g,he,lam,n,
   oo,w-,x` wrong). DP alignment score strongly negative in both draws (f78 -12 and -52, f79 +1 and -27) --
   and even with **nothing hidden** (all 35 H types scored), the DP's own best-scoring path agrees with the
   already-established key.tsv value on only 88/309 (f78, 28%) and 76/161 (f79, 47%) of H-token positions,
   confirming this is not an artefact of which 20 codes were hidden.

**Both draws fail the >=16/20 gate by a wide margin (6/20, 4/20).** Per the brief, no U value is committed:
**key.tsv and exceptions.tsv are unchanged, no C grade written.** This is a control-backed negative for
*this alignment technique on this crib pair* (rule 3): whatever the reason -- the crib's own transcription
order not matching `f78_cipher.txt`/`f79_cipher.txt`'s line order 1:1 (Bourdeau's own repository carries
separate `cribfit.py`/`cribem.py`/`forcealign.py`/`segalign.py` scripts, suggesting he needed more than
straight concatenation to use this crib himself), a different transcription convention between the two
files, or simply that the "marginal decipherment" does not run continuously beside the full two pages of
cipher -- a naive whole-leaf concatenation is not a working alignment here, so no U sign's meaning is read
off it. **1d does not close as "no meaning source" (17 signs did occur in a covered passage) -- it closes
as a negative for the alignment procedure, tested and rejected by its own control before any value was
trusted.** Next step for whoever continues: a smarter alignment (per-line correspondence checked by eye
against the image first, or reusing Bourdeau's own `cribfit.py`/`forcealign.py` rather than re-deriving the
DP) would need to pass this same known-answer gate before any U value from it is trusted.

Grade counts unchanged from (1c'): H 10,074 / M 1,648 / U 1,272 (C 0, S 0, I 0). Status stays `partial`
(rule 5). Files: `align_crib.py` (script, rule 7 -- reruns `python3 ciphers/matignon-mayenne-1586/
align_crib.py --hide CODES --targets CODES` from the repository root, no ciphertext or key files depend on
its output since nothing was committed). Hosts: github.com 1 shallow clone (dbourdeau/cyphersolver,
deleted after reading `matignon1586/`), no other host.

## NEAR step (1e) (bMAT1E), 26 Sept 2026

Job: `.claude/briefs/runs/2026-09-26-lane-b7-mat1e.md`. Intake gate `tools/intake_gate_check.py`: exit 0
("partial (line 1) -- edition/page or full-text-search citation found within 6 lines").
Source: Bourdeau's transcriptions `f78_cipher.txt`, `f79_cipher.txt`, `crib_f78.txt`, `crib_f79.txt`
(Daniel Bourdeau, dbourdeau/cyphersolver `matignon1586/`, HEAD fc0c9e8, read 26 Sept 2026, CC BY 4.0 text;
copied into `align1e/` with this credit; clone deleted). No images fetched (transcription-only test, rule 2:
the result is conditional on these transcriptions).

**Design.** `align1e/make_masked.py` writes the passage with every token replaced by its key.tsv value.
Control: 20 H codes masked as `<Xnn>`, drawn by seed (1586) from the 21 H codes with <= 11 occurrences in the
passage -- density-matched to the U test (the 22 U/unkeyed sign types there occupy ~110 tokens; the 20 drawn
codes 103 of the 470 H tokens; the 20 rarest total only 93, so a draw that includes frequent codes, like seed
1586's unrestricted draw at 270 tokens, would strip the anchors, bMAT1D's draw-1 flaw). The hand alignment was
done blind by one Opus subagent that saw only `masked_control.txt` and the two cribs (segments of ~20 tokens
between read anchors, value by vote over occurrences), output `align1e/control_answers.tsv`,
`align1e/control_alignment.md`. Scored by `align1e/score_control.py` (exact value match).

**Known-answer control: 9/20 against the 16/20 gate -- FAIL.** Correct: a, d, o, que, p, f, qui, a, l
(X01,06,07,09,11,13,14,16,18). Wrong: 3(e->i), 24(nostre->t), x(e->a), b(e->u), 26(uous->v, a near miss),
g(u->p), oo(d->s), he(l->u), X(g->r), c(p->u), D(a->places). By the subagent's own confidence: H-confidence 7/7
correct, M 1/6, L 1/7. The subagent found trustworthy anchors only in f78.1-5 and f79.3-6; f78.6-10 and
f79.1-2 did not align by reading (the key reads these leaves at 28-47% even unmasked, bMAT1D), so codes whose
occurrences fall there are guesses.

**Consequence.** Per the brief, the target run (17 U signs, `masked_target.txt`, built but not given to any
aligner) was not run, and **no U meaning is committed: key.tsv, exceptions.tsv, reading files unchanged**
(H 10,074 / M 1,648 / U 1,272; judge unchanged at -1.371 vs shuffled -1.78, not re-run since nothing changed).
This is a failed-control non-test for hand alignment on this transcription pair, not a negative on the U signs
(rule 3). Status stays `partial`.

**Suggestion (one line, not done).** The confidence split (H-confidence 7/7) suggests a pre-registered gate on
high-confidence answers only -- but that rule was seen after scoring, so it needs a fresh seed's control
before any use; better first: re-transcribe f.78v 6-10 and f.79r 1-2 from native crops (Gallica ark
btv1b9061879d canvas 85) with the margin decipherment line-by-line, since those segments are where alignment
broke. Hosts: github.com 1 shallow clone (deleted); no other host.

## NEAR step (1f) (bMAT1F), 26 Sept 2026 -- stopped at cap, partial

Job: `.claude/briefs/runs/2026-09-26-lane-b8-mat1f.md`. Intake gate re-run 06:55 UTC: `matignon-mayenne-1586: partial
(line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0. **Stopped at 07:15 UTC, over the
USD 7 cap; steps 3 (settling) and 4 (fresh-seed control) not run. Key, reading and grade counts unchanged (H 10,074 / M 1,648 / U 1,272).**

**Location.** `gallica_folio.py btv1b9061879d --folio 78/79`: the manifest has no folio labels (385 canvases, all
unlabelled), so no estimate; taken instead from Bourdeau's own folio table (matignon1586/NOTES.md, fc0c9e8): canvas 85 is
the opening, **f.78v = left page, f.79r = right page**; confirmed on the overview (images/f78v_79r/overview_1600.jpg).

**Crops.** Native regions of canvas 85 (images/f78v_79r/src_*.jpg, manifest.json). `tools/iiif_lines.py` fetched the
f.78v block (1250,2400,3070,1060) but its band detection failed on this dense slanted hand (8 of 12 centres, lines missed
and doubled; debug overlay f78v_lines_debug.jpg), so bands were set by eye from a pixel ruler and cut with PIL
(f78v_{A..F}_s{1,2}.jpg, f78v_G_tail.jpg; f79r_{A,B}_s{1,2}.jpg; boxes in manifest.json). Reference sign chart for label
consistency: f.78v lines 1-5 (the lines bMAT1E's aligner could anchor) with Bourdeau's labels
(align1f/reference_f78v_l1-5.tsv, ref/*.jpg); passes were blind for every target line.

**Transcription finding (image, one pass for f.78v -- grade M until a second pass agrees).** The f.78v cipher block has
**11 full lines plus 3-4 signs** at the head of the following prose line ("... Les armees des sieges ..."); Bourdeau's
`f78_cipher.txt` has **10**. Pass A (align1f/passA_f78v.tsv) against Bourdeau line by line, each half-line aligned
against every Bourdeau line (align1f/diff_vs_bourdeau.py -> diff_f78v.tsv): page lines 6, 7, 8 match his 6, 7, 8 on both
halves; page line 9's left half = his 9, its right half matches no Bourdeau line; page line 10's left half = his 10's left,
its right half matches none; **page line 11's right half = his line 10's right half** (16 of 19 tokens shared), its left
half matches none. So his line 10 is page line 10 (left) joined to page line 11 (right), and about 1.5 page lines (~55
signs: 9 right, 10 right, 11 left) plus the tail signs are absent from his transcription -- a line-join slip, which
explains why f78.6-10 would not align to the crib in bMAT1D/bMAT1E. Pass B for f.78v was stopped at the cap before it
wrote anything.

**f.79r lines 1-2 (two passes).** `reconcile_passes.py` (align1f/agreement.tsv, disagreements.tsv, ciphertext_draft.tsv):
agreement 44/74 = 59.5% (line 1 52%, line 2 66%), 30 disagreement columns, unsettled. Both passes follow Bourdeau's
line 1 and 2 in order and length (no missing segment); the recurring difference is **`4` (a U sign) vs `4+` (=m, H)**:
pass B reads plain `4` where Bourdeau writes `4+` at several positions, pass A mostly `4+`. Not settled on the image.

**Margin decipherment.** Bourdeau's `crib_f78.txt` has 9 lines, the last four apparently two margin columns read across;
on the overview the f.78v margin runs well below the cipher block. The native margin fetch (600,2150,800,2500) failed
twice with a connection reset at gallica.bnf.fr (07:03, 07:04 UTC); stopped the host per the good-citizen rule.

**Next step (one line, not done).** Second blind pass over f78v_{D,E,F}_s*.jpg + G only (the slip lines, ~4 subagent-
calls' worth is too many: one call, crops only), settle 4/4+ on f79r from disagreements.tsv, fetch the f.78v margin and
transcribe it, then build corrected f78/f79 streams and run make_masked.py control with a fresh seed (scripts copied
in align1f/, unchanged gate 16/20). Hosts: gallica.bnf.fr 5 answered + 2 reset (7 of 12); github.com 1 shallow clone
(dbourdeau/cyphersolver, read matignon1586/NOTES.md folio table, deleted).

## NEAR step (1g) (bMAT1G), 26 Sept 2026

Job: `.claude/briefs/runs/2026-09-26-lane-b8-mat1g.md`. Intake gate 07:32 UTC: `matignon-mayenne-1586: partial (line 1) --
edition/page or full-text-search citation found within 6 lines`, exit 0. No host touched (crops on disk from bMAT1F).
**Key, reading and grade counts unchanged (H 10,074 / M 1,648 / U 1,272); no U meaning committed.**

**U1, second blind pass.** One Sonnet subagent over f78v_{D,E,F}_s{1,2}.jpg + G_tail with reference lines 1-3
(align1g/passB_f78v.tsv, per-segment rows kept). Pass B wrote the F segments in swapped order (its F1 is the right crop);
the crop f78v_F_s1.jpg was checked by eye and pass A's order is right (line starts `9 14 c p o BOX2`).

**Correction to bMAT1F's slip description (two passes now agree on the structure).** Bourdeau's l.9 = page l.9 up to
`.v. d` + page l.10 from `Ze oo t ff h` to its end (page l.10's right half is not missing: it is in his l.9); his l.10 =
page l.10 up to `o s e` + page l.11 from `Ze d ff` to its end. What his transcription skips is **page l.9 after `.v. d`
(27 signs) and page l.11 before `Ze d ff` (17 signs) = 44 signs**, not ~55 in three half-lines.

**U2, reconciliation.** `tools/reconcile_passes.py passA_ins.tsv passB_ins.tsv` over the two skipped segments + the tail:
36/53 columns agree (67.9%), 17 disagreement columns (align1g/disagreements.tsv). Settled on f78v_D_s2.jpg / F_s1.jpg: 9R
`w` not `w-` (no bar), one sign `d` where the passes wrote `d o`/`o d`, `d` not `ff` before `7 3`, `54` not `4`; 11L `oo`
single sign (pass A's extra `o` dropped). Kept at M (one pass or single-reader settlement): 9R `2`, `w`, `d` x3, `54`,
final `7 6`; 11L initial `9` (pass B `q`), `d`. The tail (G) disagrees in every column (A `1 he ?triple-bar ?hook-x`,
B `?frac-1te ?triple-bar U L oo`) and is left out of the stream. `align1g/build_corrected.py` (--check exits 0) writes
`f78_corrected.txt` (11 lines; all 408 Bourdeau tokens kept, 44 inserted, grade C-transcription 34, M 10, marked `/C+`
`/M+`) and `f78_corrected_stream.txt`.

**U3, known-answer control on the corrected passage: 11/20 against the 16/20 gate -- FAIL.** Fresh seed **7806**
(`align1g/make_masked.py control 7806`, same density-matched rule: 20 of the H codes with <= 11 occurrences; 98 of 495 H
tokens hidden; bMAT1E's seed 1586 hid 103 of 470). One blinded Opus subagent saw only masked_control.txt and the two
cribs (copied to a scratch folder, no repo access), told that the last four f78 crib lines are two margin columns of
uncertain order. Scored by `align1g/score_control.py` (control_score.txt): correct X05 p, X06 o, X07 d, X09 p, X10 l,
X11 a, X12 b, X13 a, X17 d, X18 f, X19 qui; wrong X01 e->i, X02 e->a, X03 u->g, X04 a->s, X08 uous->b, X14 e->n,
X15 nostre->t, X16 l->u, X20 g->t. **H-confidence answers alone: 9/10** (the miss: X02 e read as a, H); M 2/5, L 0/5.
The aligner still could not tie f78.9-11 to the crib, i.e. the restored lines did not make the tail of f.78v alignable,
most likely because the f.78v margin crib (two columns, not fetched: Gallica stopped in bMAT1F) is not in cipher order.

**Consequence.** Gate not met (11 < 16; bMAT1E 9/20 on Bourdeau's text), so the 17-U-sign target was not run and no U
meaning is committed; judge not re-run (nothing changed; last -1.371 vs shuffled -1.78). The 9/10 H-confidence figure is
the second seed in which the aligner's H answers were nearly all right (bMAT1E 7/7); pooled 16/17. That is now two seeds,
but the rule "commit only H-confidence answers" was still chosen after seeing bMAT1E; pre-registered here, it would need
a third seed before use on the target. Status stays `partial`.

**Next step (one line, not done).** Pre-register "H-confidence answers only, gate >= 90% correct with >= 8 H answers" and
run one more fresh seed; if it holds, run the U target and commit only its H-confidence answers at C; separately fetch
and transcribe the f.78v margin (two columns) to fix the crib order for f78.6-11.

## NEAR step (1h) (bMAT1H), 26 Sept 2026

Job: `.claude/briefs/runs/2026-09-26-lane-b9-mat1h.md`. Intake gate 08:18 UTC: `matignon-mayenne-1586: partial (line 1) --
edition/page or full-text-search citation found within 6 lines`, exit 0. No host touched. **Key, reading and grade counts
unchanged (H 10,074 / M 1,648 / U 1,272); no U meaning committed; judge not re-run (last -1.371 vs shuffled -1.78).**

**Pre-registered gate** (orchestrator, 08:17 UTC, commit fa0b429, before any run; setup committed c198a15 before answers):
on `align1h/f78_corrected_stream.txt` + Bourdeau's f79, same density-matched draw (20 of the H codes with <= 11 occurrences),
fresh seed **8620**; PASS iff n_high >= 8 and right_high >= ceil(0.9 x n_high). One blinded Opus subagent (scratch folder,
masked_control.txt + two cribs only) marked each answer H or L before scoring. Scorer `align1h/score_gate.py`, output
`align1h/control_score.txt`.

**Result: FAIL.** n_high = 8, right among high = 7 (need 8/8). The miss: X11 = code `x` (true e, 4 occurrences), answered
`a` at H from "places" (X10 X01 X11 c = p l a c: the aligner read the vowel as a where the cipher spells `plec`/`place`
with e). Overall k = 9/20 (record only; bMAT1E 9/20, bMAT1G 11/20). Drawn codes and passage counts: n 8, 13 6, 8 3, D 1, oo 9,
g 2, H 11, a 8, b 5, c 8, x 4, 24 2, w- 10, M 5, R 6, X 4, 26 2, lam 1, 3 2, he 1 (98 of 495 H tokens hidden). **Every H answer
was a code occurring 4+ times in the passage** (8, 6, 11, 8, 4, 10, 5, 6): the high-confidence answers are the frequent,
easy codes, while the 17 U target signs are mostly rare, so even a pass would have overstated what the rule can do on the
target. Pooled over three seeds, H answers are 23/25 right (7/7, 9/10, 7/8). That falls short of the pre-registered 90% on
this seed, and the aligner could still not anchor f78.8-10 and most of f79.1-3/6-7.

**What would settle the target now (next step, not done).** Hand alignment against the margin crib has now failed three
known-answer controls. Its high-confidence subset also missed the pre-registered gate on a fresh seed. The limit is not
the aligner: the crib order for f.78v lines 6-11 is unknown, because the last four lines of Bourdeau's `crib_f78.txt` are
two narrow margin columns and their reading order was never checked on the leaf. The f.79r lines 1-3 and 6-7 also do not
anchor. The step that can move this is image work: fetch the f.78v and f.79r margin decipherment as native Gallica crops
(ark btv1b9061879d, canvas 85; bMAT1F's margin fetch at 600,2150,800,2500 was reset twice). Then transcribe it line by
line with its position against the cipher lines, fix the crib order, and only then rerun a fresh-seed control against a
new pre-registered gate. Failing that, a period key for this Matignon/Mayenne 1586 correspondence not yet located (sibling
letters in fr.15571 or the Matignon papers) would give H meanings for the 17 U signs directly. Status stays `partial`.

SO lead prompt, 26 Sept 2026, QUEUE-FILL.

## Second-opinion leads (SO-MATIGNON-LEADS, 26 Sept 2026)

ChatGPT (GPT-6) second-opinion runner's answer to `second-opinions/PROMPT-chatgpt-leads.md`, landed verbatim at
`second-opinions/chatgpt-leads-2026-09-26.md` (PR 29). Every citation below is the runner's claim, unchecked by
this repository -- a lead to verify, never a fact:

- Key family: BnF français 3974, f. 24 -- catalogued "chiffrement et déchiffrement", a 29 Sept 1581 Villeroy-to-
  Nevers letter; the runner's own best concrete comparator for key-compatibility testing. Unchecked.
- Sibling with decipherment: the same français 3974, f. 24 (and, as a poor-fit contrast, f. 83, Volta-to-Nevers
  in Italian, 8 Oct 1585). Unchecked.
- Edition: Jérémie Ferrer-Bartomeu's *"Allusions, silences et ellipses"* (in *Arcana Imperii*, 2019, pp. 67-85,
  p. 72 n.13) cites a 21 Aug 1586 Villeroy-to-Matignon letter at p. 222 of the 1749 *Lettres de Nicolas de
  Neufville ... écrites à Jacques de Matignon*. Unchecked -- the runner did not inspect the 1749 edition itself.
- Scholar: Jérémie Ferrer-Bartomeu, as above, a concrete person to ask about the 1749 edition's manuscript basis
  and any cipher tables. Unchecked.
- Weaker key leads: BnF français 3354 f. 91 (ciphered Henri III-to-Matignon letter, 3 Aug 1582, no decipherment
  reported) and français 16092 f. 5 (a cipher table among 1582-85 royal papers). Unchecked.
- Follow-on volume: BnF français 15573 (Aug-Dec 1586) lists further Forget/Mayenne/Matignon folios (ff. 7, 20,
  31, 62, 131, 299) as a defined next volume to inspect; the catalogue does not itself assert a cipher there.
  Unchecked.
- Correction noted by the runner: Henry & Loriquet's *Correspondance du duc de Mayenne* is a real Mayenne
  edition but covers 1590-91, outside this target's 1585-86 range -- not a check-solved lead, logged for the
  record. Unchecked.

Two most concrete: (1) français 3974 f. 24's catalogued cipher+decipherment pair as a key-compatibility control;
(2) Ferrer-Bartomeu's p. 222 citation in the 1749 Villeroy-Matignon *Lettres*, naming a scholar to ask.
No lead here is a printed decipherment of *this* target's own leaves; the runner found none. Not a check-solved
candidate on its own -- the 1749 edition citation is a secondary reference, not a claim the runner read it.

## MAT-3974 (26 Sept 2026)

Job: `.claude/briefs/runs/2026-09-26-parent-ytbiz-mat-3974.md`, testing SO-MATIGNON-LEADS lead (1): BnF français
3974 f. 24, catalogued "Lettre avec chiffrement et déchiffrement" of Nicolas de Neufville (Villeroy) to the duc
de Nevers, "De Fontainebleau, le XXIXe jour de septembre 1581" -- a known-answer cipher+decipherment pair from
the same royal secretariat, five years earlier than the target. Intake gate re-checked: `matignon-mayenne-1586:
partial (line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0.

**Located.** Français 3974-3995 is "Collection Mémoires de la Ligue"; français 3974 itself is a recueil of
loose letters and pieces (archivesetmanuscrits.bnf.fr `ark:/12148/cc504266/cd0e243`, item 11 of the finding aid,
confirming the catalogue description and date verbatim). Digitised: yes, ark `btv1b9059407r` (found via Gallica
SRU `dc.source all "Français 3974"`, 1 hit; the broader `gallica all` and `dc.title` forms return 0 or 2,442
irrelevant hits -- use `dc.source` for this collection). 590 canvases, all labelled `NP` in the IIIF manifest
(`tools/gallica_folio.py --folio 24` correctly reports 0 labelled canvases and no answer) -- the volume's own
foliation (visible in ink on each recto, e.g. "24", "25") is not exposed as IIIF canvas labels, so the canvas
was found by eye: canvas 46 = f.21r ("21"), 48 = f.22r ("22"), 50 = f.23r ("23"), 52 = f.24r ("24"), matching a
plain 2-canvases-per-folio, no-offset run once past the volume's front matter. **f.24r = canvas 52, f.24v =
canvas 53** (confirmed independently by content: f.24r opens "29e de Sept.e 1581" / "Monseigneur, j'ay receu..."
and f.24v closes "...vostre bien humble et obeissant serviteur / faicte a Fontainebleau le..." with a signature
matching "de Neufville", i.e. Villeroy -- the letter the catalogue describes). F.25r is blank with a sealing-tape
remnant; f.25v is the outer address panel ("A Monseigneur / Monseigneur le duc de Nevers...") -- the whole item
(ff.24-25, a folded bifolium) is confirmed to be exactly this one letter, nothing more, before item 12 starts a
new letter at f.26.

**Crops (U1).** `tools/iiif_lines.py --ark btv1b9059407r --canvas 52 --out images/f3974 --prefix f24r --debug`
and the same for canvas 53/`f24v`: 33 lines (66 crops, 2 segments/line) on f24r, 18 lines (36 crops) on f24v;
debug overlays checked by eye, one crop per detected line-band, all well under 2500px. images/f3974/manifest.json
+2 `iiif_lines` entries. Two native reference pages fetched (src_*_f52_full.jpg, src_*_f53_full.jpg).

**Two blind passes (U2).** Two independent Sonnet subagents, each given only the 102 crop paths (no key, no
prior transcription, no context beyond "transcribe cipher signs vs. plain French, line by line"):
`passA_f3974.tsv`, `passB_f3974.tsv`. **Both passes independently classify every one of the 51 lines as `plain`
or `unclear` (blank/illegible spans); `cipher` = 0 and `mixed` = 0 in both files, on both f24r and f24v.** No
digit groups, no isolated code letters, no nomenclator-style tokens, no interlinear or marginal decipherment
gloss found anywhere by either pass. A grep of both TSVs for any digit character outside the "1581"/"XXe" date
line returns nothing. Word-level raw disagreement between the two passes' literal transcriptions of the (very
difficult) secretary hand is high (95.1% of 329 word positions, by naive position-matching) -- expected for two
blind reads of a hard hand and not the operative number here, since the thing that matters (cipher-or-plain
classification) is unanimous, not close, between the two passes.

**U3/U4 (alignment, the test): not applicable, and not run.** `interlinear_align.py` aligns a cipher-sign stream
to a facing plaintext span; with zero cipher tokens found on either imaged leaf, there is no sign stream to
align and no `key_f3974.tsv` to build (0 rows, not a small or ambiguous key -- an empty one). The shuffle-control
overlap test against `key.tsv` (U4) needs at least one shared sign to compute an agreement rate on; with 0 codes
recovered from f.24, shared-sign count is 0 by construction and the test cannot be run, let alone pass or fail
against its shuffle control. This is not the "disagree, retire cheaply" outcome the brief anticipated (which
assumed f.24 would yield *some* sign/value pairs) -- it is a step earlier: the digitised leaf the catalogue
names as "chiffrement et déchiffrement" is, as imaged, plain French prose throughout both recto and verso, with
no encipherment visible on the page at all.

**Verdict: lead retires -- undecidable from this leaf, not a key-family match or mismatch.** Two independent
blind Sonnet passes agree completely that BnF français 3974 f.24-25 (ff.24r/24v text, f.25r/25v blank + address
panel) carries no cipher content on the digitised image, contradicting the BnF finding aid's "chiffrement et
déchiffrement" description for this item as far as what is bound and imaged at this exact folio. Per CLAUDE.md
rule 2 (image over transcription), the image is trusted over the catalogue phrase here. No key file was built,
no code from `key.tsv` was tested, and no claim is made about whether the Matignon/Mayenne key family is shared
with this secretariat's -- the test could not start.

Three explanations were not chased further (out of this job's scope and cap): (a) the "chiffrement et
déchiffrement" pair the finding aid describes may be a different, un-digitised leaf mis-filed under this folio
range in the finding aid's own description; (b) the actual enciphered original may not survive, and what is
bound at f.24 is only the fair-copy plaintext the recipient's cabinet retained (in which case "déchiffrement"
describes the item's *history*, not what is imaged); (c) a rarer possibility, that the cipher is a genuine
nomenclator substituting only for a handful of proper nouns/sensitive terms so seamlessly that two blind
transcription passes read it as ordinary grammatical prose without flagging anything odd -- weighed unlikely
(no anomalous proper nouns, numerals, or stand-in words were flagged by either pass) but not disproved.

**Next step (not run, named per the brief): none recommended at cost within this lead.** français 3974 f.24 is
retired as a comparator for the target's 1,272 unkeyed (U) codes. If the Matignon/Mayenne key family is still
worth cross-checking against a sibling secretariat cipher, the SO-MATIGNON-LEADS runner's weaker leads (français
3354 f.91, "no decipherment reported" per its own catalogue note; français 16092 f.5, a cipher table with no
attested letter) would need the same locate-crop-blind-pass treatment before spending on alignment, and neither
is stronger than f.24 was expected to be. Status stays `partial` (NEAR.md row).

Requests this section: archivesetmanuscrits.bnf.fr 1; gallica.bnf.fr 1 SRU query + 1 manifest fetch + ~14 image
fetches (thumbnails/native page/canvas probes, >=1.5s apart, browser UA; 1 connection reset on canvas 54,
1 retry after a pause, succeeded). 2 Sonnet subagents (the two blind passes), no third pass needed (0%
cipher-classification disagreement, well under the one-tenth trigger). No credentials used.

## MAT-CCE (27 Sept 2026, parent worker MAT-CCE)

Job: `.claude/briefs/runs/2026-09-27-parent-ytbiz-mat-cce.md` (CRYPT-LASRY (d): Lasry's cross-cipher-error
diagnostic -- check each unkeyed code against every other key attested for the Mayenne/Forget/Matignon/Nevers/
Villeroy office cluster, code by code, before treating them as unrecoverable). No hosts, disk only. Intake gate
re-run at 00:44 UTC: `matignon-mayenne-1586: partial (line 1) -- edition/page or full-text-search citation found
within 6 lines`, exit 0.

**Count correction.** The brief and this file's own import section (above) name 23 unkeyed ("+"/U) codes from
Bourdeau's original key.json import. `key.tsv` as currently committed carries only **19** grade-U rows (`104,
15, 19, 23, 27, 33, 36, 44, 46, 49, 53, 54, 62, 68, 79, 88, BOX, hash, star`) -- codes `76, 82, 84, 98` now carry
value `*` at grade H (2 total occurrences in `reading_tokens.tsv`), resolved to a null/asterisk sign at some
point after import without this file's prose being updated. `awk` over `reading_tokens.tsv`'s own value column
confirms: value `?` (this target's rendering of an unkeyed code) totals exactly 1,272 occurrences over 19
distinct codes, matching every grade-count line already on file in this NOTES.md ("U 1,272" throughout) -- the
19-code set, not 23, is what those 1,272 tokens actually are. Per CLAUDE.md rule 3 (match the control's N to the
target's own N), the control below draws **N=19**, not 23.

**U1: the office cluster.** Rule used: every `KEY-OFFICES.tsv` row whose office/correspondents/years place it in
the French royal secretariat/Catholic League orbit of Mayenne, Nevers or Villeroy, 1592-1611 (Matignon itself has
no other key on file to compare against). Seven key files, five offices:
`ciphers/fr2751-dediou-mayenne/key_mayenne_1592-93_polyphonic.tsv` (14 codes, Mayenne/de Diou, 1592-93),
`ciphers/fr2751-dediou-mayenne/key_mayenne_1593_homophonic.tsv` (44 codes, same office, 1593),
`ciphers/fr3985-nevers-revol-1593/key.tsv` (361 codes, Nevers/Revol cipher no.60, 1593),
`ciphers/fr3986-nevers-revol-1593/key.tsv` (77 codes, same cipher no.60, Oct 1593),
`ciphers/fr3987-nevers-revol-1593/key.tsv` (77 codes, same cipher no.60, Nov 1593),
`ciphers/fr7129-villeroy-bongars-1604/keys/key_f274.tsv` (36 codes, Villeroy's office, cipher no.2, in use from
1594) and `ciphers/fr7129-villeroy-bongars-1604/keys/key_f275.tsv` (211 codes, Villeroy's office, Bongars cipher
no.3, 1604-1611) -- the last two stretch past the 1580-1600 window named in the brief's cluster description but
are the only Villeroy-office keys on file and the brief names Villeroy explicitly, so kept in, flagged. 819
pooled cluster (code, value) pairs total. **Normalisation**: codes are compared as literal strings (no visual
glyph alignment attempted -- none of these keys' source images are re-opened this job); values are split on `|`
the same way `key.tsv` itself encodes alternates, and classified into `letter` (single a-z), `word` (a small
fixed list of French function-word values recurring in these tables: nostre, tous, aussi, bien, il, que, qui,
car, nous, vous, point, pas, ainsi, parceque, lui, plustost, uous, gu), `null` (`null`/`+`/`*`/empty) or `other`
(everything else -- mostly multi-word nomenclator glosses in `key_f275.tsv`, e.g. "hommes de pied", "Jesuites").
Several cluster codes are themselves the same kind of ASCII glyph-stand-in tag Bourdeau's own `key.tsv` uses
(`4+`, `T=`, `S6` in the target vs `+`, `++`, `2+`, `4+`, `8+`, `d+`... in the Nevers no.60 tables) -- these are
each transcriber's/tool's own naming convention for an unrelated period glyph, not evidence the underlying signs
are the same; this is exactly the coincidence the control below is built to catch.

**U2: control first (rule 3).** 20 seeds, `random.Random(seed).sample` of N=19 codes drawn without replacement
from the 68 non-U (keyed) rows of `key.tsv`, values hidden, same code-by-code literal lookup run against the
seven cluster keys.

| statistic | mean over 20 seeds |
|---|---|
| any-lookup-hit rate (code string found in >=1 cluster key) | 0.829 |
| exact-value recovery (found value matches the true value) | **0.042** |
| class recovery (found value's class matches the true value's class) | 0.411 |
| wrong-assignment rate (found value disagrees with truth, wrong class) | 0.571 |

Chance baselines from the pooled cluster keys' own value distribution (819 (code,value) pairs, `letter` 337 /
`other` 502 / `null` 6 / `word` 31): modal **class** share (`other`) = 0.573 -- class recovery (0.411) sits
*below* this, i.e. worse than always guessing "other". Modal single **value** share (876 pooled value tokens
after `|`-splitting; the commonest single letters `s`/`a`/`n` each ~2.5-2.9%) = **0.0285** -- the fairer
comparator for exact-value recovery, since "exact recovery at chance" (brief's phrasing) means recovering the
literal value, not the broad class. Observed exact recovery (0.042, ~0.8 of 19 codes/seed) is not distinguishable
from this 0.0285 baseline: expected hits under the baseline over 380 total draws (20 seeds x 19) is ~10.8,
observed is ~16, a gap of about 1.6 standard deviations (binomial sigma ~3.2) -- noise, not signal. The 0.571
wrong-assignment rate means that on the rare occasion a cluster key does carry the literal code string, it is
usually attached to the wrong meaning, consistent with the codes being independently-chosen ASCII tags rather
than a shared inherited table.

**Verdict: NO POWER on this cluster.** Exact-value recovery (4.2%) is at chance (2.85%) and class recovery
(41.1%) is below its own chance baseline (57.3%); the literal-code-string lookup carries no cross-cipher-error
signal for this office cluster at this N. Per the brief, U3 (the 19-code target lookup written up as
`mat_cce.tsv` M-grade candidates in HYPOTHESES.md) does not run: a lookup method that cannot recover a known
value above chance on this cluster's own keys cannot license a candidate value for an unknown one. The 19
unkeyed codes' literal-string hits against the cluster keys were computed (in scratchpad, not committed) purely
to confirm the same pattern holds there (a similarly high any-hit rate with no interpretable convergence -- e.g.
code `53` hits `nu` in the Nevers no.60 table and, separately, `Jesuites` in `key_f275.tsv`, two mutually
exclusive nomenclator glosses from unrelated offices, the wrong-assignment shape the control predicts) -- not
reported as candidates.

**Grade counts unchanged:** H 10,074 / S 0 / M 1,648 / U 1,272 (C 0, I 0). `key.tsv` and `exceptions.tsv`
untouched; `tools/decode_key.py ciphers/matignon-mayenne-1586 --check` not re-run (no key/reading change to
verify). **Status stays `partial`** (rule 5); the residue stays unkeyed and NEAR.md's "what would settle it" is
unchanged from the MAT-3974 entry above -- this test retires the Lasry cross-cipher-error lead (CRYPT-LASRY (d))
the same way MAT-3974 retired the français 3974 f.24 lead: a named, control-backed non-test, not a further open
question on the same method. No new host requests (disk-only job). No candidates, no "solved"/"new"/"first".

## GAPS-matignon-mayenne-1586 (2 Oct 2026, account-4)

Brief: `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`; the Verdict step of "Remaining gaps (1 Oct 2026)" below,
run disk-only (0 vision calls). Two scripts committed, both seeded and `--check`-able (rule 7): `align_openings.py`
(Tomokiyo's published openings aligned to the straight-substitution decode, within-line token-shuffle control) and
`judge_leaves.py` (each leaf judged alone against its own within-line letter-shuffle control, the spec's fr16 judge).
Outputs in `openings/` (`openings_alignment.tsv`, `openings_summary.json`, `leaf_judge.tsv`). No token regraded, no
value committed, `tools/decode_key.py --check` exit 0 unchanged (H 10,074 / M 1,648 / U 1,272).

**(a) Opening alignment.** Plaintext: Tomokiyo's four openings verbatim from `sources/cryptiana/web/henryiii.htm`
l.628-631 (the live page, read 2 Oct 2026 01:58 UTC, is identical in this section), u/v and i/j folded, his bare
numbers (49, 76) kept as code items that only the same cipher token can consume. DP as `align_crib.py` (bMAT1D):
H token +4 agree / -5 disagree, M token +2 in-set / -4 out, U token 0 (unscored, consumes a letter), null -2,
plaintext skip -4, both ends free; the first 1-5 lines of each leaf taken so the tokens cover the opening with slack.
Control: tokens shuffled within each line, 200 draws, seed 1; the statistic (best path score) depends on token order
against the fixed plaintext, so the control can differ from the target (rule 3's axis check: yes).

| leaf (lines taken) | tokens / plaintext items | real score | shuffle max / p95 / median | path ops |
|---|---|---|---|---|
| f143r (1-5) | 169 / 133 | **468** | -67 / -104 / -128 | agree 92, in-set 21, word 5 (12, 14, 13, 47), code 2 (49, 76), null 3, DISAGREE 0 |
| f154 (1) | 45 / 23 | **66** | 20 / 4 / -16 | agree 12, word 2 (14, 25), in-set 2, out-of-set 1 (f=c\|u on p), null 3 (the opening `4+ g g` before "en quelle") |
| f110 (1-2) | 119 / 65 | **33** | -22 / -39 / -58 | agree 32, in-set 5, DISAGREE 15, out-of-set 1, U-on-letter 11, null 11, plaintext skipped 13 |
| f150 (1-2) | 73 / 38 | -50 | -19 / -31 / -49 | agree 16, DISAGREE 12, null 11: **below the control max**, not aligned (reproduces the gap-3 scratch number) |

f143r and f154 read Tomokiyo's openings essentially token for token under Bourdeau's key (f143r: 92 H agreements, 0
disagreements over 133 plaintext items; "s'estant" is `J x d m a .v. Z` after three unread opening tokens `4+ 49 T=`,
which Bourdeau's HEAD reads "m'estant"). f110 beats its control (33 vs max -22 over 200) but the path is
fragmentary: 15 H disagreements and 13 skipped plaintext letters in 65. f150's opening does not align (gap 3 stands).

**Tabulation of U labels and disagreeing H codes** (pooled over the three leaves above their control max): only 11 U
tokens fall on a plaintext letter at all, every one on f110 (f143r's first five lines carry no U sign but 49; f154-1
none), so the tabulation the gap asked for has no power with this material -- BOX n=4: a 2, u 1, e 1 (top share 0.50 vs
0.40 mean top share over the shuffles); z n=3: i, o, s (0.33 vs 0.51); w->d, U->e, T->r, p->b once each (n=1, no
control possible). The gap-2 note's "by eye, BOX, U and T fall on u, e, r" is 1 of 4 for BOX and n=1 for U and T.
H disagreements, all on f110: `8=g` 0 agree / 4 disagree (falls on u 2, e, i), `o=i` 8/3 (a 2, s), `e=r` 4/3 (s, q, f),
`w-=d` 4/1 (u), `x=e` 7/1 (l), `n=l` 7/1 (m), `q=u` 1/1, `Ze=t` 1/1. **Verdict for the step: the openings are
too short and too U-poor to tabulate the absent labels -- untestable by this instrument with this material; a
non-result, not a negative, and no value is read off (rule 4: M at most, n 1-4).** The one lead is `8` on f110,
which never reads g where Tomokiyo has text (4/4), while Bourdeau's own HEAD table keeps "8, ▽, y -> g" -- f110's
hand or transcription (his gap: "internally inconsistent", exemplar set for this hand not built), not the key.

**(b) Per-leaf judge.** `judge_leaves.py`: letters per line as `reading_letters.txt` builds them (M first alternative,
U and name codes dropped), scored by the spec's fr16 judge model (`tools/judge_plaintext.py` NgramModel, same corpus,
same `controls()` call for real_p05/null_p99 at each leaf's N); control: the leaf's own letters shuffled within each
line, 20 seeds (the 4-gram statistic depends on letter order, so the control can differ; rule 3). Pooled reading for
reference: -1.371 (bMAT).

| leaf | lines | N | score | cover | real_p05 | null_p99 | own shuffle mean / max | gate |
|---|---|---|---|---|---|---|---|---|
| f110 | 37 | 1190 | -1.701 | 0.704 | -0.865 | -1.888 | -1.780 / -1.737 | FAIL |
| f123r | 36 | 987 | -1.699 | 0.720 | -0.879 | -1.878 | -1.967 / -1.894 | FAIL |
| f123v | 41 | 1181 | -1.395 | 0.802 | -0.869 | -1.891 | -1.922 / -1.857 | FAIL |
| f124r | 35 | 1136 | -1.448 | 0.794 | -0.883 | -1.882 | -1.890 / -1.831 | FAIL |
| f124v | 22 | 661 | -1.463 | 0.808 | -0.869 | -1.879 | -1.887 / -1.797 | FAIL |
| f143r | 21 | 776 | -1.279 | 0.830 | -0.881 | -1.878 | -1.929 / -1.845 | FAIL |
| f143v | 33 | 1261 | -1.158 | 0.858 | -0.859 | -1.912 | -1.884 / -1.810 | FAIL |
| f150 | 13 | 467 | -1.187 | 0.867 | -0.893 | -1.877 | -1.899 / -1.809 | FAIL |
| f154 | 28 | 1134 | -1.189 | 0.866 | -0.872 | -1.879 | -1.886 / -1.832 | FAIL |
| f173 | 33 | 1136 | -1.240 | 0.845 | -0.883 | -1.882 | -1.896 / -1.846 | FAIL |
| f196 | 26 | 884 | -1.293 | 0.854 | -0.877 | -1.888 | -1.889 / -1.825 | FAIL |
| f201 | 30 | 1033 | -1.245 | 0.857 | -0.885 | -1.899 | -1.894 / -1.806 | FAIL |
| fr.15571 f.177 | 24 | 639 | -1.472 | 0.801 | -0.889 | -1.883 | -1.879 / -1.816 | FAIL |

Every leaf FAILs the fr16 gate (real_p05 -0.86 to -0.89) and every leaf scores above its own shuffle max, but the
margins split the leaves cleanly: the seven leaves of gap 1 (f143r/v, 150, 154, 173, 196, 201) sit at -1.158 to
-1.293, about 0.55-0.65 above their shuffles; the six of gap 2 at -1.395 to -1.701, and **f110 at -1.701 is 0.036 above
its shuffle max with a shuffle spread of 0.08 -- at the noise level, the decode of f110 is not distinguishable from
shuffled letters.** That matches Bourdeau's "~0% read" for f110 and the `8=g` disagreement in (a): f110 is a
transcription or hand problem before it is a key problem.

**Web and blog check** (the intake gate exited 1 only for the missing CHECK-SOLVED-WEB section): run first, 0 hits
carrying a decipherment or plaintext of any of these leaves; full log at the end of this file. Bourdeau's HEAD NOTES.md
(`targets/matignon1586/`, fetched 01:58 UTC, snapshot `sources/cyphersolver/2026-10-02/matignon1586/NOTES.md`) is a
partial modern reading already cited here (status "in progress, 28% read"), not a found-solved; its glyph table now
lists ⊐ (box) and ꝉ (crossed t) as u/v, ₸ (crossed 4) as m, ƀ as i/j, Ƶe as t, ʰe as l, ʄʄ as n, ɣɣ as ss -- our
`key.tsv` (his key.json at fc0c9e8) still has BOX as '+' and no row for our T, 4, w, z, U labels, so his HEAD key may
carry values ours lacks. Whether our ASCII labels are those glyphs is not established here; it is the named next step.

Suggestion (one line, Usage 7): fetch his HEAD `key.json` and the 13 transcription files (raw.githubusercontent.com,
about 15 requests), diff label by label against `key.tsv`/`ciphertext.txt`, and re-run `judge_leaves.py` with any new
single-letter values applied as a hypothesis (published key, credited, grade M) against the same shuffle control.

## GAPS2-matignon-mayenne-1586 (2 Oct 2026, account-4)

Brief: `.claude/briefs/runs/2026-10-02-account4-gaps-step.md`; the Verdict step of "Remaining gaps (1 Oct 2026)" as
rewritten at 02:10 UTC: fetch Bourdeau's HEAD `key.json` and 13 transcriptions, diff label by label, apply any new
single-letter value as a credited M hypothesis, re-judge per leaf. Disk otherwise, 0 vision calls, 0 subagents. Intake gate
exit 0 before the step. Credit: Daniel Bourdeau, `dbourdeau/cyphersolver` `targets/matignon1586/`, HEAD
`34e0fc8981112070c6b8b718519eeed6dca3a7ee` at fetch time (03:36 UTC, 14 requests to raw.githubusercontent.com, all 200,
1.6 s apart; 1 `git ls-remote` to github.com for the id), code MIT / text CC BY 4.0; snapshot unmodified in
`sources/cyphersolver/2026-10-02/matignon1586/` (COMMIT file there).

**(a) Diff, `bourdeau_head_diff.py` (`--check`-able, output `openings/bourdeau_head_diff.json`).** His HEAD `key.json` has
87 rows: 0 added, 0 removed, 0 changed against `key.tsv` (his fc0c9e8 key.json) -- the key has not moved since 25 Sept 2026.
The 13 transcription files are token-identical to `ciphertext.txt` leaf by leaf (12,994 tokens, 379 lines; f110 37 lines /
1,699, f123r 36 / 1,097, f123v 41 / 1,251, f124r 35 / 1,203, f124v 22 / 727, f143r 21 / 724, f143v 33 / 1,182, f150 13 / 445,
f154 28 / 1,061, f173 33 / 1,082, f196 26 / 840, f201 30 / 987, fr.15571 f.177 24 / 696). No label in our ciphertext is
keyed at his HEAD and not in ours; the 31 absent labels (U 343, z 296, 4 106, w 83, T 53, ...) are unkeyed in both. So
**his HEAD key carries no new single-letter value**: the glyph-table values the 02:10 step read in his NOTES.md (⊐ box
and ꝉ crossed-t = u/v, ₸ crossed-4 = m, ƀ = i/j) are his table's, not his key's -- `key.json` keeps `BOX` as `+`, `4+` is
already m in both keys (so ₸ = `4+`, and plain `4` x106 stays unkeyed in both), and no label of his maps to ƀ or ꝉ by name.
Whether our ASCII `T` (53) is his ꝉ is not established (`T=` is m/mm in both keys).

**(b) Hypothesis test, `hypothesis_judge.py` (`--check`-able; `openings/hypothesis_judge.tsv`, `_summary.tsv`).** BOX = u
(his table, u/v folded) and T = u (label identity a guess) applied to the straight-substitution letters, per leaf with >= 5
occurrences and pooled, scored by the spec's fr16 judge; control: the same label set to each of the other 19 letters of the
key's alphabet at the same positions and N (the statistic depends on which letter is inserted, so the control can differ
from the target -- rule 3 axis check: yes). Grade: M hypothesis at most (rule 4), his key does not carry it.

| label (value) | leaf | n | score with value | rank of value / 20 | best letter / score | spread of the other 19 (max..min) |
|---|---|---|---|---|---|---|
| BOX (u) | f110 | 125 | -1.756 | 10 | i -1.624 | -1.624 .. -1.954 |
| BOX (u) | ALL | 137 | -1.380 | 9 | i -1.367 | -1.367 .. -1.405 |
| T (u) | f110 | 38 | -1.733 | 14 | i -1.680 | -1.680 .. -1.785 |
| T (u) | f124r | 8 | -1.458 | 13 | e -1.444 | -1.444 .. -1.465 |
| T (u) | ALL | 53 | -1.377 | 14 | l -1.369 | -1.369 .. -1.383 |

Neither value ranks first anywhere. But 125 of 137 BOX tokens and 38 of 53 T tokens sit on f110, the leaf whose decode the
02:10 per-leaf judge put at its own shuffle level (-1.701 vs shuffle max -1.737), so before reading this as a negative the
instrument's power was checked where the tokens are.

**(c) Known-answer power control (`openings/hypothesis_power.tsv`).** The same ranking run on every H-graded single-letter
label with >= 20 occurrences on a leaf, its true value hidden: does the instrument put the true letter first?

| leaf | labels tested | true value rank 1 | median rank | note |
|---|---|---|---|---|
| f143v | 17 | 15 | 1 | misses: q=u rank 9 (best s), s=u rank 2 |
| f154 | 16 | 15 | 1 | miss: q=u rank 9 (best s) |
| f123r | 13 | 5 | 3 | 4+=m rank 13, q=u rank 5 |
| f110 | 10 | 1 | 5 | e=r rank 7, H=o rank 14, q=u rank 8; only h=e recovered |

On the leaves that read (f143v, f154) the instrument recovers the true letter for 15 of 17 and 15 of 16 keyed labels; on f110
it recovers 1 of 10 (median rank 5), so **on f110 the ranking of BOX=u (10th) and T=u (14th) is a non-test, not a negative**
(rule 3: a control that fails at the target's own N cannot license a negative). The pooled rows are dominated by f110's
tokens (91% of BOX, 72% of T) and inherit that. Outside f110, BOX has 1-3 tokens per leaf and T 8 at most -- too few to
rank. Verdict for the step: **no new value in Bourdeau's HEAD key; his table's box = u/v (and the crossed-t guess for our
T) is untestable by this instrument on this material; no value committed, no token regraded; H 10,074 / M 1,648 / U 1,272,
`tools/decode_key.py --check` exit 0, pooled judge unchanged (FAIL -1.371 / cover 0.814 vs real_p05 -0.837), per-leaf
`judge_leaves.py --check` current.** The one thing that can test it is the f.110 image (gap 2's crop step), where BOX and
T live: the power check says f110's letters around them are themselves at shuffle level, i.e. a transcription problem first,
as Bourdeau's own "f. 110 ... internally inconsistent" says.

Side observation for the record (not acted on, Usage 7): under this instrument `q` (key value u, grade H) ranks 9th on both
f143v and f154 with `s` the best letter each time, and 5th on f123r, 8th on f110 -- the only H label to miss on every leaf
tested; Bourdeau's table lists ʃ/s/Ɋ as u/v and ʃ (long s) also as c, so `q` may be a long-s/c-like shape rather than u.
A later step could test q = s|c against the same per-letter control on f143v/f154 where the instrument has power, ~$1.

**(d) Gap 3 extent, from the same read (his HEAD "Coverage, measured", 22 Sept 2026).** Lines transcribed / on leaf: f110 37 /
54, f196 26 / 31 (untranscribed: the part-line after *auquel*, full lines 1-3 and 13), fr.15571 f.177 24 / 29; every other
Cipher-1 leaf complete (f123r 36, f123v 41, f124r 35, f124v 22, f143r 21, f143v 33, f150 13, f154 28, f173 33, f201 30).
His estimate of the untranscribed remainder: f110 +781, f196 +162, f177 +145 tokens (30 a line), Cipher-3 f.276 ~27 lines
(+810 est.) and fr.15571 f.179 ~25 lines (+750 est.): 12,994 transcribed of ~15,642 (+2,648 est.). These are his counts,
checked on his images, not ours; the Gallica line count named in gap 3 is still unrun.

Requests this step: raw.githubusercontent.com 14 (all 200), github.com 1 (`ls-remote`); no other host; vision 0.

## GAPS-matignon-mayenne-1586 gap 1 (3 Oct 2026, account-4)

Verdict step run: bMATBEAM's beam, M-only, per leaf, on the seven read-leaves (ff.143r, 143v, 150, 154, 173, 196, 201),
U held fixed as a placeholder (`TOK`), behind gates pre-registered and pushed before any scoring
(`mu_leaf_beam_prereg.md`, commit bd74c69d). Script `mu_leaf_beam.py` (reuses `mu_beam.py` unchanged; deterministic;
`--check` exit 0), results `mu_leaf_beam.json`. Disk and CPU only, no hosts, 0 vision calls.

**Control (A), per leaf, at that leaf's own N (3 seeds, held-out catheri02 enciphered with the leaf's own structure):**

| leaf | M acc (ctl) | freq base | first-cand base | gate (a) | ctl judge gain, 3 seeds | its shuffle-null max | gate (c) |
|---|---|---|---|---|---|---|---|
| f143r | 0.889 | 0.544 | 0.636 | pass | .122 .110 .118 | .141 .107 .141 | 1/3 FAIL |
| f143v | 0.847 | 0.573 | 0.691 | pass | .050 .044 .052 | .059 .083 .080 | 0/3 FAIL |
| f150 | 0.801 | 0.479 | 0.609 | pass | .103 .049 .014 | .109 .084 .106 | 0/3 FAIL |
| f154 | 0.805 | 0.447 | 0.676 | pass | .054 .080 .048 | .081 .087 .096 | 0/3 FAIL |
| f173 | 0.812 | 0.492 | 0.732 | pass | .034 .040 .043 | .074 .086 .067 | 0/3 FAIL |
| f196 | 0.757 | 0.465 | 0.545 | pass | .034 .077 .144 | .066 .083 .107 | 1/3 FAIL |
| f201 | 0.818 | 0.393 | 0.513 | pass | .139 .127 .122 | .108 .105 .110 | 3/3 pass |

Rule-3 checks: no baseline near ceiling (first-candidate 0.51-0.73, frequency 0.39-0.57: gate (b) passes everywhere),
and the beam does read M on known-answer text at every leaf's N (0.76-0.89, +29 to +42 points over the frequency
baseline: gate (a) passes everywhere). But the pre-registered *instrument* -- judge gain over a 20-draw within-line
shuffle null -- has no power at this N: on known-answer text the beam's gain beats its own shuffle null on only 5 of
21 control seeds, because the beam's LM (catheri01) is the judge's corpus, so it raises the judge score on shuffled
text about as much as on real text. Testable leaves: **1 of 7** (f201) against a pre-registered minimum of 4, so the
step is **"non-test at this N"** by the prereg's own stop rule: the beam is neither licensed nor retired by it.
For the record only (not a test of the step): on f201, the one testable leaf, the target gain is +0.029 (judge
-1.245 -> -1.216, 58 M choices changed) against a shuffle-null max of +0.078 and mean +0.048 -- below its own null.
Nothing committed to key.tsv/exceptions.tsv; grades unchanged H 10,074 / M 1,648 / U 1,272; judge unchanged -1.371.

Lesson for whoever tries again: a judge-gain gate cannot test an LM-driven choice when the LM and the judge share a
corpus -- the control's gain sits in its own null. A different instrument is needed (an LM disjoint from the judge's
corpus, or a reference reading), not a re-tuned threshold (rule 3, third-attempt clause).

## GAPS2-matignon-mayenne-1586 (3 Oct 2026, account-4): beam M choices vs Bourdeau's per-line readings

Verdict step run: the per-leaf M-only beam (`mu_leaf_beam.py`, unchanged) scored against a reference not built from
catheri01 -- Bourdeau's per-line decoder output (dbourdeau/cyphersolver HEAD 4d32ec9, MIT; his LM is Berger de
Xivrey's Lettres missives de Henri IV, `mklm.py`), snapshot `sources/cyphersolver/2026-10-03/matignon1586/`. Gate
pre-registered and pushed before scoring (`mu_leaf_agree_prereg.md`, c26ff40d). Script `mu_leaf_agree.py`
(deterministic, `--check` exit 0), results `mu_leaf_agree.json`. Scope: the 4 leaves where he has a per-line output
with line counts equal to ours (f143r 21, f143v 33, f154 28, f173 33); ff.150/196/201 have only prose summaries with
ellipses and cannot be aligned per token (deviation from the Verdict line's file list, stated in the prereg).
Normalisation (PX-BRODEC): accents off, lower case, v->u, j->i, w->u, k->c, non-letters dropped, both sides.
Statistic: per line Levenshtein alignment; an M token agrees iff every letter of its chosen alternative aligns to an
identical letter. Null: 20 within-line shuffles, beam run on the shuffled line, choices mapped back and rendered in the
original order (null choices differ from the beam's on 37-53 M tokens minimum per leaf, so the null can differ on the
statistic -- caveat c). Disk and CPU only, 0 hosts besides one github.com clone, 0 vision calls.

| leaf | M n | ctl power (beam vs null max, truth ref, 3 seeds) | A beam | A first | A null max (mean) | PASS |
|---|---|---|---|---|---|---|
| f143r | 120 | .912/.667 .847/.667 .907/.597 (3/3) | 0.850 | 0.625 | 0.642 (0.588) | yes |
| f143v | 143 | .841/.731 .886/.631 .812/.613 (3/3) | 0.797 | 0.692 | 0.657 (0.598) | yes |
| f154 | 103 | .727/.578 .805/.558 .883/.586 (3/3) | 0.748 | 0.689 | 0.592 (0.528) | yes |
| f173 | 100 | .736/.629 .833/.604 .867/.619 (3/3) | 0.780 | 0.720 | 0.680 (0.601) | yes |

Verdict by the prereg: **AGREEMENT SIGNAL**, 4/4 leaves testable, 4/4 PASS (gate: beam > null max and >= first + 0.02;
margins over first +0.225, +0.105, +0.059, +0.060). Read with rule 3 caveat (a): this is agreement between two
LM-assisted readings through the same key (his key = our key.tsv), with disjoint LM corpora -- not accuracy. Two
limits on what it licenses: on f154 and f173 the control's beam fell below the first-candidate baseline on seed 1
(0.727 vs 0.747; 0.736 vs 0.780), so the beam's own edge over "take the first value" is not uniform at this N; and the
shuffled-context null sits below the first-candidate arm, so the null max is the weaker bar and the +0.02 over first
is the binding one. Nothing committed to key.tsv/exceptions.tsv; grades unchanged H 10,074 / M 1,648 / U 1,272. The
prereg licenses only a separate commit-and-judge step with its own control: the beam's M choices on these 4 leaves
(167 changed from first) committed as S candidates and re-judged per leaf against `judge_leaves.py`'s shuffle
controls, with the bMAT1C reversal (-1.545) as the precedent to beat.

## GAPS3-matignon-mayenne-1586 (3 Oct 2026, account-4): beam M choices as S candidates, re-judged per leaf

Verdict step run: the per-leaf beam's M choices (`mu_leaf_beam.beam`, unchanged; 167 changed from first-candidate:
f143r 51, f143v 48, f154 37, f173 31) put into a scratch rendering of each of the 4 leaves and re-judged with the
spec's fr16 model against `judge_leaves.py`'s 20-draw within-line letter shuffle. Gate pre-registered and pushed
before scoring (`mu_scommit_prereg.md`, 0b58589a), including a rule-3 clause: the rise must also beat the same beam's
rise on 20 within-line token shuffles of the leaf (the beam's LM and the judge share catheri01, so G1 can hold by
construction). Script `mu_scommit.py` (deterministic, `--check` exit 0), results `mu_scommit.json`. Disk/CPU only,
0 hosts, 0 vision calls. Baseline scores reproduce `openings/leaf_judge.tsv` exactly.

| leaf | judge first | judge scratch | rise | letter-shuffle max | G1 | G2 | shuffled-target rise max (mean) | P1 | known-answer gain power |
|---|---|---|---|---|---|---|---|---|---|
| f143r | -1.279 | -1.136 | +0.144 | -1.884 | yes | yes | +0.124 (+0.068) | yes | 1/3 |
| f143v | -1.158 | -1.147 | +0.011 | -1.859 | yes | yes | +0.057 (+0.032) | no | 0/3 |
| f154 | -1.189 | -1.178 | +0.011 | -1.852 | yes | yes | +0.055 (+0.031) | no | 0/3 |
| f173 | -1.240 | -1.239 | +0.001 | -1.873 | yes | yes | +0.053 (+0.028) | no | 0/3 |

Verdict by the prereg: **NON-TEST** -- the Verdict line's own two conditions pass 4/4 (every leaf rises, every leaf
stays far above its letter-shuffle max), but those conditions cannot fail here: the letter-shuffle floor sits ~0.6
below any decoded text, and on 3 of 4 leaves the beam raises the judge *less* on the real leaf than on its own
token-shuffled copy (rise +0.001 to +0.011 vs shuffled-target max +0.053 to +0.057, and below even the shuffled mean).
Only f143r's rise (+0.144) beats its shuffled-target max (+0.124), by 0.02, on a leaf whose known-answer gain power is
1/3 seeds. Nothing committed to key.tsv/exceptions.tsv/the reading; no S grade assigned; grades unchanged H 10,074 /
M 1,648 / U 1,272; judge unchanged -1.371. This was the beam's third judge-scored attempt on the target (bMAT1C,
GAPS gap 1, GAPS3): the judge-based commit of this beam is [retired] for this target (rule 3 third-attempt clause),
"untested-by-this-tool", not refuted. The GAPS2 agreement with Bourdeau's per-line readings stands as recorded
(agreement, not accuracy); turning it into graded values needs a reference that is not an LM -- a period gloss or
clear page on a Cipher-1 leaf (gap 4's f.91-92 margin or the f.18/f.19 pair), not another judge.

## R7-MATSORT (6 Oct 2026, account-2 worker, LANE LANE-RUN7-account-2): f.110 sign sorter seeded for the owner
Built from the D2B-MATF110 line crops on disk (no request, no vision call): `sorter/` (build_inputs.py, build.sh,
signs.tsv, labels.tsv, focus.tsv, fit.tsv, pages/, README.md). 318 tiles from f.110 image lines 1-6 (284 fitted to
ciphertext.txt f110-1..5, 34 unplaced on image line 3), 39 piles by the existing shape labels, 54 "check these first" tiles
(BOX 17, z 20, T 5, U 5, w 4, 4 3) carrying pass A / pass B's readings. Not published; the lane orchestrator files the
ASKS row. No key, ciphertext or reading change; status stays partial, NEAR.md row unchanged. Limits in sorter/README.md
(52 px strips, approximate tiles).

## R8-MATCUT (6 Oct 2026, account-2 worker, LANE LANE-RUN8-account-2): f.110 sorter re-cut on the written lines

The R7-MATSORT sorter (`sorter/`, ASKS 146) is re-cut with `tools/sorter_recut.py` on five deskewed strips that follow the
written lines (`sorter/recut.py`, one Gallica request for the native region, `sorter/region.jpg`): 333 tiles, starting
piles from Bourdeau's labels by a shape-EM alignment (232/274 tokens placed), `build.sh` now passes `--region`.
`tools/sorter_preflight.py` PASS (shape flags 4.2% of 5%); on its 24-tile contact sheet 22/24 tiles hold one whole sign on
the right line and about 15/24 start in the transcription's pile (sorter/README.md, "Re-cut"). Layout observation (grade I,
no reading change): at the right edge Bourdeau's f110-1..3 tails sit on the rising ends of written lines 2..4, and the right
ends of written lines 1 and 5 match no transcribed line -- his line breaks there follow flat rows, not the written lines.
No reading, key or status change; NEAR.md row unchanged. Flagged in ROOM.md for the account-3 orchestrator to publish.

## MAT-F179 (9 Oct 2026, account-4 worker, LANE DEFAULT-account-4-20261009-1051)

Brief: `.claude/briefs/runs/2026-10-09-account4-default-1051-jobs.md` J1. Times by `date -u`: 11:03-11:16 UTC. No Gallica call (403).

**Prior-work step** (`tools/prior_work.py matignon-mayenne-1586 --item-spec 'shelfmark=BnF fr.15571;folio=179;sender=Matignon' --step-type decode --fetch`, origin/main 324111b91, 11:06 UTC): exit 2, verdict plaintext KNOWN (Tomokiyo henryiii.htm: f.179 "uses Matignon's Cipher-3 ..., which allows deciphering (see the image)"), step LEAD (NOTES.md:345, a logged web query string, not a done marker). Recorded in `prior-work.tsv`: the 1-own LEAD as CLEAR, the Tomokiyo row as KNOWN (his composite carries modern per-sign letter labels and a few words, no printed running plaintext). So this decode is a key check against Tomokiyo's published table, not a reading; key source `published` (S. Tomokiyo, cryptiana.web.fc2.com, credited). Other holds left as listed (LOOK 2-leaf, UNCHECKED-NET aaymeloglu and editions).

**(b) Nomenclature 76/82/84/98** (`decode_key.py --try`, HYPOTHESES.md row of this date): in `ciphertext.txt` only 76 occurs (x2: f143r-2, f196-7); 82, 84, 98 occur 0 times, so they are untestable on this transcription, not refuted. 76 = roydenauarre +25.0 bits over the current `*`, against the other three names at the same positions (princedeconde +20.7, uicontedeturenne -10.3, montauban -30.5). The tool could build no null at n=2 (verdict "undecided"). f143r-2 decodes "d v [76] d v qve l", the frame of Tomokiyo's paraphrase "partir du 76 duquel". **76 = le roy de Navarre held at grade M**; key.tsv not edited.

**(a) Cipher-3, fr.15571 f.179.**
- Table: `henryiii_Matignon3.png` fetched once from https://cryptiana.web.fc2.com/code/henryiii_Matignon3.png (9 Oct 2026 11:09 UTC, HTTP 200, 727x241 PNG, 79,947 bytes), kept in the worker's scratch, not committed. It is Tomokiyo's handwritten table: letter columns a-u and x, a word row (faire, de, la, le, pour, que, qui), and two boxes (n/t/u variants; u/que).
- Blind codes: the letter headers and word labels were masked, and each column, word cell and box cell was given a random code (seed 17926), so the readers could not see values. The code -> value map is `cipher3/code_key.tsv` (32 codes). The coded sheet image stays in scratch; it can be rebuilt from the PNG by whiting out y 0-21 (header), x 0-260 y 158-181 (word labels), x 440-515 y 66-88 and x 450-520 y 134-153 (box headers) and x>=525, then labelling the column centres (a 7, b 31, c 54, d 75, e 100, f 120, g 142, h 165, i 186, l 209, m 231, n 258, o 284, p 307, q 331, r 356, s 380, t 403, u 426, x 449; words faire 30, de 65, la 90, le 106, pour 157, que 197, qui 230) with the codes in `code_key.tsv`.
- Crops: `tools/iiif_lines.py --image ciphers/matignon-mayenne-1586/images/f179_gallica_native.jpg --out <scratch>/f179crops --region 440,800,1040,1040 --prefix f179 --deskew --debug` (and `--distance 34`, `--lines-per-crop 4`). The debug overlays show the line finder does not follow these slanted, crowded lines (30, then 18 bands for about 21 written lines). So the passes got five manual overlapping strips (PIL crop of x 440-1480, y 820-1075 / 1050-1275 / 1240-1455 / 1425-1625 / 1595-1860, 2x upscale, 2080 px wide), in scratch only.
- Two blind Sonnet passes, one call each, with the coded sheet and the five strips: `cipher3/passA_f179.tsv` (434 signs) and `cipher3/passB_f179.tsv` (512 signs), L1-L21. Both readers called their own output provisional. Pass A gives L4 and L5 identical, a reader error.
- `tools/reconcile_passes.py passA passB --no-write`: **agree 181/562 = 32.2%** (nw).
- Decode, matched control (`cipher3/decode_f179.py`, fr16 character model, log2 per letter, same transcription with the code -> value map permuted, 200 draws): pass A real -6.544 vs shuffled-key null mean -5.581, p95 -4.418, max -3.598; pass B real -7.284 vs mean -5.746, p95 -4.459, max -3.899. **Both FAIL; both sit below the null mean.** At this transcription quality Tomokiyo's table yields no French, which says the passes are noise, not that the table is wrong. The table is untested here.
- No reconciliation was run, and no `f179_reconciled.tsv` or reading was committed. The split is far above a tenth, and TRANSCRIPTION.md sends that to a person, not to a third machine pass. The limit is the image: `images/f179_gallica_native.jpg` is the 4300 px native region scaled to 1600 px (its manifest URL ends `/1600,/180/native.jpg`), so signs are about 20 px tall.
- Grades: no token graded; no f.179 value read.

Requests: cryptiana.web.fc2.com 1 (200). Gallica 0. Subagents: 2 Sonnet calls.
Suggestion (not run): when Gallica answers, refetch f187 at full width in tiles (two halves under 2500 px) and seed a sign-sorter page from the coded table before any further machine pass.

## MAT-NOM (15 Oct 2026, account-2 worker, LANE DEFAULT-A2-0509-15)

Brief: `.claude/briefs/runs/2026-10-15-ytbiz-default-0509-jobs.md` job MAT-NOM. Times by `date -u`: 05:30-05:4x UTC.

**Prior-work step** (`tools/prior_work.py matignon-mayenne-1586 --item-spec 'shelfmark=BnF fr.15572;folio=91-92;sender=Mayenne' --step-type crop --fetch`, origin/main 2f20acbe3, 05:3x UTC): exit 2, verdict plaintext KNOWN (Tomokiyo henryiii.htm l.640: "f.91-92 (deciphered in the margin)" -- the period margin decipherment, which is exactly what this step locates as a crib, not a reading of a target leaf); step LEAD (1-own: the lane orchestrator's own claim line of 05:16, target-level, not this item). Other holds as listed (LOOK 2-leaf, UNCHECKED-NET aaymeloglu and editions; check-solved bCSMAT covers the editions). Check 1 by hand: no earlier section of this file located or cropped ff.91-92 (Escalation "siblings" said "Not opened ... Planned").

**(a) Nomenclature 76/82/84/98.** Already run by MAT-F179 (9 Oct 2026, section above, HYPOTHESES.md row): 76 held at M (+25.0 bits, n=2, no null possible), 82/84/98 absent from `ciphertext.txt`. Not re-run (brief stop rule). `tools/design_prior.py ciphertext.txt --no-write` (offline, 12,994 tokens, 112 distinct): letter-for-letter excluded (d 1.37 vs envelope 0.32); mixed (partial table) plausible (d 1.11, null_p05 1.69); code plausible (d 1.47); multi-sign not above null (d 0.44 vs null_p05 0.39); shuffled-input false-positive rate 0.045; fine ranking advisory: syllabary 0.53, nomenclator 0.62, mixed 1.11, homophonic 1.21. Consistent with the period-verified key (letters with variants plus a numeric nomenclature); it changes no attack choice, since the key is already H.

**(b) f.91-92 Cipher-1 sibling located.** `tools/gallica_folio.py btv1b9061879d --iiif-host openapi --anchor 85=79r --anchor 116=110r --anchor 129=123r --anchor 150=143r --anchor 161=154r --folio 91` (cached manifest, 0 requests): fit canvas = 1.015 x folio + 4.52, residuals <= 0.42; estimate f97. Checked by eye on 1600 px overviews: **f.91r = canvas 97 right** (foliation "94 91", the lower number valid); **f.91v = canvas 98 left, f.92r = canvas 98 right** ("95 92"). Canvas 97 left is an address panel with a slip (not cipher). The letter: Mayenne to the King, "Sire, Je vous escrivis partant de Bouillac pour passer la Dordogne ...", closing "Du Camp de [?Saluiac] ... jour de Mars 1586", signed Charles de Lorraine (all M, read at 1600 px). It mentions Matignon in clear several times.

Six cipher blocks, each with a period decipherment written in the left margin beside it (extents and line counts in `f91/blocks.tsv`): A f.91r 4 lines; B f.91r 7; C f.91v 15; D f.91v 7; E f.92r 4-5; F f.92r 10 + 3 (two runs split by two clear lines). About **46-48 cipher lines** against about **71-75 margin lines** -- more than twice the f.78v/79r crib. Block F's second run carries "14 76" and its margin gloss ends "Et sault que le Roy de Navarre passa ..." (a lead for 76 = roi de Navarre at an independent occurrence, M, not aligned).

Crops: 2 native fetches (canvas 97 region 700,820,7360,4630 at max; canvas 98 full at max, 8722x6347), then 12 local `tools/iiif_lines.py --image ... --region ... --prefix f91r_glA ... --debug` runs, commands in `f91/regen_f91.sh` (re-run offline against the same two files: byte-identical crops, checked on two). 151 crops (cipher lines in 2 segments under 2500 px, gloss lines whole), listed with size and sha1 in `f91/crops_manifest.tsv`; images in the worker's scratch only, never committed. Debug overlays: the band finder found 13 of 15 lines in block C and 3 of 4-5 in gloss A (the slanted-hand failure bMAT1F and MAT-F179 saw); the next job should check every overlay and use manual overlapping strips where bands merge.

Not done (brief: transcription and alignment are a later job unless (a) left >= 50% of cap; the (b) half's transcription is ~47 cipher lines x 2 blind passes + ~74 gloss lines x 2 + a reconciliation, well above this cap): no transcription, no alignment, no grade, no key change.

Requests: openapi.bnf.fr 4 (2 overviews at 1600 px, 2 native), all 200; cryptiana 0. Subagents: 0.
Next (suggestion, not run): PREREG, then two blind passes of the 6 margin glosses (clear French, cheap) and of the 6 cipher blocks against `key.tsv`; then `tools/interlinear_align.py` per block, held out as a known-answer control for the H key before any use on f.110; ~$8-10 at ~1.0 per Opus vision call (one block per call).

## MAT-F91 (15 Oct 2026, account-2 worker, LANE DEFAULT-A2-0509-15)

Brief: `.claude/briefs/runs/2026-10-15-ytbiz-default-0509-jobs.md` job MAT-F91 (blocks A, B, D, E of f.91r-92r). Times by `date -u`: 05:48-06:0x UTC.
Prior-work: `tools/prior_work.py ... --item-spec 'shelfmark=BnF fr.15572;folio=91-92;sender=Mayenne' --step-type transcribe` exit 2, plaintext KNOWN
(Tomokiyo l.640: the period margin decipherment, used here as the known answer), step LEAD (the lane's own target-level claim). PREREG
`f91/PREREG-MAT-F91.md` pushed 5d85e6ebe before any read or score.

**Crops.** `f91/regen_f91.sh` (2 openapi.bnf.fr requests), byte-identical to MAT-NOM's manifest (checked on 2). The s1/s2 segments overlap by
1,920 px, so each cipher line was re-cut as one strip from the same source file (line box from the manifest, +18 px above and below, scaled
2880 -> 2400 px); images in scratch only.

**Transcription (cipher).** Two blind Sonnet passes, 2 calls each (<= 12 line images per call), reference chart = f.78v lines 1-3 with
Bourdeau's labels (`f91/PASS_BRIEF_F91.md`); `f91/passA_f91.tsv`, `f91/passB_f91.tsv`. `tools/reconcile_passes.py --keep-dots`: agree
**507/630 = 80.5%**, 123 disagreement columns (`f91/disagreements_f91.tsv`), not settled by eye (cost); they enter the alignment as unknowns
(`f91/ciphertext_draft_f91.tsv`). Per block (draft signs / agreed): A 99/89, B 216/185, D 203/158, E 112/75.
Region findings: band A1 is the clear line above the block (A's cipher is A2-A4, A2 opening after "Le Mar[escha]l de Matignon"; a 4th cipher
line may sit below the region); **block E's regions in `blocks.tsv` are offset**: its cipher lines start about 100 px left of x=5780 (the first
signs "13 n ..." are cut) and its margin gloss lies left of x=4650, not at 5130 (the 5130 crop is the cipher's own left part). E was therefore
dropped from the alignment; its passes are kept but unusable as they stand (E4 passes read different lines).

**Gloss (period decipherment, grade C).** One Opus read of wider margin crops + one Sonnet check (`f91/gloss_f91.tsv`,
`f91/gloss_check_sonnet_f91.tsv`); two splits settled (B5 'pourveu', D6 name M). Content (M wording): A "... ou estoyt reduicte son armee,
mesmes ses infanteryes il me mandoyt estre quasi toute deffaicte faulte de payement"; B "Quant au chemin que doibvent tenir ceulx qui viendront
doresnavant ... je n'y sache point de meilleur, pourveu que celuy d'Orleans a Lymoges ne soyt point empire ..."; D "... pour villages je croy
qu'il leur faudra faire tenir par Aurillac en Auvergne ... de Haultfort et sieur [?S]upplice ... les faire passer dans le Limosin, estant certain
qu'il y aura par tout de la difficulte".

**Known-answer alignment** (`f91/align_f91.py`, PREREG statistic R on H single-letter codes): **R 0.672 (174/259) vs 200 gloss word-shuffles
mean 0.408, p95 0.465, max 0.490: gate PASS.** By block A 39/56, B 72/107, D 63/96. `f91/align_f91_codes.tsv`: 17 H codes confirmed (h e, .v. n,
q u, w- d, 7 o, Ze t, 4+ m, m t, s u, 8 g, n l, e r, A l, he l, L r, H o, g u). **Conflicts** (HYPOTHESES.md row, rule 4): c (key p) gloss l 8/9;
f (key c|u) gloss r 11/18; Z (t) g 2/2; 3 (e) n 2/2 -- possibly our readers' label for a different sign than Bourdeau's (they had only 3
reference lines), so not a correction. **Candidates for unkeyed labels (M, untested):** U = e 30/34, T = r 9/12, D2 = a 6/7, BOX2 = u 3/5,
1 = s 2/2. U (343 U-graded tokens target-wide) and T (53) are the largest unkeyed labels; the f.110 Tomokiyo-opening note above ("BOX, U and T
fall on u, e, r") points the same way. No key.tsv, reading or grade change; no `--try` run (out of cap).

Requests: openapi.bnf.fr 2 (both 200). Subagents: 5 Sonnet (4 cipher passes, 1 gloss check). Next: `decode_key.py --try U=e`, `T=r`, `D2=a`
with the control at every occurrence (~$1), and an image check of the c/f conflicts against the f.78v chart (~$1); then E re-cut from the
on-disk canvas (0 requests) and blocks C, F (~$4).

## MAT-F91C (15 Oct 2026, account-2 worker, LANE DEFAULT-A2-0509-15)

Brief: `.claude/briefs/runs/2026-10-15-ytbiz-default-0509-jobs.md` job MAT-F91C (blocks C and F, crops first). Times by `date -u`: 06:58-07:2x UTC.
PREREG addendum `f91/PREREG-MAT-F91C.md` pushed 8c14b4143 before any pass, read or score. Prior-work holds as MAT-F91/F91B (plaintext KNOWN =
the period gloss, used as the known answer).

**Step 1, crop gate (no vision call before it).** Canvas c98 re-fetched once (openapi.bnf.fr 1 request, 200, sha1 dfec5334..., identical to
MAT-F91B's). `tools/iiif_lines.py --image c98 --region 1480,1050,3100,1400` (C) and `--region 5230,2640,2900,1420` (F) with `--deskew-region`
(fitted -1.35 / -1.55 deg: the lines slope, which is why fixed-y strips at +-75 px held two lines), `--band-extent --mask-neighbours --max-width 1600
--overlap 80 --debug`. A first run without deskew still cut across the sloped lines (checked on the overlay, discarded). After deskew every crop held
one line by eye (C 13 lines, F 14 of which F10-F11 are clear French); band heights 102-160 px, crop heights 141-238 px, per line in
`f91/crops_manifest_f91c.tsv`; `f91/regen_f91c.sh` re-derives them (images in scratch only).

**Transcription.** Each line = s1 above s2 (100 px overlap); C1-C12, F1-F9, F12 (cipher tail after clear "... Infanterye"), F13, F14 = 24 lines
(C13, mostly clear "Oultre que ... de Haultfort", left out to keep calls at 12 images). Two blind Sonnet passes, 2 calls each, reader brief
`f91/PASS_BRIEF_F91C.md` (f.78v chart): `f91/passA_f91c.tsv`, `f91/passB_f91c.tsv`. `tools/reconcile_passes.py --keep-dots`: agree **546/791 =
69.0%** (C 278/436 = 63.8%, F 268/355 = 75.5%; MAT-F91B 45.1%, MAT-F91 80.5%); quality gate 0.65 PASS. 245 disagreement columns not settled by eye
(cost), entered as unknowns (`f91/ciphertext_draft_f91c.tsv`, `f91/disagreements_f91c.tsv`).

**Gloss (period decipherment, grade C, M wording).** One Opus read of native margin crops (C x900-1760, F x4400-5300), `f91/gloss_f91c.tsv`; not
Sonnet-checked (the check would have crossed 80% of cap), so uncertain words are left out of the normalised column. C (21 lines): "auec sa compagnie
de Gend[armes] / le secours que luy fera de la / Guienne le Sr d'Aubeterre / il les forcera qu'ilz pourront / assemblez dans le pays / les pourra
conduire jusques / sur la riuiere ou le Sr de / St Supplice les recueillera / auec la Guienne et les ... / conduiront dans le Lim[osin] / jusques a ce
que j'espere / renvoye quelque bonne force / de l'armee pour les y / amener estant pour cest / occasion les entreprises / [illegible] / promener les
compagnies / des hommes d'armes d'Ital[ie] / et pourueoyr a leur payement / car autrement il est certain / qu'elles se debanderont par[tout]".
F run 1 (17 lines): "Mais je n'auois entendu ... / que ce pendant on ... / eschappe pour passer la / Dordongne et deca en / Xaintonge ou l'on pense /
que ce soyt son dessaing / d'aller n'estant pour ... / Sr de Matignon assez / fort pour le suyure et / moy en estant encore bien / esloigne car il a
ceste / ... que ce chemin / luy commodera toutesfoys / s'il attend plus grande / j'espere qu'il me donnera / plus pres de luy qu'il / peult estre il ne
pense"; F run 2 (3 lines): "Et [faut?] que le Roy de / Nauarre passe deca / car il ne nous ...".

**Known-answer alignment** (`f91/align_f91c.py` = MAT-F91's script, block list and file names only): **R 0.774 (254/328) vs 200 gloss
word-shuffles mean 0.448, p95 0.503, max 0.542: gate PASS** (C 140/176, F 114/152). `f91/align_f91c_codes.tsv`: 19 H codes confirmed (h e 34/35,
.v. n, 7 o, t e, L r, m t, c p 14/14, Ze t, n l, s u, e r, X a, w- d, H o, oo d, he l, A l, M f, R p); M rows pick 6=n (5/8), ff=n (4/4).
**No conflict in C/F.** MAT-F91's c conflict (gloss l 8/9 in A/B/D) meets the opposite witness here (c = p 14/14, the key value), consistent with its
own note that the readers' `c` label may cover a different sign there; logged in HYPOTHESES.md with both witnesses, not resolved by count (rule 4).
f (key c|u) undecided (s 4/9). **Candidates for unkeyed labels (M, untested):** U = e 42/54 (MAT-F91 30/34), T = r 9/11 (9/12), BOX2 = u 4/4,
5 = u 3/4, 4 = m 2/3 (Bourdeau's crossed-4 = m). No --try (its power control failed in MAT-F91B); no key.tsv, reading or grade change.

Requests: openapi.bnf.fr 1 (200). Subagents: 4 Sonnet (cipher passes). Next: block E with MAT-F91B's regions by this crop recipe (~$2.5); the
U/T/BOX2 candidates need an instrument other than the --try window score (e.g. a held-out gloss block as known answer for the label, with the same
shuffle control), ~$2; an image check of the c/f labels across A/B/D vs C/F crops against the f.78v chart, ~$1.

## MAT-F91E (15 Oct 2026, account-2 worker, LANE DEFAULT-A2-0810-15)

Brief: `.claude/briefs/runs/2026-10-15-ytbiz-default-0810-jobs.md` job MAT-F91E (f.92r block E, MAT-F91C's method). Times by `date -u`: 08:23-08:4x UTC.
PREREG addendum `f91/PREREG-MAT-F91E.md` pushed fda4a3750 before any pass, read or score. `tools/prior_work.py matignon-mayenne-1586 --item-spec
'shelfmark=BnF fr.15572;folio=92;sender=Mayenne' --step-type transcribe` exit 2: plaintext KNOWN (Tomokiyo l.640, the period margin
decipherment, used here as the known answer), step LEAD (the earlier lane's target-level claim, which does not cover block E).

**Crops.** Canvas c98 re-fetched once (openapi.bnf.fr 1 request, 200, sha1 dfec5334..., identical to MAT-F91B/C's). `f91/regen_f91e.sh`:
`tools/iiif_lines.py --deskew-region` (fitted -1.80 deg) `--band-extent --mask-neighbours --max-width 1600 --overlap 80` on 5230,1200,2900,680:
7 bands, L01 and L07 clear French, L02-L06 = cipher lines E1-E5 (E1 opens with clear "bas meilleur", E5 ends in clear "J'ay veu, Sire,
la ..."). One layout change, fixed in the PREREG: the segments overlapped 300 px (about 4 signs), so s2 was trimmed 200 px at its left to the
100 px (about one sign) the reader brief describes. Overlay and every line image checked by eye: one line each. Small superscript signs over
E3-E5 (e.g. "q", "5", "3", a barred sign) were left out by instruction. Gloss: same flags on 4470,1290,780,620, 8 bands = the 8 margin lines.

**Transcription.** Two blind Sonnet passes (1 call each, 5 line images, `f91/PASS_BRIEF_F91E.md` = F91C's brief, same f.78v chart):
`f91/passA_f91e.tsv`, `f91/passB_f91e.tsv`. `tools/reconcile_passes.py --keep-dots` (passes given as line<TAB>tokens; the tool now refuses the
4-column form as a long format): agree **125/153 = 81.7%** (E1 0.733, E2 0.971, E3 0.688, E4 0.865, E5 0.789); quality gate 0.65 PASS.
28 disagreement columns not settled by eye, entered as unknowns (`f91/ciphertext_draft_f91e.tsv`, `f91/disagreements_f91e.tsv`).

**Gloss (period decipherment, grade C, M wording).** One Opus read (`f91/gloss_f91e.tsv`), not Sonnet-checked: "Qu'il seroyt plus a propos /
de licentier [M] l'ung des d[eux] / regimentz et faire au lieu / d'iceluy [M] une leuee de quattre / mil lansquenetz que de / continuer
d'auantage une / p[er]te si notable sire leur / entretenement". (MAT-NOM's "Que(?) Siege plus a propos" in `blocks.tsv` is this first line.)

**Known-answer alignment** (`f91/align_f91e.py` = `align_f91c.py`, block list and file names only): **R 0.817 (76/93) vs 200 gloss
word-shuffles mean 0.531, p95 0.635, max 0.681: gate PASS** (R > max and >= 0.60). n = 93 is small (one block); the shuffle floor is
higher than on C/F (0.531 vs 0.448), as expected for one short block. Secondary, not a gate: C+E+F pooled (`align_f91e.py --pooled`, `f91/align_f91ce_result.tsv`) R 0.784 (330/421) vs shuffles mean 0.436, p95 0.487, max 0.517 (C and F reproduce MAT-F91C exactly, 140/176 and 114/152); pooled candidates U=e 49/62, T=r 12/14, BOX2=u 5/5, D2=a 5/5; o top a 14/33, undecided.
`f91/align_f91e_codes.tsv`: 13 H codes confirmed (h e 11/11, .v. n 8/8, n l 6/7, L r 6/6, w- d 6/6, s u 5/6, t e 6/6, Ze t 4/5, m t 5/5,
c p 2/3, 7 o 2/2, A l 2/2, e r 2/2); B picks i (key i|y) 3/3. **One conflict, o (key i, H): gloss a 3/5** -- witnesses a at E2:26, E4:13,
E4:34; i at E2:14, E2:29. Earlier blocks also put o's top chunk on a without reaching the 0.6 share (MAT-F91 a 16/29, MAT-F91C a 11/28;
`align_f91_codes.tsv`, `align_f91c_codes.tsv`); logged in HYPOTHESES.md with the witnesses, not resolved by count (rule 4) -- it may be a
reader-label merge (o vs a round sign) as with MAT-F91's c. Undecided: q (key u) u 2/5, d (key s) c 2/4, E (i|y) t 2/4, b, oo, 6.
**Candidates for unkeyed labels (M, untested):** U = e 7/8 (MAT-F91C 42/54, MAT-F91 30/34), T = r 2/3 (9/11), D2 = a 3/3, + = m 2/2
(Bourdeau's crossed-4 = m; readers wrote "+" for a cross sign), BOX2 = u 1/1. No --try; no key.tsv, reading or grade change.

Requests: openapi.bnf.fr 1 (200). Subagents: 2 Sonnet (cipher passes). Images in scratch only (`regen_f91e.sh` re-derives them).
Next: a known-answer instrument for U=e / T=r / D2=a / BOX2=u / + = m pooled over A-F (e.g. hold out one block's gloss as the known answer for
the label, same shuffle control; ~$2); an image check of the o and c labels in A/B/D/E crops against the f.78v chart (~$1).

## MAT-KA (15 Oct 2026, account-2 worker, LANE DEFAULT-A2-0810-15)

Brief: `.claude/briefs/runs/2026-10-15-ytbiz-default-0810-jobs.md` job MAT-KA (held-out known-answer test of the label candidates). Times by
`date -u`: 09:15-09:2x UTC. Disk only (0 requests, 0 vision calls). PREREG `f91/PREREG-MAT-KA.md` pushed 17451d305 before any score.
Prior-work: `tools/prior_work.py matignon-mayenne-1586 --item-spec 'shelfmark=BnF fr.15572;folio=91-92;sender=Mayenne' --step-type key --offline`
exit 4: plaintext KNOWN (Tomokiyo l.640 = the period margin decipherment, the known answer here); the two LEAD rows are this lane's own claims.

**Instrument** (`f91/mat_ka.py`, `--check` exits non-zero when `f91/mat_ka_result.tsv` / `mat_ka_folds.tsv` are stale). Rule 3's third-attempt
clause retired the `--try` window score for these labels (MAT-F91B power control failed), so this is a different instrument: each of blocks A-F
is aligned ALONE with `tools/interlinear_align.py` (settings as `align_f91e.py`), with every code that is not an H single-letter key code renamed
to a unique singleton, so a label's chunk at each position comes only from the H codes around it, never from EM agreement with its own other
occurrences. For a label, the fit is its majority gloss letter in the other five blocks; pooled leave-one-block-out (LOBO) accuracy against 200
label-shuffle draws (same per-block counts, from all scored code positions) and a power check (a known H code masked the same way, subsampled to
the label's count, 20 seeds). Sanity: the masked alignment still reads the H codes at R 0.780 (521/668; MAT-F91* 0.672-0.817).

| label | candidate | LOBO accuracy | null mean / p95 / max | power code (n) | power | verdict |
|---|---|---|---|---|---|---|
| U | e | 63/99 = 0.636 | 0.208 / 0.283 / 0.354 | h = e (71) | 20/20 beat p95, fit 20/20: PASS | candidate for key.tsv at grade S, U = e |
| T | r | 15/25 = 0.600 | 0.139 / 0.320 / 0.400 | L = r (25) | 20/20, 20/20: PASS | candidate S, T = r |
| D2 | a | 9/13 = 0.692 | 0.126 / 0.385 / 0.538 | e = r (13); X = a (7, secondary) | 20/20, 20/20: PASS; X 0/20 | candidate S, D2 = a |
| BOX2 | u | 8/10 = 0.800 | 0.126 / 0.400 / 0.600 | s = u (10) | 16/20, 20/20: PASS | candidate S, BOX2 = u |
| + | m | 0/4 = 0.000 | 0.113 / 0.500 / 1.000 | 4+ = m (4) | 1/20, 9/20: FAIL | too-short (not rejected) |

Per fold (`f91/mat_ka_folds.tsv`): every held-out block's fit letter equals the candidate for U (6/6 blocks), T (5/5), D2 (4/4) and BOX2 (5/5);
U is weakest on C (19/33) and F (11/22), D2 on F (1/3). Caveats: the labels are the readers' labels from two blind Sonnet passes at 69-82%
agreement (MAT-F91/C/E), so a label may merge two signs (MAT-F91's c, MAT-F91E's o); the gloss is one Opus read, not Sonnet-checked (C, E, F);
D2's same-letter power code X = a has only 7 scored positions and fails, so D2's power rests on the frequency-matched code e = r; BOX2's power is
16/20, the thinnest pass. A pass here is a known-answer result on the f.91-92 blocks only (grade S candidates); it does not by itself say the same
labels carry these values on the 13 Cipher-1 leaves, where U (343) and T (53) were read by other readers (Bourdeau's transcription).
No key.tsv, reading or grade change in this job. Next: a key.tsv edit job that adds U = e, T = r, D2 = a, BOX2 = u at grade S (with this
section as the control) and re-runs `tools/decode_key.py --check` and the per-leaf fr16 judge against shuffled controls (the Escalation "retry"
step), ~$1.5; whether Bourdeau's U/T/D2/BOX2 on the 13 leaves are the same signs as the f.91 readers' labels needs an image check against the f.78v
chart (~$1, with the o/c check).

## MAT-KEY (15 Oct 2026, account-2 worker, LANE DEFAULT-A2-0810-15)

Brief: `.claude/briefs/runs/2026-10-15-ytbiz-default-0810-jobs.md` job MAT-KEY. Times by `date -u`: 09:34-09:4x UTC. PREREG `f91/PREREG-MAT-KEY.md`
pushed b76bd10c8 before any score; `tools/prior_work.py` exit 4 (plaintext KNOWN from Bourdeau's key and the f.91 margin gloss; LEADs = own claims).

**Image check first (eye, openapi.bnf.fr 3 requests: c97 region + c98 max via `f91/regen_f91.sh`, c131 left half `pct:0,0,52,100` = f.124v;
images in the session scratchpad only).** Compared f.91v block D line 1 (reconciled `7 T c U t .v. o D2 A B t q 8 h 1 w- t BOX2 ...`), the f.78v
reference chart line 2 (Bourdeau's own f.78v labels, which the f.91 readers were given) and f.124v in Bourdeau's transcription (page lines 1, 2
and 12 = his f124v-1 `... o g U .v. m ...`, f124v-2 `h d B he M T d E ...`, f124v-12 `... g m BOX2 .v. z .v. o U d ... E D2 .v. Ze ...`):
- **U** = the cross sign like an inverted T with an x through it, in all three. Same shape.
- **T** = a T with the bar on top (heavy in f.91, thin on f.124v), distinct from `t` (a cross with a hook). Same shape. Checked on f.124v only.
  f.110 holds 38 of the 53 T, and its T was not eyed this job (the f.110 crops on disk are 53 px tall).
- **D2** = the open triangle, in all three. Same shape.
- **BOX2** = the flat rectangle, in all three. Same shape. Bourdeau's `BOX` (137, mostly f.110) is a different label, his open box, and was not touched.
All four pass, so all four are applied. Inference, not tested here (grade M): Bourdeau's later transcriptions (ff.110, 123r-124v, fr.15571 f.177)
use `U` and `D2` where his earlier ones (ff.143r-201) use `x` (= e, H) and `D` (= a, H): the two label sets barely overlap by leaf (see the
per-leaf label counts in this job's log). That fits U = e and D2 = a, but only an image check of `x`/`D` on f.143 would confirm it.

**Key edit.** `key.tsv` rows added: U = e, T = r, D2 = a, BOX2 = u, grade S, source MAT-KA (a948d56a8) + this image check. `+` (= m) not added
(too-short in MAT-KA; the 13 leaves carry no `+` token). `tools/decode_key.py ciphers/matignon-mayenne-1586` regenerated `reading.txt` and
`reading_tokens.tsv`; `--check`: "reading up to date", exit 0. `reading_letters.txt` is not regenerated by decode_key.py and was left as it was
(judge_leaves.py builds its letters from reading_tokens.tsv).

**Grade counts (rule 4):** before H 10,074 / M 1,648 / U 1,272 / S 0; after **H 10,074 / M 1,648 / S 418 / U 854** (C 0, I 0). Tokens changed
U -> S per leaf: f110 44, f123r 79, f123v 84, f124r 84, f124v 59, fr15571 f.177 67, f201 1, the other six leaves 0 (418 in total).

**Per-leaf judge (rule 7), `judge_leaves.py --shuffles 20` (fr16 spec judge, within-line shuffle control), before (key at 520849fb2, scratch)
and after (committed `openings/leaf_judge.tsv`):**

| leaf | changed | N b/a | score b/a | shuffle mean b/a | margin b/a | real_p05 (a) | judge (a) |
|---|---|---|---|---|---|---|---|
| f110 | 44 | 1190/1234 | -1.701/-1.704 | -1.780/-1.806 | 0.079/0.102 | -0.866 | FAIL |
| f123r | 79 | 987/1066 | -1.699/-1.573 | -1.967/-1.894 | 0.268/0.321 | -0.878 | FAIL |
| f123v | 84 | 1181/1265 | -1.395/-1.295 | -1.922/-1.883 | 0.527/0.588 | -0.865 | FAIL |
| f124r | 84 | 1136/1220 | -1.448/-1.361 | -1.890/-1.826 | 0.442/0.465 | -0.876 | FAIL |
| f124v | 59 | 661/720 | -1.463/-1.357 | -1.887/-1.823 | 0.424/0.466 | -0.863 | FAIL |
| fr15571 f.177 | 67 | 639/706 | -1.472/-1.397 | -1.879/-1.842 | 0.407/0.445 | -0.880 | FAIL |
| f201 | 1 | 1033/1034 | -1.245/-1.247 | -1.894/-1.895 | 0.649/0.648 | -0.859 | FAIL |
| f143r, f143v, f150, f154, f173, f196 | 0 | unchanged | unchanged | unchanged | 0.596-0.726 | | FAIL |

The margin over the leaf's own shuffle rises on all six changed leaves (+0.023 to +0.061), and the raw score rises on five of them (f110 flat,
-0.003). Every leaf still FAILs its real_p05 gate, before and after, as in GAPS (2 Oct): the judge says the change moves these leaves toward the
read leaves (margins 0.60-0.73), not that they read. f110 stays far below the others (margin 0.10): its 125 `BOX` and its own label problems
(D2B-MATF110 split 41.5%) are untouched. Readings changed; the target has no AUDIT.md and no reading row in SECOND-OPINIONS-QUEUE.tsv
(SO-MATIGNON-LEADS is a leads prompt), so nothing to propagate under rule 10. Next: eye the f.110 T and BOX against the f.91 chart (~$1), and
eye `x`/`D` on f.143 against `U`/`D2` (~$1), then the o/c label check.

## Remaining gaps (finish-or-blocker pass, 1 Oct 2026)
Read so far: 1,406 of 12,994 transcribed Cipher-1 tokens (10.8%) sit in a sense run. Source: the proxy split in `resolve_mu.py` / `spans.tsv`, NOTES.md "NEAR step (1)" (bMAT2), recounted from `spans.tsv` + `reading_tokens.tsv` on 2 Oct 2026 00:50 UTC. Per leaf: f110 0/1699, f123r 23/1097, f123v 92/1251, f124r 84/1203, f124v 45/727, f143r 136/724, f143v 247/1182, f150 10/445, f154 259/1061, f173 168/1082, f196 168/840, f201 163/987, fr.15571 f.177 11/696. Grades were H 10,074 / M 1,648 / U 1,272 (H 10,074 / M 1,648 / S 418 / U 854 after MAT-KEY, 15 Oct 2026; sense-run counts not recomputed), and the fr16 judge FAILs at -1.371 against real_p05 -0.837 (shuffled -1.78). The denominator is Bourdeau's partial transcription only: the spec says "13 leaves partly transcribed", and the untranscribed remainder of each leaf has never been measured. Cipher-3 (fr.15571 f.179, fr.15572 f.276) has 0 sign tokens transcribed. Bourdeau's own 28% (measure.py with his beam LM, 22 Sept) is not reproduced here. There is no AUDIT.md.
- fr.15572 ff.143r, 143v, 150, 154, 173, 196, 201 (7 Cipher-1 leaves, 6,321 tokens, U 129 = 2.0%, M 742) - blocker: not-attempted; the H key covers most of these tokens, but only 2-24% of each leaf sits in a sense run (`spans.tsv`). bMAT2's two-context rule and bMATBEAM's beam both pooled all 13 leaves (the f.78v/79r tests were crib work, not these leaves). bMATBEAM fitted its M choices jointly with U values that its own controls show are TOK/null noise, and committing them made the judge worse (bMAT1C -1.545, reverted in bMAT1D). Its own suggested per-leaf, read-context-only rerun was never made. An M-only rerun would be the second target run of the same beam, so pre-register its gate, and if it fails, retire the beam for this target rather than tuning it again; next: (GAPS 2 Oct 2026: per-leaf judge run, `judge_leaves.py` / `openings/leaf_judge.tsv` -- these 7 leaves score -1.158 to -1.293 against their own within-line shuffle max -1.806 to -1.846 (20 seeds), all FAIL the gate real_p05 -0.86 to -0.89); GAPS gap 1, 3 Oct 2026 (account-4, prereg bd74c69d): control (A) at each leaf's N reads M at 0.76-0.89 vs frequency 0.39-0.57 (gate a passes 7/7), but the judge-gain instrument fails its own known-answer power check on 6 of 7 leaves (control gain above its shuffle-null max on 5/21 seeds; the beam LM and the judge share catheri01), so 1/7 testable < 4: non-test at this N, beam neither licensed nor retired by the judge-gain instrument [retired: judge-gain gate for this beam, section "GAPS-matignon-mayenne-1586 gap 1 (3 Oct 2026)"]; f201 alone, for the record: +0.029 vs null max +0.078; GAPS2 3 Oct 2026 (prereg c26ff40d): agreement with Bourdeau's per-line decoder output (HEAD 4d32ec9) on f143r/f143v/f154/f173: beam 0.850/0.797/0.748/0.780 vs first-candidate 0.625/0.692/0.689/0.720 vs within-line shuffle null max 0.642/0.657/0.592/0.680, control power 3/3 seeds every leaf -- AGREEMENT SIGNAL 4/4 (agreement with another modern reading, not accuracy; section "GAPS2-matignon-mayenne-1586 (3 Oct 2026, account-4)"); GAPS3 3 Oct 2026 (prereg 0b58589a): the 167 changed M choices as S candidates in a scratch reading, re-judged per leaf: every leaf rises and stays above its letter-shuffle max (4/4), but the rise beats the beam's own shuffled-target rise on 1/4 leaves only (f143r +0.144 vs +0.124; f143v/f154/f173 +0.011/+0.011/+0.001 vs +0.057/+0.055/+0.053) -- NON-TEST, nothing committed [retired: judge-scored commit of the mu beam, third attempt, section "GAPS3-matignon-mayenne-1586 (3 Oct 2026, account-4)"]; next: grade the beam's M choices only against a non-LM reference -- the f.91-92 margin decipherment or the f.18/f.19 pair (gap 4's step), ~$12
- fr.15572 ff.110, 123r, 123v, 124r, 124v and fr.15571 f.177 (6 Cipher-1 leaves, 6,673 tokens, U 1,143 = 17.1% before MAT-KEY, 726 = 10.9% after it (15 Oct 2026: U/T/D2/BOX2 = e/r/a/u at S, 417 tokens), read 0-7.4%) - blocker: not-attempted; f110 alone is 30% U and 0% read. Of the target's 1,272 U tokens, 1,086 fall on 31 sign labels absent from `key.tsv` (U 343, z 296, 4 106, w 83, T 53, y 41, v 37, p 18, D2 16, 5 16, ...) and only 186 on 17 '+' rows (BOX 137); recounted from `reading_tokens.tsv` 2 Oct 2026, and MAT-CCE's "1,272 over 19 codes" is wrong. Several absent labels look like unmarked variants of keyed ones (4/4+, w/w-, T/T=, D2/D, p/P, BOX2/BOX), and bMAT1F's two blind passes of f.79r split on exactly 4 vs 4+. New, not used before: Tomokiyo's published opening for "f.111" ("Monsieur de Villeroi vous verres bien par la lettre que je fais au roi...", `sources/cryptiana/web/henryiii.htm`, Cipher-1 section) lines up with our decoded f110-1. A scratch DP this pass scored 26 against a maximum of -9 over 20 within-line shuffles (f143r-1 28 vs 0, f154-1 20 vs -1). By eye, BOX, U and T fall on u, e, r, and several H positions read i for n/s and g for e/v. That is a known-plaintext check of the label-variant idea, at grade M (a modern published reading, credited to Tomokiyo). GAPS 2 Oct 2026: committed as `align_openings.py` with a 200-draw within-line token-shuffle control -- f143r 468 vs shuffle max -67, f154 66 vs 20, f110 33 vs -22 (f150 -50 vs -19, not aligned); but only 11 U tokens fall on a letter at all, all on f110 (BOX a 2 / u 1 / e 1, z i/o/s, w, U, T, p once each), so the tabulation has no power with this material -- untestable by this instrument, no value read (section "GAPS-matignon-mayenne-1586 (2 Oct 2026)"); the one lead is `8=g` 0/4 on f110. Bourdeau's HEAD NOTES.md read the same job (snapshot `sources/cyphersolver/2026-10-02/matignon1586/NOTES.md`): his glyph table gives ⊐ box and ꝉ crossed-t = u/v, ₸ crossed-4 = m, ƀ = i/j; GAPS2 2 Oct 2026 (03:4x UTC): his HEAD `key.json` (34e0fc8) fetched and diffed -- 87 rows, 0 added / 0 removed / 0 changed against `key.tsv`, and all 13 transcriptions token-identical to `ciphertext.txt`, so no new value exists in his key; his table's box = u/v (and T = u as a label guess) tested as an M hypothesis with a 19-other-letter control (`hypothesis_judge.py`): BOX=u ranks 10/20 on f110 (n 125), 9/20 pooled, T=u 14/20 -- but the same instrument recovers the true letter for only 1 of 10 keyed H labels on f110 against 15/17 on f143v and 15/16 on f154 (`openings/hypothesis_power.tsv`), so on f110, where 91% of BOX and 72% of T sit, this is untestable by this instrument, not a negative; no value committed; next: cut f.110 line crops with `tools/iiif_lines.py` (ark btv1b9061879d) and run two blind passes plus a reconciliation over a 4-line sample, ~$9
- untranscribed remainder of the 13 Cipher-1 leaves (extent unmeasured) - blocker: not-attempted; the spec and NEAR.md both say Bourdeau transcribed these leaves "only in part", and NOTES.md bMAT2 cites his separate read_of_transcribed and read_of_leaf figures, but no line or sign count of the full leaves is on file. Tomokiyo's opening for f.150 ("il estoit me besoins car je tourvai quil auoit") does not align with our f150-1 (scratch DP -14 vs shuffle median -15; confirmed with the committed `align_openings.py` 2 Oct 2026: -50 vs shuffle max -19 over 200 draws), unlike f110/f143r/f154, so our f150 may start elsewhere on the leaf. GAPS2 2 Oct 2026: his HEAD extent recorded from his "Coverage, measured" table -- f110 37/54 lines, f196 26/31, fr.15571 f.177 24/29, the other ten leaves complete; +2,648 tokens estimated untranscribed over the whole target incl. Cipher-3 (section "GAPS2" (d)); next: count lines per leaf on Gallica canvases of btv1b9061879d against `ciphertext.txt`'s line counts and list the untranscribed lines, ~$2
- Nomenclator number codes on key.tsv '+' rows (62 x10, 33 x8, 49 x5, 44 x4, star/15/36 x3, 46/53/27/68 x2, 54/hash/88/104/79 x1 = 49 tokens) plus singleton absent labels (121, 102, Bi, u, f3, 73, 18, 101, O) - blocker: open-codes; each occurs 1-10 times in the proper-name range. Tomokiyo's list gives 76/82/84/98 as roi de Navarre/Condé/Turenne/Montauban, and 49 appears unread in his f.143 opening. MAT-CCE's cross-office lookup has no power (4.2% vs 2.85% chance). bMATBEAM's values for these signs had margins of 0.5-8.1 bits. The f.78v/79r crib is retired (rule 3(b)), so only a period gloss on a different leaf would narrow them SPLIT-matignon-mayenne-1586 (2 Oct 2026, 0 of 31 split-check rows reachable, no leaf image on disk): 37 x2 and 73 cut into 3|7 / 7|3 (e o / o e) against the key, but sit in the word-code range and 37 closes both parallel lines f196-3/f201-5, so they are held as unkeyed word codes, not glued letters, pending the image; `split_worklist.tsv` ranks all 31 labels (7 cut fully into key codes: fe x6, de x5, me x5, 37 x2, 73, Bi, f3); next: locate and crop the f.91-92 Cipher-1 letter ("deciphered in the margin", henryiii.htm l.638, never opened) or the f.18-21/f.19 pair (cipher page plus a full clear page, of which Bourdeau's repo holds only 3+2 lines, bMAT1D) on btv1b9061879d (f.78v/79r = canvas 85). Transcribe cipher lines and clear text in two passes plus a reconciliation, and run `tools/interlinear_align.py` behind a known-answer control on H codes, ~$12
Cipher-3 leaves fr.15571 f.179 and fr.15572 f.276 left this list on 19 Oct 2026: found-solved elsewhere (alejandrozarco, PR #25 in dbourdeau/cyphersolver, 6-7 Oct 2026), section "Found solved elsewhere: Cipher-3 ff.179, 276" below.

## Escalation (1 Oct 2026)
- [ ] siblings: Opened so far: fr.3974 f.24 (MAT-3974: plain prose, no cipher, retired), the DECODE 24 Sept cache (0 hits, bCSMAT d), and the 27 Sept key_crossmatch fr7129 "hit", which scored the same on all three shuffled controls (ROOM.md 27 Sept 02:51-02:52), so it is not a lead. Not opened: the f.91-92 Cipher-1 letter (deciphered in the margin, Tomokiyo l.638), the fr.15573 Forget/Mayenne/Matignon folios ff.7, 20, 31, 62, 131, 299 (SO-MATIGNON-LEADS, unchecked), and fr.3354 f.91 and fr.16092 f.5 (weaker SO leads). Located 15 Oct 2026 (MAT-NOM): f.91r = canvas 97 right, f.91v/f.92r = canvas 98, six cipher blocks (~47 lines) with ~74 lines of margin decipherment, crops regenerable (`f91/`); next: two blind passes of glosses and cipher + interlinear_align per block, ~$8-10. MAT-F91 15 Oct 2026: blocks A, B, D read (2 passes, 80.5%) and aligned to the margin gloss, key known-answer gate PASS (R 0.672 vs shuffle max 0.490), 17 H codes confirmed, 4 conflicts, candidates U=e, T=r, D2=a (M); E's blocks.tsv regions offset, dropped; next: --try U=e/T=r/D2=a with control (~$1), then E re-cut and C, F (~$4). MAT-F91B 15 Oct 2026: --try power control failed (wrong value 3=i accepted), so the candidates are a non-test, none accepted; C/F regions re-measured (F offset like E; corrected regions in section "MAT-F91B"), but its strips were cut too tall and the two passes agree 45.1%, so no alignment; next: re-cut C, F at +-50 px half-lines, 2 passes + reconcile + alignment (~$5), then E (~$2). MAT-F91C 15 Oct 2026: C, F re-cut with iiif_lines --deskew-region (one line per crop), passes 69.0%, alignment gate PASS (R 0.774 vs shuffle max 0.542), 19 H codes confirmed, no conflict, c = p 14/14 (opposite witness to MAT-F91's c conflict), candidates U=e, T=r, BOX2=u, 5=u, 4=m (M); next: E by the same recipe (~$2.5).
- [ ] clear-pages: The hand and DP alignment against the f.78v/79r margin crib is closed by rule 3(b): bMAT1D 6/20 and 4/20, bMAT1E 9/20, bMAT1G 11/20, bMAT1H failed its pre-registered gate at 7/8. That closes this crib, not clear pages in general. Never imaged by us: the f.14v/f.15r and f.18-21/f.19 period decipherments (Bourdeau's repo holds one quoted phrase and 3+2 lines, bMAT1D), the f.91-92 margin (located and cropped 15 Oct 2026, MAT-NOM; transcribed in two blind passes and aligned for all six blocks A-F on 15 Oct 2026 by account 2's MAT-F91, MAT-F91C and MAT-F91E, sections of those names), the Cipher-3 decipherments f.190, f.279-280 and f.282 margin, and the f.78v margin itself (native fetch reset twice, bMAT1F). Planned: f.91-92 margin or the f.18/f.19 pair as a fresh crib. Separately, Tomokiyo's modern published openings (f110/"f.111", f.143, f.154, f.276) serve as known-plaintext checks.
- [ ] known-keys: Done: Bourdeau's key.json fc0c9e8 (period-verified, now `key.tsv`, listed in KEY-DESIGN.tsv but not in KEY-OFFICES.tsv). MAT-CCE found no power across 7 office-cluster keys, and fr.3974 f.24 is retired. Not done: Tomokiyo's reconstructed tables `henryiii_MayenneForget1.png` (Cipher-1), `henryiii_Matignon3.png` and `henryiii_Camus.png` are not on disk or applied. His nomenclature list (76 roi de Navarre, 82 Condé, 84 Turenne, 98 Montauban) is not in `key.tsv`, which has '*' for all four, so f143r-2 reads "du * du que" where his paraphrase reads "du 76 duquel". `tools/design_prior.py` run 15 Oct 2026 (MAT-NOM): letter-for-letter excluded, mixed/code plausible, consistent with the H key. Bourdeau's HEAD NOTES.md re-read 2 Oct 2026 (GAPS, snapshot in sources/cyphersolver/2026-10-02/): glyph table ⊐ box / ꝉ crossed-t = u/v, ₸ crossed-4 = m; GAPS2 2 Oct 2026: his HEAD key.json (34e0fc8) and 13 transcriptions fetched and diffed -- identical to `key.tsv`/`ciphertext.txt`, no new value; box = u/v tested as a hypothesis, untestable on f110 by the per-letter judge instrument (power control 1/10). Planned: the two Tomokiyo tables, and the f.110 crops for BOX/T.
- [x] print: bCSMAT made seven checks: both Labande Montaigne-Matignon 1916 editions grepped whole (no 1585/86 dates, no Mayenne or Forget), the SHF Lettres de Henri III (not on IA), Tomokiyo henryiii.htm (still undeciphered), the DECODE cache, both solver repositories, a web search, and OpenAlex/S2. No prior decipherment was found. One remainder is unchecked: the 1749 Villeroy-to-Matignon Lettres (SO lead, p.222), which runs Villeroy-to-Matignon, the opposite direction to these Mayenne/Forget-to-Villeroy letters.
- [x] key-rebuild: bMAT2's two-context rule is a control-backed negative (S 41 on the target vs 40-45 shuffled). The bMATBEAM 6-gram beam reached M 0.83 on its control, but on the target the U solution matched the shuffled null pattern, and its M commit (bMAT1C) worsened the judge and was reverted (bMAT1D). MAT-CCE's cross-key lookup has no power. Untried: a per-leaf, M-only beam run (gap 1). That run would be the beam's second target attempt, so it carries a pre-registered gate, and a failure retires the beam for this target. Run 3 Oct 2026 (GAPS gap 1): control (A) M 0.76-0.89 per leaf, but the judge-gain gate had no power (1/7 leaves testable), non-test; next instrument: a reference reading (Bourdeau's per-leaf files), not the shared-corpus judge. Run 3 Oct 2026 (GAPS2): agreement with Bourdeau's per-line readings, 4/4 leaves beam > null max and > first + 0.02 (0.75-0.85 vs first 0.63-0.72). Run 3 Oct 2026 (GAPS3): per-leaf commit-and-judge NON-TEST (rise beats the shuffled-target rise on 1/4 leaves); the judge-scored commit of this beam is retired (third attempt); M choices wait on a non-LM reference (period gloss on a Cipher-1 leaf).
- [ ] image-check: Done only on the crib leaves f.78v/79r: Bourdeau's f78 skips 44 signs at a line join (bMAT1G), and two blind passes of f.79r split on 4 vs 4+ at 59.5% agreement (bMAT1F). None of the 13 target leaves has been re-read against its image. The disk-only Tomokiyo opening alignment (gap 2) ran 2 Oct 2026 and could not predict which labels collapse (11 U tokens on letters, all on f110, whose decode judges at its own shuffle level); `8` reads g 0/4 on f110. Planned: native line crops of f.110 and two blind passes over a 4-line sample, testing 4/4+, w/w-, T/T=, D2/D, U and z. D2B-MATF110 6 Oct 2026: run (lines f110-1..5, 2 blind passes, prereg 859e5757b): G0 control passes (55.7%/58.4% vs 50%), G1 fails for every label (T read as T 10/10; z, BOX, U no agreed keyed label; w/4/p too few), A-B agreement 58.5%; no key change; next: the owner's sign sorter for f.110 BOX/z/T/U/w/4 (TRANSCRIPTION.md: >10% pass split goes to a person). SPLIT-matignon-mayenne-1586 (2 Oct 2026, account-4): the 31 `--split-check` labels (7 full split candidates incl. 37/73/fe/me/de, 6 compound, 18 absent; 1,086 U tokens) all fall on leaves with no image on disk -- 0 of 31 reached, 0 vision calls, grades unchanged; `split_worklist.tsv` is the ranked crop list (about 10 native line crops over 7 leaves, 7 vision calls, ~$4), to run with the f.110 sample above. MAT-KEY 15 Oct 2026: U, T, D2, BOX2 eyed on f.124v vs f.91v D1 vs the f.78v chart, same shapes; f.110 T and BOX not eyed yet.
- [ ] retry: Not run, because no value has survived to extend the key (bMAT1C's S grades were reverted). H 10,074 / M 1,648 / U 1,272 has been unchanged since 26 Sept. Planned: after the label check or the per-leaf M run, re-run `tools/decode_key.py --check` and the fr16 judge per leaf against shuffled controls. MAT-KEY 15 Oct 2026: retry run with U=e, T=r, D2=a, BOX2=u at S (H 10,074 / M 1,648 / S 418 / U 854); per-leaf judge margins up on the six changed leaves, every leaf still FAIL; next: the f.110 T/BOX and f.143 x/D image checks, ~$2.
Verdict: keep going: 4 internal gaps; cheapest next: (15 Oct 2026, MAT-154) f.154's own 47 o tokens, 3x crops, two blind readers: A 42 / B 0 / X 5 by consensus (kappa gate FAIL by one-class prevalence, 42/44 agree on plain o; oB n = 0, too-short), so --try oB=a on f.154 is a non-test by construction and was not run; o = i (H) there unaffected (section "MAT-154"): image-check whether Bourdeau's `a` sign on f.154/f.143r is the f.91 stemmed oB (~$1), or sort f.110's o (~$4) / owner sorter. Earlier: (15 Oct 2026, MAT-ORL) the agreed o shape labels cover 0 of the 13 leaves' 662 o tokens (f.91 only), so the 13-leaf --try is n = 0 and was not run; on an f.91 copy with its power control passed, oB=a is accepted (S, f.91 tokens only) and oA=i rejected (runner-up NULL, M); no key edit: sort the 13 leaves' own o tokens by shape, one leaf first (f.154, 3x per-token crops, two blind readers), then --try oB=a there with the same control (~$4-5 per leaf), or two piles in the owner's sign sorter (section "MAT-ORL"). Earlier: (15 Oct 2026, MAT-R2) a second blind reader on the same 78 crops agrees with MAT-O3X (54/55 where both read A/B, kappa 0.962) and its own labels PASS the same split gate (28/48 vs p95 19; oA = i, oB = a candidate S; section "MAT-R2"): re-label the 13 leaves' o by shape and `decode_key.py --try` oA=i / oB=a with its control before any key edit (~$4). Earlier: (15 Oct 2026, MAT-O3X) the o re-sort from 3x per-token crops PASSes the unchanged registered split test (30/50 vs random-split p95 20, max 27): plain o = i (11/21) and stemmed o = a (19/29), both candidate S on the f.91-92 gloss (section "MAT-O3X"; no key edit): a second blind reader on the same 78 crops (~$0.6), then re-label the 13 leaves' o by shape (line crops or the owner's sign sorter as two piles) and `decode_key.py --try` oA=i / oB=a with its control before any key edit (~$4). Earlier: (15 Oct 2026, MAT-OSPLIT) the blind o shape sort (A 45 / B 17 / X 16, mostly low-confidence) FAILs the registered split test (23 vs random-split p95 23); both shapes and o as a whole lean to gloss a on held-out blocks (o 24/65, M): put the o shapes to the owner's sign sorter or re-sort from 3x per-token crops, then re-run `osplit/mat_osplit.py` (~$1.5), and register an o = a vs o = i test on f.91 (~$1). Earlier: (15 Oct 2026, MAT-BOX) BOX=u --try rejected with its power control passed (f.110 and whole text; no key change); the o label covers two shapes that split 5/5 with the f.92r gloss (plain o = i, stemmed o = a): sort o into the two shapes over f.91 A-F and f.110, then the MAT-KA block-held-out test per shape (~$2-3). Earlier: (15 Oct 2026, MAT-EYE) every f.110 `BOX` eyed (5 of 125, still U) is the flat-rectangle BOX2 shape: test BOX=u with `decode_key.py --try` at every occurrence with its control before any key edit (~$1.5), then the o/c label check (~$1); the eye check itself ran (section "MAT-EYE": f.110 T 1 native + ~10 reduced-scale all top-barred T, 0 mismatches; f.143r D 9/9 triangle = D2 shape, x 7/7 letter x, 0 mismatches, no regrade); the key edit itself ran (U=e, T=r, D2=a, BOX2=u at S, 418 tokens U -> S, per-leaf margins up on all six changed leaves, all leaves still FAIL real_p05, section "MAT-KEY"); earlier step: (15 Oct 2026, MAT-KA, done by MAT-KEY) a key.tsv edit adding U = e, T = r, D2 = a, BOX2 = u at grade S (all four passed the block-held-out gloss test with power, section "MAT-KA"; + = m too-short) and the retry step: `tools/decode_key.py --check` plus the per-leaf fr16 judge against shuffled controls (~$1.5), with an image check that Bourdeau's U/T/D2/BOX2 on the 13 leaves are the same signs as the f.91 readers' labels, together with the o/c label check (~$1); earlier step: (15 Oct 2026, MAT-F91E, done by MAT-KA) a known-answer instrument for the U=e/T=r/D2=a/BOX2=u/+=m candidates pooled over blocks A-F, holding out one block's gloss per label with the same shuffle control (~$2), then an image check of the o (gloss a 3/5 in E, conflict logged) and c labels (~$1) (block E done 15 Oct by MAT-F91E, gate PASS R 0.817 vs shuffle max 0.681; earlier step: a known-answer instrument for the U=e/T=r/BOX2=u candidates other than the --try window score (~$2) (C, F done 15 Oct by MAT-F91C, gate PASS R 0.774; the --try of U/T/D2/BOX2 is a non-test, power control failed); before that: gap 2's f.110 sample ran 6 Oct 2026 (D2B-MATF110: no label collapses, pass split 41.5%), so the f.110 glyphs go to the owner's sign sorter (seeded 6 Oct 2026 by R7-MATSORT, `sorter/`; R7-MATQA 6 Oct 2026 found it NOT fit to hand on, 6/6 checked tiles off their label; R8-MATCUT 6 Oct 2026 re-cut it deskewed with tools/sorter_recut.py + --region: preflight PASS, 22/24 sheet tiles one whole sign on the right line, flagged to the account-3 orchestrator to publish, ASKS 146; next: the owner's pass on the published sorter, then apply per sorter/README.md); after that, the other leaves' `split_worklist.tsv` crops (7 vision calls, ~$4) (gap 1's judge-scored beam commit retired 3 Oct 2026, GAPS3 NON-TEST; its M choices now wait on gap 4's period gloss, ~$12)

## Web and blog check (GAPS-matignon-mayenne-1586, 2 Oct 2026)

Run 2 Oct 2026 01:58-02:05 UTC (clock read) because `tools/intake_gate_check.py matignon-mayenne-1586` exited 1 only
for the missing CHECK-SOLVED-WEB section (`.claude/briefs/check-solved.md`, "Required step"). Rule 10 wording: what
follows is a search result, never a novelty verdict.

(a) Plain web searches (WebSearch, 9 queries):
1. `Mayenne Forget Villeroy 1586 chiffre lettre déchiffrement fr. 15572` -- BnF finding-aid pages (Français 3974-3995,
   4707, 4716, Cinq cents de Colbert 488), Wikipedia (Mayenne, Villeroy, Forget de Fresnes); nothing on fr.15572's
   cipher leaves.
2. `"15572" Mayenne Forget cipher 1586` -- this repository's own PR #29 (SO-MATIGNON-LEADS), a fork of Bourdeau's
   cyphersolver (arya1515), Wikipedia; nothing external carrying a reading.
3. `"Monsieur de Villeroi vous verres bien par la lettre"` (Tomokiyo's f.110 opening, quoted) -- 0 hits for the phrase;
   results are Sévigné, Baudelaire, Béranger, Voltaire letters mentioning a later Villeroi.
4. `Matignon Mayenne 1586 cipher BnF français 15572 undeciphered` (folder title) -- PR #29 again, BnF finding aids
   (Français 15540-15584 series page), nothing carrying a reading.
5. `"s'estant laisse entendre" "voulloit" 1586` (Tomokiyo's f.143 opening) -- Granvelle correspondance vol. IX
   supplement (commissionroyalehistoire.be, 1582 Parma letters, unrelated), Potter's François Ier inventories; not
   this letter.
6. `Mayenne Forget cipher 1586 solved Claude OR GPT OR "solves"` (model-solve announcements) -- only the Urquhart
   "cyphral distich" Fable 5.1 story (Schneier, Vals AI, 36kr), unrelated; a second cyphersolver fork (setsunaatto).
7-9. `site:` searches for the three blogs returned no on-site hits for Mayenne/Matignon/15572 (one Cipherbrain
   Catinat 1690s post, unrelated), so each blog's own search was used, below.

(b) The three blogs by their own site search (curl, 1.6 s apart, 3 requests each, all HTTP 200):
- Cipherbrain (scienceblogs.de/klausis-krypto-kolumne/?s=Mayenne | Matignon | 15572): "Wir konnten leider keine
  Beiträge finden" for all three -- no post, hence no comment thread to read.
- Cryptiana blog (cryptiana.blogspot.com/search?q=Mayenne | Matignon | 15572): "No posts matching the query" for all
  three. Tomokiyo's web pages: the on-disk snapshot `sources/cryptiana/web/` grepped first (0 requests): henryiii.htm
  (this target's source page), GL.htm (Lasry's 2022 solution of fr.15572 **f.43**, a different leaf not in this target),
  mayenne.htm, league.htm, nevers.htm, bnf4715.htm mention the names; none carries a reading of ff.110, 123-124, 143,
  150, 154, 173, 196, 201, 276 or fr.15571 f.177/179. The live henryiii.htm (cryptiana.web.fc2.com/code/henryiii.htm,
  1 request) is identical to the snapshot in the whole fr.15572 section (normalised text diff: 0 lines): every target
  leaf still "undeciphered", with the same four openings.
- Cipher Mysteries (ciphermysteries.com/?s=Mayenne | Matignon | 15572): "Nothing Found" for all three.

(c) Plausible hits opened and read: Bourdeau's HEAD `targets/matignon1586/NOTES.md` (raw.githubusercontent.com,
1 request; the SOLVERDIFF-BOURDEAU flag of 2 Oct 2026 00:22 UTC) -- "Status: in progress. Read in part, measured
22 Sept 2026: 28% of the target's cipher tokens read as sense"; "Prior art checked: no printed decipherment of these
despatches was found (searches on the BnF catalogue and on the literature, 17 Sept 2026)"; per-leaf partial readings
(f143 "about half read") of his own, already cited in this file as the key's source (bMAT, 26 Sept 2026) -- a partial
modern cryptanalytic reading, not a found-solved. Snapshot: `sources/cyphersolver/2026-10-02/matignon1586/NOTES.md`.
api.github.com (contents listing) and github.com (commits atom) answered 403, one request each, not retried, so his
HEAD commit id is not recorded. PR #29 is this repository's own second-opinion PR (not external). No other hit was
about this item.

Result: no decipherment or plaintext of this item located by these queries on 2 Oct 2026; status word stays
`partial`. Requests: WebSearch 9, scienceblogs.de 3, cryptiana.blogspot.com 3, ciphermysteries.com 3,
cryptiana.web.fc2.com 1, raw.githubusercontent.com 1, api.github.com 1 (403), github.com 1 (403); no 429 or challenge.

Gate re-run, 2 Oct 2026 02:09 UTC:
```
$ python3 tools/intake_gate_check.py matignon-mayenne-1586
matignon-mayenne-1586: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
(exit 0; was exit 1 before this section)
$ python3 tools/gaps_check.py matignon-mayenne-1586
OK keep-going matignon-mayenne-1586: keep going: 6 internal gap(s), 5 step(s) untried
```

## SPLIT-matignon-mayenne-1586 (2 Oct 2026, account-4)

Brief: `.claude/briefs/runs/2026-10-02-account4-split-check.md` -- the glued-digit image check of this target's 31 rows in
`ciphers/_triage/split-check-1-Oct-2026.tsv`. Session started 02:44 UTC (clock read); 0 of the 4 allowed vision calls used;
no Gallica fetch (the brief's own rule, after the host reset twice from the cloud on 26 Sept, bMAT1F).

**Result: 0 of 31 rows reached -- no image on disk for any flagged position.** Every flagged token falls on one of the 13
Cipher-1 leaves (fr.15572 ff.110, 123r, 123v, 124r, 124v, 143r, 143v, 150, 154, 173, 196, 201 and fr.15571 f.177), and none
of those leaves has an image on disk: `images/` holds only fr.3974 f.24r/v (`f3974/`, a retired sibling, MAT-3974), fr.15572
f.78v/79r (`f78v_79r/`, the crib leaf) and fr.15571 f.179 (`f179_gallica_native.jpg`, `BnFfr15571f179.jpg`, Cipher-3); the
cyphersolver snapshots (`sources/cyphersolver/2026-10-01/`, `2026-10-02/matignon1586/`) carry no images. So no crop was cut,
no subagent was called, `corrections.tsv` was not created, and `ciphertext.txt`, `key.tsv`, both readings and the grade
counts are unchanged: **H 10,074 / M 1,648 / U 1,272 before and after**; `python3 tools/decode_key.py
ciphers/matignon-mayenne-1586 --check` exit 0. Hits checked 31 labels / 1,086 occurrences; confirmed splits 0; kept as
one token 0 (nothing was seen); not reached 31 (all).

**What the 31 rows are** (`split_worklist.tsv`, regenerated by `split_worklist.py` from the triage TSV and `key.tsv`,
`--check`-able; 31 labels, 1,086 occurrences -- the same 1,086 the Remaining gaps section counts on "31 sign labels absent
from key.tsv"). The tool's own `splits` column is filled for two labels only, because `--split-check` cuts digit strings;
the worklist applies the same cut to letter labels and ranks the rows as the brief ranks them:
- **Full split candidates** (every part a key code), 7 labels, 21 occurrences: `fe` x6 (f|e = c|u r), `de` x5 (d|e = s r),
  `me` x5 (m|e = t r), `37` x2 (3|7 = e o), `73` x1 (7|3 = o e), `Bi` x1 (B|i = i|y i|e), `f3` x1 (f|3 = c|u e). An image
  pass checks these first.
- **Compound labels** (one part keyed), 6 labels, 28 occurrences: `D2` x16 (D|2), `BOX2` x6 (BOX|2), `16` x2 (1|6), `s1` x2
  (s|1), `121` x1 (12|1), `18` x1 (1|8). D2/D and BOX2/BOX are the unmarked variants the Remaining gaps section already names.
- **Absent labels** (no cut into key codes), 18 labels, 1,037 occurrences: U 343, z 296, 4 106, w 83, T 53, y 41, v 37, p 18,
  5 16, 2 12, 9 11, 1 10, W 5, p9 2, 101, 102, O, u (1 each). These are unkeyed signs, not glued pairs; `--split-check` lists
  them only because they are not in the key, and only a key extension (the Remaining gaps Verdict step) or a re-read against
  the image can move them. They are not split-check work and are carried in the worklist for completeness.

**Evidence on file about the three digit tokens, short of an image (an observation, no value committed, M at most):** 37
and 73 lie in the numeric range this cipher uses for two-digit word codes (12 il ... 104; Bourdeau's key has 76/82/84/98 as
names and 68, 79 unresolved), and both `37` occurrences close a line after the same eight-sign run (`f196-3` ... a E .v. a
E x 6 m 37; `f201-5` ... a L o .v. a E X 6 m 37; f.201 is the same despatch as f.196, Bourdeau's measure note, snapshot
2026-10-02 NOTES.md). A word code at a line end in parallel text fits better than two letter codes `e o` written together;
`73` sits between `24 e t` (nostre r e) and `h B n x` (e i|y l e) on fr15571-f177-6, where `o e` makes no run either. The
labels `fe`, `me`, `de` coincide with French function words or fragments; whether each is two cipher signs transcribed as
one, one sign, or an interlinear clear word, only the image shows. None of this is a correction: the image decides
(CLAUDE.md Usage 8, the Mercy lesson).

**Judge (rule 7; the same rendering as every prior figure on this target, `reading_letters.txt`):**
```
$ python3 tools/judge_plaintext.py specs/matignon-mayenne-1586.json --file ciphers/matignon-mayenne-1586/reading_letters.txt
FAIL language: score=-1.371, null_p99=-1.942, real_p05=-0.837, real_median=-0.779, mode=both, N=12485
ok   words: cover=0.814, min=0.3, real_text_median_cover=0.947
```
Unchanged since bMAT (26 Sept 2026). `reading.txt`, which renders unkeyed tokens as `[U]`, scores -1.567 / cover 0.715
through the same judge -- a rendering difference, not a change in the reading.

**Not reached (all 31 rows) and the named next step.** No image on disk for any of the 13 Cipher-1 leaves. For whoever next
holds a Gallica allowance (or the owner's desk runner, if the host resets again): the regions that settle the 7 full split
candidates first -- f.196 line 3 and f.201 line 5 (both end in `37`); fr.15571 f.177 lines 2, 3, 5, 6 (`de`, `f3`, `me`,
`73`); then f.123v lines 20/35, f.124r line 9, f.124v line 8, f.150 line 6 (`fe`), f.173 line 29, f.201 lines 1/13 -- about
10 native line crops over 7 leaves on btv1b9061879d (canvas located with `tools/gallica_folio.py --anchor`, f.78v/79r =
canvas 85) and btv1b90618802 (f.177; f.179 = canvas f187), cut with `tools/iiif_lines.py`, one blind subagent call per
leaf's crops asking only "one group or two, and which signs", 7 vision calls, ~$4. A confirmed split then goes into an
`exceptions.tsv`-shaped `corrections.tsv` (position, original token, corrected tokens, grade, source), never into
`ciphertext.txt`. PROGRESS.tsv: no count moved, row untouched. Status word unchanged: `partial`.

Gate lines, 2 Oct 2026 (clock read at the run):
```
$ date -u   # 2026-10-02 02:54 UTC
$ python3 tools/decode_key.py ciphers/matignon-mayenne-1586 --check
ciphertext.txt: tokens 12994: H 10074, M 1648, U 1272
reading up to date   (exit 0)
$ python3 ciphers/matignon-mayenne-1586/split_worklist.py --check
split_worklist.tsv current   (exit 0)
$ python3 tools/gaps_check.py matignon-mayenne-1586
OK keep-going matignon-mayenne-1586: keep going: 6 internal gap(s), 5 step(s) untried   (exit 0)
$ python3 tools/intake_gate_check.py matignon-mayenne-1586
matignon-mayenne-1586: partial (line 1) -- edition/page or full-text-search citation found within 6 lines   (exit 0)
```

## Premise check (GF4-BATCH5, 3 Oct 2026)

The adversarial pre-reading pass (`.claude/briefs/check-solved.md` "## Premise check"). Its aim was to show the
unread leaves are already read: Cipher-1 ff.110, 123-124, 143, 150, 154, 173, 196 and 201, fr.15571 f.177, and
Cipher-3 f.276 and fr.15571 f.179. No cryptanalysis or transcription was done. Result: **not found**. No period
decipherment, clear copy or printed plaintext of any target leaf turned up. One other solver's partial modern
readings are now cited. Status unchanged (`partial`).

- **(a) Decipherments the folder already mentions: found, already known; none covers a target leaf.**
  - Tomokiyo's list was re-read in full from `sources/cryptiana/web/henryiii.htm`. On 2 Oct the live page was
    identical to this snapshot (Web and blog check above).
  - Cipher-1 decipherments: f.14 in f.15, ff.18-21 in f.19, ff.78-79 in the margin, ff.91-92 in the margin. Each
    is a different letter from the target leaves. Every target leaf is "undeciphered".
  - Cipher-3 decipherments: f.189 in f.190, ff.277-278 in ff.279-280, f.282 in the margin. f.276 and fr.15571
    f.179 are "undeciphered".
  - The f.179 magenta annotation was settled as Tomokiyo's modern overlay (bMAT3, 26 Sept), not a period gloss.
  - Bourdeau's NOTES.md, "Prior art checked", reads: "no printed decipherment of these despatches was found".
  - So no mentioned decipherment is of a target leaf. The ff.91-92 margin is unopened; it is a sibling crib,
    already the Escalation's planned step.
- **(b) Other solvers' working files: found, partial modern readings, not a solve.** Fresh shallow clone on 3 Oct
  2026 of dbourdeau/cyphersolver, HEAD a4292cb (2 Oct 2026). `targets/matignon1586/NOTES.md` is byte-identical to
  our snapshot `sources/cyphersolver/2026-10-02/matignon1586/NOTES.md`. Its status line reads "in progress. Read
  in part ... 28% of the target's cipher tokens read as sense ... Cipher-3 leaves untouched".
  - **Not previously cited in this folder** (0 mentions before this section): his per-leaf reading files.
    `f123_124_reading.md`, `f143_reading.md` (recto "about two thirds", whole leaf "a quarter", f.143v not
    transcribed), `f150_reading.md`, `f154_reading.md` ("about half the cipher reads as continuous French"),
    `f173_reading.md`, `f177_reading.md` (24% of transcribed tokens, 20% of the leaf), `f196_reading.md` (45% /
    38%) and `f201_reading.md` (f.201 is the same despatch as f.196). Also `f110_status.md`, "the one leaf I could
    not read".
  - These are another solver's partial cryptanalytic readings made with the same key (Bourdeau, CC BY 4.0). They
    are not a period decipherment or a full reading of any leaf. Any reading this target later reports overlaps
    them and must be compared and credited against them (rule 8; a verifier's N-class question, rule 10).
  - aaymeloglu/unsolved-ciphers was re-cloned on 3 Oct 2026 (HEAD d2800bb, 27 Sept): no matignon/mayenne/15572 hit
    beyond those logged on 26 Sept.
- **(c) Physical neighbours: not found, one sub-check left open.** Gallica btv1b9061879d, canvas numbers from
  Bourdeau's NOTES.md (f.276 = canvas 285 right; ff.277-278 = canvases 286-287; ff.279-280 from canvas 288),
  fetched this pass at 1200-1600 px:
  - Canvas 285: the left page is a sealed address panel with an endorsement, no cipher and no clear text. The
    right page is f.276, a small slip of about 27 lines wholly in cipher, with no interlinear and no margin note.
  - Canvas 288: f.277v and f.278r are wholly in cipher, with no gloss.
  - Canvas 289: f.279r is the period clear text. Its first line, read at 1600 px, grade M: "Monsieur Forget s'est
    allé ... [?Monsieur du Mayne] a Bordeaux". That is **not** Tomokiyo's f.276 opening ("La Guiolle est en doubte
    du pu pour les amis de la Roussiere ..."). This fits Tomokiyo's statement that ff.279-280 decipher ff.277-278,
    not f.276. The left page is a blank verso with a docket.
  - **Not checked:** whether any passage further into ff.279-280 repeats f.276's text. The clear mentions
    "Eguillon" (Aiguillon) and powder, and Tomokiyo's "La Guiolle" may be the same place. A line-by-line
    comparison of f.279-280 against Tomokiyo's f.276 opening is the named sub-step; it is a reading job, not done
    here.
  - The Cipher-1 leaves' own neighbours were not re-imaged. Bourdeau's leaf-by-leaf canvas table (his NOTES.md)
    records no decipherment beside any of them, and the SPLIT job found no image of them on disk.
- **(d) Recipient side: not found.** The letters are addressed to Villeroy and Henri III.
  - IA full-text search (be-api, all items) for the openings and names: `"en quelle peine nous estions"` (Tomokiyo's
    f.154 opening; 2 hits, both Calvin, unrelated), `"La Guiolle" Roussiere` (topographical dictionaries only),
    `Bellebourg Mayenne 1586` (0) and `"Matignon" "Forget" 1586 "Villeroy" lettres chiffre`.
  - The last query found Ehrlich, *The Letters and Documents of Armand de Gontaut, baron de Biron* vol. 2 (IA
    `lettersdocuments0002biro`, lending-only; searched inside with be-api fts on "15572", "Forget à Villeroy",
    "Forget", "Mayenne", "chiffre" and "Castillon"). It prints letters from **fr.15572 ff.284, 291, 298, 303, 334
    and 351**, among them Forget to Villeroy, camp before Castillon, 18 July 1586, f.351. **None is a target
    leaf.** Its "chiffré ... déchiffrement en marge" notes concern Biron's own letters (B.N. fr. 23195 and
    others).
  - Henry and Loriquet, *Correspondance du duc de Mayenne* (Reims, 1860-62; Google Books API, keyed, country=US)
    begins 11 Nov 1590, outside 1586.
  - Already logged above: the SHF *Lettres de Henri III* are not on IA, and the 1749 Villeroy-to-Matignon
    *Lettres* run in the opposite direction and are still unchecked.

**Named next steps (not run, outside this brief).**
1. [run 3 Oct 2026, A2P4-MATIG: NO MATCH, see section below] Compare ff.279-280's clear text against f.276. Read f.279r-280 at native resolution and test Tomokiyo's f.276
   opening and the "La Guiolle"/Aiguillon question. A match makes f.276 found-solved through a period decipherment.
   About $2, one native fetch and one read.
2. The verifier for any future reading diffs it against Bourdeau's per-leaf reading files listed in (b).

Hosts this pass: gallica.bnf.fr 3 (IIIF, canvases 285, 288 and 289), be-api.us.archive.org 14, archive.org 3
(advancedsearch 2 and metadata 1; the lending-only djvu text answered 401, not retried), www.googleapis.com 2,
github.com 2 clones. All requests were at least 1.6 s apart, with no 429 or challenge. Images:
`images/premise/c285_1200.jpg`, `c288_1600.jpg`, `c289_1600.jpg`. Rule 10: this is a search log; it makes no
novelty claim.

`python3 tools/intake_gate_check.py matignon-mayenne-1586` (after this section):
```
matignon-mayenne-1586: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
exit 0
```

## A2P4-MATIG (3 Oct 2026, account-2 worker, LANE-A2PUSH4): ff.279-280 clear text vs f.276 -- NO MATCH

Named next step 1 of the Premise check. Pre-registration `premise/prereg_f279.md` (commit a357a7a3, pushed before
any read); scorer `premise/match_f279.py` (rule fixed by the prereg). Intake gate (run first):
```
matignon-mayenne-1586: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
exit 0
```
Crops (pasted before the first vision call; Gallica btv1b9061879d has no folio labels, canvases from the Premise
check: 289 = f.278v blank + f.279r, 290 = f.279v + f.280r):
```
python3 tools/iiif_lines.py --ark btv1b9061879d --canvas 289 --region 5100,1060,2950,4560 --out ciphers/matignon-mayenne-1586/images/f279 --prefix f279r --distance 100 --lines-per-crop 2 --debug
python3 tools/iiif_lines.py --ark btv1b9061879d --canvas 290 --region 1450,1100,2850,4700 --out ciphers/matignon-mayenne-1586/images/f279 --prefix f279v --distance 100 --lines-per-crop 2 --debug
python3 tools/iiif_lines.py --ark btv1b9061879d --canvas 290 --region 4900,820,2980,3050 --out ciphers/matignon-mayenne-1586/images/f279 --prefix f280r --distance 100 --lines-per-crop 2 --debug
```
(A first canvas-289 cut at region 4080,1230,4000,4900 clipped line 1 and was discarded before any vision call.)

Vision calls (4, the brief's maximum; Sonnet subagents, one crop batch each): f.279r blind pass A and pass B
(30 crops each), one reconciliation against the crops (`premise/f279r_reconciled.tsv`, 30 lines, 392 tokens,
39 wildcards, about 106 words settled from the image), and the spare on f.279v + f.280r as a single pass
(`premise/f279v_passA.tsv` 27 lines / 332 words / 166 [?]; `premise/f280r_passA.tsv` 17 lines / 219 words /
144 [?]). The hand is a fast secretary hand; all three readers called it poor. About 950 words transcribed in
all; cost per 100 words is the orchestrator's figure (get_session), not given here.

Result (`python3 premise/match_f279.py premise/f279r_reconciled.tsv premise/f279v_passA.tsv premise/f280r_passA.tsv`):

| text | tokens (wildcards) | f.276 crib (gate >= 4/5) | C1 f.143 | C1 f.111 | C1 f.260 | C2 f.282 margin | C3 planted |
|---|---|---|---|---|---|---|---|
| f.279r pass A | 388 (84) | 2 | 1 | 1 | 0 | 0 | 5 |
| f.279r pass B | 384 (55) | 2 | 1 | 2 | 1 | 0 | 5 |
| f.279r reconciled | 392 (39) | 2 | 1 | 1 | 1 | 0 | 5 |
| f.279v + f.280r (one pass) | 558 (91) | 2 | 1 | 2 | 0 | 0 | 5 |
| ff.279r-280r together | 950 (130) | **2 -- NO MATCH** | 1 | 2 | 1 | 0 | 5 |

Controls valid on every row (C1 and C2 below the gate, C3 = 5). The target's 2/5 is itself spurious: on f.279r
it is "riviere" within edit distance 2 of "roussiere" plus one "grand" ("fort grand", l.4); "amis", "nombre" and
any "doubte" in order do not occur. So **ff.279r-280r do not carry Tomokiyo's f.276 opening**; f.276 is not
found-solved through this period decipherment. Conditional: f.279v/f.280r rest on one weak pass (about half the
words [?] or doubtful), and f.280v (canvas 291 left) was not read; a Tomokiyo opening is a modern paraphrase (M).

What the clear text is about (interpretation, from the passes, names at the readers' firmness): Forget reports to
Monsieur du Mayne [Mayenne] at Bourdeaulx; crossing the Dordongne and Garonne, powder left at "[E]guillon"
(f.279r l.11), Verdun, Thoulouse (f.279r); Saint Be[at]?, Comminges, Montauban, Turenne, the Roy de Navarre,
Bourdeaux (f.279v); Bellisle at Bourdeaux, Mayne (f.280r). That is a Guyenne campaign despatch consistent with
Tomokiyo's statement that ff.279-280 decipher ff.277-278. Secondary question ("La Guiolle" = Aiguillon?): f.279r
l.11 does name Aiguillon (spelled with a doubtful initial, "[E]guillon"), but no token near "Guiolle" or
"Roussiere" occurs anywhere in ff.279r-280r; whether Tomokiyo's "La Guiolle" on f.276 is Aiguillon is not decided
by this text (interpretation only, no grade).

Grades (rule 4): 0 cipher tokens read; this is a transcription of period clear text, not a decipherment, so no
H/C/S/M/I counts apply; the transcribed words are reading-grade only (firm vs [?] as counted above).
Hosts: gallica.bnf.fr 5 requests (IIIF: canvas 289 region twice, canvas 290 at 1200 px once, canvas 290 two
regions; at least 2 s apart, no 429/challenge). Report: found -- ff.279-280 read as the
ff.277-278 despatch; not found -- any f.276 text in ff.279r-280r.


## D2B-MATF110 (6 Oct 2026, account-2 worker, LANE DEFAULT-account-2-20261005-2217): f.110 line-crop sample, label-collapse gate FAILS for every label
Pre-registered before any pass: `f110crops/PREREG.md` (commit 859e5757b). Material: f.110 = Gallica btv1b9061879d canvas 116,
right page (Bourdeau's folio table); 2 requests to gallica.bnf.fr (info.json and a 1200 px overview), plus 1 native region
via `tools/iiif_lines.py --ark btv1b9061879d --canvas 116 --region 4780,300,3330,560 --centres 156,208,258,312,371,431`
(one earlier call failed HTTP 500 because I passed the ark with a doubled `ark:/12148/` prefix; that was my error, not the
host's). Crops in `images/f110/` (manifest.json). Image lines map to f110-1, -2, -3, -4 and -5 (image line 3 straddles two rows and
matches nothing; `f110crops/score.py` assigns each image line to its nearest Bourdeau line by edit distance).
Two blind Sonnet passes (A, B), 3 calls each, used bMAT1F's protocol (`f110crops/PASS_BRIEF.md`, f.78v reference sheet). Neither
saw ciphertext.txt or key.tsv. All six calls flagged most tokens uncertain: the native crops are only ~52 px tall.
Reconciliation was the script, `f110crops/score.py` -> `f110crops/score.json`.
- **G0 known-answer control (exact reproduction of Bourdeau's keyed labels, gate >= 50%)**: A 55.7% (192 keyed positions),
  B 58.4% (173). Passes, marginally. Same-key-value rate: A 57.8%, B 59.0%. A-B agreement on 195 positions both aligned: 58.5%.
- **G1 per label (both passes give the same keyed K on >= 60% of instances, K >= 3x its background rate)**: fails for every label
  with >= 4 aligned instances. T (n=5): A T 5/5, B T 5/5. Both passes read the T glyph as the chart's own `T`, not as `T=` or
  `t`. z (n=13): A z 2, B z 6, no keyed label in either top slot. BOX (n=8): A writes `BOX2` 5, B writes `BOX` 4 (H 4/11
  overall). Both labels are unkeyed, and the passes disagree. U (n=5): A Y 2, B U 2. w (3), 4 (1-2), p (2) and v (0 in lines 1-5)
  are too few for the gate at this sample size.
- **G2 crib (Tomokiyo opening via openings_alignment.tsv)**: 0/3 (BOX), 0/1 (z, T, U) for the passes' top labels. No support.
- **Outcome**: no label collapses onto a key.tsv label. key.tsv and ciphertext.txt are unchanged, and `tools/decode_key.py . --check`
  reports "reading up to date" (H 10,074 / M 1,648 / U 1,272). Read at grade I (image check, not a reading): at ~52 px native,
  blind passes keep T, z and BOX as their own chart shapes, not as barred/crossed keyed variants. The cheapest form of the
  "unmarked variant" idea therefore gets no support for these three labels. It is not refuted: A-B agreement is 58.5%, far below the 90% that
  TRANSCRIPTION.md wants. For 4/4+, w/w- and p/P the sample is untestable at this N (too few instances).
- Request count: gallica.bnf.fr 4 (info.json, overview, 1 failed region with the bad ark, 1 region). Subagent calls 6 (Sonnet).
- Next (per TRANSCRIPTION.md, a split > 10% between two passes goes to a person, not a third machine pass): f.110's BOX / z / T / U /
  w / 4 glyphs go to the owner's sign sorter (`tools/sign_sorter.py`), seeded with these crops, to settle whether they are distinct
  signs. Without that, a re-crop at higher effective resolution (taller bands, `--follow-slope`) is the only machine instrument left.

## While waiting (9 Oct 2026, WAIT-PASS-4)

Waits on: the owner's pass on the re-cut f.110 sign sorter (ASKS 146, filed 6 Oct 2026; R7-MATSORT, R8-MATCUT). Nothing below touches f.110 or its labels.
- [retired 19 Oct 2026: found-solved elsewhere, alejandrozarco PR #25; section "Found solved elsewhere"] Cipher-3 f.179: fetch Tomokiyo's henryiii_Matignon3.png (1 cryptiana request), crop images/f179_gallica_native.jpg with tools/iiif_lines.py --image, two passes + decode; M
- Nomenclature: test Tomokiyo's 76/82/84/98 (roi de Navarre, Condé, Turenne, Montauban; henryiii.htm, on disk) at every occurrence with `tools/decode_key.py . --try 76=...`, accepted values M, never a direct key.tsv edit (MQS-CROSSWORD rule); S
- Siblings: locate and crop the f.91-92 Cipher-1 letter with its margin decipherment (Tomokiyo l.638; Escalation "siblings" and "clear-pages", planned, not run) as a fresh crib independent of f.110, `tools/gallica_folio.py --anchor` then `tools/iiif_lines.py`, when Gallica answers (403 on 9 Oct); M -- located and cropped 15 Oct 2026 (MAT-NOM, section above; `f91/`), transcription next

## MAT-F91B (15 Oct 2026, account-2 worker, LANE DEFAULT-A2-0509-15)

Brief: `.claude/briefs/runs/2026-10-15-ytbiz-default-0509-jobs.md` job MAT-F91B. Times by `date -u`: 06:25-06:3x UTC. PREREG addendum
`f91/PREREG-MAT-F91B.md` pushed 9b9908566 before any --try or read; `tools/prior_work.py` record 7e6d984a6 (plaintext KNOWN = the period gloss
used as the known answer; step LEAD).

**(a) --try of U=e, T=r, D2=a, BOX2=u: non-test.** The pre-registered power control ran first (`f91/try_power_f91b.tsv`): a wrong letter
on four H codes matched by count (4+=n, lam=c, 3=i, b=i). 3=i was **accepted** (statistic 69.1 bits vs null p95 9.9 / -4.1), and the wrong
values out-scored the key value on 3 of 4 codes (4+=n +808.8 bits over m, rejected only by the breakage rule). By PREREG this makes the
instrument non-discriminating on this target's current reading, so no candidate is accepted. For the record (`crossword_log.tsv`): U=e
reject, T=r reject, D2=a accept, BOX2=u reject. No key.tsv, reading or grade change. HYPOTHESES.md row.

**(b) Blocks C and F: transcription below quality, no alignment run.** Regions re-measured on the native canvas c98 (1 openapi.bnf.fr
request, 200; image in scratch only, sha1 dfec5334...): `blocks.tsv` F is offset like E (its "gloss" region 5130 is the cipher's left
part). Corrected native regions, x,y,w,h: **C cipher 1480,1050,3100,1380** (13 lines, line 13 = cipher + clear "Oultre que ... de
Haultfort"), **C gloss 900,1040,860,1580** (21 lines); **F cipher run 1 5250,2685,2860,840** (9 lines, line 1 opens with clear "forcer a
l'en dessouz de bos ennemie", line 9 ends in clear "J'ay"), **F cipher run 2 5250,3800,2860,240** (2 lines, the second ending in clear
"Ensuyvant Sire j'ay faict"), between them three clear lines ("Par deca ... de Montbrault", "fortifier ...", "qui seroit peut estre ...");
**F gloss 4460,2640,840,1560**; **E cipher about 5255,1240,2850,600** (5 lines, line 1 opens with clear "bas meilleur"), **E gloss about
4490,1320,750,560**. Strips (`f91/strips_f91b.py`, line centres by row ink profile, which agree with `tools/iiif_lines.py`'s bands within
10 px) were cut at centre +-75 px and scaled to 2400 px, which put most of each neighbour line in every strip. Two blind Sonnet passes
(4 calls, `f91/PASS_BRIEF_F91B.md`, `f91/passA_f91b.tsv`, `f91/passB_f91b.tsv`) agree **367/813 = 45.1%** (`f91/agreement_f91b.tsv`), against
MAT-F91's 80.5%. Pass B reports it confused the line-to-image mapping for C1-C5 and copied C2 into C1, and read F11 as clear. Below the
PREREG's working quality, so neither reconciliation nor alignment was run (no R, no control number). This is a cropping fault, not a
measure of the hand. Gloss C read once by eye (Opus, M wording, not checked, not committed as a TSV): "auec sa compagnie de gendarmes / le
secours que luy fera de la / Guienne le S[ieu]r d'Aubeterre / il les forcera qu'ilz pourront / assemblez dans le pays ... / les pourra
conduire jusques / sur la riviere ou le S[ieu]r de / S[ain]t Supplice les recueillera / auec la Guienne et les ... / conduiront dans le
Lim[osin] / jusques a ce que j'espere / renvoye quelque bonne force / de l'armee pour les y / amener estant pour cest / occasion les
entreprises / ... / promener les compagnies / des hommes d'armes d'Ital[ie] / et pourueoyr a leur payement / car autrement il est certain /
qu'elles se debanderont par[tout]". The F gloss was not read.

Stopped at the brief's pricing line: 4 Sonnet calls (~2.4) + 6 Opus looks (~6) is past 80% of the cap of 6, so no re-cut, no third pass and
no block E. Requests: openapi.bnf.fr 1 (200). Next: re-cut C and F at centre +-50 px as two half-line segments each (as MAT-F91 did, 0
requests if c98 is re-fetched once, `regen_f91.sh`), then 2 blind passes + reconcile + F gloss read + the PREREG alignment (~$5); E with the
regions above (~$2). A --try of the gloss candidates needs a different instrument (the --try window score failed its power control here).

## MAT-EYE (15 Oct 2026, account-2 worker, LANE DEFAULT-A2-0810-15)

Eye check by the worker (no subagent), 09:56-10:1x UTC by `date -u`. Images (scratchpad only, not committed): openapi.bnf.fr fr.15572
btv1b9061879d c116 region 4700,250,3500,2300 (f.110), c150 full/max (f.143r, right page), c151 full/max (f.143v); 3 requests, all 200,
>= 3 s apart; plus the committed f.110 line crops `images/f110/` and the f.78v chart crops `images/f78v_79r/ref/`. Per-token log:
`eye/mat_eye_obs.tsv`.

- **f.110 T (38 tokens, r at S).** L1 pos 26 at native resolution and about ten T shapes in lines 1-8 at 0.55x: every one a single
  top-barred T (no double bar, so not `T=`), the shape MAT-KEY described on f.91v/f.124v. The f.78v chart's T (`7 T s R`) is drawn
  `+`-like with a short stub above the bar -- a hand variant, not a different label on the evidence here. Matched: 1 at native, ~10 at
  reduced scale not aligned token by token; mismatched: 0; not eyed: about 27.
- **f.110 BOX (125 tokens, Bourdeau `BOX`, U).** 0 tokens are labelled BOX2 on f.110. The five eyed (L1 pos 21, 54, 57; L2 pos 12; two in
  the L5-6 strip) are the flat rectangle with an overhanging top stroke, the same shape as the f.78v chart's BOX2 (L2 pos 26) and the
  f.91 readers' BOX2; our own blind passes (`f110crops/passA_*`) already read them BOX2. Not applied: the brief allows only downgrades,
  and a BOX=u key edit needs its own `--try` at every occurrence with a control first (named next step).
- **f.143r D (19 on f.143r/v, a at H).** 9 of 9 eyed on f.143r (lines 1, 3x2, 6, 7, 8, 10, 11, 12) are a triangle, the D2 shape. D and D2
  both carry a, so the reading does not change; it is one more witness that the triangle reads a.
- **f.143r x (93 on f.143r/v, e at H).** 7 eyed (lines 1, 2, 3, 7, 8, 10, 11): a small letter x, distinct from U (the barred v/cross sign).
- f.143v: page fetched, not eyed (box); the f.143r sample carried all the D/x evidence above.

`tools/prior_work.py` (--item-spec folio=110,143r, --step-type key, --offline) was run late, after the image fetches, not before
the first priced step as the brief asked: exit 4, plaintext KNOWN (Bourdeau's key, the f.91 gloss), the LEADs this lane's own MAT rows.
Result: 0 mismatches, no token regraded, `tools/decode_key.py ciphers/matignon-mayenne-1586 --check` exit 0 (H 10074 / M 1648 / S 418 /
U 854, unchanged). Side observation for a later transcription pass, not acted on: in the f.110 strip of crop-line 5 a Bourdeau `A`
position shows a triangle, and Bourdeau's f.110 lines 6 and 7 share a long identical run (`w BOX h n t T 7 z o f e e`), possibly a
repeated line in his transcription; neither was checked further.

## MAT-BOX (15 Oct 2026, account-4 worker, LANE DEFAULT-A4-1035-15)

Brief: `.claude/briefs/runs/2026-10-15-acct4-default-1035-jobs.md` job MAT-BOX. Times by `date -u`: 11:10-11:3x UTC. PREREG
`box/PREREG-MAT-BOX.md` pushed 64a1b9e7a before any score or look; `tools/prior_work.py` (folio=110, step key, --offline) exit 4,
the LEAD a stale A2-0509 lane-level claim that does not cover BOX=u (only BOX2=u was tried before, MAT-F91B), log 0275e53e7.

**(a) `--try BOX=u`: rejected, power control passed.** `tools/decode_key.py --try` (fr16, window 8, nulls 100), one code per call.
- Scope A, f.110 alone (`box/make_f110.py` builds the copy; log `box/try_f110.tsv`): power control h=i (n 126) reject, o=u (128)
  reject, e=s (163) reject -> gate passed (no wrong value accepted). **BOX=u (n 125): statistic -535.6 bits vs the runner-up (I),
  null p95 -477.4 / -473.5: reject.** Vowel-class companions, reported only: BOX=a -837.4 reject, BOX=o -1235.7 reject.
- Scope B, whole text (`box/try_power_whole.tsv`; BOX=u in `crossword_log.tsv`): h=i (526) -1657.4, o=u (662) -4783.7, e=s (399)
  -1216.2, all reject (the key value beats the wrong one on every control) -> gate passed. **BOX=u (n 137): -526.9 vs p95
  -223.8 / 136.2: reject.**
- Caveat on power at f.110: the f.110 control h=i scored **+247.3 bits over the key's own e** and was rejected only by the breakage
  rule, so on f.110 the window score prefers a wrong vowel on an H code; f.110 still carries 450+ unkeyed tokens (z 158, w 73,
  4 58, v 35) and its leaf judge sits near its own shuffle (-1.704 vs shuffle max -1.769, `openings/leaf_judge.tsv`). The reject is
  a result of the registered instrument, not a strong negative on the shape identity: MAT-EYE's 5/5 BOX2 shape and MAT-KA's u
  (8/10 held-out, on f.91 blocks) stand as they were. No key.tsv, reading or grade change. Judge before = `openings/leaf_judge.tsv`
  (`judge_leaves.py --check`: current); after = unchanged (no value applied), not re-run.
- This is the second `--try` use on this target; the first (MAT-F91B) was a non-test (control accepted 3=i). This one passed its
  control, so rule 3's third-attempt clause is not reached, but the f.110 caveat above stands.

**(b) o / c label image check (worker's own eye, no subagent; `box/mat_box_eye.tsv`).** openapi.bnf.fr 2 requests (f116 region
4700,250,3500,450 for f.110 lines 1-3; f98 full/max via `f91/regen_f91e.sh`, sha1 94d007c8, not the recorded dfec5334 -- same
canvas, re-encoded), both 200, scratch only; plus the committed f.78v chart crops `images/f78v_79r/ref/`.
- **o covers two shapes.** Shape A: a small plain closed round o. Shape B: an a-like round with a right stem or tail. On f.92r
  block E the five o tokens of the conflict split exactly by shape against the period gloss: **A = gloss i at E2:14, E2:29 (2/2);
  B = gloss a at E2:26, E4:13, E4:34 (3/3).** Bourdeau's own f.78v chart labels three shape-B signs o (chart line 2 pos 15, 20,
  29); f.110 lines 1-3 carry both (A at 1:18, 3:21; B at 3:11, 3:25). Reading (M, one eye, 5 gloss witnesses on one block): the
  label o may merge two signs, one reading i and one reading a, which would explain MAT-F91E's conflict (o key i, gloss a 3/5) and
  the a-share in A/B/D (16/29) and C/F (11/28). Logged in HYPOTHESES.md with the witnesses; not resolved, no key edit, no regrade
  (the label itself matches; the value question needs a sort and a test).
- **c: 4/5 match** (open crescent, the chart's c at line 2 pos 33): f.110 2:17, 2:24, 3:16, f.92r E4:24. One candidate
  mismatch: f.110 2:25 (Bourdeau `c`) has the hooked curl of the chart's `e` (line 2 pos 34; also f.110 3:17 `e`) -- single eye at
  2x on a 1-request crop, not applied. The A/B/D c conflict (gloss l 8/9) was not re-eyed (blocks A/B/D need canvas 97; request
  budget kept).

Requests: openapi.bnf.fr 2 (both 200). Subagents: 0. Images in scratch only. Next: sort every `o` token on the f.91 blocks A-F
and f.110 into shape A / shape B (sorter or a two-reader blind pass with the two exemplars above), then MAT-KA's block-held-out
gloss test per shape (A = i, B = a) with its power control (~$2-3); the A/B/D `c` tokens re-eyed on canvas 97 against the chart
(~$1).

## MAT-OSPLIT (15 Oct 2026, account-4 worker, LANE DEFAULT-A4-1236-15)

Brief: `.claude/briefs/runs/2026-10-15-acct4-default-1236-jobs.md` job MAT-OSPLIT. Times by `date -u`: 12:45-12:5x UTC. PREREG
`osplit/PREREG-MAT-OSPLIT.md` pushed ee2c00674, addendum 1 + token list e1e49a3f5, both before the sort and any score.
`tools/prior_work.py` (folio=91-92,110, step key, --offline) exit 0, plaintext KNOWN (Tomokiyo l.640 = the f.91-92 margin decipherment).
Requests: openapi.bnf.fr 2 (`f91/regen_f91.sh`: c97 region, c98 max, sha1 dfec5334 = recorded), both 200, images in scratch only.

**Sort (blind, 2 Sonnet calls, labels only, no values, no gloss).** The 78 H-confidence `o` tokens of f.91 A-F (`osplit/sort_tokens.tsv`,
opaque ids, keyed by draft/line/position) were sorted A (plain closed round) / B (round with right stem or tail) / X, exemplars from outside
f.91 (f.78v chart o = B; f.110 1:18 = A, per MAT-BOX). Each sorter saw each line image with the line's label sequence, the o's replaced by
ids. Result (`osplit/sort_answers.tsv`, verbatim): **A 45, B 17, X 16**. Both sorters said most calls were weak: 44 of 78 notes say faint,
low or position unsure. Six X are my error, not the sorter's: the six o tokens of the MAT-F91 first-pass E draft pointed to line images my
join step never wrote, so they could not be sorted. f.110 was not sorted (record only in the PREREG; dropped given the sort quality).

**Tests (`osplit/mat_osplit.py`, `--check` exits 0; `osplit/mat_osplit_result.tsv`), MAT-KA's instrument with o masked:**

| run | test | statistic | control mean / p95 / max | verdict |
|---|---|---|---|---|
| gating (MAT-KA reader) | split: LOBO hits oA + oB | 23/56 = 0.411 | 22.7 / 23 / 25 (1000 per-block A/B relabelings) | **FAIL** (23 is not > 23) |
| gating | oA (cand. i) | 13/40 = 0.325, majority **a** | 0.175 / 0.300 / 0.375; power 7=o n40 20/20, fit 20/20 | would be S at a (flag); **M** (split FAIL) |
| gating | oB (cand. a) | 10/16 = 0.625, majority **a** | 0.135 / 0.375 / 0.562; power n=l n16 14/20, 20/20 | would be S at a; **M** (split FAIL) |
| secondary (E from f91e only) | split / oA / oB | same 23/56; 13/40; 10/16 | 22.7/23/25; 0.300; 0.375 | same |

Unsplit o (all A/B/X), for reference: held-out 24/65 = 0.369, all-block majority **a**. Folds for oA: a in every block (B 4/13, C 4/11).
Reading: the blind sort does not separate the gloss letters better than a random split of the same tokens, so the shape hypothesis is
not supported by this sort. Both sorted groups lean to gloss a, and so does o as a whole. That fits MAT-F91E's conflict (o key i, gloss a)
more than a clean two-shape split. But the sort is weak (44/78 low-confidence notes, 45:17 A:B where MAT-BOX's eye found 2:3 on block E),
so this is a FAIL of this sort, not a negative on the shapes. Grade M everywhere; no key.tsv, reading, grade or AUDIT change (the target has
no AUDIT.md). Side finding: MAT-KA's `signs` reader concatenates both block-E drafts (f91 E1-E4 and f91e E1-E5) against one E gloss
(PREREG addendum 1); here the secondary run without the duplicate gives the same split result. MAT-KA's own numbers were not re-run.
Next: settle the o shapes by a person (TRANSCRIPTION.md: an unsettled sign inventory goes to the owner's sign sorter), or per-token crops
cut at 3x around each o (not line images) for a second blind sort; then re-run `osplit/mat_osplit.py` unchanged (~$1.5). Separately, a
registered test of o = a against o = i on the f.91 blocks alone (the unsplit majority above was not a registered test) (~$1).

## MAT-O3X (15 Oct 2026, account-4 worker, LANE DEFAULT-A4-1236-15)

Brief: `.claude/briefs/runs/2026-10-15-acct4-default-1236-jobs.md` job MAT-O3X (second attempt at the o split). Times by `date -u`:
13:11-13:2x UTC. PREREG `osplit/PREREG-MAT-OSPLIT.md` addendum 2 pushed f11021383 before the re-sort and any score; gate, statistic,
control and grade rule unchanged from ee2c00674. Requests: openapi.bnf.fr 2 (`f91/regen_f91.sh`: c97 region, c98 max; c98 sha1 94d007c8,
the re-encoded copy MAT-BOX also got, 8722x6347 as recorded), both 200, images in scratch only; `regen_f91c.sh`/`regen_f91e.sh` reused c98.

**Crops.** `osplit/o3x_crops.py`: per-token windows (line strip with s1/s2 joined at manifest offsets, read-free column ink profile, column
estimated proportionally from draft position, +- 4 columns, 3x, no marker) for all 78 tokens of `sort_tokens.tsv`, with the reader label
sequence p-4..p+4 (labels only) to locate the target. The 6 first-pass E tokens now get strips from `regen_f91.sh`'s `f92r_ciE_L0n` crops
(MAT-OSPLIT's join error). Shape B exemplars: three windows of the committed f.78v chart line 2 (`images/f78v_79r/ref/`, pos 15/20/29);
shape A: words only (declared deviation, addendum 2: the committed f.110 line crops are 53 px high and 1:18 was not re-located).

**Sort (blind, 2 Sonnet calls, one sorter per token).** `osplit/sort_answers_o3x.tsv` (verbatim; o001 unanswered = X): **A 25, B 35,
X 17** (high-confidence 51 of 77 answered, against MAT-OSPLIT's 34 of 78). Agreement with MAT-OSPLIT's sort where both gave A or B: 29/48.

**Test (`osplit/mat_osplit.py --answers sort_answers_o3x.tsv`, unchanged instrument; `osplit/mat_osplit_result_o3x.tsv`, `--check` 0):**

| run | test | statistic | control mean / p95 / max | verdict |
|---|---|---|---|---|
| gating (MAT-KA reader) | split: LOBO hits oA + oB | **30/50 = 0.600** | 18.6 / 20 / 27 (1000 per-block A/B relabelings) | **PASS** |
| gating | oA (cand. i) | 11/21 = 0.524, majority **i** | 0.154 / 0.333 / 0.476; power n=l n21 beat 19/20, fit 20/20 | **candidate S at i** |
| gating | oB (cand. a) | 19/29 = 0.655, majority **a** | 0.167 / 0.345 / 0.379; power Ze=t n29 20/20, 20/20 | **candidate S at a** |
| secondary (E from f91e only) | split / oA / oB | 30/48; 11/20 i; 19/28 a | 18.6/20/27; 0.350; 0.321 | PASS; S at i; S at a |

Folds, oA: A i1/2, B i3/5, C i4/5, D i0/2, E i2/3, F i1/4; oB: A a3/4, B a4/6, C a2/5, D a4/5, E a1/2, F a5/7. Unsplit o: 24/65,
majority a (as before). Reading: on the f.91-92 margin decipherment (the period gloss, the known answer), the sorted shapes separate the
gloss letters far better than any random split of the same tokens (30 vs control max 27), and each shape's held-out value is the one
MAT-BOX's eye proposed: plain round o = i, round with a right stem or tail = a. **Grade per the PREREG: S candidates (oA = i, oB = a),
recorded in HYPOTHESES.md; no key.tsv, label, reading or grade change in this job** (the edit needs every `o` of the 13 leaves in
Bourdeau's transcription re-labelled by shape, which needs their images). No AUDIT.md exists for this target, so nothing to carry.
Limits: one sorter per token (no second blind reader), no shape-A exemplar image, window placement estimated (17 X), and only 50 scored
positions over six blocks; the per-block folds are small (2-7). MAT-OSPLIT's line-image sort failed the same gate, so the PASS rests on the
crop change; rule 3's third-attempt clause is not reached.
Next: a second blind reader on the same 78 crops (one Sonnet call, ~$0.6) to report reader agreement on A/B; then the o shape split over the
13 target leaves (Bourdeau's o tokens re-labelled oA/oB from line crops, or in the owner's sign sorter as two piles), and a `decode_key.py
--try` of o -> oA = i / oB = a at every occurrence with its control before any key edit (~$4).

## MAT-R2 (15 Oct 2026, account-4 worker, LANE DEFAULT-A4-1236-15)
Brief: `.claude/briefs/runs/2026-10-15-acct4-default-1236-jobs.md` job MAT-R2. Times by `date -u`: 13:35-13:4x UTC. PREREG
`osplit/PREREG-MAT-OSPLIT.md` addendum 3 pushed 61d695463 before the call and any score; gate, statistic, control and grade rule unchanged.
Requests: openapi.bnf.fr 2 (`f91/regen_f91.sh`, c97 region + c98 max; c98 sha1 94d007c8 as MAT-O3X) -- the brief said disk only, but the
crops are scratch-only and were not in this container; declared in ROOM take/release lines. Crops regenerated with `osplit/o3x_crops.py`
(78, same script, same windows); images in scratch only.

**Reader.** One Sonnet call, all 78 crops, crop paths + label context (labels only) + MAT-BOX's shape words + the f.78v chart line 2 halves
as B exemplar; no values, gloss, block or first-reader labels. `osplit/sort_answers_r2.tsv` (verbatim): **A 24, B 34, X 20**.

**Agreement with MAT-O3X (`sort_answers_o3x.tsv`):** on tokens both called A or B, **54/55, kappa 0.962** (one B->A); over all 78 on
A/B/X, 69/78, kappa 0.822 (disagreements are A/B vs X: 8, plus the one B/A). Per the addendum's descriptive reading (>= 0.6), the two readers
see the same split. Caveat: both readers are the same model family with the same exemplar and context, so agreement shows the sort is
stable, not that it is free of a shared bias; a person's sort is the independent check.

**Test (`osplit/mat_osplit.py`, unchanged; `--check` 0 on both result files):**

| answers | split S (control mean/p95/max) | oA | oB |
|---|---|---|---|
| R2 (`mat_osplit_result_r2.tsv`) gating | **28/48** (18.2/19/24) **PASS** | 10/20 maj i, p95 0.350, power n=l 20/20 -> **candidate S at i** | 18/28 maj a, p95 0.357, power Ze=t 20/20 -> **candidate S at a** |
| R2 secondary (E f91e only) | 28/46 PASS | 10/19 i, candidate S | 18/27 a, power c=p 3/20 FAIL -> too-short |
| consensus O3X+R2 (`mat_osplit_result_r2cons.tsv`) | 26/44 (17.3/18/23) PASS | 9/18 i, candidate S | 17/26 a, power c=p 0/20 FAIL -> too-short |
| (MAT-O3X, for reference) | 30/50 (18.6/20/27) PASS | 11/21 i, S | 19/29 a, S |

Reading: the split PASSes on the second reader's labels and on the consensus labels; oA = i holds at candidate S in every run; oB = a holds
at candidate S on each reader's full label set but its power code becomes too-short at the smaller consensus n (the power rule picks a
different frequency-matched code, c=p, below n 28), so oB's grade at consensus n is too-short, not a failure of held-out accuracy (17/26,
p95 0.346). **No key.tsv, label, reading or grade change** (both stay S candidates in HYPOTHESES.md). The 13-leaf relabel was not started.
Next: the o shape split over the 13 target leaves (Bourdeau's o tokens re-labelled oA/oB from line crops, or two piles in the owner's sign
sorter) and `decode_key.py --try` o -> oA = i / oB = a at every occurrence with its control before any key edit (~$4).

## MAT-ORL (15 Oct 2026, account-4 worker, LANE DEFAULT-A4-1441-15)
Brief: `.claude/briefs/runs/2026-10-15-acct4-default-1441-jobs.md` job MAT-ORL. Times by `date -u`: 14:52-14:5x UTC. PREREG
`orl/PREREG-MAT-ORL.md` pushed 8bca95a2d before any --try. Disk only: 0 requests, 0 vision units, 0 subagents.

**Relabel (`orl/make_orl.py coverage`).** The agreed labels (both readers A -> oA, both B -> oB; `osplit/sort_answers_r2cons.tsv`: A 22,
B 32, X 24) exist only for the 78 o tokens of the f.91-92 margin blocks. **On the 13 target leaves no o token is covered: 0 of 662.** All
662 stay o (key i, H), per the brief. A `--try` of oA / oB at every occurrence on the 13 leaves therefore has n = 0. It was not run: by
construction it is a non-test, not a result. The step MAT-R2 named ("re-label the 13 leaves' o by shape") needs the 13 leaves' own o
tokens sorted by shape first, from their images or in the owner's sorter. Line crops alone do not do it.

**--try on the only scope where oA / oB occur: an f.91 copy** (`orl/make_orl.py build`: blocks A-F, E from f91e only, draft signs below H
-> '?', 1,462 tokens, '?' 359 = 24.6%, oA 20, oB 28; key.tsv/decode.json unchanged, oA/oB unkeyed). `tools/decode_key.py --try`, fr16,
window 8, nulls 100, one code per call.
- Power control first (`orl/try_power_f91.tsv`): wrong letters on matched H codes, **n=m (n 25) -202.9, oo=f (17) -64.9, c=q (29) -424.7,
  s=a (28) -73.9: all reject -> gate passed.** (MAT-F91B's whole-text control failed. This scope's control passed. So rule 3's
  third-attempt clause is not reached.)
- Candidates (`orl/try_f91.tsv`): **oB=a (n 28): 72.1 bits over the runner-up E, null p95 positions -47.7 / value class -72.1: accept.**
  **oA=i (n 20): 24.5 bits over the runner-up NULL, below the positions null p95 33.3, breaks 8 of 20 occurrences: reject.**
- Swap, reported only: oA=a -159.4 (runner-up I) reject; oB=i -106.6 (runner-up A) reject. Each shape's own candidate beats its swap by
  184 (oA) and 179 (oB) bits.

Reading: on the f.91 blocks, read by a language model with no gloss, the stemmed shape reads a: oB = a at **S, for the 28 f.91 tokens
only**. That agrees with the held-out gloss test (MAT-O3X 19/29, MAT-R2 18/28). The plain shape prefers i over a (by 184 bits). But the
window score does not accept i over leaving the token empty (runner-up NULL), so **oA = i stays M** here. Its gloss-test support stands as
recorded (candidate S, MAT-O3X/MAT-R2). The copy's 24.6% unknown signs weaken the window score most for the short oA set. **No key.tsv,
ciphertext, reading or grade change:** oA / oB occur on 0 tokens of ciphertext.txt, so a key row would read nothing. `decode_key.py --check`
on the target: up to date. `openings/leaf_judge.tsv` is unchanged (no reading change). The target has no AUDIT.md, so nothing to propagate.
Rows: HYPOTHESES.md. The f.91 runs are logged in `orl/` and not in `crossword_log.tsv`, which logs whole-text runs.
Next: sort the 13 leaves' own o tokens by shape. Start with one leaf, f.154 (read share 259/1061, 3x per-token crops as `osplit/o3x_crops.py`
from a native fetch, two blind Sonnet readers + exemplars from the f.91 agreed set). Then run `--try` oB=a on that leaf with this PREREG's
power-control recipe before any key edit (~$4-5 per leaf). Alternatively, put the two piles in the owner's sign sorter (ASKS, no session cost).

## MAT-154 (15 Oct 2026, account-4 worker, LANE DEFAULT-A4-1441-15)
Brief: `.claude/briefs/runs/2026-10-15-acct4-default-1441-jobs.md` job MAT-154 (MAT-ORL's named next). Times by `date -u`: 15:11-15:2x UTC.
PREREG `o154/PREREG-MAT-154.md` pushed 506a3f00a before any reader call or score. `tools/prior_work.py` run first (`o154/prior_work.txt`,
exit 2 KNOWN = Tomokiyo's published f.154 opening, not used here). Requests: openapi.bnf.fr 4, all 200, with ROOM take/release lines
(c161 full/1600; c161 `pct:52.5,32.5,42,64.5/max` sha1 3416510e; c97 region and c98 max for the f.91 exemplars, sha1 dfec5334). Images in scratch only.

**Material.** f.154r = canvas 161 (foliation "154" on the overview; `o154/regen_o154.sh`). `o154/lines154.py` levels the region by the common
slope of the `iiif_lines.py --follow-slope` fits (-0.0163). (`--follow-slope` itself snapped three bands onto neighbouring lines and dropped
three others, so it was not used.) The row profile then gives **28 lines = Bourdeau f154-1..28**, checked by eye at both ends. f154-1's first 6
tokens sit on the clear line above. **47 `o` tokens** (`o154/tokens154.tsv`) were cut as 3x windows (`o154/crops154.py`, the
`osplit/o3x_crops.py` recipe) with label context p-4..p+4. Exemplars: f.91 consensus A o012, o017 and B o002, o004, regenerated by
`osplit/o3x_crops.py`.

**Readers (blind, 4 Sonnet calls: 2 readers x 2 batches of 21/26).** `o154/answers_r1.tsv`: A 44 / B 1 / X 2; `answers_r2.tsv`: A 44 / B 2 / X 1.
Every B call is low-confidence. No token is called B by both readers (p025 A/B, p040 B/A, p036 X/B).

| statistic | value | gate |
|---|---|---|
| tokens both called A or B | 44 (agree 42) | n >= 24: yes |
| Cohen's kappa, A/B on those 44 | **-0.023** | >= 0.6: **FAIL** |
| kappa, A/B/X over all 47 (reported) | 0.126 | -- |
| consensus | **A 42, B 0, X 5** | oB n >= 5: **too-short (0)** |

**Verdict by the PREREG: gate K FAIL, so no `--try` was run (`o154/agree.tsv`, `answers_cons.tsv`).** The kappa failure is the
one-class prevalence case, not reader disagreement. Both readers see f.154's `o` as the plain round shape on 42 of 44 tokens. With one class
that dominant, kappa has no room above chance. The registered too-short rule would have stopped `oB=a` anyway: no token on this leaf carries
the stemmed shape by consensus.

Reading, graded M: **on f.154, Bourdeau's `o` is almost entirely the plain round shape.** The stemmed shape that reads `a` on the f.91 blocks
(MAT-O3X/R2/ORL) does not occur under the `o` label here. So `--try oB=a` on f.154 is a non-test by construction (n = 0). This leaf neither
supports nor contradicts the f.91 result. Bourdeau's `o` = i (H) on f.154 is unaffected, consistent with GAPS2's known-answer check
(true letter rank 1 for 15/16 H labels on f154).

No key.tsv, ciphertext.txt, reading or grade change. No AUDIT.md. Rule 3: this is the first sort of a target leaf's own `o`, not a third
attempt at the same instrument.

Where f.154's stemmed shape may sit instead is a lead only, from the worker's own look at 6 of the windows, not from the readers: Bourdeau's
`a` sign on this leaf is a looped sign with a stroke. Whether it is f.91's oB is an image check (~$1).

Next:
- (1) that image check: Bourdeau `a` on f.154/f.143r against the f.91 oB exemplars (~$1);
- (2) if the two-shape `o` matters on any leaf, sort a leaf with a low read share whose `o` may be mixed (f.110, 3x crops of its o tokens,
  same PREREG recipe, ~$4) or put the f.91 two piles in the owner's sign sorter.

0 key edits; `decode_key.py --check` exit 0.


## Found solved elsewhere: Cipher-3 ff.179, 276 (19 Oct 2026, LANE BNF-FOCUS, account 2)

Found in the daily solver-repository re-screen of BNF-VALUE.tsv shelfmarks against dbourdeau/cyphersolver HEAD a03e5adda (the
per-key split of 14-15 Oct 2026). Matignon's **Cipher-3** leaves, which this folder listed as not-attempted gaps, are read in
Bourdeau's repository: work by **alejandrozarco** (PR #25, 6-7 Oct 2026; commits 72a4e80b and a3de56b4, 7 Oct), reviewed by
D. Bourdeau, now the separate entry `targets/matignon1586c3` (split from `matignon1586` under George Lasry's one-key rule).

| leaf | their result (their measure) | method (theirs) |
|---|---|---|
| fr.15572 f.276 | 706 of 734 signs read (96.2%); shuffled-key control median 6.9%, max 29.3% (50 draws) | read with Tomokiyo's Cipher-3 table, checked and extended |
| fr.15571 f.179 | 473 of 509 signs read (92.9%); control median 3.5%, max 23.8% | from Tomokiyo's interlinear decipherment, checked with his key |

Snapshot (unmodified): `sources/cyphersolver/2026-10-19-matignon1586c3/` (NOTES.md, f276/SOLUTION.md, f179/SOLUTION.md).
Credit: alejandrozarco; D. Bourdeau (review, measure); S. Tomokiyo (Cipher-3 table and the f.179 decipherment); G. Lasry (the
one-key split). Consequences here: the bMAT3 f.179 passes (section above, no reading committed) and the A2P4-MATIG f.276
premise test stay as logged; the While-waiting step "Cipher-3 f.179" is retired (found-solved elsewhere); this folder's
status stays `partial` for Cipher-1, which their `targets/matignon1586` still lists as in progress. Our screens of 13-18 Oct
grepped their tree for fr.3982/fr.3985 only and missed this 7 Oct read; the lane now crosses every BNF-VALUE.tsv shelfmark
and folio against their changed targets (lesson in BNF-VALUE.md wave 40).


## Cipher-1 and Cipher-2 contributions elsewhere (22 Oct 2026, LANE BNF-FOCUS, account 2)

- Cipher-1 (this folder's live work): dbourdeau/cyphersolver `targets/matignon1586` merged Michael Brackx's issues #64, #68-#71 (21 Oct 2026) and
  re-measured "39% of the target's cipher tokens read as sense (5,480 of ~14,082; 42% of the 12,994 transcribed; 32% after a
  scrambled-key control)". Status there "in progress, read in part". Any next step here reads their key_contrib.json and the
  control gap (39% vs 32%) first; values that agree with ours are corroboration, values that differ are rule-4 data conflicts.
- Cipher-2 (fr.15572 ff.218-219, fr.15573 ff.120, 385; outside this folder's leaves): dbourdeau/cyphersolver `targets/mayenne1586c2`, "read in
  part, contributed: 86.1% of 5,293 cipher tokens fall in runs of period French", AI transcription with no human sign check.
- Cipher-3 gains fr.15573 ff.379-381 (Brett Burford, issue #44) in their matignon1586c3.
Snapshots: `sources/cyphersolver/2026-10-22-matignon1586/`, `-mayenne1586c2/`. Status here stays `partial` (Cipher-1 below 50%
there too). Credit: Michael Brackx, Brett Burford, Harumi-Matsuba (issues #44, #46, #49, #51, #64, #68-#71); D. Bourdeau.
