#!/usr/bin/env python3
"""FIX-L17a (10 Oct 2026, account 1, for LANE LEDGER-17): apply s.5 of AUDIT (FV-L16b) for E518 E527 E526 E546 E553 E554, AUDIT (FV-L16c) for E564 E574
E558 E569, AUDIT (FV-L16d) for E441 E472 E442 E473 E469 E466, as amended by AUDIT 2 (AUD2-LEDGER16-2, -3, -4), to ciphertext.txt as header edits, decoder
directive lines and one 'note: FIX-L17a' line per entry. Same method as fixl16b_apply.py / fixl15_apply.py (reused run()); reading.md only by decode.py
--write. Idempotent: skips a block that already has a 'FIX-L17a' note. Not touched: FV-L16a's six, E447 E471 E474 (second audits live; FIX-L17b).
Held, not applied: the AUD2-LEDGER16-2 key.md proposal (Topsy -> 12 midnight, Francis -> 12 noon) would re-render every Topsy/Francis entry in the ledger;
E554 takes it as an entry-level gloss instead."""
import fixl15_apply as base
base.MARK = 'FIX-L17a (10 Oct 2026'
base.E.clear(); base.LF.clear()
E = base.E; LF = base.LF
def S(e, h=(), d=(), n=''): E[e] = dict(h=list(h), d=list(d), n=n)
def N(src, body): return "FIX-L17a (10 Oct 2026, account 1, for LANE LEDGER-17; %s): %s" % (src, body)

# ---- FV-L16b (+ AUD2-LEDGER16-2) ----
S('E518', h=[("Sheldon to S. H. Beckwith at City Point, for Brig. Gen. Ingalls, chief QM:", "Col. R. C. Webster, Chief Quartermaster at Fort Monroe, to Brig. Gen. Ingalls, chief QM, at City Point, via S. H. Beckwith (operator Geo. D. Sheldon; cf. holder 8510 p.32, Smith to Dana, 9.20 AM 7 Jan, cipher copy 5864/0; O'Brien, Telegraphing in Battle pp.179-180, Webster in cipher for Terry's expedition 4 Jan):"),
             ("(FM65-B; row 5864/1; text only)", "(FM65-B; row 5864/1; image-read by FV-L16b, matches the transcription except 'Geo.' for 'Gen')")],
  d=['plain-at: webster#1', 'gloss: sheaf=Chief:I'],
  n=N('AUDIT FV-L16b s.5, AUD2-LEDGER16-2 s.5', "'Webster' is the plain name Col. R. C. Webster, Chief Quartermaster at Fort Monroe, not a second [signed] (key row Signature misfires); 'sheaf' = Chief (I). The operator signature 'Gen D. Sheldon' in the transcription is a slip for 'Geo. D. Sheldon' (image 5864); the old reading is kept here. Header direction: from Webster at Fort Monroe for Ingalls at City Point, via Beckwith."))
LF['E518'] = ("Gen D. Sheldon", "Geo. D. Sheldon")
S('E526', h=[("by direction of the Quartermaster, signed William L. James, Captain and A.Q.M. (M for the signature)", "by direction of the Chief Quartermaster ('Sheaf Vincent', I), signed William L. James, Captain and A.Q.M. ('William' plain, Capt. William L. James; Grant Papers vol. 14, holder 7734 p.76)"),
             ("(FM65-C; row 5867/2; short, 34 tokens)", "(FM65-C; row 5867/2; short, 34 tokens; image-read by FV-L16b, matches the transcription)")],
  d=['plain-at: william#1', 'gloss: sheaf=Chief:I'],
  n=N('AUDIT FV-L16b s.5, AUD2-LEDGER16-2 s.5', "'William' is plain (Capt. William L. James, A.Q.M.), not the key row [100]; 'Sheaf Vincent' = Chief Quartermaster (sheaf = Chief, I). The signature is no longer M. Context: Capt. William L. James at Fort Monroe, Grant Papers vol. 14, holder 7734 p.76."))
S('E527', h=[("(FM65-C; row 5869/1)", "(FM65-C; row 5869/1; image-read by FV-L16b, matches the transcription; context OR I/46 pt 2 p.60, GO No. 1 of 7 Jan 1865)")],
  d=['plain-at: negro#1', 'plain-at: white#1'],
  n=N('AUDIT FV-L16b s.5', "'Negro' in 'Supt. Negro affairs' is plain (key row Artillery misfires); 'White' in 'Frank J White' is plain, Lt. Col. Frank J. White at Eastville (key row Report misfires). Both read plain, so the decode is H 10 of 10 code words. Header context OR I/46 pt 2 p.60 (GO No. 1, 7 Jan 1865)."))
S('E546', h=[("for Senator L. F. S. Faster (as transcribed), Willards Hotel, Washington:", "for Senator L. S. Foster (as 'L. F. S. Faster'), Willards Hotel, Washington:"),
             ("My executive officer Lieut. Commander Parker", "My executive officer Lieut. Commander James Parker"),
             ("signed Joseph Land Man (as transcribed)", "signed Joseph Lanman (as 'Land Man'), Commodore, U.S.S. Minnesota; context ORN I/11 p.725"),
             ("(FM65-D; row 5890/2; 36 tokens)", "(FM65-D; row 5890/2; 36 tokens; image-read by FV-L16b, matches the transcription)")],
  d=['plain-at: hotel#1', 'plain-at: washington#1'],
  n=N('AUDIT FV-L16b s.5', "'Hotel' in 'Willards Hotel' is plain (key row Longstreet misfires); the header word 'Washington' in 'Maj. Eckert , Washington' is plain (lesson 8, key row Volunteer misfires; FIX-L16 left E546 to this audit). Names: Senator L. S. Foster ('Faster'), Commodore Joseph Lanman of the U.S.S. Minnesota ('Land Man'), Lieut. Commander James Parker. Header context ORN I/11 p.725."))
S('E553', h=[("J. H. Emerick, Hdqrs Army of the James, for [Maj. Gen. Ord]:", "Brig. Gen. George H. Gordon at Fort Monroe to Maj. Gen. Ord at Hdqrs Army of the James, via J. H. Emerick (operator):"),
             ("(FM65-E; row 5902/1)", "(FM65-E; row 5902/1; image-read by FV-L16b, matches the transcription; context OR I/46 pt 2 pp.348, 504, Gordon, War Diary (1882) p.378, Butler Corr. V p.545, Shepley notified the morning of 8 Feb)")],
  n=N('AUDIT FV-L16b s.5, AUD2-LEDGER16-2 s.5', "no decoder change. Header direction only: Gordon at Fort Monroe to Ord at Hd Qrs Army of the James, via Emerick; context OR I/46 pt 2 pp.348, 504, Gordon p.378 (summarised, not printed), Butler Corr. V p.545."))
S('E554', h=[("8 Feb 1865 [12 noon or 12.30 PM] Ft Monroe, Geo. D. Sheldon, for [Brig. Gen.] Gordon:", "8 Feb 1865 [12 midnight] Hdqrs Army of the James (Ord, operator J. H. Emerick) to Brig. Gen. Gordon, via Sheldon at Fort Monroe:"),
             ("(FM65-E; row 5902/2)", "(FM65-E; row 5902/2; image-read by FV-L16b, matches the transcription; context OR I/46 pt 2 pp.348, 504, Gordon, War Diary (1882) p.378, Butler Corr. V p.545)")],
  d=['gloss: topsy=12_midnight:H', 'gloss: v=Vogdes:I', 'graded: obtain:M'],
  n=N('AUDIT FV-L16b s.5, AUD2-LEDGER16-2 s.5', "time 'Topsy' = 12 midnight (the key's TIME page reads '12 (midnight)', H; midnight 8-9 Feb is coherent), replacing '12 noon or 12.30 PM'; applied as an entry-level gloss, not as a key.md edit (the proposed key.md rows Topsy -> '12 midnight' and Francis -> '12 noon' would re-render every Topsy and Francis entry in the ledger; held for a job that regenerates them). 'obtain' x2 are unread (M). 'V' = Vogdes (I). Header direction: from Hd Qrs Army of the James (Ord, operator Emerick) to Gordon via Sheldon at Fort Monroe."))
# ---- FV-L16c (+ AUD2-LEDGER16-3) ----
S('E564', h=[("signed Captain James;", "signed Captain [William L.] James, A.Q.M.;"),
             ("(FM65-E; row 5918/1)", "(FM65-E; row 5918/1; image-read by FV-L16c, matches the transcription; context OR I/46 pt 2 p.908, two other James-to-Bradley telegrams of 9 Mar)")],
  d=['plain-at: pilots#1', 'plain-at: pilots#2'],
  n=N('AUDIT FV-L16c s.5, AUD2-LEDGER16-3 s.5', "'Pilots' and 'pilots' are plain words (key row Pilot = Capture misfires twice); 'James' is plain (Capt. William L. James). Header context OR I/46 pt 2 p.908 (James to Bradley, 9 Mar)."))
S('E574', h=[("'[Secretary of War] [left] here 1 P.M. for [City Point];", "'The Secretary of War (Stanton) left here 1 P.M. for City Point by the River Queen;"),
             ("Name of boat is [River Queen]'", "Name of boat is River Queen'"),
             ("(FM65-F; row 5931/0;", "(FM65-F; row 5931/0; image-read by FV-L16c; context OR I/46 pt 3 p.28; the visit: Grant Papers vol. 14, note to Grant to Stanton 14 Mar and Grant to Ord 15 Mar;")],
  d=['plain-at: person#1', 'plain-at: queen#1', 'gloss: honor=on:I'],
  n=N('AUDIT FV-L16c s.5, AUD2-LEDGER16-3 s.5', "'person' (key row 5) and 'queen' (key row Danger) are plain, so the River Queen is read in full and 'in person' is plain; 'honor' = on ('on arrival', phonetic, I). Header: Stanton left Washington 1 PM for City Point by the River Queen; context OR I/46 pt 3 p.28."))
S('E558', d=['variant: polking=Polka', 'merge: opera+tours', 'gloss: operatours=operators:I'],
  h=[("(FM65-E; row 5912/1)", "(FM65-E; row 5912/1; image-read by FV-L16c; context E560 and holder 8605)")],
  n=N('AUDIT FV-L16c s.5, AUD2-LEDGER16-3 s.5', "'polking' = [Command]ing (Polka = Command + -ing; E560 / MS18-R5 precedent); 'opera tours' = operators (phonetic, I). The address-line 'Washington' fix stands from FIX-L15."))
S('E569', d=['plain-at: washington#1', 'variant: polking=Polka', 'merge: off+i+sir', 'gloss: offisir=officer:I', 'merge: corn+fed+in+shall', 'gloss: cornfedinshall=confidential:I', 'gloss: toby=to_be:I'],
  h=[("(FM65-F; row 5924/0;", "(FM65-F; row 5924/0; image-read by FV-L16c;")],
  n=N('AUDIT FV-L16c s.5, AUD2-LEDGER16-3 s.5', "the address-line 'Washington' is plain (lesson 8, key row Volunteer misfires; FIX-L16 left E569 to this audit); 'polking' = [Command]ing; 'off I sir' = officer, 'Corn fed in Shall' = confidential, 'toby' = to be (all phonetic, I). 'Mrs. Ord' ('Mentor') is the key reading and the WEAK flag stays."))
# ---- FV-L16d (+ AUD2-LEDGER16-4) ----
S('E441', h=[("also how wide at West Point;", "also how wide is [the] Mattapony at West Point (M: 'Martha pony' is plain-phonetic Mattapony, one occurrence);"),
             ("(FM-F1, filed from FM-R9; row 5699/1)", "(FM-F1, filed from FM-R9; row 5699/1; image-read by FV-L16d and AUD2-LEDGER16-4, matches the transcription; context OR I/36 pt 3 p.262, Butler's route across the Mattapony, and pp.281, 321)")],
  d=['merge: martha+pony', 'gloss: marthapony=Mattapony:M'],
  n=N('AUDIT FV-L16d s.5, AUD2-LEDGER16-4 s.3/s.5', "'Martha pony' is plain-phonetic Mattapony (M for the sense: one occurrence; strengthened by OR I/36 pt 3 p.262), not {time: 7 PM} [9]; 'it' = at (plain word, not graded). The FM-F1 note's phrase 'garbled by the decoder's time and number rows' is withdrawn. Class N3, D3 on the audits."))
S('E472', h=[("20 May 1864 1.30 PM Ft Monroe, Sheldon to the Quartermaster General (Meigs), Washington:", "20 May 1864 1.30 PM Washington, the Quartermaster General (Meigs) to Lt. Col. Herman Biggs, chief quartermaster, Fort Monroe (received):"),
             ("(FM-S3; row 5679/0; transcription only)", "(FM-S3; row 5679/0; image-read by FV-L16d, matches the transcription; received copy of E90 (mssEC 19 p.73, pointer 8965); the answer OR I/36 pt 3 pp.29-30, holder 4642)")],
  d=['plain-at: big#1'],
  n=N('AUDIT FV-L16d s.5, AUD2-LEDGER16-4 s.3', "header direction corrected: the Quartermaster General's office to Lt. Col. Biggs at Fort Monroe, received; it is the received copy of E90 (mssEC 19 p.73, pointer 8965). 'big' = Biggs (plain). The answer is printed OR I/36 pt 3 pp.29-30 (holder 4642). Upheld by AUD2-LEDGER16-4 in full."))
S('E442', h=[("one at the [Bermuda] landing", "one at the Bermuda landing"),
             ("(FM-F1, filed from FM-R9; row 5707/0)", "(FM-F1, filed from FM-R9; row 5707/0; image-read by FV-L16d and AUD2-LEDGER16-4, matches the transcription; context OR I/36 pt 3 p.262 (antecedent) and p.322)")],
  d=['plain-at: bermuda#1'],
  n=N('AUDIT FV-L16d s.5, AUD2-LEDGER16-4 s.3', "'Bermuda' is plain (the Bermuda landing), not the key row White River; the M for the landing is dropped. Context OR I/36 pt 3 p.262 and p.322. Upheld by AUD2-LEDGER16-4 in full (Hebrew = Williamsburg)."))
S('E473', h=[("for Captain Clark: [new regime, Edgar's name]; why [publish] Edgar's name;", "for Captain [H. C.] Clark, [editor of the] New Regime: why publish Edgar's name (Capt. George P. Edgar, aide to the provost marshal at Norfolk; identity supported, context not a C grade);"),
             ("(FM-S3; row 5633/1; transcription only)", "(FM-S3; row 5633/1; image-read by FV-L16d and AUD2-LEDGER16-4, matches the transcription; context Peirpoint 1864 pp.35, 39-41, Butler Corr. IV p.339)")],
  d=['plain-at: publish#1'],
  n=N('AUDIT FV-L16d s.5, AUD2-LEDGER16-4 s.3/s.5', "'publish' is plain (key row 100 misfires), so the decode is H 6 of 6. Addressee: Capt. H. C. Clark, aide-de-camp on Butler's staff and editor of the New Regime (Peirpoint pp.35, 39-41); Edgar most likely Capt. George P. Edgar, aide to the provost marshal at Norfolk (supported, context only)."))
S('E469', h=[("30 May 1864 7.30 PM, Gen Butler's Hd Qrs,", "30 May 1864 7.30 PM (ledger header 30 May; the day code reads 29, M: it conflicts with the ledger date), Gen Butler's Hd Qrs,"),
             ("(FM-F1, filed from FM-S2; row 5720/0)", "(FM-F1, filed from FM-S2; row 5720/0; image-read by FV-L16d and AUD2-LEDGER16-4; context OR I/36 pt 3 p.415, Butler to Stanton 31 May; the next row 5720/1 is headed 'May 30 / 7.30 P.M.' in clear)")],
  n=N('AUDIT FV-L16d s.5, AUD2-LEDGER16-4 s.3/s.5', "'harsh pony' = 20 + 9 = 29 (H as key values after the transcription fix 'poney' -> 'pony', image-checked; the old reading is kept here); FV-L16d's re-dating to 29 May is NOT upheld, the header stays 30 May 7.30 PM (ledger header, the clear next row 5720/1, OR I/36 pt 3 p.415), and the sense of 'harsh pony' is M. The place 'battery [Bridge]' stays M (a guess, not a reading). Depth D2."))
LF['E469'] = ("harsh poney", "harsh pony")
S('E466', h=[("I referred your telegram about Dunn to General Butler;", "I referred your telegram about Dunn (the Cherrystone operator, W. A. Dunn; antecedent 5637/0-1) to General Butler;"),
             ("(FM-F1, filed from FM-S2; row 5638/0)", "(FM-F1, filed from FM-S2; row 5638/0; image-read by FV-L16d and AUD2-LEDGER16-4, matches the transcription; antecedent 5637/0-1 in clear)")],
  n=N('AUDIT FV-L16d s.5, AUD2-LEDGER16-4 s.3/s.5', "no decoder change. 'Dunn' = the Cherrystone operator (W. A. Dunn, holder 13561), supported by the facing page 5637/0-1 (Eckert 28 Apr on Dunn's loyalty, Sheldon's answer). Depth raised to D3 by AUD2-LEDGER16-4 (every cipher token H, external check in clear text)."))
base.E = E
if __name__ == '__main__': base.run('ciphertext.txt')
