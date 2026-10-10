#!/usr/bin/env python3
"""FIX-FM24 (10 Oct 2026, account 1, for LANE LEDGER-12): carry s.5 of AUDIT (FV-MS18r) and AUDIT (FV-MS18s) into ../ciphertext.txt
(header text and per-entry note/gloss lines read by decode.py; the manuscript lines are never edited). E420's body was re-filed separately from
ms18_r10_entries.txt X7 (ms18_r10_file.py read ms18_r8_entries.txt by mistake, so E388's 4 Apr 1864 text had been filed under E420).
Usage: fix_fm24.py [--dry]  Idempotent."""
import sys
from pathlib import Path
P = Path(__file__).resolve().parent.parent / "ciphertext.txt"
HDR = {
 "E402": [("for [Maj. Gen. David Hunter, M] or [the code word 'Wesley', unread]", "for [Maj. Gen. David Hunter] or [Maj. Gen. H. G. Wright] ('Wesley', C by print)"),
          ("for [Hunter's, the decoder reads Ord's, M] head quarters", "for [Gen. Hunter's] head quarters ('Mackerals', C by print; the leaf reads 'Mackerel', M)"),
          ("transportation for [5] from", "transportation for five from"),
          ("; not located in print (MS18-R9;", "; printed, Simon, ed., The Papers of Ulysses S. Grant vol. 11, editorial note (IA be-api; lending-only item, page not read), text C (FV-MS18r) (MS18-R9;")],
 "E403": [("for [Brig. Gen.] Stevenson [M]:", "for [Brig. Gen.] Stevenson (name plain on the leaf):")],
 "E404": [("the two regiments from the Northwest are en route;", "the two regiments from the Northwest are en route, but as they had a long march before reaching railroad or steam-boat transportation, we may not hear of them for some days;"),
          ("signed [Halleck] General in Chief:", "signed [Halleck] (ledger General in Chief; print Major-General and Chief of Staff):"),
          ("printed OR I/41 pt 4 p.389 (MS18-R9;", "printed OR I/41 pt 4 p.389 (page image, FV-MS18r) (MS18-R9;")],
 "E420": [("(before the head of Boreman's letter, p.291 or 292)", "p.291 (page image, FV-MS18r; before Boreman's letter); 'why so slow' not in the print")],
 "E430": [("(IA privateofficialc04butl, pp.161-162 by OCR)", "(IA privateofficialc04butl, p.161, page image: both parts as received by Butler, the Grant message headed 'Message from Sparta, two [2] a.m., Ford, May 4th For Maj. Gen. Halleck', then Halleck's 3 p.m. cipher)"),
          ("(Germanna Ford 4 May 1864, rec'd 1.50 p.m.; page not read)", "p.1 (page image; Germanna Ford 4 May 1864, rec'd 1.50 p.m.)"),
          ("printed OR I/36 pt 2 p.391 by OCR running heads", "printed OR I/36 pt 2 p.391 (page image; Washington 4 May 1864, 2 p.m.)")],
}
ADD = {
 "E402": ["gloss: wesley=Maj._Gen._H._G._Wright:C <insertion>mackerals</insertion>=Gen._Hunter's:C meridens=struck_word,_not_read:M",
          "note: FIX-FM24 (10 Oct 2026; AUDIT FV-MS18r s.5 item 1): N1 D1; printed in Simon, Papers of U. S. Grant vol. 11, editorial note (Comstock to Hunter or Wright near Monocacy; page not read, lending-only). Wesley = Wright, Mackerals = Hunter's (C by print; was Right / Ord's); [5] = five (C). The inserted word reads 'Mackerel' on the leaf (M)."],
 "E403": ["note: FIX-FM24 (10 Oct 2026; AUDIT FV-MS18r s.5 item 2): N3 D1, not located in print. 'Steven son' is plain on the leaf (rank by key). Context, not print of this telegram: Stephen Maxon is named in the New York soldier-vote forgery testimony (press 2 Nov 1864; Benton, Voting in the Field). Next: OR ser. II vol. 7 / ser. III vol. 4 by page and the Ferry-Donohue commission record, ~$0.4."],
 "E404": ["note: FIX-FM24 (10 Oct 2026; AUDIT FV-MS18r s.5 item 3): N1 D1; OR I/41 pt 4 p.389 on the page image. The header now carries the long-march clause (on the leaf and in the reading); print signature 'Major-General and Chief of Staff' against the ledger 'General in Chief'."],
 "E420": ["plain: hoped",
          "note: FIX-FM24 (10 Oct 2026; AUDIT FV-MS18r s.5 item 4 and FV-MS18s s.5 item 4): N1 D1; OR I/37 pt 2 p.291 on the page image. Body re-filed from ms18_r10_entries.txt X7: ms18_r10_file.py had read ms18_r8_entries.txt, so E388's 4 Apr 1864 Grant-to-Sherman text stood under this header until 10 Oct 2026 ~09:1x UTC; the script is corrected. 'why so slow' is not in the print (operator's remark or null)."],
 "E430": ["gloss: judah's=Maj_Genl_U.S._Grant's:H inland=Halleck:C know=Maj_Gen_B._F._Butler:C chinamen=null_or_check_word:M",
          "note: FIX-FM24 (10 Oct 2026; AUDIT FV-MS18s s.5): N1 D1; OR I/36 pt 1 p.1 (Grant's message), OR I/36 pt 2 p.391 (Halleck's cover, 2 p.m.) and Butler Corr. IV p.161 (both parts as received, 3 p.m.), all on page images. Judah's = Grant's (H, key row; possessive), Inland = Halleck (C by Butler IV 'For Maj. Gen. Halleck'), Know = Butler (a slip for key.md Knox, C by print), Chinamen M. The printed heading 'Message from Sparta, two [2] a.m., Ford' may garble the ledger's 'Germ ana [Ford] May [4]' (M, remark)."],
}
lines = P.read_text(encoding="utf-8").split("\n"); n = 0
for e in HDR:
    i = next(k for k, l in enumerate(lines) if l.startswith(f"### {e} |"))
    for a, b in HDR[e]:
        if a in lines[i]: lines[i] = lines[i].replace(a, b); n += 1
        elif b not in lines[i]: sys.exit(f"{e}: header text not found: {a[:60]}")
    j = i + 1
    while j < len(lines) and not lines[j].startswith("### ") and lines[j].strip(): j += 1
    block = lines[i:j]
    new = [x for x in ADD[e] if x not in block]
    lines[j:j] = new; n += len(new)
if "--dry" not in sys.argv: P.write_text("\n".join(lines), encoding="utf-8")
print(("would change " if "--dry" in sys.argv else "changed ") + str(n))
