#!/usr/bin/env python3
"""FM65-B: file nine of the twelve rows of fm65b_entries.txt into ../ciphertext.txt (Cipher No. 1) as E512-E520 (contiguous; E521-E523 stay free).
Not filed: F2 5856/1 (no book reads a clause in the row's own word order), F7 5860/2 (in print, OR I/47 pt 2 p.106), F9 5861/2 (first message: holder
clear copy, pointer 8508). Usage: python3 fm65b_file.py [--dry]  Idempotent. Text as transcribed by the volunteers (no image read), 10 Oct 2026."""
import json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
S0 = {}
for ln in (HERE/"fm65b_step0.out").read_text().splitlines()[1:]:
    f = ln.split("\t")
    S0[(f[1], f[2])] = (f[4], f[5], f[6])
def s0(row):
    a = S0[(row, "no1")]; b = S0[(row, "no1shuf")]
    return (f"Step 0 (fm65b_step0.py, step0_ordered.py's functions): (a) {a[0]} ({a[1]}), (b) p95 {a[2]}, HIT; under a meaning-shuffled copy of No. 1 (seed 7) (a) {b[0]}, also HIT: "
            "on mssEC 25 the holder transcription is the cipher copy itself, so a step-0 hit is a non-test (RULING, LEDGER-13 jobs wave 2) and does not hold the row. ")
HOLD = "Holder (CISOSEARCHALL, all pointers, control 9678 returned): no clear copy of this row. "
PRINT = "Print: not located (phrase grep over 177 cached volumes, loose co-occurrence search, IA be-api whole-collection queries; a search result, not a verdict). "
ROWS = {
 "F1": ("E512", "5856/0",
  "mssEC 25 (obj 5952, pointer 5856), 4 Jan 1865, Ft Monroe: two messages in one segment -- Sheldon to S. H. Beckwith at City Point (9 PM; the steamers Eliza Hancox and Winants, a Capt. Howell, QM) and a second, 10.30 PM, Hd Qrs A.J. to Sheldon (have the Winants in order to go with the expedition, tug D. D. Porter), signed R. O'Brien (FM65-B; row 5856/0; text only)",
  "BOOK-FM65 test row, No. 1 (weak: one clause, two code meanings): 'please have the Winants in order to go with [expedition], also the tug D. D. Porter, will try bring down a tug [tomorrow] for your use'. "
  "M by hand: [McMinnville] (dodge) is not a Fort Monroe place; 'Seneca' (plain, a steamer) is read [Fear] by a key row -- a misfire on plain text; Winants, Eliza Hancox and Seneca are steamers (IA: Bard, steam vessels of the Hudson; Winants and Hancox as dispatch boats of the Army of the James, OR I/40 pt 2). "
  "Not in print: the 13 June 1864 and Jan 1865 Butler fleet orders mention the boats, not this text."),
 "F3": ("E513", "5857/1",
  "mssEC 25 (obj 5952, pointer 5857), 5 Jan 1865 1 PM Ft Monroe, Sheldon to Maj. Eckert at Washington: Binney (chief additional paymaster, Norfolk) to Brig. Gen. B. W. Brice, Paymaster General -- Gen. Butler orders payment of company and field officers of a second expedition who were not mustered for 31 December; Binney declined as opposed to law and General Orders and asks authority to pay except on muster rolls (FM65-B; row 5857/1; text only)",
  "M by hand: 'Amos' (plain) is read [New York] by a key row (misfire); [Norfolk] [5] opening is the sender's place and date; 'whipal' = field (plain-ish). Context, not a copy: Brice to Sheldon, 12 Dec 1864, on Binney's payments (pointers 5829 and 9913, cipher copies, not clear). "),
 "F4": ("E514", "5858/0",
  "mssEC 25 (obj 5952, pointer 5858), City Point 5 Jan 1865 (1 PM), S. H. Beckwith to Sheldon at Ft Monroe, for a colonel: some 350 troops have no transportation and will be sent in a river steamer, to be put aboard in time to sail with the rest; a Dr/Mr Leary is required for special service, Blackstone can be dispensed with and turned over to the medical department; signed Ingalls, Beckwith (FM65-B; row 5858/0; text only)",
  "M by hand: the opening [Colonel] [Reinforcements] (Harriet pandora) names the addressee only by code; 'Leary' and 'Blackstone' plain names, roles inferred (M). "),
 "F5": ("E515", "5858/1",
  "mssEC 25 (obj 5952, pointer 5858), Ft Monroe 5 Jan 1865, Sheldon to J. W. Sampson at Baltimore, for Col. R. M. Newport, chief quartermaster: the Ariel, Victor, Illinois, Gen. Sedgwick and Baltic were sent to report to you by order of the Quartermaster General; by direction of the chief QM; signed Capt. William L. James, QM (FM65-B; row 5858/1; text only)",
  "C support for the addressee: pointer 8508 (clear, Baltimore 6 Jan 1865) is signed 'RM Newport Col & chf qm'. M by hand: 'Baltic' (plain) is read [Chattahoochee] by a key row (misfire); pointer 9153 block 2 (Washington cipher copy, 5 Jan) orders the same five vessels from Monroe to Baltimore (decode: Ariel, Illinois, Sedgwick, Victor, Baltic) -- a different telegram, context only. "),
 "F6": ("E516", "5860/1",
  "mssEC 25 (obj 5952, pointer 5860), City Point 6 Jan 1865 10 AM, S. H. Beckwith to Sheldon at Ft Monroe: last night a large package of papers containing Gen. Butler's report of the Wilmington expedition was lost from an overcoat pocket -- the only two places the coat was off were the theatre and the hotel kept by Mr Phillips; please have inquiries made at both (FM65-B; row 5860/1; image-read at 2400 px, the entry's lines match the transcription)",
  "M by hand: plain 'Hotel' is read [Longstreet] by a key row (misfire; orbit = [At the]); [Shipley] is not read (the addressee of the header); the tail 'didn't travel very much' is plain. Context, not a copy: Grant to Capt. Leet, 8 Jan 1865 10 PM, 'Send back General Butler's report of the Wilmington expedition ... I wish to change the indorsement' (OR I/46 pt 2 p.68; Butler Corr. V p.476) -- a different telegram. "),
 "F8": ("E517", "5861/1",
  "mssEC 25 (obj 5952, pointer 5861), Ft Monroe 6 Jan 1865, Sheldon to J. W. Sampson at Baltimore, for Col. R. M. Newport, chief quartermaster: if the Baltic has been ordered to Monroe consider the order countermanded; let her embark troops as before ordered; signed by the Quartermaster General (FM65-B; row 5861/1; text only)",
  "M by hand: 'Baltic' (plain) is read [Chattahoochee] by a key row (misfire); pointer 8508 (clear, Baltimore 6 Jan 1865 3.45 PM, Newport to the QM General) reports the Baltic at Swann Point needing an anchor, chain and 750 tons of coal -- the antecedent situation, a different telegram. "),
 "F10": ("E518", "5864/1",
  "mssEC 25 (obj 5952, pointer 5864), Ft Monroe 7 Jan 1865, Sheldon to S. H. Beckwith at City Point, for Brig. Gen. Ingalls, chief QM: Mr Elias Smith, correspondent of the New York Tribune, desires permission to go on the next boat joining the expedition; please inform me if Gen. Grant will permit him to pass (FM65-B; row 5864/1; text only)",
  "Context, not a copy: pointer 8510 (clear, Ft Monroe 7 Jan 1865 9 AM) is Elias Smith's own request to C. A. Dana at Washington for War Department permission to go on the expedition. M by hand: 'Gen D. Sheldon' is the transcription's reading of Geo. D. Sheldon; the sign-off [Colonel] [signed] [Quartermaster] is code. "),
 "F11": ("E519", "5866/0",
  "mssEC 25 (obj 5952, pointer 5866), Ft Monroe 7 Jan 1865 (12.30), Sheldon to J. W. Sampson at Baltimore, for Col. Newport, chief QM: adopt whatever method will soonest ship troops on the Baltic; use your own judgment after seeing the captain; coal may be at Annapolis but is more readily had at Baltimore, and she cannot approach the docks at Annapolis; by order of the Quartermaster General (FM65-B; row 5866/0; text only)",
  "Antecedent (clear, pointer 8508): Newport to the QM General, Baltimore 6 Jan 1865 3.45 PM, the captain of the Baltic reports his vessel at Swann Point, cannot come nearer, needs an anchor and chain and 750 tons of coal, five days to coal at Annapolis ('Shall I order her to NY'). This is the reply and confirms the vessel is the Baltic and that 'Banditti' = Baltimore (H). M by hand: plain 'Baltic' read [Chattahoochee] (misfire). "),
 "F12": ("E520", "5866/2",
  "mssEC 25 (obj 5952, pointer 5866), Ft Monroe 7 Jan 1865, Sheldon to S. H. Beckwith at City Point, for Brig. Gen. Ingalls: the Ariel, Gen. Sedgwick, Victor and Illinois were all ordered to Baltimore at 10 PM 3 January and the Baltic at 11 PM 4 January; nothing heard since except that the Baltic was at Baltimore this morning (FM65-B; row 5866/2; text only)",
  "Context, not a copy: pointer 7682 (clear, Ft Monroe 4 Jan 1865 5.30 PM, Ingalls to the QM General) 'the Ariel, Illinois, Gen. Sedgwick, Victor & Baltic are ordered to Balto; these vessels can carry 4,000 men'. M by hand: plain 'Baltic' read [Chattahoochee] (misfire). "),
}
txt = (HERE.parent/"ciphertext.txt").read_text(encoding="utf-8")
blocks = {}; cur = None
for ln in (HERE/"fm65b_entries.txt").read_text(encoding="utf-8").splitlines():
    if ln.startswith("### "): cur = ln.split()[1]; blocks[cur] = []; continue
    if cur and ln.strip(): blocks[cur].append(ln)
add = ""
for fid, (eid, row, desc, extra) in ROWS.items():
    if f"### {eid} |" in txt: print("already present", eid); continue
    ptr = row.split("/")[0]; pg = json.load(open(HERE.parent/"sources"/"fortmonroe"/f"p{ptr}.json"))["title"]
    note = "note: FM65-B: " + s0(row) + "Book: No. 1 (BOOK-FM65: No. 1 reads all ten tested 1865 rows; this row predicted No. 1 from its month and header). " + HOLD + PRINT + extra.strip()
    add += f"### {eid} | {pg} | {ptr} | {desc}\n" + "\n".join(blocks[fid] + [note]) + "\n\n"
if not add: print("nothing to add")
elif "--dry" in sys.argv: print(add)
else: (HERE.parent/"ciphertext.txt").write_text(txt.rstrip("\n") + "\n\n" + add.rstrip("\n") + "\n", encoding="utf-8"); print("added", add.count("### E"))
