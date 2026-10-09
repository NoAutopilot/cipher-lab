#!/usr/bin/env python3
"""FM-R7a: file six Fort Monroe entries of fm_r7a_entries.txt into ../ciphertext.txt (Cipher No. 1) as E310-E315 and F7 into ../ciphertext-no9.txt as O9-BD.
Notes lines (plain-at / note) are decode.py's own mechanism; transcription lines unchanged. Usage: python3 fm_r7a_file.py [--dry]  Idempotent.
Every line image-read at 2400 px (FM-R7a, 9 Oct 2026)."""
import re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
def d(page, ptr, row, rest): return f"Page {page} | {ptr} | mssEC 25 (obj 5952, pointer {ptr}), {rest} (FM-R7a; row {row}; image-read at 2400 px)"
MAP = {
 "F1": ("ciphertext.txt", "E310", d(100, 5644, "5644/1", "1 May 1864 Ft Monroe, Sheldon to G. W. Baldwin, Hd Qrs Baltimore: W. W. Shore, correspondent of the World at Baltimore and from Monroe, sent away from the Department, to be arrested (sibling of pointer 5656, 5 May)"), ["plain: world", "note: FM-R7a: 'world' is plain English (pointer 5656 writes 'Corresp't of the world' plain); the key row world = Valley does not apply. season/aunt unread, U."]),
 "F2": ("ciphertext.txt", "E311", d(37, 5581, "5581/1", "9 Mar 1864 Ft Monroe, Sheldon to Maj. Eckert: our outpost near Suffolk evacuated in a hurry and retreated to Bowers Hill, Homans left his key behind"), ["note: FM-R7a: Turtle and warwicked decode as outpost and retreated; Georgia = Suffolk is M."]),
 "F3": ("ciphertext.txt", "E312", d(202, 5746, "5746/1", "13 June 1864 Washington, Eckert to Sheldon at Ft Monroe: office kept open for some days, the line cannot be taken down, hold the building party ready to go to Jamestown, work on the south side of the river"), ["note: FM-R7a: 'while horse wilby' (White House will be?) and 'waxend/windpipe' read South/River in No. 1; South side of River is M; the first clause is unread, U."]),
 "F4": ("ciphertext.txt", "E313", d(116, 5660, "5660/2", "10 May 1864 Washington, Eckert to R. O'Brien at Bermuda Landing: your ciphers come here untimed and with important words open, use arbitrary words, never leave out the time, punctuate carefully"), ["plain-at: bermuda#1", "note: FM-R7a: Bermuda Landing is the plain address line (image-read); No. 1 would give White River, wrong. penfields = Cipher fits."]),
 "F5": ("ciphertext.txt", "E314", d(122, 5666, "5666/1", "12 May 1864 Gen. Butler's Hd Qrs 11 AM, R. O'Brien to Sheldon: the operator left at the landing tore his relay to pieces, ten porous cups broken, spools burnt through, asks supplies"), ["plain-at: relay#1", "plain-at: relay#2", "plain-at: relay#3", "note: FM-R7a: relay is the telegraph relay, plain English, read in context (image-read); No. 1's key row relay = Evacuate does not apply here (it reads in E311). Maxims = Gillmore is M."]),
 "F6": ("ciphertext.txt", "E315", d(206, 5750, "5750/1", "14 June 1864 Ft Monroe, Sheldon to Maj. Eckert: S. P. Lee's telegram from flag ship Agawam, Farrar's Island, 13 June 10 PM via Ft Monroe 14th 9 PM, for Welles (printed ORN I/10, Lee to Welles)"), ["plain-at: flag#1", "plain-at: farrars#1", "note: FM-R7a: flag ship and Farrars are plain (image-read; printed as 'Flagship Agawam, Farrar's Island'); the telegram is printed in ORN I/10 word for word, so the body readings are C against that print."]),
 "F7": ("ciphertext-no9.txt", "O9-BD", d(227, 5771, "5771/1", "13 July 1864 New Castle, M. V. B. Buell to Maj. Eckert, copy to Sheldon: Ord (Baltimore) to Grant, rebel cavalry crossed the railroad to Washington between Laurel and Beltsville; read in No. 9 (No. 1 and No. 2 give nonsense); printed OR I/37 pt 2, Ord to Grant, Baltimore 13 July"), ["note: FM-R7a: No. 9. Image = Baltimore (printed dateline Baltimore); 'to Bangor Image' = to Grant, Baltimore. Printed in OR I/37 pt 2 (Ord to Grant, City Point), so the clause is C. 'to Washington' printed vs 'two pagoda'."]),
}
blocks = {}; cur = None
for ln in (HERE/"fm_r7a_entries.txt").read_text(encoding="utf-8").splitlines():
    m = re.match(r"### (F\d+) \|", ln)
    if m: cur = m.group(1); blocks[cur] = []; continue
    if cur and ln.strip(): blocks[cur].append(ln)
n = 0
for fn in ("ciphertext.txt", "ciphertext-no9.txt"):
    p = HERE.parent/fn; txt = p.read_text(encoding="utf-8")
    add = [f"### {nid} | {desc}\n" + "\n".join(blocks[k] + notes) + "\n" for k, (f, nid, desc, notes) in MAP.items() if f == fn and f"### {nid} |" not in txt]
    n += len(add)
    if add and "--dry" not in sys.argv: p.write_text(txt.rstrip("\n") + "\n\n" + "\n".join(add), encoding="utf-8")
print(("would add " if "--dry" in sys.argv else "added ") + str(n))
