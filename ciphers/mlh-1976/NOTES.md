# mlh-1976

open
Minimal check-solved, 25 Sept 2026 (LANE B2 worker bMLH), before any transcription (intake step, `.claude/briefs/breadth.md`): Cipherbrain post 31 (Schmeh, 23 May 2017, scienceblogs.de/klausis-krypto-kolumne, already on disk at `sources/schmeh/posts/31-mlh.txt`) and its 15-comment thread read in full -- no solution posted anywhere in the thread, only speculative hypotheses (rebus reading, ALGOL68/APL/IBM-keyboard symbol mapping, right-to-left order, meaningless-symbols null hypothesis); the post itself states the ACA's Tobias Schrodel follow-up in 2016/17 found nothing new since the 1976 magazine printing. Both solver repositories grepped via shallow clone (github.com/dbourdeau/cyphersolver, github.com/aaymeloglu/unsolved-ciphers; cloned to /tmp, grepped, deleted, not committed): cyphersolver's `top50/top50.json` and `top50/TARGETS.md` list "31. The MLH cryptogram" / "MLH 1974" as a low-priority unsolved target ("Four lines of symbols; 44 letters. All far too short"), no reading or key on file; aaymeloglu/unsolved-ciphers has no MLH-named folder or file at all. OpenAlex full-text search (api.openalex.org/works?search=, `Authorization: Bearer $OPENALEX_KEY`) for "MLH cryptogram solved" returned 0 results. Semantic Scholar full-text search (api.semanticscholar.org/graph/v1/paper/search, `x-api-key: $S2_KEY`) for "MLH cryptogram decrypted" returned 23 generic cryptography-unrelated hits (stream ciphers, DRM control words), none naming this item. No standard printed edition applies here (the only primary source is the ACA's own Cryptogram magazine, Jan-Feb 1976, itself only known through Schmeh's paraphrase -- no full text or scan of the magazine issue found on disk or searched this pass).

Status: open, unsolved by any source checked. Proceeding to cheap test 1 (image fetch + blind symbol catalogue) per brief `.claude/briefs/runs/2026-09-25-lane-b2-mlh-1976.md`.

## Cheap test 1: image fetch + single blind symbol catalogue (25 Sept 2026, LANE B2 worker bMLH)

Fetched `https://scienceblogs.de/klausis-krypto-kolumne/files/2016/04/MLH-Cryptogram.jpg` (1 request to
scienceblogs.de, HTTP 200, 79615 bytes, 1000x295px JPEG, browser User-Agent, sha1 in
`images/manifest.json`). This is the sole image; no second image exists in the post or on disk.

**Rule 2 (image over transcription):** this section works from the page image itself, on disk at
`images/MLH-Cryptogram.jpg`. `ciphertext.txt` is a **single pass, draft** (rule 7's grading: every token
here is M -- uncertain/inferred from a first read, not yet reconciled against a second independent pass).
Test 2 (a second blind pass and reconciliation) is out of scope for this brief.

### Line/word structure

Three handwritten lines on a strip of paper (matches the ACA's paragraph 2: "a strip of paper
torn/cut from a larger sheet"), no ruled lines visible, left-to-right within each line as drawn (no
attempt made to test the right-to-left hypothesis this pass -- that is downstream analysis, not
transcription). Word-groupings (gaps wide enough to read as breaks) per line:

- Line 1: `[S1]` / `MLH` / `⇒` / `[S2 S3][dot][S5] D O [S5][S8]` -- one clear wide gap after the
  leading S1 mark, another after "MLH", another after the double-arrow "⇒"; the seven marks after
  the arrow are drawn as one continuous run with no internal gaps.
- Line 2: `[S9]` / `[S10]` / `[dot][S11][S12]` / `[S13]` / `MLH/e` / `[S14][S15]` / `[S16][S17][S16][S18] O O`
  -- looser spacing than line 1, several short runs rather than one long one.
- Line 3: `[S19] O [S20] . |` -- one run, tightly spaced, the shortest line.

**Structural note (why this matters before any decode attempt):** line 1 reads literally as
"`[S1]` MLH `⇒` `[7 symbols]`" -- the plaintext word "MLH" (the mother's initials, per the ACA's own
paragraph 2) sits immediately before a double-line arrow that elsewhere in ordinary notation means
"yields" or "is represented by". Read at face value this is the sender himself glossing one plaintext
word against its 7-symbol encoding -- a self-supplied crib, if the reading is right. This is an
observation from the image, not a decode; grade the reading of "MLH" itself as C (it is drawn as plain
Latin capitals, not a sign) and the "⇒ means encodes-as" interpretation as M (inferred, single pass,
unconfirmed). "MLH" recurs plainly a second time on line 2 (as "MLH/e", also plain Latin letters plus
a slash and a lowercase e), which is consistent with the word functioning as a repeated anchor rather
than appearing once by chance.

### Sign table (single pass; codes are this pass's own labels, not a claimed alphabet)

| code | shape (blind description) | count | crop(s) |
|---|---|---|---|
| (literal) MLH | plain Latin capitals M, L, H | 2 | `images/crops/line1_S5_D_O_S5_S8.png` (line 1, before ⇒); `images/crops/line2_MLH_slash_e.png` (line 2, as "MLH/e") |
| (literal) ⇒ | double-stroke rightward arrow (thicker/doubled vs. the single arrows below) | 1 | `images/crops/line1_S5_D_O_S5_S8.png` region (left edge) |
| (literal) / , e | plain slash then lowercase e, immediately after the second "MLH" | 1 each | `images/crops/line2_MLH_slash_e.png` |
| S1 | small dash then a cursive integral-/S-shaped curl (resembles a musical treble-clef fragment or a loose figure-8) | 1 | `images/crops/line1_lead_S1.png` |
| S2 | vertical stem, filled solid teardrop/dot near the top, a short macron bar above that | 1 | `images/crops/line1_S2_S3_dot.png` |
| S3 | open-loop "P" shape on a stem, unfilled, no bar | 1 | `images/crops/line1_S2_S3_dot.png` |
| dot (reused label) | small isolated filled dot, used 3x in different contexts (after S3; atop the stem before S11; as the "." near line 3's end) -- **not confirmed to be one sign**; catalogued together only because blind reading can't yet tell a repeated symbol from incidental punctuation | 3 | `images/crops/line1_S2_S3_dot.png`; `images/crops/line2_S9_S10_dot_S11_S12_S13.png`; `images/crops/line3_S19_O_S20_dot_bar.png` |
| S5 | plain outline triangle, apex up, closed base, no fill | 2 | `images/crops/line1_S5_D_O_S5_S8.png` |
| (literal?) D | closed loop with a straight back stroke, reads as a plain block "D" -- **ambiguous**: sits inside the same unbroken symbol run as S5/O/Λ with no gap marking it as a separate "word", so it may be an invented sign that happens to be letter-shaped (SantaColoma's ALGOL/APL/keyboard hypothesis) rather than literal text; transcribed as "D" per the brief's "letters as text" instruction, flagged here rather than resolved | 1 | `images/crops/line1_S5_D_O_S5_S8.png` |
| (literal?) O | plain open circle -- same ambiguity as D above | 4 | `images/crops/line1_S5_D_O_S5_S8.png` (x1); `images/crops/line2_S16_S17_S16_S18_O_O.png` (x2); `images/crops/line3_S19_O_S20_dot_bar.png` (x1) |
| S8 | open caret/chevron (Λ), no base stroke, just two meeting diagonal strokes | 1 | `images/crops/line1_S5_D_O_S5_S8.png` |
| S9 | "n"-like shape (two legs) with an extra diagonal tail descending off the right leg past the baseline | 1 | `images/crops/line2_S9_S10_dot_S11_S12_S13.png` |
| S10 | vertical stem topped by a rounded arch/umbrella with a small dot at each end of the arch (like two "eyebrow" dots) | 1 | `images/crops/line2_S9_S10_dot_S11_S12_S13.png` |
| S11 | triangle (apex up) with a trailing zigzag/hook stroke exiting to the right, like Δ fused to a short lightning-bolt tail -- distinct from the plain S5 triangles, which have no tail | 1 | `images/crops/line2_S9_S10_dot_S11_S12_S13.png` |
| S12 | angular zigzag/lightning-bolt stroke (reads like a blocky "5" or "S") | 1 | `images/crops/line2_S9_S10_dot_S11_S12_S13.png` |
| S13 | lowercase-"e"-like loop sitting on an underline that curls up into a rightward arrowhead | 1 | `images/crops/line2_S9_S10_dot_S11_S12_S13.png` |
| S14 | plain rightward arrow (single stroke, thinner than the line-1 "⇒") | 1 | `images/crops/line2_S14_S15.png` |
| S15 | open circle with a small filled dot centred inside ("eye"/target shape) -- matches commenter Richard SantaColoma's "eye" hypothesis in the spec's constraints | 1 | `images/crops/line2_S14_S15.png` |
| S16 | vertical stem crossed by two short horizontal bars (one near the top, one lower) -- resembles a stylised "F" or a minus-plus mark | 2 | `images/crops/line2_S16_S17_S16_S18_O_O.png` |
| S17 | closed loop resembling "D" or "6" with an extra small internal curl near the top-left | 1 | `images/crops/line2_S16_S17_S16_S18_O_O.png` |
| S18 | open-loop "P" shape with a small filled dot inside the bowl, no macron (compare S2, which has both dot and macron, and S3, which has neither) | 1 | `images/crops/line2_S16_S17_S16_S18_O_O.png` |
| S19 | asymmetric cross/dagger shape (like a lowercase "x" or "+" with uneven arm lengths) | 1 | `images/crops/line3_S19_O_S20_dot_bar.png` |
| S20 | elongated/flattened closed oval with a small arrowhead-like mark inside on the right side | 1 | `images/crops/line3_S19_O_S20_dot_bar.png` |
| (literal) \| | plain vertical stroke (could be numeral 1, letter l, or an unmarked stroke) | 1 | `images/crops/line3_S19_O_S20_dot_bar.png` |

**Rebus/picture note (per brief):** S15 (circle-with-central-dot) and S10 (arch with two dots) both read
more naturally as pictures than as letters -- S15 as an eye (matching the SantaColoma "eye" hypothesis
already in the spec), S10 as a stylised face/eyebrows-and-nose shape or an umbrella. S20 (oval with an
internal arrow-mark) and S13 (e-shape riding an arrow) also look more like small pictograms than letterforms.
None of this is a proposed reading -- it is what a shape resembles on a single blind pass, offered because
the brief asks where a shape could be a rebus rather than a letter sign.

### Counts, IC, and controls (all single pass -- rule 2/7 caveat above applies to every number below)

Full reading-order token stream (`ciphertext.txt`, `;`-separated, `tools/freq.py`): **N = 33 tokens,
K (distinct) = 26, IC = 0.0189** (flat/1-K baseline for 26 symbols = 0.0385).

Symbol-only stream (excludes the two literal "MLH" tokens, the "⇒" connector, and the literal
"/", "e", ".", "|" marks -- i.e. everything this pass read as plain Latin text or punctuation rather
than an invented sign): **N = 26, K (distinct) = 20, IC = 0.0277** (flat baseline for 20 symbols = 0.0500).

Matched controls (`tools/data/pg1661_holmes.txt`, English; uniform-random string; 100 samples each,
seed 42, script not yet committed as a standalone tool -- ad hoc for this pass, reproducible from the
numbers given):

| | N | K | mean IC (100 samples) |
|---|---|---|---|
| **target, full stream** | 33 | 26 | 0.0189 |
| English control (Holmes, random 33-letter windows) | 33 | 26 (English alphabet) | 0.0616 |
| Uniform-random control | 33 | 26 | 0.0393 |
| **target, symbol-only stream** | 26 | 20 | 0.0277 |
| English control (Holmes, random 26-letter windows) | 26 | 20 | 0.0614 |
| Uniform-random control | 26 | 20 | 0.0485 |

At N this small (26-33 tokens) no IC comparison is a reliable signal either way -- these numbers are
reported per the brief, not as a verdict. For what it is worth, the target's IC sits *below* both the
English and the uniform-random control on both stream definitions, consistent with a symbol set close to
or above the token count (heavy hapax: 21 of 26 distinct tokens in the full stream appear exactly once),
which is itself consistent with a system that is not a simple monoalphabetic substitution of ~26-30
letters (too many distinct shapes for the text to repeat any of them by chance at this length) -- but is
equally consistent with several of the "distinct" codes above actually being the same sign drawn
inconsistently (S2/S3/S18 are three visually close "P-with-stem" variants; a second pass could collapse
some of these). This is exactly the ambiguity a second pass (test 2, not run here) exists to resolve.

### Where this leaves cheap test 2 (spec's next step, not run this pass)

The spec's test 2 proposes cross-referencing the catalogued shapes against ALGOL68/APL/mid-1970s IBM
keyboard character sets. Candidates worth checking first from this catalogue: S5/S8 (Δ, Λ triangle/caret
pair -- Δ is literally ALGOL's own "quad"/delta character); S16 (double-bar stem, resembles a struck-through
letter or a mathematical ∓); the letter-shaped D/O ambiguity noted above. Left as a suggestion per rule 8
of Usage (a worker does not start a test its brief did not name).

