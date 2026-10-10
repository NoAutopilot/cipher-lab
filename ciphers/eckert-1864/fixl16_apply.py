#!/usr/bin/env python3
"""FIX-L16 (10 Oct 2026, account 1, for LANE LEDGER-16): apply AUDIT (FV-L15m) s.5 (E550, E543, E571, E465 and the clear-copy notes for E542 E548 E562)
and the NOTES '## FIX-L15' open lead (`plain-at: washington#1` on the 'Maj. Eckert , Washington' rows E166 E215 E250 E562 E542 E548 E550; NOT E546/E569)
to ciphertext.txt as header edits, decoder directive lines and one 'note: FIX-L16' line per entry. Same method as fixl15_apply.py (reused run());
reading.md only by decode.py --write. Idempotent: skips a block that already has a 'FIX-L16' note."""
import fixl15_apply as base
base.MARK = 'FIX-L16 (10 Oct 2026'
base.E.clear(); base.LF.clear()
E = base.E
def S(e, h=(), d=(), n=''): E[e] = dict(h=list(h), d=list(d), n=n)
def N(src, body): return "FIX-L16 (10 Oct 2026, account 1, for LANE LEDGER-16; %s): %s" % (src, body)
W = "'Washington' in the address line 'Maj. Eckert , Washington' is the plain header word (key row Volunteer misfires); read plain (NOTES '## FIX-L15' open lead)."

S('E550', h=[("for Captain Blodget, Quartermaster, Annapolis (2 AM):", "for Captain Blodget, Quartermaster, Annapolis:"),
             ("(FM65-D; row 5897", "(FM65-D; image-read by FV-L15m; N1: holder clear copy 8561, Page 83, word for word; row 5897")],
  d=['plain-at: washington#1', 'plain-at: anna#1', 'plain-at: apple#1'],
  n=N('AUDIT FV-L15m s.5', W + " 'anna police' is the place Annapolis (clear copy 'a Q m Annapolis'), not Anna = a 2 AM time word + 'police'; 'An apple is' is Annapolis (sound-spelling; clear copy 'arrive in annapolis'), not 'An [Sumter] is'; both read plain. 'ditto ditto ditto' repeats the three-word group, 'at Annapolis'. Header '(2 AM)' removed. Other code words (pilgrim, vinton, Kitten, whelp, Knapsack, Tappan) C by the clear copy. Clear copy holder 8561 (Page 83). Class N1."))
S('E543', h=[("see that in case of contingency", "so that in case of necessity (the ledger reads 'see that'; print 'so that')"),
             ("(FM65-D; row 5888/1", "(FM65-D; N1: OR ser. I vol. 46 pt 2 p.259, Grant to Ord, City Point 25 Jan 1865, 3 p.m.; row 5888/1")],
  d=['gloss: tarquinty=necessity:C'],
  n=N('AUDIT FV-L15m s.5', "'tarquinty' = Tarquin (key row Necessary) + 'ty' = necessity (print 'in case of necessity'), C by print; the header's 'contingency' withdrawn. Ledger 'see that' against print 'so that' is the ledger's own word (eye-checked by FV-L15m), not a reading error. Printed OR I/46 pt 2 p.259. Class N1."))
S('E571', h=[("with [convoy] for", "with pilots for"),
             ("(FM65-F; row 5929/1)", "(FM65-F; row 5929/1; N1: The Papers of Ulysses S. Grant vol. 14, in a note, Babcock to Rawlins; page unresolved)")],
  d=['plain-at: pilot#1'],
  n=N('AUDIT FV-L15m s.5', "'pilot' is the plain word 'pilots' (print 'with pilots for Col Roberts'); the key row Pilot = Capture misfires here and the FM65-F note's 'Capture' reading is withdrawn. Shannon = gunboat is C by print ('gun boats'); signer Babcock (print 'Babcock, Fort Monroe, telegraphed to ... Rawlins'). In print: Grant Papers vol. 14 (Google Books DVLPEPsH1_oC; IA papersofulyssess0014gran), page unresolved. Class N1. Lead: the opening entry of leaf 5929 (12 Mar 1865, Glisson to the Sec. Navy) has a holder clear copy at 7818 (Page 160)."))
S('E465', h=[("(FM-S2; row 5768/3;", "(FM-S2; N1: holder clear copy 4788 (Page 347) and OR ser. I vol. 40 pt 3 p.142 (abridged); row 5768/3;")],
  d=['merge: feeble+ghost', 'gloss: feebleghost=10_15:H'],
  n=N('AUDIT FV-L15m s.5', "'feeble ghost' = 10 15 (Feeble = 10, Ghost = 15, H; clear copy '10th 15 am', print '10.15 a.m.'), read as two numeral words, not summed to [25]; the header's 10.15 AM stands. Clear copy 4788 (Page 347); OR I/40 pt 3 p.142 (abridged: omits 'of the New Orleans troops'). Class N1."))
S('E542', d=['plain-at: washington#1'],
  n=N('AUDIT FV-L15m s.5', W + " Clear copy holder 7722 (Page 64), body identical word for word (grapes = Washington, John = Grant, Farmer = Norfolk, Buxton = Sec. Navy all C); signer Berrien. Class N1."))
S('E548', d=['plain-at: washington#1'],
  n=N('AUDIT FV-L15m s.5', W + " Clear copy holder 7741 (Page 83), identical ('enemy' in the clear copy is the holder transcriber's misreading of the ledger's 'immed'y'); 'Annie police' = Annapolis plain. Class N1."))
S('E562', h=[("His confidential [statement] is clear", "His confidential is clear")],
  d=['plain-at: washington#1'],
  n=N('AUDIT FV-L15m s.5', W + " Clear copy holder 7787 (Page 129), identical word for word; the clear copy has no 'statement' (the header gloss was editorial and is removed). Class N1."))
for e in ('E166', 'E215', 'E250'):
    S(e, d=['plain-at: washington#1'], n=N('NOTES FIX-L15 open lead', W + " No other change to this entry."))
base.E = E
if __name__ == '__main__': base.run('ciphertext.txt')
