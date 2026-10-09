#!/usr/bin/env python3
"""FM-R3a: file the ten Fort Monroe (mssEC 25 / obj 5952) entries of fm_r3a_entries.txt into ../ciphertext.txt (Cipher No. 1) as E210-E219.
Usage: python3 fm_r2a_file.py [--dry]   Idempotent: skips an ID already present."""
import re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
MAP = {
 "F1": ("E210", 'Page 93 | 5637 | mssEC 25 (obj 5952, pointer 5637), 28 Apr 1864 Ft Monroe, Sheldon to Maj. Eckert for Capt. H. S. Taft, signal officer, Washington; signer L. B. Norton, chief signal officer (FM-R3a, 9 Oct 2026; row 5637/2; image-read)'),
 "F2": ("E211", "Page 105 | 5649 | mssEC 25 (obj 5952, pointer 5649), 3 May 1864 Ft Monroe, Sheldon to Maj. Eckert for Fox, Asst. Secretary of the Navy, forwarding the 'little party of pleasure' telegram signed Butler, Yorktown 5 PM; the Yorktown copy (H. N. Snow, partly clear, 'Nankin' for the Navy title) stands above it on the page (FM-R3a; row 5649/2; image-read)"),
 "F3": ("E212", 'Page 223 | 5767 | mssEC 25 (obj 5952, pointer 5767), 7 July 1864 Washington, T. T. Eckert to Sheldon at Ft Monroe, for Lt. Col. Biggs, chief quartermaster: transportation to City Point, signed Quartermaster General (FM-R3a; row 5767/2; image-read)'),
 "F4": ("E213", 'Page 63 | 5607 | mssEC 25 (obj 5952, pointer 5607), 16 Apr 1864 Ft Monroe, Sheldon to Maj. Eckert, surplus telegraph material to go with the Tenth Corps (FM-R3a; row 5607/1; image-read)'),
 "F5": ("E214", 'Page 159 | 5703 | mssEC 25 (obj 5952, pointer 5703), 27 May 1864 Washington, T. T. Eckert to Sheldon at Ft Monroe, telegraph wire and insulators for West Point (FM-R3a; row 5703/1; image-read)'),
 "F6": ("E215", "Page 190 | 5734 | mssEC 25 (obj 5952, pointer 5734), 8 June 1864 Ft Monroe, Sheldon to Maj. Eckert, forwarding Acting Rear-Adm. S. P. Lee's telegram to the Secretary of the Navy from Trent's Reach, 7 June 10 PM (FM-R3a; row 5734/0; image-read)"),
 "F7": ("E216", 'Page 199 | 5743 | mssEC 25 (obj 5952, pointer 5743), 13 June 1864 4.20 PM Washington, T. T. Eckert to Sheldon at Ft Monroe, for Lt. Col. Biggs: vessels to White House, signed Quartermaster General (FM-R3a; row 5743/1; image-read)'),
 "F8": ("E217", "Page 226 | 5770 | mssEC 25 (obj 5952, pointer 5770), 10 July 1864 4.30 PM Ft Monroe, Sheldon to Maj. Eckert for the Quartermaster General, forwarding Ingalls's City Point message on transports for Gen. Wright's command (FM-R3a; row 5770/0; image-read)"),
 "F9": ("E218", "Page 224 | 5768 | mssEC 25 (obj 5952, pointer 5768), 9 July 1864 6 PM City Point, S. H. Beckwith to Sheldon at Ft Monroe, forwarding Grant's message to the commanding officer, Fort Monroe, on the 19th Corps (FM-R3a; row 5768/0; image-read)"),
 "F10": ("E219", "Page 236 | 5780 | mssEC 25 (obj 5952, pointer 5780), 27 Aug 1864 6.30 PM City Point, S. H. Beckwith to Sheldon at Ft Monroe, forwarding Ingalls's message: Gen. Grant to meet his family at Monroe, steamer Greyhound at his disposal (FM-R3a; row 5780/1; image-read)"),
}
blocks = {}; cur = None
for ln in (HERE/"fm_r3a_entries.txt").read_text(encoding="utf-8").splitlines():
    m = re.match(r"### (F\d+) \|", ln)
    if m: cur = m.group(1); blocks[cur] = []; continue
    if cur and ln.strip(): blocks[cur].append(ln)
p = HERE.parent/"ciphertext.txt"; txt = p.read_text(encoding="utf-8")
add = [f"### {nid} | {desc}\n" + "\n".join(blocks[k]) + "\n" for k, (nid, desc) in MAP.items() if f"### {nid} |" not in txt]
if not add: print("nothing to add")
elif "--dry" in sys.argv: print("would add", len(add))
else: p.write_text(txt.rstrip("\n") + "\n\n" + "\n".join(add), encoding="utf-8"); print("added", len(add))
