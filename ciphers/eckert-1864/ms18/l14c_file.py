#!/usr/bin/env python3
"""L14-C: file three held mssEC 18 rows under the LEDGER-14 ruling (step-0 hit is a non-test; file unless holder clear copy / in print / plain / no clause):
9897/1 -> E620 and 9862/0 -> E621 (Cipher No. 1, ../ciphertext.txt, bodies from ms18_r11_entries.txt X6/X7); 9850/2 -> N2-SA (Cipher No. 2, ../ciphertext-no2.txt, body from n2r6_entries.txt Z6).
Not filed (in print): 9869/4 9764/1 9885/3 9688/0 9848/0 9811/0. Usage: l14c_file.py [--dry]  Idempotent. Leaves not eye-checked (holder transcription only)."""
import re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
def block(fn, key):
    src = (HERE/fn).read_text(encoding="utf-8")
    m = re.search(rf"### {key} \|[^\n]*\n(.*?)(?=\n### |\Z)", src, re.S)
    return [l for l in m.group(1).splitlines() if l.strip()]
S0 = "Step 0 (ms18 step0_ordered functions, as recorded by the earlier reader; information only under the LEDGER-14 ruling, a non-test: STEP0-KEYCTL): "
HOLD = "Holder clear copy: one CISOSEARCHALL query on the row's plain words (all pointers, control 9678 returned 9678) returned only the row's own pointer. "
E = {
 "E620": ("ciphertext.txt", "X6", "Page 237 | 9897 | mssEC 18 (obj 10074, pointer 9897; printed page 231), 15 Nov 1864 Washington 10 PM ('John Horner, New York, Washn Nov 15th 1864'), signed [C. A. Dana] by the key (M), to [Maj. Gen. Dix] (M): "
  "I am confidentially informed that Beverly Tucker will cross at [Niagara] Falls on Thursday morning; I am also informed that John Odell may be relied upon to arrest him, but I do not know Odell; have you any officer of sufficient discretion who can at once be dispatched to the falls for the purpose? (L14-C; row 9897/1; holder transcription, leaf not eye-checked)",
  "note: L14-C: No. 1 by sense (whole-entry vocabulary share No.1 / No.2 / No.9 = .32/.29/.16, not discriminating; the meaning-shuffled copy of No. 1 reads H10 vs H11, so the count control cannot fail and licenses nothing; No. 2 gives 'Wheeler 1000', 'Imboden'; No. 9 gives 'Niagara Falls' and 'John Odell' in the plain-word positions but its time word 7.30 PM and 'Kasson'/'Movement' groups are nonsense). "
  + S0 + "(a) 0.765 (26/34), (b) p95 0.353, hit; (c) 8: dix, general, grant, jno, major, porter, ... (the No. 1 decode's 'D. D. Porter Falls' for the place is wrong and is read M as 'Niagara'). " + HOLD
  + "Print: not located (cached 177 volumes, letters-only phrase grep on 'Beverly Tucker will cross', 'officer of sufficient discretion', 'dispatched to the falls' and a 14-16 Nov 1864 date-window with Tucker/Niagara/Dix: OR I/43 pt 2 (warofrebellion432unit), Butler Corr. V, 0 phrase hits; be-api whole-collection phrase queries, 0 hits; the be-api control was missing in whole-collection mode, so a miss there is weak). Grades: see decode.py output; names Dix, Dana, Niagara M."),
 "E621": ("ciphertext.txt", "X7", "Page 202 | 9862 | mssEC 18 (obj 10074, pointer 9862; printed page 196), 7 Oct 1864 Washington 4 PM ('J W Sampson, Washn Oct 7th 1864'), signed [General-in-Chief] (Halleck, M), for J. W. Garrett (B&O Railroad): "
  "arms were sent from here to Harper's Ferry on the afternoon of the 5th inst.; it is reported that they have not arrived there; please see if they have been delayed on the Rail Road; it is important that there should be no delay (L14-C; row 9862/0; holder transcription, leaf not eye-checked)",
  "note: L14-C: No. 1 by sense (share .36/.36/.14: a tie of No. 1 and No. 2, not discriminating; No. 1 H10 vs No. 2 H8 vs No. 9 H4; the shuffled-copy H count ties No. 1, so the count control cannot fail and licenses nothing; No. 1 gives the whole clause, No. 2 'Florence', 'Thomas Geo H', nonsense). "
  + S0 + "(a) 0.579 (11/19), (b) p95 0.316, hit; (c) 8: arms, ferry, five, harpers, rail, report, road, ... " + HOLD
  + "Print: not located (cached 177 volumes: letters-only phrase grep on 'arms were sent from here to Harpers Ferry', 'delayed on the Rail Road' and a 6-8 Oct 1864 date-window with Garrett/Harper/arms, 0 hits; OR I/39 pt 3 (Oct 1864) is NOT among the cached volumes; be-api whole-collection and inside warofrebellion393unit 0 hits). The ledger's tail 'she went on to tell (Cal) 6 P. m' is a service note, not message text. Names M."),
 "N2-SA": ("ciphertext-no2.txt", "Z6", "Page 190 | 9850 | mssEC 18 (obj 10074, pointer 9850; printed page 184), 26 Sept 1864 Washington 12.30 PM ('Kimber N.O., Washn Sept 26th 1864'; entry 2 of the leaf; 'No 1 9 AM' is a service note), to Maj. Gen. E. R. S. Canby, signed H. W. Halleck (tail group 'welch Lamb', M): "
  "an officer of rank and experience should be sent by you to investigate alleged frauds and inefficiencies in Arkansas and especially at Fort Smith and the Indian Territory; Grant has given [Smith] full discretion to act with his command as he may deem best against Kirby Smith, Price and company (L14-C; row 9850/2; holder transcription, leaf not eye-checked)",
  "note: L14-C: No. 2 (N2R-6's shares .36/.44/.11; 200-seed day test in n2r6_coherence.out: decoded day 26 = header day; the 'No. 1 reads Prentiss/Hartsuff' no-clause finding of N2R-4 for the neighbouring entry of the same pointer applies the same way). "
  + S0 + "(a) 0.500 (18/36), (b) p95 0.250, hit at the 0.5 line; (c) 14: arkansas, canby, command, fort, grant, kirby, price, hundred, ... ('Fort [100]' is Fort Smith, M; 'Smith' after 'has given' is the commander the key leaves open, M). " + HOLD
  + "Print: not located (cached 177 volumes, letters-only grep on 'alleged frauds and inefficiencies', 'especially at Fort Smith and the Indian Territory', 'full discretion to act' and a 25-27 Sept 1864 window with Canby/Fort Smith/fraud: 0 hits; OR I/41 pt 3 (Sept 1864, Canby) is NOT among the cached volumes; be-api whole-collection 0 hits, inside warofrebellion413unit 0 hits (that identifier is a guess for I/41 pt 3, M)). Names M."),
}
for nid, (fn, key, desc, note) in E.items():
    p = HERE.parent/fn; txt = p.read_text(encoding="utf-8")
    if f"### {nid} |" in txt or "--dry" in sys.argv: print("skip/dry", nid); continue
    body = block("ms18_r11_entries.txt" if key.startswith("X") else "n2r6_entries.txt", key)
    p.write_text(txt.rstrip("\n") + f"\n\n### {nid} | {desc}\n" + "\n".join(body + [note]) + "\n", encoding="utf-8"); print("added", nid)
