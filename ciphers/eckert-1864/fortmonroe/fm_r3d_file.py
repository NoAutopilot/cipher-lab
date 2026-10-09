#!/usr/bin/env python3
"""FM-R3d: file the six Fort Monroe (mssEC 25 / obj 5952) entries of fm_r3d_entries.txt into ../ciphertext.txt (Cipher No. 1) as E210-E219.
Usage: python3 fm_r3d_file.py [--dry]   Idempotent: skips an ID already present."""
import re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
MAP = {
 "F1": ("E240", "Page 240 | 5784 | mssEC 25 (obj 5952, pointer 5784), 30 Sept 1864 6.30 PM Ft Monroe, Sheldon to Maj. Eckert for Brig. Gen. Barnes, Washington, forwarding Surgeon D. W. Hand's report of yellow fever at Newbern (FM-R3d; row 5784/1; image-read at 2400 px)"),
 "F2": ("E241", "Page 119 | 5663 | mssEC 25 (obj 5952, pointer 5663), 10 May 1864 4.30 PM Ft Monroe, Sheldon to Maj. Eckert for Fulton and Craig: the fight of 9 May near Bermuda Hundred, Kautz at Hicksford, list of wounded offered (FM-R3d; row 5663/1; image-read at 2400 px)"),
 "F3": ("E242", "Page 138 | 5682 | mssEC 25 (obj 5952, pointer 5682), 21 May 1864 3.45 PM Hd Qrs Gen. Butler, R. O'Brien to Maj. Eckert: operators at the Bermuda front, signal field cord wanted (FM-R3d; row 5682/0; image-read at 2400 px)"),
 "F4": ("E243", "Page 282 | 5826 | mssEC 25 (obj 5952, pointer 5826), 10 Dec 1864 Ft Monroe, Sheldon to S. H. Beckwith, City Point, for Col. G. W. Bradley, chief quartermaster: two messages signed Wm L. James, Capt. and Asst. Quartermaster, steamer Brady, the Matilda, a sea-going steamer for horses (FM-R3d; row 5826/1; image-read at 2400 px)"),
 "F5": ("E244", "Page 252 | 5796 | mssEC 25 (obj 5952, pointer 5796), 17 Oct 1864 (ledger date) Washington; the message is Schofield (Chattanooga, 17 Oct 3 PM) to C. A. Dana, Hood's movements; addressee line 'Dealy F' unread; in print OR I/39 pt 3 (FM-R3d; row 5796/0; image-read at 2400 px)"),
 "F6": ("E245", "Page 225 | 5769 | mssEC 25 (obj 5952, pointer 5769), 10 July 1864 Ft Monroe, Sheldon to Maj. Eckert for the Secretary of the Navy, forwarding Acting Rear-Adm. S. P. Lee, flagship Malvern, Hampton Roads: pursuit of the Florida (FM-R3d; row 5769/0; image-read at 2400 px)"),
}
NOTES = {
 "F1": ["plain: oh william", "note: image (2400 px) reads 'palsy Barnes grapes'; Barnes is missing from the Huntington transcription, left as transcribed"],
 "F2": ["gloss: bermuda=Bermuda_Hundred:I"],
 "F3": ["plain: snow", "gloss: bermuda=Bermuda:I"],
 "F4": ["plain: william", "split: harsh"],
 "F5": [],
 "F6": ["plain: florida georgia america vernon adams"],
}
blocks = {}; cur = None
for ln in (HERE/"fm_r3d_entries.txt").read_text(encoding="utf-8").splitlines():
    m = re.match(r"### (F\d+) \|", ln)
    if m: cur = m.group(1); blocks[cur] = []; continue
    if cur and ln.strip(): blocks[cur].append(ln)
p = HERE.parent/"ciphertext.txt"; txt = p.read_text(encoding="utf-8")
add = [f"### {nid} | {desc}\n" + "\n".join(blocks[k] + NOTES[k]) + "\n" for k, (nid, desc) in MAP.items() if f"### {nid} |" not in txt]
if not add: print("nothing to add")
elif "--dry" in sys.argv: print("would add", len(add))
else: p.write_text(txt.rstrip("\n") + "\n\n" + "\n".join(add), encoding="utf-8"); print("added", len(add))
