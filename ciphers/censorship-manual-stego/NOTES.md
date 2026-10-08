open

Check-solved (minimal, 25 Sept 2026, LANE B4 worker bCEN): read sources/schmeh/posts/33-censorship-manual.txt
(Klaus Schmeh, Cipherbrain, "The Top 50 unsolved encrypted messages: 33. The censorship manual steganograms",
3 May 2017) and its full 13-comment thread (latest comment 8 Feb 2023) -- no solution posted for either
mystery, the last comment (James Mulliss, 2023) is a minor observation, not a reading. Manual itself now read
directly (page 14, Illustration No. 11; page 17, Illustration No. 14; quoted below) -- confirms Schmeh's
transcription of the English captions verbatim. Both solver repositories grepped shallow-cloned then deleted
(dbourdeau/cyphersolver, aaymeloglu/unsolved-ciphers): Bourdeau's repo has its own `censorship/` folder, a
real 15 Sept 2026 attempt, outcome "not solved" / "blocked on image resolution" (full detail below) --
confirms still open, not found-solved. OpenAlex (`works?search=`) and Semantic Scholar
(`graph/v1/paper/search`) queries for the item, both 0 hits. Verdict: open.

## Status

open

## What this target is

Two known-plaintext steganograms in a WW2 British postal-censorship training manual, The National Archives
KV 2/2424 ("Postal Censorship: Brochure for Use of Overseas Censorships (Code Section)", War Office). Schmeh's
Top 50 no. 33; UNSOLVED-SURVEY.md row 30; specs/censorship-manual-stego.json.

## Search before solving (rule 1, 25 Sept 2026)

- Cipherbrain post + 13-comment thread (2017-2023): read in full, on disk at sources/schmeh/posts/33-censorship-manual.{txt,html}. No solution.
- Both solver repos: shallow-cloned to /tmp, grepped for `censor|arras|modezeichnung|fashion.draw`, then deleted. `aaymeloglu/unsolved-ciphers` has no hit on this item. **`dbourdeau/cyphersolver` has a `censorship/` folder with a dated attempt (15 Sept 2026, session recorded in its own `profile.json`), MIT code / CC BY 4.0 text (CLAUDE.md rule 8) -- credited and summarized below.** Not copied into this repo verbatim; findings restated here with credit.
- Internet Archive / TNA: not queried directly this pass (Bourdeau's repo already did, see below); the manual is `KV 2/2424` at nationalarchives.gov.uk, downloadable in full (Bourdeau's NOTES.md: 115 images, downloaded 15 Sept 2026, pixel-identical to Schmeh's blog scan for the map spread).
- OpenAlex (`api.openalex.org/works?search=`, key header): 0 results for "censorship manual steganogram Arras fashion drawing".
- Semantic Scholar (`x-api-key` header, one 429 then one retry after a pause per the good-citizen rule): 0 results for "censorship manual steganography morse Arras".
- Calendars/state papers: not applicable (WW2 training manual, not a diplomatic archive series).
- de-crypt.org (DECODE): not queried -- not named in this brief's host list, and this is a British military manual, not a DECODE-catalogued item.

Verdict: **open**, consistent with UNSOLVED-SURVEY.md row 30 and Bourdeau's own 15 Sept 2026 "not solved" outcome.

## Important prior work found: dbourdeau/cyphersolver's own `censorship/` attempt (15 Sept 2026)

Credit: dbourdeau/cyphersolver, `censorship/` folder (code MIT, text CC BY 4.0, CLAUDE.md rule 8). Session
2026-09-15, one Opus session, tools `crib.py`, `bands.py`, `marks_raad.py`. Their own outcome:
`"method": "not solved"`, `"class": "not read"`, `"fraction_read": 0`. Summary of what they established
(their words, restated with credit, not copied code):

- **The map's shift direction is fixed by a 2016 blog fragment.** A commenter ("m") on Schmeh's 14 Oct 2016
  post read pen marks under the Raadhuisstraat tram band as `AATHUT`; `+11` gives `LLESFE`, from *ALLES
  FERTIG* ("everything is ready") -- matching the manual's own statement that the message is shifted 11
  positions (see quote below). This is also visible directly in our own comment-thread text above (comment
  #4/#5, Norbert quoting the 2016 comment). Their `crib.py` predicts a full-wording mark sequence of
  roughly 150-190 marks for the German message -- close to this pass's own reference count for the manual's
  English translation (167 marks, see Morse counts below).
- **The tram bands themselves are not the Morse carrier.** They unrolled four tram bands (Rokin inner/outer,
  Kalverstraat, Raadhuisstraat) and measured ink-run lengths: ordinary alternating tram-line fill (30-90 px
  runs, no two-length dot/dash structure). The actual carrier is small pen marks *added beside* a band
  (matching the manual's own wording, "introduced into the heavy lining in the print", quoted below).
- **"French shorthand" points to Duployé** over the 2017 blog guess of German Stolze-Schrey, supporting the
  2020 blog comment's reading of "Arras" in the Duployan strokes of the signature's initial "H". Neither
  reading verified at available resolution.
- **Blocked on image resolution for both mysteries.** Their mark detector (`marks_raad.py`) found 24
  candidate marks along the Raadhuisstraat band but their widths (1-38 px) do not separate into dots and
  dashes; several are band texture or map lettering. The pen marks are estimated 0.1-0.3 mm, i.e. 2-5 px in
  the best available image (Schmeh's own 2017 photograph, 2,437 px map width, ~17 px/mm); reliable dot/dash
  discrimination needs roughly 1,200 dpi (~47 px/mm). **Downloading TNA's own official digital copy of KV
  2/2424 (115 images) did not help: the map spread (their image 44) is pixel-identical to Schmeh's blog scan**
  -- so re-fetching from TNA is a known dead end, not an untried route.
- Their conclusion: needs a new, sharper photograph of the original at Kew (a record-copying order), for
  both the map (p.17) and the fashion drawing (p.14) signature and dress trims.

This matters for cheap test 2/3 planning: do not re-run a plain mark-detector on the same images (already
tried and already failed on resolution, not on approach) or re-fetch TNA's own scan (confirmed no gain).
Any next attempt needs either a higher-resolution source image or a hypothesis that does not depend on
distinguishing dot- from dash-sized marks at the current resolution.

## The manual's own text (read directly this pass, page images below; not a transcription -- rule 2)

Manual: "Postal Censorship. Brochure for Use of Overseas Censorships (Code Section)." The War Office, London,
S.W.1. `[SECURITY B 408]`. The PDF fetched this pass (`Censor-Manual-WW2.pdf`, TNA reference filenames
`KV-2-2424_036.jpg` through `_053.jpg`, 18 page-images) covers manual pages 2-17 plus the cover -- **not** the
full item; Bourdeau's repo records the full TNA digitisation as 115 images.

**Page 14, "5. Freehand drawings of all kinds."** (Illustration No. 11 -- corrects Bourdeau's NOTES.md, which
calls this "Illustration No. 13"; the manual page itself, `images/manual_pp14-15.png`, plainly reads "Illustration
No. 11"):

> *Comment.*--These must be examined for the introduction of writing in trees, etc., or Morse or other signs
> in the lines of the drawing.
>
> *Illustration No. 11 shows a fashion plate in which a system of Morse (not the usual dot and dash) has been
> introduced into the embroidery, etc., of the dresses.*

Caption under the drawing (signed "Mary Helen Shaw"):

> Message.--(In figures 1, 2 and 3).
> Heavy reinforcements for the enemy expected hourly.
> (In signature in French shorthand)--
> Before Arras.

**Correction to specs/censorship-manual-stego.json:** the manual's own page-14 caption gives **only the
English** text for message part (a) ("Heavy reinforcements..."). The German sentence in the spec
("Massive Feindverstärkungen werden stündlich erwartet") is **not** in the manual's caption -- it is Schmeh's
own added German on his blog post ("The German original reads as follows:"), not sourced to the manual. Same
for part (b): the manual gives only "Before Arras" in English; there is no German in the manual for this
part either (Schmeh's "Vor Arras" is explicitly his own guess, per his own post). The spec's line
`"German original, per the manual's own caption"` should read "per Schmeh's blog, not the manual" -- flagged
here, not yet edited into specs/censorship-manual-stego.json's constraints block by this worker (out of this
test's scope; the orchestrator or a later worker should correct it).

**Also note the manual's own caveat that is easy to miss when working from Schmeh's paraphrase alone: it
explicitly says the fashion-drawing Morse is "not the usual dot and dash"** -- i.e. some other paired-symbol
system standing in for dot/dash, not classic International Morse. Any cheap test built on standard Morse
timing/shape assumptions for the *fashion drawing* should say so; the *map* mystery's caption (below) does
not carry this caveat and plausibly does use ordinary Morse-shaped marks.

**Page 16, "11. Printed maps or printed drawings enclosed in letters."**:

> *Comment.*--Morse can be introduced into the heavy lining in the print such as tram lines, etc.
>
> *Illustration No. 14 shows part of a map enclosed in a letter with Morse so introduced.*

**Page 17, Illustration No. 14 (the map)**, caption:

> The morse letters had to be transposed 11 positions forward.
>
> The message in German when translated read:--
> Oil has arrived, everything is ready.
> Gustav available for the appointed day.

The manual gives **only the English translation** for mystery 2 as well; no German original appears anywhere
in the pages fetched this pass. Schmeh's blog German back-translation ("Öl ist angekommen...") is explicitly
his own guess, not from the manual.

## Morse reference counts (`scripts/morse_counts.py`, International Morse Code as a REFERENCE alphabet only --
see the manual's own "not the usual dot and dash" caveat above for the fashion drawing)

| text | letters | dots | dashes | total marks | letter gaps | word gaps |
|---|---|---|---|---|---|---|
| mystery1a EN "HEAVY REINFORCEMENTS FOR THE ENEMY EXPECTED HOURLY" (manual, verbatim) | 44 | 66 | 47 | 113 | 37 | 6 |
| mystery1a DE "MASSIVE FEINDVERSTAERKUNGEN..." (Schmeh blog only, not the manual) | 50 | 78 | 38 | 116 | 45 | 4 |
| mystery1b EN "BEFORE ARRAS" (manual, verbatim; carrier is French shorthand, not Morse -- count given for completeness only) | 11 | 19 | 10 | 29 | 9 | 1 |
| mystery2 EN "OIL HAS ARRIVED EVERYTHING IS READY GUSTAV AVAILABLE FOR THE APPOINTED DAY" (manual, verbatim English translation) | 63 | 107 | 60 | 167 | 51 | 11 |
| mystery2 DE "OEL IST ANGEKOMMEN..." (Schmeh blog speculative back-translation only) | 68 | 101 | 57 | 158 | 55 | 12 |

The mystery2 EN count (167 marks) is close to Bourdeau's own independent estimate for the German full wording
("about 150-190 marks", their `crib.py`) -- a rough cross-check, not a solve.

## Images on disk (`images/manifest.json`)

- `manual_pp14-15.png`, `manual_pp16-17.png` -- manual pages 14-15 and 16-17, rendered at 300 dpi from the
  fetched PDF (the PDF itself was not kept committed per the breadth-worker file-size rule; its URL and sha1
  are in the manifest so it can be re-fetched).
- `Fashion-Drawing-hires.jpg` -- Schmeh's own 2016 high-resolution photograph of the original at TNA.
- `Fashion-Signature.png` -- close-up of the "Mary Helen Shaw" signature (the claimed French-shorthand carrier).
- `Modezeichnung-1.png`, `Modezeichnung-3.png` -- the fashion drawing and the map as originally posted (2015),
  lower resolution than the hi-res photo / manual scan.

## Cheap test 1 status

Done (fetch + manual read). Test 2 (candidate visual-feature search on the fashion drawing) and test 3
(shorthand comparison) not run this pass, per this brief -- and per the finding above, a plain mark-detector
repeat of Bourdeau's already-failed approach is not a new test; any future test 2/3 should target either a
higher-resolution image (none found beyond what Bourdeau already tried) or a hypothesis that does not need
sub-5px mark discrimination.

## Rule 10

Not classifying novelty; not run by a verifier. Nothing here is claimed as new, unpublished, unread, first,
or never printed -- report only what was found and where it was not found. Both mysteries remain open per
Schmeh's own blog (2017-2023) and Bourdeau's independent 15 Sept 2026 attempt.

## Hosts

scienceblogs.de: 5 requests (browser UA, 2s apart), 0 blocks -- free for the next holder. OpenAlex: 1 request
(keyed). Semantic Scholar: 2 requests (keyed; first 429'd, one retry after a pause succeeded per the
good-citizen rule). No other hosts this pass.

## Next step (suggestion only, not run this pass)

A record-copying order or fresh high-resolution photography at Kew of manual pages 14 and 17 is the only
route either Bourdeau's repo or this pass identified that could break the resolution limit; log as an
ASKS.md row if the orchestrator wants to pursue it. Short of that, the honest next cheap test is the
shorthand comparison (test 3, already narrower and less resolution-dependent than the Morse mark detection)
rather than another attempt at test 2's visual Morse search, which Bourdeau's `marks_raad.py` already ran
and failed on resolution, not method.

## Solver-repo check (bourdeau, 2 Oct 2026)

Fresh shallow clone of github.com/dbourdeau/cyphersolver, HEAD 34e0fc89 (1 Oct 2026), diffed against this folder on 2 Oct 2026 (worker SOLVERDIFF-BOURDEAU, sources/solver-diffs/2026-10-02-bourdeau.tsv). Match class b (they attempted it and closed or explained it).
- Their page: https://github.com/dbourdeau/cyphersolver/blob/main/targets/censorship/NOTES.md ; TARGETS.md #33
- Their extent, in their words: attempted 15 Sept, blocked on image resolution
- Their date: 15 Sept 2026
- Note: already cited in our NOTES.md
Credit: D. Bourdeau, cyphersolver (code MIT, text CC BY 4.0). Status line unchanged; the parent decides any status change from the ROOM flag.

## Web and blog check (GF-A2-12, 3 Oct 2026)

Plain web searches (WebSearch, 3 Oct 2026):
1. `censorship manual steganogram KV 2/2424 Amsterdam map Morse solved` (shelfmark + the item) -- Cipherbrain 14 Oct 2016, 3 May 2017 (top-50 no.33) and 7 May 2017 "Censorship manual steganograms partially solved"; Futility Closet 16 May 2019; Wikipedia list of steganography techniques.
2. `"Postal Censorship" "Brochure for Use of Overseas Censorships" steganography` (the manual's own title, quoted) -- no page about this item; general postal-censorship pages only (Wikipedia, encyclopedia.pub, British Online Archives "secret codes in the second world war").
3. `Schmeh censorship manual fashion drawing Arras shorthand steganogram solution` (distinctive phrase) -- same Cipherbrain posts; also HNN "German spies fashioned messages in drawings of models", opiniojuris "Morse code in filigree?", alecmuffett.com (general press items, no reading).
4. `ciphermysteries censorship manual steganography map Morse tram lines` (descriptive title + Cipher Mysteries) -- no Cipher Mysteries post on this item returned; Cipherbrain posts only.
Site searches: Cipherbrain (queries 1, 3, 4); Cipher Mysteries (query 4: none found); `cryptiana censorship manual steganography WW2 fashion drawing` (Cryptiana: no cryptiana.blogspot.com or Tomokiyo page returned).
Hits opened and threads read:
- Cipherbrain 14 Oct 2016 "Hidden messages in a letter, a map and a fashion drawing", 10 comments (14 Oct 2016 - Sep 2023): Thomas reads the separate 1914 letter example (not part of this target); "m" (15 Oct 2016) finds the "aathut" -> "alles fertig" map fragment (already in this folder via Bourdeau); Bugfish (Sep 2023, two comments) agrees "Alles Fertig" is readable but "before and after that only partial" and links a marked-up map at forum.bugfish.eu/viewtopic.php?t=19 -- that host is unreachable from here (proxy CONNECT rejected; one Wayback CDX attempt, connection reset; not retried).
- Cipherbrain 7 May 2017 "partially solved", 5 comments (Thomas Ernst x4, Thomas; 7 May - 6 Jun 2017): Gerry's "von aras" reading of the signature (shorthand half of mystery 1) and the "alles fertig" map fragment; Ernst's tentative cape/collar Morse letters ("EINE", "S", "TUE", "ND") are offered as guesses needing better images. No full carrier located for either picture.
- Futility Closet 16 May 2019 "A Fashion Puzzle": restates Schmeh ("I could neither find the morse message nor the shorthand message ... It didn't help"); no solution.
- Cipherbrain 3 May 2017 post and its 13 comments: on disk, read in full by bCEN (25 Sept 2026).
Result: no full location of either Morse carrier found on the open web or in these comment threads; the two partial readings (shorthand "von aras"; map "alles fertig") are the ones already recorded in this folder. Requests: WebSearch 5; WebFetch scienceblogs.de 3, futilitycloset.com 1; forum.bugfish.eu 1 (refused by proxy); web.archive.org 1 (connection reset).

## Premise check (GF-A2-12, 3 Oct 2026)

(a) Decipherments the folder already mentions -- found, opened: the plaintexts themselves are printed in the manual (captions, pp.14 and 17, quoted above); what is unread is where and how they are hidden. The two partial locations are "von aras" in the signature (Gerry, Cipherbrain 7 May 2017) and "aathut"+11 -> "alles fertig" under the Raadhuisstraat band ("m", 15 Oct 2016; Bugfish, Sep 2023). No source places the rest of either Morse message: no full mapping found.
(b) Other solvers' working files -- shallow clones 3 Oct 2026: dbourdeau/cyphersolver HEAD 810a777 targets/censorship (NOTES.md, profile.json "not solved / not read / fraction_read 0", crib.py, bands.py, marks_raad.py; already summarised above, MIT/CC BY, credited) -- no rendering of either carrier beyond the published fragment; aaymeloglu/unsolved-ciphers HEAD d2800bb: no file on this item. Bugfish's marked-up map (forum.bugfish.eu) would count here but is unreachable: found (Bourdeau, no reading) / unreachable (Bugfish).
(c) Physical neighbours -- the manual's other pages: Bourdeau downloaded TNA's 115 images of KV 2/2424 and reports no gain in resolution; the manual's own explanatory text around pp.14-17 is quoted above and does not give the mark positions. No answer key or "solution" page is known in the brochure: not found (from the pages read by bCEN and Bourdeau).
(d) Recipient's side -- not a letter; the "recipients" are the overseas censorship stations that used the brochure. Related KV/DEFE censorship files at TNA were not searched this pass (out of a gate-fix brief): not found / not searched.

## GAPS183-censorship-manual-stego (3 Oct 2026, account-4)

Step run: the "Next step" section's cheap test, the shorthand comparison (test 3): does the initial "H" of the
signature "Mary Helen Shaw" (manual p.14) read as Duployé shorthand for the manual's "Before Arras"? Scripts:
`scripts/duploye_control.py` (control render and scoring) and `scripts/sig_hypothesis_score.py` (hypothesis vs nulls).
Crop: `tools/iiif_lines.py --image images/Fashion-Signature.png --top-margin 130 --bottom-margin 130` (one crop,
565x225, shown at 2x). Two vision calls in all, one for the control and one for the signature, each image carrying the
same reference chart of 18 basic Duployan letters (Noto Sans Duployan, from the notofonts jsDelivr mirror).

Matched control (rule 3): a random string of 7 Duployan letters (seed 183) from the same 18-letter inventory, at the
signature's stroke height (about 60 px), blurred and downsampled 2x. Read blind (key opened only after the reading
was recorded): `K F P N R V F` against key `K F P N R V F`, **accuracy 1.000**. The control can fail on the statistic
(a misread letter lowers the edit accuracy), so it is a real test of the reader. Limitation: it is at ceiling and
easier than the target, because the glyphs are machine-set and separated, while the signature is joined handwriting
in a Latin hand. So it shows only that the reader can tell the Duployan primitives apart at this pixel size. It does
not show that a joined cursive Duployé word can be segmented. Match on N and alphabet, not on design (rule 3's
Salviati paragraph).

Target reading of the "H", in Duployan primitives, left to right: `A G A B T B`, every token graded M (rule 4: H 0,
C 0, S 0, M 6, I 0). That is: an entry loop, a long steep rising stroke, a loop at the top, a descending upright, the
crossbar, the second upright. The loops are where a cursive Latin "H" has them anyway. The reading was **not blind**:
the hypotheses were known before the call.

Scores (best local edit similarity of each Duployé phonetic spelling inside the reading; null = 2000 random 6-letter
readings from the same inventory, seed 183):

| hypothesis | spelling | sim | null mean | null p95 | p |
|---|---|---|---|---|---|
| ARRAS | A R A | 0.667 | 0.182 | 0.667 | 0.055 |
| AVANT ARRAS | A V A N T A R A | 0.375 | 0.153 | 0.250 | 0.046 |
| DEVANT ARRAS | D E V A N T A R A | 0.222 | 0.171 | 0.333 | 0.497 |
| VON ARAS (Gerry, Cipherbrain 7 May 2017) | V O N A R A S | 0.286 | 0.188 | 0.286 | 0.354 |
| 10 decoy towns (Lille, Lens, Metz, Lyon, Paris, Calais, Verdun, Douai, Nancy, Reims) | -- | 0.000-0.250 | 0.18-0.25 | 0.33-0.67 | 0.77-1.00 |

Result: **borderline, not decisive.** "Arras" and "avant Arras" sit at the edge of the null (p about 0.05), and every
decoy town scores at or below its null. But the only match is A_A (two loops) plus a G read where R is wanted, both
of them rising diagonals that differ only in slope. Loops at those places are what any cursive Latin "H" carries.
The reader was not blind, and the control does not match the joined-hand design. So this is not a reading, and not a
negative either: the test cannot decide at this resolution and with this control. Nothing changes the folder's
status. No reading is claimed (rule 4: 6 M tokens, no H/C/S). Rule 10: nothing here is new; the "Arras" reading of
the signature is Gerry's (Cipherbrain, 7 May 2017) and the 2020 blog comment's, already credited above.

Requests: cdn.jsdelivr.net 1 (font) plus 1 reachability probe; no other host.

## D2-DUPL joined-hand control + blind re-read (8 Oct 2026, LANE DEFAULT-account-2-20261008-0710)

Pre-registered in PREREG-D2-DUPL.md (pushed ac622c643 before any read). Control material: "VERSION 3" of the Institut
sténographique de France, *Méthode de sténographie Duployé perfectionnée* (1905), Internet Archive `cihm_84595`, PDF
p.12 (printed p.9): four lines of joined Duployé word forms (T D L R with A O), known answer printed on PDF p.13
("Traduction de la version 3"); key `dupl_control/version3_key.tsv` (133 primitives, phonetic). Crops:
`tools/iiif_lines.py --image v-12.png --region 160,1090,1660,400 --lines-per-crop 2 --top-margin 45 --bottom-margin 45`,
scaled to ~60 px stroke height, blur 1.5, halved and doubled (GAPS183's degradation): `images/dupl_control/`.
Two fresh Sonnet subagents, the same 18-letter chart, neither told any hypothesis, the words or GAPS183's reading.

| | read | score |
|---|---|---|
| control (Version 3, 133 primitives) | `dupl_control/read_control.txt` (101 primitives) | **accuracy 0.376**, gate 0.60; chance mean 0.177, p95 0.211; loop-merged (A=O, E=I) 0.519; R/L/G/K subsequence 0.479 |
| target (signature 'H') | `B T B` (long stem, crossbar, long stem) | ARRAS sim 0.000 p=1.000; AVANT ARRAS 0.125 p=0.620; VON ARAS p=1.000; 10 decoys p=1.000 (`dupl_control/score_target.txt`) |

Result: **CONTROL BELOW GATE.** The reader beats chance on joined Duployé at this pixel size but reads only about 38% of
primitives right (it writes most loops as A and confuses R/L/K), so at this resolution a blind primitive read of joined
shorthand cannot carry the A/R distinctions "Arras" needs. Per the pre-registration the target read does not count. It
is also worth recording that the blind reader saw no loops at all in the 'H' (`B T B`, a plain Latin H), where
GAPS183's non-blind read saw `A G A B T B`: the loops that drove GAPS183's p about 0.05 did not reappear blind. Neither
read is a reading (rule 4: 3 M tokens, no H/C/S). Not a negative either (rule 3): a non-test at this resolution. The
shorthand step now needs the ASKS row 126 image; a further primitive-read pass on the present 565x225 image is the same
instrument at the same resolution (rule 3, third-attempt clause) and should not be briefed.
Requests: archive.org 4 (advancedsearch 1, metadata 1, PDFs of cihm_80270 and cihm_84595), cdn.jsdelivr.net 2
(one 404). Vision subagent calls 2.

## Remaining gaps (GAPS183, 3 Oct 2026)
Read so far: unmeasured -- the plaintexts are printed in the manual, and what is unread is where the marks lie; no carrier located beyond the published fragments
- fashion-drawing Morse (p.14 dress trims) - blocker: illegible; marks 2-5 px in every online copy, TNA scan pixel-identical (Bourdeau 15 Sept 2026); waiting-on ASKS row 126 (Kew record copy at 1200 dpi)
- signature shorthand "Before Arras" (p.14) - blocker: illegible; the GAPS183 shorthand test (3 Oct 2026) was borderline at p about 0.05 with a non-blind, design-unmatched control; settling it needs the ASKS row 126 image or a joined-hand Duployé control (While waiting)
- map Morse beyond "alles fertig" (p.17, tram-band pen marks) - blocker: illegible; Bourdeau's marks_raad.py found 24 candidates that do not separate into dots and dashes; waiting-on ASKS row 126

## Escalation (3 Oct 2026)
- [n/a] siblings: a single training brochure, no sibling items carry these illustrations
- [x] clear-pages: the manual's own captions pp.14, 16, 17 read and quoted (bCEN, 25 Sept 2026)
- [n/a] known-keys: the plaintexts are given; there is no key to recover
- [x] print: Cipherbrain threads, Futility Closet, solver repositories read (bCEN 25 Sept, GF-A2-12 3 Oct 2026)
- [n/a] key-rebuild: image steganography, no cipher key involved
- [x] image-check: TNA scan equals Schmeh's (Bourdeau); signature shorthand test run 3 Oct 2026 (GAPS183), borderline
- [ ] retry: joined-hand Duployé control from a period Duployé manual on Internet Archive (While waiting), then a blind re-read
Verdict: keep going: 0 internal gaps; cheapest next: joined-hand Duployé control and a blind re-read (While waiting; the images wait on ASKS row 126), ~$3

## While waiting

- Done 8 Oct 2026 (D2-DUPL): the joined-hand Duployé control read 0.376 against its 0.60 gate, so the blind re-read does not count. No further action here depends on nobody: when the ASKS row 126 image arrives, re-run the same control at the new image's stroke size (PREREG-D2-DUPL.md, scripts/duploye_joined_control.py) before any re-read.
- Waiting on the owner: ASKS row 126, a TNA record copy of KV 2/2424 manual pp.14 and 17 at 1200 dpi or better.

## Remaining gaps (D2-DUPL, 8 Oct 2026)
Read so far: unmeasured -- the plaintexts are printed in the manual, and what is unread is where the marks lie; no carrier located beyond the published fragments
- fashion-drawing Morse (p.14 dress trims) - blocker: illegible; marks 2-5 px in every online copy, TNA scan pixel-identical (Bourdeau 15 Sept 2026); waiting-on ASKS row 126 (Kew record copy at 1200 dpi)
- signature shorthand "Before Arras" (p.14) - blocker: illegible; D2-DUPL's joined-hand control read 0.376 against its 0.60 gate at this resolution (PREREG-D2-DUPL.md), so no blind primitive read of the present image can decide; waiting-on ASKS row 126
- map Morse beyond "alles fertig" (p.17, tram-band pen marks) - blocker: illegible; Bourdeau's marks_raad.py found 24 candidates that do not separate into dots and dashes; waiting-on ASKS row 126

## Escalation (8 Oct 2026)
- [n/a] siblings: a single training brochure, no sibling items carry these illustrations
- [x] clear-pages: the manual's own captions pp.14, 16, 17 read and quoted (bCEN, 25 Sept 2026)
- [n/a] known-keys: the plaintexts are given; there is no key to recover
- [x] print: Cipherbrain threads, Futility Closet, solver repositories read (bCEN 25 Sept, GF-A2-12 3 Oct 2026)
- [n/a] key-rebuild: image steganography, no cipher key involved
- [x] image-check: TNA scan equals Schmeh's (Bourdeau); signature shorthand test run 3 Oct 2026 (GAPS183), borderline
- [x] retry: joined-hand Duployé control + blind re-read (D2-DUPL, 8 Oct 2026): control 0.376 below gate 0.60, non-test at this resolution; only the ASKS row 126 image reopens it
Verdict: parked: every gap has an outside blocker
