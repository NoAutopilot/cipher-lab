#!/usr/bin/env python3
"""FM-R6a: file the four Fort Monroe (mssEC 25 / obj 5952) entries of fm_r6a_entries.txt into ../ciphertext.txt (Cipher No. 1) as E300-E303.
Usage: python3 fm_r6a_file.py [--dry]   Idempotent: skips an ID already present."""
import re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
MAP = {
 "F1": ("E300", 'Page 95 | 5639 | mssEC 25 (obj 5952, pointer 5639), 29 Apr 1864 Ft Monroe, Sheldon to Maj. Eckert for the Secretary of the Navy: Butler informs that Plymouth is evacuated and the rebels are leaving North Carolina, signed S. P. Lee, 2 PM via Monroe, with a second message for Eckert to say what to do; the same words are in print (ORN I/9, OR I/33 and Butler IV, volumes matched by phrase, pages not located); no clear copy found at another pointer (FM-R6a, 9 Oct 2026; row 5639/1; image-read at the tail, transcription agrees)'),
 "F2": ("E301", 'Page 220 | 5764 | mssEC 25 (obj 5952, pointer 5764), 21 June 1864 Ft Monroe, Sheldon to Maj. Eckert for the Secretary of the Navy: flag-ship Malvern, Farrars Island 10.30 PM 20th, no change in the naval situation, look out that the rebel ironclads are taking on board sand in bags, signed S. P. Lee; a clear period copy stands at pointer 10435, Page 293, and ORN I/10 prints it (FM-R6a; row 5764/0; transcription-only, the image strip read was another entry on a shared page)'),
 "F3": ("E302", 'Page 153 | 5697 | mssEC 25 (obj 5952, pointer 5697), 27 May 1864 Ft Monroe, Sheldon to Maj. Eckert: reply on the telegraph line if White House is made the base of supplies, West Point depot, route from Gloucester Point by Yorktown to West Point, chestnut poles on the railroad, little wire on hand; the question it answers stands clear at pointer 5696, Page 152; no print of this reply found in the volumes searched (FM-R6a; row 5697/1; image-read at its middle lines, transcription agrees)'),
 "F4": ("E303", 'Page 253 | 5797 | mssEC 25 (obj 5952, pointer 5797), 17 Oct 1864 Nashville, B. B. Glass to S. H. Beckwith at City Point for the General-in-Chief: Sherman from Ship\'s Gap 16 Oct (Hood, Snake Creek pass, railroad repair) and Thomas (Roddy moved from Tuscumbia), continues at pointer 5798; no print found in the volumes searched (FM-R6a; row 5797/1; image-read at the head lines, transcription agrees)'),
}
blocks = {}; cur = None
for ln in (HERE/"fm_r6a_entries.txt").read_text(encoding="utf-8").splitlines():
    m = re.match(r"### (F\d+) \|", ln)
    if m: cur = m.group(1); blocks[cur] = []; continue
    if cur and ln.strip(): blocks[cur].append(ln)
p = HERE.parent/"ciphertext.txt"; txt = p.read_text(encoding="utf-8")
add = [f"### {nid} | {desc}\n" + "\n".join(blocks[k]) + "\n" for k, (nid, desc) in MAP.items() if f"### {nid} |" not in txt]
if not add: print("nothing to add")
elif "--dry" in sys.argv: print("would add", len(add))
else: p.write_text(txt.rstrip("\n") + "\n\n" + "\n".join(add), encoding="utf-8"); print("added", len(add))
