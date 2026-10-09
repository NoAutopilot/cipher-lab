#!/usr/bin/env python3
"""FM-R5a: file the ten Fort Monroe (mssEC 25 / obj 5952) entries of fm_r5a_entries.txt into ../ciphertext.txt (Cipher No. 1) as E270-E279.
Usage: python3 fm_r5a_file.py [--dry]   Idempotent: skips an ID already present."""
import re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
MAP = {
 "F1": ("E270", 'Page 257 | 5801 | mssEC 25 (obj 5952, pointer 5801), 1 Nov 1864 Ft Monroe, R. O\'Brien (Butler\'s Hd Qrs, Army of the James) to Sheldon, for Maj. Gen. Terry near Varina: Butler leaves for Washington, Lt. Col. Smith to attend (FM-R5a, 9 Oct 2026; row 5801/0; image-read, transcription agrees; no clear copy found at another pointer)'),
 "F2": ("E271", 'Page 128 | 5641 | mssEC 25 (obj 5952, pointer 5641), 1 May 1864 Ft Monroe, Sheldon to S. H. Beckwith at Culpepper for Grant: one iron-clad arrived, two more due, four gunboats due, Gillmore not yet arrived; a clear period copy stands at pointer 4587, Page 146, and Butler\'s Private and Official Correspondence IV prints it; trailing second text ("would it meet your views to have new Man at ...", signed S.) not matched to a clear copy (FM-R5a; row 5641/1; transcription-only)'),
 "F3": ("E272", 'Page 237 | 5768 | mssEC 25 (obj 5952, pointer 5768), 10 July 1864 10.15 AM Ft Monroe, S. H. Beckwith (Hd Qrs U.S.A.) to Sheldon, for Brig. Gen. John A. Rawlins: none of the 19th Corps has arrived, signed J. W. Shaffer (FM-R5a; row 5768/2; image-read at the date line and tail; no clear copy found)'),
 "F4": ("E273", 'Page 234 | 5724 | mssEC 25 (obj 5952, pointer 5724), 31 May 1864 9.30 PM Ft Monroe, Sheldon to Maj. Eckert for the Quartermaster General: pay-steamer not obstructed to White House, enemy reported at mouth of the Chickahominy with a pontoon train, signed Herman Biggs; a clear period copy stands at pointer 10376, Page 234 (FM-R5a; row 5724/2; transcription-only)'),
 "F5": ("E274", 'Page 152 | 5645 | mssEC 25 (obj 5952, pointer 5645), 2 May 1864 4.30 PM Ft Monroe, Sheldon to S. H. Beckwith for Gen. Grant: letter from Gillmore, he comes with the last detachment, signed Butler; a clear period copy stands at pointer 4593, Page 152 (FM-R5a; row 5645/2; transcription-only)'),
 "F6": ("E275", 'Page 280 | 5824 | mssEC 25 (obj 5952, pointer 5824), 9 Dec 1864 3.30 PM Ft Monroe, Sheldon to Maj. Eckert for Capt. Allen, Quartermaster: no boots to spare, signed Capt. James, Quartermaster (FM-R5a; row 5824/0; image-read, transcription agrees; no clear copy found)'),
 "F7": ("E276", 'Page 52 | 5582 | mssEC 25 (obj 5952, pointer 5582), 12 Mar 1864 Ft Monroe, Sheldon to Maj. Gen. Pleasonton from Kilpatrick: men all embarked by tomorrow noon, will report in person Tuesday; a clear period copy stands at pointer 4493, Page 52, and OR I/33 prints it (FM-R5a; row 5582/1; transcription-only)'),
 "F8": ("E277", 'Page 258 | 5802 | mssEC 25 (obj 5952, pointer 5802), 2 Nov 1864 Ft Monroe, R. O\'Brien (Hd Qrs A. of J.) to Sheldon, for Col. Howard, chief of artillery: strength of batteries and style of guns, signed Fred Martin (FM-R5a; row 5802/1; image-read, transcription agrees; no clear copy found)'),
 "F9": ("E278", 'Page 285 | 5829 | mssEC 25 (obj 5952, pointer 5829), 13 Dec 1864 1 PM Ft Monroe, Sheldon to S. H. Beckwith at City Point for Gen. Ingalls: the few remaining vessels of the fleet to get away this evening (FM-R5a; row 5829/2; image-read, transcription agrees; no clear copy found)'),
 "F10": ("E279", 'Page 96 | 5609 | mssEC 25 (obj 5952, pointer 5609), 17 Apr 1864 8 PM Ft Monroe, Sheldon to Maj. Eckert for the Quartermaster General: Gillmore has no shelter tents, 20,000 asked, signed Butler; a clear period copy stands at pointer 10238, Page 96 (FM-R5a; row 5609/0; transcription-only)'),
}
blocks = {}; cur = None
for ln in (HERE/"fm_r5a_entries.txt").read_text(encoding="utf-8").splitlines():
    m = re.match(r"### (F\d+) \|", ln)
    if m: cur = m.group(1); blocks[cur] = []; continue
    if cur and ln.strip(): blocks[cur].append(ln)
p = HERE.parent/"ciphertext.txt"; txt = p.read_text(encoding="utf-8")
add = [f"### {nid} | {desc}\n" + "\n".join(blocks[k]) + "\n" for k, (nid, desc) in MAP.items() if f"### {nid} |" not in txt]
if not add: print("nothing to add")
elif "--dry" in sys.argv: print("would add", len(add))
else: p.write_text(txt.rstrip("\n") + "\n\n" + "\n".join(add), encoding="utf-8"); print("added", len(add))
