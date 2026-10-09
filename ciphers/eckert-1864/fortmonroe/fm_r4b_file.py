#!/usr/bin/env python3
"""FM-R4b: file ten Fort Monroe (mssEC 25 / obj 5952) entries of fm_r4b_entries.txt into ../ciphertext.txt (Cipher No. 1) as E260-E269.
Per-entry note lines (plain:/variant:/merge:) are decode.py's own mechanism; the transcription lines are unchanged.
Usage: python3 fm_r4b_file.py [--dry]   Idempotent. Text = Huntington transcription; every page image-read at 2400 px (FM-R4b)."""
import re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
def d(page, ptr, row, rest): return f"Page {page} | {ptr} | mssEC 25 (obj 5952, pointer {ptr}), {rest} (FM-R4b; row {row}; image-read at 2400 px)"
MAP = {
 "F1": ("E260", d(243, 5787, "5787/1", "5 Oct 1864 Ft Monroe, Sheldon to R. O'Brien at Butler's Hd Qrs: Gen. Ingalls's claim on the steamer City of Hudson, water short; signed R. C. Webster"), ["variant: winton=Vinton:M", "plain-at: webster#2"]),
 "F2": ("E261", d(85, 5629, "5629/1", "24 Apr 1864 Ft Monroe, Sheldon to Maj. Eckert for the Quartermaster General: requisition of 12 Apr, mules for Capt. Farquhar's pontoon train, 200 wagons; signed Herman Biggs"), []),
 "F3": ("E262", d(197, 5741, "5741/0", "12 June 1864 Gen. Butler's Hd Qrs, R. O'Brien to Maj. Eckert: rebels(?) arriving, cable for the James and for Appomattox"), ["plain: apple mattox"]),
 "F4": ("E263", d(268, 5812, "5812/0", "29 Nov 1864 Ft Monroe, Sheldon to the Cipher Agent City Point, for Capt. William T. Howell, Grant's Hd Qrs: empty steamers to Washington, signed Rufus Ingalls, Chief Quartermaster"), ["plain: william"]),
 "F5": ("E264", d(66, 5610, "5610/1", "19 Apr 1864 Ft Monroe, Sheldon to Maj. Eckert for the General-in-Chief, Washington: Truman Seymour's application to leave the Department of the South"), ["plain: seymour"]),
 "F6": ("E265", d(278, 5822, "5822/1", "8 Dec 1864 Hd Qrs A. of J., R. O'Brien to G. D. Sheldon Ft Monroe, for Porter: the monitors and the vessels at Aiken's Landing below Dutch Gap, from Wm A. Parker"), ["plain: hemp william", "variant: wylies=Wiley:M"]),
 "F7": ("E266", d(65, 5609, "5609/2", "18 Apr 1864 Ft Monroe, Sheldon to Maj. Eckert for the Quartermaster General: shelter tents and 500 artillery horses; signed Herman Biggs"), ["plain: shelter webster"]),
 "F8": ("E267", d(246, 5790, "5790/0", "10 Oct 1864 Washington, T. T. Eckert to W. J. Dealy: meet the Secretary of War, who left Washington on the Keyport"), ["plain: wharf person", "merge: key+post"]),
 "F9": ("E268", d(198, 5742, "5742/1", "12 June 1864 7.30 PM Gen. Butler's Hd Qrs, R. O'Brien to Sheldon for Col. Biggs: plank afloat, no scantling, an operator wanted"), []),
 "F10": ("E269", d(231, 5775, "5775/1", "30 July 1864 Baltimore, J. W. Sampson to Sheldon for Col. Biggs: removal of the York River light vessel"), ["plain: sampson"]),
}
blocks = {}; cur = None
for ln in (HERE/"fm_r4b_entries.txt").read_text(encoding="utf-8").splitlines():
    m = re.match(r"### (F\d+) \|", ln)
    if m: cur = m.group(1); blocks[cur] = []; continue
    if cur and ln.strip(): blocks[cur].append(ln)
p = HERE.parent/"ciphertext.txt"; txt = p.read_text(encoding="utf-8")
add = [f"### {nid} | {desc}\n" + "\n".join(blocks[k] + notes) + "\n" for k, (nid, desc, notes) in MAP.items() if f"### {nid} |" not in txt]
if not add: print("nothing to add")
elif "--dry" in sys.argv: print("would add", len(add))
else: p.write_text(txt.rstrip("\n") + "\n\n" + "\n".join(add), encoding="utf-8"); print("added", len(add))
