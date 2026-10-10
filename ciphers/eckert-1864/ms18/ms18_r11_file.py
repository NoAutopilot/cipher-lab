#!/usr/bin/env python3
"""MS18-R11: file X4 (9730/0, the one row that missed step 0) of ms18_r11_entries.txt into ../ciphertext.txt as E430. Usage: ms18_r11_file.py [--dry]  Idempotent.
Image check: leaf 9730 at 2400 px (IIIF, scratch), whole entry read; transcription matches line by line."""
import re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
desc = ("Page 70 | 9730 | mssEC 18 (obj 10074, pointer 9730; printed page 64), 4 May 1864 Washington 2.30 PM, operator Geo. D. Sheldon, for [Maj. Gen. B. F. Butler], signed [Halleck]: "
 "Grant's army has crossed the Rapidan; relays Grant's message from Germanna Ford for Halleck ('The crossing of the Rapidan effected. Forty-eight hours now will demonstrate whether the enemy intends giving battle this side of Richmond. Telegraph Butler that we have crossed the Rapidan'); "
 "Grant's text printed OR I/36 pt 1 (Germanna Ford 4 May 1864, rec'd 1.50 p.m.; page not read) and Butler's Private and Official Correspondence vol. IV (IA privateofficialc04butl, pp.161-162 by OCR); Halleck's short cover text printed OR I/36 pt 2 p.391 by OCR running heads (MS18-R11; row 9730/0; leaf image-read at 2400 px, whole entry)")
note = ("note: MS18-R11: No. 1 (whole-entry vocabulary share No.1/No.2/No.9 = .72/.57/.28; read by sense, count control non-discriminating: shuffled copy H30 = H30). Step 0 (ms18_r11_step0.py): (a) 0.091 (1/11), (b) p95 0.091, MISS "
 "(the holder transcription of page 9730 carries the cipher text and its plain words only); (c) key-dependent words: army, Butler, cross, general, Grant, major, Rapidan. Printed: the Grant message word for word in OR I/36 pt 1 and Butler Corr. IV; "
 "the Halleck relay as sent to Butler is printed only in the short form 'General Grant's army has crossed the Rapidan' (OR I/36 pt 2 p.391; Butler Corr. IV 'Lt. General Grant Comd'g has crossed the Rapidan', 3 p.m.), so the ledger's wording 'Here is Grant's message from Germanna Ford for Halleck' is not located as such. Holder clear copy: 3 CISOSEARCHALL queries 0 hits (control 9678).")
src = (HERE/"ms18_r11_entries.txt").read_text(encoding="utf-8")
m = re.search(r"### X4 \|[^\n]*\n(.*?)(?=\n### X5|\Z)", src, re.S)
body = [l for l in m.group(1).splitlines() if l.strip()]
p = HERE.parent/"ciphertext.txt"; txt = p.read_text(encoding="utf-8")
if "### E430 |" not in txt and "--dry" not in sys.argv:
    p.write_text(txt.rstrip("\n") + f"\n\n### E430 | {desc}\n" + "\n".join(body + [note]) + "\n", encoding="utf-8")
    print("added 1")
