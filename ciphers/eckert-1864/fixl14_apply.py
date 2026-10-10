#!/usr/bin/env python3
"""FIX-L14 (10 Oct 2026, account 1, for LANE LEDGER-14): apply s.3/s.5 of AUDIT (FV-L14a), (FV-L14b), (FV-L14c) to ciphertext.txt and
ciphertext-no2.txt as header edits, decoder directive lines, <del> marks on wrongly attached header fragments, one image-checked line fix
(E616) and a note: line (FIX-FM65 method; reading*.md only by decode*.py --write). Idempotent: skips a block that has a 'FIX-L14 (10 Oct 2026' note."""
import re, sys
def norm(w): return w.strip(" .,;:'\"()").lower()
MARK = 'FIX-L14 (10 Oct 2026'
E1, E2 = {}, {}
def S(file, e, h=(), d=(), l=(), dl=(), n=''):
    (E1 if file == 1 else E2)[e] = dict(h=list(h), d=list(d), l=list(l), dl=list(dl), n=n)
A, B, C = 'AUDIT FV-L14a s.3', 'AUDIT FV-L14b s.5', 'AUDIT FV-L14c s.5'
S(1, 'E600', h=[("Washington (11.30 AM)", "Washington (11 AM: the leaf header reads 'Sampson Balt. Wash Oct. 27 1864 11 am', FV-L14a)")],
  dl=['No 1  11.30 am'],
  n="FIX-L14 (10 Oct 2026, account 1, for LANE LEDGER-14; %s, FV-L14a N3 D2): header time 11 AM (leaf header 'Sampson Balt. Wash Oct. 27 1864 11 am', No. 1); the trailing line 'No 1  11.30 am' is the header of the next entry (9877/2, Glass at Nashville) which the extractor attached here, now struck <del>; it also fed the decoder's {time}. 'pontiac' = Command is on the leaf. 'leghorn' decoded Hurlbut, sense 'can be': M. Class N3, safe sentence: read with the period Cipher No. 1 key; no prior plaintext or decipherment located after the search logged in AUDIT.md (FV-L14a). Not 'first', not 'previously unread'." % A)
S(1, 'E601', h=[("signature word unread ('Nicarangua')", "signed C. C. Augur, Maj. Gen. Commanding Dept. of Washington ('Nicarangua', C by print)"),
                ("for [P. H. Sheridan, M]", "for Sheridan (C by print)"),
                ("Among the [prisoners] brought in", "Among the persons brought in"), ("Laughters [Gap]", "Snicker's Gap"),
                ("capable of [Bowling Green]ing arms", "capable of bearing arms"),
                ("than I can send;", "than I can send; I will do all I can, however;"),
                ("movement of the rebels in this direction;", "movement of the rebels in this direction; I trust he will not deceive me;"),
                ("(10.30 PM)", "(10.30 PM by the decoder: print 9 p.m., not visible on the leaf header, M)"),
                ("not located in print (L14-A; row 9826/0)", "in print, OR I/43 pt 1 p.909 (and Williamson, Mosby's Rangers, 1896; FV-L14a) (L14-A; row 9826/0)")],
  d=['plain: persons bearing', 'gloss: laughters=Snicker\'s:C'],
  n="FIX-L14 (10 Oct 2026; %s, FV-L14a N1 D3): sender C. C. Augur (print; 'Nicarangua' his signature, C), addressee Sheridan (C); 'persons' and 'bearing' plain on the leaf (the decoder's [5]s and [Bowling Green]ing are misfires); 'Laughters' is a code word, C by print = Snicker's (the decoder's Gap is the following word); the summary now carries 'I will do all I can, however' and 'I trust he will not deceive me' (both on the leaf and in the decode). The reading's 10.30 PM is not visible on the leaf header (M); print 9 p.m. Plaintext printed OR I/43 pt 1 p.909 (1893): our reading is an independent re-decipherment (N1)." % A)
S(1, 'E602', h=[("(10 AM; the clerk", "(10 AM, not visible on the leaf header, M; the clerk")],
  d=['plain: locust hunters'],
  n="FIX-L14 (10 Oct 2026; %s, FV-L14a N3 D2): 'Locust' plain on the leaf ('optic Locust Pt Depot'; the decoder's [Banks] is a key-row misfire) and 'Hunters' plain (decoder [Lee] misfire); the '10 AM' is not on the leaf header (M). Depth sentence (D2): on 7 July 1864 Washington told Capt. Thomas at Baltimore that Ricketts's division, about 8000 men without ambulances or wagons, would arrive by steamer, to be landed at Locust Point and forwarded to Harper's Ferry. Safe sentence: read with the period Cipher No. 1 key; no prior plaintext or decipherment located after the search logged in AUDIT.md (FV-L14a)." % A)
S(1, 'E603', h=[("for [the recipient code 'bobby', unread]", "for Sheridan, Comdg. Middle Military Division, Charlestown ('bobby', C by print)"),
                ("signed [Orgirldrillbore screw cut, a code signature, unread]", "signed C. A. Augur... see note: C. C. Augur, Major-General, Commanding ('Orgirldrillbore screw cut', C by print)"),
                ("Major [Tappan], 'fry' [unread]", "Major Fry ('Tappan' = Major; 'fry' the plain name)"),
                ("[Sazeel [unclear on the leaf]]", "Lazelle (plain name, clerk's spelling 'Sazeel')"),
                ("in [5, decoder reading, M] passed", "in person passed"),
                ("this [Gordonsville] last Monday last Monday", "this [Gordonsville] ('this' on the leaf, print 'through') last Monday"),
                ("'tankards' [unread]", "mountains ('tankards', C by print)"),
                ("not located in print (L14-A; row 9823/3)", "in print, OR I/43 pt 1 p.843 (FV-L14a) (L14-A; row 9823/3)")],
  d=['plain: person', 'gloss: tankards=mountains:C bobby=Sheridan:C'],
  n="FIX-L14 (10 Oct 2026; %s, FV-L14a N1 D3): addressee 'bobby' = Sheridan (C), signature 'Orgirldrillbore screw cut' = C. C. Augur, Major-General, Commanding (C); 'fry' plain (Major Fry; 'Tappan' = Major); 'Sazeel' = Lazelle (plain, clerk's spelling); 'person' plain on leaf 9824; 'last Monday' once (leaf 9824 has it once); 'tankards' = mountains (C). Leaf 'Muddy Branch whf', print 'Muddy Branch to-day': the leaf is kept. Plaintext printed OR I/43 pt 1 p.843 (1893): independent re-decipherment (N1)." % A)
S(1, 'E604', h=[("and Kent are ordered", "and Burbridge ('Kent', the code word, C by print; not the clerk's Kentucky) are ordered"),
                ("[Maj. Gen. Schofield] and Kent", "[Maj. Gen. Schofield] and Kent") if False else ("[we] will leave none", "you will leave none"),
                ("signed [General-in-Chief Halleck, M]", "signed H. W. Halleck, Major-General and Chief of Staff (print)"),
                ("not located in print (L14-A; row 9865/1)", "message 1 in print, OR I/39 pt 3 pp.251-252; message 2 not located (FV-L14a) (L14-A; row 9865/1)")],
  d=['gloss: kent=Burbridge:C'],
  n="FIX-L14 (10 Oct 2026; %s, FV-L14a msg 1 N1 D3, msg 2 N3 D1): 'Kent' is the code word for Burbridge (print 'Generals Schofield and Burbridge'), not the clerk's 'Kentucky'; '[we] will leave none' is 'you will leave none' (the ledger's 'Ewill'); signer H. W. Halleck, Major-General and Chief of Staff (the ledger's General-in-Chief is the key's value). Message 2 stands (not located, D1). Message 1 printed OR I/39 pt 3 pp.251-252 (1892): independent re-decipherment." % A)
S(1, 'E610', h=[("signed [Halleck]", "signed Halleck (print: Major-General and Chief of Staff)"),
                ("in print, OR I/37 pt 2, 11 July 1864 12.30 p.m., word for word", "in print, OR I/37 pt 2 p.210 (11 July 1864 12.30 p.m., word for word; FV-L14c)")],
  d=['merge: sir+come+stanzas', 'gloss: sircomestanzas=circumstances:C'],
  n="FIX-L14 (10 Oct 2026; %s, FV-L14c N1): header 'in print, OR I/37 pt 2 p.210' (page image head, IA warofrebellion372unit n216); 'Sir come stanzas' = circumstances (plain pun, C by print); signer as printed 'Major-General and Chief of Staff' (the decoder's [General-in-Chief] is the key's title)." % C)
S(1, 'E611', d=['plain-at: animals#1'],
  n="FIX-L14 (10 Oct 2026; %s): '[60000] [Monroe]'s' is '60,000 animals' (the clerk wrote 'Animals' in clear, M) 'will probably be supplied hereafter via [Monroe]'; leaf header 'Wash'n May 7th 1864 11 a.m.' confirmed. Next: OR ser. III vol. 4 by page (owner's IA loan or HathiTrust, a LOCAL-QUEUE row) and NARA RG 92 QMG letters-sent." % B)
S(1, 'E612', n="FIX-L14 (10 Oct 2026; %s): context added: Captain Ferry, Quartermaster of Transportation at Louisville (Louisville Daily Journal 5 and 7 Jan 1864); the leaf has no hour or operator ('Harriet' = the hour word)." % B)
S(1, 'E613', h=[("in print, Lincoln's telegram, IA letterstelegrams0008abra, below", "in print, Basler, Collected Works of Abraham Lincoln vol. 7 (1953), IA collectedworksof0007royp_l5c3 (be-api snippets), also letterstelegrams0008abra (FV-L14c)")],
  n="FIX-L14 (10 Oct 2026; %s): the print is Basler, Collected Works vol. 7 (1953), IA collectedworksof0007royp_l5c3 (be-api snippets), not only letterstelegrams0008abra; the addressee is Gov. Andrew Johnson, the decoder's [Johnston] is the key's spelling." % C)
S(1, 'E614', h=[("for Col. Brown and Maj. Van Vliet, Quartermaster Department, signed [Qr Master Genl U.S.]", "for Col. S. L. Brown, QM Dept., New York (same to Maj. Stewart Van Vliet), signed M. C. Meigs, Quartermaster-General"),
                ("in print, OR I/39, below", "in print, OR I/39 pt 3 p.395 (FV-L14c)")],
  d=['gloss: gassette=16th:C vernon=other_point:C', 'merge: tooth+list', 'gloss: toothlist=to_the_list:C'],
  n="FIX-L14 (10 Oct 2026; %s): header OR I/39 pt 3 p.395; addressee Col. S. L. Brown, QM Dept., New York (same to Maj. Stewart Van Vliet), signer M. C. Meigs; 'Gassette' = 16th (C, print), 'vernon' = other point, 'tooth list' = to the list." % C)
S(1, 'E615', h=[("for Maj. Gen. David Hunter, signed [Halleck]", "for Maj. Gen. David Hunter, Cumberland, Md., signed Halleck (print: Major-General and Chief of Staff)"),
                ("in print, OR I/37 pt 2, word for word", "in print, OR I/37 pt 2 p.123, word for word (FV-L14c)")],
  n="FIX-L14 (10 Oct 2026; %s): header OR I/37 pt 2 p.123, addressee Hunter at Cumberland, Md." % C)
S(1, 'E616', h=[("in print, OR I/37 pt 1, word for word", "in print, OR I/37 pt 1 p.525, word for word (FV-L14c)"),
                ("signed [Halleck]", "signed Halleck (print: Major-General and Chief of Staff)")],
  l=[("recon mend to", "recon mend them to")],
  n="FIX-L14 (10 Oct 2026; %s): header OR I/37 pt 1 p.525; ciphertext line 'any are worth less recon mend to' -> 'recon mend them to' (leaf 9743, image-checked by FV-L14c); 'Duffin' M (the leaf likely reads 'Duffie')." % C)
S(1, 'E617', h=[("4 March 1864 by the cipher date words (ledger header 'Mar 14th', unreconciled, M)", "14 March 1864 (ledger header 'Washn Mar 14th 1864' on the leaf and OR I/34 pt 2 p.606 agree; the day group's decode '4' is wrong)"),
                ("for [Curtis, Fort Leavenworth]", "for Gen. S. R. Curtis, Leavenworth City, Kans. (C by print)"),
                ("in print, OR I/34 pt 2, below", "in print, OR I/34 pt 2 p.606, word for word except 'received' (ledger, on the leaf) for the print's 'issued' (FV-L14c)")],
  d=['gloss: pension=14:C'],
  n="FIX-L14 (10 Oct 2026; %s): date 14 March 1864 10.30 AM (ledger header and OR I/34 pt 2 p.606 agree; the day group's decode '4' is wrong); addressee Gen. S. R. Curtis, Leavenworth City, Kans. (C, print); word for word except 'received' (ledger, on the leaf) for the print's 'issued'. Supersedes NOTES '## L14-B' 'word for word' for E617 and its open 'E617 date conflict'." % C)
S(1, 'E620', d=['plain: niagara john'],
  h=[("to [Maj. Gen. Dix] (M)", "to [Maj. Gen. Dix] (H, Kasson)"), ("signed [C. A. Dana] by the key (M)", "signed [C. A. Dana] (H; C via E142's print)"),
     ("I am confidentially informed that Beverly Tucker will cross at [Niagara] Falls", "I am confidentially informed that Beverly Tucker will cross at Niagara Falls (plain on the leaf)")],
  n="FIX-L14 (10 Oct 2026; %s): 'Niagara' plain on the leaf (the decoder's D. D. Porter is wrong) and 'John Odell' plain (the decoder's Grant is wrong); signature [C. A. Dana] H (image; C via E142's print) and addressee [Dix] H (Kasson). Context: sequel printed OR II/7 p.1132 (= E142), Baker 1867 testimony; sibling 9897/2 (10.15 PM, 'Who is John Odell ... Bunker's first name') unfiled." % B)
S(1, 'E621', dl=['" (Cal) "  6 P. m'],
  n="FIX-L14 (10 Oct 2026; %s): the transcription tail '\" (Cal) \" 6 P. m' is the next entry's header (Wright, San Francisco), not a service note of E621, now struck <del>. Context: OR I/43 pt 2 (Halleck-Stevenson 6 Oct, Halleck-Garrett 10 Oct p.336)." % B)
S(2, 'N2-SA', h=[("not located", "printed, OR I/41 pt 3 p.373 (page image, IA warofrebellion413unit n376), text C") ] if False else
  [("; 'No 1 9 AM' is a service note)", "; 'No 1 9 AM' is the next entry's header, Eddy, Atlanta, 27 Sept 9 a.m.)"),
   ("holder transcription, leaf not eye-checked)", "in print, OR I/41 pt 3 p.373 (page image, IA warofrebellion413unit n376), text C; FV-L14b)"),
   ("[Smith] full discretion", "A. J. Smith (C by print) full discretion")],
  d=['plain: rank smith'], dl=['No 1  9 AM'],
  n="FIX-L14 (10 Oct 2026; %s): header now 'printed, OR I/41 pt 3 p.373 (page image n376), text C'; 'rank' plain (decoder '[Has been sent]' wrong); 'Smith' after Fort plain (decoder '[100]' wrong); Nuptial = A. J. Smith, Madrid = Grant, Asp = Arkansas, Jargon = Kirby Smith, Knell = Price are C by print (key grades unchanged: the decode agrees); 'inefficiencies' = leaf 'inefficiences', print 'inefficiency'; the trailing 'No 1  9 AM' is the next entry's header (Eddy, Atlanta, 27 Sept 9 a.m.), struck <del>; '#2' over Kimber on the leaf." % B)

def run(F, E):
    L = open(F, encoding='utf-8').read().split('\n'); i = 0; done = []
    while i < len(L):
        m = re.match(r'### (\S+) ', L[i])
        if m and m.group(1) in E:
            e = m.group(1); s = E[e]; j = i + 1
            while j < len(L) and not L[j].startswith('### '): j += 1
            blk = L[i:j]
            if any(l.startswith('note: ' + MARK) for l in blk): i = j; continue
            for old, new in s['h']:
                if old not in blk[0]: print('HEADER MISS', e, old[:60]); continue
                blk[0] = blk[0].replace(old, new, 1)
            k = next(x for x, l in enumerate(blk) if l.startswith('note:'))
            for old, new in s['l']:
                hit = [x for x in range(1, k) if old in blk[x]]
                if not hit: print('LINE MISS', e, old)
                else: blk[hit[0]] = blk[hit[0]].replace(old, new, 1)
            for t in s['dl']:
                hit = [x for x in range(1, k) if blk[x].strip() == t.strip()]
                if not hit: print('DEL MISS', e, t)
                else: blk[hit[-1]] = '<del>' + blk[hit[-1]] + '</del>'
            blk[k:k] = s['d']
            end = max(x for x, l in enumerate(blk) if l.strip())
            blk.insert(end + 1, 'note: ' + s['n'])
            L[i:j] = blk; done.append(e); i += len(blk)
        else: i += 1
    open(F, 'w', encoding='utf-8').write('\n'.join(L))
    print(F, done)
run('ciphertext.txt', E1); run('ciphertext-no2.txt', E2)
