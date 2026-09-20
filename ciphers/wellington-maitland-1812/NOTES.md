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
