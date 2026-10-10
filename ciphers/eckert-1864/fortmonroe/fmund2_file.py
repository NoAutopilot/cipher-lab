#!/usr/bin/env python3
"""FM-UND2 (10 Oct 2026, account 1, for LANE LEDGER-17): extend E622 with its head (pages 5614 l.21-5615, Cipher No. 1) and file 5658/0 telegram 2 as E624.
E622 is replaced in place (header, body, a `plain:` line, FM-UND's note kept, an FM-UND2 note added); E624 is appended. Usage: python3 fmund2_file.py [--dry]. Idempotent."""
import re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
P = HERE.parent/"ciphertext.txt"
txt = P.read_text(encoding="utf-8")
head = (HERE/"fmund2_head_lines.txt").read_text(encoding="utf-8").rstrip("\n").splitlines()
BASE = "FM-UND2 (10 Oct 2026, account 1, for LANE LEDGER-17): book No. 1 (April-May 1864 Fort Monroe rows per BOOK-FM65's date-to-book table). "
E622_HDR = ("### E622 | Page 70 | 5614 | mssEC 25 (obj 5952, pointers 5614 l.21 'Washington Apr 20 1864' to 5616/0; pages 70-72), 20 Apr 1864 4 PM Washington (the mssEC 18 cipher copy at "
 "pointer 9712 reads 'Wash Apr. 20th 4 P. M.'), Eckert (446 pd) to Sheldon at Ft Monroe, for Lieut. Col. H. Biggs, Chief Quartermaster, relaying a Meigs message: Capt. Wise has gone to New York and is to join "
 "at Monroe and help manage the fleet; General Rucker will send an officer down the Potomac to stop all vessels first despatched and ordered to assemble there and send them on to Monroe; send a vessel into the bay "
 "to stop all bound for the Potomac light and change their destination to Monroe; vessels chartered for the expedition that sailed yesterday and today already have orders for Monroe; Major Van Vliet's list not yet received; "
 "below, Captain Wise's list of 17 side-wheel boats, 11 propellers (total 2200 and 40 tons, 2800 men), 8 steam tugs and 50 canal barges (150 men each); 3 ferry boats and 3 tugs on their way from Washington; "
 "send steamers to Chesapeake City to meet and escort the tows down the Bay (FM-UND, FM-UND2; rows 5614/2, 5616/0; transcription only, page images not eye-checked)")
E622_NOTE = ("note: FM-UND2 (10 Oct 2026, account 1, for LANE LEDGER-17): the head of the telegram (5614 l.21 to the end of 5615) joined to E622 as ONE entry (same telegram: 5614 l.21 header 'Washington Apr 20 1864', no break, and "
 "the signature 446 pd Eckert closes it on 5616/0; the 'yoke meigs Bender' signature marker inside it is Meigs's own forwarded message, the decoder's tail brace starts there). Book No. 1 (decoded under No. 1; shuffled control in fmund2_head.out). "
 "Step 0 (fmund2_step0.py, information only on mssEC 25): whole telegram No. 1 (a) 0.238 (36/151) vs (b) p95 0.086, no hit (window of 2 blocks); under one meaning-shuffled No. 1 copy (seed 7) 0.224 vs 0.087, no hit. "
 "Hand corrections as `plain:` (decoder stem or key collisions on ship names and 'charters', each checked against the printed list): charters (Chart+ers read 'Knoxville'), John A. Warner ('John' = Grant), Planter, Rockland, Winona, Wyoming, and the propeller and tug names Rebecca, Barton, Wallace, Emma, Mary, Bishop (which the decoder had read as times of day, 'Adjt Genl. U.S.', 'Ram', 'Atlanta'); "
 "'Briggs' is plain (the mssEC 18 copy 9712 reads 'H Biggs'; Lieut. Col. Herman Biggs, Chief Quartermaster, Dept. of Va. and N. C., is the OR I/33 index's 'Biggs, Herman'). "
 "Print: the vessel LIST is in print, OR I/33 p.915 (running head 915 on the page before it in the cached text): Philadelphia, Pa., April 19, 1864 (received 9 p.m.), Capt. G. D. Wise, Asst. QM, to Brig. Gen. M. C. Meigs, side-wheel boats John A. Warner (600 tons, 1,200 men), Matilda (700, 1,500), George Weems (449, 800), Highland Light (291, 600), Pioneer (256, 500), Planter (400, 800), Rockland (300, 350), Keyport (350, 350), Favorite (350, 300), Tallaca (400, 600), Champion (309, 600), Kent (281, 400), Winona (600, 1,000), Wyoming (400, 500), Portsmouth (400, 500), Jefferson (400, 500), Kingston (400, 500); propellers Rebecca Barton, Mayflower, a sea steamer, Leader, Wallace, Cahill, New York, Brayerly, Mayflower, Beverly, Emma; steam-tugs Hutchins, Delaney, Palmer, Tempest, Ajax, Mary Freeman, Vatterlin, Bishop; 50 canal barges, average capacity 150 men. "
 "The decode agrees with the printed list on every vessel name and on every tonnage and men figure but one (cipher 'pioneer [306] tons', print 256 tons: a numeral read to settle on the image, M), and the cipher's propeller total '2200 and 40 tons, 2800 men' equals the printed propellers' sum (2,240 tons, 2,800 men). "
 "What is NOT located in print: the relay itself (Eckert's head: Rucker, Biggs, Van Vliet, the order to stop vessels in the Potomac, 'send steamers to Chesapeake City ... down the Bay'): 16 letters-only phrases over the 211 cached volumes (fmund2_printcheck.out) hit nothing for the head; be-api whole-collection 7 queries 0 hits (fmund2_beapi.out); OR I/33 pp.914-916 around the list read: Wise's closing sentences ('Should judge I had comfortable transportation for 20,000 men ...') are printed and are not in this cipher, which has instead the totals and the Chesapeake City order. "
 "Holder (CISOSEARCHALL, all pointers, 4 fresh queries, control 9678 hit; fmund2_hdl.out): the head's words hit only 5614 and 5615 (this ledger) and 9712 (the mssEC 18 CIPHER copy, Page 46, read by dmGetItemInfo: cipher, 'no 6. F. M Geo D. Sheldon Washn Wash Apr. 20th 4 P. M.'); no clear copy. "
 "Shuffled-key control (fmund2_head.out, seeds 1, 2, 3, 7): the head's clause does not survive any shuffled copy: 'Potomac' becomes Rhode Island / Pieces / Connecticut / Washington, 'Monroe' becomes Help / Ohio / Alexandria / Newbern, 'Captain' becomes Effective / City Point / Tullahoma, 'Colonel' becomes Maj Gen Joseph Hooker / Favorable / Norfolk / Cleveland; the plain words (Rucker, Van Vliets, wise, chartered) and the numerals stay. "
 "Grades by hand: the decoder's H are key rows (Potomac, Monroe, Colonel, Quartermaster, Captain, General, Major, Expedition, New York, Baltimore, Philadelphia, Washington, Ferry, Men, numerals); M: 'Briggs' (plain), 'pioneer [306]'; a sentence not read: 'Julia ... vinton unity' (the greeting words before 'for Lieut'). Also in mssEC 18 (pointers 9712-9713) a second cipher copy of the whole telegram: a duplicate diff for a verifier, not done here.")
T2_HDR = ("### E624 | Page 114 | 5658 | mssEC 25 (obj 5952, pointer 5658), 9 May 1864 3.30 AM Jamestown, R. O'Brien to Maj. Eckert (second telegram of row 5658/0; the first, Eckert to Butler, 8 May 1864, is in print in Butler Corr. IV and is not filed): "
 "I left General Butler's headquarters 5 miles from Bermuda Landing, all quiet and ready to move in the morning; [cavalry expedition crossing] at Harrison's Landing to join us; I will start tomorrow; all working fine; will endeavor to keep you posted "
 "(FM-UND2; row 5658/0 telegram 2; thin, about 40 words, 6 key-row tokens; transcription only, page image not eye-checked)")
T2_NOTE = ("note: FM-UND2 (10 Oct 2026, account 1, for LANE LEDGER-17): book No. 1 (O'Brien to Eckert, 9 May 1864 per BOOK-FM65; fmund.out gives No. 1 H 43 for the row against No. 2 H 34 and No. 9 H 17, the whole row). Thin: 6 H tokens (Knox = Butler, person = 5, "
 "pacific = Cavalry, roman = Expedition, pluming = crossing) in about 40 words; the rest is plain English. 'Bermuda' is set `plain` by hand: the key row Bermuda = White River (p.10 l.16) would read 'five miles from White River landing', "
 "while E164 (10 May 1864) has O'Brien dating a telegram from 'Bermuda Landing' as plain place text, so 'Bermuda landing' is the place and the key row is a collision (M). 'wests' stays unread. "
 "Step 0 (fmund2_step0.py, information only on mssEC 25): No. 1 (a) 0.737 (28/38) vs (b) p95 0.289, HIT; under one meaning-shuffled No. 1 copy (seed 7) 0.683 vs 0.268, HIT: a tie, so a non-test. "
 "Shuffled-key control (fmund2_t2.out, seeds 1, 2, 3, 7): all four copies keep the plain frame and the numeral 5 and replace the key-dependent words (Butler -> Parole / Louisa C.H. / Arms / Maj Gen Geo. H. Thomas; Cavalry -> Beaufort / T. J. Wood / New Hampshire / Lebanon; Expedition -> Danger / Battle Creek / North / Position), so the key-dependent part of the clause does not survive; the plain 'all quiet and ready to move in the morning' does. "
 "Holder: 2 CISOSEARCHALL queries by FM-UND (fmund_hdl.out: 'Harrisons landing Jamestown Bermuda landing Eckert' and 'Ingalls reserves programme apprise condition gratifying'; none run again here: the telegram's own words are too plain to be rare) hit only 5658 and 9734 (mssEC 18 cipher copy); no clear copy. Print (fmund2_printcheck.out, 211 cached volumes, letters-only): 'miles from Bermuda landing', 'all quiet and ready to move in the morning', 'crossing at Harrison's landing to join us', 'I left General Butler's headquarters', 'I will start tomorrow all working fine': none; the generic 'will endeavor to keep you posted' and 'all working fine' hit unrelated volumes (ids warofrebellion013402rootrich, 013404rootrich, 411unit, 413unit, 482unit) and are not this message. be-api whole-collection (fmund2_beapi.out): 3 queries (2 whole-collection, 1 Grant Papers 10) 0 hits. "
 "Not searched: OR I/36 pt 2 by date (9 May) was covered by the cache grep only, Butler Corr. IV pages for 9 May by the cache grep only; the press of the day not searched.")

blocks = re.split(r"(?m)^(?=### )", txt)
done = False; out = []
for b in blocks:
    if b.startswith("### E622 |") and "FM-UND2" not in b:
        old = b.rstrip("\n").splitlines()
        oldnote = [l for l in old if l.startswith("note: FM-UND ")]
        body = ["Washington Apr 20 1864"] + head
        body.insert(1, "")  # placeholder removed below
        body = ["Washington Apr 20 1864"] + head[:1] + ["plain: charters John warner Planter Rockland Winona Wyoming Briggs Rebecca Barton Wallace Emma Mary Bishop"] + head[1:]
        b = "\n".join([E622_HDR] + body + oldnote + [E622_NOTE]) + "\n\n"
        done = True
    out.append(b)
txt2 = "".join(out)
if "### E624 |" not in txt2:
    seg = (HERE/"fmund2_entries.txt").read_text(encoding="utf-8").split("### T2")[1].splitlines()[1:]
    t2 = [l for l in seg if l.strip()]
    body = [t2[0], "plain: Bermuda"] + t2[1:] if False else [t2[0]] + t2[1:] + ["plain: Bermuda"]
    txt2 = txt2.rstrip("\n") + "\n\n" + "\n".join([T2_HDR] + body + [T2_NOTE]) + "\n"
if "--dry" in sys.argv: print(txt2[-6000:])
elif txt2 != txt: P.write_text(txt2, encoding="utf-8")
