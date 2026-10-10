#!/usr/bin/env python3
"""FIX-AUD2-L14 (10 Oct 2026, owner account): apply AUDIT 2 (AUD2-LEDGER14-1) s.2/s.5 and AUDIT 2 (AUD2-LEDGER14-2) s.4/s.5 to ciphertext.txt
(E600, E602, E611, E612, E620) as header edits, decoder directive lines (added or removed) and a note: line, and to the readers' NOTES.md verdict
cells. Same method as fixl14_apply.py (reading*.md only by decode.py --write). Idempotent: skips a block that already has a 'FIX-AUD2-L14' note."""
MARK = 'FIX-AUD2-L14 (10 Oct 2026'
A, B = 'AUDIT 2 AUD2-LEDGER14-1 s.2/s.5', 'AUDIT 2 AUD2-LEDGER14-2 s.4/s.5'
E = {}
def S(e, h=(), d=(), rm=(), n=''): E[e] = dict(h=list(h), d=list(d), rm=list(rm), n=n)
S('E600', h=[("Washington (11 AM: the leaf header reads 'Sampson Balt. Wash Oct. 27 1864 11 am', FV-L14a)",
              "Washington (11 AM (header: 'Sampson Balt. Wash Oct. 27 1864 11 am'); time word 'florence' 11.30 AM (H), the ledger's half-hour offset, AUD2-LEDGER14-1)"),
             ("for [Maj. Gen. Lew Wallace at Baltimore, M], signed [Secretary of War, M]",
              "for Maj. Gen. Lew Wallace at Baltimore ('Submit', C), signed Secretary of War ('Infant', H)"),
             ("not located in print (L14-A; row 9877/1)",
              "substance in print: Stahr, Stanton (2017), note 'Stanton to Wallace, Oct. 26, 1864, M473 (furlough Delaware cavalry)'; Wallace's reply OR I/43 pt 2 p.484; wording not located (AUD2-LEDGER14-1) (L14-A; row 9877/1)")],
  d=['variant: leghorn=Leghorn:M'], rm=['gloss: florence=11_AM:M'],
  n="FIX-AUD2-L14 (10 Oct 2026, owner account; %s, N2 D3): the time word 'florence' reads 11.30 AM by its key row (H); the leaf header says 11 am and the next entry on the leaf (Glass, Nashville: header 11.30 am, time word 'francis' = 12) shows the same half-hour offset, a ledger convention, not a slip; FIX-L14's gloss to 11 AM is removed and the header gives both; 'leghorn' (key row Hurlbut, sense 'can be') graded M by a variant line. Addressee 'Submit' = Wallace (C, key row and E168), signer 'Infant' = Secretary of War (H). Substance in print (Stahr 2017, M473 note dated 26 Oct; the ledger leaf reads 27 Oct, unsettled); Wallace's reply of 28 Oct, OR I/43 pt 2 p.484. Supersedes FIX-L14's 'Class N3' and safe sentence: safe now 'read with the period Cipher No. 1 key; the substance is known (Stahr 2017, citing NARA M473; Wallace's reply OR I/43 pt 2 p.484); its wording was not located in print'." % A)
S('E602', h=[("signed [bender, unread]", "signed Quartermaster General U.S. = M. C. Meigs ('bender', H)"),
             ("'Endless' [unread]", "Sigel ('Endless', H, E168's key supplement)")],
  d=['gloss: endless=Maj._Gen._Franz_Sigel:H', 'unjoin: bender', 'variant: bender--=Bender:H'],
  n="FIX-AUD2-L14 (10 Oct 2026, owner account; %s, N3 D2 kept): signer 'bender' = Qr Master Genl U.S. (key.md p.10 l.24, H), i.e. M. C. Meigs, his own order to his Baltimore quartermaster; 'Endless' = Maj. Gen. Franz Sigel (H; the E168 key supplement adds Orphan/Endless for Sigel and has no key.md row, hence the gloss), fitting Sigel's withdrawal from Martinsburg, 3-6 July. 'francis' after 'Banditti above' stays unread. Not located in print after FV-L14a and AUD2-LEDGER14-1 (Grant Papers vol. 11 searched). Directives: 'unjoin: bender' and 'variant: bender--=Bender:H' (the trailing dashes had glued to the signature word, which the decoder left unread)." % A)
S('E611', n="FIX-AUD2-L14 (10 Oct 2026, owner account; %s, N3 D2 kept): context, not a copy: holder pointer 9699 (p.33, 8-9 Apr 1864, Horner N.Y., Meigs to S. L. Brown: 'Send forty thousand bushels of grain and seven hundred tons of hay ... Confidential signed Meigs'), same office, operator and addressee a month earlier." % B)
S('E612', h=[("signed [Qr Master Genl U.S.] (M, the signature groups read 'M see Me Eggs')",
              "signed M. C. Meigs, Quartermaster-General ('M see Me Eggs', a phonetic split, I; 'Bender' = Qr Master Genl U.S., H)"),
             ("(row 9883/0; L14-B; not located in sources searched by date, below)",
              "(row 9883/0; L14-B; not located in sources searched by date, below; context: S.O. No. 309, AGO, 17 Sept 1864, relieving Captain J. H. Ferry at Louisville and sending him to Memphis; Mereness Calendar lead unread, AUD2-LEDGER14-2)")],
  d=['merge: m+see+me+eggs', 'gloss: mseemeeggs=M._C._Meigs:I'],
  n="FIX-AUD2-L14 (10 Oct 2026, owner account; %s, N3 D3): the signature span 'M see Me Eggs' is a phonetic split of 'M. C. Meigs' (the ledger's device, key.md s.1), read I, agreeing with 'Bender' = Qr Master Genl U.S. (H). Context: Special Orders No. 309, AGO, 17 Sept 1864, relieving Captain J. H. Ferry as Chief Quartermaster of Depot at Louisville and sending him to Memphis (Army and Navy Official Gazette, snippet); QMG report 'John H. Ferry, until October, 1864' at Louisville; Blair, With Malice Toward Some (2014), note citing Ferry to McClellan, Louisville, 3 Oct 1864. Open lead: the Mereness Calendar (1971) entry 'E. M. Stanton to Robert Allen, Louisville ... Ferry', unread (if it calendars this order, E612 moves to N2)." % B)
S('E620', h=[("(L14-C; row 9897/1; holder transcription, leaf not eye-checked)",
              "(L14-C; row 9897/1; holder transcription, leaf not eye-checked; N1 D1, AUD2-LEDGER14-2: the body is in clear in the holder's public transcription, the key adds only the hour, date, addressee and signer)")],
  n="FIX-AUD2-L14 (10 Oct 2026, owner account; %s, N1 D1): no body code word (Rebecca, Ghost, Kasson, Image, Webster, Sugar and the stops are time, date, address, signature and punctuation; Niagara and John Odell are clear on the leaf), so the body is known from the Huntington's public transcription of pointer 9897 and the class is N1 (the D2V-E74 line); no code clause, D1. Supersedes FIX-L14's and FV-L14b's N3 D3. Safe sentence: 'Dana's 15 Nov 1864 10 PM telegram to Dix on Beverly Tucker's expected crossing at Niagara Falls is in clear in the Huntington's public transcription of the ledger (mssEC 18 p.231); the period key adds only the hour, Dix as addressee and Dana as signer. The next day's arrest order is printed in OR ser. II vol. 7 p.1132.'" % B)

NOTES = [  # (unique old substring, new) in the readers' verdict cells
 ("[Superseded 10 Oct 2026, FIX-L14 / FV-L14a: N3 D2, header time 11 AM; 'not located' stands, a search result, not a novelty verdict.]",
  "[Superseded 10 Oct 2026, FIX-L14 / FV-L14a: N3 D2, header time 11 AM; 'not located' stands, a search result, not a novelty verdict.] [Superseded 10 Oct 2026, FIX-AUD2-L14 / AUD2-LEDGER14-1: N2 D3 -- substance in print (Stahr 2017, M473 note; Wallace's reply OR I/43 pt 2 p.484), wording not located; header 11 AM, time word 11.30 AM (H).]"),
 ("[Superseded 10 Oct 2026, FIX-L14 / FV-L14a: N3 D2; 'not located' stands as a search result.]",
  "[Superseded 10 Oct 2026, FIX-L14 / FV-L14a: N3 D2; 'not located' stands as a search result.] [AUD2-LEDGER14-1: N3 D2 kept; signer 'bender' = M. C. Meigs (H), 'Endless' = Sigel (H); FIX-AUD2-L14.]"),
 ("**not located** [FV-L14b: N3 D2; 'not located' stands.]",
  "**not located** [FV-L14b: N3 D2; 'not located' stands.] [AUD2-LEDGER14-2: N3 D3; signed M. C. Meigs ('M see Me Eggs', I); Mereness Calendar lead open; FIX-AUD2-L14.]"),
 ("**filed E620** [FV-L14b: N3 D3.]",
  "**filed E620** [FV-L14b: N3 D3.] [Superseded 10 Oct 2026, AUD2-LEDGER14-2: N1 D1 -- body in clear in the holder transcription; FIX-AUD2-L14.]"),
]

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
                if old not in blk[0]: print('HEADER MISS', e, old[:60]); continue
                blk[0] = blk[0].replace(old, new, 1)
            for t in s['rm']:
                if t in blk: blk.remove(t)
                else: print('RM MISS', e, t)
            k = next(x for x, l in enumerate(blk) if l.startswith('note:'))
            blk[k:k] = s['d']
            end = max(x for x, l in enumerate(blk) if l.strip())
            blk.insert(end + 1, 'note: ' + s['n'])
            L[i:j] = blk; done.append(e); i += len(blk)
        else: i += 1
    open(F, 'w', encoding='utf-8').write('\n'.join(L)); print(F, done)

def notes(F):
    t = open(F, encoding='utf-8').read(); n = 0
    for old, new in NOTES:
        if new in t: continue
        if t.count(old) != 1: print('NOTES MISS/AMBIG', t.count(old), old[:60]); continue
        t = t.replace(old, new, 1); n += 1
    open(F, 'w', encoding='utf-8').write(t); print(F, n, 'cells')

run('ciphertext.txt'); notes('NOTES.md')
