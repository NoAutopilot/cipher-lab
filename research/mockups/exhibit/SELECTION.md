# Exhibit selection: which readings earn a display (EXHIBIT-2)

Written 9 Oct 2026, 23:06 UTC by `date -u`, before any page was built. Private mock-up notes; not published.

**The question per item:** what does the audited reading itself tell a reader that is not in print? Evidence is the item's
status.json `depth_sentence` and its AUDIT.md safe sentence only, never the letter's surrounding context. Pool: every
status.json result at N3 or better (plaintext class) and D2 or better, not superseded: 139 rows, 104 of them Eckert telegrams.
Excluded before scoring, because the decipherment is on the leaf or the text is in print (not our reading):
Du Vergier 1696 (N0, interlinear decipherment on the leaf), Cañada 1869 (N0), Suriname maps (key N1, 2061 legend N0),
Gramont to Montmorency 28 Mar 1530 (N0, printed 1688; a key check), Orange to Schwarzburg 1561 (N0), WVO 5811/5810/4503 (N0),
WVO 126 Queen of Spain (plaintext N2: the period decipherment of a sibling carries it), Gersdorff 1713 (N2, D1).

**Score:** 3 = a specific, dated, named fact a visitor can repeat, not found in print; 2 = specific, but its event is already
known or the cipher carries only part of the sense; 1 = thin (a courier's note, a salutation, fragments, names alone);
0 = nothing beyond the print.

| # | item | class | depth | % read | key | the one thing the reading says (quoted from depth_sentence) | names people/places/dates? | content already in print? | score | reason | thin? |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Eckert E46, '? Govr' to John A. Kennedy, NY police, 30 Nov 1864 | N3 | D3 | 100 | period (War Dept Cipher No. 1) | "a man believed to be the chief conspirator of the attempt to burn New York, as described in Monday's Evening Post, is in the Old Capitol Prison, and asked to send someone to identify him" | yes: Kennedy, New York, Old Capitol, 30 Nov 1864 | the Post's description is reprinted (Evening Star 29 Nov 1864); the prisoner and the telegram are not located | **3** | a named plot, a prison, an order; the whole message reads | |
| 2 | Eckert E52, Dana to Wallace, Baltimore, 7 Nov 1864 | N3 | D3 | 100 | period | "a rebel agent calling himself Dr Hamilton passed through Elmira going south on Thursday last, six feet two, with light hair, moustache and whiskers and fine teeth, and to catch him" | yes | not located | **3** | a wanted notice in cipher; vivid | |
| 3 | Eckert O9/E-ledger, Turner for the Secretary of War to Dix, 26 May 1864 | N3 | D3 | 96.4 | period | "warned General Dix at New York of a rebel plot to seize a steamer on the New York-New Orleans line and described three suspects who had come from Havana" | yes | not located | **3** | a plot and three suspects; same ledger family as #1 | |
| 4 | Eckert E123, Stanton to Peck, 3 Sept 1864 | N3 | D3 | 94.1 | period | "the rebel plot to seize the Long Island Sound steamers has been received and passed to the Secretary of the Navy" | yes | not located | 3 | same family; the plot is Peck's report, Stanton's reply is routine | |
| 5 | WVO 53, Orange to Elector August, Breda 24 Oct 1561 | N4 | D3 | 97.8 | **ours** (cryptanalytic, S) | "news that the Prince of Spain is to marry his father's sister and come to govern these lands, and that the Duke of Vendome wants to recover his kingdom of Navarre by fair means or war" | yes | the rumours themselves are in print (audit D2); Orange passing them in cipher to August is not; a proposal from a recovered key | **2** | known rumours, our key; the honest hook is the key, not the news | |
| 6 | WVO 57, August to Orange, Torgau 18 Nov 1561 | N4 | D3 | 97.7 | period (Orange's 1562 key) | "the Emperor has recently, through a formal embassy, asked him to elect his son Maximilian King of the Romans in the Emperor's own lifetime, and that the other Electors will be asked the same" | yes | the approach is well known (57 unsafe sentence); this letter's report of it, and the request to keep it secret, are not (Demandt's regest covers the clear text only) | **2** | a known event, told in confidence by an Elector; the reading itself is clean | |
| 7 | Manteuffel frame 0391, P.S. 13 Oct 1712 | N3 | D2 | 46.7 | published (Krauske 1893 table) | "Oxford had said the Queen of England was too far off to meddle in pacifying the North and would defer to Hanover ... Bolingbroke's declaration had been far more violent (Denmark to be detached from its allies by the spring)" | yes | not located in Heinsius XIV or Droysen; background printed | **2** | the story is in the clear text; the cipher carries the names (Oxford, Bolingbroke, the Queen, Hanover, Denmark) and one verb (détacheroit) | |
| 8 | Chavigny to d'Avaux, f.228, 25 Aug 1640 | N3 | D2 | 36.0 | published (Tomokiyo) | "a fear that the Landgravine and the dukes of Lüneburg would [verb unread] with the enemy ... of the Landgravine he can hardly believe it" | yes | not located | 2 | a feared defection, but the key verb is unread | |
| 9 | Chavigny to d'Avaux, f.229, 25 Aug 1640 | N3 | D2 | 29.0 | published | "the dukes and Madame la Landgrave want their troops joined to M. de Longueville" | yes | not located | 2 | specific troop politics; 29% read | |
| 10 | Linhares fragment (ANTT) | N3 | D2 | 88.5 | ours (the dictionary found) | "something is to be kept secret even from the ministry" | no names | not located | 2 | the object (a pocket dictionary as key) is the story; the line is one clause | |
| 11 | Eckert E46-family others (about 95 telegrams: steamers, coal, horses, telegraph lines) | N3 | D2-D3 | 65-100 | period | e.g. "Meigs ... the Salvor to Annapolis and coal for Hilton Head" | yes | not located | 1 | routine logistics | thin |
| 12 | Eckert 1864, Fox and Meigs to Butler, 21-22 Apr 1864 | N4 | D4 | 100 | period | "Fox asks Butler to block the channel at Roanoke Island against the ram" | yes | not located | 2 | a real naval worry; one of many | |
| 13 | Birago no.90, Saluzzo 2 Oct 1572 | N4 | D2 | 75.6 | published | "a negotiation with a count, of articles sent, of a stronghold held in favour of the Huguenots" | partly | not located | 1 | fragmentary | thin |
| 14 | Birago no.86, 27 Aug 1572 | N4 | D2 | 83.0 | published | "names the Huguenots, Carmagnola and the Baron des Adrets, and fears ... ill favour" | yes | not located | 1 | names and a fear | thin |
| 15 | Manteuffel f.410, Nov 1712 | N4 | D2 | 66.7 | published | "the Queen of England is named three times ... 'ne fera rien pour lui, mais luy ...'" | yes | not located | 1 | fragments around one name | thin |
| 16 | Blathwayt BLA 191(a), 1727-29 | N4 | D2 | 84.3 | period | "Mr Keene likes him but has no orders concerning him, and asks to be sent some order" | yes | not located | 1 | a spy's complaint about pay and orders | thin |
| 17 | Stamford to Thurloe, Calais 13 Mar 1655 | N4 | D2 | 97.9 | period | "the matter came to his knowledge 'by meere chance' and 'without the least injunction of secrecy'" | no | Birch prints the cipher, not the reading | 1 | a source's disclaimer | thin |
| 18 | Danzay to Lorraine, 27 Jan 1557 | N4 | D2 | 77.4 | published | "speaks of the King of Denmark and of a promise ... and it names the chancellor" | yes | not located | 1 | fragments | thin |
| 19 | Lodewijk 4610/4611/4612/4616, 1573-74 | N4 | D2 | 62.6 | period | "'il fault que on pardonne' ... 'la rechute'" | no | not located | 1 | fragments | thin |
| 20 | WVO 5797 blanks, 22 Oct 1573 | N4 | D2 | 11.1 | period + ours | "name the Landgrave beside the Duke of Saxony ... the Elector Palatine ... 'helt sich wol und thut in warheit viel'" | yes | the letter is printed (Groen); only the two blanks are ours | 1 | two names an editor could not read | thin |
| 21 | **Gramont to Villandry, f.29r, 20 May 1530** | N4 | D2 | 93.8 | published | "he has given the bearer an article set apart ... and calls it 'le total fondement'" | yes | not located | **1** | a courier's note: the article's content is not in the letter | thin |

**Gramont dropped:** its own reading is a courier's note about a separate article whose content the letter does not give;
the divorce-suit hook belonged to the printed Montmorency letter (N0), so the EXHIBIT-1 display borrowed another letter's interest.

## Top five (by score, then by how much of the item the reading carries)
1. Eckert E46, the New York arson suspect in the Old Capitol, 30 Nov 1864: **3** (N3 D3, 100%, period key)
2. Eckert E52, the "Dr Hamilton" wanted telegram, 7 Nov 1864: **3** (N3 D3, 100%)
3. Eckert, the New York-New Orleans steamer plot, 26 May 1864: **3** (N3 D3, 96.4%)
4. WVO 53 + 57, Orange and Elector August, Oct-Nov 1561: **2** each (N4 D3, ~98%; 53 on our own key)
5. Manteuffel frame 0391, Oxford against Bolingbroke on the North, 13 Oct 1712: **2** (N3 D2, 46.7%)

## The three built
Items 1-3 are one ledger and one key; three Eckert displays would be one display three times. So: **(A) Washington 1864**,
E46 as the hero with E52 and the steamer plot as companion telegrams; **(B) Breda and Torgau 1561**, WVO 57 as the hero
(period key, the cleanest reading) with 53 beside it (our key, labelled a proposal); **(C) Berlin 1712**, frame 0391, whose
headline says what it is: five names and one verb in cipher that tell who said what inside a clear-text report.
Chavigny f.228 (2) was the next candidate; it lost to 0391 because its key verb is unread.
