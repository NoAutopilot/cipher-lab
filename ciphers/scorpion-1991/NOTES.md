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
