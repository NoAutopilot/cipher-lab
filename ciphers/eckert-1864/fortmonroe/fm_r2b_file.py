#!/usr/bin/env python3
"""FM-R2b: file the ten Fort Monroe (mssEC 25 / obj 5952) entries of fm_r2b_entries.txt into ../ciphertext.txt (Cipher No. 1) as E185-E194.
Usage: python3 fm_r2b_file.py [--dry]   Idempotent: skips an ID already present. Text = Huntington transcription (transcription only unless noted)."""
import re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
MAP = {
 "F1": ("E185", "Page 280 | 5824 | mssEC 25 (obj 5952, pointer 5824), 10 Dec 1864 Ft Monroe, Geo. D. Sheldon to R. O'Brien (Hd Qrs A.J.) and S. H. Beckwith (City Point): two telegrams on one page, forwarding D. D. Porter's order to Commodore Parker (Onondaga) and a second to a ship's commander about the Saugus (FM-R2b; row 5824/2; transcription only)"),
 "F2": ("E186", "Page 91 | 5635 | mssEC 25 (obj 5952, pointer 5635), 27 Apr 1864 Ft Monroe, Sheldon to S. H. Beckwith, Culpepper CH, for Grant, Butler's telegram on Rowley, the ironclad and Gillmore (FM-R2b; row 5635/0; transcription only)"),
 "F3": ("E187", "Page 255 | 5799 | mssEC 25 (obj 5952, pointer 5799), 29 Oct 1864 Ft Monroe, Sheldon to Caldwell, Hd Qrs A.P., for Gen. M. R. Patrick (FM-R2b; row 5799/1; transcription only)"),
 "F4": ("E188", "Page 40 | 5584 | mssEC 25 (obj 5952, pointer 5584), 12 Mar 1864 Ft Monroe, Sheldon to Maj. Eckert, Wistar's Middlesex-Mathews expedition (FM-R2b; row 5584/0; transcription only)"),
 "F5": ("E189", "Page 204 | 5748 | mssEC 25 (obj 5952, pointer 5748), 14 June 1864 Ft Monroe, Sheldon to Maj. Eckert, for Rucker (FM-R2b; row 5748/1; transcription only)"),
 "F6": ("E190", "Page 287 | 5831 | mssEC 25 (obj 5952, pointer 5831), 14 Dec 1864 Ft Monroe, Sheldon to R. O'Brien, Hd Qrs A.J., forwarding J. C. Hicks (FM-R2b; row 5831/0; transcription only)"),
 "F7": ("E191", "Page 45 | 5589 | mssEC 25 (obj 5952, pointer 5589), 28 Mar 1864 Ft Monroe, Sheldon to Geo. W. Baldwin, Baltimore, for Gen. Wallace (FM-R2b; row 5589/2; transcription only)"),
 "F8": ("E192", "Page 99 | 5643 | mssEC 25 (obj 5952, pointer 5643), 1 May 1864 Ft Monroe, Sheldon to S. H. Beckwith, Culpepper, for Grant, Butler's telegram (FM-R2b; row 5643/0; transcription only)"),
 "F9": ("E193", "Page 240 | 5784 | mssEC 25 (obj 5952, pointer 5784), 19 Sept 1864 Fortress Monroe, Sheldon to Maj. Eckert, Wash'n, for Rucker (FM-R2b; row 5784/0; transcription only)"),
 "F10": ("E194", "Page 261 | 5805 | mssEC 25 (obj 5952, pointer 5805), 4 Nov 1864 Butler's Hd Qrs, R. O'Brien to Sheldon, Ft Monroe (FM-R2b; row 5805/2; transcription only)"),
}
blocks = {}; cur = None
for ln in (HERE/"fm_r2b_entries.txt").read_text(encoding="utf-8").splitlines():
    m = re.match(r"### (F\d+) \|", ln)
    if m: cur = m.group(1); blocks[cur] = []; continue
    if cur and ln.strip(): blocks[cur].append(ln)
p = HERE.parent/"ciphertext.txt"; txt = p.read_text(encoding="utf-8")
add = [f"### {nid} | {desc}\n" + "\n".join(blocks[k]) + "\n" for k, (nid, desc) in MAP.items() if f"### {nid} |" not in txt]
if not add: print("nothing to add")
elif "--dry" in sys.argv: print("would add", len(add))
else: p.write_text(txt.rstrip("\n") + "\n\n" + "\n".join(add), encoding="utf-8"); print("added", len(add))
