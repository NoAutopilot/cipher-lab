#!/usr/bin/env python3
"""FM-R6c: file three Fort Monroe (mssEC 25 / obj 5952) entries of fm_r6c_entries.txt into ../ciphertext.txt (Cipher No. 1) as E307-E309.
Per-entry note lines (plain:/variant:/plain-at:) are decode.py's own mechanism; the transcription lines are unchanged.
Usage: python3 fm_r6c_file.py [--dry]   Idempotent. Text = Huntington transcription; every line graded here image-read at 2400 px (FM-R6c)."""
import re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
def d(page, ptr, row, rest): return f"Page {page} | {ptr} | mssEC 25 (obj 5952, pointer {ptr}), {rest} (FM-R6c; row {row}; image-read at 2400 px)"
MAP = {
 "F1": ("E307", d(233, 5777, "5777/2", "9 Aug 1864 Ft Monroe, Sheldon to Maj. Eckert, from Newbern 6 Aug: news of the Chambersburg burning, asks leave of about a week or two, Mack Gaughey to take charge (continues on pointer 5778)"), ["plain: mother hope", "note: FM-R6c: mother and hope are plain English (image-read); the tail after Webster (Jay are Gilmore) is on pointer 5778, not eye-checked, M."]),
 "F2": ("E308", d(115, 5659, "5659/0", "9 May 1864 Ft Monroe, Sheldon to Maj. Eckert, Newbern 7 May for Carlton and Porter, Daily Christian Advocate: the Albemarle fight in Albemarle Sound; clear copy at pointer 4607 (object 4849, p.166)"), ["plain-at: white#1", "plain-at: plant#1", "note: FM-R6c: clear copy at holder pointer 4607 reads Chaplain White and cotton planter (Cotton Plant); fool before zebra reads Philadelphia in the key, the clear copy has a stop there, M."]),
 "F3": ("E309", d(242, 5786, "5786/0", "4 Oct 1864 Washington 3 PM, Eckert to Sheldon for Col Webster, Chief Quartermaster Vinton, steamers wanted, signed D H Rucker; with Sheldon's reply of 5.30 PM, no spare boats but the Illinois"), ["plain-at: webster#1"]),
}
blocks = {}; cur = None
for ln in (HERE/"fm_r6c_entries.txt").read_text(encoding="utf-8").splitlines():
    m = re.match(r"### (F\d+) \|", ln)
    if m: cur = m.group(1); blocks[cur] = []; continue
    if cur and ln.strip(): blocks[cur].append(ln)
p = HERE.parent/"ciphertext.txt"; txt = p.read_text(encoding="utf-8")
add = [f"### {nid} | {desc}\n" + "\n".join(blocks[k] + notes) + "\n" for k, (nid, desc, notes) in MAP.items() if f"### {nid} |" not in txt]
if not add: print("nothing to add")
elif "--dry" in sys.argv: print("would add", len(add))
else: p.write_text(txt.rstrip("\n") + "\n\n" + "\n".join(add), encoding="utf-8"); print("added", len(add))
