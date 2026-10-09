#!/usr/bin/env python3
"""FM-R7b: file three Fort Monroe (mssEC 25 / obj 5952) entries of fm_r7b_entries.txt into ../ciphertext.txt (Cipher No. 1) as E307-E309.
Per-entry note lines (plain:/variant:/plain-at:) are decode.py's own mechanism; the transcription lines are unchanged.
Usage: python3 fm_r7b_file.py [--dry]   Idempotent. Text = Huntington transcription; every line graded here image-read at 2400 px (FM-R7b)."""
import re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
def d(page, ptr, row, rest): return f"Page {page} | {ptr} | mssEC 25 (obj 5952, pointer {ptr}), {rest} (FM-R7b; row {row}; image-read at 2400 px)"
MAP = {
 "F2": ("E318", d(165, 5709, "5709/1", "28 May 1864 Washington, Eckert to Sheldon: the Gloucester route is best, 100 men can guard that line, Mackintosh's building party, Bickford's operators"), ["plain-at: white#1", "note: FM-R7b: Ivory (read General-in-Chief by the key) is probably 'my'; M. Image-read only down to 'Cowans'; the last lines are transcription only."]),
 "F4": ("E319", d(151, 5695, "5695/2", "27 May 1864 Ft Monroe, Sheldon to Eckert: distances across York River at Yorktown and Mattapony at West Point, cannot string wire, navigation must remain open, country as favourable as the route up the peninsula"), ["note: FM-R7b: pony after Mattie reads [9] in the key, plainly 'River' (Mattapony); M. Transcription only, not eye-checked."]),
 "F5": ("E320", d(158, 5702, "5702/0", "27 May 1864 Washington, Eckert to Sheldon: O'Brien to stay at Bermuda Hundred in charge of cipher work, Caldwell to take it when the White House line is done, Mackintosh to bring builders"), ["plain: bermuda", "plain-at: white#1", "note: FM-R7b: Bermuda and white (White House) are plain English where the key gives White River and Report; first lines image-read, the rest transcription only."]),
 "F6": ("E321", d(238, 5782, "5782/0", "1 Sept 1864 Head Qrs A. P., Caldwell to Eckert: cable to be laid on the north side of the river, less danger from anchors, channel nearest the south shore"), ["plain: anchors", "note: FM-R7b: anchors is plain English where the key gives Donelson; signature Caldwell plain; first 7 lines image-read."]),
}
blocks = {}; cur = None
for ln in (HERE/"fm_r7b_entries.txt").read_text(encoding="utf-8").splitlines():
    m = re.match(r"### (F\d+) \|", ln)
    if m: cur = m.group(1); blocks[cur] = []; continue
    if cur and ln.strip(): blocks[cur].append(ln)
p = HERE.parent/"ciphertext.txt"; txt = p.read_text(encoding="utf-8")
add = [f"### {nid} | {desc}\n" + "\n".join(blocks[k] + notes) + "\n" for k, (nid, desc, notes) in MAP.items() if f"### {nid} |" not in txt]
if not add: print("nothing to add")
elif "--dry" in sys.argv: print("would add", len(add))
else: p.write_text(txt.rstrip("\n") + "\n\n" + "\n".join(add), encoding="utf-8"); print("added", len(add))
