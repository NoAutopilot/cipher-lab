#!/usr/bin/env python3
"""MS18-R2: file nine of the ten ms18_r2_entries.txt rows into ../ciphertext.txt (Cipher No. 1) as E322-E330 (X3 = no book in hand, not filed).
Note lines (plain-at / note) are decode.py's own mechanism; transcription lines unchanged. Usage: python3 ms18_r2_file.py [--dry]  Idempotent.
Every line image-read at 2400 px full page (MS18-R2, 9 Oct 2026)."""
import re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
def d(page, ptr, row, pp, rest): return f"Page {page} | {ptr} | mssEC 18 (obj 10074, pointer {ptr}; printed page {pp}), {rest} (MS18-R2; row {row}; image-read at 2400 px)"
MAP = {
 "X1": ("E322", d(349, 10009, "10009/1", 343, "17 May 1865 Washington, to H. F. Lines at Macon, for Wilson, by Rawlins for Grant: the Quartermaster Dept has stores at Port Royal, Maj. Thomas of the Dept of the South leaves New York today with funds, send estimates, remain with the part of the command left in Georgia, infantry and cavalry to garrison necessary points, see a competent officer has the force returned to Tennessee"),
   ["plain-at: john#1", "note: MS18-R2: No. 1 (share .42; control median .41, p10 .29, p90 .58). 'John A Rawlins' is the plain signature (image-read), not John = Grant. 'shady', 'opera shine', 'Laution', 'temper airy wants', 'esteem mates' (estimates), 'compete aunt' (competent) are unread or sound-alike spellings; Aaron = Rhode Island does not read (M)."]),
 "X2": ("E323", d(350, 10010, "10010/2", 344, "18 May 1865 (holder transcription 19th; the image reads 18th) 2.30 PM Washington, to R. C. Clowry for Pope: orders breaking up Hurlbut's division and assigning Sheridan to the command west of the Mississippi, Reynolds to take orders from Sheridan, troops Canby spared from Arkansas; signed Grant"),
   ["note: MS18-R2: No. 1 (share .54). Date: image reads 'May 18th' (the 'Henrietta' = 18 date code agrees), the holder transcription says 19th, kept as transcribed. Middle clauses (dish venus fall, whinny, hopper paddle) are unread; the gist is M."]),
 "X4": ("E324", d(364, 10024, "10024/2", 358, "28 May 1865 Washington, to Gillmore at Hilton Head, signed by the Secretary of War (Brutus): Grant has ordered Judge Campbell, R. M. T. Hunter and Seddon, late Secretary of War, sent to Fort Pulaski and held in close custody until further orders; they are now at [Galway, key = Richmond] and will be forwarded"),
   ["note: MS18-R2: No. 1 (share .30, just above the control p10 .29; the sense reads). 'R empty Hunt her' = R. M. T. Hunter, 'Sed don' = Seddon, 'Camp bell' = Campbell are plain, phonetic. Galway = Richmond (key row) is M: the prisoners were at Fort Monroe/Hampton Roads, so the place is not settled. Sibling on the holder page 10022 (28 May 1865, 'Seddon had better go also', cipher, same day)."]),
 "X5": ("E325", d(229, 9889, "9889/0", 223, "5 Nov 1864 Washington, to Clowry at St Louis for Maj. Gen. Rosecrans: the Secretary of War directs the arrest at 10 AM on Monday next of the following named rebel agents and the seizure of their papers: Wm Kendall and Capt. Lewis Kennerly (St Louis), John or Wm Ritchie (St Joseph, Mo.), James Hunter (New Madrid, Mo.), Wm Harper (Cape Girardeau); signed Dana"),
   ["plain-at: john#1", "plain-at: saint#1", "plain-at: hunter#1", "plain-at: madrid#1", "plain-at: harper#1", "note: MS18-R2: No. 1 (share .55 vs No. 2 .52, No. 9 .17: the shares do not pick the book, the sense does). Names are plain (image-read; the image has 'Kennerly' where the holder transcription says Kennedy, kept as transcribed). 'Saint Joseph Aragon' = St Joseph, Missouri (Aragon = Missouri key row, H). Same telegram as E326 and a third copy to Louisville (Bruch, pointer 9889/1, not filed here)."]),
 "X6": ("E326", d(229, 9889, "9889/2", 223, "5 Nov 1864 Washington, to Capt. Van Duzer at Nashville for Brig. Gen. J. F. Miller: the Secretary of War directs the arrest at 10 AM on Monday next of the following named rebel agent and the seizure of his papers, Col. Thos T. Tunstall of Nashville; signed Dana (the same telegram as E325 and the Louisville copy)"),
   ["note: MS18-R2: No. 1 (share .57). 'Thos T Tunstall' is plain (image-read, repeated 'Tun stall' at the end); Embrace = Nashville is the key row, H. Palate = Brig. General is H."]),
 "X7": ("E327", d(153, 9813, "9813/1", 147, "6 Aug 1864 Washington, to McCaine (addressee 'Makent'), signed General-in-Chief: the Cavalry Bureau asks that all unserviceable cavalry horses in your department be sent to the depots at Gallipolis, Ohio and Giesboro, D.C.; every effort has been directed to mount your cavalry"),
   ["note: MS18-R2: No. 1 (share .54; No. 2 .46). 'Gallipolis' and 'Geesbora D C' (Giesboro) are plain (image-read). Pledge Francis / Makent are the addressee's cipher names, unread."]),
 "X8": ("E328", d(356, 10016, "10016/2", 350, "22 May 1865 7 PM Washington, to R. C. Clowry at St Louis for Pope, signed Grant: Reynolds need not a Co.[?], the [whistle] from Arkansas; he can probably not well be replaced in that state; the Quartermaster will send you 2700 horses as fast as possible"),
   ["note: MS18-R2: No. 1 (share .59, above the control p90 .58). 'need not a Co. The whisile from' is unread (U). 'Harrow postpone prolong' = 2700 (numeral run, H)."]),
 "X9": ("E329", d(204, 9864, "9864/1", 198, "13 Oct 1864 11.30 AM Washington, to Schofield at Louisville (copy to Burbridge at Lexington and Bruch), signed General-in-Chief (Halleck): all forces that can be spared from Kentucky to be sent to General Thomas at Nashville to meet any force Hood may send north; printed OR I/39 pt 3 p.253 word for word, 'Same to General Burbridge' = send copy to Kearney"),
   ["note: MS18-R2: No. 1 (share .59). Printed OR I/39 pt 3 p.253 (Halleck to Schofield, 13 Oct 1864, 11.30 a.m.): the body is C against that print; Kearney = Burbridge by the print's '(Same to General Burbridge)'. Not a key edit (rule 4)."]),
 "X10": ("E330", d(213, 9873, "9873/1", 207, "20 Oct 1864 3 PM Washington, to Maj. Gen. Thomas at Nashville, signed General-in-Chief (Halleck): Forrest is reported threatening both Paducah and Memphis; if by the assistance of Burbridge and Washburn you could drive him south it would relieve that part of the country; printed OR I/39 pt 3 p.379 word for word"),
   ["plain-at: forrest#1", "plain-at: duke#1", "note: MS18-R2: No. 1 (share .58). Printed OR I/39 pt 3 p.379 (Halleck to Thomas, Washington 20 Oct 1864, 3 p.m.): the body is C against that print; 'Pa Duke Key' = Paducah, Ky is plain, phonetic; Kearney = Burbridge, lavender = Washburn by the print. Not a key edit (rule 4)."]),
}
blocks = {}; cur = None
for ln in (HERE/"ms18_r2_entries.txt").read_text(encoding="utf-8").splitlines():
    m = re.match(r"### (X\d+) \|", ln)
    if m: cur = m.group(1); blocks[cur] = []; continue
    if cur and ln.strip() and ln.strip() != "No 1": blocks[cur].append(ln)
p = HERE.parent/"ciphertext.txt"; txt = p.read_text(encoding="utf-8")
add = [f"### {nid} | {desc}\n" + "\n".join(blocks[k] + notes) + "\n" for k, (nid, desc, notes) in MAP.items() if f"### {nid} |" not in txt]
if add and "--dry" not in sys.argv: p.write_text(txt.rstrip("\n") + "\n\n" + "\n".join(add), encoding="utf-8")
print(("would add " if "--dry" in sys.argv else "added ") + str(len(add)))
