#!/usr/bin/env python3
"""FM-R5c: file ten Fort Monroe (mssEC 25 / obj 5952) entries of fm_r5c_entries.txt into ../ciphertext.txt (Cipher No. 1) as E290-E299.
Per-entry note lines (plain:/variant:/merge:) are decode.py's own mechanism; the transcription lines are unchanged.
Usage: python3 fm_r5c_file.py [--dry]   Idempotent. Text = Huntington transcription; every page image-read at 2400 px (FM-R5c)."""
import re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
def d(page, ptr, row, rest): return f"Page {page} | {ptr} | mssEC 25 (obj 5952, pointer {ptr}), {rest} (FM-R5c; row {row}; image-read at 2400 px)"
def d2(page, ptr, row, rest, mark="image-read at 2400 px"): return f"Page {page} | {ptr} | mssEC 25 (obj 5952, pointer {ptr}), {rest} (FM-R5c; row {row}; {mark})"
NI = "transcription only, page image not eye-checked"
MAP = {
 "F1": ("E290", d2(207, 5751, "5751/2", "15 June 1864 Washington, T. T. Eckert to G. D. Sheldon Ft Monroe, for Lt Col Biggs: vessels to Fort Powhatan for ferrying troops and trains (signed Meigs in print)"), ["variant: whiskey=Whistle:M"]),
 "F2": ("E291", d2(178, 5722, "5722/0", "31 May 1864 Washington, T. T. Eckert to G. D. Sheldon Ft Monroe: tell Bickford not to build farther than White House; a card cipher for the wire"), ["plain: pembroke"]),
 "F3": ("E292", d2(239, 5783, "5783/1", "16 Sept 1864 Harpers Ferry, G. J. Lawrence for Lt Col Morgan: raid on the cattle herd near Coggins Point, from Lt Col Wilson, signed Sheldon", NI), []),
 "F4": ("E293", d2(278, 5822, "5822/0", "8 Dec 1864 Ft Monroe, G. D. Sheldon: Colonel Webster, the Rice Dupont and Sedgwick, signed S. H. Beckwith", NI), []),
 "F5": ("E294", d2(72, 5616, "5616/1", "20 Apr 1864 Ft Monroe, Sheldon to Maj. Eckert for Gen. Rucker, from Biggs: no steamers to send to sea", NI), []),
 "F6": ("E295", d2(80, 5624, "5624/0", "22 Apr 1864 Ft Monroe, Sheldon to Maj. Eckert for the Quartermaster General: assistant quartermasters wanted, signed Butler", NI), []),
 "F7": ("E296", d2(283, 5827, "5827/2", "11 Dec 1864 Ft Monroe, S. H. Beckwith City Point to Sheldon for Grant: Shepley's scout toward Hicksford and cavalry to South Quay (continues on pointer 5828)"), ["plain-at: black#2"]),
 "F8": ("E297", d2(88, 5632, "5632/0", "24 Apr 1864 Ft Monroe, Sheldon to Maj. Eckert for C. A. Dana: the blockade runner Diamond about to be sold in New York, signed W. F. Smith", NI), []),
 "F9": ("E298", d2(250, 5794, "5794/1", "16 Oct 1864 Washington, Maj. Eckert for the President, from the Secretary of War: Logan for Hooker's command, Hooker to Missouri", NI), []),
 "F10": ("E299", d2(65, 5609, "5609/1", "18 Apr 1864 Ft Monroe, Sheldon to Maj. Eckert for the Secretary of War: J. H. Maddox seized with tobacco, signed Butler", NI), []),
}
blocks = {}; cur = None
for ln in (HERE/"fm_r5c_entries.txt").read_text(encoding="utf-8").splitlines():
    m = re.match(r"### (F\d+) \|", ln)
    if m: cur = m.group(1); blocks[cur] = []; continue
    if cur and ln.strip(): blocks[cur].append(ln)
p = HERE.parent/"ciphertext.txt"; txt = p.read_text(encoding="utf-8")
add = [f"### {nid} | {desc}\n" + "\n".join(blocks[k] + notes) + "\n" for k, (nid, desc, notes) in MAP.items() if f"### {nid} |" not in txt]
if not add: print("nothing to add")
elif "--dry" in sys.argv: print("would add", len(add))
else: p.write_text(txt.rstrip("\n") + "\n\n" + "\n".join(add), encoding="utf-8"); print("added", len(add))
