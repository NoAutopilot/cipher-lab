#!/usr/bin/env python3
"""MS18-R10: file X7 (the one mssEC 18 No. 1 row that missed step 0) of ms18_r10_entries.txt into ../ciphertext.txt as E420. Usage: ms18_r10_file.py [--dry]  Idempotent.
Image check: all ten leaves (2400 px IIIF, to scratch) were read on the entry's own lower/upper lines; none was a full-entry read: see NOTES MS18-R10."""
import re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
def d(page, ptr, row, pp, rest, chk, led="mssEC 18 (obj 10074"): return f"Page {page} | {ptr} | {led}, pointer {ptr}; printed page {pp}), {rest} (MS18-R10; row {row}; {chk})"
I = "leaf image-read at 2400 px (whole entry)"
DROP = {}
BOOK = "MS18-R10: No. 1 (whole-entry vocabulary share No.1 / No.2 / No.9 = "
MAP = {
 "X7": ("E420", d(130, 9790, "9790/1", 124, "13 July 1864 Washington (hour 3 PM), R. R. McCaine (operator), for Maj. Gen. David Hunter, signed [Halleck] (ledger 'why so slow' after the signature words; print H. W. Halleck, Major-General and Chief of Staff): the enemy left our front in the night and seem to be moving toward Edwards Ferry; General Wright will follow by the River road with about 12,000 men; it is hoped that your forces and those of General Howe will form a junction with him at that place; the rebel force is probably about the same as that you encountered in the Valley and is estimated at over 20,000; printed OR I/37 pt 2 (before the head of Boreman's letter, p.291 or 292)", I),
  ["note: " + BOOK + ".58/.46/.38): No. 1 (No. 9 reads 20 groups of nonsense; sense decides). Step 0 (Wave 3 ruling, ms18_r10_step0.py): (a) 0.439 (18/41), (b) p95 0.195, MISS (the holder transcription is the cipher text itself plus its plain words); (c) key-dependent words: David, enemy, Ferry, follow, force, front, general, Hunter, junction, major, men, nineteen, rebel, river, road, twelve, twenty, Valley. Printed OR I/37 pt 2 (IA warofrebellion372unit, cached text): Halleck to Hunter, Washington 13 July 1864 3 p.m., word for word ('The enemy left our front in the night, and seem to be moving toward Edwards Ferry. General Wright will follow by the River road with about 12,000 men. It is hoped that your forces and those of General Howe will form a junction with him at that place. The rebel force is probably about the same as that you encountered in the Valley, and is estimated at over 20,000'); C against the print; the page number is 291 or 292 by the running head in the OCR text (not read on the image). The print's 'in the Valley' is the ledger's 'stephen world' (key reading [In the] [Valley]); the ledger's tail 'Jordan why so slow' is the signature group and a null phrase (M). Image (ledger page 124, whole entry on the crop): the transcription matches line by line; the header carries no hour (the 3 PM is the code group 'Fever'/'Imogene' pair, read by the key, matching the print's 3 p.m.). No Huntington clear copy: 3 CISOSEARCHALL queries 0 hits (positive control returned 9678)."]),
}
blocks = {}; cur = None
for ln in (HERE/"ms18_r8_entries.txt").read_text(encoding="utf-8").splitlines():
    m = re.match(r"### (X\d+) \|", ln)
    if m: cur = m.group(1); blocks[cur] = []; continue
    if cur and ln.strip() and ln.strip() not in DROP.get(cur, []): blocks[cur].append(ln)
p = HERE.parent/"ciphertext.txt"; txt = p.read_text(encoding="utf-8")
add = [f"### {nid} | {desc}\n" + "\n".join(blocks[k] + notes) + "\n" for k, (nid, desc, notes) in MAP.items() if f"### {nid} |" not in txt]
if add and "--dry" not in sys.argv: p.write_text(txt.rstrip("\n") + "\n\n" + "\n".join(add), encoding="utf-8")
print(("would add " if "--dry" in sys.argv else "added ") + str(len(add)))
