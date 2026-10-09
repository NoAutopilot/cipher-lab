#!/usr/bin/env python3
"""FM-R3b: file nine Fort Monroe (mssEC 25 / obj 5952) entries of fm_r3b_entries.txt into ../ciphertext.txt (Cipher No. 1) as E220, E222-E229.
F2 (5587/1, 17 Mar 1864, plain-text restatement of E168, AUDIT.md l.6056) is not filed as a cipher entry: E221 is left unused.
Usage: python3 fm_r3b_file.py [--dry]   Idempotent. Text = Huntington transcription; every page image-read at 2400 px (FM-R3b)."""
import re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
def d(page, ptr, row, rest): return f"Page {page} | {ptr} | mssEC 25 (obj 5952, pointer {ptr}), {rest} (FM-R3b; row {row}; image-read at 2400 px)"
MAP = {
 "F1": ("E220", d(267, 5811, "5811/2", "29 Nov 1864 Ft Monroe, Sheldon to Maj. Eckert, for Rucker: the steamers he will send that night, answering Eckert's call of the same day on the page")),
 "F3": ("E222", d(203, 5747, "5747/1", "13 June 1864 3.30 PM, R. O'Brien (Gen. Butler's Hd Qrs) to Sheldon, for Biggs: ferry boats and lumber to Fort Powhatan")),
 "F4": ("E223", d(279, 5823, "5823/2", "9 Dec 1864 Ft Monroe, Sheldon to Maj. Eckert, for Surgeon Barns, from Charles McCormick, Medical Director")),
 "F5": ("E224", d(157, 5701, "5701/1", "27 May 1864 10.30 AM, R. O'Brien (Gen. Butler's Hd Qrs) to Sheldon: Captain Farquhar ordered to report to W. F. Smith as chief engineer")),
 "F6": ("E225", d(82, 5626, "5626/0", "23 Apr 1864 Ft Monroe, Sheldon to S. H. Beckwith, Culpeper, for Grant: a scout's report of Longstreet at Charlottesville, signed John I. Davenport")),
 "F7": ("E226", d(204, 5748, "5748/0", "14 June 1864 Ft Monroe, Sheldon to Maj. Eckert, for Allen: mail boats to Charles City Landing, H. B. Blood")),
 "F8": ("E227", d(264, 5808, "5808/1", "6 Nov 1864 Ft Monroe, Sheldon to John Horner, New York, for Capt. D. Stinson: Ninth Vermont draft")),
 "F9": ("E228", d(270, 5814, "5814/1", "1 Dec 1864 Ft Monroe, Sheldon to Maj. Eckert, for the Chief of the Bureau of Ordnance: torpedoes invented by Mr Woods")),
 "F10": ("E229", d(289, 5833, "5833/0", "14 Dec 1864 Ft Monroe, Sheldon to Maj. Eckert, Washington: the press despatch on Foster and Pocotaligo bridge")),
}
blocks = {}; cur = None
for ln in (HERE/"fm_r3b_entries.txt").read_text(encoding="utf-8").splitlines():
    m = re.match(r"### (F\d+) \|", ln)
    if m: cur = m.group(1); blocks[cur] = []; continue
    if cur and ln.strip(): blocks[cur].append(ln)
p = HERE.parent/"ciphertext.txt"; txt = p.read_text(encoding="utf-8")
add = [f"### {nid} | {desc}\n" + "\n".join(blocks[k]) + "\n" for k, (nid, desc) in MAP.items() if f"### {nid} |" not in txt]
if not add: print("nothing to add")
elif "--dry" in sys.argv: print("would add", len(add))
else: p.write_text(txt.rstrip("\n") + "\n\n" + "\n".join(add), encoding="utf-8"); print("added", len(add))
