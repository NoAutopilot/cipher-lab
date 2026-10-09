#!/usr/bin/env python3
"""FM-R4a: file the ten Fort Monroe (mssEC 25 / obj 5952) entries of fm_r4a_entries.txt into ../ciphertext.txt (Cipher No. 1) as E250-E258 (E257 of the plan = F8 not filed).
Usage: python3 fm_r4a_file.py [--dry]   Idempotent: skips an ID already present."""
import re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
MAP = {
 "F1": ("E250", 'Page 226 | 5770 | mssEC 25 (obj 5952, pointer 5770), 12 July 1864 Ft Monroe, Sheldon to Maj. Eckert, forwarding Maj. W. M. Este (A.D.C.) to the Secretary of War on the fight near Silver Spring; a clear period copy stands at pointer 10490, Page 348 (FM-R4a, 9 Oct 2026; row 5770/1; transcription-only, page image not viewed)'),
 "F2": ("E251", "Page 272 | 5816 | mssEC 25 (obj 5952, pointer 5816), 4 Dec 1864 12.50 PM Hd Qrs Army of the James, R. O'Brien (Butler's office) to Sheldon at Ft Monroe, for Maj. Carney: Col. Saunders's report on property of Stephen Barton (FM-R4a; row 5816/0; image-read)"),
 "F3": ("E252", 'Page 237 | 5781 | mssEC 25 (obj 5952, pointer 5781), 28 Aug 1864 Ft Monroe, Sheldon to the General-in-Chief, Washington, from Lt. Col. T. D. Hart on the arrival of the 104th Pa. Vols from Hilton Head; trailing second text unread (FM-R4a; row 5781/1; transcription-only)'),
 "F4": ("E253", 'Page 245 | 5789 | mssEC 25 (obj 5952, pointer 5789), 8 Oct 1864 Ft Monroe, Sheldon to Maj. Eckert, fever at Morehead City, signed Gilmore (FM-R4a; row 5789/1; transcription-only)'),
 "F5": ("E254", "Page 285 | 5829 | mssEC 25 (obj 5952, pointer 5829), 12 Dec 1864 Washington, B. W. Brice (Acting Paymaster General) to Sheldon at Ft Monroe, pay of officers via Maj. Binney; the sent copy with partly clear text is mssEC 18 pointer 9913 Page 247 (FM-R4a; row 5829/0; transcription-only)"),
 "F6": ("E255", 'Page 253 | 5797 | mssEC 25 (obj 5952, pointer 5797), 17 Oct 1864 8 PM Nashville, J. C. Van Duzer to S. H. Beckwith (marked "U. S."), Sherman and Hood at Ship\'s Gap; in print as Van Duzer to Eckert, OR I/39 pt 3 (FM-R4a; row 5797/0; transcription-only)'),
 "F7": ("E256", 'Page 208 | 5752 | mssEC 25 (obj 5952, pointer 5752), 16 and 17 June 1864 Ft Monroe, Sheldon to Maj. Eckert: material for Col. Pettus (signed Channing Clapp) and a boat report on the crossing of the James (FM-R4a; row 5752/1; transcription-only)'),
 "F9": ("E257", "Page 230 | 5774 | mssEC 25 (obj 5952, pointer 5774), 25 July 1864 2 PM Ft Monroe, Sheldon to J. W. Sampson, Baltimore, for Com. Purviance, light-house inspector: light-ship moved to the Elizabeth River obstructions; a clear copy stands at pointer 4823, Page 382 (FM-R4a; row 5774/0; transcription-only)"),
 "F10": ("E258", 'Page 237 | 5781 | mssEC 25 (obj 5952, pointer 5781), 28 Aug 1864 4 PM Ft Monroe, from Hilton Head 26 Aug, to Maj. Eckert for the General-in-Chief: the 104th Pa. Vols by the Fulton, signed Foster (FM-R4a; row 5781/0; transcription-only)'),
}
blocks = {}; cur = None
for ln in (HERE/"fm_r4a_entries.txt").read_text(encoding="utf-8").splitlines():
    m = re.match(r"### (F\d+) \|", ln)
    if m: cur = m.group(1); blocks[cur] = []; continue
    if cur and ln.strip(): blocks[cur].append(ln)
p = HERE.parent/"ciphertext.txt"; txt = p.read_text(encoding="utf-8")
add = [f"### {nid} | {desc}\n" + "\n".join(blocks[k]) + "\n" for k, (nid, desc) in MAP.items() if f"### {nid} |" not in txt]
if not add: print("nothing to add")
elif "--dry" in sys.argv: print("would add", len(add))
else: p.write_text(txt.rstrip("\n") + "\n\n" + "\n".join(add), encoding="utf-8"); print("added", len(add))
