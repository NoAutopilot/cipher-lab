#!/usr/bin/env python3
"""FM-R1: file the ten Fort Monroe (mssEC 25 / obj 5952) entries of fm_r1_entries.txt into ../ciphertext.txt (Cipher No. 1) as E160-E169.
Usage: python3 fm_r1_file.py [--dry]   Idempotent: skips an ID already present."""
import re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
MAP = {
 "F1": ("E160", "Page 258 | 5802 | mssEC 25 (obj 5952, pointer 5802), 2 Nov 1864 Hd Qrs A. of J., R. O'Brien to Geo. D. Sheldon, Ft Monroe (FM-R1, 8 Oct 2026; row 5802/2; image-read)"),
 "F2": ("E161", "Page 228 | 5772 | mssEC 25 (obj 5952, pointer 5772), 13 July 1864 Baltimore, J. W. Sampson to Sheldon, forwarding Lieut. D. L. Braine's Annapolis telegram (FM-R1; row 5772/0; image-read)"),
 "F3": ("E162", "Page 258 | 5802 | mssEC 25 (obj 5952, pointer 5802), 1 Nov 1864 Butler's Hd Qrs, R. O'Brien to Sheldon (FM-R1; row 5802/0; image-read)"),
 "F4": ("E163", "Page 279 | 5823 | mssEC 25 (obj 5952, pointer 5823), 9 Dec 1864 Butler's Hd, R. O'Brien to Sheldon (FM-R1; row 5823/1; transcription only)"),
 "F5": ("E164", "Page 120 | 5664 | mssEC 25 (obj 5952, pointer 5664), 10 May 1864 Bermuda Landing, R. O'Brien to Sheldon (FM-R1; row 5664/0; transcription only)"),
 "F6": ("E165", "Page 264 | 5808 | mssEC 25 (obj 5952, pointer 5808), 14 Nov 1864 Washington, T. T. Eckert to Sheldon (FM-R1; row 5808/2; transcription only)"),
 "F7": ("E166", "Page 236 | 5780 | mssEC 25 (obj 5952, pointer 5780), 20 Aug 1864 Fortress Monroe, Sheldon to Maj. Eckert, forwarding a Hilton Head dispatch (FM-R1; row 5780/0; transcription only)"),
 "F8": ("E167", "Page 274 | 5818 | mssEC 25 (obj 5952, pointer 5818), 6 Dec 1864 New York, John Horner to Sheldon (FM-R1; row 5818/0; transcription only)"),
 "F9": ("E168", "Page 40 | 5584 | mssEC 25 (obj 5952, pointer 5584), 17 Mar 1864 Washington, H. W. Halleck (signed) to Sheldon, text written forward then in reverse word order (FM-R1; row 5584/1; image-read)"),
 "F10": ("E169", "Page 238 | 5782 | mssEC 25 (obj 5952, pointer 5782), 9 Sept 1864 Washington, T. T. Eckert to Sheldon, Beckwith and Caldwell (FM-R1; row 5782/1; transcription only)"),
}
blocks = {}; cur = None
for ln in (HERE/"fm_r1_entries.txt").read_text(encoding="utf-8").splitlines():
    m = re.match(r"### (F\d+) \|", ln)
    if m: cur = m.group(1); blocks[cur] = []; continue
    if cur and ln.strip(): blocks[cur].append(ln)
p = HERE.parent/"ciphertext.txt"; txt = p.read_text(encoding="utf-8")
add = [f"### {nid} | {desc}\n" + "\n".join(blocks[k]) + "\n" for k, (nid, desc) in MAP.items() if f"### {nid} |" not in txt]
if not add: print("nothing to add")
elif "--dry" in sys.argv: print("would add", len(add))
else: p.write_text(txt.rstrip("\n") + "\n\n" + "\n".join(add), encoding="utf-8"); print("added", len(add))
