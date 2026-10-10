#!/usr/bin/env python3
"""FIX-L15 (10 Oct 2026, account 1, for LANE LEDGER-15): apply the s.5 corrections of AUDIT (FV-L15a/b/c/d/n) and AUDIT 2 (AUD2-LEDGER15-1..4) to
ciphertext.txt (Fort Monroe entries) as header edits, decoder directive lines and one 'note: FIX-L15' line per entry. Same method as fixaud2l14_apply.py;
reading.md only by decode.py --write. Idempotent: skips a block that already has a 'FIX-L15' note. Two one-word line fixes, both image-checked by the
audit (E560 'William D. James' -> 'William L. James', E575 'sacy' -> 'say'), are recorded in the entry note."""
MARK = 'FIX-L15 (10 Oct 2026'
E = {}
LF = {}   # line fixes: entry -> (old, new)
def S(e, h=(), d=(), n=''): E[e] = dict(h=list(h), d=list(d), n=n)
def N(src, body): return "FIX-L15 (10 Oct 2026, account 1, for LANE LEDGER-15; %s): %s" % (src, body)

# ---- FV-L15d (+ AUD2-LEDGER15-4) ----
S('E539', h=[("(the row has 'William ah Parker' and 'Diversion' for Division, M)", "('William' plain, Wm. A. Parker; 'plaster Prescott' = Fifth Division, H, C-supported by holder 8538 'Comdg 5th Divn' and ORN I/11 p.634 'Comdg. Fifth Division')"),
              ("(FM65-D; row 5885/1)", "(FM65-D; row 5885/1; image-read by FV-L15d, matches the transcription; N2, substance in holder 8538, the clear copy of Lynch's forward, AUD2-LEDGER15-4)")],
  d=['plain-at: saint#1', 'plain-at: william#1'],
  n=N('AUDIT FV-L15d s.5, AUD2-LEDGER15-4 s.5, N2', "'saint' (key row Force) is the plain St. in 'ship saint lawrence' (the ordnance ship St. Lawrence) and 'William' (key row 100) is the plain Wm. in Wm. A. Parker; both read plain, so the decode is H 13 of 13. 'plaster Prescott' = Fifth Division (Plaster = 5, Prescott = Diversion, the clerk's homophone), H, C-supported by holder 8538 and ORN I/11 p.634. Class N2 (substance in holder 8538, Lynch's forward; FV-L15d's 'N3 weak' superseded), context ORN I/11 p.634."))
S('E528', h=[("signed by a Colonel and Quartermaster (name not in the row)", "signed [Col. R. C.] Webster, Quartermaster (M: the signature or Col. R. C. Webster)"),
             ("(FM65-C; row 5870/0)", "(FM65-C; row 5870/0; image-read by FV-L15d; context OR I/46 pt 2 pp.105-106 and holder 8514)")],
  d=['graded: webster:M'],
  n=N('AUDIT FV-L15d s.5', "'Webster' between Paradise (Colonel) and Vinton (Quartermaster) is the name (Col. R. C. Webster, Quartermaster at Monroe; the sibling 5866 spells 'Webb Stir'), or the Webster/Signature key row: read as written and graded M (H 14 + M 1). 'James' is plain (already read plain). Context in print: OR I/46 pt 2 pp.105-106; holder 8514."))
S('E500', h=[("(FM65-A; row 5847/2; read from the transcription, no image)", "(FM65-A; row 5847/2; image-read by FV-L15d, matches the transcription; the row runs onto p.304, pointer 5848 row 0; context holder 7681 (5849))")],
  d=['plain-at: sampson#1', 'plain-at: anchor#1', 'plain-at: baltic#1', 'plain-at: william#1'],
  n=N('AUDIT FV-L15d s.5, AUD2-LEDGER15-4 s.5', "'Sampson' (key row Ferry), 'anchor' (Donelson), 'Baltic' (Chattahoochee) and 'William' (100) are plain words the key rows misfire on; read plain (H 11 of 11). Supersedes the 'Image not read (transcription only)' clause of the FM65-A note: the whole leaf was image-read by FV-L15d and the row runs onto p.304, pointer 5848 row 0. Context holder 7681 (5849)."))
S('E517', h=[("signed by the Quartermaster General (FM65-B; row 5861/1; text only)", "signed by the Quartermaster General (FM65-B; row 5861/1; image-read by FV-L15d, matches the transcription; sent from on board steamer [North]urn (M) at Monroe, I; siblings 5865 and 5868 = E525; Stanton's telegram 5861/2 = holder 8508)")],
  d=['plain-at: sampson#1', 'plain-at: baltic#1', 'variant: tremble=Tremble:M'],
  n=N('AUDIT FV-L15d s.5, AUD2-LEDGER15-4 s.5', "'Sampson' (Ferry) and 'Baltic' (Chattahoochee) are plain; 'tremble urn' (Tremble = North; 'urn' unread) stays M, so the steamer's name is M. The next row on the leaf (5861/2) is Stanton's own telegram from Fort Monroe, 6 Jan 1.30 PM (clear copy 8508), so a telegram signed Qr Master Genl U.S. from on board a steamer at Monroe that day fits the Quartermaster General travelling with the Secretary's party (inference, I)."))
S('E573', h=[("for [Secretary of the Navy at Washington] (M):", "for the Secretary of the Navy at Washington (C: ORN I/12 p.66 and holder 7823):"),
             ("'[Maj. Gen. Hurlbut] in from [Charleston]", "'The monitor Lehigh in from [Charleston]"),
             ("(FM65-F; row 5930/1)", "(FM65-F; row 5930/1; image-read by FV-L15d; N1: ORN I/12 p.66 and holder clear copy 7823)")],
  d=['plain-at: lehigh#1'],
  n=N('AUDIT FV-L15d s.5', "'Lehigh' is the plain name of the monitor Lehigh; the key row Hurlbut misfires on it (the FM65-F note's 'Hurlbut' identification is withdrawn). The Secretary of the Navy at Washington is C by print (ORN I/12 p.66, holder 7823). Class N1."))
S('E557', h=[("the [submarine torpedoes ('Sub squdron torpid owes', plain, read by hand, M)]", "the submarine torpedoes ('Sub squdron torpid owes', plain; 'Sub marine Torpedoes' in the clear copy, C)"),
             ("(FM65-E; row 5907/1)", "(FM65-E; row 5907/1; image-read by FV-L15d; N1: holder clear copy 7768)")],
  d=['plain-at: washington#1'],
  n=N('AUDIT FV-L15d s.5', "'Washington' in the address line 'Maj. Eckert , Washington' is the plain header word (key row Volunteer misfires); read plain. The torpedo phrase is C by the clear copy 7768 ('Sub marine Torpedoes'). Class N1. The same address-line misfire is corrected in E529, E513, E552, E560, E536, E568 and E558 by this job; every other 'Maj. Eckert , Washington' row outside these audits is listed in NOTES '## FIX-L15'."))
S('E558', d=['plain-at: washington#1'],
  n=N('AUDIT FV-L15d s.5', "'Washington' in the address line 'Maj. Eckert , Washington' is the plain header word (key row Volunteer misfires); read plain. No other change to this entry (not itself audited by FV-L15d)."))
# ---- FV-L15c (+ AUD2-LEDGER15-3) ----
S('E551', h=[("addressee and opening words unread (FM65-E; row 5898/1; weak, 41 words)", "from the Secretary of the Navy to Capt. J. M. Berrien, Comdt Navy Yard Norfolk ('Berrying', plain), opening words 'Are there' ('arthur', C by print); N1: printed in ORN I/12 (page to resolve), second cipher copy holder 9953 (p.287) (FM65-E; row 5898/1; image-read by FV-L15c)")],
  d=['plain-at: berrying#1', 'gloss: arthur=Are_there:C'],
  n=N('AUDIT FV-L15c s.5', "'Berrying' is the plain name Berrien (Capt. J. M. Berrien, Comdt Navy Yard Norfolk), not the key row Chief of Staff + -ing; 'arthur' = 'Are there' (the opening of the question, C by print). A question from the Secretary of the Navy (Welles) to Berrien at Norfolk, printed ORN I/12 (page to resolve); class N1. A second cipher copy sits in the Washington sent ledger at holder 9953 (p.287), a cross-reference only, not filed as a new entry."))
S('E552', h=[("promised] to [an officer, name unread]", "promised] to Commo. Bell"),
             ("signed 'Jay M. ...' (unread)", "signed Jay M. Berrien, Comdt (Capt. J. M. Berrien, Norfolk; 'Berrying polkant')"),
             ("(FM65-E; row 5899/0)", "(FM65-E; row 5899/0; image-read by FV-L15c; N1: from Berrien at Norfolk for the Secretary of the Navy, 5.20 P.M., clear copy 7749, p.91)")],
  d=['plain-at: washington#1', 'plain-at: promised#1', 'plain-at: berrying#1', 'gloss: polkant=Comdt.:I', 'merge: ditto+door', 'gloss: dittodoor=Commo.:I'],
  n=N('AUDIT FV-L15c s.5', "'promised' is plain (not the key row 1000 + d); 'Berrying polkant' = Berrien Comdt (plain name + Polka = Command, phonetic, I); 'ditto door Bell' = Commo. Bell (phonetic, I). From Berrien at Norfolk for the Secretary of the Navy, 5.20 P.M.; clear copy holder 7749 (p.91); class N1."))
S('E529', h=[("12 Jan 1865 Ft Monroe,", "13 Jan 1865 (the leaf's dateline reads Jan. 12; the date group 'Fever' = 13, holder 7696) Ft Monroe,"),
             ("(plain 'John Rod jars'; the decoder prints [Maj Genl U.S. Grant] for 'John', a misfire)", "(plain 'John Rod jars' = John Rodgers at Norfolk, no rank in 7696; 'John' now read plain)"),
             ("the blockade runner arrived 4 PM", "the blockade runner Julia arrived (the word 'Julia' is the name, M, not the 4 PM time word)"),
             ("(FM65-C; row 5871/0)", "(FM65-C; row 5871/0; image-read by FV-L15c; N1: holder clear copy 7696, p.38)")],
  d=['plain-at: john#1', 'plain-at: washington#1', 'graded: julia:M'],
  n=N('AUDIT FV-L15c s.5', "'John' is plain (John Rodgers), 'Washington' in the address line is plain; 'Julia' is the blockade runner Julia per 7696 (read as written, M; not the Julia = 4 PM time row). Date 13 Jan 1865 ('Fever' = 13; holder 7696), from John Rodgers at Norfolk (7696 gives no rank). Clear copy 7696 (p.38); class N1."))
S('E513', h=[("5 Jan 1865 1 PM Ft Monroe", "5 Jan 1865 Ft Monroe (leaf header 1 P. M.; the holder clear copy 8505 gives 2 PM)"),
             ("(FM65-B; row 5857/1; text only)", "(FM65-B; row 5857/1; image-read by FV-L15c; N1: holder clear copy 8505, p.27)")],
  d=['plain-at: amos#1', 'plain-at: washington#1', 'gloss: whipal=Regimental:H'],
  n=N('AUDIT FV-L15c s.5', "'Amos' is the plain first name of Amos Binney (key row New York misfires); 'whipal' = [Regiment]al (Whip = Regiment + al, H); 'Washington' in the address line is plain. Clear copy holder 8505 (p.27), 2 PM; class N1."))
S('E515', h=[("(FM65-B; row 5858/1; text only)", "(FM65-B; row 5858/1; image-read by FV-L15c; N2: substance in OR I/46 pt 2 p.51 (Meigs) and p.66 (Newport))")],
  d=['plain-at: sampson#1', 'plain-at: baltic#1', 'plain-at: william#1'],
  n=N('AUDIT FV-L15c s.5', "'Sampson' (Ferry), 'Baltic' (Chattahoochee) and 'William' (100) are plain; read plain. Substance in OR I/46 pt 2 p.51 (Meigs) and p.66 (Newport); class N2."))
S('E549', h=[("answer; T. T. Eckert (FM65-D; row 5896/2; 50 tokens)", "answer; closing line 'T. T. Eckert' (the office for Eckert; the sender's person M); context OR I/47 pt 2 pp.189-190 and p.205 (Eckert at Fort Monroe 2 Feb 1 p.m.), Plum II p.274, holder 7870 (Mack in North Carolina to 14 Apr 1865) (FM65-D; row 5896/2; 50 tokens; image-read by FV-L15c)")],
  n=N('AUDIT FV-L15c s.5, AUD2-LEDGER15-3 s.4', "no decoder change. Sender M (the Washington office for Eckert; the closing line carries Eckert's name). Context OR I/47 pt 2 pp.189-190 and p.205, Plum II p.274 (Richard O'Brien and a party sent with Schofield), holder 7870. N3 D3 confirmed by the second audit; O'Brien 1910 (Telegraphing in Battle) is a live lead."))
# ---- FV-L15b (+ AUD2-LEDGER15-2) ----
S('E545', h=[("Lieut. Colonel G. W. Schofield (as written)", "Lieut. Colonel G. W. Schofield (as written; the general's brother, plain)"),
             ("(FM65-D; row 5889/2; 51 tokens)", "(FM65-D; row 5889/2; 51 tokens; image-read by FV-L15b; N1: holder clear copy 7731, Huntington object 8066; not filed under the RULING had it been found first)")],
  n=N('AUDIT FV-L15b s.5', "no decoder change: 'a vinton' reads a [Quartermaster] (clear copy 'a Qr Mr'), C by the clear copy; addressee G. W. Schofield is the general's brother (plain name, not M). Clear copy 7731 (Huntington object 8066); not filed as a new entry under the RULING had it been found at intake."))
S('E560', h=[("[William] D. James", "William L. James"),
             ("(FM65-E; row 5915/0)", "(FM65-E; row 5915/0; image-read by FV-L15b; N1: holder clear copy 8605, object 8886, OR I/46 pt 2)")],
  d=['plain-at: washington#1', 'plain-at: william#1', 'gloss: polking=Comdg.:C'],
  n=N('AUDIT FV-L15b s.5', "transcription line 'William D. James pilgrim' corrected to 'William L. James pilgrim' (leaf 5915, clear copy 8605, OR I/46 pt 2: Capt. William L. James, A.Q.M.; the old reading is kept here). 'Washington' in the address line and 'William' are plain (key rows Volunteer and 100 misfire); 'polking' = Comdg. (no key row; C by the clear copy). The FM65-E note's 'pagan [Battery] is a slip (M)' is withdrawn: 'pagan' = Battery is right, a telegraph battery. Clear copy 8605 (object 8886)."))
LF['E560'] = ("William D. James pilgrim", "William L. James pilgrim")
S('E505', h=[("(FM65-A; row 5851/1; transcription only)", "(FM65-A; row 5851/1; image-read by FV-L15b and AUD2-LEDGER15-2, matches the transcription; msg 2 is from Capt. Howell at City Point to Col. Webster, S. H. Beckwith the operator; msg 1 N1 (OR I/46 pt 2 p.21), msg 2 N3 D2)"),
             ("(2) City Point 9.30 PM, Beckwith to Sheldon: Gen. Rawlins wishes", "(2) City Point 9.30 PM, Capt. Howell (S. H. Beckwith the operator) to Col. Webster at Fort Monroe: Gen. Rawlins wishes")],
  d=['plain-at: webster#1', 'plain-at: webster#2', 'plain-at: william#1', 'variant: verion=Vernon:I', 'variant: wreate=Wreathe:I', 'plain-at: honor#1'],
  n=N('AUDIT FV-L15b s.5, AUD2-LEDGER15-2 s.3/s.5', "'Webster' (x2) and 'William' are plain names (Col. R. C. Webster, Capt. William T. Howell); msg 2 sender Capt. Howell, not Beckwith to Sheldon. Plain phonetic words: bessie = best, heifer = have her, addie shun tooth = addition to, utah = you to, honor = on her ('no rations will be required on her'; not a code word, so it leaves the count). 'verion' (the second audit reads verion/vernon, not 'venon') = the key row Vernon = Point (I); 'wreate' = Wreathe = Telegraph (I). Msg 2 count H 10 + I 2 of 12 code-word tokens (83.3% H), supersedes FV-L15b's H 10 + M 3 of 13. Msg 1 C by print, OR I/46 pt 2 p.21."))
S('E567', h=[("for [Maj. Gen. Grant/Rawlins at] City Point (M):", "for Maj. Gen. U. S. Grant at City Point (C by print):"),
             ("[Colonel] Wright", "Col. W. W. Wright"),
             ("(FM65-F; row 5920/1)", "(FM65-F; row 5920/1; image-read by FV-L15b; N1: in print, The Papers of Ulysses S. Grant vol. 14 (IA papersofulyssess0014gran; Google Books DVLPEPsH1_oC))")],
  n=N('AUDIT FV-L15b s.5', "no decoder change. Addressee Maj. Gen. U. S. Grant (Grant Papers vol. 14, 'Schofield telegraphed to USG'), not 'Grant/Rawlins (M)'; Wright = Col. W. W. Wright, military railroads, plain. In print: Grant Papers vol. 14 (IA papersofulyssess0014gran; Google Books DVLPEPsH1_oC). Class N1."))
S('E525', h=[("reads as signed R. M. Newport, Colonel and Quartermaster (FM65-C; row 5868/0)", "from Col. R. M. Newport, Colonel and Quartermaster, Baltimore (his printed signature, OR I/46 pt 2) to Col. R. C. Webster, Chief Quartermaster, Fort Monroe (both identified, not M; the operator is J. W. Sampson) (FM65-C; row 5868/0; image-read by FV-L15b and AUD2-LEDGER15-2; N3 D3; context holder 7693 (Newport 10 Jan), OR I/46 pt 2 Meigs 5 Jan and Wise 7 Jan 10.30 a.m.)")],
  d=['plain-at: baltic#1', 'plain-at: sampson#1', 'plain-at: webster#1', 'variant: princess=Princess:M'],
  n=N('AUDIT FV-L15b s.5, AUD2-LEDGER15-2 s.5', "'Baltic' (Chattahoochee), 'Sampson' (Ferry) and 'Webster' (Signature) are plain; 'princess' (the Captain row) stays M because Newport was a colonel. H 14 + M 1 of 15 (93.3%). Sender Col. R. M. Newport to Col. R. C. Webster, both identified. Context: holder 7693 (Newport 10 Jan), OR I/46 pt 2 Meigs 5 Jan and Wise 7 Jan 10.30 a.m."))
S('E572', h=[("[received/entered] 14 [March] ([Baltimore] as a place word, M)", "for C. C. Fulton, American office, Baltimore (C, holder clear copy 7822), 14 March"),
             ("(FM65-F; row 5929/2)", "(FM65-F; row 5929/2; image-read by FV-L15b; N1: holder clear copy 7822; the same news in the press of 16 Mar 1865)")],
  d=['gloss: ditto=N._C.:C'],
  n=N('AUDIT FV-L15b s.5', "the header word group 'See See Full turn American office' + Baltimore is 'for C. C. Fulton, American office, Baltimore' (C by the clear copy 7822), not a received/entered line with Baltimore as a place word; 'ditto' = N. C. (Wilmington N. C., C by the clear copy); the tail 'youth no yoke' = 'sig No sig' (no signature, of course not sent)."))
S('E171', h=[("(FM-R2a; row 5779/1; image-read)", "(FM-R2a; row 5779/1; image-read; N1: printed in full in OR ser. I vol. 43 pt 1 p.860, print 'Will await, as ordered', FV-L15n)")],
  n=N('AUDIT FV-L15n s.5', "no decoder change. The whole body is printed in OR I/43 pt 1 p.860 (Fort Monroe, 20 Aug 1864, 10 p.m., Heine to Halleck, Chief of Staff; print 'Will await, as ordered', ledger 'will wait as ordered'); every code group graded H is also C by print. Class N1 (was N3). Postmortem: the earlier N3 rested on a mislabelled volume (warofrebellion431unit = I/47 pt 2)."))
# ---- FV-L15n ----
S('E544', h=[("'All asked for has been ordered;", "'All asked for by you has been ordered;"),
             ("(FM65-D; row 5888/2; short, 28 tokens)", "(FM65-D; row 5888/2; short, 28 tokens; N1: OR I/46 pt 2 p.271 and Grant Papers vol. 13)")],
  n=N('AUDIT FV-L15n s.5', "no decoder change ('bayou' = by you). Header now carries 'by you' (the print has 'All asked for by you'); the code groups are C by print, OR I/46 pt 2 p.271 and Grant Papers vol. 13 (Grant to Palmer, New Berne, 26 Jan 1865, 10.30 a.m.). Class N1."))
S('E565', h=[("'I cannot find the scout that was to report to me this morning. [We shall] be ready", "'I cannot find the scout that was to report to me this morning. Will be ready"),
             ("(FM65-E; row 5919/1)", "(FM65-E; row 5919/1; N1: Grant Papers vol. 14, Roberts to Bowers, 5 Mar 1865, received 11.30 a.m.)")],
  n=N('AUDIT FV-L15n s.5', "no decoder change ('Wilby' = Will be). Header 'Will be ready' (leaf 'Wilby', print 'Will be'); in print Grant Papers vol. 14 (note: Col. S. H. Roberts, 139th N. Y., to Lt. Col. T. S. Bowers, received 11.30 a.m.; the ledger's sent 11.35 is the Fort Monroe hand). Class N1."))
S('E537', h=[("a code word that the decoder prints [New York], M)", "a code word 'frog' = New York, C by print: 'Steamer New York')"),
             ("(FM65-D; row 5883/0; short, 29 tokens)", "(FM65-D; row 5883/0; short, 29 tokens; N1: Grant Papers vol. 13, Grant to Ord, 20 Jan 1865, 6 P.M.)")],
  d=['gloss: frog=New_York:C'],
  n=N('AUDIT FV-L15n s.5', "'frog' (New York, the flag-of-truce steamer) is C by print (Grant Papers vol. 13: 'Steamer New York'), no longer M. Class N1."))
# ---- FV-L15a (+ AUD2-LEDGER15-1) ----
S('E536', h=[("General [Whiting, the row's 'Report'ing, M]", "General Whiting (plain)"),
             ("loss 'not exceed 6 ditto and 50' (numbers M)", "loss 'not exceed 6 ditto and 50' = 650 ('ditto' = hundred, C)"),
             ("(FM65-D; row 5879/0; 140 tokens)", "(FM65-D; row 5879/0; 140 tokens; image-read by FV-L15a; N1: holder clear copy 7703-7704 and New-York Daily Tribune 18 Jan 1865 p.1; every code group C by the clear copy)")],
  d=['plain-at: whiting#1', 'plain-at: washington#1'],
  n=N('AUDIT FV-L15a s.5', "'Whiting' is the plain name (Gen. W. H. C. Whiting), not the key row Report + -ing; 'pledge ditto and mansion' = six hundred and fifty (ditto = hundred), C by the clear copy; the decode still prints the two 'ditto' tokens as written because 'ditto' is also the stop word elsewhere in the row. Every code group C by the clear copy 7703-7704; Tribune 18 Jan 1865 p.1. Class N1 (not filed as unread under the mssEC 25 ruling's item i: kept as an independent re-decipherment)."))
S('E541', h=[("(FM65-D; row 5887/0; 85 tokens)", "(FM65-D; row 5887/0; 85 tokens; image-read by FV-L15a and AUD2-LEDGER15-1; = E85 (mssEC 18 p.277, pointer 9943, the Washington copy); N3 D3 weak: message 2's substance relayed in ORN I/11 p.634)")],
  d=['plain-at: webster#1', 'plain-at: saint#1', 'plain-at: ordnance#1', 'variant: audit=Audit:M'],
  n=N('AUDIT FV-L15a s.5', "'Webster' (Harriet paradise Webster vincent Animal) is the plain name Col. R. C. Webster, Quartermaster at Monroe, so the signature tail no longer opens there and both messages are read as text; 'saint' (Force) is the plain St. in St. Lawrence; 'Ordnance' (After the) is the plain 'the ordnance yard'; 'audit' (Rapidan) stays M (likely 'as it', 'available, as it will take months'). The signature tails are 'yoke rucker' and 'youth H a wise Chief Bureau T. T. Eckert'. = E85 (mssEC 18 p.277, pointer 9943, the Washington copy): E85 is the same telegram, read here."))
S('E555', h=[("(FM65-E; row 5904/1; BOOK-FM65 test row: clause reused, not re-derived)", "(FM65-E; row 5904/1; BOOK-FM65 test row: clause reused, not re-derived; image-read by FV-L15a and AUD2-LEDGER15-1; Washington's copy is in another cipher at mssEC 18 pointer 9957 (p.291, '#3'); 5904/0 above it is printed, OR I/46 pt 2 and a Grant Papers vol. 13 note)")],
  d=['variant: pledge=Pledge:M'],
  n=N('AUDIT FV-L15a s.5, AUD2-LEDGER15-1', "'promise' (1000) before 'Kisses' and 'pledge for spit' ([6] for [Men]) have no place in the sentence as read: M for both senses (tokens stand H by the key; 'pledge' graded M here, 'promise' not, because the word recurs elsewhere in the row as a true code word). Counts H 51 + M 2 of 53. 'Glass ring alls' is plain, probably Gen. Ingalls (phonetic, I). Washington's copy: mssEC 18 pointer 9957 (Page 291, '#3'); reading it is an independent cross-check. N3 D3, weak."))
S('E568', h=[("Sheldon to Maj. Thomas T. Eckert, Superintendent, &c., Washington: [General Schofield] arrived here this morning", "Richard O'Brien, Wilmington, 26 Feb 1865, to Maj. Thomas T. Eckert, Superintendent, &c., Washington, forwarded by Sheldon from Fort Monroe on 5 Mar ('arrived here this morning' is at Wilmington): [General Schofield] arrived here this morning"),
             ("20 [evacuate?] ,", "20 relays,"),
             ("4 [loring]'s [probably hatchets],", "4 hatchets,"),
             ("(FM65-F; row 5923/1;", "(FM65-F; row 5923/1; image-read by FV-L15a and AUD2-LEDGER15-1; O'Brien's diary, Telegraphing in Battle p.218: 26 Feb 'Sent order to Major Eckert for one hundred miles of material, twenty operators, twenty instruments, eight construction men';")],
  d=['plain-at: washington#1', 'plain-at: relays#1', 'plain-at: hatchets#1'],
  n=N('AUDIT FV-L15a s.5, AUD2-LEDGER15-1 s.5', "'relays' (key row Evacuate) = 20 relays and 'hatchets' (key row Loring) = 4 hatchets are plain telegraph stores, read plain (H 35 of 35). The telegram is R. O'Brien's from Wilmington of 26 Feb 1865, sent on by Sheldon from Fort Monroe on 5 Mar (O'Brien signs it; not 'Sheldon to Eckert ... arrived here'). O'Brien's diary (Telegraphing in Battle p.218, 26 Feb: 'Sent order to Major Eckert ...'; 27 Feb 'Russia left with my dispatches', by sea to Fort Monroe) summarises the request; its text is not printed. N3 D3."))
S('E575', h=[("[Impregnable]'s [cavalry]", "Sumner's cavalry"),
             ("sent 5 P.M., Beckwith to Sheldon", "sent 5 P.M. from City Point (S. H. Beckwith) to Sheldon"),
             ("[Nansemond?]", "Nansemond"),
             ("(FM65-F; row 5931/1)", "(FM65-F; row 5931/1; image-read by FV-L15a and AUD2-LEDGER15-1; Gordon's reply OR I/46 pt 2 p.993 and holder 5932; N3 D3 weak)")],
  d=['plain-at: summers#1', 'plain-at: nancy#1'],
  n=N('AUDIT FV-L15a s.5, AUD2-LEDGER15-1 s.3/s.5', "'summers' (Summer = Impregnable) is the plain name Sumner's cavalry; 'nancy' (the 8 PM time row) in 'Banks torch nancy moaned' is plain, the Nansemond ('nancy moaned'); line 6 reads 'party say plaster publish', transcribed 'sacy' (plain-word slip, image-checked at leaf 5931 line 6; the old reading 'sacy' is kept here); 'woody party say [500] [cavalry] hefty carry [pontoons] to [cross] to the not away' = 'would a party, say 500 cavalry, have to carry pontoons to cross to the Nottoway' (plain-phonetic, I). Sent from City Point (S. H. Beckwith), 15 Mar 5 PM; Gordon's reply OR I/46 pt 2 p.993 and holder 5932. H 24 of 24."))
LF['E575'] = ("party sacy plaster publish", "party say plaster publish")
S('E576', h=[("without [bridging]", "without pontoons"),
             ("(FM65-F; row 5933/0)", "(FM65-F; row 5933/0; image-read by FV-L15a and AUD2-LEDGER15-1; follows Gordon's 6.30 p.m. telegram of 15 Mar, OR I/46 pt 2 p.993; Ord's summary OR I/46 pt 3 p.9; N3 D3 weak)")],
  d=['plain-at: black#1', 'gloss: villager=pontoons:M'],
  n=N('AUDIT FV-L15a s.5, AUD2-LEDGER15-1 s.5', "'Black' (City Point row) in 'the Black water canby pocketed' is the plain Blackwater; 'villager' = Village (Pontoon) + -er, 'without pontoons' (Ord's printed summary: 'ferry or pontoons'), M. H 27 + M 1 of 28. Sent after Gordon's 6.30 p.m. telegram of 15 Mar (OR I/46 pt 2 p.993); Ord's summary OR I/46 pt 3 p.9."))

def run(F):
    L = open(F, encoding='utf-8').read().split('\n'); i = 0; done = []
    while i < len(L):
        hd = L[i].split(' ')
        if L[i].startswith('### ') and len(hd) > 1 and hd[1] in E:
            e = hd[1]; s = E[e]; j = i + 1
            while j < len(L) and not L[j].startswith('### '): j += 1
            blk = L[i:j]
            if any(l.startswith('note: ' + MARK) for l in blk): i = j; continue
            for old, new in s['h']:
                if old not in blk[0]: print('HEADER MISS', e, old[:70]); continue
                blk[0] = blk[0].replace(old, new, 1)
            if e in LF:
                old, new = LF[e]; hit = [x for x, l in enumerate(blk[1:], 1) if old in l and not l.startswith('note:')]
                if len(hit) != 1: print('LINE MISS', e, old)
                else: blk[hit[0]] = blk[hit[0]].replace(old, new, 1)
            k = next(x for x, l in enumerate(blk) if l.startswith('note:'))
            blk[k:k] = s['d']
            end = max(x for x, l in enumerate(blk) if l.strip())
            blk.insert(end + 1, 'note: ' + s['n'])
            L[i:j] = blk; done.append(e); i += len(blk)
        else: i += 1
    open(F, 'w', encoding='utf-8').write('\n'.join(L)); print(F, len(done), done)
    print('NOT FOUND:', sorted(set(E) - set(done)))

if __name__ == '__main__': run('ciphertext.txt')
