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
