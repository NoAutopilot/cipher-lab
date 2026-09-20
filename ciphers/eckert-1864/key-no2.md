# Key: Cipher No. 2 (Huntington mssEC 47) as used in the 1864 "Ciphers Sent" ledger mssEC 19 for Grant's and Canby's headquarters

Written 20 Sept 2026. Grades follow CLAUDE.md rule 4: H = read from a key source (here the filled-in cipher book
mssEC 47), C = known plaintext (the Official Records print of the same telegram), I = inferred from another
entry or from the layout, M = uncertain. Every row of sections 3-7 is grade H unless the grade column says
otherwise; the source column gives page, printed line (or row), side and the Huntington page pointer, whose image
is `images/mssEC47_p<pointer>.jpg` (1200 px wide; the transcription was made from 1600 px and 2400 px copies of
the same IIIF images). decode_no2.py reads every `| code word |` table of this file with the machinery of
decode.py; where a printed word occurs in two tables the later row wins, which is why the route pages
(section 4) stand before the arbitraries (section 5).

## 1. What this key is for

NOTES.md section 2 records that the entries of mssEC 19 to S. H. Beckwith (Grant's headquarters, Culpeper and
City Point) and to S. P. Kimber (with Canby, New Orleans and Vicksburg) are not in Cipher No. 1: they use the
same printed words with other meanings, the punctuation set "tulip / pike / yacht / yawl / yard", "For Crowd"
to Grant and "For Mastiff" to Canby. mssEC 47 gives those words those meanings (Crowd and Chart = Lieut Gen
U.S. Grant, p.13 l.26; Mastiff = Canby, p.18 l.15; Tulip, Yacht, Yardstick = Period; Pike = Comma; Yawl =
Signed), and three such entries read from it word for word against the Official Records (reading-no2.md).
The same book is the one Tomokiyo's worked example of Cipher No. 2 (Canby to Halleck, 19 June 1864, sent by
Kimber from New Orleans) is written in.

## 2. The book

mssEC 47 (Huntington Digital Library object 596, 48 page images) is a filled-in copy of Stager's printed
template "Cipher for Telegraphic Correspondence ... 1861 & '62", the same template as mssEC 41 (Cipher No. 1)
and mssEC 67 (No. 9). The title page verso carries the holders' list: "The following persons have copy: Chas.
G. Eddy, Hd Qrs Gen Sherman; Capt W. G. Fuller, New Orleans; A. H. Caldwell, Hd Qrs A. P.; S. H. Beckwith, Hd
Qrs Gen Grant; R. R. McCaine, Hd Qrs Gen Sheridan" (pointer 553). Page [A] (554) is headed "No 2 General
Cipher" by hand, with the printed explanation corrected as in No. 1 ("Line Indicators", "Columns", the sentence
on "three combinations" struck). The Huntington's catalogue dates the volume "approximately 1866" from the
loose sheets laid in (a list of cipher holders for Nos. 1 and 5 in the Division of the Gulf, 7 May 1866, and a
receipt for No. 12 cipher of 13 July 1866, pointers 593-595); the tables themselves are the 1864 cipher: the
generals' page 13 gives "Lieut Gen U.S. Grant" (so filled after 9 March 1864) and the ledger entries of April
and June 1864 read from it. The sister copy mssEC 48 (object 636, 39 images) carries on its title page verso
"This Cipher is used by Maj Eckert, Washington; S H Beckwith, Hd Qurs Genl Grant; Col. Stager, Cleveland O;
Capt Chas. S Bulkley, New Orleans" (pointer 602), which is the narrow distribution Halleck described to Grant
on 22 Jan 1864 for the headquarters cipher (Tomokiyo, civilwar1.htm, "General Grant's Special Cipher"); its
tables were not transcribed.

Contents: page 1 the printed TIME table (48 names); pages 2-9 route pages for 7, 8, 5, 6, 7, 8, 9 and 10
columns, each with nine blind words carrying a handwritten figure, the route, and fifteen pairs of line
indicators (1-15 lines); pages 10-25 the arbitraries, 26 printed lines a page with a printed code word at each
end (Rivers, States, Forts, the President and Secretaries, Places and Generals, Rebel generals, Generals and
Admirals, then "Miscellaneous" in alphabetical order of meaning, with a handwritten section of days of the week
on page 25); four handwritten pages numbered 27-30 bound between pages 11 and 12 (generals, Georgia places,
common words, with their arbitraries); three written and one blank blue leaves after page 25 ([25A]-[25D]:
common words and the months); and a handwritten page "26" of numerals (pointer 588). The printed
"Commencement Word" / "Up" of the route pages is struck and "Columns" / "Down" written where the hand differs
from the print, as Tomokiyo describes for Nos. 1 and 2.

Transcription: single pass per page set by five subagents from the 1600 px images with 2400 px crops for the
doubtful spots (pages 10-15; 16-21; 22-25 with the blue leaves and the numerals page; TIME and routes; pages
27-30), 20 Sept 2026, checked by the orchestrator on the words the three ledger entries use and on the [25B]
alignment (section 6). The check on the entries is the control: 111 code-word tokens of the three entries read
from these tables, and the three readings agree with the Official Records word for word (reading-no2.md). A
second independent pass, as was done for mssEC 41, has not been made; readings the transcribers flagged carry
"[?]" in the meaning column.


## 3. Time words (grade H, mssEC 47 page 1, pointer 555)

The hours are as written on the printed TIME page; the last name of each column (12.30) is taken as in key.md section 5.

# Pass D: TIME page and route pages, mssEC 47 "Cipher No. 2" (Huntington, Eckert Papers)

Transcribed 20 Sept 2026 from the 1600 px IIIF JPEGs (pointers 555-563), with 2x local crops for the headers and doubtful rows. All entries read directly from the page image, grade H.



| code word | meaning | grade | source |
|---|---|---|---|
| Ann | 1 AM (time word) | H | TIME page (555) |
| Agnes | 1.30 AM (time word) | H | TIME page (555) |
| Anna | 2 AM (time word) | H | TIME page (555) |
| Amelia | 2.30 AM (time word) | H | TIME page (555) |
| Alice | 3 AM (time word) | H | TIME page (555) |
| Betsy | 3.30 AM (time word) | H | TIME page (555) |
| Barney | 4 AM (time word) | H | TIME page (555) |
| Barbara | 4.30 AM (time word) | H | TIME page (555) |
| Cora | 5 AM (time word) | H | TIME page (555) |
| Clara | 5.30 AM (time word) | H | TIME page (555) |
| Catharine | 6 AM (time word) | H | TIME page (555) |
| Cornelia | 6.30 AM (time word) | H | TIME page (555) |
| Clotilda | 7 AM (time word) | H | TIME page (555) |
| Delia | 7.30 AM (time word) | H | TIME page (555) |
| Deborah | 8 AM (time word) | H | TIME page (555) |
| Dorothy | 8.30 AM (time word) | H | TIME page (555) |
| Emma | 9 AM (time word) | H | TIME page (555) |
| Eugenia | 9.30 AM (time word) | H | TIME page (555) |
| Emily | 10 AM (time word) | H | TIME page (555) |
| Elizabeth | 10.30 AM (time word) | H | TIME page (555) |
| Fanny | 11 AM (time word) | H | TIME page (555) |
| Florence | 11.30 AM (time word) | H | TIME page (555) |
| Francis | 12.30 AM (time word) | H | TIME page (555) |
| Gertrude | 12 noon AM (time word) | H | TIME page (555) |
| Harriet | 1.30 PM (time word) | H | TIME page (555) |
| Hannah | 1 PM (time word) | H | TIME page (555) |
| Helen | 2 PM (time word) | H | TIME page (555) |
| Henrietta | 2.30 PM (time word) | H | TIME page (555) |
| Imogene | 3.30 PM (time word) | H | TIME page (555) |
| Jennie | 3 PM (time word) | H | TIME page (555) |
| Julia | 4 PM (time word) | H | TIME page (555) |
| Katy | 4.30 PM (time word) | H | TIME page (555) |
| Lucy | 5.30 PM (time word) | H | TIME page (555) |
| Laura | 5 PM (time word) | H | TIME page (555) |
| Libby | 6 PM (time word) | H | TIME page (555) |
| Mary | 6.30 PM (time word) | H | TIME page (555) |
| Martha | 7.30 PM (time word) | H | TIME page (555) |
| Minnie | 7 PM (time word) | H | TIME page (555) |
| Nancy | 8 PM (time word) | H | TIME page (555) |
| Nelly | 8.30 PM (time word) | H | TIME page (555) |
| Rosalie | 9.30 PM (time word) | H | TIME page (555) |
| Rosetta | 9 PM (time word) | H | TIME page (555) |
| Rebecca | 10 PM (time word) | H | TIME page (555) |
| Reliance | 10.30 PM (time word) | H | TIME page (555) |
| Sarah | 11.30 PM (time word) | H | TIME page (555) |
| Susan | 11 PM (time word) | H | TIME page (555) |
| Topsy | 12.30 PM (time word) | H | TIME page (555) |
| Viola | 12 midnight PM (time word) | H | TIME page (555) |

## 4. Blind words, routes and line indicators (grade H, mssEC 47 pages 2-9, pointers 556-563)

As in Cipher No. 1 the nine blind words of a page stand for the number of columns at its head and for the page's route; a handwritten figure before each blind word (Tomokiyo's observation on No. 2) is recorded with it. Two line indicators are added to give the number of lines. The ledger entries are recorded untransposed, so none of this is needed to read them; decode.py leaves these words as written inside an entry, and the arbitraries tables below take precedence for the printed words that occur in both (Battle, Yard ...).

### Routes (pages 2-9)

| page (pointer) | columns | blind words with their handwritten figures | route as filled in |
|---|---|---|---|
| p.2 (556) | 7 | 6 Army, 8 Anson, 10 Action, 5 Astor, 9 Advance, 6 Artillery, 8 Anderson, 10 Ambush, 5 Agree | down the 1st (printed Up struck, Down written), down the 6th, up the 7th, down the 2nd, up the 5th, down the 3rd, up the 4th |
| p.3 (557) | 8 | 9 Battle, 7 Boston, 6 Blair, 10 Banks, 7 Board, 5 Battery, 6 Brigade, 7 Beverly, 9 Bates | down the 8th (printed Up struck, Down written), down the 7th, up the 1st, down the 6th, up the 3rd, down the 2nd, up the 5th, down the 4th (hand-added continuation line) |
| p.4 (558) | 5 | 10 Cairo, 8 Curtin, 6 Cavalry, 7 Congress, 9 Colburn, 8 Childs, 6 Calhoun, 9 Church, 10 Cobb | up the 3rd, down the 2nd, up the 1st, down the 5th, up the 4th (last two printed slots left blank) |
| p.5 (559) | 6 | 5 Driver, 7 Dupont, 9 Dunn, 10 Enemy, 9 Enlist, 8 Engage, 7 Forward, 5 Foote, 10 Forts | [first printed slot "Up the ___" left unfilled, a dash drawn in it], down the 6th, up the 3rd, down the 1st, up the 5th, down the 4th, up the 2nd |
| p.6 (560) | 7 | 6 Grayson, 8 Giles, 10 Grafton, 9 Guard, 5 Henry, 8 Harbor, 10 Kelly, 6 Lucky, 9 Mobile | up the 7th, down the 1st, up the 5th, down the 4th, up the 6th, down the 3rd, up the 2nd |
| p.7 (561) | 8 | 5 Morton, 6 Memphis, 7 Navy, 7 Potts, 9 Porter, 10 Perry, 5 Regulars, 6 Rosecrans, 7 Run | up the 6th, down the 7th, up the 2nd, down the 1st, up the 8th, down the 5th, up the 3rd, down the 4th (hand-added continuation line) |
| p.8 (562) | 9 | 6 Skirmish, 7 Sherman, 8 Sumter, 5 Todd, 7 Threaten, 10 Thomas, 8 Volunteers, 6 Wise, 10 War | up the 2nd, down the 3rd, up the 9th, down the 1st, up the 6th, down the 4th, up the 8th, down the 7th, up the 5th (last two legs hand-added continuation line) |
| p.9 (563) | 10 | 5 Yates, 6 Lincoln, 7 Chase, 6 Stanton, 7 McClellan, 8 McDowell, 7 Halleck, 8 Buell, 9 Sibley | up the 5th, down the 1st, up the 10th, down the 6th, up the 4th, down the 2nd, up the 9th, down the 8th, up the 3rd, down the 7th (last three legs hand-added continuation line below the rule) |

### page 2 (556)

| code word | meaning | grade | source |
|---|---|---|---|
| Army | blind word: 7 columns, route of page 2; handwritten figure 6 | H | p.2 (556) |
| Anson | blind word: 7 columns, route of page 2; handwritten figure 8 | H | p.2 (556) |
| Action | blind word: 7 columns, route of page 2; handwritten figure 10 | H | p.2 (556) |
| Astor | blind word: 7 columns, route of page 2; handwritten figure 5 | H | p.2 (556) |
| Advance | blind word: 7 columns, route of page 2; handwritten figure 9 | H | p.2 (556) |
| Artillery | blind word: 7 columns, route of page 2; handwritten figure 6 | H | p.2 (556) |
| Anderson | blind word: 7 columns, route of page 2; handwritten figure 8 | H | p.2 (556) |
| Ambush | blind word: 7 columns, route of page 2; handwritten figure 10 | H | p.2 (556) |
| Agree | blind word: 7 columns, route of page 2; handwritten figure 5 | H | p.2 (556) |
| Absent | line indicator: 1 lines (page 2) | H | p.2 (556) L |
| Assent | line indicator: 1 lines (page 2) | H | p.2 (556) R |
| Admit | line indicator: 2 lines (page 2) | H | p.2 (556) L |
| Arsenal | line indicator: 2 lines (page 2) | H | p.2 (556) R |
| Ample | line indicator: 3 lines (page 2) | H | p.2 (556) L |
| Assist | line indicator: 3 lines (page 2) | H | p.2 (556) R |
| Alarm | line indicator: 4 lines (page 2) | H | p.2 (556) L |
| Avail | line indicator: 4 lines (page 2) | H | p.2 (556) R |
| Anxious | line indicator: 5 lines (page 2) | H | p.2 (556) L |
| Attempt | line indicator: 5 lines (page 2) | H | p.2 (556) R |
| Approve | line indicator: 6 lines (page 2) | H | p.2 (556) L |
| Assume | line indicator: 6 lines (page 2) | H | p.2 (556) R |
| Baffle | line indicator: 7 lines (page 2) | H | p.2 (556) L |
| Blame | line indicator: 7 lines (page 2) | H | p.2 (556) R |
| Benefit | line indicator: 8 lines (page 2) | H | p.2 (556) L |
| Bloody | line indicator: 8 lines (page 2) | H | p.2 (556) R |
| Bashful | line indicator: 9 lines (page 2) | H | p.2 (556) L |
| Bread | line indicator: 9 lines (page 2) | H | p.2 (556) R |
| Bounty | line indicator: 10 lines (page 2) | H | p.2 (556) L |
| Bunting | line indicator: 10 lines (page 2) | H | p.2 (556) R |
| Blunder | line indicator: 11 lines (page 2) | H | p.2 (556) L |
| Bulk | line indicator: 11 lines (page 2) | H | p.2 (556) R |
| Blank | line indicator: 12 lines (page 2) | H | p.2 (556) L |
| Brunt | line indicator: 12 lines (page 2) | H | p.2 (556) R |
| Canal | line indicator: 13 lines (page 2) | H | p.2 (556) L |
| Conduct | line indicator: 13 lines (page 2) | H | p.2 (556) R |
| Captive | line indicator: 14 lines (page 2) | H | p.2 (556) L |
| Consume | line indicator: 14 lines (page 2) | H | p.2 (556) R |
| Complain | line indicator: 15 lines (page 2) | H | p.2 (556) L |
| Caution | line indicator: 15 lines (page 2) | H | p.2 (556) R |

### page 3 (557)

| code word | meaning | grade | source |
|---|---|---|---|
| Battle | blind word: 8 columns, route of page 3; handwritten figure 9 | H | p.3 (557) |
| Boston | blind word: 8 columns, route of page 3; handwritten figure 7 | H | p.3 (557) |
| Blair | blind word: 8 columns, route of page 3; handwritten figure 6 | H | p.3 (557) |
| Banks | blind word: 8 columns, route of page 3; handwritten figure 10 | H | p.3 (557) |
| Board | blind word: 8 columns, route of page 3; handwritten figure 7 | H | p.3 (557) |
| Battery | blind word: 8 columns, route of page 3; handwritten figure 5 | H | p.3 (557) |
| Brigade | blind word: 8 columns, route of page 3; handwritten figure 6 | H | p.3 (557) |
| Beverly | blind word: 8 columns, route of page 3; handwritten figure 7 | H | p.3 (557) |
| Bates | blind word: 8 columns, route of page 3; handwritten figure 9 | H | p.3 (557) |
| Challenge | line indicator: 1 lines (page 3) | H | p.3 (557) L |
| Confirm | line indicator: 1 lines (page 3) | H | p.3 (557) R |
| Channel | line indicator: 2 lines (page 3) | H | p.3 (557) L |
| Combat | line indicator: 2 lines (page 3) | H | p.3 (557) R |
| Cripple | line indicator: 3 lines (page 3) | H | p.3 (557) L |
| Cargo | line indicator: 3 lines (page 3) | H | p.3 (557) R |
| Draft | line indicator: 4 lines (page 3) | H | p.3 (557) L |
| Defeat | line indicator: 4 lines (page 3) | H | p.3 (557) R |
| Damage | line indicator: 5 lines (page 3) | H | p.3 (557) L |
| Disband | line indicator: 5 lines (page 3) | H | p.3 (557) R |
| Defend | line indicator: 6 lines (page 3) | H | p.3 (557) L |
| Delay | line indicator: 6 lines (page 3) | H | p.3 (557) R |
| Doubt | line indicator: 7 lines (page 3) | H | p.3 (557) L |
| Demand | line indicator: 7 lines (page 3) | H | p.3 (557) R |
| Divide | line indicator: 8 lines (page 3) | H | p.3 (557) L |
| Defect | line indicator: 8 lines (page 3) | H | p.3 (557) R |
| Effect | line indicator: 9 lines (page 3) | H | p.3 (557) L |
| Enrol | line indicator: 9 lines (page 3) | H | p.3 (557) R |
| Elude | line indicator: 10 lines (page 3) | H | p.3 (557) L |
| Enough | line indicator: 10 lines (page 3) | H | p.3 (557) R |
| Encamp | line indicator: 11 lines (page 3) | H | p.3 (557) L |
| Entire | line indicator: 11 lines (page 3) | H | p.3 (557) R |
| Evidence | line indicator: 12 lines (page 3) | H | p.3 (557) L |
| Expect | line indicator: 12 lines (page 3) | H | p.3 (557) R |
| Extend | line indicator: 13 lines (page 3) | H | p.3 (557) L |
| Enable | line indicator: 13 lines (page 3) | H | p.3 (557) R |
| Family | line indicator: 14 lines (page 3) | H | p.3 (557) L |
| Finish | line indicator: 14 lines (page 3) | H | p.3 (557) R |
| Fatal | line indicator: 15 lines (page 3) | H | p.3 (557) L |
| Freshet | line indicator: 15 lines (page 3) | H | p.3 (557) R |

### page 4 (558)

| code word | meaning | grade | source |
|---|---|---|---|
| Cairo | blind word: 5 columns, route of page 4; handwritten figure 10 | H | p.4 (558) |
| Curtin | blind word: 5 columns, route of page 4; handwritten figure 8 | H | p.4 (558) |
| Cavalry | blind word: 5 columns, route of page 4; handwritten figure 6 | H | p.4 (558) |
| Congress | blind word: 5 columns, route of page 4; handwritten figure 7 | H | p.4 (558) |
| Colburn | blind word: 5 columns, route of page 4; handwritten figure 9 | H | p.4 (558) |
| Childs | blind word: 5 columns, route of page 4; handwritten figure 8 | H | p.4 (558) |
| Calhoun | blind word: 5 columns, route of page 4; handwritten figure 6 | H | p.4 (558) |
| Church | blind word: 5 columns, route of page 4; handwritten figure 9 | H | p.4 (558) |
| Cobb | blind word: 5 columns, route of page 4; handwritten figure 10 | H | p.4 (558) |
| False | line indicator: 1 lines (page 4) | H | p.4 (558) L |
| Friends | line indicator: 1 lines (page 4) | H | p.4 (558) R |
| Fancy | line indicator: 2 lines (page 4) | H | p.4 (558) L |
| Future | line indicator: 2 lines (page 4) | H | p.4 (558) R |
| Funds | line indicator: 3 lines (page 4) | H | p.4 (558) L |
| Folly | line indicator: 3 lines (page 4) | H | p.4 (558) R |
| Gabble | line indicator: 4 lines (page 4) | H | p.4 (558) L |
| Glad | line indicator: 4 lines (page 4) | H | p.4 (558) R |
| Grade | line indicator: 5 lines (page 4) | H | p.4 (558) L |
| Gossip | line indicator: 5 lines (page 4) | H | p.4 (558) R |
| Goods | line indicator: 6 lines (page 4) | H | p.4 (558) L |
| Grant | line indicator: 6 lines (page 4) | H | p.4 (558) R |
| Grain | line indicator: 7 lines (page 4) | H | p.4 (558) L |
| Guide | line indicator: 7 lines (page 4) | H | p.4 (558) R |
| Grave | line indicator: 8 lines (page 4) | H | p.4 (558) L |
| Gunner | line indicator: 8 lines (page 4) | H | p.4 (558) R |
| Happen | line indicator: 9 lines (page 4) | H | p.4 (558) L |
| Homage | line indicator: 9 lines (page 4) | H | p.4 (558) R |
| Handle | line indicator: 10 lines (page 4) | H | p.4 (558) L |
| Health | line indicator: 10 lines (page 4) | H | p.4 (558) R |
| Havoc | line indicator: 11 lines (page 4) | H | p.4 (558) L |
| Hospital | line indicator: 11 lines (page 4) | H | p.4 (558) R |
| Help | line indicator: 12 lines (page 4) | H | p.4 (558) L |
| Hostage | line indicator: 12 lines (page 4) | H | p.4 (558) R |
| Honest | line indicator: 13 lines (page 4) | H | p.4 (558) L |
| Harp | line indicator: 13 lines (page 4) | H | p.4 (558) R |
| Invade | line indicator: 14 lines (page 4) | H | p.4 (558) L |
| Impending | line indicator: 14 lines (page 4) | H | p.4 (558) R |
| Inspect | line indicator: 15 lines (page 4) | H | p.4 (558) L |
| Implore | line indicator: 15 lines (page 4) | H | p.4 (558) R |

### page 5 (559)

| code word | meaning | grade | source |
|---|---|---|---|
| Driver | blind word: 6 columns, route of page 5; handwritten figure 5 | H | p.5 (559) |
| Dupont | blind word: 6 columns, route of page 5; handwritten figure 7 | H | p.5 (559) |
| Dunn | blind word: 6 columns, route of page 5; handwritten figure 9 | H | p.5 (559) |
| Enemy | blind word: 6 columns, route of page 5; handwritten figure 10 | H | p.5 (559) |
| Enlist | blind word: 6 columns, route of page 5; handwritten figure 9 | H | p.5 (559) |
| Engage | blind word: 6 columns, route of page 5; handwritten figure 8 | H | p.5 (559) |
| Forward | blind word: 6 columns, route of page 5; handwritten figure 7 | H | p.5 (559) |
| Foote | blind word: 6 columns, route of page 5; handwritten figure 5 | H | p.5 (559) |
| Forts | blind word: 6 columns, route of page 5; handwritten figure 10 | H | p.5 (559) |
| Impulse | line indicator: 1 lines (page 5) | H | p.5 (559) L |
| Influence | line indicator: 1 lines (page 5) | H | p.5 (559) R |
| Include | line indicator: 2 lines (page 5) | H | p.5 (559) L |
| Invalid | line indicator: 2 lines (page 5) | H | p.5 (559) R |
| Increase | line indicator: 3 lines (page 5) | H | p.5 (559) L |
| Inflict | line indicator: 3 lines (page 5) | H | p.5 (559) R |
| Jail | line indicator: 4 lines (page 5) | H | p.5 (559) L |
| Jealous | line indicator: 4 lines (page 5) | H | p.5 (559) R |
| Just | line indicator: 5 lines (page 5) | H | p.5 (559) L |
| Join | line indicator: 5 lines (page 5) | H | p.5 (559) R |
| Jewel | line indicator: 6 lines (page 5) | H | p.5 (559) L |
| Journey | line indicator: 6 lines (page 5) | H | p.5 (559) R |
| Jump | line indicator: 7 lines (page 5) | H | p.5 (559) L |
| Junction | line indicator: 7 lines (page 5) | H | p.5 (559) R |
| Judge | line indicator: 8 lines (page 5) | H | p.5 (559) L |
| Justify | line indicator: 8 lines (page 5) | H | p.5 (559) R |
| Keep | line indicator: 9 lines (page 5) | H | p.5 (559) L |
| Knob | line indicator: 9 lines (page 5) | H | p.5 (559) R |
| Knife | line indicator: 10 lines (page 5) | H | p.5 (559) L |
| Knowledge | line indicator: 10 lines (page 5) | H | p.5 (559) R |
| Kind | line indicator: 11 lines (page 5) | H | p.5 (559) L |
| Knave | line indicator: 11 lines (page 5) | H | p.5 (559) R |
| Kill | line indicator: 12 lines (page 5) | H | p.5 (559) L |
| Key | line indicator: 12 lines (page 5) | H | p.5 (559) R |
| Kneel | line indicator: 13 lines (page 5) | H | p.5 (559) L |
| Known | line indicator: 13 lines (page 5) | H | p.5 (559) R |
| Long | line indicator: 14 lines (page 5) | H | p.5 (559) L |
| Little | line indicator: 14 lines (page 5) | H | p.5 (559) R |
| Loyal | line indicator: 15 lines (page 5) | H | p.5 (559) L |
| Load | line indicator: 15 lines (page 5) | H | p.5 (559) R |

### page 6 (560)

| code word | meaning | grade | source |
|---|---|---|---|
| Grayson | blind word: 7 columns, route of page 6; handwritten figure 6 | H | p.6 (560) |
| Giles | blind word: 7 columns, route of page 6; handwritten figure 8 | H | p.6 (560) |
| Grafton | blind word: 7 columns, route of page 6; handwritten figure 10 | H | p.6 (560) |
| Guard | blind word: 7 columns, route of page 6; handwritten figure 9 | H | p.6 (560) |
| Henry | blind word: 7 columns, route of page 6; handwritten figure 5 | H | p.6 (560) |
| Harbor | blind word: 7 columns, route of page 6; handwritten figure 8 | H | p.6 (560) |
| Kelly | blind word: 7 columns, route of page 6; handwritten figure 10 | H | p.6 (560) |
| Lucky | blind word: 7 columns, route of page 6; handwritten figure 6 | H | p.6 (560) |
| Mobile | blind word: 7 columns, route of page 6; handwritten figure 9 | H | p.6 (560) |
| Labor | line indicator: 1 lines (page 6) | H | p.6 (560) L |
| Lawful | line indicator: 1 lines (page 6) | H | p.6 (560) R |
| Lament | line indicator: 2 lines (page 6) | H | p.6 (560) L |
| Legal | line indicator: 2 lines (page 6) | H | p.6 (560) R |
| Large | line indicator: 3 lines (page 6) | H | p.6 (560) L |
| Land | line indicator: 3 lines (page 6) | H | p.6 (560) R |
| Manage | line indicator: 4 lines (page 6) | H | p.6 (560) L |
| March | line indicator: 4 lines (page 6) | H | p.6 (560) R |
| Map | line indicator: 5 lines (page 6) | H | p.6 (560) L |
| Mutiny | line indicator: 5 lines (page 6) | H | p.6 (560) R |
| Mail | line indicator: 6 lines (page 6) | H | p.6 (560) L |
| Mutual | line indicator: 6 lines (page 6) | H | p.6 (560) R |
| Money | line indicator: 7 lines (page 6) | H | p.6 (560) L |
| Model | line indicator: 7 lines (page 6) | H | p.6 (560) R |
| Menace | line indicator: 8 lines (page 6) | H | p.6 (560) L |
| Musket | line indicator: 8 lines (page 6) | H | p.6 (560) R |
| Noble | line indicator: 9 lines (page 6) | H | p.6 (560) L |
| Never | line indicator: 9 lines (page 6) | H | p.6 (560) R |
| Nothing | line indicator: 10 lines (page 6) | H | p.6 (560) L |
| Nature | line indicator: 10 lines (page 6) | H | p.6 (560) R |
| News | line indicator: 11 lines (page 6) | H | p.6 (560) L |
| Naval | line indicator: 11 lines (page 6) | H | p.6 (560) R |
| Neglect | line indicator: 12 lines (page 6) | H | p.6 (560) L |
| Nominal | line indicator: 12 lines (page 6) | H | p.6 (560) R |
| Next | line indicator: 13 lines (page 6) | H | p.6 (560) L |
| Notify | line indicator: 13 lines (page 6) | H | p.6 (560) R |
| Oath | line indicator: 14 lines (page 6) | H | p.6 (560) L |
| Observe | line indicator: 14 lines (page 6) | H | p.6 (560) R |
| Obtain | line indicator: 15 lines (page 6) | H | p.6 (560) L |
| Offend | line indicator: 15 lines (page 6) | H | p.6 (560) R |

### page 7 (561)

| code word | meaning | grade | source |
|---|---|---|---|
| Morton | blind word: 8 columns, route of page 7; handwritten figure 5 | H | p.7 (561) |
| Memphis | blind word: 8 columns, route of page 7; handwritten figure 6 | H | p.7 (561) |
| Navy | blind word: 8 columns, route of page 7; handwritten figure 7 | H | p.7 (561) |
| Potts | blind word: 8 columns, route of page 7; handwritten figure 7 | H | p.7 (561) |
| Porter | blind word: 8 columns, route of page 7; handwritten figure 9 | H | p.7 (561) |
| Perry | blind word: 8 columns, route of page 7; handwritten figure 10 | H | p.7 (561) |
| Regulars | blind word: 8 columns, route of page 7; handwritten figure 5 | H | p.7 (561) |
| Rosecrans | blind word: 8 columns, route of page 7; handwritten figure 6 | H | p.7 (561) |
| Run | blind word: 8 columns, route of page 7; handwritten figure 7 | H | p.7 (561) |
| Outrage | line indicator: 1 lines (page 7) | H | p.7 (561) L |
| Operate | line indicator: 1 lines (page 7) | H | p.7 (561) R |
| Official | line indicator: 2 lines (page 7) | H | p.7 (561) L |
| Object | line indicator: 2 lines (page 7) | H | p.7 (561) R |
| Oppose | line indicator: 3 lines (page 7) | H | p.7 (561) L |
| Oblige | line indicator: 3 lines (page 7) | H | p.7 (561) R |
| Painful | line indicator: 4 lines (page 7) | H | p.7 (561) L |
| Progress | line indicator: 4 lines (page 7) | H | p.7 (561) R |
| Patrol | line indicator: 5 lines (page 7) | H | p.7 (561) L |
| Prompt | line indicator: 5 lines (page 7) | H | p.7 (561) R |
| Penalty | line indicator: 6 lines (page 7) | H | p.7 (561) L |
| Prison | line indicator: 6 lines (page 7) | H | p.7 (561) R |
| Perfidy | line indicator: 7 lines (page 7) | H | p.7 (561) L |
| Possible | line indicator: 7 lines (page 7) | H | p.7 (561) R |
| Plenty | line indicator: 8 lines (page 7) | H | p.7 (561) L |
| Punish | line indicator: 8 lines (page 7) | H | p.7 (561) R |
| Quality | line indicator: 9 lines (page 7) | H | p.7 (561) L |
| Perform | line indicator: 9 lines (page 7) | H | p.7 (561) R |
| Quarter | line indicator: 10 lines (page 7) | H | p.7 (561) L |
| Persist | line indicator: 10 lines (page 7) | H | p.7 (561) R |
| Quota | line indicator: 11 lines (page 7) | H | p.7 (561) L |
| Pleasant | line indicator: 11 lines (page 7) | H | p.7 (561) R |
| Quite | line indicator: 12 lines (page 7) | H | p.7 (561) L |
| Policy | line indicator: 12 lines (page 7) | H | p.7 (561) R |
| Praise | line indicator: 13 lines (page 7) | H | p.7 (561) L |
| Portable | line indicator: 13 lines (page 7) | H | p.7 (561) R |
| Ratify | line indicator: 14 lines (page 7) | H | p.7 (561) L |
| Relapse | line indicator: 14 lines (page 7) | H | p.7 (561) R |
| Reduce | line indicator: 15 lines (page 7) | H | p.7 (561) L |
| Remark | line indicator: 15 lines (page 7) | H | p.7 (561) R |

### page 8 (562)

| code word | meaning | grade | source |
|---|---|---|---|
| Skirmish | blind word: 9 columns, route of page 8; handwritten figure 6 | H | p.8 (562) |
| Sherman | blind word: 9 columns, route of page 8; handwritten figure 7 | H | p.8 (562) |
| Sumter | blind word: 9 columns, route of page 8; handwritten figure 8 | H | p.8 (562) |
| Todd | blind word: 9 columns, route of page 8; handwritten figure 5 | H | p.8 (562) |
| Threaten | blind word: 9 columns, route of page 8; handwritten figure 7 | H | p.8 (562) |
| Thomas | blind word: 9 columns, route of page 8; handwritten figure 10 | H | p.8 (562) |
| Volunteers | blind word: 9 columns, route of page 8; handwritten figure 8 | H | p.8 (562) |
| Wise | blind word: 9 columns, route of page 8; handwritten figure 6 | H | p.8 (562) |
| War | blind word: 9 columns, route of page 8; handwritten figure 10 | H | p.8 (562) |
| Request | line indicator: 1 lines (page 8) | H | p.8 (562) L |
| Repulse | line indicator: 1 lines (page 8) | H | p.8 (562) R |
| Resist | line indicator: 2 lines (page 8) | H | p.8 (562) L |
| Round | line indicator: 2 lines (page 8) | H | p.8 (562) R |
| Reform | line indicator: 3 lines (page 8) | H | p.8 (562) L |
| Rumor | line indicator: 3 lines (page 8) | H | p.8 (562) R |
| Salute | line indicator: 4 lines (page 8) | H | p.8 (562) L |
| Station | line indicator: 4 lines (page 8) | H | p.8 (562) R |
| Sanguine | line indicator: 5 lines (page 8) | H | p.8 (562) L |
| Sudden | line indicator: 5 lines (page 8) | H | p.8 (562) R |
| Satisfy | line indicator: 6 lines (page 8) | H | p.8 (562) L |
| Sundry | line indicator: 6 lines (page 8) | H | p.8 (562) R |
| Signal | line indicator: 7 lines (page 8) | H | p.8 (562) L |
| Surprise | line indicator: 7 lines (page 8) | H | p.8 (562) R |
| Submit | line indicator: 8 lines (page 8) | H | p.8 (562) L |
| Silence | line indicator: 8 lines (page 8) | H | p.8 (562) R |
| Talent | line indicator: 9 lines (page 8) | H | p.8 (562) L |
| Treason | line indicator: 9 lines (page 8) | H | p.8 (562) R |
| Testify | line indicator: 10 lines (page 8) | H | p.8 (562) L |
| Track | line indicator: 10 lines (page 8) | H | p.8 (562) R |
| Timely | line indicator: 11 lines (page 8) | H | p.8 (562) L |
| Transmit | line indicator: 11 lines (page 8) | H | p.8 (562) R |
| Tidings | line indicator: 12 lines (page 8) | H | p.8 (562) L |
| Temper | line indicator: 12 lines (page 8) | H | p.8 (562) R |
| Transfer | line indicator: 13 lines (page 8) | H | p.8 (562) L |
| Terminus | line indicator: 13 lines (page 8) | H | p.8 (562) R |
| Unjust | line indicator: 14 lines (page 8) | H | p.8 (562) L |
| Union | line indicator: 14 lines (page 8) | H | p.8 (562) R |
| Unfit | line indicator: 15 lines (page 8) | H | p.8 (562) L |
| Usual | line indicator: 15 lines (page 8) | H | p.8 (562) R |

### page 9 (563)

| code word | meaning | grade | source |
|---|---|---|---|
| Yates | blind word: 10 columns, route of page 9; handwritten figure 5 | H | p.9 (563) |
| Lincoln | blind word: 10 columns, route of page 9; handwritten figure 6 | H | p.9 (563) |
| Chase | blind word: 10 columns, route of page 9; handwritten figure 7 | H | p.9 (563) |
| Stanton | blind word: 10 columns, route of page 9; handwritten figure 6 | H | p.9 (563) |
| McClellan | blind word: 10 columns, route of page 9; handwritten figure 7 | H | p.9 (563) |
| McDowell | blind word: 10 columns, route of page 9; handwritten figure 8 | H | p.9 (563) |
| Halleck | blind word: 10 columns, route of page 9; handwritten figure 7 | H | p.9 (563) |
| Buell | blind word: 10 columns, route of page 9; handwritten figure 8 | H | p.9 (563) |
| Sibley | blind word: 10 columns, route of page 9; handwritten figure 9 | H | p.9 (563) |
| Urgent | line indicator: 1 lines (page 9) | H | p.9 (563) L |
| Unworthy | line indicator: 1 lines (page 9) | H | p.9 (563) R |
| Unwise | line indicator: 2 lines (page 9) | H | p.9 (563) L |
| Untrue | line indicator: 2 lines (page 9) | H | p.9 (563) R |
| Utmost | line indicator: 3 lines (page 9) | H | p.9 (563) L |
| Unsound | line indicator: 3 lines (page 9) | H | p.9 (563) R |
| Vacancy | line indicator: 4 lines (page 9) | H | p.9 (563) L |
| Vicinity | line indicator: 4 lines (page 9) | H | p.9 (563) R |
| Valuable | line indicator: 5 lines (page 9) | H | p.9 (563) L |
| Vital | line indicator: 5 lines (page 9) | H | p.9 (563) R |
| Version | line indicator: 6 lines (page 9) | H | p.9 (563) L |
| Victim | line indicator: 6 lines (page 9) | H | p.9 (563) R |
| Veteran | line indicator: 7 lines (page 9) | H | p.9 (563) L |
| Variety | line indicator: 7 lines (page 9) | H | p.9 (563) R |
| Vessel | line indicator: 8 lines (page 9) | H | p.9 (563) L |
| Voyage | line indicator: 8 lines (page 9) | H | p.9 (563) R |
| Wagon | line indicator: 9 lines (page 9) | H | p.9 (563) L |
| Winter | line indicator: 9 lines (page 9) | H | p.9 (563) R |
| Warm | line indicator: 10 lines (page 9) | H | p.9 (563) L |
| Weather | line indicator: 10 lines (page 9) | H | p.9 (563) R |
| Welcome | line indicator: 11 lines (page 9) | H | p.9 (563) L |
| Wrong | line indicator: 11 lines (page 9) | H | p.9 (563) R |
| Witness | line indicator: 12 lines (page 9) | H | p.9 (563) L |
| Worthy | line indicator: 12 lines (page 9) | H | p.9 (563) R |
| Wonder | line indicator: 13 lines (page 9) | H | p.9 (563) L |
| Warrant | line indicator: 13 lines (page 9) | H | p.9 (563) R |
| Yard | line indicator: 14 lines (page 9) | H | p.9 (563) L |
| Yield | line indicator: 14 lines (page 9) | H | p.9 (563) R |
| Year | line indicator: 15 lines (page 9) | H | p.9 (563) L |
| You | line indicator: 15 lines (page 9) | H | p.9 (563) R |

### Notes

- TIME page (555): the half-hours are written as a small superscript "30" over a stroke (e.g. "1 30"), except Agnes "1.30"; all normalised here to "n.30". The pairing is not monotonic: in the AM column Francis = 12.30 precedes Gertrude = 12 noon; in the PM column Harriet = 1.30 precedes Hannah = 1, and the pairs Imogene 3.30 / Jennie 3, Lucy 5.30 / Laura 5, Martha 7.30 / Minnie 7, Rosalie 9.30 / Rosetta 9, Sarah 11.30 / Susan 11, Topsy 12.30 / Viola 12 midnight are likewise reversed relative to the AM pattern. Read as written.
- Every route page has the printed word after "Message or division of ___" (probably "lines") struck with a heavy ink bar and "Columns" written after it; a second heavy bar strikes the printed heading beneath ("COMMENCEMENT WORDS", still legible on pp. 5-6 = 559-560).
- The printed "Columns" after each brace is also overwritten by hand with "Columns" on every page (cursive, sometimes written diagonally along the brace).
- Pages 2 (556) and 3 (557): the printed "Up" at the start of the ROUTE line is struck and "Down" is written above it, so the route begins down-down (down 1st, down 6th on p.2; down 8th, down 7th on p.3).
- Page 3 (557), page 7 (561), page 8 (562), page 9 (563): the eight printed slots are not enough for 8, 8, 9 and 10 columns; the extra legs are written by hand on a further line ("Down the 4th"; "Down the 4th"; "Down the 7th Up the 5th"; "Down the 8th Up the 3rd Down the 7th").
- Page 4 (558): 5 columns; only five slots filled, the last two printed slots ("down the ___ - up the ___") left blank.
- Page 5 (559): 6 columns; the first printed slot ("Up the ___ column") is left unfilled with a short dash drawn in it, and the six legs occupy slots 2-7 (down 6th ... up 2nd).
- Pages 7 (561) and 9 (563): the blind-word figures of the left group (p.7) and of all three groups (p.9) are written to the right of the word, between word and brace, not to the left as on the other pages; page order is preserved here.
- Page 6 (560), right group: the figures 10 / 6 / 9 for Kelly / Lucky / Mobile are partly overwritten by the brace; read as 10, 6, 9.
- Page 2 (556): line indicator 12 R read as "Brunt" (checked on 2x crop). Page 3 (557) 9 R "Enrol" is spelled with one l. Page 4 (558) 13 R "Harp" and 15 R "Implore" have long flourished tails. Page 9 (563) 15 R "You" and 14 R "Yield" have flourished tails.
- No word is marked [?]: after enlargement no reading remained doubtful.
- Figures per page: 9 blind words and 30 line-indicator words on each of the eight route pages (72 blind words, 240 line indicators); 48 time words.

## 5. Arbitrary words (grade H, mssEC 47 pages 10-25, pointers 564-565, 570-583)

Meanings as written; "(-ed, -ing)" renders the book's "= ed = ing"; "[#]" marks the code word against which the inflection sign stands. Source "p.10 l.3 (564) L" = page 10, printed line 3, left-hand printed word, Huntington pointer 564 (image images/mssEC47_p564.jpg).

### page 10 (564)

| code word | meaning | grade | source |
|---|---|---|---|
| (l.0: heading "Rivers" written in the top margin above the first printed line) | - | H | p.10 l.0 (564) |
| Adam | Arkansas | H | p.10 l.1 (564) L |
| Asia | Alabama | H | p.10 l.1 (564) R |
| Abel | Aquia Creek | H | p.10 l.2 (564) L |
| Austria | Big Sandy | H | p.10 l.2 (564) R |
| Aaron | Bear | H | p.10 l.3 (564) L |
| Arabia | Big Black | H | p.10 l.3 (564) R |
| Amos | Cumberland | H | p.10 l.4 (564) L |
| Africa | Cumberland | H | p.10 l.4 (564) R |
| Anthony | Chattahoochie | H | p.10 l.5 (564) L |
| America | Chickamunga [sic] | H | p.10 l.5 (564) R |
| Acton | Chowan | H | p.10 l.6 (564) L |
| Alba | Clinch | H | p.10 l.6 (564) R |
| Abner | Coosa | H | p.10 l.7 (564) L |
| Alpha | Edisto | H | p.10 l.7 (564) R |
| Alden | Elizabeth | H | p.10 l.8 (564) L |
| Andover | Etowah | H | p.10 l.8 (564) R |
| Alvord | Hiawassie | H | p.10 l.9 (564) L |
| Antwerp | Holston | H | p.10 l.9 (564) R |
| Abbot | James | H | p.10 l.10 (564) L |
| Aragon | Kanawha | H | p.10 l.10 (564) R |
| Agnew | Mississippi | H | p.10 l.11 (564) L |
| Aurora | Mississippi | H | p.10 l.11 (564) R |
| Adonis | Missouri | H | p.10 l.12 (564) L |
| Ashland | Neuse | H | p.10 l.12 (564) R |
| Abacus | Ohio | H | p.10 l.13 (564) L |
| Avon | Ohio | H | p.10 l.13 (564) R |
| Argus | Potomac | H | p.10 l.14 (564) L |
| Advent | Potomac | H | p.10 l.14 (564) R |
| Argyle | Rappahannock | H | p.10 l.15 (564) L |
| Adverb | Rappahannock | H | p.10 l.15 (564) R |
| Arno | Oostanoula [sic] | H | p.10 l.16 (564) L |
| Ague | Pearl | H | p.10 l.16 (564) R |
| Adrian | Rapidan | H | p.10 l.17 (564) L |
| Alloy | Roanoke | H | p.10 l.17 (564) R |
| Apollo | Shenandoah | H | p.10 l.18 (564) L |
| Altar | Red R | H | p.10 l.18 (564) R |
| Alps | Sequotchie [sic] | H | p.10 l.19 (564) L |
| Amber | Savannah | H | p.10 l.19 (564) R |
| Andes | Shallow Fork | H | p.10 l.20 (564) L |
| Anchor | Tar R | H | p.10 l.20 (564) R |
| Arctic | Tombigbee | H | p.10 l.21 (564) L |
| Angel | Tallapoosa | H | p.10 l.21 (564) R |
| Appian | Tennessee | H | p.10 l.22 (564) L |
| Animal | Tennessee | H | p.10 l.22 (564) R |
| Atlas | White R | H | p.10 l.23 (564) L |
| Annal | Potomac | H | p.10 l.23 (564) R |
| Alamo | York | H | p.10 l.24 (564) L |
| Armada | Yazoo | H | p.10 l.24 (564) R |
| Akron | Cumberland | H | p.10 l.25 (564) L |
| Anvil | Cumberland | H | p.10 l.25 (564) R |
| Adair | Tennessee | H | p.10 l.26 (564) L |
| Apple | Tennessee | H | p.10 l.26 (564) R |

### page 11 (565)

| code word | meaning | grade | source |
|---|---|---|---|
| (l.0: heading "States" written in the top margin above the first printed line) | - | H | p.11 l.0 (565) |
| Archery | Alabama | H | p.11 l.1 (565) L |
| Ark | Arizona | H | p.11 l.1 (565) R |
| Asp | Arkansas | H | p.11 l.2 (565) L |
| Axis | Connecticut | H | p.11 l.2 (565) R |
| Alkali | California | H | p.11 l.3 (565) L |
| Attica | Delaware | H | p.11 l.3 (565) R |
| Applause | Florida | H | p.11 l.4 (565) L |
| Abortion | Georgia | H | p.11 l.4 (565) R |
| Adorn | Indiana | H | p.11 l.5 (565) L |
| Agate | Illinois | H | p.11 l.5 (565) R |
| Alias | Iowa | H | p.11 l.6 (565) L |
| Amen | Kansas | H | p.11 l.6 (565) R |
| Abbey | Kentucky | H | p.11 l.7 (565) L |
| Audit | Louisiana | H | p.11 l.7 (565) R |
| Babel | Maine | H | p.11 l.8 (565) L |
| Baden | Massachusetts | H | p.11 l.8 (565) R |
| Baltic | Maryland | H | p.11 l.9 (565) L |
| Berlin | Mississippi | H | p.11 l.9 (565) R |
| Bremen | Missouri | H | p.11 l.10 (565) L |
| Brussels | Michigan | H | p.11 l.10 (565) R |
| Bangor | Minnesota | H | p.11 l.11 (565) L |
| Bengal | New York | H | p.11 l.11 (565) R |
| Bagdad | New Jersey | H | p.11 l.12 (565) L |
| Bethel | New Hampshire | H | p.11 l.12 (565) R |
| Bedford | North Carolina | H | p.11 l.13 (565) L |
| Biscay | Ohio | H | p.11 l.13 (565) R |
| Bergen | Pennsylvania | H | p.11 l.14 (565) L |
| Bomba | Rhode Island | H | p.11 l.14 (565) R |
| Botany | South Carolina | H | p.11 l.15 (565) L |
| Bourbon | Tennessee | H | p.11 l.15 (565) R |
| Belgium | Texas | H | p.11 l.16 (565) L |
| Bermuda | Virginia | H | p.11 l.16 (565) R |
| Berkshire | Vermont | H | p.11 l.17 (565) L |
| Belgrade | Wisconsin | H | p.11 l.17 (565) R |
| (line 18: heading Forts; printed code words Bologna and Bolivia struck through) | - | H | p.11 l.18 (565) |
| Bruno | Donaldson | H | p.11 l.19 (565) L |
| Brutus | Delaware | H | p.11 l.19 (565) R |
| Byron | Magruder | H | p.11 l.20 (565) L |
| Bunyan | Monroe | H | p.11 l.20 (565) R |
| Burton | McHenry | H | p.11 l.21 (565) L |
| Buxton | Sumter | H | p.11 l.21 (565) R |
| Barnard | President of U.S. | H | p.11 l.22 (565) L |
| Balfour | President of U.S. | H | p.11 l.22 (565) R |
| Beach | Secretary of War | H | p.11 l.23 (565) L |
| Barton | Secretary of War | H | p.11 l.23 (565) R |
| Bender | Secretary of Treasury | H | p.11 l.24 (565) L |
| Belcher | Secretary of Treasury | H | p.11 l.24 (565) R |
| Benjamin | Secretary of Navy | H | p.11 l.25 (565) L |
| Bennet | Secretary of Navy | H | p.11 l.25 (565) R |
| Borgia | Secretary of State | H | p.11 l.26 (565) L |
| Berry | Secretary of State | H | p.11 l.26 (565) R |

### page 12 (570)

| code word | meaning | grade | source |
|---|---|---|---|
| (l.0: heading "Places and Generals" written in the top margin above the first printed line) | - | H | p.12 l.0 (570) |
| Bethune | Abingdon | H | p.12 l.1 (570) L |
| Blanchard | Abingdon | H | p.12 l.1 (570) R |
| Bigelow | Augusta | H | p.12 l.2 (570) L |
| Bolton | Augusta | H | p.12 l.2 (570) R |
| Bonner | Atlanta | H | p.12 l.3 (570) L |
| Bishop | Atlanta | H | p.12 l.3 (570) R |
| Baboon | Athens | H | p.12 l.4 (570) L |
| Badger | Athens | H | p.12 l.4 (570) R |
| Banjo | Alexandria | H | p.12 l.5 (570) L |
| Barber | Alexandria | H | p.12 l.5 (570) R |
| Bard | Baltimore | H | p.12 l.6 (570) L |
| Baron | Baltimore | H | p.12 l.6 (570) R |
| Ballad | Battle Creek | H | p.12 l.7 (570) L |
| Balmoral | Battle Creek | H | p.12 l.7 (570) R |
| Banditti | Baton Rouge | H | p.12 l.8 (570) L |
| Baptism | Baton Rouge | H | p.12 l.8 (570) R |
| Bible | Beaufort | H | p.12 l.9 (570) L |
| Basement | Beaufort | H | p.12 l.9 (570) R |
| Bassoon | Bellefonte | H | p.12 l.10 (570) L |
| Beadle | Bellefonte | H | p.12 l.10 (570) R |
| Beacon | Bridgeport | H | p.12 l.11 (570) L |
| Bear | Bridgeport | H | p.12 l.11 (570) R |
| Beauty | Bowling Green | H | p.12 l.12 (570) L |
| Beaver | Bowling Green | H | p.12 l.12 (570) R |
| Bigamy | Cahawba | H | p.12 l.13 (570) L |
| Bigot | Cahawba | H | p.12 l.13 (570) R |
| Bladder | Calhoun | H | p.12 l.14 (570) L |
| Bleaching | Calhoun | H | p.12 l.14 (570) R |
| Black | Cairo | H | p.12 l.15 (570) L |
| Blubber | Cairo | H | p.12 l.15 (570) R |
| Bogus | Charleston | H | p.12 l.16 (570) L |
| Booby | Charleston | H | p.12 l.16 (570) R |
| Brandy | Charlottsville [sic] | H | p.12 l.17 (570) L |
| Bravo | Charlottsville [sic] | H | p.12 l.17 (570) R |
| Bridle | City Point | H | p.12 l.18 (570) L |
| Brimstone | City Point | H | p.12 l.18 (570) R |
| Brocade | Cincinnati | H | p.12 l.19 (570) L |
| Bromley | Cincinnati | H | p.12 l.19 (570) R |
| Budget | Chattanooga | H | p.12 l.20 (570) L |
| Buffet | Chattanooga | H | p.12 l.20 (570) R |
| Burglar | Quarter[?] Master General | H | p.12 l.21 (570) L |
| Buggy | Quarter[?] Master General | H | p.12 l.21 (570) R |
| Bargain | Adjutant General | H | p.12 l.22 (570) L |
| Basket | Adjutant General | H | p.12 l.22 (570) R |
| Battle | Maj Gen H W Halleck | H | p.12 l.23 (570) L |
| Behead | Maj Gen H W Halleck | H | p.12 l.23 (570) R |
| Bellows | Maj Genl U S Grant | H | p.12 l.24 (570) L |
| Belly | Maj Genl U S Grant | H | p.12 l.24 (570) R |
| Berth | Maj Gen G G Meade | H | p.12 l.25 (570) L |
| Biped | Maj Gen G G Meade | H | p.12 l.25 (570) R |
| Blossom | Maj Gen A E Burnside | H | p.12 l.26 (570) L |
| Bracket | Maj Gen A E Burnside | H | p.12 l.26 (570) R |

### page 13 (571)

| code word | meaning | grade | source |
|---|---|---|---|
| (l.0: heading "Places and Generals" written in the top margin above the first printed line) | - | H | p.13 l.0 (571) |
| Camden | Corinth | H | p.13 l.1 (571) L |
| Cadmus | Corinth | H | p.13 l.1 (571) R |
| Clarence | Columbus | H | p.13 l.2 (571) L |
| Claudius | Columbus | H | p.13 l.2 (571) R |
| Coburg | Cleveland | H | p.13 l.3 (571) L |
| Cognac | Cleveland | H | p.13 l.3 (571) R |
| Columbia | Clarksburg | H | p.13 l.4 (571) L |
| California | Clarksburg | H | p.13 l.4 (571) R |
| Chester | Culpepper | H | p.13 l.5 (571) L |
| Carroll | Culpepper | H | p.13 l.5 (571) R |
| Clifton | Cumberland Gap | H | p.13 l.6 (571) L |
| Carthage | Cumberland Gap | H | p.13 l.6 (571) R |
| Cuba | Dalton | H | p.13 l.7 (571) L |
| Champlain | Dalton | H | p.13 l.7 (571) R |
| Cheshire | Danville | H | p.13 l.8 (571) L |
| Clyde | Danville | H | p.13 l.8 (571) R |
| China | Decatur | H | p.13 l.9 (571) L |
| Catawba | Decatur | H | p.13 l.9 (571) R |
| Camargo | Decherd | H | p.13 l.10 (571) L |
| Census | Decherd | H | p.13 l.10 (571) R |
| Century | Elizabeth City | H | p.13 l.11 (571) L |
| Cedar | Elizabeth City | H | p.13 l.11 (571) R |
| Castor | Fredericksburg | H | p.13 l.12 (571) L |
| Cologne | Fredericksburg | H | p.13 l.12 (571) R |
| Carbon | Fort Valley | H | p.13 l.13 (571) L |
| Carpet | Fort Valley | H | p.13 l.13 (571) R |
| Cancer | Florence | H | p.13 l.14 (571) L |
| Camel | Florence | H | p.13 l.14 (571) R |
| Canary | Galveston | H | p.13 l.15 (571) L |
| Camphor | Galveston | H | p.13 l.15 (571) R |
| Calendar | Goldsboro | H | p.13 l.16 (571) L |
| Cabbage | Goldsboro | H | p.13 l.16 (571) R |
| Charity | Gordonsville | H | p.13 l.17 (571) L |
| Cherry | Gordonsville | H | p.13 l.17 (571) R |
| Chicken | Grenada | H | p.13 l.18 (571) L |
| Children | Grenada | H | p.13 l.18 (571) R |
| Chorus | Grand Junction | H | p.13 l.19 (571) L |
| Clam | Grand Junction | H | p.13 l.19 (571) R |
| Climax | Hanover | H | p.13 l.20 (571) L |
| Cider | Hanover | H | p.13 l.20 (571) R |
| Churn | Harpers Ferry | H | p.13 l.21 (571) L |
| Chapel | Harpers Ferry | H | p.13 l.21 (571) R |
| College | President U.S. | H | p.13 l.22 (571) L |
| Color | President U.S. | H | p.13 l.22 (571) R |
| Comet | Maj Genl H W Halleck | H | p.13 l.23 (571) L |
| Cupid | Maj Genl H W Halleck | H | p.13 l.23 (571) R |
| Costume | Secretary of War | H | p.13 l.24 (571) L |
| Comb | Secretary of War | H | p.13 l.24 (571) R |
| Corunna | Maj Gen N P Banks | H | p.13 l.25 (571) L |
| Cherub | Maj Gen N P Banks | H | p.13 l.25 (571) R |
| Chart | Lieut Gen U.S. Grant | H | p.13 l.26 (571) L |
| Crowd | Lieut Gen U.S. Grant | H | p.13 l.26 (571) R |

### page 14 (572)

| code word | meaning | grade | source |
|---|---|---|---|
| (l.0: heading "Places and Generals" written in the top margin above the first printed line) | - | H | p.14 l.0 (572) |
| David | Helena | H | p.14 l.1 (572) L |
| Daniel | Helena | H | p.14 l.1 (572) R |
| Denmark | Holly Springs | H | p.14 l.2 (572) L |
| Danube | Holly Springs | H | p.14 l.2 (572) R |
| Darby | Humboldt | H | p.14 l.3 (572) L |
| Dalton | Humboldt | H | p.14 l.3 (572) R |
| Dresden | Huntsville | H | p.14 l.4 (572) L |
| Dryden | Huntsville | H | p.14 l.4 (572) R |
| Dolphin | Independence | H | p.14 l.5 (572) L |
| Dragon | Independence | H | p.14 l.5 (572) R |
| Damon | Indianapolis | H | p.14 l.6 (572) L |
| Dublin | Indianapolis | H | p.14 l.6 (572) R |
| Durham | Jackson | H | p.14 l.7 (572) L |
| Diana | Jackson | H | p.14 l.7 (572) R |
| Dawn | Jasper | H | p.14 l.8 (572) L |
| Devon | Jasper | H | p.14 l.8 (572) R |
| Domain | Jacksonville | H | p.14 l.9 (572) L |
| Dropsy | Jacksonville | H | p.14 l.9 (572) R |
| Damask | Jefferson | H | p.14 l.10 (572) L |
| Dimple | Jefferson | H | p.14 l.10 (572) R |
| Dagger | Kingston | H | p.14 l.11 (572) L |
| Darling | Kingston | H | p.14 l.11 (572) R |
| Dauphin | Knoxville | H | p.14 l.12 (572) L |
| Dentist | Knoxville | H | p.14 l.12 (572) R |
| Dirge | Kingsville | H | p.14 l.13 (572) L |
| Discount | Kingsville | H | p.14 l.13 (572) R |
| Dismal | Kingsville | H | p.14 l.14 (572) L |
| Divine | Kingsville | H | p.14 l.14 (572) R |
| Docket | Lafayette | H | p.14 l.15 (572) L |
| Dodge | Lafayette | H | p.14 l.15 (572) R |
| Drill | Larkinsville | H | p.14 l.16 (572) L |
| Drum | Larkinsville | H | p.14 l.16 (572) R |
| Duke | La Grange | H | p.14 l.17 (572) L |
| Duchess | La Grange | H | p.14 l.17 (572) R |
| Dungeon | Lebanon | H | p.14 l.18 (572) L |
| Dumps | Lebanon | H | p.14 l.18 (572) R |
| Europe | Louisa C H | H | p.14 l.19 (572) L |
| Empire | Louisa C H | H | p.14 l.19 (572) R |
| Egypt | Louisville | H | p.14 l.20 (572) L |
| Emblem | Louisville | H | p.14 l.20 (572) R |
| Eagle | London | H | p.14 l.21 (572) L |
| Essex | London | H | p.14 l.21 (572) R |
| Eddy | Lynchburg | H | p.14 l.22 (572) L |
| Emmet | Lynchburg | H | p.14 l.22 (572) R |
| Empress | General in Chief | H | p.14 l.23 (572) L |
| Embrace | General in Chief | H | p.14 l.23 (572) R |
| Falcon | Maj Gen G H Thomas | H | p.14 l.24 (572) L |
| Finland | Maj Gen G H Thomas | H | p.14 l.24 (572) R |
| Flora | Maj Gen W T Sherman | H | p.14 l.25 (572) L |
| Fortune | Maj Gen W T Sherman | H | p.14 l.25 (572) R |
| Farmer | Maj Gen E R S Canby | H | p.14 l.26 (572) L |
| Famish | Maj Gen E R S Canby | H | p.14 l.26 (572) R |

### page 15 (573)

| code word | meaning | grade | source |
|---|---|---|---|
| (l.0: heading "Places and Generals" written in the top margin above the first printed line) | - | H | p.15 l.0 (573) |
| France | Macon | H | p.15 l.1 (573) L |
| Frog | Macon | H | p.15 l.1 (573) R |
| Feather | Madison | H | p.15 l.2 (573) L |
| Filter | Madison | H | p.15 l.2 (573) R |
| Fladners | Marietta | H | p.15 l.3 (573) L |
| Flannel | Marietta | H | p.15 l.3 (573) R |
| Flint | Martinsburg | H | p.15 l.4 (573) L |
| Florida | Martinsburg | H | p.15 l.4 (573) R |
| Fool | McMinnville | H | p.15 l.5 (573) L |
| Fox | McMinnville | H | p.15 l.5 (573) R |
| Fork | Memphis | H | p.15 l.6 (573) L |
| Fraction | Memphis | H | p.15 l.6 (573) R |
| Gideon | Meridian | H | p.15 l.7 (573) L |
| Gabriel | Meridian | H | p.15 l.7 (573) R |
| Gotham | Milledgeville | H | p.15 l.8 (573) L |
| Galena | Milledgeville | H | p.15 l.8 (573) R |
| Galway | Mobile | H | p.15 l.9 (573) L |
| Garden | Mobile | H | p.15 l.9 (573) R |
| Gallon | Montgomery | H | p.15 l.10 (573) L |
| Gourd | Montgomery | H | p.15 l.10 (573) R |
| Garter | Murfreesboro | H | p.15 l.11 (573) L |
| Germany | Murfreesboro | H | p.15 l.11 (573) R |
| Georgia | Natchez | H | p.15 l.12 (573) L |
| Genoa | Natchez | H | p.15 l.12 (573) R |
| Geneva | Nashville | H | p.15 l.13 (573) L |
| Gaul | Nashville | H | p.15 l.13 (573) R |
| Gem | Newberne | H | p.15 l.14 (573) L |
| Ginseng | Newberne | H | p.15 l.14 (573) R |
| Ginger | New Orleans | H | p.15 l.15 (573) L |
| Gland | New Orleans | H | p.15 l.15 (573) R |
| Girdle | New York | H | p.15 l.16 (573) L |
| Granada | New York | H | p.15 l.16 (573) R |
| Glasgow | Norfolk | H | p.15 l.17 (573) L |
| Gilead | Norfolk | H | p.15 l.17 (573) R |
| Globe | Opelika | H | p.15 l.18 (573) L |
| Glover | Opelika | H | p.15 l.18 (573) R |
| Golden | Orange C.H | H | p.15 l.19 (573) L |
| Goose | Orange C.H | H | p.15 l.19 (573) R |
| Gondola | Petersburg | H | p.15 l.20 (573) L |
| Granby | Petersburg | H | p.15 l.20 (573) R |
| Grammar | Philadelphia | H | p.15 l.21 (573) L |
| Gregory | Philadelphia | H | p.15 l.21 (573) R |
| Godwin | Port Royal | H | p.15 l.22 (573) L |
| Gliddon | Port Royal | H | p.15 l.22 (573) R |
| Griffin | Maj Gen R. C. Schenck | H | p.15 l.23 (573) L |
| Gifford | Maj Gen R. C. Schenck | H | p.15 l.23 (573) R |
| Guns | Maj Gen J G Foster | H | p.15 l.24 (573) L |
| Girls | Maj Gen J G Foster | H | p.15 l.24 (573) R |
| Grapes | Maj Gen B. F. Butler | H | p.15 l.25 (573) L |
| Growl | Maj Gen B. F. Butler | H | p.15 l.25 (573) R |
| Grub | Maj Gen G G Meade | H | p.15 l.26 (573) L |
| Grunt | Maj Gen G G Meade | H | p.15 l.26 (573) R |

# Pass B transcription, Cipher No. 2 (mssEC 47), pages 16-21 (pointers 574-579)

Read from the 1600 px JPEGs and from 2400 px full-page IIIF images
(`https://hdl.huntington.org/digital/iiif/p16003coll11/<pointer>/full/2400,/0/default.jpg`; the server ignores
region requests and returns the full page) cropped locally, 20 Sept 2026. Line numbers count the 26 printed
lines from the top printed line; handwritten additions are l.0 (above the first printed line) or l.27 (below the
last). A page heading written by hand above the first printed line is noted but not numbered. Where a line is
divided by a red vertical rule, a handwritten brace `}` or a red bar, L and R carry different meanings; otherwise
both code words carry the one meaning. "[#]" after a meaning means the `#` inflection mark stands against that
code word (each page's foot-note reads `# Add "ed" or "ing" to Arbitrary`).

### page 16 (574)

Heading (handwritten, above l.1): "Places Concluded".

| code word | meaning | grade | source |
|---|---|---|---|
| Hagar | Raleigh | H | p.16 l.1 (574) L |
| Homer | Raleigh | H | p.16 l.1 (574) R |
| Horace | Richmond | H | p.16 l.2 (574) L |
| Harvey | Richmond | H | p.16 l.2 (574) R |
| Hamlet | Rome | H | p.16 l.3 (574) L |
| Hannibal | Rome | H | p.16 l.3 (574) R |
| Hebrew | Savannah | H | p.16 l.4 (574) L |
| Hindoo | Savannah | H | p.16 l.4 (574) R |
| Harvard | Selma | H | p.16 l.5 (574) L |
| Humboldt | Selma | H | p.16 l.5 (574) R |
| Hastings | Shelbyville | H | p.16 l.6 (574) L |
| Haven | Shelbyville | H | p.16 l.6 (574) R |
| Harlem | Sparta | H | p.16 l.7 (574) L |
| Hampden | Sparta | H | p.16 l.7 (574) R |
| Holland | St Louis | H | p.16 l.8 (574) L |
| Honduras | St Louis | H | p.16 l.8 (574) R |
| Hungary | Stevenson | H | p.16 l.9 (574) L |
| Hunger | Stevenson | H | p.16 l.9 (574) R |
| Hayti | Suffolk | H | p.16 l.10 (574) L |
| Helix | Suffolk | H | p.16 l.10 (574) R |
| Hemlock | Summerville | H | p.16 l.11 (574) L |
| Hemp | Summerville | H | p.16 l.11 (574) R |
| Hymen | Talladega | H | p.16 l.12 (574) L |
| Hair | Talladega | H | p.16 l.12 (574) R |
| Herald | Trenton | H | p.16 l.13 (574) L |
| Harp | Trenton | H | p.16 l.13 (574) R |
| Highness | Tullahoma | H | p.16 l.14 (574) L |
| History | Tullahoma | H | p.16 l.14 (574) R |
| Hosanna | Tuscumbia | H | p.16 l.15 (574) L |
| Husband | Tuscumbia | H | p.16 l.15 (574) R |
| Hammock | Tuscaloosa | H | p.16 l.16 (574) L |
| Hammer | Tuscaloosa | H | p.16 l.16 (574) R |
| Holly | Vicksburg | H | p.16 l.17 (574) L |
| Hero | Vicksburg | H | p.16 l.17 (574) R |
| Huron | Washington | H | p.16 l.18 (574) L |
| Hang | Washington | H | p.16 l.18 (574) R |
| Hunter | Washington | H | p.16 l.19 (574) L |
| Happy | Washington | H | p.16 l.19 (574) R |
| Harlot | Warrenton | H | p.16 l.20 (574) L |
| Hatchet | Warrenton | H | p.16 l.20 (574) R |
| Hoax | Weldon | H | p.16 l.21 (574) L |
| Hotel | Weldon | H | p.16 l.21 (574) R |
| Humbug | West Point | H | p.16 l.22 (574) L |
| Huckster | West Point | H | p.16 l.22 (574) R |
| Haddock | Wilmington | H | p.16 l.23 (574) L |
| Humphrey | Wilmington | H | p.16 l.23 (574) R |
| Harmony | Williamsburg | H | p.16 l.24 (574) L |
| Hawley | Williamsburg | H | p.16 l.24 (574) R |
| Honey | Winchester | H | p.16 l.25 (574) L |
| Humble | Winchester | H | p.16 l.25 (574) R |
| Hug | Yorktown | H | p.16 l.26 (574) L |
| Hulk | Yorktown | H | p.16 l.26 (574) R |

### page 17 (575)

Heading (handwritten, above l.1): "Rebel Generals".

| code word | meaning | grade | source |
|---|---|---|---|
| Ida | Beauregard | H | p.17 l.1 (575) L |
| Ink | Beauregard | H | p.17 l.1 (575) R |
| Irving | Bragg | H | p.17 l.2 (575) L |
| Ingress | Bragg | H | p.17 l.2 (575) R |
| Ingrate | Breckenridge | H | p.17 l.3 (575) L |
| Ingot | Breckenridge | H | p.17 l.3 (575) R |
| India | Buckner | H | p.17 l.4 (575) L |
| Indus | Buckner | H | p.17 l.4 (575) R |
| Indigo | Chalmers | H | p.17 l.5 (575) L |
| Infant | Chalmers | H | p.17 l.5 (575) R |
| Image | Cheatham | H | p.17 l.6 (575) L |
| Insanity | Cheatham | H | p.17 l.6 (575) R |
| Ireland | Ewell | H | p.17 l.7 (575) L |
| Italy | Ewell | H | p.17 l.7 (575) R |
| Indians (printed "Indiana", last letters overwritten by hand to "ns") | Echols | H | p.17 l.8 (575) L |
| Ivory | Echols | H | p.17 l.8 (575) R |
| Jacob | Hill | H | p.17 l.9 (575) L |
| Jasper | Hill | H | p.17 l.9 (575) R |
| Jonah | Hardee | H | p.17 l.10 (575) L |
| Jordan | Hardee | H | p.17 l.10 (575) R |
| Judah | Imboden | H | p.17 l.11 (575) L |
| John | Imboden | H | p.17 l.11 (575) R |
| Juno | Jenkins | H | p.17 l.12 (575) L |
| Jupiter | Lomax | H | p.17 l.12 (575) R |
| Japan | Jeff Davis | H | p.17 l.13 (575) L |
| Jersey | Jeff Davis | H | p.17 l.13 (575) R |
| Jasmine | Jones | H | p.17 l.14 (575) L |
| Jew (printed code word struck through in black ink, illegible; "Jew" written above it in black ink) | Jones | H | p.17 l.14 (575) R |
| Java | Johnston | H | p.17 l.15 (575) L |
| Jamaica | Johnston | H | p.17 l.15 (575) R |
| Jargon | Kirby Smith | H | p.17 l.16 (575) L |
| Jaundice | Kirby Smith | H | p.17 l.16 (575) R |
| Jaunt | Lee | H | p.17 l.17 (575) L |
| Javelin | Lee | H | p.17 l.17 (575) R |
| Jolly | Loring | H | p.17 l.18 (575) L |
| Journal | Kershaw | H | p.17 l.18 (575) R |
| Kettle | Longstreet | H | p.17 l.19 (575) L |
| Kindle | Longstreet | H | p.17 l.19 (575) R |
| King | Marmaduke | H | p.17 l.20 (575) L |
| Kingdom | Marmaduke | H | p.17 l.20 (575) R |
| Kitten | Pemberton | H | p.17 l.21 (575) L |
| Kiss | Pemberton | H | p.17 l.21 (575) R |
| Knell | Price | H | p.17 l.22 (575) L |
| Knight | Price | H | p.17 l.22 (575) R |
| Koran | Stevenson | H | p.17 l.23 (575) L |
| Kennet | Rosser | H | p.17 l.23 (575) R |
| Kennebec | Roddy | H | p.17 l.24 (575) L |
| Kidnap | Rhodes | H | p.17 l.24 (575) R |
| Knapsack | Walker | H | p.17 l.25 (575) L |
| Kitchen | Walker | H | p.17 l.25 (575) R |
| Kasson | Wheeler | H | p.17 l.26 (575) L |
| Kunkle | Wheeler | H | p.17 l.26 (575) R |
| Kearsarge (handwritten) | Hood | H | p.17 l.27 (575) L |
| Kossuth (handwritten) | Hood | H | p.17 l.27 (575) R |
| Kirkwood (handwritten) | Early | H | p.17 l.28 (575) L |
| Kerner (handwritten) | Early | H | p.17 l.28 (575) R |

### page 18 (576)

Heading (handwritten, above l.1): "Generals". A red vertical rule divides the column on most lines; it is
interrupted at l.1, l.13, l.17 and l.19-21, where one name spans the line.

| code word | meaning | grade | source |
|---|---|---|---|
| Lady | H W Halleck | H | p.18 l.1 (576) L |
| Lamb | H W Halleck | H | p.18 l.1 (576) R |
| Lantern | Augur C C | H | p.18 l.2 (576) L |
| Lafitte | Averill W W | H | p.18 l.2 (576) R |
| Lapland | Banks N P | H | p.18 l.3 (576) L |
| Language | Butterfield D | H | p.18 l.3 (576) R |
| Lark | Blair F P | H | p.18 l.4 (576) L |
| Lawn | Burnside A E | H | p.18 l.4 (576) R |
| Leghorn | Buford | H | p.18 l.5 (576) L |
| Legend | Butler B F | H | p.18 l.5 (576) R |
| Lehigh | Brannon [sic] J M | H | p.18 l.6 (576) L |
| Leopard | Boyle J T | H | p.18 l.6 (576) R |
| Liberia | Brooks W T H | H | p.18 l.7 (576) L |
| Lobster | Couch D N | H | p.18 l.7 (576) R |
| Lock | Dix Jno A | H | p.18 l.8 (576) L |
| Locust | Dana N J T | H | p.18 l.8 (576) R |
| Logan | French W H | H | p.18 l.9 (576) L |
| Luther | Foster J G | H | p.18 l.9 (576) R |
| Luna | Franklin W B | H | p.18 l.10 (576) L |
| Limpid | Getty G W | H | p.18 l.10 (576) R |
| Lonesome | Gillmore Q A | H | p.18 l.11 (576) L |
| Lester | Granger R S | H | p.18 l.11 (576) R |
| Magnet | Granger G | H | p.18 l.12 (576) L |
| Madder | Geary J W | H | p.18 l.12 (576) R |
| Madrid | Grant U S | H | p.18 l.13 (576) L |
| Magic | Grant U S | H | p.18 l.13 (576) R |
| Magnolia | Hartsuff G L [?] | H | p.18 l.14 (576) L |
| Malta | Hooker Jos | H | p.18 l.14 (576) R |
| Mastiff | Canby Ed R S | H | p.18 l.15 (576) L |
| Melon | Heintzelman S P | H | p.18 l.15 (576) R |
| Mentor | Howard O O | H | p.18 l.16 (576) L |
| Meriden | Hunter D | H | p.18 l.16 (576) R |
| Merlin | Kelly B F | H | p.18 l.17 (576) L |
| Midas | Kelly B F | H | p.18 l.17 (576) R |
| Milan | Kilpatrick J | H | p.18 l.18 (576) L |
| Milk | Lockwood H H | H | p.18 l.18 (576) R |
| Mint | Logan Jno A | H | p.18 l.19 (576) L |
| Mogul | Logan Jno A | H | p.18 l.19 (576) R |
| Mohawk | Meade G G | H | p.18 l.20 (576) L |
| Monarch | Meade G G | H | p.18 l.20 (576) R |
| Monster | McPherson J B | H | p.18 l.21 (576) L |
| Montrose | McPherson J B | H | p.18 l.21 (576) R |
| Moon | Negley J S | H | p.18 l.22 (576) L |
| Moscow | Ord E O C | H | p.18 l.22 (576) R |
| Myrtle | Prentiss B M | H | p.18 l.23 (576) L |
| Mystic | Pope John | H | p.18 l.23 (576) R |
| Maroon | Parke J G | H | p.18 l.24 (576) L |
| Mellow | Palmer J M | H | p.18 l.24 (576) R |
| Music | Quinby I F [?] | H | p.18 l.25 (576) L |
| Maxim | Reynolds J J | H | p.18 l.25 (576) R |
| Mud | Rosecrans W S | H | p.18 l.26 (576) L |
| Muss | Rosseau [sic] L H | H | p.18 l.26 (576) R |
| Monk (handwritten) | Schofield J M | H | p.18 l.27 (576) L |
| Monkey (handwritten) | Schofield J M | H | p.18 l.27 (576) R |

### page 19 (577)

Heading (handwritten, above l.1): "Generals . Admirals and Miscellaneous" ("and" written small above the line).
A red vertical rule divides the column on most lines; lines 12-13 are boxed in red with a handwritten brace on
each side and the marginal label "Rear Admirals" in red ink, written vertically.

| code word | meaning | grade | source |
|---|---|---|---|
| Nabob | Schenck R C | H | p.19 l.1 (577) L |
| Nankin | Schenck R C | H | p.19 l.1 (577) R |
| Naples | Saunders | H | p.19 l.2 (577) L |
| Nero | Sickles D E | H | p.19 l.2 (577) R |
| Nestor | Sedgwick Jno | H | p.19 l.3 (577) L |
| Nettle | Scammon E P | H | p.19 l.3 (577) R |
| Neptune | Sigel F | H | p.19 l.4 (577) L |
| Negus | Sheridan P H | H | p.19 l.4 (577) R |
| Niagara | Slocum H W | H | p.19 l.5 (577) L |
| Nile | Shackleford J M | H | p.19 l.5 (577) R |
| Nose | Sullivan J C | H | p.19 l.6 (577) L |
| Nasty | Stoneman Geo | H | p.19 l.6 (577) R |
| Nutmeg | Steele Fdk | H | p.19 l.7 (577) L |
| Nugget | Stahel Jul | H | p.19 l.7 (577) R |
| Nuptial | Smith | H | p.19 l.8 (577) L |
| Negro | Steidman [sic] J B | H | p.19 l.8 (577) R |
| Niggard | Thomas Geo H | H | p.19 l.9 (577) L |
| Nuisance | Thomas Geo H | H | p.19 l.9 (577) R |
| Nurse | Van Cleve H P | H | p.19 l.10 (577) L |
| Nymph | Warren G K | H | p.19 l.10 (577) R |
| Opal | Wallace Lew | H | p.19 l.11 (577) L |
| Oyster | Washburn C C | H | p.19 l.11 (577) R |
| Offal | Dahlgren J A | H | p.19 l.12 (577) L |
| Olive | Farragut D G | H | p.19 l.12 (577) R |
| Oakum | Lee S P | H | p.19 l.13 (577) L |
| Odor | Porter D D | H | p.19 l.13 (577) R |
| Oats | Abandon (-ed, -ing) | H | p.19 l.14 (577) L |
| Oil | Abandon (-ed, -ing) [#] | H | p.19 l.14 (577) R |
| Optic | Available | H | p.19 l.15 (577) L |
| Orbit | Arms | H | p.19 l.15 (577) R |
| Orchard | Arrest (-ed, -ing) | H | p.19 l.16 (577) L |
| Owl | Arrest (-ed, -ing) [#] | H | p.19 l.16 (577) R |
| Oxide | At the | H | p.19 l.17 (577) L |
| Ordnance | After the | H | p.19 l.17 (577) R |
| Peru | Army | H | p.19 l.18 (577) L |
| Persia | Army | H | p.19 l.18 (577) R |
| Pagan | Artillery | H | p.19 l.19 (577) L |
| Pagoda | Artillery | H | p.19 l.19 (577) R |
| Palate | Ammunition | H | p.19 l.20 (577) L |
| Palsy | Ammunition | H | p.19 l.20 (577) R |
| Panther | As soon as | H | p.19 l.21 (577) L |
| Pelican | By the way of | H | p.19 l.21 (577) R |
| Pardon | Attack (-ed, -ing) [#] | H | p.19 l.22 (577) L |
| Parson | Attack (-ed, -ing) | H | p.19 l.22 (577) R |
| Patent | Advance (-ed, -ing) [#] | H | p.19 l.23 (577) L |
| Patron | Advance (-ed, -ing) | H | p.19 l.23 (577) R |
| Peasant | Concentrate (-ed, -ing) | H | p.19 l.24 (577) L |
| Perfume | Concentrate (-ed, -ing) [#] | H | p.19 l.24 (577) R |
| Pewter | Bridge (-ed, -ing) | H | p.19 l.25 (577) L |
| Pilot | Bridge (-ed, -ing) [#] | H | p.19 l.25 (577) R |
| Princess | Battled [?] | H | p.19 l.26 (577) L |
| Pilgrim | Battled [?] | H | p.19 l.26 (577) R |

Foot-note (handwritten, below l.26): `# Add - "ed" or "ing" to Arbitrary`.

### page 20 (578)

Heading (handwritten, above l.1): "Miscellaneous". Red vertical rule on the divided lines only (l.4-5, 10,
14-16, 20, 23).

| code word | meaning | grade | source |
|---|---|---|---|
| Pacific | Battery | H | p.20 l.1 (578) L |
| Panama | Battery | H | p.20 l.1 (578) R |
| Palermo | Brig. General | H | p.20 l.2 (578) L |
| Palestine | Brig. General | H | p.20 l.2 (578) R |
| Palmetto | Brigade | H | p.20 l.3 (578) L |
| Palmyra | Brigade | H | p.20 l.3 (578) R |
| Pandora | Casualties | H | p.20 l.4 (578) L |
| Paradise | Cars | H | p.20 l.4 (578) R |
| Paulding | Convoy | H | p.20 l.5 (578) L |
| Pauline | Camp | H | p.20 l.5 (578) R |
| Paxton | Colonel | H | p.20 l.6 (578) L |
| Pearl | Colonel | H | p.20 l.6 (578) R |
| Pedlar | Cavalry | H | p.20 l.7 (578) L |
| Pekin | Cavalry | H | p.20 l.7 (578) R |
| Pelham | Corps | H | p.20 l.8 (578) L |
| Pelton | Corps | H | p.20 l.8 (578) R |
| Pembroke | Communications | H | p.20 l.9 (578) L |
| Penfield | Communications | H | p.20 l.9 (578) R |
| Pigeon | Cipher | H | p.20 l.10 (578) L |
| Pike | Comma | H | p.20 l.10 (578) R |
| Pine | Communicate (-ed, -ing) | H | p.20 l.11 (578) L |
| Plant | Communicate (-ed, -ing) [#] | H | p.20 l.11 (578) R |
| Plate | Capture (-ed, -ing) [#] | H | p.20 l.12 (578) L |
| Plainfield | Capture (-ed, -ing) | H | p.20 l.12 (578) R |
| Plum | Cross (-ed, -ing) | H | p.20 l.13 (578) L |
| Pocket | Cross (-ed, -ing) [#] | H | p.20 l.13 (578) R |
| Polk | Commander | H | p.20 l.14 (578) L |
| Pontiac | City | H | p.20 l.14 (578) R |
| Poplar | Citizen | H | p.20 l.15 (578) L |
| Portage | Country | H | p.20 l.15 (578) R |
| Prescott | Colored | H | p.20 l.16 (578) L |
| Preston | Cut off | H | p.20 l.16 (578) R |
| Princeton | Command (-ed, -ing) | H | p.20 l.17 (578) L |
| Prospect | Command (-ed, -ing) | H | p.20 l.17 (578) R |
| Putnam | Demoralize (-ed, -ing) | H | p.20 l.18 (578) L |
| Picket | Demoralize (-ed, -ing) | H | p.20 l.18 (578) R |
| Quaker | Division | H | p.20 l.19 (578) L |
| Queen | Division | H | p.20 l.19 (578) R |
| Quincy | Danger | H | p.20 l.20 (578) L |
| Quitman | Diversion | H | p.20 l.20 (578) R |
| Quiver | Destroy (-ed, -ing) [#] | H | p.20 l.21 (578) L |
| Quack | Destroy (-ed, -ing) | H | p.20 l.21 (578) R |
| Quadrant | Deserter | H | p.20 l.22 (578) L |
| Quadroon | Deserter | H | p.20 l.22 (578) R |
| Queenly | Depot | H | p.20 l.23 (578) L |
| Quotient | Department | H | p.20 l.23 (578) R |
| Quince | Defend (-ed, -ing) | H | p.20 l.24 (578) L |
| Question | Defend (-ed, -ing) [#] | H | p.20 l.24 (578) R |
| Query | Detach (-ed, -ing) | H | p.20 l.25 (578) L |
| Quicken (printed "Quick", "en" added by hand) | Detach (-ed, -ing) [#] | H | p.20 l.25 (578) R |
| Quorum | Defeat (-ed, -ing) | H | p.20 l.26 (578) L |
| Quarrel | Defeat (-ed, -ing) [#] | H | p.20 l.26 (578) R |

Foot-note (handwritten, below l.26): `# Add "ed" or ing to Arbitrary`.

### page 21 (579)

Heading (handwritten, above l.1): "Miscellaneous". Red vertical rule on the divided lines (l.0-1, 6, 8-10,
18-21, 25).

| code word | meaning | grade | source |
|---|---|---|---|
| Rape (handwritten) | Driving back | H | p.21 l.0 (579) L |
| Reproach (handwritten) | Driven back | H | p.21 l.0 (579) R |
| Randolph | Demonstration | H | p.21 l.1 (579) L |
| Raymond | Drove back | H | p.21 l.1 (579) R |
| Richard | Embark (-ed, -ing) | H | p.21 l.2 (579) L |
| Rodney | Embark (-ed, -ing) [#] | H | p.21 l.2 (579) R |
| Ramsay | Entrench (-ed, -ing) | H | p.21 l.3 (579) L |
| Ranson | Entrench (-ed, -ing) [#] | H | p.21 l.3 (579) R |
| Robin | Enemy | H | p.21 l.4 (579) L |
| Raven | Enemy | H | p.21 l.4 (579) R |
| Rabbit | Enemy | H | p.21 l.5 (579) L |
| Racine | Enemy | H | p.21 l.5 (579) R |
| Raleigh | Equipage | H | p.21 l.6 (579) L |
| Reading | Equiping [sic] | H | p.21 l.6 (579) R |
| Relay | Effect (-ed, -ing) [#] | H | p.21 l.7 (579) L |
| Roanoke | Effect (-ed, -ing) | H | p.21 l.7 (579) R |
| Ripley | Expedition | H | p.21 l.8 (579) L |
| Richland | Effective | H | p.21 l.8 (579) R |
| Ridge | Equipment | H | p.21 l.9 (579) L |
| Rome | Earthworks | H | p.21 l.9 (579) R |
| Rose | Engine | H | p.21 l.10 (579) L |
| Rockland | Engineer | H | p.21 l.10 (579) R |
| Roland | East | H | p.21 l.11 (579) L |
| Rubens | East | H | p.21 l.11 (579) R |
| Ramble | Evacuate (-ed, -ing) [#] | H | p.21 l.12 (579) L |
| Rampant | Evacuate (-ed, -ing) | H | p.21 l.12 (579) R |
| Rapture | Flank (-ed, -ing) [#] | H | p.21 l.13 (579) L |
| Ravish | Flank (-ed, -ing) [#] | H | p.21 l.13 (579) R |
| Reptile | Evacuation | H | p.21 l.14 (579) L |
| Ragged | Evacuation | H | p.21 l.14 (579) R |
| Retrench | Fight (-ing, Fought) [#] | H | p.21 l.15 (579) L |
| Review | Fight (-ing, Fought) [#] | H | p.21 l.15 (579) R |
| Reward | Follow (-ed, -ing) [#] | H | p.21 l.16 (579) L |
| Romance | Follow (-ed, -ing) | H | p.21 l.16 (579) R |
| Rusty | Forage (-ed, -ing) | H | p.21 l.17 (579) L |
| Ruffle | Forage (-ed, -ing) [#] | H | p.21 l.17 (579) R |
| Saco | Fort | H | p.21 l.18 (579) L |
| Salem | Force | H | p.21 l.18 (579) R |
| Saginaw | Favorable | H | p.21 l.19 (579) L |
| Scotland | Fork | H | p.21 l.19 (579) R |
| Sandy | Feint | H | p.21 l.20 (579) L |
| Saint | Force | H | p.21 l.20 (579) R |
| Saxon | Fear | H | p.21 l.21 (579) L |
| Savory | From the | H | p.21 l.21 (579) R |
| Sampson | Ferry | H | p.21 l.22 (579) L |
| Salmon | Ferry | H | p.21 l.22 (579) R |
| Seneca | Front | H | p.21 l.23 (579) L |
| Sexton | Front | H | p.21 l.23 (579) R |
| Saffron | Force | H | p.21 l.24 (579) L |
| Sable | Force | H | p.21 l.24 (579) R |
| Segment | Finding | H | p.21 l.25 (579) L |
| Seymour | Found | H | p.21 l.25 (579) R |
| Shade (printed "Shad", "e" added by hand) | Fall back (-ing back, fell back) [#] | H | p.21 l.26 (579) L |
| Shaker | Fall back (-ing back, fell back) | H | p.21 l.26 (579) R |
| Stop (handwritten) | Fortify (-ed, -ing, -cation) [#] | H | p.21 l.27 (579) L |
| Suggest (handwritten) | Fortify (-ed, -ing, -cation) [#] | H | p.21 l.27 (579) R |

Foot-note (handwritten, below l.27): `# Add "ed" or "ing" to Arbitrary`.

# Pass C: Cipher No. 2 (mssEC 47), pages 22-25, addenda [25A]-[25D], back fly leaves

Transcribed 20 Sept 2026 from the Huntington IIIF images (pointers 580-589), 1600 px overview
plus 2400-3000 px crops for every doubtful token. Grade H throughout (read from the key source).
Printed lines are numbered 1-26 from the top of each page; the "Miscellaneous" heading on pages
22-25 stands above line 1 and is not itself a ruled line, so every page has 26 printed lines and
52 code words. Undivided lines give both code words the one meaning.

### page 22 (580)

| code word | meaning | grade | source |
|---|---|---|---|
| Saddle | Guard (-ed, -ing) | H | p.22 l.1 (580) L |
| Shallow | Guard (-ed, -ing) | H | p.22 l.1 (580) R |
| Shannon | Gap | H | p.22 l.2 (580) L |
| Sharon | Gun | H | p.22 l.2 (580) R |
| Shark | General | H | p.22 l.3 (580) L |
| Spark | General | H | p.22 l.3 (580) R |
| Sharper | Government | H | p.22 l.4 (580) L |
| Sheffield | Gunboat | H | p.22 l.4 (580) R |
| Shelby | Harbor | H | p.22 l.5 (580) L |
| Shelter | Helping | H | p.22 l.5 (580) R |
| Shoal | Harass (-ed, -ing) | H | p.22 l.6 (580) L |
| Smoke | Harass (-ed, -ing) | H | p.22 l.6 (580) R |
| Silver | Horse | H | p.22 l.7 (580) L |
| Snake | Head Quarters | H | p.22 l.7 (580) R |
| Simms | Heavy | H | p.22 l.8 (580) L |
| Snow | Intercept (-ed, -ing) | H | p.22 l.8 (580) R |
| Soap | Has (or) have been reenforced | H | p.22 l.9 (580) L |
| Somers | Has (or) have been reenforced | H | p.22 l.9 (580) R |
| Spafford | Island | H | p.22 l.10 (580) L |
| Spartan | Impregnable | H | p.22 l.10 (580) R |
| Spencer | Information | H | p.22 l.11 (580) L |
| Spring | In the mean time [?] | H | p.22 l.11 (580) R |
| Shylock | In the | H | p.22 l.12 (580) L |
| Stanhope | Interrogation | H | p.22 l.12 (580) R |
| Spur | Invest (-ed, -ing) | H | p.22 l.13 (580) L |
| Spruce | Invest (-ed, -ing) | H | p.22 l.13 (580) R |
| Star | Infantry | H | p.22 l.14 (580) L |
| Sugar | Infantry | H | p.22 l.14 (580) R |
| Sulphur | Junction | H | p.22 l.15 (580) L |
| Squash | Infantry | H | p.22 l.15 (580) R |
| Sweden | Join | H | p.22 l.16 (580) L |
| Sutton | Joined | H | p.22 l.16 (580) R |
| Smyrna | Joining | H | p.22 l.17 (580) L |
| Sidney | Killed | H | p.22 l.17 (580) R |
| Sligo | Killing | H | p.22 l.18 (580) L |
| Stephen | Left | H | p.22 l.18 (580) R |
| Stanley | Missing | H | p.22 l.19 (580) L |
| Swallow | Light | H | p.22 l.19 (580) R |
| Summer | Men | H | p.22 l.20 (580) L |
| Summit | Marine | H | p.22 l.20 (580) R |
| Sylvan | Mile | H | p.22 l.21 (580) L |
| Steuben | Mountain | H | p.22 l.21 (580) R |
| Swindle | Move (-ed, -ing) | H | p.22 l.22 (580) L |
| Surgery | Movement | H | p.22 l.22 (580) R |
| Supper | Movement | H | p.22 l.23 (580) L |
| Superb | Movement | H | p.22 l.23 (580) R |
| Stomach | Necessary | H | p.22 l.24 (580) L |
| Stagger | Menace (-ed, -ing) | H | p.22 l.24 (580) R |
| Spunky | Major | H | p.22 l.25 (580) L |
| Squadron | North | H | p.22 l.25 (580) R |
| Spoon | North | H | p.22 l.26 (580) L |
| Spit | Near | H | p.22 l.26 (580) R |

### page 23 (581)

| code word | meaning | grade | source |
|---|---|---|---|
| Table | Organize (-ed, -ing) | H | p.23 l.1 (581) L |
| Tambour | Organize (-ed, -ing) | H | p.23 l.1 (581) R |
| Talbot | Of the | H | p.23 l.2 (581) L |
| Tanner | Over the | H | p.23 l.2 (581) R |
| Tappan | Our pickets | H | p.23 l.3 (581) L |
| Taunton | Our lines | H | p.23 l.3 (581) R |
| Taylor | Outpost | H | p.23 l.4 (581) L |
| Tankard | Parole | H | p.23 l.4 (581) R |
| Tarquin | Our scouts report | H | p.23 l.5 (581) L |
| Tartar | Our scouts report | H | p.23 l.5 (581) R |
| Trance | Outflank (-ed, -ing) | H | p.23 l.6 (581) L |
| Topple | Outflank (-ed, -ing) | H | p.23 l.6 (581) R |
| Torrent | Offensive | H | p.23 l.7 (581) L |
| Tremble | Open (-ed, -ing) | H | p.23 l.7 (581) R |
| Twinkle | Overtook (or taking) the Enemy | H | p.23 l.8 (581) L |
| Temple | Overtook (or taking) the Enemy | H | p.23 l.8 (581) R |
| Tinker | Position | H | p.23 l.9 (581) L |
| Tipton | Position | H | p.23 l.9 (581) R |
| Torch | Pursue (-ed, -ing) | H | p.23 l.10 (581) L |
| Tower | Pursue (-ed, -ing) | H | p.23 l.10 (581) R |
| Tracy | Picket (-ed, -ing) | H | p.23 l.11 (581) L |
| Trade | Picket (-ed, -ing) | H | p.23 l.11 (581) R |
| Tremont | Presence | H | p.23 l.12 (581) L |
| Trenton | Post | H | p.23 l.12 (581) R |
| Triangle | Pieces | H | p.23 l.13 (581) L |
| Trinity | Point | H | p.23 l.13 (581) R |
| Tulip | Period | H | p.23 l.14 (581) L |
| Turtle | Parenthesis | H | p.23 l.14 (581) R |
| Udder | Pontoon | H | p.23 l.15 (581) L |
| Umber | Pursuit | H | p.23 l.15 (581) R |
| Ursa | Practicable | H | p.23 l.16 (581) L |
| Upton | Pending | H | p.23 l.16 (581) R |
| Utophia | Re-enforce (-ed, -ing) | H | p.23 l.17 (581) L |
| Unite | Re-enforce (-ed, -ing) | H | p.23 l.17 (581) R |
| Valley | Quotation | H | p.23 l.18 (581) L |
| Vermont | Quarter Master | H | p.23 l.18 (581) R |
| Vernon | Reconnoissance | H | p.23 l.19 (581) L |
| Vermin | Reconnoissance | H | p.23 l.19 (581) R |
| Venus | Re-enforcements | H | p.23 l.20 (581) L |
| Vesper | Re-enforcements | H | p.23 l.20 (581) R |
| Vienna | Rebel | H | p.23 l.21 (581) L |
| Village | Rebel | H | p.23 l.21 (581) R |
| Virtue | Rear | H | p.23 l.22 (581) L |
| Vulcan | Resist | H | p.23 l.22 (581) R |
| Vulture | Retreat (-ed, -ing) | H | p.23 l.23 (581) L |
| Vomit | Retreat (-ed, -ing) | H | p.23 l.23 (581) R |
| Vincent | Rifle Pits | H | p.23 l.24 (581) L |
| Vinton | Rations | H | p.23 l.24 (581) R |
| Violet | Rebel | H | p.23 l.25 (581) L |
| Virgin | Repulse | H | p.23 l.25 (581) R |
| Vista | Repulsed | H | p.23 l.26 (581) L |
| Volcano | Repulsing | H | p.23 l.26 (581) R |

### page 24 (582)

| code word | meaning | grade | source |
|---|---|---|---|
| Walden | Resisted | H | p.24 l.1 (582) L |
| Wales | Resisting | H | p.24 l.1 (582) R |
| Wafer | River | H | p.24 l.2 (582) L |
| Wallace | River | H | p.24 l.2 (582) R |
| Walpole | Rail-road | H | p.24 l.3 (582) L |
| Walnut | Rail-road | H | p.24 l.3 (582) R |
| Warner | Rail-road | H | p.24 l.4 (582) L |
| Warsaw | Rail-road | H | p.24 l.4 (582) R |
| Warwick | Recruit | H | p.24 l.5 (582) L |
| Wampum | Ram | H | p.24 l.5 (582) R |
| Watkins | Right | H | p.24 l.6 (582) L |
| Watson | Report | H | p.24 l.6 (582) R |
| Wayland | Regiment | H | p.24 l.7 (582) L |
| Wayne | Regiment | H | p.24 l.7 (582) R |
| Weakness | Road | H | p.24 l.8 (582) L |
| Webb | Regiment | H | p.24 l.8 (582) R |
| Welch | Signature | H | p.24 l.9 (582) L |
| Weldon | Stragglers | H | p.24 l.9 (582) R |
| Wells | Siege | H | p.24 l.10 (582) L |
| Wesley | Siege Gun | H | p.24 l.10 (582) R |
| Wharton | Skirmish (-ed, -ing) | H | p.24 l.11 (582) L |
| Whip | Skirmish (-ed, -ing) | H | p.24 l.11 (582) R |
| White | South | H | p.24 l.12 (582) L |
| Wick | South | H | p.24 l.12 (582) R |
| Wiley | Signature | H | p.24 l.13 (582) L |
| Windham | Signed | H | p.24 l.13 (582) R |
| Windpipe | Subsistence | H | p.24 l.14 (582) L |
| Windsor | Subsistence | H | p.24 l.14 (582) R |
| Winthrop | Surprise | H | p.24 l.15 (582) L |
| Woodbine | Surround | H | p.24 l.15 (582) R |
| Woodford | Surrender | H | p.24 l.16 (582) L |
| Woodland | Surprised | H | p.24 l.16 (582) R |
| Woolwich | Surrounded | H | p.24 l.17 (582) L |
| Wyoming | Surprising | H | p.24 l.17 (582) R |
| Walrus | Surrendered | H | p.24 l.18 (582) L |
| Webster | Surrounding | H | p.24 l.18 (582) R |
| Wag | Spy | H | p.24 l.19 (582) L |
| Waltz | Steam | H | p.24 l.19 (582) R |
| Warden | Scout (-ed, -ing) | H | p.24 l.20 (582) L |
| Warp | Scout (-ed, -ing) | H | p.24 l.20 (582) R |
| Waspish | Scatter (-ed, -ing) | H | p.24 l.21 (582) L |
| Watch | Scatter (-ed, -ing) | H | p.24 l.21 (582) R |
| Waxend | Subsist (-ed, -ing) | H | p.24 l.22 (582) L |
| Wax | Subsist (-ed, -ing) | H | p.24 l.22 (582) R |
| Wayworn | Transportation | H | p.24 l.23 (582) L |
| Weasel | Transportation | H | p.24 l.23 (582) R |
| Wean | Transport (-ed, -ing) | H | p.24 l.24 (582) L |
| Weird | Transport (-ed, -ing) | H | p.24 l.24 (582) R |
| Web | Threaten (-ed, -ing) | H | p.24 l.25 (582) L |
| Weld | Threaten (-ed, -ing) | H | p.24 l.25 (582) R |
| Widow | Troops | H | p.24 l.26 (582) L |
| Wedding | Throwing | H | p.24 l.26 (582) R |

### page 25 (583)

| code word | meaning | grade | source |
|---|---|---|---|
| Wedlock | Tomorrow | H | p.25 l.1 (583) L |
| Whack | Troops | H | p.25 l.1 (583) R |
| Wedge | Troops | H | p.25 l.2 (583) L |
| Wharf | Troops | H | p.25 l.2 (583) R |
| Weigh | Track | H | p.25 l.3 (583) L |
| Wheedle | Towards | H | p.25 l.3 (583) R |
| Whelp | Throw | H | p.25 l.4 (583) L |
| Wheaten | Thrown | H | p.25 l.4 (583) R |
| Wherry | To day | H | p.25 l.5 (583) L |
| Whig | Train | H | p.25 l.5 (583) R |
| Whiff | Telegraph (-ed, -ing) | H | p.25 l.6 (583) L |
| Whimper | Telegraph (-ed, -ing) | H | p.25 l.6 (583) R |
| Whinny | Unserviceable | H | p.25 l.7 (583) L |
| Whisky | Union | H | p.25 l.7 (583) R |
| Whist | Unite (-ed, -ing) | H | p.25 l.8 (583) L |
| Whistle | Unite (-ed, -ing) | H | p.25 l.8 (583) R |
| Wrangle | Valley | H | p.25 l.9 (583) L |
| Wreathe | Valley | H | p.25 l.9 (583) R |
| Wriggle | Volunteer | H | p.25 l.10 (583) L |
| Wrinkle | Volunteered | H | p.25 l.10 (583) R |
| Wadding | Volunteering | H | p.25 l.11 (583) L |
| Waggish | Union | H | p.25 l.11 (583) R |
| Weston | Watch | H | p.25 l.12 (583) L |
| Wisdom | Watched | H | p.25 l.12 (583) R |
| Washington | Wounded | H | p.25 l.13 (583) L |
| Wilcox | Wounded | H | p.25 l.13 (583) R |
| Wooster | Rear Guard | H | p.25 l.14 (583) L |
| Worcester | Rear Guard | H | p.25 l.14 (583) R |
| World | West | H | p.25 l.15 (583) L |
| Walker | West | H | p.25 l.15 (583) R |
| Winston | Watching | H | p.25 l.16 (583) L |
| Wilkes | Wounded | H | p.25 l.16 (583) R |
| Wicoff | Drove in our Pickets | H | p.25 l.17 (583) L |
| Wilson | Drove in our Pickets | H | p.25 l.17 (583) R |
| Wabash | Drove in Enemys Pickets | H | p.25 l.18 (583) L |
| Winona | Drove in Enemys Pickets | H | p.25 l.18 (583) R |
| Winchester | Encountered enemy in force | H | p.25 l.19 (583) L |
| Williamsport | Encountered enemy in force | H | p.25 l.19 (583) R |
| Woodbury | Monday | H | p.25 l.20 (583) L |
| Waldo | Killed | H | p.25 l.20 (583) R |
| Young | Tuesday | H | p.25 l.21 (583) L |
| Yarmouth | Reverse | H | p.25 l.21 (583) R |
| Yancey | Wednesday | H | p.25 l.22 (583) L |
| Yacht | Period | H | p.25 l.22 (583) R |
| Yankee | Thursday | H | p.25 l.23 (583) L |
| Yardstick | Period | H | p.25 l.23 (583) R |
| Yellow | Friday | H | p.25 l.24 (583) L |
| Yawl | Signed | H | p.25 l.24 (583) R |
| Youth | Saturday | H | p.25 l.25 (583) L |
| Yoke | 100 (numeral) | H | p.25 l.25 (583) R |
| Zodiac | Sunday | H | p.25 l.26 (583) L |
| Zebra | 1000 (numeral) | H | p.25 l.26 (583) R |

## 6. Handwritten addenda (grade H unless marked: pages 27-30 bound between 11 and 12, pointers 566-569; blue leaves [25A]-[25C], pointers 584-586)

Pages 27-30 (page 27 headed, in a cancelled title, "Arbitraries to be used between C.A. Dana & Washington", with "Add'l" in the margin) list generals, Georgia and Tennessee places and common words with their arbitraries (Names | Arbitraries), the names in dark ink and the arbitraries in red on pages 27-28; the blue leaves list common words and the months. On [25B] the copyist's Names column runs one line out against the Arbitraries column from row 4 to row 8: "Page 32" (a cross-reference, not a word) stands against Radical, "Officer" against Religion, "Operations" against Repeat, "Order" against Revenge and "Occupy" against Slumber, and three pencil slashes stand beside rows 4-7. The ledger fixes Radical = officer and Repeat = order (N2-A, N2-B against the Official Records), so the arbitraries are taken one row up from the copyist's alignment for rows 4-8, with the grades shown; from row 9 (Sober = Push) the columns agree line by line again.

# Pass E: mssEC 47 "Cipher No. 2", manuscript pages 27-30 (pointers 566-569)

Transcribed 20 Sept 2026 from the Huntington IIIF images (1600 px and 3000 px copies, local crops, autocontrast on 568-569). Row = entry line counted from the first line under the column headings; blank ruled lines are counted. Meaning = "Names" column as written (surname first, initials as written); code word = "Arbitraries" column.

### page 27 (566)

| code word | meaning | grade | source |
|---|---|---|---|
| Addison | Baird A | H | p.27 row 1 (566) |
| Albany | Beatty J | H | p.27 row 2 (566) |
| Alexandria | Beatty S | H | p.27 row 3 (566) |
| Altoona | Carter S.P. | H | p.27 row 4 (566) |
| Annapolis | Carr | H | p.27 row 5 (566) |
| Arlington | Cook J | H | p.27 row 6 (566) |
| Augusta | Crook S [?] | H | p.27 row 7 (566) |
| Baldwin | Crocker M M | H | p.27 row 8 (566) |
| Bailey | Campbell W B | H | p.27 row 9 (566) |
| Barclay | Crittenden | H | p.27 row 10 (566) |
| Baltimore | Cruft J [?] | H | p.27 row 11 (566) |
| Belfast | Craig J | H | p.27 row 12 (566) |
| Belmont | Dodge | H | p.27 row 13 (566) |
| Bolivar | Davis J.C | H | p.27 row 14 (566) |
| Bologna | Davidson J W | H | p.27 row 15 (566) |
| Bradford | Dumont | H | p.27 row 16 (566) |
| Brunswick | Ewing | H | p.27 row 17 (566) |
| Buffalo | Elliott W L | H | p.27 row 18 (566) |
| Buchanan | Ferrero [?] E | H | p.27 row 19 (566) |
| Cambridge | Fry S.S. | H | p.27 row 20 (566) |
| Cameron [?] | Garrard T T | H | p.27 row 21 (566) |
| Canton | Garfield J A | H | p.27 row 22 (566) |
| Campbell | Harker | H | p.27 row 23 (566) |
| Chicago | Hatch J P | H | p.27 row 24 (566) |
| Chelsea | Hazen W B | H | p.27 row 25 (566) |
| Colorada [sic] | Herron F J | H | p.27 row 26 (566) |
| Davenport | Hobson E.H. | H | p.27 row 27 (566) |
| Dennison | Hovey A.P. | H | p.27 row 28 (566) |
| Detroit | Johnson R W | H | p.27 row 29 (566) |

### page 28 (567)

| code word | meaning | grade | source |
|---|---|---|---|
| Dixon | King | H | p.28 row 1 (567) |
| Drake | Lauman J G | H | p.28 row 2 (567) |
| Duncan | Lawler M K | H | p.28 row 3 (567) |
| England | McArthur J | H | p.28 row 4 (567) |
| Elmira | Morgan J D. | H | p.28 row 5 (567) |
| Elgin | Oglesby R J | H | p.28 row 6 (567) |
| Falmouth | Osterhaus J P | H | p.28 row 7 (567) |
| Frederick | Paine G | H | p.28 row 8 (567) |
| Fulton | Potter E E | H | p.28 row 9 (567) |
| Goldsmith | Prince H H | H | p.28 row 10 (567) |
| Gordonsville | Ranson [sic] T.E.G | H | p.28 row 11 (567) |
| Harrisburg | Schurz Carl | H | p.28 row 12 (567) |
| Harding | Smith A.J. | H | p.28 row 13 (567) |
| Henderson | Smith J E | H | p.28 row 14 (567) |
| Harlem | Smith M L | H | p.28 row 15 (567) |
| Illinois | Smith W.F | H | p.28 row 16 (567) |
| Jackson | Spears J.G. | H | p.28 row 17 (567) |
| Joliet [?] | Stanley D S | H | p.28 row 18 (567) |
| Liverpool | Stevenson T.G. | H | p.28 row 19 (567) |
| Louisville | Turchin J B | H | p.28 row 20 (567) |
| London | Tuttle J M | H | p.28 row 21 (567) |
| Lexington | Willich A | H | p.28 row 22 (567) |
| Mansfield | Wilcox O B | H | p.28 row 23 (567) |
| Marengo | Wilson | H | p.28 row 24 (567) |
| Ohio | Wood T J | H | p.28 row 25 (567) |
| Sandusky | Comstock Lt Col C B | H | p.28 row 26 (567) |
| (row 27: blank) | - | H | p.28 row 27 (567) |
| Mars | Dana C A | H | p.28 row 28 (567) |
| Pollux | Dana C A | H | p.28 row 29 (567) |
| Saturn | Dana C A | H | p.28 row 30 (567) |
| Charles | McCallum D C | H | p.28 row 31 (567) |
| George | McCallum D C | H | p.28 row 32 (567) |

### page 29 (568)

| code word | meaning | grade | source |
|---|---|---|---|
| Annex | Blue Bird Gap | H | p.29 row 1 (568) |
| Amuse | Catlets " [ditto = Gap] | H | p.29 row 2 (568) |
| Arrange | Dug " [ditto = Gap] | H | p.29 row 3 (568) |
| Astonish | Fricks " [ditto = Gap] | H | p.29 row 4 (568) |
| Bandage | Juliens [?] " [ditto = Gap] | H | p.29 row 5 (568) |
| Blockade | McDaniels " [ditto = Gap] | H | p.29 row 6 (568) |
| Breath | Parkers " [ditto = Gap] | H | p.29 row 7 (568) |
| Brush | Stevens " [ditto = Gap] | H | p.29 row 8 (568) |
| Business | Browns Ferry | H | p.29 row 9 (568) |
| Confederate | Kellys " [ditto = Ferry] | H | p.29 row 10 (568) |
| Capital | Williams " [ditto = Ferry] | H | p.29 row 11 (568) |
| Censure | Campbells Station | H | p.29 row 12 (568) |
| Charm | Canton | H | p.29 row 13 (568) |
| Clear | Chickamauga Hill | H | p.29 row 14 (568) |
| Close | Eastport | H | p.29 row 15 (568) |
| Concern | Gordons Mill | H | p.29 row 16 (568) |
| Confess | Graysville Station | H | p.29 row 17 (568) |
| Collect | Harrison | H | p.29 row 18 (568) |
| Corrupt | Johns Mountain | H | p.29 row 19 (568) |
| Deposit | Lookout | H | p.29 row 20 (568) |
| Degrade | Lexington | H | p.29 row 21 (568) |
| Despond | Lookout Mountain | H | p.29 row 22 (568) |
| Desire | Lookout Valley | H | p.29 row 23 (568) |
| Despatch | McLamores Cove | H | p.29 row 24 (568) |
| Depress (struck: Dissolve, written Depress) | Missionary Ridge | H | p.29 row 25 (568) |
| Dislike | Pigeon Mountain | H | p.29 row 26 (568) |
| Disburse | Pealers Mill | H | p.29 row 27 (568) |
| Dissolve | Rossville | H | p.29 row 28 (568) |
| Dispute | Shellmound | H | p.29 row 29 (568) |
| Dismiss | Summertown | H | p.29 row 30 (568) |
| Democrat | Taylors Ridge | H | p.29 row 31 (568) |
| Endeavor | Tuckers Station | H | p.29 row 32 (568) |

### page 30 (569)

| code word | meaning | grade | source |
|---|---|---|---|
| Enforce [?] | Tunnel Hill | H | p.30 row 1 (569) |
| Express | Tyners Station | H | p.30 row 2 (569) |
| Enlarge | Varnells " [ditto = Station] | H | p.30 row 3 (569) |
| Encounter | Wauhatchie | H | p.30 row 4 (569) |
| Endure | Whiteside | H | p.30 row 5 (569) |
| Expand | White Oak Ridge | H | p.30 row 6 (569) |
| Federal | Conasauga River | H | p.30 row 7 (569) |
| Fugitive | Coosawattie " [ditto = River] | H | p.30 row 8 (569) |
| Female | Cooyehuttie " [ditto = River] | H | p.30 row 9 (569) |
| Flood | Duck Creek | H | p.30 row 10 (569) |
| Flourish | Citico " [ditto = River] | H | p.30 row 11 (569) |
| Figure | Little River | H | p.30 row 12 (569) |
| (row 13: blank) | - | H | p.30 row 13 (569) |
| Flag | Acton [sic, ? Action] | H | p.30 row 14 (569) |
| Gallant | Across | H | p.30 row 15 (569) |
| Glory | Across | H | p.30 row 16 (569) |
| Harness | Ascertain-ed-ing | H | p.30 row 17 (569) |
| Hasten | Assault | H | p.30 row 18 (569) |
| Humble | Attempt | H | p.30 row 19 (569) |
| Haunt | Body | H | p.30 row 20 (569) |
| Improve | Build | H | p.30 row 21 (569) |
| Index | Centre | H | p.30 row 22 (569) |
| Insult | Carry | H | p.30 row 23 (569) |
| Interest | Captain | H | p.30 row 24 (569) |
| Intrude | Confederate | H | p.30 row 25 (569) |
| Import | Creek | H | p.30 row 26 (569) |
| Laugh | Column | H | p.30 row 27 (569) |
| Learn | Design | H | p.30 row 28 (569) |
| Libel | Day | H | p.30 row 29 (569) |
| Miserable | Execution | H | p.30 row 30 (569) |
| Manifest | Execute (struck: Manifest, written Execute) | H | p.30 row 31 (569) |
| Manure | Endanger | H | p.30 row 32 (569) |

### page [25A] (584)

| code word | meaning | grade | source |
|---|---|---|---|
| Measure | Engage | H | p.[25A] row 1 (584) |
| Mend | Expose | H | p.[25A] row 2 (584) |
| Navigate | Encounter | H | p.[25A] row 3 (584) |
| Oppress | Everything | H | p.[25A] row 4 (584) |
| Opinion | Field | H | p.[25A] row 5 (584) |
| Plaster | Failure | H | p.[25A] row 6 (584) |
| Pack | Forward | H | p.[25A] row 7 (584) |
| Pass | Fire | H | p.[25A] row 8 (584) |
| Pencil | Form | H | p.[25A] row 9 (584) |
| Pepper | Failed | H | p.[25A] row 10 (584) |
| Persuade | Gain | H | p.[25A] row 11 (584) |
| Powder | Heights | H | p.[25A] row 12 (584) |
| Presume | Hotly [?] | H | p.[25A] row 13 (584) |
| Rank | Has been sent | H | p.[25A] row 14 (584) |
| Ration | Hill | H | p.[25A] row 15 (584) |
| Republic | Important | H | p.[25A] row 16 (584) |
| Rebellion | Importance | H | p.[25A] row 17 (584) |
| Resemble | Interpose | H | p.[25A] row 18 (584) |
| Revolution | Line of battle | H | p.[25A] row 19 (584) |
| Revenue | Lieutenant | H | p.[25A] row 20 (584) |
| Refuse (-ed, -ing) | Loss Losing | H | p.[25A] row 21 (584) |
| Register | Land | H | p.[25A] row 22 (584) |
| Regret | Mass | H | p.[25A] row 23 (584) |
| Respect | Mask | H | p.[25A] row 24 (584) |
| Rain | March | H | p.[25A] row 25 (584) |

### page [25B] (585)

| code word | meaning | grade | source |
|---|---|---|---|
| Reject | Maneuvre [sic] | H | p.[25B] row 1 (585) |
| Rubbish | Mill | H | p.[25B] row 2 (585) |
| Rumpus | Ordnance | H | p.[25B] row 3 (585) |
| Radical | Officer | C | p.[25B] row 4 (585); alignment fixed by N2-B (OR I/34 pt 3 p.331 "any officer") |
| Religion | Operations | I | p.[25B] row 5 (585); alignment inferred, see section 6 |
| Repeat | Order | C | p.[25B] row 6 (585); alignment fixed by N2-A (OR I/34 pt 3 p.169 "ordered") |
| Revenge | Occupy [pencil: operate] | I | p.[25B] row 7 (585); alignment inferred, see section 6 |
| Slumber | (Names column: "Page 32", a cross-reference; no meaning in this copy) | M | p.[25B] row 8 (585) |
| Sober | Push | H | p.[25B] row 9 (585) |
| Soften | Possess | H | p.[25B] row 10 (585) |
| Suffer | Produce | H | p.[25B] row 11 (585) |
| Submit | Progress | H | p.[25B] row 12 (585) |
| Shift | Press | H | p.[25B] row 13 (585) |
| Subject | Protect | H | p.[25B] row 14 (585) |
| Salt | Plan | H | p.[25B] row 15 (585) |
| Sample | Prisoners | H | p.[25B] row 16 (585) |
| Sublime | Rapid | H | p.[25B] row 17 (585) |
| Sentence | Reconnoitre | H | p.[25B] row 18 (585) |
| Salary | Ridge | H | p.[25B] row 19 (585) |
| Snuff | Rebellion | H | p.[25B] row 20 (585) |
| Sword | Supplies | H | p.[25B] row 21 (585) |
| Staff | Station | H | p.[25B] row 22 (585) |
| Substance | Should have been | H | p.[25B] row 23 (585) |
| Singular | Successful | H | p.[25B] row 24 (585) |
| Sheriff | Success | H | p.[25B] row 25 (585) |

### page [25C] (586)

| code word | meaning | grade | source |
|---|---|---|---|
| Season | Supply | H | p.[25C] row 1 (586) |
| Seperate [sic] | Support | H | p.[25C] row 2 (586) |
| Swamp | Secure | H | p.[25C] row 3 (586) |
| Scholar | Safe | H | p.[25C] row 4 (586) |
| Swimming | Strong | H | p.[25C] row 5 (586) |
| Satan | Staff | H | p.[25C] row 6 (586) |
| Sarcasm | Squadron | H | p.[25C] row 7 (586) |
| Shampoo | Unsuccessful | H | p.[25C] row 8 (586) |
| Translate | Work | H | p.[25C] row 9 (586) |
| Telegraph | Withdraw | H | p.[25C] row 10 (586) |
| Trumpet | Wing | H | p.[25C] row 11 (586) |
| Tremendous | Will be sent | H | p.[25C] row 12 (586) |
| Trifle | Will be | H | p.[25C] row 13 (586) |
| Abraham | January | H | p.[25C] row 14 (586) |
| Balaam | February | H | p.[25C] row 15 (586) |
| Enoch | March | H | p.[25C] row 16 (586) |
| Genesis | April | H | p.[25C] row 17 (586) |
| Job | May | H | p.[25C] row 18 (586) |
| Luke | June | H | p.[25C] row 19 (586) |
| Mark | July | H | p.[25C] row 20 (586) |
| Moses | August | H | p.[25C] row 21 (586) |
| Nimrod | September | H | p.[25C] row 22 (586) |
| Noah | October | H | p.[25C] row 23 (586) |
| Obadiah | November | H | p.[25C] row 24 (586) |
| Pharoah [sic] | December | H | p.[25C] row 25 (586) |

### page [25D] (587)

| code word | meaning | grade | source |
|---|---|---|---|
| (page blank: ruled blue leaf, no writing) | - | H | p.[25D] (587) |

## 7. Numerals (grade H, mssEC 47 handwritten page "26", pointer 588)

Two names per value, 1-20, 30-90 by tens, hundred and thousand; consecutive numeral words combine the English way (decode.py). The day of the month is written in numeral words and the month by its addenda word ([25C]) or in clear.

| code word | meaning | grade | source |
|---|---|---|---|
| Allen | 1 (numeral) | H | fly leaf row 1 (588) L |
| Brown | 1 (numeral) | H | fly leaf row 1 (588) R |
| Arnold | 2 (numeral) | H | fly leaf row 2 (588) L |
| Brooks | 2 (numeral) | H | fly leaf row 2 (588) R |
| Austin | 3 (numeral) | H | fly leaf row 3 (588) L |
| Benton | 3 (numeral) | H | fly leaf row 3 (588) R |
| Andrew | 4 (numeral) | H | fly leaf row 4 (588) L |
| Baker | 4 (numeral) | H | fly leaf row 4 (588) R |
| Caldwell | 5 (numeral) | H | fly leaf row 5 (588) L |
| Dayton | 5 (numeral) | H | fly leaf row 5 (588) R |
| Clarke | 6 (numeral) | H | fly leaf row 6 (588) L |
| Dawson | 6 (numeral) | H | fly leaf row 6 (588) R |
| Cushing | 7 (numeral) | H | fly leaf row 7 (588) L |
| Downing | 7 (numeral) | H | fly leaf row 7 (588) R |
| Edwards | 8 (numeral) | H | fly leaf row 8 (588) L |
| Fisher | 8 (numeral) | H | fly leaf row 8 (588) R |
| Ellsworth | 9 (numeral) | H | fly leaf row 9 (588) L |
| Franklin | 9 (numeral) | H | fly leaf row 9 (588) R |
| Elliott | 10 (numeral) | H | fly leaf row 10 (588) L |
| French | 10 (numeral) | H | fly leaf row 10 (588) R |
| Gardner | 11 (numeral) | H | fly leaf row 11 (588) L |
| Hawkins | 11 (numeral) | H | fly leaf row 11 (588) R |
| Gilbert | 12 (numeral) | H | fly leaf row 12 (588) L |
| Hoffman | 12 (numeral) | H | fly leaf row 12 (588) R |
| Graham | 13 (numeral) | H | fly leaf row 13 (588) L |
| Hudson | 13 (numeral) | H | fly leaf row 13 (588) R |
| James | 14 (numeral) | H | fly leaf row 14 (588) L |
| Kirby | 14 (numeral) | H | fly leaf row 14 (588) R |
| Jones | 15 (numeral) | H | fly leaf row 15 (588) L |
| Kimball | 15 (numeral) | H | fly leaf row 15 (588) R |
| Johnson | 16 (numeral) | H | fly leaf row 16 (588) L |
| Knapp | 16 (numeral) | H | fly leaf row 16 (588) R |
| Lewis | 17 (numeral) | H | fly leaf row 17 (588) L |
| Marshall | 17 (numeral) | H | fly leaf row 17 (588) R |
| Ludlow | 18 (numeral) | H | fly leaf row 18 (588) L |
| Mason | 18 (numeral) | H | fly leaf row 18 (588) R |
| Loomis | 19 (numeral) | H | fly leaf row 19 (588) L |
| Morgan | 19 (numeral) | H | fly leaf row 19 (588) R |
| Nelson | 20 (numeral) | H | fly leaf row 20 (588) L |
| Oliver | 20 (numeral) | H | fly leaf row 20 (588) R |
| Norris | 30 (numeral) | H | fly leaf row 21 (588) L |
| Ogden | 30 (numeral) | H | fly leaf row 21 (588) R |
| Nathan | 40 (numeral) | H | fly leaf row 22 (588) L |
| Oscar | 40 (numeral) | H | fly leaf row 22 (588) R |
| Palmer | 50 (numeral) | H | fly leaf row 23 (588) L |
| Randall | 50 (numeral) | H | fly leaf row 23 (588) R |
| Perkins | 60 (numeral) | H | fly leaf row 24 (588) L |
| Russell | 60 (numeral) | H | fly leaf row 24 (588) R |
| Prentiss | 70 (numeral) | H | fly leaf row 25 (588) L |
| Rodgers | 70 (numeral) | H | fly leaf row 25 (588) R |
| Tucker | 80 (numeral) | H | fly leaf row 26 (588) L |
| Roach | 80 (numeral) | H | fly leaf row 26 (588) R |
| Thayer | 90 (numeral) | H | fly leaf row 27 (588) L |
| Rowley | 90 (numeral) | H | fly leaf row 27 (588) R |
| Douglas | 100 (numeral) | H | fly leaf row 28 (588) L |
| Smith | 100 (numeral) | H | fly leaf row 28 (588) R |
| Davis | 100 (numeral) | H | fly leaf row 29 (588) L |
| Snyder | 100 (numeral) | H | fly leaf row 29 (588) R |
| Seward | 1000 (numeral) | H | fly leaf row 30 (588) L |
| Dwight | 1000 (numeral) | H | fly leaf row 30 (588) R |
| Sprague | 1000 (numeral) | H | fly leaf row 31 (588) L |
| Donaldson | 1000 (numeral) | H | fly leaf row 31 (588) R |

## 8. The clerk's forms the book does not give

Filled in after the three entries were read (reading-no2.md): tokens of the entries that are not printed in
mssEC 47 as written, with the grade the evidence allows. These rows stand last so that they override the
route-page reading of "Yard".

| code word | meaning | grade | source |
|---|---|---|---|
| Yard | Period | I | N2-A twice, N2-B once, each where the OR prints a full stop; the clerk's short form of Yardstick (p.25 l.23 R = Period); Yard itself is a line indicator (p.9) |
| reswindling | removing | I | N2-B: "re" + Swindling (Swindle = Move, p.22 l.22 L); OR I/34 pt 3 p.331 "removing General Banks" |
| whim | telegram | C | N2-B "Your whim of 10.30": OR I/34 pt 3 p.331 "Your telegram of 10.30 a. m."; the ledger uses "whims" the same way on page 9 (15 Feb 1864) |
| Chumb | Maj Gen N P Banks | M | N2-B; the book's word is Cherub (p.13 l.25 R) or Lapland (p.18 l.3 L); the clerk wrote "Chumb"; OR "General Banks" |
