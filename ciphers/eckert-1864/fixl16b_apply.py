#!/usr/bin/env python3
"""FIX-L16b (10 Oct 2026, account 1, for LANE LEDGER-16): apply s.5 of AUDIT (FV-L16c) for E566 E577 and AUDIT (FV-L16e) for E468 E470 E443 E445 E446 E448
(the entries no second audit holds; E564 E574 E558 E569 and E447 E471 E474 and FV-L16a's six wait for the FIX after the second audits) to ciphertext.txt as
header edits, decoder directive lines and one 'note: FIX-L16b' line per entry. Same method as fixl16_apply.py / fixl15_apply.py (reused run());
reading.md only by decode.py --write. Idempotent: skips a block that already has a 'FIX-L16b' note."""
import fixl15_apply as base
base.MARK = 'FIX-L16b (10 Oct 2026'
base.E.clear(); base.LF.clear()
E = base.E
def S(e, h=(), d=(), n=''): E[e] = dict(h=list(h), d=list(d), n=n)
def N(src, body): return "FIX-L16b (10 Oct 2026, account 1, for LANE LEDGER-16; %s): %s" % (src, body)

S('E566', h=[("(FM65-F; row 5919/2)", "(FM65-F; row 5919/2; image-read by FV-L16c, matches the transcription; N1: OR ser. I vol. 46 pt 2 p.847, Sumner to Turner, Fort Monroe 5 Mar 1865 12 m.; the print omits 'Colonel' and 'Leave soon so get quick answer', which are the ledger's own)")],
  n=N('AUDIT FV-L16c s.5', "no decoder change. 'Turn her' = Turner is plain-phonetic (I; C by the print 'Brig. Gen. Turner'); Francis = 12, palsy = Brigadier General, Berry = Chief of Staff, whip = regiment, rape = expedition, frog = New York agree with the print (C). The header word 'Colonel' (paradise, H) and the closing 'Leave soon so get quick answer' are not in OR I/46 pt 2 p.847. Class N1."))
S('E577', h=[("when informed of the order [of Gen.] Abbot to issue [it],", "when informed of the order about to issue,"),
             ("(FM65-F; row 5933/2)", "(FM65-F; row 5933/2; image-read by FV-L16c; N1: printed G. H. Gordon, A War Diary of Events (1882) p.384, Ord's telegram of 18 Mar 1865; the cipher copy is Hd qrs A. J. (operator Emerick), Ord's headquarters, relayed by Sheldon to Gordon at Norfolk; the signature word 'mereden' is an unread name, M)")],
  d=['plain-at: abbot#1', 'merge: there+four', 'gloss: therefour=therefore:I'],
  n=N('AUDIT FV-L16c s.5', "'abbot' is the plain-phonetic 'about' (Gordon's print 'the order about to issue'; the key row Abbot = Minnesota misfires), so the header's 'order of Gen. Abbot' is withdrawn. 'Francis' after the address is a time word = 12 (M: the print gives no hour); the decoder's line join ('Monroe -' + 'Francis') hides it, so it stays as written and is not graded here. 'there four' = therefore (I). 'mereden' after yoke (= signed) is an unread signature name, left as written. H 10 + M 1 of 11 code groups, 8 C by the print. Printed Gordon 1882 p.384; class N1."))
S('E468', h=[("for Butler: [if so] I will meet you [at Monroe] tomorrow at 10.30 AM and the Admiral there at 3 PM; about", "for Butler, from Grant at City Point (10.30 AM, the time of sending; Beckwith the operator): 'will you be at Fort Monroe all day tomorrow? If so I will meet you and the Admiral there at 3 PM'"),
             ("(FM-F1, filed from FM-S2; row 5810/1)", "(FM-F1, filed from FM-S2; row 5810/1; image-read by FV-L16e, matches the transcription; N1: OR ser. I vol. 42 pt 3 p.735, Butler Correspondence vol. V p.369, Grant Papers vol. 13)")],
  d=['plain-at: alday#1', 'plain-at: beat#1', 'graded: monday:M', 'graded: miller:M', 'graded: about:M'],
  n=N('AUDIT FV-L16e s.5', "the header's 'I will meet you tomorrow at 10.30 AM' misplaced the hour: 10.30 AM is the time of sending (print 'City Point, 10.30 a.m.'); the telegram is Grant's to Butler, 'Will you be at Fort Monroe all day tomorrow? If so I will meet you and the Admiral there at 3 p.m.' 'Alday' = all day and 'beat' = be at are plain-phonetic; 'Monday miller' (printed 'Will you') and the 'about' after the signature are unexplained by the key: M. Every code word C against the print (Knox = Butler, Elizabeth = 10.30 AM, animal = Monroe, whelp = tomorrow, Imogene = 3 PM, youth = signed, John = Grant). Class N1: OR I/42 pt 3 p.735; Butler Corr. V p.369; Grant Papers vol. 13 (the sent original at CSmH)."))
S('E470', h=[("for D. D. Porter: your telegram received; the three monitors Mahopac, Canonicus and Saugus are ready for service; Commander Parker", "for D. D. Porter: your telegram received; the three monitors Mahopac, Canonicus and Saugus are ready for service; Commander [Wm. A.] Parker (signature plain, 'park Kerr')"),
             ("(FM-F1, filed from FM-S2; row 5814/0)", "(FM-F1, filed from FM-S2; row 5814/0; image-read by FV-L16e, matches the transcription; N2: substance in Parker's letter of the same day, ORN I/11 p.116)")],
  n=N('AUDIT FV-L16e s.5', "no decoder change. 'park Kerr' is the plain name Parker, so the signature is not M ('Commander [Wm. A.] Parker', Wm. A. Parker, Commanding Fifth Division). Deborah = 8 AM, Niagara = D. D. Porter, wrangle = telegram, pebble = 3, polkaer = Command-er: H, and C in sense against ORN I/11 p.116. H 8 of 8. Class N2 (the substance is printed in Parker's letter of 1 Dec 1864; this telegram's text is not)."))
S('E443', h=[("(FM-F1, filed from FM-S1; row 5785/1; image-read at 2400 px by FM-S1)", "(FM-F1, filed from FM-S1; row 5785/1; image-read at 2400 px by FM-S1 and FV-L16e; context OR I/42 pt 3 p.1153, yellow fever at New Berne; John Horner the New York operator, Plum vol. II; N3 weak, D1)")],
  d=['plain-at: john#1', 'plain-at: fever#1'],
  n=N('AUDIT FV-L16e s.5', "'John' in 'John Horner New York' is the addressee's first name (key row Maj Genl U.S. Grant misfires) and 'fever' in 'Yell oh fever' is plain (yellow fever; key row 13 misfires); both read plain, so the reading is H 6 of 6, not 8. The address-line artefact and '13 for fever' are withdrawn. Body code word 1 (Newbern); too short for a clause: D1, N3 (weak)."))
S('E445', h=[("(FM-F1, filed from FM-S1; row 5816/2; image-read at 2400 px by FM-S1)", "(FM-F1, filed from FM-S1; row 5816/2; image-read at 2400 px by FM-S1 and FV-L16e, matches the transcription; N3 weak, D1)")],
  n=N('AUDIT FV-L16e s.5', "no decoder change. 'Hendron' stays as written (image; 'City of Hudson' is a guess); Knave = Maj Gen B. F. Butler in the sign-off position stays M; 'sly' and 'furies' unread (M). H 6 + M 1 of 7; one body code word (tomorrow): D1, N3 (weak)."))
S('E446', h=[("(FM-F1, filed from FM-S1; row 5583/2)", "(FM-F1, filed from FM-S1; row 5583/2; image-read by FV-L16e, matches the transcription; context ORN I/9 p.527, William H. Dunn, Cherrystone operator, 5 Mar 1864; N3 weak, D1)")],
  d=['plain-at: cherry#1'],
  n=N('AUDIT FV-L16e s.5', "'Cherry' in 'Cherry Stone' is plain (Cherrystone; key row Humboldt misfires), so the [Humboldt] reading is withdrawn. Knox = Butler, Stephen = In the, Banditti = Baltimore: H 3 of 3, too short for a clause: D1, N3 (weak). Context ORN I/9 p.527 (Titan, William H. Dunn)."))
S('E448', h=[("(FM-F1, filed from FM-S1; row 5793/1)", "(FM-F1, filed from FM-S1; row 5793/1; image-read by FV-L16e, matches the transcription; the companion 5793/2 is clear on the page and not yet filed; N3 weak, D1)")],
  d=['plain-at: washington#1', 'plain-at: wharf#1'],
  n=N('AUDIT FV-L16e s.5', "'wharf' is plain ('be at wharf'; key row Today misfires), so [Today] is withdrawn; 'Washington' in the date line is plain (key row Volunteer by collision). grapes = Washington and brutus = Secretary of War (H), both read in clear in the companion 5793/2. H 2 of 2, too short for a clause: D1, N3 (weak)."))
base.E = E
if __name__ == '__main__': base.run('ciphertext.txt')
