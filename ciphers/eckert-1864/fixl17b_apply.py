#!/usr/bin/env python3
"""FIX-L17b (10 Oct 2026, account 1, for LANE LEDGER-17): apply s.5 of AUDIT (FV-L16a) for E509 E511 E514 E521 E508 E506 and AUDIT (FV-L16e) for E447 E471
E474, as amended by AUDIT 2 (AUD2-LEDGER16-1 for the six, AUD2-LEDGER16-5 for the three), to ciphertext.txt as header edits, decoder directive lines and one
'note: FIX-L17b' line per entry. Same method as fixl17a_apply.py / fixl15_apply.py (reused run()); reading*.md only by decode.py --write. Idempotent: skips a
block that already has a 'FIX-L17b' note. key.md is not edited (the Francis/Topsy time rows stay held; E474 takes Frances = Francis as an entry-level variant)."""
import fixl15_apply as base
base.MARK = 'FIX-L17b (10 Oct 2026'
base.E.clear(); base.LF.clear()
E = base.E; LF = base.LF
def S(e, h=(), d=(), n=''): E[e] = dict(h=list(h), d=list(d), n=n)
def N(src, body): return "FIX-L17b (10 Oct 2026, account 1, for LANE LEDGER-17; %s): %s" % (src, body)
IMG = "image-read by FV-L16a and AUD2-LEDGER16-1, matches the transcription"

# ---- FV-L16a (+ AUD2-LEDGER16-1) ----
S('E509', h=[("Hd Qrs. Army of the James 5 PM, R. O'Brien to Sheldon for Col. Dodge:", "Ft Monroe 5 PM (via Sheldon), from Col. R. C. Webster to R. O'Brien at Hd Qrs. Army of the James, for Col. George S. Dodge:"),
             ("the Bendford is not here", "the Ben De Ford is not here"),
             ("the hospital boat Metropolis;", "the hospital boat [West]ern Metropolis (the hospital steamer, H);"),
             ("signed Sheldon (FM65-A; row 5854/0; transcription only)", "signed Webster (the signer's plain name; Sheldon the operator) (FM65-A; row 5854/0; %s; answers Dodge's request printed OR I/46 pt 2 pp.34-35 (= holder 5853/0, unfiled); O'Brien, Telegraphing in Battle pp.179-180; Western Metropolis a hospital transport, Medical and Surgical History 1870)" % IMG)],
  d=['plain-at: dodge#1', 'plain-at: webster#1', 'graded: orcey:M'],
  n=N('AUDIT FV-L16a s.5, AUD2-LEDGER16-1 s.3/s.5', "'Dodge' (key row McMinnville) is the plain name Col. George S. Dodge; the closing 'Webster' (key row Signature) is the signer's plain name, Col. R. C. Webster, not a signature word; 'Wicoff win Metropolis' = [West]ern Metropolis (H, the hospital steamer; the reader's M lifted); 'Orcey' (after 'John' = Grant) is unread (M). Header direction: from Fort Monroe (Webster, via Sheldon) to R. O'Brien at Hd Qrs. Army of the James, for Dodge, not 'R. O'Brien to Sheldon' (FV-L16a s.5). Counts H 12 + M 1 of 13."))
S('E511', h=[("S. H. Beckwith to Sheldon at Ft Monroe, from Gen. Rawlins:", "Capt. W. T. Howell (operator S. H. Beckwith) to Col. Webster at Ft Monroe, for Gen. Rawlins:"),
             ("signed Howell (FM65-A; row 5855/2; transcription only)", "signed W. T. Howell (FM65-A; row 5855/2; %s; context OR I/46 pt 2 p.90, ORN I/11 pp.~574-575)" % IMG)],
  d=['plain-at: webster#1', 'plain-at: william#1', 'graded: ditto:M'],
  n=N('AUDIT FV-L16a s.5, AUD2-LEDGER16-1 s.3', "structure error corrected: 'Webster' after 'Laura' (5.30 PM) is the addressee (Col. R. C. Webster), plain, so the signature tail no longer opens there and the whole message is read as text; the tail is 'walrus William Tea Howl' = [signed] W. T. Howell, 'William' plain (the initial). 'ditto' before 'Nutmeg' (= Available) is unexplained (M). 'shelby rawlins' = General Rawlins (plain name). H 12 + M 1 of 13."))
S('E514', h=[("S. H. Beckwith to Sheldon at Ft Monroe, for a colonel:", "Brig. Gen. Ingalls (operator S. H. Beckwith) to Sheldon at Ft Monroe, for Colonel Webster, chief quartermaster, Fort Monroe:"),
             ("a Dr/Mr Leary is required", "the C. C. Leary is required"),
             ("signed Ingalls, Beckwith (FM65-B; row 5858/0; text only)", "signed Ingalls, Beckwith (FM65-B; row 5858/0; %s; context OR I/46 pt 2 p.22, OR I/46 pt 1 p.166, holder 8506, Ingalls 5 Jan 4.30 PM, 'for special service')" % IMG)],
  d=['plain-at: webb#1', 'merge: way+worner'],
  n=N('AUDIT FV-L16a s.5, AUD2-LEDGER16-1 s.3/s.5', "'Webb steer' = Webster (plain-phonetic, the clerk's split of a name that is itself a code word; 'Webb' = Reinforcements misfires); 'way worner' = Wayworn (Steam) + -er, 'sea-going [steam]er' (H; the reader left it plain). 'the see C Leary' = the C. C. Leary. H 12 of 12."))
S('E521', h=[("(FM65-D, from FM65-B's decode of row 5861/2, second message only; short, about 24 tokens)", "(FM65-D, from FM65-B's decode of row 5861/2, second message only; short, about 24 tokens; %s; the first message of row 5861/2 (Stanton to Mrs Stanton, 6 Jan) = holder 8508; parallel 8491 (Beckwith's discreet inquiry, 29 Dec 1864); context holder 8509, OR I/46 pt 2 p.52, O'Brien pp.180-181)" % IMG)],
  n=N('AUDIT FV-L16a s.5, AUD2-LEDGER16-1 s.3/s.5', "no decoder change (H 4 of 4). Header carries E521 as the second message of row 5861/2, whose first message has its clear copy at 8508; parallel 8491; context 8509."))
S('E508', h=[("Sheldon to Beckwith for Capt. Howell, AQM, from Webster:", "Sheldon to Beckwith for Capt. W. T. Howell, AQM, from Col. Webster:"),
             ("(FM65-A; row 5853/1; transcription only; about 28 words)", "(FM65-A; row 5853/1; %s; about 28 words)" % IMG)],
  d=['plain-at: william#1', 'plain-at: webster#1', 'unjoin: here'],
  n=N('AUDIT FV-L16a s.5, AUD2-LEDGER16-1 s.3', "'hereWalrus' was one glued token: the line-end dash is a printed dash, so 'Walrus' (= Signature, H) is read on its own and opens the tail; 'Webster' after it is the signer's plain name (not [signed]); 'William' before 'Tea Howell' is the initial W. (plain). H 7 of 7."))
S('E506', h=[("S. H. Beckwith to Sheldon at Ft Monroe, from Gen. Rawlins:", "Capt. W. T. Howell (operator S. H. Beckwith) to Col. Webster at Ft Monroe, for Gen. Rawlins:"),
             ("(FM65-A; row 5852/1; transcription only; about 25 words)", "(FM65-A; row 5852/1; %s; about 25 words; answered by E507)" % IMG)],
  d=['plain-at: webster#1', 'plain-at: william#1'],
  n=N('AUDIT FV-L16a s.5, AUD2-LEDGER16-1 s.3', "structure error corrected: 'Webster' after 'Harriet penny' (1 PM, 4th) is the addressee, plain, so the message is read as text and the tail is only 'yoke William tea Howl' = [signed] W. T. Howell ('William' plain, the initial). 'ran lines' = Rawlins (plain-phonetic), 'inure' = in your. H 6 of 6."))
# ---- FV-L16e (+ AUD2-LEDGER16-5): E447 E471 E474 only ----
S('E447', h=[("will start down at [daylight?] tomorrow; E. R. Cole, Commander;", "will start down at early daylight tomorrow; E. R. Colhoun, Commander of the Saugus;"),
             ("(FM-F1, filed from FM-S1; row 5827/0)", "(FM-F1, filed from FM-S1; row 5827/0; image-read by FV-L16e, matches the transcription; antecedent E185 (holder 5824, Porter's order to Colhoun); context ORN I/11 p.194, the Saugus aground on the way down, afloat 14 Dec)")],
  d=['plain-at: cole#1', 'plain-at: hound#1'],
  n=N('AUDIT FV-L16e s.5, AUD2-LEDGER16-5 s.3/s.5', "'Cole hound' = Colhoun (plain name, holder 5824 'E. are Colhoun'; ORN I/11 'Edmd. R. Colhoun, Commander'), read plain; the signature's M is dropped; 'polkaer' = Command-er (H). 'early delight' = early daylight (plain-phonetic). H 11 of 11 stands (second audit)."))
S('E471', h=[("(FM-S3; row 5577/0; transcription only)", "(FM-S3; row 5577/0; image-read by FV-L16e, matches the transcription; the first No. 1 entry on the ledger (entries before it read with No. 9; AUD2-LEDGER16-5); context OR I/33 p.197, Butler's 8 p.m. telegram, = unfiled row 5577/1)")],
  n=N('AUDIT FV-L16e s.5, AUD2-LEDGER16-5 s.3/s.5', "no decoder change (H 8 of 8). Header only: image-read; the entry is the first No. 1 reading on the ledger (a statement about the ledger's order, not about novelty); context OR I/33 p.197 and the unfiled row 5577/1."))
S('E474', h=[("13 Dec 1864 City Point,", "13 Dec 1864 12 M City Point,"),
             ("(FM-S3; row 5829/1; transcription only)", "(FM-S3; row 5829/1; image-read by FV-L16e and AUD2-LEDGER16-5, matches the transcription; 'Frances' = Francis = 12 (TIME page), E200 precedent; H 6 + I 1 of 7)")],
  d=['plain-at: webster#1', 'variant: frances=Francis:I'],
  n=N('AUDIT FV-L16e s.5, AUD2-LEDGER16-5 s.3/s.5', "'webster' is the addressee's plain name (Col. R. C. Webster, chief quartermaster), not [Signature]; 'Frances fever' = {time: 12 M} [13] ('Frances' = Francis, the TIME-page word, as E200; applied as an entry-level variant, key.md untouched), replacing '[New York]'s [13]' and the two M. 'arsey' = R. C. (plain-phonetic). The E474 step-0 note's 'No. 1 H8' and 'first clause M' are superseded. H 6 + I 1 of 7."))
base.E = E
if __name__ == '__main__': base.run('ciphertext.txt')
