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
