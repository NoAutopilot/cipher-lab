# kaliningrad-2015

status: open

## What this is

Two sheets of paper (a torn front sheet with 20 lines, and a separate second sheet with 6 lines,
not its reverse) found rolled in a bottle during excavation work on Lenin Street, Baltiysk
(formerly Pillau), Kaliningrad Oblast, in 2015. First reported in a Russian local-news article
(strana39.ru, 2016) and covered by Klaus Schmeh as no. 19 on his Top 50 unsolved list
(scienceblogs.de/klausis-krypto-kolumne, 17 Oct 2017; comment thread has 58 comments, no solve).
Source page saved at `sources/schmeh/posts/19-kaliningrad.{html,txt}`.

## Search before solving (rule 1)

Not run fresh this session (out of scope for a breadth cheap-test-1 worker; the spec itself
(`specs/kaliningrad-2015.json`, written 24 Sept 2026) already records: "open per Schmeh 2017;
nothing later found 24 Sept 2026"). The saved Schmeh post's 58-comment thread was read in full
this session and contains no claimed solution, only structural speculation (Thomas Ernst's
autokey/Cardano guess, comment #36) and an image-forensics offer from a Moscow specialist
(Alex Ulyanenkov, comment #37) that trails off without a transcription or reading. Not
independently re-checked against DECODE, the solver repositories, or the archive catalogues this
session; a future worker running check-solved should do that before any campaign (CLAUDE.md
pipeline step 2).

## cheap_tests_in_order[1] -- transcription + images (this session, 25 Sept 2026)

**Images.** Fetched both cryptogram photos named in the post directly from scienceblogs.de
(`ciphers/kaliningrad-2015/images/`, manifest.json with sha1). A third image in the post
(`Kalinigrad-Frequencies.png`) is a reader's own frequency-count graphic, not a third page of the
cryptogram, and was not fetched.

**Transcription.** The brief pointed at "the Russian thread" (simple_life.dirty.ru, linked from
the post, line 171 of the saved text) for the full transcription, but the saved Schmeh post
itself already carries a complete, line-numbered transcript: Thomas Ernst, comment #32
(22 Oct 2017, `#comment-924706`), who transcribed both sheets letter-by-letter from the images
after an earlier attempt (comment #31) was silently dropped by the site's comment filter. This
transcript is the one used here (`ciphertext.txt`), credited in its header; the Russian thread
was not separately fetched (it is a discussion of the same cryptogram by different commenters,
not a second source image, and fetching it was not needed once Ernst's transcript was found
on the page already on disk).

Ernst's own transcription convention (his note, comment #31): he replaced a Cyrillic
hard-sign-like glyph -- described in the thread as looking like a "2" turned upside down -- with
the Latin letter "x" throughout. That is a labelling choice, not a claim about the plaintext
language; `ciphertext.txt`'s header records it so a later worker does not read "x" as literally
attested in the manuscript.

**Row-level agreement check (this worker's own pass against the images).** Read both fetched
images directly and compared word-for-word against Ernst's transcript, line by line. All 26
lines (20 in section I, 6 in section II) match in word count, word shape and letter sequence at
the resolution the photos allow; the only systematic difference found is exactly the "x" for the
hard-sign-like glyph noted above (e.g. image line I/1 reads as `elhxikiracel` at a glance where
the transcript has `elhxikixacel` -- same glyph, different label). No line was found where a
word is missing, added, or reordered relative to Ernst's transcript. This is a spot-check at
normal photo resolution, not a second blind pass with a reconciler (out of scope for cheap test
1; a real second pass would need higher-resolution crops of individual lines, which test 1's
budget did not cover).

**Counts.** `scripts/ic_analysis.py` tokenises `ciphertext.txt` into signs (apostrophe- and
diaeresis-modified letters counted as one sign each, per the alphabet Thomas describes in the
post) and reports:

```
N=978 K=36 IC=0.0657
```

N=978 signs is close to the sum of Ernst's own seven running character-counts per repeated
section (194+194+187+199+166+5 = 945; the difference is tokenisation choices around the four
dotted groups like `x.s.f.d.` and the two section headers, which this script splits into
individual signs). K=36 is one below reader Thomas's count of 37 in the post (comment #4); the
difference is plausibly the "f2" mark on the first "f" of line I/13, which Ernst flags (comment
#32) as possibly a doubled apostrophe rather than a distinct sign, and which this script folded
into a single sign rather than inventing a 37th class. IC=0.0657 differs from Thomas's own
reported ~0.054 (comment #5); this is very likely a sign-boundary artefact (whether an
apostrophe merges into the preceding letter as one sign, as done here, or is scored as a
separate symbol) rather than a disagreement about the underlying text -- flagged, not resolved,
since resolving it is test 2's job (an annealer needs one fixed convention, and cheap test 1 is
not that).

**Matched-N controls.** `scripts/matched_controls.py`, 20 windows of N=978 letters each, seed 42:

```
target:                    N=978  K=36  IC=0.0657
ru (transliterated, 30774): IC mean=0.0563  range=(0.0543-0.0605)   [Gutenberg 30774, "Московия в представлении иностранцев XVI-XVII в.", one fetch]
de (composed_enhg.txt):     IC mean=0.0724  range=(0.0676-0.0765)   [tools/data/de16, existing corpus, only 6855 letters so the 20 windows overlap heavily -- not fully independent]
```

Polish was not fetched (the spec allows "one Gutenberg fetch at most"; that one fetch was spent
on Russian, the language the spec and Thomas both flag as the most likely candidate on IC
grounds, and a first Gutenberg attempt at a Russian text, id 19681 "Детство", turned out to be
an audiobook readme with no prose body and was discarded before the working fetch of id 30774).

The target's IC (0.0657) sits above the Russian control's range and inside/near the German
control's range, at K=36 (vs the corpora's natural alphabet sizes, ~32-33 for transliterated
Russian, ~30 for German). Not informative on its own for language choice -- a K=36 alphabet
that splits many letters into hard/soft or plain/modified pairs would, if the plaintext really
is a simple substitution or a straightforward transliteration, be expected to show a *lower* IC
than a natural-alphabet control of the same language, not a higher one; the target does neither
relative to Russian (higher, not lower) nor sits cleanly inside German's range either. This is
a test-1 observation for test 2 to use, not a verdict; no candidate plaintext, no annealing, no
periodic-IC (cheap test 3) was attempted this session per the brief ("run cheap_tests_in_order[0]
... nothing else").

## Files

- `ciphertext.txt` -- as transcribed (Ernst's comment #32), with the source and the "x for
  hard-sign glyph" convention documented in the header. Never silently repaired (rule 2).
- `images/cryptogram1.png`, `images/cryptogram2.png`, `images/manifest.json`.
- `scripts/ic_analysis.py`, `scripts/matched_controls.py`, `scripts/ru_gutenberg_30774.txt`
  (the fetched Russian corpus, kept so a later worker does not re-fetch it).

## Grades (rule 4)

No reading claimed this session -- transcription and counts only. Not applicable.

## Rule 10

No novelty claim made. This is open per Schmeh 2017 and this session's read of the comment
thread found no solution posted there.
