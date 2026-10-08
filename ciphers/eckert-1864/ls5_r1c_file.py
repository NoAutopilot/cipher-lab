#!/usr/bin/env python3
"""LS5-R1c: file the read entries of ls5_r1c_entries.txt into ciphertext.txt (Cipher No. 1) and ciphertext-no2.txt (Cipher No. 2).
Usage: python3 ls5_r1c_file.py [--dry]   Idempotent: skips an ID already present. IDs fixed here after a fetch (rule: next free IDs)."""
import re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
MAP = {
 "Y1":  ("no1", "E103", "Page 235 | 9129 | 28 Nov 1864 10.30 AM, J. C. Van Duzer (LS5-R1c, 8 Oct 2026; row 9129/1; image-read)"),
 "Y2":  ("no1", "E104", "Page 15 | 8907 | 4 Mar 1864, operator Caldwell (HQ Army of the Potomac), for Humphreys (LS5-R1c; row 8907/1; image-read)"),
 "Y5":  ("no1", "E105", "Page 180 | 9072 | 12 Sept 1864, operator Carey at Lexington (LS5-R1c; row 9072/0; image-read)"),
 "Y9":  ("no1", "E106", "Page 77 | 8969 | 22 May 1864 10.30 PM, R. R. McCaine, entry struck through and marked 'Not sent' (LS5-R1c; row 8969/3; image-read)"),
 "Y10": ("no1", "E107", "Page 90 | 8982 | 11 June 1864, Sam Bruch at Louisville (LS5-R1c; row 8982/2; image-read)"),
 "Y12": ("no1", "E108", "Page 104 | 8996 | 6 July 1864, R. R. McCaine at Parkersburg (LS5-R1c; row 8996/0; image-read)"),
 "Y3":  ("no2", "N2-DA", "Page 128 | 9020 | 28 July 1864 9 AM (cipher time word), S. H. Beckwith (LS5-R1c; row 9020/1; image-read; first tried against No. 1, read as No. 2)"),
 "Y6":  ("no2", "N2-DB", "Page 198 | 9090 | 10 Oct 1864 10.50 AM, Beckwith at City Point (LS5-R1c; row 9090/1; image-read; first tried against No. 1, read as No. 2)"),
}
blocks = {}; cur = None
for ln in (HERE/"ls5_r1c_entries.txt").read_text(encoding="utf-8").splitlines():
    m = re.match(r"### (Y\d+) \|", ln)
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
