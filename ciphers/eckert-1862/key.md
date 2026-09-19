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

| code word | meaning | grade | evidence |
|---|---|---|---|
| Alden | Halleck | C | OR 7 p.584, 591, 624, 628; ledger addressee "St Louis" |
| Alvord | Buell | C | OR 7 p.593, 609, 626, 646 |
| Andes | McClellan | C | ledger p.[9] deletion; OR 7 passim |
| Anthon | Banks | I | ledger p.[11]: plain telegram to Banks at Frederick repeats the coded one to "Anthon" |
| Arno | Rosecrans | M | received ledger mssEC 01 p.14: Wheeling telegram signed "Arthur"; sent ledger uses "Arno" |
| Bagdad | Cullum | I | ledger p.[49] coded and p.[51] plain versions of the same order |
| Bremen | Grant | C | OR 7 p.591, 624 |
| Camden | Thomas | C | OR 7 p.624, 646 |
| Carroll | Hunter | C | OR 8 p.551 |
| Chester | Curtis | C | OR 7 p.646 (McClellan to Halleck 21 Feb 1862, "push Curtis beyond Bentonville") |
| Cuba | (an officer, cavalry) | M | ledger p.[17], [20] |
| Devon | Norfolk | M | ledger p.[55], Fort Monroe line; on p.[10] the same word stands with "Indianapolis" (Gov. Morton?), so two keys were in use |
| Humboldt | Lander | M | ledger p.[28], [29] "Humboldt was seriously ill" (Lander died 2 Mar 1862); but on p.[57] "Humboldt" is the plain Tennessee town (OR 7 p.646), so the eastern-line entries use a different meaning set |
| Ingress | Thomas A. Scott, Asst. Sec. of War | C | OR 7 p.628 |
| Irving | Lincoln | C | OR 8 p.551, OR 7 p.624 |
| Jolly | (relay office, Cincinnati?) | M | ledger p.[14] |
| Koran | Ohio | C | OR 7 p.584, 593 |
| Lamb | Kansas | I | ledger p.[24], [26] (Lane's Kansas expedition) |
| Lark | Indiana | C | OR 7 p.593 |
| Lather | Michigan | C | OR 7 p.593 |
| Legend | Kentucky | C | OR 7 p.628 |
| Lonesome | Tennessee | C | OR 7 p.591, 626 |
| Magnet | Arkansas | C | OR 7 p.646 |
| Mary | Tennessee River | I | ledger p.[13] "expedition up the Mary ... Fort Henry" |
| Merlin | Virginia | C | OR 7 p.584 ("Western Virginia") |
| Mystic | Green River | C | OR 7 p.626 |
| Myrtle | Cumberland River | C | OR 7 p.646 |
| Negus | Potomac | I | ledger p.[31] "reserve whack of the youth of the negus" |
| Ocean | Washington | I | received ledger mssEC 01 p.8, 13 address line "Andes Ocean"; Plum via Tomokiyo |
| Opal | Winchester | M | ledger p.[7], [45] |
| Palate | Cairo | I | ledger p.[48], [49] |
| Pastor | St Louis | C | OR 7 p.628 (Scott "Saint Louis") |
| Quotient | Leavenworth | C | OR 8 p.551 |
| Rapture | Louisville | C | OR 7 p.584 (Buell "Louisville"); Plum via Tomokiyo |
| Saffron | Columbus | C | OR 7 p.591, 593, 646 |
| Sermon | Bowling Green | C | OR 7 p.584, 624, 626 |
| Shylock | Nashville | C | OR 7 p.591, 593, 624, 626, 646 |
| Torrent | Memphis | C | OR 7 p.591, 593, 646 |
| Twinkle | Romney | I | ledger p.[11]: plain telegram to Banks "Lander moving on Romney" repeats coded "Lander is moving on Twinkle" |
| Vesper | Cumberland (Md.) | M | ledger p.[5], [6] (Lander's base) |
| Virtue | Frederick | I | ledger p.[6], [14] (Banks's headquarters) |
| Vomit | Paw Paw | M | ledger p.[28] |
| wag | batteries | C | OR 7 p.608 |
| wayworn | army | I | ledger p.[17], [26], [42] |
| whack | artillery | I | ledger p.[12], [31] |
| whale | cavalry | C | OR 7 p.608 |
| wharf | infantry | C | OR 7 p.608 |
| whig | advance | C | OR 7 p.626, 646 |
| wean | threaten | C | OR 7 p.646 ("seriously threaten Memphis") |
| whist | regiment(s) | I | ledger p.[5], [8], [40] |
| whistle | the enemy | I | ledger p.[5], [7], [33], [34] |
| widow | (troops sent, reinforcements?) | M | ledger p.[26], [27] |
| wreathe | gunboat(s) | C | OR 7 p.624, 646 |
| yankee | (stores? transportation?) | M | ledger p.[7], [45] |
| youth | arms | I | ledger p.[5], [6], [40] |
| Eugenia | 8 PM (time word) | I | ledger: 7 Feb 7.15 PM, 15 Feb 8 PM twice |
| Florence | 7 PM (time word) | I | ledger: 6 Feb 7 PM twice, 13 Feb 7 PM |
| Francis | 11 PM (time word) | I | ledger: 14 Feb 11 PM twice, 15 Feb 11 PM |
| Nancy | 6 PM (time word) | I | ledger: 9 Feb 5.30 PM, 12 Feb 6 PM |
| Sarah | 2 PM (time word) | I | ledger: 11 Feb 2 PM, 14 Feb 2 PM twice |
| Dorothy | (time word, morning) | M | ledger: 6, 16, 17 Feb, no hour given |
| Hannah | (time word) | M | ledger: 21 Feb, OR gives 9.30 PM for the Buell telegram |
| Martha | (time word, about 10 PM) | M | ledger: 15 Feb between the 8 PM and 11 PM entries |

Not code: "finis", "etc", "signed", and the chatty tails ("whats news", "cold day", "Im for the union",
"hurry") are the operator's check or filler words; decode.py drops them from the reading.
