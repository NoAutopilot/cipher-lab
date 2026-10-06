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

## Remaining gaps (finish-or-blocker pass, 1 Oct 2026)
Read so far: 1,406 of 12,994 transcribed Cipher-1 tokens (10.8%) sit in a sense run. Source: the proxy split in `resolve_mu.py` / `spans.tsv`, NOTES.md "NEAR step (1)" (bMAT2), recounted from `spans.tsv` + `reading_tokens.tsv` on 2 Oct 2026 00:50 UTC. Per leaf: f110 0/1699, f123r 23/1097, f123v 92/1251, f124r 84/1203, f124v 45/727, f143r 136/724, f143v 247/1182, f150 10/445, f154 259/1061, f173 168/1082, f196 168/840, f201 163/987, fr.15571 f.177 11/696. Grades are H 10,074 / M 1,648 / U 1,272, and the fr16 judge FAILs at -1.371 against real_p05 -0.837 (shuffled -1.78). The denominator is Bourdeau's partial transcription only: the spec says "13 leaves partly transcribed", and the untranscribed remainder of each leaf has never been measured. Cipher-3 (fr.15571 f.179, fr.15572 f.276) has 0 sign tokens transcribed. Bourdeau's own 28% (measure.py with his beam LM, 22 Sept) is not reproduced here. There is no AUDIT.md.
- fr.15572 ff.143r, 143v, 150, 154, 173, 196, 201 (7 Cipher-1 leaves, 6,321 tokens, U 129 = 2.0%, M 742) - blocker: not-attempted; the H key covers most of these tokens, but only 2-24% of each leaf sits in a sense run (`spans.tsv`). bMAT2's two-context rule and bMATBEAM's beam both pooled all 13 leaves (the f.78v/79r tests were crib work, not these leaves). bMATBEAM fitted its M choices jointly with U values that its own controls show are TOK/null noise, and committing them made the judge worse (bMAT1C -1.545, reverted in bMAT1D). Its own suggested per-leaf, read-context-only rerun was never made. An M-only rerun would be the second target run of the same beam, so pre-register its gate, and if it fails, retire the beam for this target rather than tuning it again; next: (GAPS 2 Oct 2026: per-leaf judge run, `judge_leaves.py` / `openings/leaf_judge.tsv` -- these 7 leaves score -1.158 to -1.293 against their own within-line shuffle max -1.806 to -1.846 (20 seeds), all FAIL the gate real_p05 -0.86 to -0.89); GAPS gap 1, 3 Oct 2026 (account-4, prereg bd74c69d): control (A) at each leaf's N reads M at 0.76-0.89 vs frequency 0.39-0.57 (gate a passes 7/7), but the judge-gain instrument fails its own known-answer power check on 6 of 7 leaves (control gain above its shuffle-null max on 5/21 seeds; the beam LM and the judge share catheri01), so 1/7 testable < 4: non-test at this N, beam neither licensed nor retired by the judge-gain instrument [retired: judge-gain gate for this beam, section "GAPS-matignon-mayenne-1586 gap 1 (3 Oct 2026)"]; f201 alone, for the record: +0.029 vs null max +0.078; GAPS2 3 Oct 2026 (prereg c26ff40d): agreement with Bourdeau's per-line decoder output (HEAD 4d32ec9) on f143r/f143v/f154/f173: beam 0.850/0.797/0.748/0.780 vs first-candidate 0.625/0.692/0.689/0.720 vs within-line shuffle null max 0.642/0.657/0.592/0.680, control power 3/3 seeds every leaf -- AGREEMENT SIGNAL 4/4 (agreement with another modern reading, not accuracy; section "GAPS2-matignon-mayenne-1586 (3 Oct 2026, account-4)"); GAPS3 3 Oct 2026 (prereg 0b58589a): the 167 changed M choices as S candidates in a scratch reading, re-judged per leaf: every leaf rises and stays above its letter-shuffle max (4/4), but the rise beats the beam's own shuffled-target rise on 1/4 leaves only (f143r +0.144 vs +0.124; f143v/f154/f173 +0.011/+0.011/+0.001 vs +0.057/+0.055/+0.053) -- NON-TEST, nothing committed [retired: judge-scored commit of the mu beam, third attempt, section "GAPS3-matignon-mayenne-1586 (3 Oct 2026, account-4)"]; next: grade the beam's M choices only against a non-LM reference -- the f.91-92 margin decipherment or the f.18/f.19 pair (gap 4's step), ~$12
- fr.15572 ff.110, 123r, 123v, 124r, 124v and fr.15571 f.177 (6 Cipher-1 leaves, 6,673 tokens, U 1,143 = 17.1%, read 0-7.4%) - blocker: not-attempted; f110 alone is 30% U and 0% read. Of the target's 1,272 U tokens, 1,086 fall on 31 sign labels absent from `key.tsv` (U 343, z 296, 4 106, w 83, T 53, y 41, v 37, p 18, D2 16, 5 16, ...) and only 186 on 17 '+' rows (BOX 137); recounted from `reading_tokens.tsv` 2 Oct 2026, and MAT-CCE's "1,272 over 19 codes" is wrong. Several absent labels look like unmarked variants of keyed ones (4/4+, w/w-, T/T=, D2/D, p/P, BOX2/BOX), and bMAT1F's two blind passes of f.79r split on exactly 4 vs 4+. New, not used before: Tomokiyo's published opening for "f.111" ("Monsieur de Villeroi vous verres bien par la lettre que je fais au roi...", `sources/cryptiana/web/henryiii.htm`, Cipher-1 section) lines up with our decoded f110-1. A scratch DP this pass scored 26 against a maximum of -9 over 20 within-line shuffles (f143r-1 28 vs 0, f154-1 20 vs -1). By eye, BOX, U and T fall on u, e, r, and several H positions read i for n/s and g for e/v. That is a known-plaintext check of the label-variant idea, at grade M (a modern published reading, credited to Tomokiyo). GAPS 2 Oct 2026: committed as `align_openings.py` with a 200-draw within-line token-shuffle control -- f143r 468 vs shuffle max -67, f154 66 vs 20, f110 33 vs -22 (f150 -50 vs -19, not aligned); but only 11 U tokens fall on a letter at all, all on f110 (BOX a 2 / u 1 / e 1, z i/o/s, w, U, T, p once each), so the tabulation has no power with this material -- untestable by this instrument, no value read (section "GAPS-matignon-mayenne-1586 (2 Oct 2026)"); the one lead is `8=g` 0/4 on f110. Bourdeau's HEAD NOTES.md read the same job (snapshot `sources/cyphersolver/2026-10-02/matignon1586/NOTES.md`): his glyph table gives ⊐ box and ꝉ crossed-t = u/v, ₸ crossed-4 = m, ƀ = i/j; GAPS2 2 Oct 2026 (03:4x UTC): his HEAD `key.json` (34e0fc8) fetched and diffed -- 87 rows, 0 added / 0 removed / 0 changed against `key.tsv`, and all 13 transcriptions token-identical to `ciphertext.txt`, so no new value exists in his key; his table's box = u/v (and T = u as a label guess) tested as an M hypothesis with a 19-other-letter control (`hypothesis_judge.py`): BOX=u ranks 10/20 on f110 (n 125), 9/20 pooled, T=u 14/20 -- but the same instrument recovers the true letter for only 1 of 10 keyed H labels on f110 against 15/17 on f143v and 15/16 on f154 (`openings/hypothesis_power.tsv`), so on f110, where 91% of BOX and 72% of T sit, this is untestable by this instrument, not a negative; no value committed; next: cut f.110 line crops with `tools/iiif_lines.py` (ark btv1b9061879d) and run two blind passes plus a reconciliation over a 4-line sample, ~$9
- untranscribed remainder of the 13 Cipher-1 leaves (extent unmeasured) - blocker: not-attempted; the spec and NEAR.md both say Bourdeau transcribed these leaves "only in part", and NOTES.md bMAT2 cites his separate read_of_transcribed and read_of_leaf figures, but no line or sign count of the full leaves is on file. Tomokiyo's opening for f.150 ("il estoit me besoins car je tourvai quil auoit") does not align with our f150-1 (scratch DP -14 vs shuffle median -15; confirmed with the committed `align_openings.py` 2 Oct 2026: -50 vs shuffle max -19 over 200 draws), unlike f110/f143r/f154, so our f150 may start elsewhere on the leaf. GAPS2 2 Oct 2026: his HEAD extent recorded from his "Coverage, measured" table -- f110 37/54 lines, f196 26/31, fr.15571 f.177 24/29, the other ten leaves complete; +2,648 tokens estimated untranscribed over the whole target incl. Cipher-3 (section "GAPS2" (d)); next: count lines per leaf on Gallica canvases of btv1b9061879d against `ciphertext.txt`'s line counts and list the untranscribed lines, ~$2
- Nomenclator number codes on key.tsv '+' rows (62 x10, 33 x8, 49 x5, 44 x4, star/15/36 x3, 46/53/27/68 x2, 54/hash/88/104/79 x1 = 49 tokens) plus singleton absent labels (121, 102, Bi, u, f3, 73, 18, 101, O) - blocker: open-codes; each occurs 1-10 times in the proper-name range. Tomokiyo's list gives 76/82/84/98 as roi de Navarre/Condé/Turenne/Montauban, and 49 appears unread in his f.143 opening. MAT-CCE's cross-office lookup has no power (4.2% vs 2.85% chance). bMATBEAM's values for these signs had margins of 0.5-8.1 bits. The f.78v/79r crib is retired (rule 3(b)), so only a period gloss on a different leaf would narrow them SPLIT-matignon-mayenne-1586 (2 Oct 2026, 0 of 31 split-check rows reachable, no leaf image on disk): 37 x2 and 73 cut into 3|7 / 7|3 (e o / o e) against the key, but sit in the word-code range and 37 closes both parallel lines f196-3/f201-5, so they are held as unkeyed word codes, not glued letters, pending the image; `split_worklist.tsv` ranks all 31 labels (7 cut fully into key codes: fe x6, de x5, me x5, 37 x2, 73, Bi, f3); next: locate and crop the f.91-92 Cipher-1 letter ("deciphered in the margin", henryiii.htm l.638, never opened) or the f.18-21/f.19 pair (cipher page plus a full clear page, of which Bourdeau's repo holds only 3+2 lines, bMAT1D) on btv1b9061879d (f.78v/79r = canvas 85). Transcribe cipher lines and clear text in two passes plus a reconciliation, and run `tools/interlinear_align.py` behind a known-answer control on H codes, ~$12
- fr.15571 f.179 (Matignon Cipher-3, whole leaf, sign count unmeasured) - blocker: not-attempted; a native, overlay-free image is on disk (`images/f179_gallica_native.jpg`, bMAT3). The magenta labels are Tomokiyo's modern overlay (grade M at most). Tomokiyo's reconstructed table `henryiii_Matignon3.png` (built from the period decipherments f.189/190, f.277-278/279-280, f.282 margin, henryiii.htm l.689) is referenced but not on disk and has never been applied; next: fetch `henryiii_Matignon3.png` from cryptiana.web.fc2.com (1 request), cut line crops with `tools/iiif_lines.py --image images/f179_gallica_native.jpg`, run two blind passes against the table plus a reconciliation, then decode (key: published, Tomokiyo), ~$9
- fr.15572 f.276 (Matignon Cipher-3) - blocker: not-attempted; never fetched at any resolution, because bMAT3 used its whole Gallica allowance on f.179. Tomokiyo gives only an opening paraphrase ("La Guiolle est en doubte du pu pour les amis de la Roussiere...", l.692), which can serve as a crib check; next: after the f.179 table step, locate the canvas on btv1b9061879d with `tools/gallica_folio.py --anchor` (f.78v/79r = canvas 85), cut crops, run two passes plus a reconciliation against the Cipher-3 table, decode, and check the opening against Tomokiyo's paraphrase, ~$7 (A2P4-MATIG 3 Oct 2026: the period clear text ff.279r-280r was compared against Tomokiyo's f.276 opening under prereg a357a7a3 -- NO MATCH, 2/5 vs gate 4, controls 1-2/5 / 0/5 / 5/5; ff.279-280 do not decipher f.276, so this leaf has no period decipherment on ff.279-280 and the table step is still the route; section "A2P4-MATIG")

## Escalation (1 Oct 2026)
- [ ] siblings: Opened so far: fr.3974 f.24 (MAT-3974: plain prose, no cipher, retired), the DECODE 24 Sept cache (0 hits, bCSMAT d), and the 27 Sept key_crossmatch fr7129 "hit", which scored the same on all three shuffled controls (ROOM.md 27 Sept 02:51-02:52), so it is not a lead. Not opened: the f.91-92 Cipher-1 letter (deciphered in the margin, Tomokiyo l.638), the fr.15573 Forget/Mayenne/Matignon folios ff.7, 20, 31, 62, 131, 299 (SO-MATIGNON-LEADS, unchecked), and fr.3354 f.91 and fr.16092 f.5 (weaker SO leads). Planned: locate and crop f.91-92.
- [ ] clear-pages: The hand and DP alignment against the f.78v/79r margin crib is closed by rule 3(b): bMAT1D 6/20 and 4/20, bMAT1E 9/20, bMAT1G 11/20, bMAT1H failed its pre-registered gate at 7/8. That closes this crib, not clear pages in general. Never imaged by us: the f.14v/f.15r and f.18-21/f.19 period decipherments (Bourdeau's repo holds one quoted phrase and 3+2 lines, bMAT1D), the f.91-92 margin, the Cipher-3 decipherments f.190, f.279-280 and f.282 margin, and the f.78v margin itself (native fetch reset twice, bMAT1F). Planned: f.91-92 margin or the f.18/f.19 pair as a fresh crib. Separately, Tomokiyo's modern published openings (f110/"f.111", f.143, f.154, f.276) serve as known-plaintext checks.
- [ ] known-keys: Done: Bourdeau's key.json fc0c9e8 (period-verified, now `key.tsv`, listed in KEY-DESIGN.tsv but not in KEY-OFFICES.tsv). MAT-CCE found no power across 7 office-cluster keys, and fr.3974 f.24 is retired. Not done: Tomokiyo's reconstructed tables `henryiii_MayenneForget1.png` (Cipher-1), `henryiii_Matignon3.png` and `henryiii_Camus.png` are not on disk or applied. His nomenclature list (76 roi de Navarre, 82 Condé, 84 Turenne, 98 Montauban) is not in `key.tsv`, which has '*' for all four, so f143r-2 reads "du * du que" where his paraphrase reads "du 76 duquel". `tools/design_prior.py` has not been run. Bourdeau's HEAD NOTES.md re-read 2 Oct 2026 (GAPS, snapshot in sources/cyphersolver/2026-10-02/): glyph table ⊐ box / ꝉ crossed-t = u/v, ₸ crossed-4 = m; GAPS2 2 Oct 2026: his HEAD key.json (34e0fc8) and 13 transcriptions fetched and diffed -- identical to `key.tsv`/`ciphertext.txt`, no new value; box = u/v tested as a hypothesis, untestable on f110 by the per-letter judge instrument (power control 1/10). Planned: the two Tomokiyo tables, and the f.110 crops for BOX/T.
- [x] print: bCSMAT made seven checks: both Labande Montaigne-Matignon 1916 editions grepped whole (no 1585/86 dates, no Mayenne or Forget), the SHF Lettres de Henri III (not on IA), Tomokiyo henryiii.htm (still undeciphered), the DECODE cache, both solver repositories, a web search, and OpenAlex/S2. No prior decipherment was found. One remainder is unchecked: the 1749 Villeroy-to-Matignon Lettres (SO lead, p.222), which runs Villeroy-to-Matignon, the opposite direction to these Mayenne/Forget-to-Villeroy letters.
- [x] key-rebuild: bMAT2's two-context rule is a control-backed negative (S 41 on the target vs 40-45 shuffled). The bMATBEAM 6-gram beam reached M 0.83 on its control, but on the target the U solution matched the shuffled null pattern, and its M commit (bMAT1C) worsened the judge and was reverted (bMAT1D). MAT-CCE's cross-key lookup has no power. Untried: a per-leaf, M-only beam run (gap 1). That run would be the beam's second target attempt, so it carries a pre-registered gate, and a failure retires the beam for this target. Run 3 Oct 2026 (GAPS gap 1): control (A) M 0.76-0.89 per leaf, but the judge-gain gate had no power (1/7 leaves testable), non-test; next instrument: a reference reading (Bourdeau's per-leaf files), not the shared-corpus judge. Run 3 Oct 2026 (GAPS2): agreement with Bourdeau's per-line readings, 4/4 leaves beam > null max and > first + 0.02 (0.75-0.85 vs first 0.63-0.72). Run 3 Oct 2026 (GAPS3): per-leaf commit-and-judge NON-TEST (rise beats the shuffled-target rise on 1/4 leaves); the judge-scored commit of this beam is retired (third attempt); M choices wait on a non-LM reference (period gloss on a Cipher-1 leaf).
- [ ] image-check: Done only on the crib leaves f.78v/79r: Bourdeau's f78 skips 44 signs at a line join (bMAT1G), and two blind passes of f.79r split on 4 vs 4+ at 59.5% agreement (bMAT1F). None of the 13 target leaves has been re-read against its image. The disk-only Tomokiyo opening alignment (gap 2) ran 2 Oct 2026 and could not predict which labels collapse (11 U tokens on letters, all on f110, whose decode judges at its own shuffle level); `8` reads g 0/4 on f110. Planned: native line crops of f.110 and two blind passes over a 4-line sample, testing 4/4+, w/w-, T/T=, D2/D, U and z. D2B-MATF110 6 Oct 2026: run (lines f110-1..5, 2 blind passes, prereg 859e5757b): G0 control passes (55.7%/58.4% vs 50%), G1 fails for every label (T read as T 10/10; z, BOX, U no agreed keyed label; w/4/p too few), A-B agreement 58.5%; no key change; next: the owner's sign sorter for f.110 BOX/z/T/U/w/4 (TRANSCRIPTION.md: >10% pass split goes to a person). SPLIT-matignon-mayenne-1586 (2 Oct 2026, account-4): the 31 `--split-check` labels (7 full split candidates incl. 37/73/fe/me/de, 6 compound, 18 absent; 1,086 U tokens) all fall on leaves with no image on disk -- 0 of 31 reached, 0 vision calls, grades unchanged; `split_worklist.tsv` is the ranked crop list (about 10 native line crops over 7 leaves, 7 vision calls, ~$4), to run with the f.110 sample above.
- [ ] retry: Not run, because no value has survived to extend the key (bMAT1C's S grades were reverted). H 10,074 / M 1,648 / U 1,272 has been unchanged since 26 Sept. Planned: after the label check or the per-leaf M run, re-run `tools/decode_key.py --check` and the fr16 judge per leaf against shuffled controls.
Verdict: keep going: 6 internal gaps; cheapest next: gap 2's f.110 sample ran 6 Oct 2026 (D2B-MATF110: no label collapses, pass split 41.5%), so the f.110 glyphs go to the owner's sign sorter (seeded 6 Oct 2026 by R7-MATSORT, `sorter/`; R7-MATQA 6 Oct 2026 found it NOT fit to hand on, 6/6 checked tiles off their label; R8-MATCUT 6 Oct 2026 re-cut it deskewed with tools/sorter_recut.py + --region: preflight PASS, 22/24 sheet tiles one whole sign on the right line, flagged to the account-3 orchestrator to publish, ASKS 146; next: the owner's pass on the published sorter, then apply per sorter/README.md); after that, the other leaves' `split_worklist.tsv` crops (7 vision calls, ~$4) (gap 1's judge-scored beam commit retired 3 Oct 2026, GAPS3 NON-TEST; its M choices now wait on gap 4's period gloss, ~$12)

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
