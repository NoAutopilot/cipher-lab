status: open
Check-solved web pass by GF-A2-12, 3 Oct 2026: sources/schmeh/posts/12-scorpion.txt (Cipherbrain top-50 no.12, 30 Jan 2018, with its 7 comments to 29 Dec 2021) read in full by this worker; the ciphermysteries.com Scorpion category (10 posts, 1 Jun 2014 - 30 Dec 2020) and the 16 Oct 2018 "Scorpion S1, a different view" post with its 9 comments read; Cipherbrain 7 Jan 2022 post read; dbourdeau/cyphersolver targets/scorpion grepped. No accepted decipherment of S1 or S5 found; three claimed plaintexts are on record (Farmer 2007, Roberts 2016, "Rubislaw32" forum 2018/2022), none accepted, the 2018 one tested by Bourdeau and found no more probable than random fits (see Premise check). No printed standard edition exists for these letters; Bauer, Unsolved! (2017) p.224 discusses them (cited by a Cipherbrain commenter, not opened by this worker).

# Scorpion letters (1991), two published cryptograms

Anonymous letters to America's Most Wanted host John Walsh in 1991, sender called himself "Scorpion",
claimed 23 crimes (robberies and murders). Two of five published excerpts are encrypted; three more
encrypted messages exist but were never published (kept by police, per Schmeh). Hoax risk flagged by
both Schmeh and Aymeloglu's SHORTLIST -- there is no evidence the sender is the Zodiac Killer, and the
claim of 23 crimes is considered very unlikely to be true. **Check-solved not run this pass** -- this
worker only ran spec `cheap_tests_in_order[0]` (image fetch + one blind transcription pass); intake
gate / check-solved verdict is a separate step, not done here.

## Source and provenance

Schmeh's post (`sources/schmeh/posts/12-scorpion.txt`, scienceblogs.de, "Top 50 unsolved encrypted
messages" #12) scans from Dave Oranchak's Zodiac Killer site (oranchak.com/scorpion-cipher.html; not
fetched this pass, not a host this brief named -- flagged below as a follow-up). Schmeh's own counts:
first cryptogram 70 characters/53 unique, second cryptogram 180 characters/155 unique.

**Filenames are reversed relative to the post's own text order** (spec already flagged this, confirmed
here against the fetched images):
- `Scorpion-Letter-2.jpg` (62,115 bytes, 454x345px) = Schmeh's **first** encrypted passage (the one he
  says is "70 characters, 53 of which are unique").
- `Scorpion-Letter-1.jpg` (174,411 bytes, 527x766px) = Schmeh's **second**, larger cryptogram ("155 of
  the 180 symbols ... are unique"). This image also carries a plain-English caption above the cipher
  grid ("Hi! Remember me?") and one row of the grid is crossed out / hatched over in the source scan
  (visible about two-thirds of the way down) -- flagged, not decoded, worth a closer look in a later
  pass: is it redacted by whoever scanned/published it, or part of the original letter?

`images/manifest.json`: URL, byte size, sha1 for both, with a note on which cryptogram each file is.

## Cryptogram 1 (Scorpion-Letter-2.jpg) -- full single-pass transcription

`ciphertext.txt`: 70 tokens, row-major, 7 rows x 10 columns, reading top-to-bottom then left-to-right
within each row (matches the printed grid layout; no word spacing in the source, confirmed by Schmeh's
own note that there are no spaces between words). Sign codes are this worker's own inventory,
`sign_table1.tsv` (53 rows: code, count, a short shape description, one example position). Transcribed
directly from the image by eye (row crops at 4x upscale), **not** from any existing transcription.

Stats (`tools/freq.py ciphers/scorpion-1991/ciphertext.txt`):
- N = 70, distinct K = 53, IC = 0.0083.
- This N/K **exactly matches** Schmeh's independently published count (70 chars, 53 unique) -- a
  reassuring cross-check on this blind pass, not a claim of certainty on every individual symbol
  (grade S throughout, single pass, no H/C; a handful of visually similar shape-pairs, e.g. the two
  "circle with a black wedge" variants OWEDGE/CFLAG or the two bracket-corner shapes BRACKET1/BRACKET2,
  are the most likely spots a second pass would want to re-check).

Controls (`scripts/controls.py`, matched N=70, K=53, English = Project Gutenberg Sherlock Holmes
`tools/data/pg1661_holmes.txt`, 5 seeds each, no fetch):
| | IC |
|---|---|
| target (this transcription) | 0.0083 |
| English, N=70, 5 seeds | mean 0.0664, range 0.0600-0.0704 |
| uniform random, N=70 K=53, 5 seeds | mean 0.0189, range 0.0174-0.0199 (flat theory 1/53=0.0189) |

Target IC sits **below** even the uniform-random-over-53-symbols control, not just below English. That
is consistent with a homophonic cipher deliberately avoiding symbol repetition (39 of 53 codes are
hapax -- seen exactly once), which is exactly the design goal Schmeh describes ("a cipher that provides
several cleartext equivalents for some letters"); it is not evidence against a homophonic design, if
anything a suppressed-repeat IC this far below chance is itself a signature worth a name-check in a
cryptanalysis pass (rule 3 lesson: report the control number alongside, never the target number alone).
Cheap test 2 (a homophonic anneal against English with the same matched-control design) was **not**
run this pass -- it is next in `cheap_tests_in_order`, not this worker's job (single test, single pass).

## Cryptogram 2 (Scorpion-Letter-1.jpg) -- partial, N only, K/IC deferred

Much denser (180 vs 70 characters in a smaller-relative glyph size, 527x766px source) and this worker's
cap did not allow the same by-eye row-by-row identification used for cryptogram 1. Instead ran a
connected-component script pass (`scripts/segment.py`, `scripts/tokens_flat.py`, output
`scripts/tokens2.tsv`): binary ink threshold, morphological closing (dilate=3) to merge multi-stroke
glyphs, connected-component labelling, components under area 80px dropped as noise, sorted into raster
(row-estimate, then left-to-right) order.

- Component count at the calibration that best matches Schmeh's stated total: **N=179** (dilate=3,
  min-area=80), close to but not exactly Schmeh's published 180 (off by one component; a genuine
  multi-stroke glyph likely still merged or split somewhere, not hand-verified).
- **K not determined this pass.** The only automatic descriptor tried (a coarse aspect-ratio x
  fill-density bucket, 8 buckets total) is nowhere near fine-grained enough to separate ~155
  near-unique hand-drawn glyphs -- using it as K would understate the true count by roughly 20x and
  artificially inflate IC. Rather than report a number that misleads, K and IC for cryptogram 2 are
  left undone. Getting a real K needs the same by-eye per-glyph pass done for cryptogram 1, at roughly
  2.5x the token count -- a second worker's job (test 2 / a dedicated pass), not a re-run of this one.
- Line/word structure (by eye): a plain-English caption "Hi! Remember me?" sits above the cipher grid,
  then an underline, then the grid itself, roughly 15 rows of hand-drawn glyphs with no consistent
  column count and no word spacing (same as cryptogram 1). One row partway down is visibly crossed out
  / hatched in the source scan -- flagged above, not investigated further this pass.

## Follow-ups (one-line suggestions, not run this pass)

- [done 3 Oct 2026, A2P4-SCORP: no typed transcription there; see the section at the end] oranchak.com/scorpion-cipher.html may already have a typed transcription of both cryptograms (noted
  in the spec) -- not fetched (one host per worker, this worker's host was scienceblogs.de only). A
  future pass should check it and diff against `ciphertext.txt`/`sign_table1.tsv` before trusting either
  over the other.
- Cryptogram 2 needs a full by-eye pass (test 2 territory) for a real symbol inventory and K.
- The crossed-out row in cryptogram 2's source image is unexplained; worth asking whether Oranchak's
  site has an uncrossed version or commentary on it.
- Cheap test 2 [done 3 Oct 2026, A2P4-SCORP: control below gate, untestable at N=70] (homophonic anneal, matched control) and test 3 (Zodiac Z408/Z340 homophone-shape
  comparison) from the spec are both still open.

## Search log

No search for prior solutions run this pass (out of scope for a breadth cheap-test-1 worker; the spec's
own `value` field already notes "claimed solutions 2018 unverified" per the Aymeloglu survey row --
not independently checked here). Rule 10: nothing in this file should be read as a novelty claim.

## Requests

scienceblogs.de: 2 requests (one per cryptogram image), curl with a browser User-Agent, 2s apart, both
HTTP 200, no 429/403/challenge.

## Solver-repo check (bourdeau, 2 Oct 2026)

Fresh shallow clone of github.com/dbourdeau/cyphersolver, HEAD 34e0fc89 (1 Oct 2026), diffed against this folder on 2 Oct 2026 (worker SOLVERDIFF-BOURDEAU, sources/solver-diffs/2026-10-02-bourdeau.tsv). Match class b (they attempted it and closed or explained it).
- Their page: https://github.com/dbourdeau/cyphersolver/blob/main/targets/scorpion/NOTES.md ; README.md "Scorpion letters S1 and S5"
- Their extent, in their words: attempted, closed: S5 transcribed (180 symbols, 145 distinct), below the unicity distance for a homophonic key; controls run
- Their date: 15 Sept 2026
- Note: NOT in our NOTES.md (grep bourdeau/cyphersolver: 0)
Credit: D. Bourdeau, cyphersolver (code MIT, text CC BY 4.0). Status line unchanged; the parent decides any status change from the ROOM flag.

## Web and blog check (GF-A2-12, 3 Oct 2026)

Plain web searches (WebSearch, 3 Oct 2026):
1. `Scorpion letters 1991 John Walsh cipher solved` -- Cipher Mysteries Scorpion category and posts (2014-2020), Cipherbrain top-50 no.12, history.com (Craig Bauer, "When killers leave ciphers"): all say unsolved; Farmer's 2007 S1 claim noted as inconsistent (cipher K -> a and g).
2. `"Scorpion" cipher "America's Most Wanted" 1991 cryptogram solution claim` -- adds Cipherbrain "Mail from a Zodiac copycat: The Scorpion Letters" (7 Jan 2022); same verdict.
3. `"Bagel Bob's" Scorpion cipher` (the most distinctive phrase of the 2018 claimed plaintext, quoted) -- no web page carrying the phrase was returned; only Cipher Mysteries Scorpion posts.
4. Descriptive title: covered by 1-2 (the folder title "Scorpion letters (1991), two published cryptograms").
Site searches: `site:ciphermysteries.com Scorpion ciphers` (Cipher Mysteries: category pages 1-2, posts 2014-2018); Cipherbrain hits via queries 1-2 (2018 and 2022 posts); `cryptiana blogspot Scorpion cipher Walsh` (Cryptiana: no cryptiana.blogspot.com or Tomokiyo page returned -- not a target of that blog).
Hits opened and threads read:
- Cipher Mysteries category "scorpion ciphers" page 1 (10 posts, 1 Jun 2014 - 30 Dec 2020): no post reports S1 or S5 read; Pelling's 2020 note is that strictly cycling homophonics "may well prove to be surprisingly solvable" after Louie Helm read Pelling's own challenge cipher #1 -- not a Scorpion text.
- Cipher Mysteries 16 Oct 2018 "Scorpion S1, a different view" and 9 comments (16 Oct - 13 Nov 2018: Karl, Thomas, Pelling x3, milongal, Zlatoděj, Jarlve x2): one speculative letter substitution (Zlatoděj), no accepted plaintext.
- Cipherbrain 30 Jan 2018 (on disk, 7 comments read): no solution; comment 6 (Septimius Severus, 16 Dec 2021) corrects S5's distinct-symbol count to 145 and notes Bauer, Unsolved! (2017) p.224 repeats the 155 error.
- Cipherbrain 7 Jan 2022 "Mail from a Zodiac copycat": no solution; comments are on the German version only (not located; logged as not read).
Result: no accepted decipherment or plaintext found on the open web or in these comment threads. The 2018 "Rubislaw32" claimed plaintext lives on zodiackillermystery.freeforums.net (per Bourdeau), which this pass did not open (forum host, not one of the three blogs); its text is quoted in Bourdeau's NOTES.md. Requests: WebSearch 5; WebFetch ciphermysteries.com 2, scienceblogs.de 1.

## Premise check (GF-A2-12, 3 Oct 2026)

(a) Decipherments the folder already mentions -- found: the spec's own "claimed solutions 2018 unverified" (Search log above). Opened via Bourdeau's record: the "Rubislaw32" readings of S1 ("A picture in collection of people: Bagel Bob's Old Dairy Frothy Late Cofee. Pour action.") and S5 (begins "I am sending other picture of people for the collection of recent hybrid genders ..."), first posted 19 Oct 2018 on zodiackillermystery.freeforums.net. These are claimed plaintexts, not accepted ones: Bourdeau's claimed.py (15 Sept 2026) finds them consistent with most repeat constraints (S1 10/13, S5 26/27) but scoring worse in English (-2.74/-2.61 nats/letter) than the false solutions his annealer returns for random keys of the same size, and both texts sit below the unicity distance. Farmer 2007 (S1) is inconsistent per Pelling; Roberts 2016 is listed by Bourdeau, not opened here. Flagged to the account-3 orchestrator in ROOM.md for the found-solved question; status line unchanged by this worker.
(b) Other solvers' working files -- shallow clones 3 Oct 2026, dbourdeau/cyphersolver HEAD 810a777 and aaymeloglu/unsolved-ciphers HEAD d2800bb: Bourdeau targets/scorpion (NOTES.md, s1.txt, s5.txt, claimed.py, alternatives.py, unicity.py, profile.json -- attempted, closed as below unicity; MIT/CC BY, credited); Aymeloglu SHORTLIST.md lists Scorpion among "Hoax risk, no context, or no real system" (cited, not copied). No key either solver would hand us has been applied to a further text: found (as above), no reading.
(c) Physical neighbours -- S2-S4 (and a further unpublished text per Severus) are held by law enforcement and were never published; the plain-English caption "Hi! Remember me?" on S5's sheet is already in this folder. No clear copy known: not found; the unpublished letters are unreachable.
(d) Recipient's side -- America's Most Wanted / John Walsh and the FBI release (via Oranchak's site): no decipherment reported in any source read here (Pelling 2014-2020, Schmeh 2018/2022). The FBI/AMW files themselves are unreachable from here: not found / unreachable.

## Transcription diff and cheap test 2 (A2P4-SCORP, 3 Oct 2026, 17:36-17:42 UTC)

Intake gate, run before any work: `python3 tools/intake_gate_check.py scorpion-1991` ->
```
scorpion-1991: open (line 1) -- edition/page or full-text-search citation found within 6 lines
exit 0
```

**Oranchak.** `oranchak.com/scorpion-cipher.html` fetched once (descriptive UA). Over https the host presents Dreamhost's
default self-signed certificate (CN sni.dreamhost.com), so the fetch went over plain http (301 to www.oranchak.com, 200,
240 bytes). The page is eight `<img>` tags (scorpion1.jpg-scorpion8.jpg) and nothing else: **no typed transcription and no
commentary on S5's crossed-out row**. The images were not fetched (not named by the brief; one possible follow-up is
whether one of the eight is an uncrossed scan of S5).

**Diff against an independent typed transcription instead.** Bourdeau's S1 (`github.com/dbourdeau/cyphersolver`
targets/scorpion/s1.txt, transcribed 15 Sept 2026 from the same Cipherbrain scan; MIT, credited; copied to
`sources_other/bourdeau_s1.txt`). Script `scripts/transcription_diff.py` maps each of our codes to the other side's code
it shares most positions with (one-to-one) and lists positions that break the map: `bourdeau_diff.tsv` (position, ours,
his, status). Both sides find K=53. **61/70 positions agree** (0.871); pairwise same/different agreement 0.9917; but of the
repeat pairs (ours 20, his 22) only **11 are shared** -- the 9 disputed positions are exactly where the repeats live
(r3c5, r4c3, r4c9, r4c10, r6c4, r6c5, r7c4, r7c8, r7c9; mostly the black-square-with-notch and circle-with-wedge families
that both transcribers flagged as uncertain). Nothing in `ciphertext.txt` was changed. No vision call was made: the
family test below fails on its control whatever these 9 signs are, so settling them would not change this result. A
two-reader settlement of those 9 crops is the transcription next step if a future test needs S1's repeat structure.

**Cheap test 2: homophonic anneal, control before target** (prereg in `HYPOTHESES.md`, commit 42329030, before the run).
`python3 tools/family_run.py specs/scorpion-1991.json --family homophonic --cipher ciphers/scorpion-1991/scripts/s1_ours_oneline.txt --tokens space --param profile=target --seeds 3 --restarts 8 --gate 0.6`

| run | control (N=70 English, seeds 1-3) | realized control K | target |
|---|---|---|---|
| preregistered, profile=target | mean 0.038 (0.000-0.071) | 35-39 | not run (CONTROL BELOW GATE) |
| sensitivity, default profile (not preregistered) | mean 0.133 (0.086-0.171) | 40-47 | not run (CONTROL BELOW GATE) |

The controls realize fewer distinct signs than S1's 53 in 70 letters, so they are *easier* than the target and still read
4-13 percent: the homophonic family is **untestable at N=70, K=53** (rule 3), not a negative on S1. This agrees with
Bourdeau's unicity estimate (S1 key 249 bits vs about 224 bits of text). Grades: no reading, so no tokens graded.

**Verdict:** status stays `open`. Next step: test 3 from the spec (compare S1/S5 sign shapes against the Z408/Z340
homophone alphabets, about USD 1); cryptogram 2 (S5, N=180) is the only published text long enough to be worth a family
run, and needs a by-eye K before that (Bourdeau finds 145 distinct; a matched control at N=180, K=145 should be run before any
target attempt, about USD 2).

## Cheap test 3: S1 sign shapes vs the Zodiac Z408/Z340 alphabet (A2P4-SCORP2, 3 Oct 2026, 17:55-18:06 UTC)

Intake gate re-run first: `python3 tools/intake_gate_check.py scorpion-1991` -> `scorpion-1991: open (line 1) -- edition/page
or full-text-search citation found within 6 lines`, exit 0.

**Pre-registration** `shape_prereg.md` (commit 4745c5b9) before any scoring: feature-code list, statistic, control,
decision rule.

**Zodiac reference.** Z408 (54 symbols) and Z340 (63) as typed in D. Oranchak's webtoy (zodiackillerciphers.com/webtoy:
`zodiac.js` alphabet strings and char-to-glyph map, one image per glyph under `webtoy/alphabet2/`), 70 glyph types in the
union, fetched 3 Oct 2026 (73 requests to that host, 1.5 s apart; credit Oranchak). Wikimedia Commons/Wikipedia answered 429
(shared egress) and was not retried. Glyph images stay in the scratchpad (not committed); `shape/zodiac_codes.tsv` gives
each glyph's webtoy name, Z408/Z340 membership and code.

**Control.** Unicode Geometric Shapes U+25A0..U+25E5 (70 code points), coded from their Unicode names
(`shape/control_unicode_geometric.tsv`): not Zodiac-derived, built from the same primitives (filled/half-filled circles,
squares, triangles), so it can score above or below the Zodiac set on the statistic. Letters are excluded from the
primary statistic because the control has none by construction.

**Crops and vision calls.** S1 row crops cut with the shared tool (default line finding merged rows; re-cut with centres
read off the row ink profile):
`python3 tools/iiif_lines.py --image ciphers/scorpion-1991/images/Scorpion-Letter-2.jpg --out <scratchpad>/scrop --prefix s1 --debug --centres 54,89,126,167,210,253,293`
-> 7 crops, 454 px wide. Two vision calls: (1) a 70-cell labelled sheet of the Zodiac glyphs, (2) a sheet of the 7 S1 row
crops at 2x. 123 glyphs viewed (70 Zodiac + 53 S1 types).

**Result** (`python3 ciphers/scorpion-1991/shape/score.py`, `--check` exits non-zero when `shape/result.tsv` is stale):

| statistic (S1 sign types with an identical-code counterpart) | Zodiac Z408+Z340 (70) | control, Unicode geometric (70) |
|---|---|---|
| primary: non-letter types (41) | **14** | **12** |
| of which shape/stroke codes (38) | 11 | 12 |
| of which mirrored letters RL:E, RL:F, RL:L (3) | 3 | 0 (by construction) |
| letter types (12), descriptive | 12 | n/a (plain A-Z also 12) |

Preregistered decision (Zodiac minus control >= 5 and at least one Zodiac-only match): difference 2 -> **no support** for
"draws on published Zodiac material" from this test. Codes are one coder's eye judgement (grade M for every code); no
reading, so no tokens graded.

Descriptive, not preregistered, cannot license support: counted by distinct codes rather than S1 types the picture is
Zodiac 13 vs control 6, because the control's matches pile onto two S1 families (five circle-with-wedge types, three
solid dome/half-disc types), while the Zodiac-only matches are spread: mirrored E (REVE = Zodiac `be`), mirrored F (HOOK,
read here as a mirrored F, = `bf`), mirrored L (BRACKET1 = `bl`), circle with extended cross (TARGET, TARGET2 = `zodiac`),
pi-shape (PI = `sidek`), triangle with dot (TRIDOT = `n7`), square with dot (`sqd`), caret, slash, dash. Several S1
families have no counterpart in either set (notched black squares and rectangles, circle-with-wedge, headphone, Venus,
gamma, cup-with-dot).

**Transcription notes from crop view 2 (flagged, `ciphertext.txt` unchanged):** r2c4 DASH2 shows one stroke at 2x, not two;
r2c8 BRACKET2 is a solid half-ellipse, not a bracket; r1c8/r4c2 HOOK reads as a mirrored F; r6c4 (table: I) looks like a
right-angle bracket and r6c5 (table: O) like a dark half-oval -- both among the 9 positions the Bourdeau diff already
disputes.

**Verdict:** status stays `open`; all three spec cheap tests are now run, none moved it. Next step: a distinct-code
statistic preregistered with a second, blind coder (one coder's codes decide both sides here), about USD 1, and for the
family question, S5 (N=180) with a by-eye K and a matched control at N=180, K=145 first, about USD 2.

## S5 matched control, homophonic family (A2P4-SCORP3, 3 Oct 2026, 18:13-18:18 UTC)

Intake gate: `python3 tools/intake_gate_check.py scorpion-1991` -> `scorpion-1991: open (line 1) -- edition/page or
full-text-search citation found within 6 lines`, exit 0. Script only; no vision call, no host.

Question: once S5 (cryptogram 2) is transcribed, can the `homophonic` family read anything at its size? Control only,
**no target run** (S5 has no settled transcription). Prereg in `HYPOTHESES.md` (commit 9fad4b05) before any run. N and K
come from a shape-only placeholder, `scripts/s5_shape_placeholder.py` (flattest profile: as many hapax as possible, the
rest doubletons), never a transcription: `scripts/s5_shape_N180_K155.txt`, `scripts/s5_shape_N180_K145.txt`.
`python3 tools/family_run.py specs/scorpion-1991.json --family homophonic --control-only --cipher ciphers/scorpion-1991/scripts/s5_shape_N180_K155.txt --tokens space --param profile=target --seeds 3 --restarts 8`
(spec judge corpora pg1661_holmes + pg2701_mobydick, seeds 1-3, restarts 8, gate 0.6, as A2P4-SCORP).

| run | control recovery mean (range), seeds 1-3 | realized control K | target |
|---|---|---|---|
| primary: N=180, K=155 (spec/Schmeh), profile=target | 0.037 (0.011-0.067) | 95-110 | not run (no transcription) |
| sensitivity: N=180, K=145 (Bourdeau), profile=target | 0.131 (0.061-0.228) | 94-106 | not run |
| sensitivity: N=180, K=155, default profile | 0.081 (0.050-0.100) | 107-113 | not run |
| for reference, S1 (A2P4-SCORP): N=70, K=53, profile=target | 0.038 (0.000-0.071) | 35-39 | not run (CONTROL BELOW GATE) |

All three are far below the 0.6 gate. The controls realize fewer distinct signs (94-113) than the nominal 145-155 (English
text of 180 letters cannot fill that many homophones under the generator), so they are *easier* than S5 would be and still
read 4-13 percent. Per the prereg: the `homophonic` family is **untestable at N=180, K=145-155**, and with A2P4-SCORP's
N=70 result, untestable by this family on both published cryptograms (rule 3: not a negative on either). It agrees with
Bourdeau's unicity analysis (S5 below the unicity distance for a homophonic key). Grades: no reading, so no tokens graded.

**Verdict:** status stays `open`. A full S5 transcription is **not** worth costing for a homophonic-family attempt: the
control shows the family cannot read a text of this shape even when the transcription is perfect. What would move it:
new material (the three unpublished Scorpion messages Schmeh mentions, held by police, would pool the sign count), or a
constrained design hypothesis (a cycling/sequential homophonic, per Pelling 2020, as a family with its own control at
N=180) -- no such family is on the shelf (tools/families/, checked 3 Oct 2026); next: a cycling-homophonic family module plus
its control at N=180, a tool job, ~$3-4, worth briefing only if the lane wants a design hypothesis on a hoax-risk target.

## Cycling-homophonic family, matched controls (R11-SCORPCYC, 6 Oct 2026, 13:42-13:50 UTC)

Intake gate (lane, 13:40 UTC): `scorpion-1991: open (line 1) -- edition/page or full-text-search citation found within 6
lines`. Script only; no vision call, no host contacted.

Question: A2P4-SCORP3's named next step -- does Pelling's (2020) cycling/sequential homophonic design (each letter's
homophones used in one fixed cyclic order) give a solver enough extra constraint to read a text of S1's or S5's shape?
New shared module `tools/families/cycling_homophonic.py` (test `tools/tests/test_cycling_homophonic.py`, SYSTEM.md row):
control = a held-out corpus window enciphered cyclically; solver = n-gram anneal with a -lam x cycle-violation term (no
sign twice between two consecutive occurrences of another sign of the same letter; zero on the true key). Offline test,
easy control N=400 K=40: lam=2 reads 0.995 (0 violations) vs 0.953 with the term off, so the cycle term works where there
is something to bite on. Prereg and its one pre-run amendment (violation definition; dev only) in `HYPOTHESES.md`,
commits 8808f6b6e and 7c60398e1, both before the scored runs.

| run (spec judge corpora pg1661_holmes + pg2701_mobydick, seeds 1-3, restarts 8, gate 0.6) | control mean (range) | realized K, hapax | target |
|---|---|---|---|
| primary S1: N=70, K=53, lam=2 | 0.067 (0.057-0.071) | 53, 36 (S1 itself: 53, 39) | not run (CONTROL BELOW GATE) |
| S5 shape placeholder: N=180, K=155, lam=2 | 0.078 (0.044-0.111) | 155, 130 | not run (no transcription) |
| sensitivity N=180, K=145, lam=2 | 0.059 (0.050-0.072) | 145, 110 | not run |
| sensitivity S1 N=70, K=53, lam=50 (near-hard cycle) | 0.114 (0.086-0.157) | 53, 36 | not run |
| for reference, `homophonic` family (A2P4-SCORP/3) | 0.038-0.133 | 35-113 | not run |

Unlike the `homophonic` controls (realized K 35-39 at N=70, 94-113 at N=180), a cycling encipherment uses every
homophone, so these controls carry the full nominal K and a hapax share close to S1's own -- a closer match to the
target's shape, and they still read 6-11 percent. Per the prereg: the `cycling_homophonic` family is **untestable at N=70,
K=53 and at N=180, K=145-155** (rule 3: not a negative on either cryptogram, and not evidence for or against the cycling
design). Why: with 36 of 53 signs hapax the cycle constraint is nearly empty (a letter whose signs are all hapax has zero
violations under any key), so the solver is back to an n-gram anneal below the unicity distance. Grades: no reading, no
tokens graded.

**Verdict:** status stays `open`. The cycling-homophonic design hypothesis is now tested at both published shapes and
is untestable by this family; neither homophonic design justifies costing an S5 transcription. What would move it: new
material (the unpublished Scorpion messages Schmeh mentions would pool the sign count; a cycling key reused across
letters would let repeated signs carry the constraint), or the second-coder distinct-code shape test named after
A2P4-SCORP2 (~USD 1). Cheapest next: that blind second-coder test.

## Blind second-coder distinct-code test (R13-SCORP2C, 6 Oct 2026, 17:41-17:49 UTC)

The step named after A2P4-SCORP2 and again after R11-SCORPCYC. **Pre-registration** `PREREG-R13-SCORP2C.md` (commit
a6095cd72), pushed before coder B's codes were seen. Coder A = A2P4-SCORP2's codes (`shape/scorpion_codes.tsv`,
`shape/zodiac_codes.tsv`); coder B = one Sonnet subagent given only the 7 S1 row crops
(`python3 tools/iiif_lines.py --image ciphers/scorpion-1991/images/Scorpion-Letter-2.jpg --out <scratchpad>/scrop --prefix s1 --debug --centres 54,89,126,167,210,253,293`
-> 7 crops, 454 px wide, plus a 2x labelled composite of the same crops), a labelled sheet of the 70 Zodiac webtoy glyphs
(refetched from zodiackillerciphers.com/webtoy/alphabet2/, 70 requests + 1 probe, 1.6 s apart, all 200; credit
D. Oranchak; images kept in the scratchpad, not committed) and the feature-code vocabulary from `shape_prereg.md`. No
earlier codes, notes or sign names. B coded all 70 S1 positions and all 70 Zodiac glyphs (`shape/coder_b_s1.tsv`,
`shape/coder_b_zodiac.tsv`; every code inside the vocabulary). Scored by `python3 shape/score_b.py` (`--check` OK;
`shape/result_b.tsv`).

| distinct non-letter S1 codes with an identical counterpart | Zodiac | control (Unicode geometric, no coder) | difference |
|---|---|---|---|
| **primary, cross-coder: B's S1 codes vs A's Zodiac codes** (B: 29 distinct codes) | **11** | **8** | **3** |
| secondary (a), B on both sides | 15 | 8 | 7 |
| reference, A on both sides (A2P4-SCORP2, descriptive) | 13 | 6 | 7 |

Per-type (secondary b, 41 non-letter types by B's modal code): Zodiac(A) 16, Zodiac(B) 24, control 13.
Zodiac-only codes in the primary: RL:E, ST:caret, ST:dash, ST:pi, ST:slash, circle/cross, square/dot.

**Agreement A vs B.** S1, 70 positions: exact 55.7%, Cohen's kappa 0.549; at family level (base shape / stroke name /
letter class) 78.6%, kappa 0.756. Zodiac, 70 glyphs: exact 71.4%, kappa 0.710; family 84.3%, kappa 0.794. Typical splits
on S1: notched squares (A notch, B inner-square), hollow vs filled rects, which half of a half-disc, circle-with-wedge vs
circle/cross, mirrored F vs mirrored E (HOOK), BRACKET1 (A mirrored L, B rotated L).

**Decision (preregistered: cross-coder difference >= 5 and >= 1 Zodiac-only code): NO SUPPORT** (difference 3; 7
Zodiac-only codes, so the second clause holds, the first does not). The pattern says why the earlier descriptive 13-vs-6
looked stronger: when the same coder codes both the Scorpion signs and the Zodiac glyphs the gap is 7 for both A and B;
when the sides are coded by different people it falls to 3. Part of the apparent Zodiac excess is one coder's own
vocabulary habits matching themselves. B saw the Zodiac sheet (as the brief required), which can only prime towards
SUPPORT, so the NO SUPPORT is conservative. Grades: every code M (eye judgement); no reading, no tokens graded.

**Verdict:** status stays `open`. The shape question "does S1 draw on the published Zodiac alphabets" now has three
preregistered tests and none supports it; with exact-code kappa 0.55 on S1 a fourth coder would add little. What would
move it: new material (the further Scorpion messages Schmeh mentions), or an S5 transcription if a later family needs it.
