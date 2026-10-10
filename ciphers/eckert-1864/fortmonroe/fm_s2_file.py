#!/usr/bin/env python3
"""FM-S2: file F9 (5768/3) of fm_s2_entries.txt into ../ciphertext.txt (Cipher No. 1) as E465. The other nine rows are not filed (Step-0 ruling: hit).
Usage: python3 fm_s2_file.py [--dry]  Idempotent. Image-read at 2400 px (own entry), 10 Oct 2026."""
import re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
desc = ("Page 224 | 5768 | mssEC 25 (obj 5952, pointer 5768), 10 July 1864 Ft Monroe 10.15 AM, Sheldon for the General-in-Chief at Washington, "
        "carrying Col. J. W. Shaffer's words: none of the New Orleans troops (the 19th Army Corps of the sibling entries on the page) have arrived yet; "
        "shorter twin of the Rawlins/Beckwith entry 5768/2 (FM-S2; row 5768/3; image-read at 2400 px)")
notes = ["note: FM-S2: Step 0 (fm_s2_step0.py): (a) 0.385 (5/13), (b) p95 0.308, MISS; (c) key-dependent words: five, general, New Orleans, troops, twenty, Washington. "
         "The time reads 10.15 AM (feeble = 10, ghost = 15; the decoder prints [25], a numeral-combination quirk; the sibling 5768/2 header says 10.15 AM). "
         "whiskey = Troops is S (key row), supported by sibling 5768/1 'troops arriving from New Orleans'. Indian = General-in-Chief is H but an odd address for 10 July 1864 (Halleck was Chief of Staff): M for who is meant. "
         "Not in print: phrase grep over 164 cached volumes, Huntington CISOSEARCHALL (no clear copy), be-api: none located."]
txt = (HERE.parent/"ciphertext.txt").read_text(encoding="utf-8")
blk = None; cur = False; out = []
for ln in (HERE/"fm_s2_entries.txt").read_text(encoding="utf-8").splitlines():
    if ln.startswith("### "): cur = ln.startswith("### F9 |"); continue
    if cur and ln.strip(): out.append(ln)
add = f"### E465 | {desc}\n" + "\n".join(out + notes) + "\n"
if "### E465 |" in txt: print("already present")
elif "--dry" in sys.argv: print("would add\n" + add)
else: (HERE.parent/"ciphertext.txt").write_text(txt.rstrip("\n") + "\n\n" + add, encoding="utf-8"); print("added E465")
