# Sektu blog (sektu.blogspot.com), "Debosnys" label, Jun-Aug 2017

Author credited as the blog names them: "Sektu" (self-described "a thaasophobe's blog"; posts
signed only as the blog author, no full name given -- credited as "Sektu" per rule 8, not ours).
All 20 posts under the Debosnys label, 8 Jun - 7 Aug 2017, fetched in one request via the Blogger
JSON feed (`sektu.blogspot.com/feeds/posts/default/-/Debosnys?alt=json&max-results=50`, full post
content included, not summaries) after the label archive page itself returned only a client-side-
rendered shell (0 usable links). Raw feed and per-post plain-text extracts saved to
`sources/sektu/` (not committed images/PDFs, text only). No claim below is ours (rule 10); this is
a search-log summary of someone else's public hypotheses and numbers.

## What Sektu calls things (terminology used below)

- **"the cipher poem" / DCP** = the two-page cryptogram that is "clearly a poem" (rhyming
  couplets, AABB), which Sektu transcribed from Pelling's Cipher Foundation scans. This is almost
  certainly **cryptogram #4** (the "monographe. verse." page + its continuation) in this repo's
  numbering -- Sektu's own line/glyph counts (below) match cryptogram 4 as a *whole* (both pages),
  not cryptogram 4a alone.
- **Debosnys' "plaintext poem"** = the clear French poem "Oh! mes amis je vous supplie en grâce...",
  which Sektu quotes rhyme-pairs from (`grâce/passe`, `blessure/dure`, `brave/nuage`) that match
  this repo's `clear_poems.tsv` c3 lines 1/3, 5/7, 9/11 exactly -- confirms it is the same poem
  transcribed here.
- **"one block of text... above a plaintext poem in French"** = almost certainly **cryptogram #3**
  (the 4-line cipher block sitting directly above the clear poem on the same page here).

## Hypotheses and tests, in date order

1. **8 Jun 2017, "A shiny thing"** -- introductory post; found the cipher via Nick Pelling's Cipher
   Foundation site (source of Sektu's own scans, separate from this repo's Schmeh-sourced images).
   Identifies the two-page cipher poem, AABB rhyming couplets.
2. **9 Jun 2017, "First hypothesis for the Debosnys cipher"** -- phonetic-syllable hypothesis: each
   cipher symbol represents a spoken syllable-final "rhyme group" (onset of the *next* syllable
   folded in), modelled on the accented-phonetic-English device in a Tintin translation. Tests it
   against the clear poem's first two lines using an 1880 French phonetic dictionary. States the
   cipher poem's lines average **15 symbols/line**, vs 10-11 expected for iambic pentameter --
   close to a match if some phonetic groups need 2 symbols.
3. **11 Jun 2017, "Minor update on the Debosnys poem"** -- (a) notes French "identical rhyme"
   convention (onset+nucleus, e.g. cœur/vainqueur) as an alternative to (2)'s onset-split scheme;
   (b) **the clear poem's meter is irregular**, not consistent alexandrine/iambic pentameter --
   "the longest line has 14-15 syllables" (this repo's own count, independently: max 15 syllables,
   line 12 -- see `clear_poems.tsv`); (c) **key methodological finding**: Sektu transcribed both the
   cipher poem (cryptogram 4) and "one block of text above a plaintext poem in French" (cryptogram
   3) and found "quite different" symbol frequency/inventory between them -- read by Sektu as the
   same cipher system used for **two different languages**, i.e. Sektu does not treat cryptogram 3
   as a simple crib for its own neighbouring clear poem.
4. **13 Jun 2017, "Feminine and Masculine Rhymes in Debosnys' Poem"** -- catalogues the clear
   poem's feminine rhymes (grâce/passe, blessure/dure, brave/nuage -- the last flagged "(!)" as an
   imperfect rhyme); hypothesizes the cipher poem alternates masculine/feminine rhyme the same way;
   notes two odd-line rhymes use symbol variants of "♀" and one even-line rhyme a variant of "♂" as
   weak, inconclusive supporting evidence.
5. **15 Jun 2017, "19th Century Sténographie Française"** -- notes most rhyming symbols need only
   ~3 pen strokes, prompting a side-study of period French stenography manuals for efficient
   syllable-encoding conventions (no cipher-specific number reported).
6. **21 Jun 2017 (12:40), "What the Debosnys Cipher Poem isn't"** -- **tested and rejected** the
   French-alexandrine/one-symbol-per-syllable hypothesis against Baudelaire's rhyming alexandrines
   (5 different syllable-division schemes tried): DCP's high-frequency symbols occur *more* often
   than French's high-frequency syllables, and DCP has *more* repeated symbol-pairs than Baudelaire
   has repeated syllable-pairs. Proposes the cipher poem's language might instead be **Greek or
   Latin**, since the reverse side of that leaf (per Klaus Schmeh's blog and a commenter's
   transcription) carries a Greek poem -- identified by Sektu as an altered excerpt of Thomas
   Moore's preface ode to his *Odes of Anacreon* translation, cut off 20-21 lines before the end.
7. **21 Jun 2017 (15:56), "A possible theme for the Cipher Poem"** -- reads Debosnys' altered Greek
   lines as Wisdom asking "why, old one, do you employ your life in the violence of tranquility?",
   and speculates the (still-unread) cipher poem might be Debosnys' answer to that question, mirror-
   ing Thomas Moore's original structure (goddess's question / poet's reply).
8. **23 Jun 2017, "What is Debosnys' 'Portuguese'?"** -- after buying Farnsworth's *Adirondack
   Enigma*: a manuscript page shows Debosnys writing sample sentences in Latin, French, English,
   Spanish and "Portuguese"; Latin/French/English read as competent (Latin is a Vulgate quote), the
   Portuguese sample reads as linguistically doubtful (no verdict reached in this post's excerpt).
9. **28-29 Jun 2017, "Debosnys' Real Name" parts I-IV** -- biographical/identity research (a
   Deletnack Debosnys name analysis, a "Jacob Pomries" identification lead); not cipher-form
   content, one line each: identity hypotheses, no cipher numbers.
10. **30 Jun 2017, "Pasigraphie"** -- background research into whether Debosnys' claim that his
    cipher was "in common use in Europe" matches any known 19th-c. French secret-writing or
    pasigraphy tradition; inconclusive, no matching system found in this post.
11. **3 Jul 2017, "Colonel Henry"**, **5 Jul 2017, "Deletnack"**, **19 Jul 2017 (16:12), "The 19th
    Century Criminal Handshake"** -- further identity/biography research (a Paris Commune "Colonel
    Henry" lead, the "Deletnack" middle name as a possible literary allusion, tattoo/Masonic-grip
    imagery); not cipher-form content.
12. **19 Jul 2017 (23:37), "Back to the cipher"** -- reports a completed transcription of "all of
    the cipher text in the images in Farnsworth's book" (i.e. all four cryptograms, Sektu's own
    segmentation convention, a glyph = one whitespace-bounded ink cluster, which can bundle what
    this repo's segmentation treats as several signs): **1188 total glyph instances, 425 distinct
    glyph types**; 65 repeating glyph-pairs; the single most frequent glyph occurs **89 times
    (7.5%)**, followed by types at 3.6%, 2.5%, 2.4%, 1.9%.
13. **4 Aug 2017, "Debosnys Cipher Transcription Revision"** -- restates the corpus-wide 1188/425
    figure and adds a second, decomposed transcription splitting each glyph into "subglyphs" (an
    explicit attempt at sub-symbol/letter-level structure, with a Backus-Naur-style grammar
    example for one glyph family); reports subglyph frequency follows Zipf's law, with subglyph
    "O" the most frequent, compared favourably (no number given) to French "e" frequency.
14. **7 Aug 2017 (10:00), "A look at N-Glyphs"** -- defines "N-glyphs" (topped by a tilde-like
    subglyph, transliterated N): N never occurs alone but N.N does; favoured reading is N as a
    **nasalization marker** (like the tilde in ã/ẽ/ĩ/õ/ũ), to be tested against French nasal-vowel
    frequency.
15. **7 Aug 2017 (12:08), "Another note on N-Glyphs"** (latest post in the label) -- runs that test:
    Baudelaire's *Fleurs du Mal* (3182 alexandrine lines) has **6536 nasalized syllables, mean 2.05
    per line**, distribution 0:11.5% 1:25.6% 2:28.2% 3:20.1% 4:9.8% 5:3.2% 6-7:1.6%. **"Of the 20
    lines of the cipher poem"** Sektu counts **30 N-glyphs total, mean 1.5/line**, distribution
    0:10% (2 lines) 1:30% (6) 2:45% (9) 3:10% (2). Sektu's own verdict: "this looks like a promising
    match, but more work needs to be done" -- explicitly not a solve claim, still hypothesis-testing
    as of the post series' end.

## Numbers usable for this repo's form test (GOLD-4B)

- **Sektu's own line count for "the cipher poem" is 20**, not 14 -- this matches this repo's
  combined cryptogram-4 total (c4a 14 + c4b 5 = **19** lines, one line off Sektu's count, plausibly
  a segmentation-boundary difference) far better than cryptogram 4a alone (14 lines). This directly
  bears on GOLD-4B's line-count-match finding below: the 14-line coincidence between cryptogram 4a
  alone and the c3 clear poem looks, in light of Sektu's independent 20-line count for the same
  cryptogram, like an artefact of only counting half the cipher poem, not a real structural match.
- Sektu's ~15 symbols/line for the cipher poem is close to both this repo's c4a mean (15.29
  signs/line) and full-c4 mean (14.89 signs/line) -- consistent either way, not a discriminator.
- Sektu's own corpus-wide glyph count, 1188/425, is **not directly comparable** to this repo's N/K
  (1315 signs / 90 raw clusters, 69 merged) without normalizing segmentation conventions first
  (CLAUDE.md rule 3 lesson, PX-BRODEC): Sektu's "glyph" is a whitespace-bounded ink cluster that can
  itself contain several of this repo's atomic "signs" (his own worked example splits one glyph
  into six subglyphs), so his N is lower and K is higher per output-unit than a literal comparison
  would suggest -- flagged, not reconciled, no cost budget in this test to redo either segmentation.
- Sektu **tested and rejected** the French-alexandrine/one-symbol-per-syllable hypothesis for the
  cipher poem against a real Baudelaire control (5 syllabification schemes) in 2017 -- this repo's
  own spec cheap test 3 (homophonic/MASC anneal) should not re-assume pure French alexandrine
  syllable-per-symbol without accounting for this documented negative result.

Requests: sektu.blogspot.com 2 (the label archive page, which rendered nothing usable client-side,
and the Blogger JSON feed for the Debosnys label, which returned full text of all 20 posts in one
call) -- well under the 20-request budget; no further requests needed once the feed's full content
was confirmed non-truncated.
