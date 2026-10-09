#!/usr/bin/env python3
"""FM-R3c: file the ten Fort Monroe (mssEC 25 / obj 5952) entries of fm_r3c_entries.txt into ../ciphertext.txt (Cipher No. 1) as E230-E239.
Usage: python3 fm_r3c_file.py [--dry]  Idempotent."""
import re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
P = "mssEC 25 (obj 5952, pointer %s), %s"
MAP = {
 "F1": ("E230", "Page 295 | 5839 | " + P % ("5839", "25 Dec 1864 Ft Monroe, Sheldon to Maj. Eckert, for Fox: Rodgers, the brasses are worn again (FM-R3c; row 5839/2; image-read at 2400 px)")),
 "F2": ("E231", "Page 190 | 5734 | " + P % ("5734", "9 June 1864 Ft Monroe, Sheldon to Maj. Eckert, for the Secretary of the Navy: S. P. Lee, Agawam, Farrar's Island (FM-R3c; row 5734/2; transcription only)")),
 "F3": ("E232", "Page 192 | 5736 | " + P % ("5736", "9 June 1864 Ft Monroe, Sheldon to Maj. Eckert, for the Secretary of the Navy: S. P. Lee, Agawam, gunboats from the Potomac to York River (FM-R3c; row 5736/1; transcription only)")),
 "F4": ("E233", "Page 216 | 5760 | " + P % ("5760", "19 June 1864 Ft Monroe, Sheldon to Maj. Eckert, for the General-in-Chief: Foster (Hilton Head, 16 June) on the officers placed under fire at Charleston (FM-R3c; row 5760/0; image-read at 2400 px)")),
 "F5": ("E234", "Page 139 | 5683 | " + P % ("5683", "22 May 1864 5 PM Ft Monroe, Sheldon to Maj. Eckert: O'Brien on press despatches, Rowe's press telegram on the attacks at Fort Powhatan and Bermuda Hundred (FM-R3c; row 5683/0; image-read at 2400 px)")),
 "F6": ("E235", "Page 287 | 5831 | " + P % ("5831", "14 Dec 1864, received at Ft Monroe, Maj. Eckert to Sheldon, Foster's landing at Tullifinny Creek and exchanged prisoners (FM-R3c; row 5831/2; transcription only)")),
 "F7": ("E236", "Page 126 | 5670 | " + P % ("5670", "14 May 1864 Ft Monroe, Sheldon to Maj. Eckert, press telegram from Bermuda Hundreds 13 May for Fulton and Craig (FM-R3c; row 5670/1; transcription only)")),
 "F8": ("E237", "Page 185 | 5729 | " + P % ("5729", "3 June 1864, received at Ft Monroe, Maj. Eckert to Sheldon (copy to Beckwith, Grant's Hd Qrs): Carter's Knoxville telegram on a Hanoverian named Finck, Van Duzer (FM-R3c; row 5729/1; transcription only)")),
 "F9": ("E238", "Page 293 | 5837 | " + P % ("5837", "17 Dec 1864 Washington, Eckert to Sheldon, Fox to Commodore John Rodgers; same words as the Washington sent copy mssEC 19 p.247 (9141/1) and as ORN I/11 pp.197-198: a known-plaintext key test (FM-R3c; row 5837/1; image-read at 2400 px)")),
 "F10": ("E239", "Page 293 | 5837 | " + P % ("5837", "17 Dec 1864 Ft Monroe, Sheldon to Maj. Eckert for the General-in-Chief, Major J. F. Anderson's arrival from Sherman and Foster (FM-R3c; row 5837/0; image-read at 2400 px)")),
}
blocks = {}; cur = None
for ln in (HERE/"fm_r3c_entries.txt").read_text(encoding="utf-8").splitlines():
    m = re.match(r"### (F\d+) \|", ln)
    if m: cur = m.group(1); blocks[cur] = []; continue
    if cur and ln.strip(): blocks[cur].append(ln)
p = HERE.parent/"ciphertext.txt"; txt = p.read_text(encoding="utf-8")
add = [f"### {nid} | {desc}\n" + "\n".join(blocks[k]) + "\n" for k, (nid, desc) in MAP.items() if f"### {nid} |" not in txt]
if not add: print("nothing to add")
elif "--dry" in sys.argv: print("would add", len(add))
else: p.write_text(txt.rstrip("\n") + "\n\n" + "\n".join(add), encoding="utf-8"); print("added", len(add))
