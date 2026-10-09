#!/usr/bin/env python3
"""FM-R5b: file ten Fort Monroe (mssEC 25 / obj 5952) entries of fm_r5b_entries.txt into ../ciphertext.txt (Cipher No. 1) as E280-E289.
Per-entry note lines (plain:/variant:/merge:) are decode.py's own mechanism; the transcription lines are unchanged.
Usage: python3 fm_r5b_file.py [--dry]   Idempotent. Text = Huntington transcription; every page image-read at 2400 px (FM-R5b)."""
import re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
def d(page, ptr, row, rest): return f"Page {page} | {ptr} | mssEC 25 (obj 5952, pointer {ptr}), {rest} (FM-R5b; row {row}; image-read at 2400 px)"
MAP = {
 "F1": ("E280", d(241, 5785, "5785/0", "30 Sept 1864 Ft Monroe, Sheldon to Maj. Eckert, relaying a message from Newbern signed Gilmore: yellow fever prevailing to an alarming extent, sick at Newport Barracks, Vanderhoef to be relieved, men wanted to keep the offices open"), ["plain: fever nursing"]),
 "F2": ("E281", d(162, 5706, "5706/0", "27 May 1864 Washington, T. T. Eckert to Geo. Sheldon, Ft Monroe: a detail to cut poles and build line from Gloster to West Point, Bickford to leave Port Royal on the Rappahannock; cable for Gloster and West Point"), ["plain: white"]),
 "F3": ("E282", d(86, 5630, "5630/0", "24 Apr 1864 5 PM Ft Monroe, Sheldon to Maj. Eckert for Qr Mr Gen Meigs: the steamers and tugs reported at Fort Monroe, barges and lighters; signed Herman Biggs; PERIOD CLEAR COPY at holder pointers 10267-10268 (pp.125-126), C-grade known text"), ["plain: rockland wyoming"]),
 "F4": ("E283", d(275, 5819, "5819/1", "7 Dec 1864 Ft Monroe, to R. O'Brien Hd Qrs A. of J., for Commander Parker, Onondaga, from Porter: two gunboats down to White Shoal light and Point of Shoals, stop boats at night"), ["plain: white shoal shoals watch", "graded: paulding:M"]),
 "F5": ("E284", d(260, 5804, "5804/1", "4 Nov 1864 Ft Monroe, Sheldon to S. H. Beckwith, City Point: whether the men are to be transferred here without authority, Lizzie Baker the only boat reported; Babcock here"), []),
 "F6": ("E285", d(254, 5798, "5798/2", "27 Oct 1864 Ft Monroe, Sheldon to Maj. Eckert, Washington, for the Secretary of the Navy, from Porter: Tallapoosa, Yantic and Maumee off Montauk Point and steering for Halifax before the Tallahassee"), []),
 "F7": ("E286", d(61, 5605, "5605/2", "14 Apr 1864 Ft Monroe, Sheldon to Maj. Eckert: whether the 5th New Jersey Battery can be spared from the defences of Washington, else forward the request"), []),
 "F8": ("E287", d(244, 5788, "5788/2", "7 Oct 1864 9 AM, Ft Monroe, Sheldon to S. H. Beckwith care Maj. Eckert, Butler's Head Quarters to Lieut. Gen. Grant: the enemy have attacked and driven Kautz back and opened fire on Fort Harrison; IN PRINT OR I/42 pt 3 pp.106-107 and Butler's Private and Official Correspondence V p.231"), []),
 "F9": ("E288", d(180, 5724, "5724/0", "31 May 1864 Ft Monroe, Sheldon to Maj. Eckert for Gen. Taylor, Commissary General: two millions of rations and 1000 head of cattle to White House; signed M. P. Small, Lt Col and C. S."), ["plain: taylor white"]),
 "F10": ("E289", d(270, 5814, "5814/2", "1 Dec 1864 Ft Monroe, Sheldon to Maj. Eckert for the Secretary of the Navy, from Porter: orders for Captain Taylor and Lieut. Commander Dewey to appear before a court martial, shall the witnesses leave"), ["plain: taylor prospect"]),
}
blocks = {}; cur = None
for ln in (HERE/"fm_r5b_entries.txt").read_text(encoding="utf-8").splitlines():
    m = re.match(r"### (F\d+) \|", ln)
    if m: cur = m.group(1); blocks[cur] = []; continue
    if cur and ln.strip(): blocks[cur].append(ln)
p = HERE.parent/"ciphertext.txt"; txt = p.read_text(encoding="utf-8")
add = [f"### {nid} | {desc}\n" + "\n".join(blocks[k] + notes) + "\n" for k, (nid, desc, notes) in MAP.items() if f"### {nid} |" not in txt]
if not add: print("nothing to add")
elif "--dry" in sys.argv: print("would add", len(add))
else: p.write_text(txt.rstrip("\n") + "\n\n" + "\n".join(add), encoding="utf-8"); print("added", len(add))
