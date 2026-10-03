# Key: the cipher behind the 1862 "Ciphers Sent" ledger (mssEC 15)

Written 19 Sept 2026. Sources are named per item. Grades follow CLAUDE.md rule 4: H = read from a key source,
C = known plaintext (the Official Records print of the same telegram), I = carried over from a meaning fixed by
known plaintext in another entry of the same ledger, M = uncertain.

## 1. What the ledger records

mssEC 15 (Huntington Digital Library object 5126, 172 page images) is the War Department telegraph office's
outgoing book for 1 Feb to 21 July 1862. Every entry is written the way the operator received it from the
sender, before route transposition: the address, the text with names and sensitive words already replaced by
"arbitrary" code words, the signature (itself a code word), a time-of-day code word, and one or more filler
words ("cold day", "Im for the union", "whats news"). The route transposition was applied on the wire and is
not recorded. So the entries are dictionary-coded plaintext, not transposed ciphertext, and reading them means
resolving the arbitraries. Several entries carry a deleted plain signature replaced by the code word (page [9],
5 Feb 1862: "G B McClellan Maj Genl" struck out, "Andes" written in), which fixes Andes = McClellan (H, from
the ledger itself).

## 2. The printed template (H: mssEC 67, mssEC 41, images in images/)

The arbitraries used in Feb 1862 are the printed words of Anson Stager's booklet "Cipher for Telegraphic
Correspondence; arranged expressly for Military Operations, and for important Government despatches ...
1861 & '62", the template Tomokiyo identifies for Ciphers No. 9, 10, 12, 1 and 2 (civilwar1.htm, snapshot in
sources/cryptiana/web/). The Huntington copy mssEC 67 (object 1750; Tomokiyo: Cipher No. 9) shows the structure:

- Title page verso (page 1718): the printed directions. "Write a given number of words in each line; space
  regularly so as to form columns. The message will then be prepared for transmission by copying up and down
  the columns in the order of the 'Route' named in connection with the 'Commencement word' used. At the end of
  each column an 'extra' or 'check' word will be added ... The 'Commencement Word' indicates the number of lines
  in the message, or division of a message ... there are three combinations of cipher on each of the first
  eight pages, and three commencement words for each combination." Facing it, the list of holders of this copy
  (War Dept Washington; Col. A. Stager, Cleveland; Capt. S. Bruch, Louisville; G. H. Smith, St Louis; Chas.
  Bulkley, New Orleans; J. C. Van Duzer, Nashville; W. L. Gross, Danville Ky; W. G. Fuller, Memphis;
  S. H. Beckwith, Grant's HQ; Jno. F. Wilber, Knoxville; C. F. Gross, Danville Ky).
- Page [A]: TIME, 48 women's names for every hour and half hour, meanings handwritten (mssEC 41 page 315 shows
  the same list filled in: Ann 1 AM, Agnes 1.30, Anna 2, Amelia 2.30, Alice 3, Betsy 3.30, Barney 4,
  Barbara 4.30, Cora 5, Clara 5.30, Catharine 6, Cornelia 6.30, Clotilda 7, Delia 7.30, Deborah 8,
  Dorothy 8.30, Emma 9, Eugenia 9.30, Emily 10, Elizabeth 10.30, Fanny 11, Florence 11.30, Francis 12 noon,
  Gertrude 12.30; PM: Harriet 1, Hannah 1.30, Helen 2, Henrietta 2.30, Imogene 3, Jennie 3.30, Julia 4,
  Katy 4.30, Lucy 5, Laura 5.30, Libby 6, Mary 6.30, Martha 7, Minnie 7.30, Nancy 8, Nelly 8.30, Rosalie 9,
  Rosetta 9.30, Rebecca 10, Reliance 10.30, Sarah 11, Suzan 11.30, Topsy 12 midnight, Viola 12.30). The
  hours in mssEC 41 are the 1864 assignment; the 1862 ledger uses the same names with different hours (section 4).
- Pages 1-8, one per message length of 3 to 10 lines (page 1721 = 3 lines): three printed groups of three
  commencement words, the number of columns for each group written in ("Army / Anson / Action" = 5 columns,
  "Astor / Advance / Artillery" = 6, "Anderson / Ambush / Agree" = 4), the printed six-column route filled in
  ("Up the 4 column, down the 3, up the 2, down the 1, up the 5, down the 6") and the four- and five-column
  routes written below ("Down first, down fourth, down second, up third"; "Up second, up third, up fourth,
  down first, down fifth").
- Pages [9]-[24], arbitraries: 26 printed lines per page, a printed word at each end of the line and the meaning
  written between, so every meaning has two code words. Sections in mssEC 67: cabinet and staff (Adam/Asia =
  President; Anthon/America = Sec. of the Navy; Andes/Anchor = Jno. G. Tucker; Arno/Ague = Meade), Maj. Generals
  (Asp/Axis = McClellan, Applause/Abortion = Halleck, Bremen/Brussels = McDowell, Bangor/Bengal = Grant,
  Bagdad/Bethel = Buell, Baltic/Berlin = Hunter ...), Commodores, Brig. Generals, Governors (Dirge/Discount = Tod,
  Ohio; Docket/Dodge = Morton, Ind.; Eagle/Essex = Magoffin, Ky), Rebel Generals (Polk/Pontiac = Buckner,
  Queenly/Quotient = Joe Johnston), States, Places (Irving/Ingress = Augusta, Jolly/Journal = Little Rock,
  Knell/Knight = Elizabeth City), ranks (Venus/Vesper = Colonel, Virtue/Vulcan = Captain, Vulture/Vomit =
  Lieutenant) and a miscellaneous vocabulary (Whist/Whistle = wounded, Wherry/Whig = skirmish, Yankee/Yardstick =
  reinforcements, Youth/Yoke = troops, Zodiac/Zebra = movement).

Every arbitrary in the 1862 ledger that was checked is a printed word of this template: Alden, Alvord, Andes,
Anthon, Arno, Bremen, Bagdad, Carroll, Camden, Devon, Ingress, Irving, Jolly, Knight, Koran, Lark, Legend,
Lonesome, Luna, Magnet, Merlin, Myrtle, Negus, Nugget, Quotient, Torrent, Twinkle, Vesper, Virtue, Vomit,
Wag, Wayworn, Wean, Whack, Wharf, Whig, Whist, Whistle, Widow, Wreathe, Yankee, Youth (H: pages 1729, 1730,
1733, 1736, 1739, 1742, 1744 of mssEC 67). The meanings differ from every filled-in copy the Huntington has
digitised (mssEC 39-48, 67 are 1864-66 issues; mssEC 37, 40 are post-war handwritten codes; mssEC 38 is a
Department of the Gulf list of about 1863; mssEC 36 is not a cipher book at all but Stager's 1865-67
memorandum of which keys were held where). The Feb 1862 meanings agree with those Plum gives for Cipher
No. 7 (Buell to Halleck, 29 Sept 1862, quoted by Tomokiyo: Alvord = Buell, Camden = Thomas, Rapture =
Louisville, Ocean = Washington), so the ledger is written in the vocabulary of Cipher No. 7, the western
cipher abandoned after Sept 1862, of which no copy is in the digitised collection.

## 3. The 1862 vocabulary as recovered

The meaning column is what the Official Records print for the same telegram (C), or what another ledger entry
with a printed counterpart fixes (I), or an inference from context (M). "OR 7" = War of the Rebellion, series I,
vol. 7 (1882); "OR 8" = vol. 8 (1883); page numbers from the Internet Archive copies (identifiers in NOTES.md).
decode.py reads this table; keep the column order.

Witness dates (GAPS127, 3 Oct 2026): the fourth column is the first and last ledger date of the telegrams that support
the row, computed by `python3 print/key_dates.py --write` (method in its docstring; `--check` exits 1 when stale) from
the ten entries, the ledger pages and pointers cited, the OR 7 page matches and the OR 11-12 alignments. A word may have
more than one row: the spring-summer 1862 eastern-line tables reuse Feb words for other values. decode.py reads a word
by the row whose range covers the entry's ledger date; outside every range, or where two values cover the date, the
token is graded M (rule 4). `python3 decode.py --at "18 Jun" WORD...` prints the value and grade for a date. The rows
at the end of the table marked "dated split" are the later values of a Feb word; "true conflict" rows overlap a rival
value in date and stay M.

| code word | meaning | grade | witness dates | evidence |
|---|---|---|---|---|
| Alden | Halleck | C | 05 Feb-10 Mar 1862 | OR 7 p.584, 591, 624, 628; ledger addressee "St Louis" |
| Alvord | Buell | C | 05 Feb-02 Mar 1862 | OR 7 p.593, 609, 626, 646 |
| Andes | McClellan | C | 01 Feb-04 Jul 1862 | ledger p.[9] deletion; OR 7 passim |
| Anthon | Banks | I | 06 Feb 1862 | ledger p.[11]: plain telegram to Banks at Frederick repeats the coded one to "Anthon" |
| Arno | Rosecrans | M | undated | received ledger mssEC 01 p.14: Wheeling telegram signed "Arthur"; sent ledger uses "Arno" |
| Bagdad | Cullum | I | 20 Feb 1862 | ledger p.[49] coded and p.[51] plain versions of the same order |
| Bremen | Grant | C | 07 Feb-16 Feb 1862 | OR 7 p.591, 624 |
| Camden | Thomas | C | 16 Feb-21 Feb 1862 | OR 7 p.624, 646 |
| Carroll | Hunter | C | 10 Feb 1862 | OR 8 p.551 |
| Chester | Curtis | C | 21 Feb 1862 | OR 7 p.646 (McClellan to Halleck 21 Feb 1862, "push Curtis beyond Bentonville") |
| Cuba | (an officer, cavalry) | M | 07 Feb-10 Feb 1862 | ledger p.[17], [20] |
| Devon | Norfolk | M | 21 Feb 1862 | ledger p.[55], Fort Monroe line; on p.[10] the same word stands with "Indianapolis" (Gov. Morton?), so two keys were in use |
| Humboldt | Lander | M | 13 Feb-03 Mar 1862 | ledger p.[28], [29] "Humboldt was seriously ill" (Lander died 2 Mar 1862); but on p.[57] "Humboldt" is the plain Tennessee town (OR 7 p.646), so the eastern-line entries use a different meaning set |
| Ingress | Thomas A. Scott, Asst. Sec. of War | C | 17 Feb 1862 | OR 7 p.628 |
| Irving | Lincoln | C | 10 Feb-11 Jul 1862 | OR 8 p.551, OR 7 p.624 |
| Jolly | (relay office, Cincinnati?) | M | 06 Feb-07 Feb 1862 | ledger p.[14] |
| Koran | Ohio | C | 05 Feb-07 Feb 1862 | OR 7 p.584, 593 |
| Lamb | Kansas | I | 10 Feb-13 Feb 1862 | ledger p.[24], [26] (Lane's Kansas expedition) |
| Lark | Indiana | C | 07 Feb 1862 | OR 7 p.593 |
| Lather | Michigan | C | 07 Feb 1862 | OR 7 p.593 |
| Legend | Kentucky | C | 07 Feb-08 Jun 1862 | OR 7 p.628 |
| Lonesome | Tennessee | C | 07 Feb-08 Jun 1862 | OR 7 p.591, 626 |
| Magnet | Arkansas | C | 21 Feb 1862 | OR 7 p.646 |
| Mary | Tennessee River | I | 06 Feb 1862 | ledger p.[13] "expedition up the Mary ... Fort Henry" |
| Merlin | Virginia | C | 05 Feb-17 Jun 1862 | OR 7 p.584 ("Western Virginia") |
| Mystic | Green River | C | 16 Feb 1862 | OR 7 p.626 |
| Myrtle | Cumberland River | C | 21 Feb 1862 | OR 7 p.646 |
| Negus | Potomac | I | 15 Feb-03 Mar 1862 | ledger p.[31] "reserve whack of the youth of the negus" |
| Ocean | Washington | I | 11 Jul 1862 | received ledger mssEC 01 p.8, 13 address line "Andes Ocean"; Plum via Tomokiyo |
| Opal | Winchester | M | 01 Feb-30 May 1862 | ledger p.[7], [45] |
| Palate | Cairo | I | 20 Feb 1862 | ledger p.[48], [49] |
| Pastor | St Louis | C | 17 Feb 1862 | OR 7 p.628 (Scott "Saint Louis") |
| Quotient | Leavenworth | C | 10 Feb 1862 | OR 8 p.551 |
| Rapture | Louisville | C | 05 Feb 1862 | OR 7 p.584 (Buell "Louisville"); Plum via Tomokiyo |
| Saffron | Columbus | C | 07 Feb-21 Feb 1862 | OR 7 p.591, 593, 646 |
| Sermon | Bowling Green | C | 05 Feb-21 Feb 1862 | OR 7 p.584, 624, 626 |
| Shylock | Nashville | C | 07 Feb-21 Feb 1862 | OR 7 p.591, 593, 624, 626, 646 |
| Torrent | Memphis | C | 07 Feb-21 Feb 1862 | OR 7 p.591, 593, 646 |
| Twinkle | Romney | I | 01 Feb-03 Mar 1862 | ledger p.[11]: plain telegram to Banks "Lander moving on Romney" repeats coded "Lander is moving on Twinkle" |
| Vesper | Cumberland (Md.) | M | 01 Feb-05 Feb 1862 | ledger p.[5], [6] (Lander's base) |
| Virtue | Frederick | I | 01 Feb-07 Feb 1862 | ledger p.[6], [14] (Banks's headquarters) |
| Vomit | Paw Paw | M | 13 Feb-15 Feb 1862 | ledger p.[28] |
| wag | batteries | C | 06 Feb-13 Feb 1862 | OR 7 p.608 |
| wayworn | army | I | 07 Feb-03 Jul 1862 | ledger p.[17], [26], [42] |
| whack | artillery | I | 06 Feb-15 Feb 1862 | ledger p.[12], [31] |
| whale | cavalry | C | 13 Feb-27 Mar 1862 | OR 7 p.608 |
| wharf | infantry | C | 13 Feb-27 Mar 1862 | OR 7 p.608 |
| whig | advance | C | 01 Feb-21 Feb 1862 | OR 7 p.626, 646 |
| wean | threaten | C | 21 Feb 1862 | OR 7 p.646 ("seriously threaten Memphis") |
| whist | regiment(s) | I | 01 Feb-27 Mar 1862 | ledger p.[5], [8], [40] |
| whistle | the enemy | I | 01 Feb-16 Jun 1862 | ledger p.[5], [7], [33], [34] |
| widow | reinforcements | C | 13 Feb-03 Jul 1862 | OR 11 pt3 p.286, OR 12 pt1 p.659 (ledger 5095, 5079, June 1862; GAPS122); was M "(troops sent, reinforcements?)" from ledger p.[26], [27] (Feb), which the print agrees with |
| wreathe | gunboat(s) | C | 16 Feb-21 Feb 1862 | OR 7 p.624, 646 |
| yankee | transportation | C | 01 Feb-20 Mar 1862 | ledger p.[7], [45]; OR 51 pt1 (ledger 5000, 19 Feb, "minimum amount of additional transportation") and OR 11 pt3 p.25 (ledger 5053, 20 Mar), two telegrams, GAPS153 pooled held-out; was M "(stores? transportation?)" |
| youth | arms | I | 01 Feb-02 Mar 1862 | ledger p.[5], [6], [40] |
| Arctic | Fremont | C | 25 May-16 Jun 1862 | OR 11 pt3 p.202, 205 (ledger 5069-5070, 31 May-1 June 1862; GAPS118 alignment, print/or_align.py) |
| Genoa | Washington | C | 25 May-28 Jun 1862 | OR 11 pt3 p.217, 269 (ledger 5073-5074, 5092, June 1862; GAPS118); Feb entries use Ocean |
| humming | Richmond | C | 02 May-28 Jun 1862 | OR 11 pt3 p.173, 217, 232, 234, 269 (ledger 5060-5092, May-June 1862; GAPS118) |
| Indus | Fredericksburg | C | 25 May-17 Jul 1862 | OR 11 pt3 p.217, 232, 325 (ledger 5073-5074, 5085, 5110, June-July 1862; GAPS118); on 5049 (13 Mar) "signed Indus" is a signature, so an earlier meaning differs |
| Jasper | Winchester | C | 25 May-01 Jun 1862 | OR 11 pt3 p.202, 205 (ledger 5069-5070, May-June 1862; GAPS118); Feb entries use Opal (M) |
| Juno | Gordonsville | C | 18 Jun-21 Jul 1862 | OR 11 pt3 p.232, 234, 327 (ledger 5085, 5086, 5111, June-July 1862; GAPS118) |
| panther | advance | C | 29 May-20 Jul 1862 | OR 11 pt3 p.205, 221 (ledger 5070, 5076, June 1862; GAPS118); Feb entries use whig |
| princess | artillery | C | 06 Jun-21 Jul 1862 | OR 11 pt3 p.217, 260 (ledger 5073-5074, 5090, June 1862; GAPS118); Feb entries use whack (I) |
| rampant | (the) enemy | C | 06 Apr-21 Jul 1862 | OR 11 pt3 p.117, 205, 269, 278, 325 (ledger 5058-5110, Apr-July 1862; GAPS118); Feb entries use whistle (I) |
| rampants | (the) enemy | C | 06 Apr-21 Jul 1862 | OR 11 pt3 p.199, 202, 205, 269 (ledger 5064-5092, May-June 1862; GAPS118) |
| robin | division | C | 08 Jun-17 Jul 1862 | OR 11 pt3 p.260, 326 (ledger 5090, 5110, June-July 1862; GAPS118) |
| wedding | transportation | C | 06 Apr-26 Jun 1862 | OR 11 pt3 p.217, 260 (ledger 5073, 5090, June 1862; GAPS118) |
| welsh | reinforcements | C | 18 Jun-30 Jun 1862 | OR 11 pt3 p.232, 234, 258, 269, 270 (ledger 5085-5093, June 1862; GAPS118) |
| Danube | McDowell | C | 02 May-29 May 1862 | OR 12 pt3 p.125, OR 12 pt1 p.533 (ledger 5060, 5064, May-June 1862; GAPS122); Anthon is also McDowell in the same months (GAPS118) |
| Ingot | Lynchburg | C | 17 Jul-21 Jul 1862 | OR 11 pt3 p.326, OR 12 pt3 p.491 (ledger 5110, 5116, July 1862; GAPS122) |
| Jargon | Charlottesville | C | 08 Jun-21 Jul 1862 | OR 11 pt3 p.325-326, OR 12 pt3 p.354, 481, 490-491 (ledger 5075, 5110, 5111, 5116, 5117, June-July 1862; GAPS122) |
| Offal | Richmond | C | 09 Jun-03 Jul 1862 | OR 11 pt3 p.294, OR 12 pt1 p.659 (ledger 5096, 5079, June-July 1862; GAPS122); humming is also Richmond |
| Quack | Sigel | C | 04 Jul-11 Jul 1862 | OR 12 pt3 p.453, 454 (ledger 5099, 5100, June-July 1862; GAPS122) |
| quadrant | cavalry | C | 14 Jul-21 Jul 1862 | OR 11 pt3 p.326, OR 12 pt3 p.476, 481, 490-491 (ledger 5109, 5110, 5111, 5116-5117, July 1862; GAPS122) |
| tambour | infantry | C | 20 Jul-21 Jul 1862 | OR 12 pt3 p.486, 491 (ledger 5112, 5116, July 1862; GAPS122); Feb entries use wharf |
| wafer | regiment | C | 25 May-21 Jul 1862 | OR 12 pt3 p.481, 490 (ledger 5111, 5116, July 1862; GAPS122); Feb entries use whist (I) |
| Eugenia | 8 PM (time word) | I | 07 Feb-15 Feb 1862 | ledger: 7 Feb 7.15 PM, 15 Feb 8 PM twice |
| Florence | 7 PM (time word) | I | 06 Feb-13 Feb 1862 | ledger: 6 Feb 7 PM twice, 13 Feb 7 PM |
| Francis | 11 PM (time word) | I | 14 Feb-15 Feb 1862 | ledger: 14 Feb 11 PM twice, 15 Feb 11 PM |
| Nancy | 6 PM (time word) | I | 09 Feb-12 Feb 1862 | ledger: 9 Feb 5.30 PM, 12 Feb 6 PM |
| Sarah | 2 PM (time word) | I | 11 Feb-14 Feb 1862 | ledger: 11 Feb 2 PM, 14 Feb 2 PM twice |
| Dorothy | (time word, morning) | M | 17 Feb 1862 | ledger: 6, 16, 17 Feb, no hour given |
| Hannah | (time word) | M | 21 Feb 1862 | ledger: 21 Feb, OR gives 9.30 PM for the Buell telegram |
| Martha | (time word, about 10 PM) | M | 15 Feb 1862 | ledger: 15 Feb between the 8 PM and 11 PM entries |
| Anthon | McDowell | C | 06 Apr-17 Jul 1862 | OR 11 pt3 p.117, 202, 326 (ledger 5058, 5069, 5110; GAPS118); the Feb value is Banks (p.[11]); dated split GAPS127 |
| Alden | Banks | C | 25 May-20 Jul 1862 | OR 11 pt3 p.326, OR 12 pt3 p.486-487 (ledger 5110, 5112; GAPS118, GAPS122); the Feb value is Halleck; dated split GAPS127 |
| Arno | Banks | M | 09 Jun-16 Jun 1862 | OR 12 pt1 p.659 (ledger 5079-5080, one telegram, Lincoln to Fremont 12-13 June 1862; GAPS122); dated split GAPS127 |
| Arno | Halleck | C | 03 Jul-20 Jul 1862 | OR 11 pt3 p.291, 294, OR 12 pt3 p.487 (ledger 5096, 5099, 5112; GAPS118, GAPS122); dated split GAPS127 |
| Lather | James River | C | 26 Jun-21 Jul 1862 | OR 11 pt3 p.269, 270, 326, OR 12 pt3 p.476, 491 (ledger 5091, 5093, 5109, 5110, 5116; GAPS118, GAPS122); the Feb value is Michigan; dated split GAPS127 |
| Camden | Banks | C | 02 May-04 Jul 1862 | OR 12 pt3 p.125, 453 (ledger 5060, 5097; GAPS122); the Feb value is Thomas; dated split GAPS127 |
| Virtue | artillery | M | 04 Jul-11 Jul 1862 | OR 12 pt3 p.453-454 (ledger 5099-5100, one telegram; GAPS122); the Feb value is Frederick; dated split GAPS127 |
| Palate | bridges | C | 06 Apr-21 Jul 1862 | OR 11 pt3 p.117, OR 12 pt3 p.491 (ledger 5058, 5116-5117, two telegrams; GAPS118, GAPS122); the Feb value is Cairo; dated split GAPS127 |
| wedding | battle | M | 09 Jun-16 Jun 1862 | OR 12 pt1 p.34, 659 (ledger 5079, one telegram, Lincoln to Fremont 12-13 June 1862; GAPS122); overlaps transportation (McClellan's line, same month): a true conflict, read M |
| Vulcan | headquarters | M | 27 Mar 1862 | OR 12 pt3 p.23 (ledger 5057, one telegram, 27 Mar 1862; GAPS122 held); dated split GAPS127 |
| Vulcan | railroad | M | 21 Jul 1862 | OR 12 pt3 p.490-491 (ledger 5116-5117, one telegram; GAPS122 held); dated split GAPS127 |
| Stanhope | flank | M | 01 Jun-21 Jul 1862 | OR 11 pt3 p.325, OR 12 pt3 p.491 (ledger 5071, 5117; GAPS122 held); overlaps 'the Shenandoah': a true conflict, read M |
| Stanhope | the Shenandoah | M | 04 Jul-11 Jul 1862 | OR 12 pt3 p.454 (ledger 5100, one telegram; GAPS122 held); inside the range of 'flank': a true conflict, read M |
| Japan | Manassas | C | 25 May 1862 | OR 11 pt1 p.31, 32 (ledger 5061, 5063, two telegrams, Lincoln to McClellan 25 May 1862; GAPS147 pooled held-out) |
| Persian | army | C | 21 Jun-28 Jun 1862 | OR 11 pt1 p.48, OR 11 pt3 p.269 (ledger 5089, 5092, two telegrams, 21 and 28 Jun 1862; GAPS147 pooled held-out) |
| tarquin | movements | C | 25 May-26 Jun 1862 | OR 11 pt1 p.32, OR 11 pt3 p.260 (ledger 5063, 5090, two telegrams, 25 May and 26 Jun 1862; plural tarquins 5062; GAPS147 pooled held-out) |
| Pastor | battle | C | 25 May-28 Jun 1862 | OR 11 pt1 p.31, OR 11 pt3 p.269 (ledger 5061, 5092, two telegrams, 25 May and 28 Jun 1862; GAPS147 pooled held-out); the Feb value is St Louis; dated split GAPS147 |
| damon | batteries | C | 13 Feb-10 Mar 1862 | OR 51 pt1 (ledger 4985, 15 Feb, Marcy to Hooker, "upon all the batteries") and OR 5 p.524 (ledger 5044, 9 Mar), two telegrams, GAPS153 pooled held-out |

Not code: "finis", "etc", "signed", and the chatty tails ("whats news", "cold day", "Im for the union",
"hurry") are the operator's check or filler words; decode.py drops them from the reading.
