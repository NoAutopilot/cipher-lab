found-solved
Source of the prior decipherment: the contemporary interlinear decipherment written above every code group on the despatch itself (Spink sale 26066 lot 1184, images 06-07), the printed clear text in Gurwood, Dispatches vol. 9 (1834 pp.388-389; 1838 pp.392-393), and S. Tomokiyo, "Wellington's Polyalphabetic Cipher with a Dictionary Code", https://cryptiana.web.fc2.com/code/maitland.htm (8 Sept 2026, modified 19 Sept 2026; crediting Patrick Hayes and George Lasry), which reads all four strip runs. Status set found-solved by GF4-BATCH6, 3 Oct 2026, by the brief's rule (premise check below); was partial.
Gurwood, *The Dispatches of Field Marshal the Duke of Wellington*, vol. 9 (1834 ed. pp. 388-389; 1838 ed. pp.
392-393) read by this worker (OCR excerpts in `sources/gurwood/`, Internet Archive items
`dispatchesoffie09welluoft` and `vol9dispatchesof00well`), matching the interlinear decipherment word for
word (grade C) -- verdict-format correction, LANE CX2 25 Sept 2026 (the intake gate's own first-line scan was
matching the unrelated word "Open" in "Open Library/Google Books" at line 221, not a real verdict word; no
substantive change).

# Wellington to Lieut.-General Frederick Maitland, Villa Castin, 2 September 1812

**Status: partial** (dictionary code with a contemporary decipherment matching Gurwood's printed clear text
word-for-word at grade C; the dictionary-code scheme and one strip-cipher key were already published by Patrick
Hayes and George Lasry before Tomokiyo's article, which adds two more strip keys; the dictionary edition and the
strip-cipher null/permutation rule remain to be recovered). Written 19 Sept 2026; status changed from `open` to
`partial` 20 Sept 2026, see "Check-solved sweep" below.

## What it is

A despatch from Wellington's head-quarters at Villa Castin (north of the Guadarrama pass, on the road from Madrid to
Arevalo) to the general commanding the Anglo-Sicilian force at Alicante. Two pages (recto and verso of one slip),
signed "Wellington", numbered "5" in red by a later hand, the recto addressed at the foot "Lt Genl Maitland". Roughly
a third of the text is in a **dictionary code**: groups such as `5b429`, `15l405`, `12x408`, each followed by a slash,
with the contemporary decipherment written above each group in a small hand. Three stretches are in a
**letter-substitution cipher** worked with the ten paper strips kept in the same lot (`chdkflbngmxishxgo` = Alicant,
`fxdkfst` = Alicant, two undeciphered runs on the last recto line). The rest is clear English.

It is lot 1184 of Spink sale 26066, *Historical Documents, Autographs and Ephemera* (timed bidding from 28 Aug 2026,
live session 23 Sept 2026, 14:00 London), estimate GBP 12,000-15,000, "offered by descent": the private papers of
General Frederick Maitland (1763-1848), three bound volumes and a box, of which the volume "Letters from the Duke of
Wellington 1812-1846" holds this despatch, five other despatches of Aug-Sept 1812, Maitland's own duplicate letter of
resignation from Alicante, and the wrapper of cipher strips endorsed "a Cypher recd from Lord Wellington July 1812".

## Sources (all checked 19 Sept 2026)

- **Images.** Spink's 19 catalogue photographs, saved in `images/` (see `images/README.md` for URLs, sizes and what
  each shows). The despatch is images 06 (recto) and 07 (verso), 1100 x 248 px each; the site serves nothing larger
  (both CDNs tested, see the README). The strips are images 03 (letters) and 04 (A/B labels). Lot page:
  https://live.spink.com/lots/view/4-ML16CI/great-britain-duke-of-wellington-peninsular-war-etc-general-frederick-maitland-1763-1848-17
  Page snapshot and verbatim description: `sources/spink/`.
- **Printed clear text.** The whole letter is printed in clear in Gurwood, *The Dispatches of Field Marshal the Duke
  of Wellington*, vol. 9: 1834 edition pp. 388-389, 1838 edition pp. 392-393 (from Wellington's letter-book copy;
  OCR excerpts of both in `sources/gurwood/`, Internet Archive items dispatchesoffie09welluoft and
  vol9dispatchesof00well). Gurwood's text agrees with the interlinear decipherment word for word except in the
  places listed under "Readings" below, so every code group has known plaintext (grade C) independent of the
  clerk's interlinear reading (grade H).
- **Tomokiyo.** S. Tomokiyo, "Wellington's Polyalphabetic Cipher with a Dictionary Code",
  https://cryptiana.web.fc2.com/code/maitland.htm, first posted 8 Sept 2026, last modified 19 Sept 2026, announced
  on the Cryptiana blog on 8 Sept 2026 (https://cryptiana.blogspot.com/2026/09/wellingtons-codecipher-during.html,
  one comment, by the author, 9 Sept 2026). Snapshot: `sources/cryptiana/web/maitland.htm` and its three figures
  `maitland1812.png` (the two pages side by side), `maitland.png` (his table of 56 code groups with their
  readings), `maitland2.png` (the strip keys). He credits Patrick Hayes (for Spink) and George Lasry with the
  dictionary-code scheme and "Key 1" of the strip cipher, adds Keys 2 and 3, and reads the last undeciphered recto
  run as "Vila Castin" (with Gemini). He states that the null and key-permutation indicators are undiscovered.
- **Urban.** Mark Urban, *The Man Who Broke Napoleon's Codes* (2001), pp. 232-233 and 252-253 (cited by Spink and
  Tomokiyo; not consulted directly here): Scovell's dictionary code of the form 134A18 = page 134, column A,
  word 18, and Wellington's 11 Aug 1812 letter to Popham saying he had no cipher.
- **Solver repositories.** Bourdeau, github.com/dbourdeau/cyphersolver: no Wellington, Maitland or Scovell folder
  (fetched 19 Sept 2026). Aymeloglu, github.com/aaymeloglu/unsolved-ciphers, SHORTLIST.md (raw, fetched 19 Sept
  2026): "New open items seen on Tomokiyo's blog in 2026: ... Wellington's Peninsular War code (Sept 8 2026 post,
  worth a look)", no tracker row, no work.
- **Other.** Web search for the lot, "Villa Castin" + Maitland + cypher, Cipherbrain and DECODE (de-crypt.org) found
  nothing beyond Spink, Tomokiyo, Gurwood and Oman (19 Sept 2026). Oman, *History of the Peninsular War* vol. 6
  (Gutenberg 73069) places Wellington at Villa Castin on 2 Sept and Arevalo on 3 Sept 1812 and quotes the 31 Aug and
  4 Sept letters to Maitland but not this one. Not checked: the Scovell papers at TNA (WO 37), the Bentinck papers
  (Nottingham, Pw Jd), and Maitland's in-letters at Alicante, which would carry the incoming copy of the same
  code.

## Historical frame

Frederick Maitland (3 Sept 1763 - 27 Jan 1848), lieutenant-general 1811, was appointed second in command in the
Mediterranean under Lord William Bentinck on 1 Jan 1812 and commanded the Anglo-Sicilian corps (about 9,000
British, King's German Legion, Swiss, Sicilian and Neapolitan troops) that Bentinck sent from Sicily to Suchet's
flank: off Palamos 31 July 1812, landed at Alicante in August, entrenched there at the end of August, and,
his health broken, resigned the command to General Mackenzie at the beginning of November 1812 (Dictionary of
National Biography, "Maitland, Frederick"). Tomokiyo's article hesitates between him and his cousin Sir Thomas
Maitland; the lot's own address line "Lt General F. Maitland" (image 11) and the DNB settle it. The despatch
answers Maitland's letter of 24 Aug, tells him to occupy the heights south and west of Alicante with his left on the
sea, explains that the Secretary of State's cipher (announced in the 29 Aug addendum as "now on its passage from
England", image 08-09) cannot spell words, so the strip alphabet sent to Bentinck is to be used for words not in
it, and encloses a corrected alphabet.

## What is established (H = read from the document, C = from Gurwood's printed text, S = inferred with evidence)

- **Group format** (H, S). A code group is `<position><letter><page>`: a number 1-33, one lower-case letter from
  {b, l, m, n, x, y, z}, and a page number 14-438. Page numbers are alphabetical (alphabet 14, and 17, be 38,
  cypher 79, day 116, early 146, head 203, me 261, occupy 288, sea 365, the 405, use 429, you 438), and positions
  within a page are alphabetical too (that 7, the 15, this 23 on p. 405; use 5, to use 6 on p. 429; cypher 21,
  to cypher 22 on p. 79; more 1, morrow 13 on p. 272; south 17, southward 23 on p. 388; you 8, your 15 on p. 438).
  So the dictionary runs A on pp. 1-c.30 to Y about p. 438: a pocket spelling dictionary of about 440-450 pages,
  entries listed noun then verb ("Cypher / to Cypher", "Use / to Use", "Rest / to Rest"), which is Entick's
  arrangement among others.
- **The middle letter is part of the word's code, not a null** (S). Every repeated word has the same letter each
  time: of 17l289 (x2), are 9n23 (x2), at 3y28 (x3), and 10n17 (x2), to 12x408 (x4), words 23x436 (x2), cypher
  21l79 (x2), the 15l405 (x3), you 8y438 (x2), will 4y434 (x2), it 6y232 (x2). Seven letters are used, so it is
  not simply "column A / column B". Adjacent entries share a letter or not: use 5**b**429 and to use 6**l**429 are
  consecutive entries, so b and l denote the same column; the 15**l**405 and this 23**n**405 are about 40 entries
  apart, which fits "the" in the first column and "this" in the second. Working hypothesis: two columns, each
  with several homophonic letters (l, b, ... = first; n, ... = second), to be settled once the dictionary is found.
- **Plaintext of every group** (H and C). The interlinear reading and Gurwood agree; the coded text drops the
  article in "which is [a] fortunate event" and codes "tomorrow" as "morrow" (13y272, next to more 1y272).
- **Strip cipher** (H, S). Ten strips, five lettered A (plaintext) and five B (ciphertext), each carrying five
  letters of a 25-letter alphabet without j (image 03: `d a m x r / c l w i q / f s e n y / g z h t u / b v p o k`
  on one row, `m f w o q / k x p d e / h i b s v / n z u t y / l c a g r` on the other; the row-to-set assignment
  is Tomokiyo's, not visible in the photograph). Tomokiyo's Keys 1-3 (`maitland2.png`) read Alicant (x2), Arevalo
  and Vila Castin; more than half of each ciphertext run is nulls, and the rule that marks nulls and selects the
  strip permutation is unknown.

## Transcription

`ciphertext.txt`: full diplomatic transcription of both pages, one manuscript line per line, each code group
followed by its interlinear reading in braces, doubtful characters marked `?`. Made 19 Sept 2026 from images 06-07
at 2x, 3x and 4x, in two independent passes by separate agents, reconciled by a third reading against Tomokiyo's
table and Gurwood's text; the disagreements are listed at the foot of the file.

| | count |
|---|---|
| code groups (occurrences) | 73 |
| distinct code groups | 57 |
| letter-cipher runs | 4 (17, 21, 18 and 7 letters) |
| doubtful characters in the reconciled text | 2 (one letter in each of the two unread runs) |
| pass B disagreements with the reconciled reading | 14 spots (listed at the foot of `ciphertext.txt`), all resolved at 8x or by the adjacent-entry logic; none changes a page number |
| pass A disagreements with the reconciled reading | 13 spots (same list), including one phantom group produced by a tile boundary and two interlinear words it could not read; 8 spots were raised by both passes; none changes a page number |

## Readings, graded per token

| grade | tokens | what |
|---|---|---|
| H | 73 code groups (57 distinct) + 2 strip runs | interlinear reading by the contemporary hand: every code group, and "Alicant" above both short runs |
| C | 81 of 81 reading words | the same readings found in order in Gurwood's printed text (`check.py`) |
| S | 2 strip runs | the two runs on the last recto line have no interlinear reading; Tomokiyo's Key 1 gives Arevalo (agrees with the word written below) and Key 3 "Vila Castin" (agrees with Gurwood's "Head quarters are this day at Villa Castin"); both keys are his, not re-derived here |
| M | 2 characters | one letter in each of those runs (see the foot of `ciphertext.txt`) |
| I | 0 | nothing repaired |

`check.py` regenerates `codebook.tsv` (57 groups: page, letter, position, reading, count, lines) from
`ciphertext.txt`, checks that every repeated group carries the same reading, that the readings occur in Gurwood's
text in manuscript order, that page numbers run alphabetically, and exits non-zero if the committed table is stale.
Compared with Tomokiyo's table (`maitland.png`): identical on all 56 groups he lists, plus 22l79 "to Cypher"
(r5), which he omits, and 8b243, which he reads "let?" and the clerk wrote "left" (Gurwood: "to rest your left on
the sea").

## Next step

1. **Identify the dictionary edition.** Test candidates on the Internet Archive, Google Books and HathiTrust
   against the constraints in `codebook.tsv` (word -> page, and position within column): the first entry of
   p. 272 is "more", the 13th "morrow"; "the" and "that" are on p. 405, "this" on the same page; "you" and
   "your" on p. 438; "alphabet" on p. 14; "supplying" is the 33rd entry of its column on p. 400, so columns hold at
   least 33 entries. Candidates: Entick's New Spelling Dictionary (Dilly, many editions 1764-1812), Johnson's
   Dictionary in Miniature, Perry's Royal Standard, Walker's abridgements, Sheridan abridged. A first pass on 19 Sept 2026
   (below, "Dictionary candidates") rules out the editions on the Internet Archive; the London Entick editions of
   1801-1811 and Scott's (Edinburgh) are the next to test, from a browser.
2. Once the edition is found, the seven-letter column code and the "position" convention (entry or line) follow
   directly, and the Scovell attribution can be tested against Urban's 134A18 example.
3. **Strip cipher:** with the four known runs and their keys, search for the null rule (e.g. every second letter,
   or letters outside the current strip pair) and the permutation indicator; a control run should be a synthetic
   run of the same length with the same key.
4. **Archives:** Wellington's other 1812 coded letters to Maitland and Bentinck (Bentinck papers, Nottingham; WO 37
   Scovell) would give more groups from the same dictionary.

## Dictionary candidates

First pass, 19 Sept 2026, by an agent working from Internet Archive page OCR (`_djvu.xml`, printed page numbers read
from the running heads; HathiTrust gave 403 and the Google Books API 429 from this environment, so only editions on
the Internet Archive were tested). Target: alphabet 14, be 38, can 66, day 116, early 146, fortunate 184, head 203,
me 261, occupy 288, period 308, rejoin 346, south 388, the 405, use 429, will 434, you 438.

| edition | IA item | result |
|---|---|---|
| Entick, *New Spelling Dictionary*, London 1787, 1795, 1800 (Crakelt) | bim_eighteenth-century_enticks-new-spelling-di_entick-john_1787 / _1795 / _1800 | same pagination in all three: alphabet 13, be 32, early 123, fortunate 156, head 177, more 244, occupy 258, period 276, rejoin 313, south 354, the 382, use 426, will 434, you 438. Two columns, 50+ entries per column. Agrees at the end (use, which, will, with, you) and nearly at the start, but runs 23-34 pages early from E to T. **Closest, not it.** |
| Entick variant "copious and accented vocabulary", 1791 | ..._entick-john_1791_0 | alphabet 10, period 202: no |
| Entick, American ed. with Lindley Murray, 1812 | enticksnewspell00murrgoog | early 118, rejoin 265: no |
| Perry, *Royal Standard English Dictionary*, 1806 and 1775 | royalstandarden00cogoog; bim_..._perry-william-lecturer_1775 | the 429, will 474; early 115: no |
| Johnson's *Dictionary in Miniature* (Hamilton), 1810 and 1799 | johnsonsdictiona00jo; bim_..._johnsons-dictionary-of_1799 | about half the scale (occupy 156): no |
| Jones, *Sheridan Improved*, 1812 | 10797864bsb | the 377, you 426, 9-34 pages early throughout: no |
| Bentick 1786, Sheridan 1800, Newbery 1792 | bim_... items | alphabet 9 / 9 / too small: no |
| Fisher 1788, Browne *Union Dictionary* 1810, Walker 1791 octavo | bim_..._fisher-a-anne_1788; uniondictionaryc00brow; bim_..._walker-john_1791 | page numbers not OCR-readable; leaf counts imply c. 380, 490 and 500+ pages: unlikely, untested |

Not on the Internet Archive, so untested: Scott's *New Spelling, Pronouncing and Explanatory Dictionary*
(Edinburgh 1797, 1807), Fulton and Knight (Edinburgh 1802), any London Entick of 1801-1811, Ash, Fenning, Bailey,
Dyche pocket editions, pre-1813 Walker abridgements. These need HathiTrust or Google Books from a browser.

Observation from the pass: the target gives A-B about 62 pages (14% of c. 440) and T-Z only about 35 (8%), whereas
Entick has A-B 37 and T-Z 60 with the same total. Either the dictionary has an unusual distribution (a
pronouncing dictionary with long A entries?), or the "page" number is not a plain page number in the middle of the
alphabet. The page numbers in `codebook.tsv` are read consistently by all three readers and confirmed by
Tomokiyo, so the transcription is not the weak point. Literature: Wikipedia ("Book cipher", "George Scovell") and
navyhistory.au describe Scovell's system as page, column letter, entry number in "an English pocket dictionary that
both headquarters had copies of" without naming it; a full-text search of Urban's book on the Internet Archive
found no dictionary named either.

## Failure log

- 19 Sept 2026: no larger image exists online; the CDN's size parameters only pad, spink.com serves byte-identical
  files, and the auctionmobility catalogue API needs a client token.

## Dictionary search, 19 Sept 2026

Second pass, worker session, about two hours: 57 volumes tested against the page constraints of `codebook.tsv` by
Google Books search-within (printed page numbers) and Internet Archive per-page OCR, full results in
`DICTIONARY.md` and `dictionary_tests_2026-09-19.txt`, scripts in `tools/gbooks_search_within.py` and
`tools/ia_djvu_headwords.py`. **Not found.** Five Entick settings (1766-1780, 1781-1783, 1782, 1784, 1786-1800)
plus the 1812 settings, Perry (six settings), Scott 1807/1810, Fulton and Knight, Jones, Sheridan, Walker and two
abridgments, Browne, Enfield, Fisher, Webster, Johnson's Miniature, and the English parts of Nugent, Vieyra and
Bottarelli all fail. Near misses: Entick's 1782 setting has alphabet 14 and south 388 but runs on to youth 482;
Entick 1786-1800 matches the tail (use 426, will 434, you 438) but is 23-34 pages early in the middle; Perry 1795
matches the middle within a few pages but starts at p. 17 and ends at 455. Three inferences (grade I): the
dictionary spells "Cipher"; its T-Z is compressed to half the usual length; the 41 body groups have positions
1-23 only, so a column holds about 24 entries, a smaller format than Entick's 12mo. HathiTrust is unreachable
from this environment (Cloudflare 403); Scott 1797/1799, Perry's 24mo 1810-1813, Jones 1800, the 1810 Walker
abridgment, Dublin Entick reprints and Urban pp. 232-233 remain untested (list in `DICTIONARY.md` section 6).

## HathiTrust pass, 20 Sept 2026

Worker session. HathiTrust's pages stay behind a Cloudflare challenge and the browser tool could not be used (Chromium
rejects the container's proxy certificate; the fix was refused by the session's permission policy, see CLAUDE.md),
but the Bibliographic API and the HathiTrust Research Center's Extracted Features API both answer, and
`tools/htrc_ef_headwords.py` places headwords from the per-page word counts they serve. 19 volumes tested, everything
HathiTrust holds of the candidate titles between 1764 and 1812: Entick 1783, 1791, 1812; Perry's American editions
1788-1806; Jones 1798, 1804, 1805, 1812; Walker 1791-1809; Sheridan 1794; Johnson abridged 1797; Peacock 1785;
Wesley 1764. **All fail**; best is Jones 1805 with a maximum residual of 54 pages. Scott 1797/1799, Fulton and Knight
1802-1808, Jones 1800, London Perry, the 1810 Walker abridgment and Dublin Entick are not in HathiTrust at all; the
"Perry 24mo 1810-1813" and "Walker abridgment 1810" of the 19 Sept list turn out to be American printings and an 1836
edition. Details, corrections and what remains in `DICTIONARY.md` section 8; raw output in
`dictionary_tests_2026-09-20-hathitrust.txt`. Status unchanged: open; dictionary edition still unidentified.

## Dictionary search, round 3, 25 Sept 2026

Worker session (LANE YX YX-WMDICT). Tested every untested edition reachable from this environment: 2 new Fulton
and Knight copies (1826, 1833) and 2 new Perry London settings (1777, and a second 1788 pagination) found via
Open Library/Google Books and tested against `codebook.tsv` -- **all fail**, no constant offset. Confirmed by
holding record (Open Library) that Scott's three printings (1786 Toronto, 1797 Harvard OCLC 82324728, 1799
Dublin), Fulton and Knight's actual 1802 first edition, and any Dublin Entick reprint have **no digital copy
anywhere searched** (HathiTrust Bibliographic API checked by OCLC and LCCN for the Scott 1797 copy: not held).
Status unchanged: partial, dictionary edition still unidentified; the remaining candidates now need a library
copy, not a further cloud search (Access playbook item 4). Fixed `tools/gbooks_search_within.py`'s per-word
sleep (0.5s -> 1.5s) to meet the good-citizen host rule; it had been non-compliant since 19 Sept. Full detail,
counts and request tallies in `DICTIONARY.md` "Round 3, 25 Sept 2026".

## Check-solved sweep, 20 Sept 2026

Six independent search passes (check-solved skill), run before continuing the campaign, per CLAUDE.md rule 1.

### 1. Web search + WebFetch blind sweep

Checked 15 queries covering the target's name, shelfmark, Tomokiyo's article title, "solved"/"undeciphered",
Cipherbrain, DECODE and the two solver repositories, plus a live WebFetch of Tomokiyo's article and blog post.
Confirms Tomokiyo's article (https://cryptiana.web.fc2.com/code/maitland.htm, posted 8 Sept 2026, last modified
19 Sept 2026) is exactly the partial decipherment already recorded in this file: dictionary-code format
(page/column/entry, e.g. `134A18`), "Key 1" for the strip cipher credited to Patrick Hayes (Spink's expert) and
George Lasry, Keys 2-3 added by Tomokiyo, one previously-undeciphered strip run resolved as "Vila Castin" (with
Gemini's help). Live quote: "The indication of these nulls as well as the indication of the permutation of the
five strips remain to be discovered." The companion Cryptiana blog post
(https://cryptiana.blogspot.com/2026/09/wellingtons-codecipher-during.html) corroborates. No other independent
solution, key or documented attempt found anywhere else on the open web: Cipherbrain- and DECODE-targeted
searches returned nothing specific; the two solver repositories returned nothing specific; a Schneier on
Security post that surfaced for "Wellington Maitland cipher solved" concerns an unrelated c.1653 cipher and is a
false-positive lead, ruled out.

### 2. Internet Archive full text, Gurwood vol. 9 (two independent IA copies)

Fetched and grepped the full OCR text of both `dispatchesoffie09welluoft` (1834-39 printing) and
`vol9dispatchesof00well` (1838 printing). Confirms the despatch is printed in full clear English prose in both
copies (pp. 388-389 and pp. 392-393 respectively), word-for-word consistent with what this file already records
under "Printed clear text," including the sentence naming the cipher itself ("As the cipher sent by the
Secretary of State is deficient as affording no means of spelling words, I propose to use that which I sent to
Lord William Bentinck...") and "Head quarters are this day at Villa Castin, and will be to-morrow at Arevalo."
No occurrence of the letter, "Villa Castin," or any code-group-shaped token found outside these two printings.
**Unchecked, not negative:** HathiTrust's catalogue web UI returned HTTP 403 to curl from this environment and
was not searched directly; its Bibliographic API is reachable but does not do full-text search. The
Supplementary Despatches and any Historical Manuscripts Commission/Camden Society Wellington volumes were
checked only via WebSearch snippets, which found no specific match, not by opening or full-text-searching the
volumes themselves.

### 3. Community-list sweep (Cryptiana, Cipherbrain, Cipher Mysteries, MysteryTwister, r/codes)

Live-fetched Tomokiyo's `maitland.htm`, his blog post and its comment thread, and his `unsolved.htm` index.
New detail beyond what this file already had: Tomokiyo's own comment on his blog post (9 Sept 2026, quoted in
full) states that *before* his article, Spink's own lot page already carried an analysis by Patrick Hayes
("an expert who works with the auction house," thanking "cryptanalyst George Lasry for providing his
expertise") that had *already* established the full scheme of the dictionary code, associated it with Scovell
(citing Urban), identified the strip-cipher substitution Tomokiyo calls "Key 1," and quoted relevant letters —
i.e. the core decipherment and Scovell attribution are Hayes/Lasry's, predating and prompting Tomokiyo's write-up,
which he explicitly credits. Also new: this item does **not** appear on Tomokiyo's own "Unsolved Historical
Ciphers" index page (`unsolved.htm`) — it is filed only as a standalone article, not among his listed open
targets. **Unchecked, not negative:** Cipherbrain (cipherbrain.de / scienceblogs.de/klausis-krypto-kolumne),
Cipher Mysteries, MysteryTwister and r/codes returned no hits for site-restricted WebSearch queries, but none of
the four sites could be fetched directly in this environment (TLS error, connection blocked, HTTP 406, HTTP 403
respectively), so this is a search-index-only absence, not a check against those sites' own search or full
comment sections.

### 4. DECODE database (de-crypt.org), queried live

Site and its quick-search endpoint (`RecordsList?cmd=search&search=<term>`) are reachable (HTTP 200) and the
search mechanism was sanity-checked as functional. No record for Wellington, Maitland, Frederick Maitland,
Villa Castin, Alicante, Spink, sale 26066, Scovell, "Duke of Wellington," or "Peninsular" ("No records found"
for every such query). The only queries returning any hits (1812, 1184, Bentinck) matched unrelated records: a
15th-century Aragon cipher, a Charles V/Milan cipher, two blank-field key records, and a distinct Napoleonic
French-side cluster naming Marmont, Suchet and the Duc de Bassano. Corroborates this file's prior 19 Sept 2026
DECODE search with a fresh, direct query. Closed-negative.

### 5. github.com/dbourdeau/cyphersolver

Fresh shallow clone. No target folder, no docs page, and no mention of Wellington, Maitland, Scovell, Villa
Castin or Alicante in README.md, TARGETS.md, SOLVED_CATALOGUE.md, CATALOGUE.md, SOLVED_RANKING.md or
`docs/search.json`. The only repo-wide "Maitland" hits (2, both in `urquhart/NOTES.md` and `docs/urquhart.html`)
refer to the unrelated 19th-century Maitland Club (an Edinburgh antiquarian society that reprinted Sir Thomas
Urquhart), confirmed by reading the surrounding text. Corroborates and extends this file's 19 Sept 2026 finding.
Closed-negative.

### 6. github.com/aaymeloglu/unsolved-ciphers + George Lasry's (robertpitt) repositories

Fresh shallow clone: no Wellington/Maitland target folder; README.md, TARGETS.md and CATALOGUE.md have zero
occurrences of the relevant names. The only mention anywhere in the repo is the same SHORTLIST.md line already
recorded in this file ("New open items seen on Tomokiyo's blog in 2026: ... Wellington's Peninsular War code
(Sept 8 2026 post, worth a look)") — a bare pointer, no tracker row, no work done. robertpitt's 40 public GitHub
repositories and a GitHub code search for "wellington maitland" / "maitland cipher" scoped to that user returned
no hits. Closed-negative.

### People and dates established by this sweep

- **Patrick Hayes**, cataloguer/expert for Spink, and **George Lasry**, cryptanalyst: independently established
  the dictionary-code scheme (page/column/entry) and the strip-cipher "Key 1", and made the Scovell attribution,
  on Spink's own lot page, before 8 Sept 2026 (the date Tomokiyo says he accessed it).
- **Satoshi Tomokiyo**: published "Wellington's Polyalphabetic Cipher with a Dictionary Code" on Cryptiana,
  first posted 8 Sept 2026, last modified 19 Sept 2026, crediting Hayes and Lasry, adding strip-cipher Keys 2
  and 3 and one further resolved run ("Vila Castin," with Gemini's help); announced on the Cryptiana blog the
  same day, one comment (by Tomokiyo himself, 9 Sept 2026) giving the fuller Hayes/Lasry credit quoted above.
- No further named contributor or dated attempt was found by any of the six passes.

### Verdict

All six passes confirm, and none contradicts, the picture this file already recorded on 19 Sept 2026: the
despatch's plaintext is established throughout at grade C (Gurwood's independently printed text) and is not in
question, and a partial decipherment of the code system itself — the dictionary-code scheme and one of (now)
three strip-cipher keys — was already public, credited to Patrick Hayes and George Lasry, before Tomokiyo's 8
Sept 2026 article, which he explicitly builds on and extends. No search surfaced a complete solution (so not
`solved` or `found-solved`), and none surfaced grounds to abandon the target (so not `closed-negative`). What
remains open is unchanged: the printed dictionary edition (57+ candidates tested and ruled out, see "Dictionary
candidates" and the HathiTrust pass above) and the strip-cipher null/permutation rule. **Verdict: the status
changes from `open` to `partial`** — Tomokiyo/Hayes/Lasry's existing, independently-corroborated published work
is a partial solution of this target, not a reason to close it, and not grounds to call it solved.

## GAPS-wellington-maitland-1812 (2 Oct 2026, account-4)

Verdict step of the 1 Oct 2026 finish-or-blocker pass, run 2 Oct 2026 01:57-02:2x UTC (clock read): ASKS.md row 101
filed, self-contained for the owner's desk (parent.md duty 3b) -- the four undigitised candidate editions, their
holding records as read that day (Open Library OL19659468M and OL18902006M from the University of Toronto MARC, OL62336566M
from Harvard's bibliographic metadata with OCLC 82324728 / LCCN 10025951, Google Books gEBCnQEACAAJ for the Dublin 1799
Wogan printing), the five discriminator pages with the one question each answers (DICTIONARY.md section 1), each library's
public contact read on its own page that day (Fisher fisher.library@utoronto.ca; Houghton houghton_library@harvard.edu,
Imaging Services via the HOLLIS Special Request form, about USD 8-12 an image, 20 business days; TCD rescoll@tcd.ie,
images via Digital.Collections@tcd.ie, three weeks minimum) and a paste-ready request text with the disclosure sentence
(outreach/README.md rule 1). Not confirmed: which Dublin library holds the 1799 printing -- Library Hub Discover answered
a Cloudflare challenge (HTTP 403, one retry with a browser agent) and the NLI catalogue HTTP 403; Harvard's LibraryCloud
API answered HTTP 429 twice, so the HOLLIS record itself was not opened. Gap 1 above moves from needs-physical-access
to waiting-on ASKS row 101; the Verdict line now names gap 2's format search (~$4). Status word unchanged: partial.
Vision calls 0. Requests: openlibrary.org 3, googleapis.com 1, api.lib.harvard.edu 2 (429, 429), discover.libraryhub.jisc.ac.uk
2 (403, 403), catalogue.nli.ie 1 (403), library.utoronto.ca 1, fisher.library.utoronto.ca 3 (301s), library.harvard.edu 2,
tcd.ie 3 (one 404), spink.com 1 (lot 1184 shows SOLD GBP 42,000), plus the web and blog check's requests listed in its own
section below.

## Remaining gaps (finish-or-blocker pass, 1 Oct 2026)
Read so far: 73 of 73 code-group occurrences (57 distinct) read at H and at C, with 81 of 81 reading words in manuscript order in Gurwood vol. 9 (`check.py`, NOTES "Readings, graded per token"). 4 of 4 strip runs read: 2 at H ("Alicant"), 2 at S ("Vila Castin", "Arevalo", from Tomokiyo's Keys 3 and 1, not re-derived here). 2 letters are M. So 77 of 77 cipher units (100%) read as sense, 75 of them at H. What is still partial is the key: the dictionary edition, and the strip cipher's null and arrangement rule. Adversarial check, 2 Oct 2026 (clock read): the classifier's Urban gap is closed by IA full-text snippets (see print below), and three sibling leads were added that the classifier missed (Scovell's "Conradus notebook", the Pellew alphabet, and the corrected alphabet enclosed on 2 Sept).
- Dictionary edition behind all 57 groups, among the editions still worth testing (Scott 1786/1797/1799, Fulton and Knight 1802, any Dublin Entick, the 14 catalogue-only London Entick 1801-1811 records) - blocker: waiting-on ASKS row 101 (filed 2 Oct 2026 by GAPS-wellington-maitland-1812: five discriminator pages, 14/79/272/405/438, from the Toronto, Harvard and Dublin copies, with each library's contact read that day and a paste-ready request; the Dublin 1799 holder is unconfirmed from the cloud, Library Hub Discover and the NLI catalogue both bot-blocked); previously needs-physical-access; DICTIONARY.md "Round 3, 25 Sept 2026": none of these has a digital copy in Google Books, IA or HathiTrust (Scott 1797 OCLC 82324728 / LCCN 10025951 not held). About 80 reachable volumes fail across three rounds (19, 20 and 25 Sept; sections 4-5, 8, Round 3), with no constant offset, so the title-by-title cloud test is retired for these editions (rule 3, third-attempt clause). Holding libraries: Toronto (Scott 1786, Fulton and Knight 1802), Harvard (Scott 1797), Dublin (Scott 1799). ASKS row 3 lapsed at the 23 Sept sale; ASKS row 101 now carries the request (done 2 Oct 2026)
- Dictionary candidates found by format rather than by title (about 24 entries per body column, about 430-450 pp, 18mo-32mo, 1780-1812) - blocker: not-attempted; DICTIONARY.md section 1 observation 3, section 6 "Miniature formats", and the Round 3 closing line all name it as never done. Section 8 adds that HathiTrust's own full-text search was never run (cloud Cloudflare block). This is a different instrument from the retired title search; next: search catalogues by format and page count (Jisc Library Hub Discover, Open Library, Google Books records) and queue one LOCAL-QUEUE.tsv row for a full-view-only HathiTrust full-text search of 1770-1812 English dictionaries. Test any digitised hit not already in DICTIONARY.md with tools/gbooks_search_within.py, tools/ia_djvu_headwords.py or tools/htrc_ef_headwords.py, ~$4
- Sibling letters and papers in the same Secretary of State's code or strip alphabet: Bentinck papers (Nottingham, Pw Jd); TNA WO 37 at piece level, including Scovell's "Conradus notebook", which Urban cites as the source of the 134A18 example; WO 1 / WO 6 for the cipher "now on its passage from England"; Pellew papers, for the alphabet Donkin reported "not correct"; Wellington Papers, Southampton; Maitland's Alicante in-letters - blocker: not-attempted; NOTES "Sources" lists Scovell/Bentinck/Alicante as "Not checked", NOTES "Next step" item 4 names them, DICTIONARY.md section 2 read only the WO 37 series description, and the Pellew and Conradus leads come from sources/spink/lot-1184-description-2026-09-19.txt and the Urban snippets of 2 Oct 2026. These could yield more groups, the strip "instruction", or the dictionary itself; next: catalogue-only search of the TNA Discovery API (WO 37, WO 1, WO 6, "Conradus", cipher/cypher 1812), the Nottingham Manuscripts catalogue (Pw Jd, 1812) and the Southampton and NMM catalogues (Pellew), logging shelfmarks and digitisation flags, ~$3
- Strip cipher null rule and arrangement indicator (4 runs of 17, 21, 18 and 7 letters, more than half of them nulls) - blocker: not-attempted; NOTES "Next step" item 3 was never run (grep of NOTES, DICTIONARY.md, ROOM.md and LEDGER.md finds no attempt, and there is no HYPOTHESES.md). Tomokiyo (sources/cryptiana/web/maitland.htm line 51) says both indicators "remain to be discovered", and Keys 1-3 are his (NOTES "Readings", S row); next: re-derive Keys 1-3 from the strip letters (NOTES "Strip cipher", maitland2.png) and the 4 runs, mark the nulls, and test candidate rules (alternation, letters outside the active strip pair, a leading indicator) against a synthetic control of the same run lengths and design, reporting both numbers. At 63 letters this may end as too-short, ~$4
- Two letters in the r8 runs (run 1 letter 17, z or y; run 2 letter 13, g or q) - blocker: illegible; foot of ciphertext.txt: two passes plus an 8x reconciliation left both open, and Spink serves nothing larger than 1100x248 px (NOTES "Failure log", images/README.md). Image 06 still serves at the same 137250 bytes (HTTP 200, checked 2 Oct 2026), so no better copy has appeared; next: regrade both from the re-derived strip key during the strip step (Key 3 needs z, Key 1 needs q), ~$0
- Lot 1184 contents never photographed (the box file; the 6 Aug and Cuellar 2 Aug despatches; the corrected alphabet that the 2 Sept letter encloses; any strip "instruction" or pocket dictionary) - blocker: needs-physical-access; the lot sold at Spink on 23 Sept 2026 to a private buyer, ASKS row 3 lapsed unsent, and Spink's description (sources/spink/) names cipher only in the 2 Sept letter and the July strips. Any post-sale question to Spink is the owner's to send

## Escalation (1 Oct 2026)
- [ ] siblings: done so far: lot images 08-15 (Madrid 16/24/29 Aug) viewed, all clear text (images/README.md), and DECODE has no record (check-solved pass 4). Never done: an archive catalogue search for sibling letters and papers (Bentinck Pw Jd, WO 37 at piece level including Scovell's Conradus notebook, WO 1/WO 6, the Pellew papers, Southampton). Planned at ~$3
- [x] clear-pages: the clerk's interlinear decipherment and Gurwood vol. 9 (1834 pp. 388-389, 1838 pp. 392-393, two IA copies) together are the decipherment, with 81 of 81 reading words matching in order (check.py). The strip "instruction" is not among the lot photographs (listed under siblings/lot)
- [x] known-keys: about 80 dictionary candidates tested against codebook.tsv (57 on 19 Sept, 19 HathiTrust EF on 20 Sept, 4 in Round 3 on 25 Sept). All fail, with 3 near misses and no constant offset (DICTIONARY.md). The title-based cloud test is retired after these three rounds and needs a library copy or a format-found candidate. Tomokiyo's strip Keys 1-3 adopted. KEY-OFFICES.tsv and KEY-DESIGN.tsv hold no Wellington, Scovell or War Office key, and KEY-CROSSMATCH.tsv has no usable match
- [x] print: Gurwood vol. 9 (both printings), Supplementary Despatches vol. 7 (12 "cypher" hits, no dictionary), Oman vol. 6, Tomokiyo, and the Spink/Hayes/Lasry description. Urban, The Man Who Broke Napoleon's Codes, was searched 2 Oct 2026 through IA be-api full-text snippets (manwhobrokenapol0000urba_n2j5, 19 requests). The snippets give the p. 232 passage: both headquarters "had copies of the same edition of pocket dictionary", and "134 was the page number; A is the column; 18 is the number of words or letters from the top", sourced to Scovell's "Conradus notebook". "Entick", "Perry", "Walker", "Johnson's", "Pellew" and "Maitland" return 0 hits, so the book names no edition (a search result on its OCR, not a reading of the printed page)
- [ ] key-rebuild: on the code side there is nothing to extend without the book, since every group already reads at H and C. On the strip side, the null and arrangement rule was never searched (NOTES "Next step" item 3). Planned: re-derive Keys 1-3 and test candidate rules against a matched synthetic control, ~$4
- [x] image-check: images 06-07 read in two independent passes (2x-4x) and reconciled at up to 8x, settling 27 disagreements, none on a page number. 2 letters stay doubtful. Image 06 re-fetched 2 Oct 2026 at HTTP 200 and the same size, so no larger image exists (NOTES "Failure log")
- [ ] retry: once the strip keys are re-derived, rerun the 4 runs, regrade the 2 doubtful letters, and move the two runs read with Tomokiyo's keys onto our own derivation
Verdict: keep going: 3 internal gaps; cheapest next: the format-based catalogue search of gap 2 (Open Library and Google Books records by page count and format, 1780-1812; Library Hub Discover from the owner's browser only, it served a Cloudflare challenge to the cloud on 2 Oct 2026; plus one LOCAL-QUEUE.tsv row for a full-view HathiTrust full-text search), ~$4

## Web and blog check (GAPS-wellington-maitland-1812, 2 Oct 2026)

The intake gate's required open-web and blog comment-thread step (`.claude/briefs/check-solved.md`, CHECK-SOLVED-WEB,
28 Sept 2026), run 2 Oct 2026 01:58-02:10 UTC before the Verdict step below. Rule 10 wording throughout: a search
result, never a novelty verdict.

Plain web searches (5):
1. `Wellington Maitland "2 September 1812" cipher` -- ship and biography pages (HMS Wellesley, Thomas and Charles
   Maitland), Oman vol. 5 on Gutenberg, a brewminate.com spies overview: nothing on this despatch.
2. `Spink "lot 1184" Wellington Maitland cypher dictionary code` -- the Spink sale 26066 listing page (opened below),
   Wikipedia "Book cipher" (Scovell's page/column/entry scheme, no edition named): nothing new.
3. `"Villa Castin" Maitland cypher Wellington Alicante strips` -- Battle of Castalla, villa rentals: nothing.
4. `"Wellington's Polyalphabetic Cipher with a Dictionary Code"` (the folder's descriptive title, Tomokiyo's) --
   generic polyalphabetic-cipher pages only; Tomokiyo's own page not returned by this engine.
5. Model-solve announcements, `Wellington Maitland 1812 dictionary code cipher solved Claude OR GPT OR Gemini` --
   Cyphral Distich (1653) and WWI/Enigma announcements only, none about this item.

Blog site searches (3 by the engine, 3 on the blogs' own search boxes):
- Cipherbrain: `site:scienceblogs.de/klausis-krypto-kolumne Wellington Maitland 1812 Scovell dictionary` -- ten
  unrelated posts (incl. "A dictionary code challenge", 29 Oct 2018, opened: a 10,000-word list challenge, 12
  comments, no Wellington/Maitland/Scovell). The blog's own search `?s=Scovell` -- 4 hits: "A coded dispatch from
  1812 and its exciting story" (22 June 2021, German and English versions, opened: Clarke to Caffarelli, 19 Oct 1812,
  French Grand Chiffre; 14 comments on the German page, Norbert and Karsten Hansky recommend Urban's book on
  Scovell, no comment names a dictionary edition or a British 1812 code) and two pigpen posts.
- Cryptiana blog: `site:cryptiana.blogspot.com Wellington Maitland` -- the engine returned no blogspot pages; the
  blog's own search `search?q=Maitland` -- one post, "Wellington's Code/Cipher during the Peninsular War"
  (8 Sept 2026, 1 comment). Opened live: the single comment is Tomokiyo's own (9 Sept 2026, 21:33), the Hayes/Lasry
  credit already quoted in the 20 Sept sweep; no dictionary edition named, no claim that the nulls or the strip
  permutation are found. Tomokiyo's article page (cryptiana.web.fc2.com/code/maitland.htm) opened live: first
  posted 8 Sept 2026, last modified 19 Sept 2026, no section added since, still "The indication of these nulls as
  well as the indication of the permutation of the five strips remain to be discovered." On-disk snapshot
  `sources/cryptiana/` grepped first (0 requests): only maitland.htm and the blog index mention Maitland.
- Cipher Mysteries: `site:ciphermysteries.com Wellington Maitland 1812 Scovell dictionary cipher` -- Beale, De
  Lancey and BL posts, none on this item; the site's own search `?s=Scovell` -- one post, "The Lady Magdalene De
  Lancey ciphers" (9 Nov 2011, opened: 18 comments, Scovell named once as Napoleon's codebreaker, no Maitland,
  no dictionary code, no strips).

Other hits opened: Spink sale 26066 listing (www.spink.com/auction/26066?page=10): lot 1184 shows **SOLD, GBP
42,000** (hammer, read 2 Oct 2026); the listing text names no cipher, dictionary or code. Aymeloglu's live README
(raw.githubusercontent.com): no Wellington/Maitland/Scovell/Peninsular line (the SHORTLIST.md pointer of 19 Sept
stands as recorded).

Result: no decipherment or plaintext of this item located by these queries on 2 Oct 2026 beyond the
Hayes/Lasry/Tomokiyo partial work already recorded above (Gurwood's printed clear text and the clerk's
interlinear reading are the plaintext, already on file at grade C and H). Status word unchanged: partial. Requests:
scienceblogs.de 4, cryptiana.blogspot.com 2, cryptiana.web.fc2.com 1, ciphermysteries.com 2, spink.com 1,
raw.githubusercontent.com 1, plus 8 web-search calls; no 403/429/challenge.

## Premise check (GF4-BATCH6, 3 Oct 2026)

Worker GF4-BATCH6 (account-4), 01:46-01:5x UTC 3 Oct 2026 by the clock. The adversarial pass of `.claude/briefs/check-solved.md`
"## Premise check". No cryptanalysis, no transcription, no vision call.

- **(a) Decipherments the folder already mentions -- FOUND (this very item).** (1) The clerk's interlinear decipherment on the
  despatch (images 06-07): every one of the 73 code-group occurrences and the two "Alicant" strip runs carry a contemporary
  reading (grade H in "Readings, graded per token"). (2) Gurwood vol. 9, both printings (`sources/gurwood/`, IA
  dispatchesoffie09welluoft and vol9dispatchesof00well): the whole letter in clear, 81 of 81 reading words in manuscript order
  (`check.py`); an IA full-text query today ("Villa Castin" Maitland cipher, be-api, 1 request, 101 hits) returns the Gurwood
  volumes first, nothing else printing this despatch. (3) Tomokiyo's maitland.htm, re-fetched live today (1 request):
  byte-identical to the snapshot `sources/cryptiana/web/maitland.htm` (13,510 bytes, "modified on 19 September 2026"): his
  table of 56 code groups with readings, Keys 1-3 of the strip cipher (Key 1 credited to Hayes and Lasry), and the readings
  Arevalo and "Vila Castin" for the two runs with no interlinear. The Cryptiana blog's own search for "Wellington" today (1
  request): the 8 Sept 2026 post only, no later post on this item. So the plaintext of every cipher token of this item is
  published, and a period decipherment sits on the document; what no source gives is the dictionary edition and the strip null /
  permutation rule (key recovery, not reading).
- **(b) Other solvers' working files -- not found.** Fresh shallow clones 3 Oct 2026 (dbourdeau/cyphersolver a4292cb;
  aaymeloglu/unsolved-ciphers d2800bb), `grep -ril` maitland / wellington / scovell: Bourdeau has no folder for this item (hits
  are Napoleon 1812 sources, the Urquhart "Maitland Club" edition, CSP Maitlands of the 1560s); Aymeloglu's SHORTLIST.md still
  has only the pointer "Wellington's Peninsular War code (Sept 8 2026 post, worth a look)", no working file.
- **(c) Physical neighbours -- not found beyond what is on file.** All 19 Spink lot photographs are on disk and identified
  (`images/README.md`): 08-15 the Madrid 16/24/29 Aug 1812 despatches (clear text), 03-04 the ten strips and the wrapper "a Cypher
  recd from Lord Wellington July 1812", 05 the group shot; no separate decipherment slip, no strip instruction, no corrected
  alphabet photographed. The despatch's own verso (07) is the continuation and signature; the interlinear is on the cipher lines
  themselves. Spink serves nothing above 1100 px, so "native resolution" here is 1100x248 (Failure log). The lot sold (GBP 42,000,
  2 Oct read), so the unphotographed contents need the buyer (blocker needs-physical-access, Remaining gaps).
- **(d) Recipient's side -- not found in print.** The recipient copy is this document (Maitland's papers, the lot itself), which
  carries the decipherment. No printed edition of Maitland's or Bentinck's in-letters for Aug-Sept 1812 is known to the folder
  (Bentinck papers, Nottingham Pw Jd, unprinted); Supplementary Despatches vol. 7 (sender side) was searched on 20 Sept (12
  "cypher" hits, no dictionary). Not searched today: TNA WO 37 / WO 1 piece descriptions (already listed as a siblings gap).

**Verdict:** (a) found -- a contemporary decipherment on the item plus the printed clear text (Gurwood) plus Tomokiyo's published
reading of the strip runs: the plaintext of this very item is known, as the folder has recorded since 19-20 Sept. Per this job's
brief the status word is set to `found-solved` with the sources on line 2. Flagged to the account-4 parent: the open work here
is key recovery (the dictionary edition, ASKS row 101; the strip null rule), which `found-solved` does not close; "Remaining gaps"
and "Escalation" above stay as the record. Rule 10: nothing here is new, first or unpublished.

Requests this job (this target): cryptiana.web.fc2.com 1, cryptiana.blogspot.com 1, be-api.us.archive.org 1, WebSearch 1;
github.com clones shared with the batch. No credentials.

```
$ python3 tools/intake_gate_check.py wellington-maitland-1812   # before: exit 1, no Premise check section
wellington-maitland-1812: found-solved (line 1) -- edition/page or full-text-search citation found within 6 lines
exit=0
```
