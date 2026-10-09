#!/usr/bin/env python3
"""FM-R6b: file three Fort Monroe (mssEC 25 / obj 5952) entries of fm_r6b_entries.txt into ../ciphertext.txt (Cipher No. 1) as E304-E306.
Per-entry note lines (plain:/variant:/merge:) are decode.py's own mechanism; the transcription lines are unchanged.
Usage: python3 fm_r5c_file.py [--dry]   Idempotent. Text = Huntington transcription; every page image-read at 2400 px (FM-R6b)."""
import re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
def d(page, ptr, row, rest): return f"Page {page} | {ptr} | mssEC 25 (obj 5952, pointer {ptr}), {rest} (FM-R6b; row {row}; image-read at 2400 px)"
def d2(page, ptr, row, rest, mark="image-read at 2400 px"): return f"Page {page} | {ptr} | mssEC 25 (obj 5952, pointer {ptr}), {rest} (FM-R6b; row {row}; {mark})"
NI = "transcription only, page image not eye-checked"
MAP = {
 "F1": ("E304", d2(118, 5662, "5662/0", "9 May 1864 Butler's Hd Qrs via Ft Monroe 10 May 3 PM, Sheldon to Maj. Eckert for Samuel Wilkeson, Tribune rooms: Swift Creek, Heckman's charge, the Brewster blown up; signed Kent, by order Butler, J. W. Shaffer (clear copy at holder pointers 4610-4611; NY Daily Tribune 11 May 1864 p.1)", "page image checked on 3 of 9 line strips at 2400 px"), ["plain: black darling apple person"]),
 "F2": ("E305", d2(196, 5740, "5740/0", "12 June 1864 Washington, T. T. Eckert to G. D. Sheldon Ft Monroe: cannot save all the wire between White House and Wilson's Point, cut it up, cable at West Point to be taken up", "page image checked on the first strip (8 lines) at 2400 px"), ["plain: wilson"]),
 "F3": ("E306", d2(200, 5744, "5744/1", "13 June 1864 Ft Monroe, Sheldon to Maj. Eckert: Butler can only protect the line from City Point to Fort Powhatan; Bickford to close out the White House line; Abercrombie wants the office kept open", "page image checked on one strip (8 lines) at 2400 px"), []),
}
blocks = {}; cur = None
for ln in (HERE/"fm_r6b_entries.txt").read_text(encoding="utf-8").splitlines():
    m = re.match(r"### (F\d+) \|", ln)
    if m: cur = m.group(1); blocks[cur] = []; continue
    if cur and ln.strip(): blocks[cur].append(ln)
p = HERE.parent/"ciphertext.txt"; txt = p.read_text(encoding="utf-8")
add = [f"### {nid} | {desc}\n" + "\n".join(blocks[k] + notes) + "\n" for k, (nid, desc, notes) in MAP.items() if f"### {nid} |" not in txt]
if not add: print("nothing to add")
elif "--dry" in sys.argv: print("would add", len(add))
else: p.write_text(txt.rstrip("\n") + "\n\n" + "\n".join(add), encoding="utf-8"); print("added", len(add))
