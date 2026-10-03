open
Bulliet, "The Diviner's Handbook" (Mizan Project, mizanproject.org/the-diviners-handbook/, 31 Dec 2021) read in full by GF4-BATCH18 on 3 Oct 2026: the author's own latest account; the violin inscription is still untranslated (only the name Muhammad in line 5 read), Maranao ruled out by M. Kawashima, Tausug/Sulu proposed, a query to R. D. Trimillos pending.

Intake (25 Sept 2026, LANE B4 worker bSUF, minimal check-solved per breadth.md's intake step):
Cipherbrain post "The Top 50 unsolved encrypted messages: 38. The Sufi Fiddle mystery" (Klaus
Schmeh, 3 April 2017) and its full 6-comment thread read in full from
`sources/schmeh/posts/38-sufi-fiddle.txt` (already on disk, fetched 25 Sept 2026). The post's
own account (relaying Louis Kruh's review in Cryptologia 3/1991, pp. not given by Schmeh) states
the inscription "is never solved" in the novel, and Schmeh's own 2014 investigation and direct
email exchange with the author, Richard Bulliet, produced no reading -- only Bulliet's own
unpublished hypothesis (Philippine/Maranao origin). None of the 6 comments (#1 James Simpson via
Facebook: "It's in Arabic or Farsi... that's about all I can see"; #2 tomtoo, off-topic; #3
Bernhard Gruber asking for news; #4 Schmeh replying with the Philippines hypothesis, no reading;
#5 MF, 24 Jan 2019: "Not Farsi, but could be Kurdish"; #6 J Muso, 18 Feb 2023: spoke to an Iraqi,
Iranian, Afghan and Kurdish reader, none could read it) claims a decipherment or even a firm
script identification.

Both solver repositories shallow-cloned (25 Sept 2026), grepped case-insensitively for
"sufi"/"fiddle", then deleted per CLAUDE.md item 3 (digests, not repositories): both repos'
`top50/top50.*` files (dbourdeau/cyphersolver) carry only the same unsolved-list entry ("38. The
Sufi Fiddle mystery -- An inscription found on the inside of an old fiddle has never been
deciphered", linking the same Cipherbrain post); aaymeloglu/unsolved-ciphers had no relevant hit
at all. No decryption or transcription of this item in either repository.

One OpenAlex query (`works?search=sufi fiddle violin inscription decrypted`, key via
Authorization header) returned 0 results. One Semantic Scholar query (same terms, `x-api-key`
header) returned `total: 0`. Full-text search of the open indexes found nothing pre- or
post-1990 corroborating or solving the inscription, consistent with Schmeh's own pre-2017
search finding no independent reference outside Bulliet's novel.

Verdict: open. No transcription of the inscription's script exists anywhere (not in Schmeh's
post, not in Kruh's review as relayed, not published by Bulliet beyond the two low-resolution
images embedded in the post) -- this is fundamentally an authenticity/provenance question before
it is a cryptanalytic one (spec's own framing, specs/sufi-fiddle.json). intake_gate_check.py
output pasted below.

## Intake gate check

```
$ python3 tools/intake_gate_check.py sufi-fiddle
sufi-fiddle: open (line 1) -- edition/page or full-text-search citation found within 6 lines
exit 0
```

## Cheap test 1: script identification (25 Sept 2026, worker bSUF)

Fetched `Suffi-Fiddle-614.png` (scienceblogs.de, 2 requests total including the cover image;
browser UA, 2 s apart; host now free for the next holder). The image is a hand copy of the
seven lines captioned "copied by V. Castle Winter" (name partly illegible), overlaid on a page
of English prose visible faintly behind the ink -- consistent with a scan of a page from
Bulliet's own novel (or working notes), **not** a photograph of the violin panel itself. Rule 2
therefore applies twice over here: this pass reads the image, but the image is already a
secondary hand-copy of an inscription whose primary source (the violin) has never been
photographed or published, per the spec. Any script judgement below is conditional on the copy
being a faithful visual rendering of the original -- unverifiable and, per the spec's own
`authenticity_caveat`, not corroborated by any named third party.

One blind single-pass sign transcription of the copy: **N=165** visible signs, **K=21** distinct
visual shape-types (own sign ids and labels in `ciphertext.txt`; two spans illegible under a
crosshatched "glue" repair mark on the original copy, line 3 mid-line and line 4 line-end, are
excluded from N; two further signs the copyist herself flagged "hard to read?" are recorded but
excluded). K is likely a slight undercount: several dotted-letter clusters (b/t/th; j/h/kh) were
pooled as one label each where the dot pattern was not resolvable at this image's resolution --
noted, not corrected, since resolving it needs a better source image this pass does not have.

### Script checklist: target vs. two reference lines

Reference lines are stated from memory (training-data knowledge of the two script families), not
fetched this pass -- the $1 cap for test 1 was spent on the fetch and the sign pass; no
Wikimedia request was made.

| Checklist item | Target (Suffi-Fiddle-614.png) | Reference: ordinary Arabic-script line (naskh hand) | Reference: Baybayin line (pre-colonial Philippine abugida, e.g. Doctrina Christiana 1593 style) |
|---|---|---|---|
| Sign inventory size | ~21 distinct shapes observed in 165 signs (likely undercounted toward the high 20s/low 30s once positional/dot variants are resolved) | ~28 base letters (abjad), each with up to 4 positional forms | ~17 base characters (3 independent vowels + 14 consonant symbols with inherent /a/) |
| Repeats | High -- top shapes (kaf 23x, lam 19x, waw 15x) recur many times across only 7 lines | High -- any line of ordinary length reuses the ~28 letters repeatedly | High -- reuses the small ~17-symbol set repeatedly |
| Direction | Right-to-left within each line (denser word-initial forms at the line's right edge, trailing connective strokes to the left); Latin numerals 1-7 added in the left margin by the (apparently English-speaking) copyist, not part of the script | Right-to-left | Traditionally top-to-bottom in columns read left-to-right, or (later/printed, e.g. Doctrina Christiana) left-to-right horizontal lines -- not right-to-left |
| Ligature/joining | Strong: letters within each word-group are connected by a continuous cursive baseline stroke, word-groups separated by small gaps -- the same visual joining behaviour as Arabic naskh/ruq'ah cursive | Strong: most letters join to both neighbours; a handful of non-joining letters (alif, dal, ra, waw, zay, ...) still join to the preceding letter | None: each character is a discrete, unconnected glyph; no cursive joining between adjacent syllable-signs |
| Diacritic-like marks | Dots above and below several letters, in clusters of 1-3 dots, on lines 2, 3, 4 and 6 -- visually matches Arabic i'jam (dot-clusters distinguishing e.g. b/t/th or j/h/kh) rather than a single mark per glyph | Dots (i'jam) integral to about half the letters' identity, 1-3 dots above or below; vowel marks (harakat) optional and usually absent in ordinary prose | Kudlit: a single dot (or small stroke) placed above or below a character to change its inherent vowel -- one mark per glyph, not the multi-position dot-clusters seen here |

**Verdict (script ID only, not a reading):** the target is consistent with the Arabic-script
family (an abjad written in a cursive, naskh-like hand -- Arabic, Persian, Urdu, Ottoman Turkish,
or a Jawi-style script such as Maranao, all of which share this checklist profile) on every
checklist axis: small alphabetic inventory with high repeats, right-to-left direction, strong
cursive joining, and multi-position dot-diacritics. It is **not** consistent with Baybayin
specifically: Baybayin has no cursive joining at all and is not written right-to-left, both of
which the target clearly shows (joining, RTL). This does not contradict Bulliet's own
"Philippine" hypothesis as relayed in the post -- comment #6 (J Muso) and the post's own
paragraph about "a linguist" both point to **Maranao**, a Muslim Mindanao language historically
written in a Jawi-style Arabic-derived abjad, not in Baybayin (which is used for Tagalog and
other non-Muslim Philippine languages, not for Mindanao's Muslim languages). So the visual
evidence here is consistent with the Maranao/Jawi strand of the hypothesis already in the post,
while ruling out the generic "Baybayin" framing the spec's `language_candidates` field uses as
shorthand for it. Test 3 (Baybayin character-set comparison) is accordingly **not run**: its own
trigger condition in the spec ("if test 1 supports the Philippine/Baybayin-family hypothesis
specifically") is not met -- the checklist points away from Baybayin, not toward it.

No cryptanalytic claim is made. No pseudo-script judgement is made either: the letterforms
resemble real, distinguishable Arabic-family letters closely enough (not a small set of
repeated abstract squiggles) that a pseudo-script verdict is not supported by this pass, but
whether the text is meaningful Maranao/Arabic/Persian/Urdu, a different Jawi-family language, or
meaningless letter-strings arranged to look like one is outside this test's scope.

Status stays `open`. Next test in the spec's order (test 2, an independent pre-1990 provenance
search) and test 3 (not triggered, see above) are not run this pass, per the brief.

## Cheap test 3: read the hand copy as Arabic script (25 Sept 2026, worker bSUF3)

Note: this is a different test 3 from the spec's original `cheap_tests_in_order` item 3 (a
Baybayin character-set comparison, not triggered since test 1 ruled out Baybayin specifically).
Parent 7d approved this replacement test 3 in ROOM.md at 23:10 UTC 25 Sept 2026: attempt an actual
transliteration and reading of the hand copy as Arabic-family script, now that test 1 established
the script family.

Full transliteration table (letter-by-letter, sure/probable/guess), the (weak, stated-why) control
discussion, and the segmentation attempt across Arabic/Persian/Ottoman Turkish/Malay-Jawi/Maranao
are in `ciphers/sufi-fiddle/reading-attempt.md`. Summary: no coherent line reading in any of the
five languages tried; no primary Sufi formula (Allah, Hu, ya, bismillah, la ilaha illa llah, named
tariqa order) matches any word-group. Three isolated M-graded word-level guesses only: L1 g4
standalone waw ("and", weak); L6 g4 "برکت", one letter from "بركة/بركت" (baraka(t), "blessing" --
a loanword common to Arabic/Persian/Ottoman/Malay/Maranao, the best candidate of the pass but
resting on three guess-or-probable letters); L6 g7/g9 "عل", possibly "على" ("on/upon") with a
dropped final alif, weaker still. No ar/fa/ota/ms/mrw judge corpus exists in `tools/data`, so
`tools/judge_plaintext.py` was not run -- reported as "no judge" per the brief, not omitted.
Every letter graded I (inferred from visual resemblance in a hand copy); counts: sure ~39,
probable ~60, guess ~60, excluded (obscured/uncertain, unchanged from bSUF's own marks) 4
spans/signs. Not a solve; not closed-negative either (no matched synthetic control exists to
license that verdict -- rule 3's own headline paragraph: a negative means nothing without one).
Status stays `open`.

## Web and blog check (GF4-BATCH18 (account-4), 3 Oct 2026)

Plain web searches (WebSearch): (1) `Sufi Fiddle inscription Bulliet violin solved` -- Cipherbrain Top 50 no. 38, Amazon listing of the 1991 novel, Mizan Project "The Diviner's Handbook"; all say unread, none gives a reading; (2) `"Sufi Fiddle" Bulliet inscription decipherment Arabic Maranao` -- the same plus Goodreads, a Columbia Seminar on Religion and Writing abstracts page (blogs.cuit.columbia.edu, WebFetch HTTP 403, not retried) and Mindanao manuscript papers on academia.edu (unrelated to the violin, not opened: academia.edu is 403 from the cloud); (3) `Sufi Fiddle cipher Claude solves OR GPT solves 2026` (model-solve family) -- only the Vals AI / Fable Cyphral Distich announcements (another item) and the "No, ChatGPT didn't solve Kryptos 4" gist; no AI-solve claim for this item; (4) `violin Boston 1968 Harvard Arabic script talisman inscription "Sufi Fiddle" hoax` (descriptive title) -- Mizan Project essay again; (5) `Bulliet violin inscription Tausug biyula Trimillos translation` -- Mizan essay again and Tausug music pages; no published reply from Trimillos and no translation.
**Hit read in full:** Richard W. Bulliet, "The Diviner's Handbook", Mizan Project, 31 Dec 2021 (curl, HTTP 200). The author's own account, later than everything the folder had: the seven lines were copied in 1968 by Labib Zuwiyya-Yamak (Widener Library, Middle East division) from the back plate; Schimmel and Frye saw it; "no one ... could read a single word, except for the name Muhammad in line 5"; Bulliet's own careful copy is printed as Figure 1 (a second, independent copy beside the folder's "V. Castle Winter" hand copy); a 1983 letter relays three Philippine embassy staff who "read the inscription but none of them could really translate it", calling it an anting-anting charm, "Tausug, Maguindanaw or Maranaw"; a bundle of texts bought ca. 2001 from a Boston curio shop (the "Blue Booklet", identified as Maranao) is written in a similar hand; Prof. Midori Kawashima (Sophia University) assured him the violin inscription "is not" Maranao and suggested the Sulu archipelago (Tausug *biyula*); he was awaiting a reply from R. D. Trimillos (Tausug music, UCLA PhD 1972). No translation of the inscription is given anywhere in the essay. Status of this account: the author's own report of an unread text -- not a decipherment, not claimed as one.
Blog site searches: Cipherbrain (scienceblogs.de, Top 50 no. 38, 3 Apr 2017, live re-fetch: still 6 comments, same as bSUF's 25 Sept read -- Simpson, tomtoo, Gruber, Schmeh, MF, J Muso; no reading); klausschmeh.net `?s=Sufi+Fiddle`: Nothing Found; Cryptiana blog `search?q=Sufi+Fiddle`: no posts; Cipher Mysteries `?s=Sufi+Fiddle`: Nothing Found; Apeiron (apeiron.re: no working site search; its Next.js build manifest lists one publication only, `/publication/apeiron-koehler-cryptograms`) -- nothing on this item. Reddit r/codes (OAuth search `sufi fiddle`): 0 results.
Solver repos (fresh shallow clones, 3 Oct 2026, deleted after): dbourdeau/cyphersolver HEAD 46f8056 (2 Oct 2026) -- research/top50/NOTES.md row 38 "low ... no transcription has ever been published ... A palaeography problem before it is a cipher problem", no targets/ folder; aaymeloglu/unsolved-ciphers HEAD d2800bb (27 Sept 2026) -- no "sufi"/"fiddle" anywhere. DECODE: 0 hits for "sufi"/"fiddle" in the on-disk listings (sources/decode/*.tsv).
Requests: mizanproject.org 1 + 1 WebFetch, scienceblogs.de 1, klausschmeh.net 1, cryptiana.blogspot.com 1, ciphermysteries.com 1, apeiron.re 3 (search, home, build manifest; shared across this batch's three targets), oauth.reddit.com 1 (+1 token, shared), blogs.cuit.columbia.edu 1 WebFetch (403), github.com 2 clones (shared); all >= 1.5 s apart.

## Premise check (GF4-BATCH18 (account-4), 3 Oct 2026)

(a) Folder's own mentions of a decipherment or clear copy: none. bSUF3's reading-attempt.md is our own I-graded transliteration (no formula found; best M guess "baraka(t)" in L6). Cross-check from the Mizan essay: Harvard readers and Bulliet read "Muhammad" in line 5; reading-attempt.md lists no محمد and its L5 group 4 is مهيد (m-h-y-d), one letter from محمد -- a lead for the next reader, not a reading.
(b) Other solvers' working files: none -- Bourdeau a list row only, Aymeloglu nothing, no DECODE record; Bulliet's own decades of queries (Schimmel, Frye, embassy staff, Leiden, Kawashima) produced no translation.
(c) Physical neighbours: FIND (provenance, not a reading). Bulliet's Figure 1 is a second hand copy of the same seven lines, independent of the folder's image; and the "Blue Booklet" text bundle (Maranao, a similar hand, Bulliet's own possession) is the closest sibling material. Neither carries a translation of the violin lines.
(d) Recipient / owner side: the violin's owner was never identified (the instrument first went to Widener's Hebrew Division); Bulliet's query to Trimillos was open at Dec 2021, no published answer located.
Result: no decipherment located; the language hypothesis has moved from Bulliet's 2014 "Maranao" (as relayed by Schmeh) to Tausug (Kawashima, 2021). Status stays open.

## Verdict (GF4-BATCH18 (account-4), 3 Oct 2026)

**open (unchanged).** No published or accepted reading of the violin inscription in Bulliet's own 2021 essay (read in full), Cipherbrain no. 38 and its 6-comment thread, klausschmeh.net, Cryptiana, Cipher Mysteries, Apeiron, r/codes, DECODE listings, or either solver repository, searched 3 Oct 2026. Claimed-but-unaccepted: none (only script/language guesses: Arabic or Farsi, Kurdish, Maranao, Tausug).

## While waiting (GF4-BATCH18, 3 Oct 2026)

Nothing here waits on a person. The zero-dependency step: fetch Bulliet's Figure 1 copy from the Mizan essay (mizanproject.org/wp-content/uploads/2021/12/Diviners-Handbook.docx-10.jpg), diff it sign by sign against the folder's hand copy (images/Suffi-Fiddle-614.png) to measure copyist disagreement, and check whether line 5 carries a محمد form on either copy -- before any further reading attempt, and with the language prior moved to Tausug.

## Intake gate (GF4-BATCH18, 3 Oct 2026)

$ python3 tools/intake_gate_check.py sufi-fiddle
sufi-fiddle: open (line 1) -- edition/page or full-text-search citation found within 6 lines
exit 0

$ python3 tools/next_steps.py --wait-only | grep sufi-fiddle
(no line)
