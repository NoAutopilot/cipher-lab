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


## Web and blog check (GF-A2-12, 3 Oct 2026)

Plain web searches (WebSearch, 3 Oct 2026):
1. `MLH cryptogram solved son Israel parents 1974 Cryptogram ACA` (sender/recipient/date) -- Cipherbrain post 31 (23 May 2017) and Cipherbrain archive/category pages; nothing reports a reading.
2. `"MLH" cryptogram "Milestone" Israel encrypted note parents California` (distinctive phrase, the envelope's return-address word) -- same post; also returns Cipherbrain "California cryptogram largely solved", opened: a basement-wall cryptogram in a California house (Gelotti, c.2016), a different item, not this note.
3. `Wer löst dieses verschlüsselte Schreiben eines Sohns an seine Eltern Klausis Krypto Kolumne` (the German first post's title, 8 Apr 2016) -- search did not return it; opened directly from the URL in the 2017 post (below).
4. `ciphermysteries MLH cryptogram` (descriptive title + Cipher Mysteries site query) -- no Cipher Mysteries post on this item; Wikipedia "List of ciphertexts" and Cipherbrain's top-50 list only.
Site searches: Cipherbrain (queries 1-3, all hits on scienceblogs.de/klausis-krypto-kolumne); Cipher Mysteries (query 4: no post on MLH found); `cryptiana MLH cryptogram 1976 Israel` (Cryptiana: no cryptiana.blogspot.com or Tomokiyo page returned; one geocaching.com hit, GC6FNDV "Oded", opened -- an unrelated substitution-cipher puzzle cache, not this note).
Hits opened and threads read:
- Cipherbrain 8 Apr 2016 "Wer löst dieses verschlüsselte Schreiben eines Sohns an seine Eltern?" and its 12 comments (8-17 Apr 2016: SantaColoma x2, McCarthy x2, Schmeh x3, Schrödel x3, Mac-FD, Jane Smith): rebus, right-to-left, programming-language-symbol and astrology ideas; Schrödel reports the ACA's answer that Cryptogram's "MA 1978" issue still calls it unsolved. No plaintext offered or accepted.
- Cipherbrain 23 May 2017 post 31 and its 15 comments: already on disk (sources/schmeh/posts/31-mlh.txt), read in full by bMLH (25 Sept 2026); the post itself re-checked by this worker (no reading; "has never been deciphered").
Result: no decipherment or plaintext found on the open web or in these comment threads. Requests: WebSearch 5; WebFetch scienceblogs.de 2, geocaching.com 1.

## Premise check (GF-A2-12, 3 Oct 2026)

(a) Decipherments the folder already mentions -- none: NOTES.md, spec and the two Cipherbrain threads mention only hypotheses (rebus, APL/ALGOL symbols, astrology, right-to-left, meaningless symbols): not found.
(b) Other solvers' working files -- shallow clones 3 Oct 2026, dbourdeau/cyphersolver HEAD 810a777 (only research/top50 NOTES.md row "7, 31, 44 ... MLH 1974 ... low ... All far too short"; no targets folder, no rendering) and aaymeloglu/unsolved-ciphers HEAD d2800bb (no file names MLH; "mlh" matches only unrelated substrings): not found.
(c) Physical neighbours -- the only witness is the single image printed by the ACA and reposted by Schmeh (images/MLH-Cryptogram.jpg); the envelope ("Milestone" in place of a return address) is described, not reproduced. No second sheet or clear copy is known: not found; the family's original letter is unreachable.
(d) Recipient's side -- the receiving "office" is the ACA, which printed it in The Cryptogram Jan-Feb 1976 and, per Schrödel's 16 Apr 2016 comment relaying the ACA, again in an MA 1978 issue still calling it unsolved. The ACA issues themselves were not opened (members' archive; not found online this pass): not found in what was reachable; the ACA back issues are unreachable from here.

## GAPS131-mlh-1976: cheap test 2, sign shapes vs period character sets (3 Oct 2026, account-4)

Script `charset_xref.py` (outputs `charset_xref.tsv`, `charset_xref_summary.json`; `--check` exits 1 if stale).
No vision, no fetch: the input is this file's own sign table (single blind pass, every sign grade M, rule 2:
conditional on that transcription). Each of the 20 non-literal signs (S1-S20 with S4 = the reused dot, plus the
letter-shaped D and O; S6/S7 are unused labels) got a short list of candidate glyphs its shape description could
be, then set membership was computed against four printable repertoires written from public documentation:
ASCII-1967 (94 printable), EBCDIC as printed on System/360 (88), APL\360 / APLSV on the IBM 2741 APL typeball
(106: base keys plus the standard 1966-75 overstrikes; APL2-era glyphs excluded), ALGOL 68 Revised Report 1975
representation symbols (98). Matched control: 2,000 random catalogues of the same size, each sign's candidate
list replaced by a random sample of the same length from a 1,764-glyph Unicode pool (the blocks the candidates
come from), seed 1976. The control changes which glyphs are candidates, so it can fail differently from the target.

| statistic (of 20 signs) | target | control mean | control p95 | p(control >= target) |
|---|---|---|---|---|
| matches ASCII-1967 | 13 | 3.64 | 7 | 0.0005 |
| matches EBCDIC-S360 | 11 | 3.43 | 6 | 0.0015 |
| matches APL\360 2741 | 18 | 4.06 | 7 | 0.0005 |
| matches ALGOL 68 RR | 13 | 3.76 | 7 | 0.0005 |
| programming-specific (APL or ALGOL 68, not ASCII or EBCDIC) | 5 | 1.65 | 4 | 0.0205 |

Programming-specific signs: S5 (outline triangle = APL ∆), S11 (triangle with tail = APL ∆ / ⍙), S10 (stem with
arch = APL ⊤ or ↑, ALGOL 68 ↑), S14 (single arrow = APL →), S15 (circle with central dot = APL ⍟ circle-star,
only an approximate fit). No candidate in any set: S2 (stem, dot, macron), S20 (oval with inner arrowhead), and the
double arrow ⇒ (in none of the four period repertoires).

What this does and does not show:
- The four general-set excesses (11-18 of 20 vs a null of about 4) are not evidence for the hypothesis: the
  candidates are common shapes (letters, triangle, circle, caret, arrow, plus) while the random pool is mostly
  exotic glyphs, so the null is lenient toward the target, and the candidate lists were written by a reader who
  knows these repertoires (a bias toward glyphs that are in them). APL's 18 is the largest only because APL\360's
  repertoire is letters plus the most geometric symbols.
- The discriminating figure, 5 programming-specific signs against a null p95 of 4 (p = 0.02), is a weak excess
  under the same biases; S15's ⍟ and S10's ⊤/↑ are loose fits. Read it as "several shapes are consistent with
  the APL typeball", the commenter's observation restated with a number, not as support for an APL or ALGOL source.
- No letter-to-symbol mapping emerges: APL/ALGOL operator glyphs carry no letter values, and the letter-shaped
  signs (D, O, P-variants, F, e) match every set equally. Cheap test 3 (judge decodes against English) therefore
  has no input and stays not runnable. No reading is claimed (rule 4: none).

## Remaining gaps (GAPS131, 3 Oct 2026)
Read so far: 0 of 33 tokens read (no reading; cheap tests 1-2 are catalogue and character-set tests, no mapping)
- whole note (33 tokens) - blocker: not-attempted; sign table is a single blind pass (S2/S3/S18 may be one sign), see "Cheap test 1" above; next: second blind transcription pass of the existing crops + reconciliation, ~$4
- letter-to-symbol mapping for cheap test 3 - blocker: too-short; 26 symbol tokens / 20 distinct, IC below both controls, and test 2 (GAPS131 above) yields no letter values
- the ACA's printed context (The Cryptogram Jan-Feb 1976 and the 1978 issue Schrodel cites) - blocker: needs-physical-access; ACA members' back-issue archive, not online (Premise check (d) above)

## Escalation (GAPS131, 3 Oct 2026)
- [n/a] siblings: no other note from this sender is known
- [n/a] clear-pages: the strip carries only MLH, e and slash in clear
- [x] known-keys: test 2 (GAPS131) checked ASCII/EBCDIC/APL/ALGOL 68 glyph sets; weak programming-specific excess, no key
- [ ] print: ACA Cryptogram back issues not opened; planned only if a member copy becomes reachable
- [n/a] key-rebuild: no key material exists to rebuild from
- [ ] image-check: second blind transcription pass on images/crops + reconciliation
- [n/a] retry: no earlier decode attempt exists to retry
Verdict: keep going: 1 internal gaps; cheapest next: second blind transcription pass + reconciliation, ~$4
