#!/usr/bin/env python3
"""FM-R2a: file the ten Fort Monroe (mssEC 25 / obj 5952) entries of fm_r2a_entries.txt into ../ciphertext.txt (Cipher No. 1) as E170-E179.
Usage: python3 fm_r2a_file.py [--dry]   Idempotent: skips an ID already present."""
import re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
MAP = {
 "F1": ("E170", "Page 262 | 5806 | mssEC 25 (obj 5952, pointer 5806), 5 Nov 1864 Ft Monroe, Geo. D. Sheldon to S. H. Beckwith, City Point, reply to Beckwith's dispatch above it (FM-R2a, 8 Oct 2026; row 5806/1; image-read)"),
 "F2": ("E171", "Page 235 | 5779 | mssEC 25 (obj 5952, pointer 5779), 20 Aug 1864 Ft Monroe, Sheldon to Maj. Eckert, forwarding Col. W. Heine's arrival report (FM-R2a; row 5779/1; image-read)"),
 "F3": ("E172", "Page 243 | 5787 | mssEC 25 (obj 5952, pointer 5787), 6 Oct 1864 8 P.M. Ft Monroe, Sheldon to Maj. Eckert, for E. L. Wentz, forwarding a Gen. Ingalls message on a railroad extension; continues on page 244 (FM-R2a; row 5787/2; page 243 image-read, the continuation from the transcription)"),
 "F4": ("E173", "Page 296 | 5840 | mssEC 25 (obj 5952, pointer 5840), 26 Dec 1864 Ft Monroe, Sheldon to R. O'Brien, Hd. Qrs. A. J., for Gen. Turner (FM-R2a; row 5840/0; image-read)"),
 "F5": ("E174", "Page 203 | 5747 | mssEC 25 (obj 5952, pointer 5747), 14 June 1864 Ft Monroe, Sheldon to R. O'Brien, Butler's Hd. Qrs., answering O'Brien's two telegrams of 13 June on the same page (FM-R2a; row 5747/2; image-read)"),
 "F6": ("E175", "Page 294 | 5838 | mssEC 25 (obj 5952, pointer 5838), 19 Dec 1864 Ft Monroe, Sheldon to Maj. T. T. Eckert, monitors Dictator, Pontoosuc, Saugus, Nereus (FM-R2a; row 5838/0; image-read)"),
 "F7": ("E176", "Page 276 | 5820 | mssEC 25 (obj 5952, pointer 5820), 8 Dec 1864 Bermuda Hundreds, S. H. Beckwith to Sheldon, embarkation list by steamer (FM-R2a; row 5820/0; image-read)"),
 "F8": ("E177", "Page 279 | 5823 | mssEC 25 (obj 5952, pointer 5823), 8 Dec 1864 Hd Qrs A. of J., R. O'Brien to Sheldon, steamers for Monroe (FM-R2a; row 5823/0; image-read)"),
 "F9": ("E178", "Page 294 | 5838 | mssEC 25 (obj 5952, pointer 5838), 20 Dec 1864 Ft Monroe, Sheldon to Maj. Eckert, six steamers ordered out in bad weather (FM-R2a; row 5838/2; image-read)"),
 "F10": ("E179", "Page 56 | 5600 | mssEC 25 (obj 5952, pointer 5600), 11 Apr 1864 Ft Monroe, Sheldon to Maj. Eckert, requisition of tents and ferry boats (FM-R2a; row 5600/0; image-read)"),
}
blocks = {}; cur = None
for ln in (HERE/"fm_r2a_entries.txt").read_text(encoding="utf-8").splitlines():
    m = re.match(r"### (F\d+) \|", ln)
    if m: cur = m.group(1); blocks[cur] = []; continue
    if cur and ln.strip(): blocks[cur].append(ln)
p = HERE.parent/"ciphertext.txt"; txt = p.read_text(encoding="utf-8")
add = [f"### {nid} | {desc}\n" + "\n".join(blocks[k]) + "\n" for k, (nid, desc) in MAP.items() if f"### {nid} |" not in txt]
if not add: print("nothing to add")
elif "--dry" in sys.argv: print("would add", len(add))
else: p.write_text(txt.rstrip("\n") + "\n\n" + "\n".join(add), encoding="utf-8"); print("added", len(add))
