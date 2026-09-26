partial
Check-solved (LANE B5 worker bMAT, 26 Sept 2026): Tomokiyo `sources/cryptiana/web/henryiii.htm` (on disk, grepped 26 Sept 2026) still lists every leaf in this target -- Mayenne-Forget's Cipher-1 ff.110, 123-124, 143, 150, 154, 173, 196, 201, and Matignon's Cipher-3 f.276 and fr.15571 f.179 -- as "undeciphered" (f.276 gets a fragmentary paraphrase only: "La Guiolle est en doubte du pu pour les amis de la Roussiere..."). Internet Archive full-text search (be-api fts, 26 Sept 2026) on "Correspondance de Montaigne avec le maréchal de Matignon (1582-1588)" (Labande ed., IA ids `correspondancede00montuoft`/`correspondanc00mont`, the only Matignon correspondence edition on IA whose date range covers 1585-86; the two "Correspondance de Joachim de Matignon" editions on IA are the wrong Matignon, 1516-1548) for "Bellebourg" (the place-name closing f.110's cipher per Bourdeau's transcription) returns 0 hits in either volume. aaymeloglu/unsolved-ciphers (shallow clone, grepped for matignon/mayenne/forget/15571/15572, 26 Sept 2026, then deleted): no hit outside its own tools/decode.py and an unrelated PARES jsonl row. DECODE (de-crypt.org): no fresh crawl run this job (cost); `sources/decode/records-non-decrypted-2026-09-24.tsv` and `records-decrypted-2026-09-24.tsv` (login-free RecordsList cache, 24 Sept 2026) grepped for matignon/mayenne/15571/15572, no hit. OpenAlex (`api.openalex.org/works?search=Matignon Mayenne cipher 1586`, keyed, 26 Sept 2026): 0 results. Semantic Scholar (`x-api-key` header, one query plus the one allowed retry): both 429 (rate-limited even with the key); not answered, logged as unreachable this session, not a negative. Bourdeau's own `matignon1586/NOTES.md` (dbourdeau/cyphersolver, commit fc0c9e8, 25 Sept 2026 18:14 CDT) independently records "no printed decipherment of these despatches was found (searches on the BnF catalogue and on the literature, 17 Sept 2026)". Net: open, no printed or prior decipherment found by any of these six checks; Cipher-3 (f.276, fr.15571 f.179) untouched by any transcription as of this commit.

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
