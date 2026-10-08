#!/usr/bin/env python3
"""LS5-R1d: file the read entries of ls5_r1d_entries.txt into ciphertext.txt (Cipher No. 1) and ciphertext-no2.txt (No. 2).
Usage: python3 ls5_r1d_file.py [--dry]   Idempotent: skips an ID already present."""
import re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
MAP = {
 "X1": ("no1", "E120", "Page 151 | 9043 | 11 Aug 1864 3 PM, S. H. Beckwith (to Lieut. Col. T. S. Bowers, Grant's staff) (LS5-R1d, 8 Oct 2026; row 9043/0; image-read)"),
 "X2": ("no1", "E121", "Page 157 | 9049 | 16 Aug 1864 8.30 PM, McCaine (LS5-R1d; row 9049/1; image-read)"),
 "X3": ("no1", "E122", "Page 161 | 9053 | 21 Aug 1864 4 PM, McCaine at Winchester, signed Augur (LS5-R1d; row 9053/2; image-read)"),
 "X4": ("no1", "E123", "Page 170 | 9062 | 3 Sept 1864 8.30 PM, to Peck (LS5-R1d; row 9062/2; image-read)"),
 "X5": ("no1", "E124", "Page 194 | 9086 | 2 Oct 1864 12 m, Beckwith at City Point, signed Geo K Leet (LS5-R1d; row 9086/1; image-read)"),
 "X7": ("no1", "E125", "Page 221 | 9113 | 4 Nov 1864, H. F. Schermerhorn(?), to Stevenson (LS5-R1d; row 9113/1; image-read)"),
 "X8": ("no1", "E126", "Page 75 | 8967 | 21 May 1864 10 AM, J. C. Van Duzer, Nashville (LS5-R1d; row 8967/2; image-read)"),
 "X6": ("no2", "N2-EA", "Page 196 | 9088 | 8 Oct 1864 2 PM, Beckwith at Fort Monroe, signed Geo K Leet (LS5-R1d; row 9088/1; first tried as No. 1, read as No. 2; image-read)"),
}
blocks = {}; cur = None
for ln in (HERE/"ls5_r1d_entries.txt").read_text(encoding="utf-8").splitlines():
    m = re.match(r"### (X\d+) \|", ln)
    if m: cur = m.group(1); blocks[cur] = []; continue
    if cur and ln.strip(): blocks[cur].append(ln)
out = {"no1": [], "no2": []}
for k, (f, nid, desc) in MAP.items():
    out[f].append((nid, f"### {nid} | {desc}\n" + "\n".join(blocks[k]) + "\n"))
for f, fn in (("no2", "ciphertext-no2.txt"), ("no1", "ciphertext.txt")):
    p = HERE/fn; txt = p.read_text(encoding="utf-8")
    add = [b for nid, b in out[f] if f"### {nid} |" not in txt]
    if not add: print(fn, "nothing to add"); continue
    if "--dry" in sys.argv: print(fn, "would add", len(add)); continue
    p.write_text(txt.rstrip("\n") + "\n\n" + "\n".join(add), encoding="utf-8"); print(fn, "added", len(add))
