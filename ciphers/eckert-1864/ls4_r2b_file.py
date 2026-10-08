#!/usr/bin/env python3
"""LS4-R2b: file the read entries of ls4_r2b_entries.txt into ciphertext-no2.txt (Cipher No. 2) and ciphertext.txt (Cipher No. 1).
Usage: python3 ls4_r2b_file.py [--dry]   Idempotent: skips an ID already present. Headers carry the ledger page, pointer and the row."""
import re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
MAP = {  # working label -> (file, new ID, header description)
 "R2B-01": ("no2", "N2-CB", "Page 240 | 9132 | 1 Dec 1864 3 PM (cipher time word), S. H. Beckwith, to Billy (LS4-R2b, 8 Oct 2026; row 9132/0; image-read)"),
 "R2B-02": ("no2", "N2-CC", "Page 90 | 8982 | 11 June 1864, Kimber at Vicksburg, to Canby (LS4-R2b; row 8982/1; image-read)"),
 "R2B-03": ("no2", "N2-CD", "Page 94-95 | 8986, 8987 | 17 June 1864, S. H. Beckwith, to Grant (LS4-R2b; row 8986/1; image-read, runs on to the next page)"),
 "R2B-04": ("no2", "N2-CE", "Page 146-147 | 9039, 9040 | 9 Aug 1864 9.30 AM, F. T. Bickford (LS4-R2b; row 9040/0 is the tail of this entry; image-read)"),
 "R2B-05": ("no2", "N2-CF", "Page 160 | 9052 | 21 Aug 1864 1 PM (ledger), Beckwith at City Point (LS4-R2b; row 9052/1; image-read)"),
 "R2B-06": ("no2", "N2-CG", "Page 229 | 9121 | 11 Nov 1864 (cipher time word 3 PM), S. H. Beckwith, to Grant (LS4-R2b; row 9121/1; image-read)"),
 "R2B-07": ("no2", "N2-CH", "Page 230 | 9122 | 12 Nov 1864 9 AM, Beckwith, G. V. Fox to Grant (LS4-R2b; row 9122/2; image-read)"),
 "R2B-08": ("no2", "N2-CI", "Page 233 | 9125 | 19 Nov 1864, Beckwith at Burlington N. J., to Grant (LS4-R2b; row 9125/2; image-read)"),
 "R2B-09": ("no2", "N2-CJ", "Page 250 | 9142 | 18 Dec 1864, J. H. Emerick at City Point (LS4-R2b; row 9142/0, first telegram; image-read)"),
 "R2B-10": ("no2", "N2-CK", "Page 250 | 9142 | 18 Dec 1864 11.15 PM, Emerick at City Point, signed T. T. Eckert (LS4-R2b; row 9142/0, second telegram; image-read)"),
 "R2B-11": ("no2", "N2-CL", "Page 56 | 8948 | 26 Apr 1864 (ledger header read from the image; the volunteer text has 20), A. H. Caldwell (LS4-R2b; row 8948/2; image-read)"),
 "R2B-13": ("no2", "N2-CM", "Page 110-111 | 9002, 9003 | 15 July 1864, S. H. Beckwith (LS4-R2b; row 9003/0 is the tail on p.111 of this entry; image-read)"),
 "R2B-12": ("no1", "E102", "Page 79 | 8971 | 26 May 1864, operator Sam Bruch (LS4-R2b; row 8971/2; first tried as No. 2, read as No. 1; image-read)"),
}
blocks = {}
cur = None
for ln in (HERE/"ls4_r2b_entries.txt").read_text(encoding="utf-8").splitlines():
    m = re.match(r"### (R2B-\d+) \|", ln)
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
