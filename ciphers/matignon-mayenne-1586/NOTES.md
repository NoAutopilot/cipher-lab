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
