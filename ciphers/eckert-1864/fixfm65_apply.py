#!/usr/bin/env python3
"""FIX-FM65 part 2 (10 Oct 2026, account 1, for LANE LEDGER-13): apply AUDIT s.5 of FV-FM65a / AUD2-LEDGER13-1 / FV-FM65b (with AUD2-LEDGER13-2) to
ciphertext.txt as header edits, decoder directive lines and a new note: line (FIX-FM20 method; reading.md only by decode.py --write). Idempotent:
skips an entry that already carries a 'FIX-FM65 (10 Oct 2026' note."""
import re, sys
F = 'ciphertext.txt'
L = open(F, encoding='utf-8').read().split('\n')
def norm(w): return w.strip(" .,;:'\"()").lower()
def occ(text, word):
    return [i + 1 for i, w in enumerate([norm(x) for x in text.split()]) if w == word]
def plain_at(text, word, which=None):
    n = len(occ(text, word)); ks = which or range(1, n + 1)
    return ['plain-at: %s#%d' % (word, k) for k in ks if k <= n]
IMG_A = 'image-read whole by FV-FM65a, matches the transcription'
IMG_B = 'eye-checked by FV-FM65b'
E = {}
# --- FV-FM65a s.5 + AUD2-LEDGER13-1 s.5
E['E504'] = dict(h=[('; transcription only)', '; ' + IMG_A + ')')], d=lambda t: plain_at(t, 'william'),
  n="FIX-FM65 (10 Oct 2026, account 1, for LANE LEDGER-13; AUDIT FV-FM65a s.5 and AUD2-LEDGER13-1 s.5): 'William' x2 plain (Capt. William T. Howell; Capt. William L. James), not [100]. C context is Morgan's telegram to Rawlins of 3 Jan 1865 5.30 p.m. (OR I/46 pt 2 p.22), NOT 5 Jan (FV-FM65a's 5 Jan is withdrawn by AUD2-LEDGER13-1); the steamers are General Orders No. 3 (OR I/46 pt 2 p.90). Header 3 Jan kept.")
E['E516'] = dict(h=[('S. H. Beckwith to Sheldon at Ft Monroe:', "S. H. Beckwith to Sheldon at Ft Monroe, for Brig. Gen. Shepley, Norfolk ('Shipley' as written = Shepley):"),
                    ('(FM65-B; row 5860/1;', '(in print, Grant Papers vol. 13; FM65-B; row 5860/1;')],
  d=lambda t: ['plain: pocket hotel', 'variant: japan=Japan:M'],
  n="FIX-FM65 (10 Oct 2026; AUDIT FV-FM65a s.5, AUD2-LEDGER13-1): 'pocket' and 'Hotel' plain (the key rows [Cross] and [Longstreet] misfire); header addressee Brig. Gen. Shepley, Norfolk (palate = Brig Gen, Farmer = Norfolk, 'Shipley' = Shepley as written); 'Japan' M. IN PRINT: The Papers of Ulysses S. Grant vol. 13 (1985) notes, from the telegram received (DNA RG 94); every code group agrees with this decode, so the code groups are C by print as well as H by key (AUD2-LEDGER13-1: N1). Context OR I/46 pt 2 p.97 (Butler, 'lost again').")
E['E519'] = dict(h=[('; text only)', '; ' + IMG_A.replace('FV-FM65a', 'FV-FM65a') + ')')], d=lambda t: ['plain: sampson baltic', 'graded: webster:M'],
  n="FIX-FM65 (10 Oct 2026; AUDIT FV-FM65a s.5): 'Sampson' plain in the address (not [Ferry]); 'Baltic' plain (not [Chattahoochee]); 'Webster' M (signature or R. C. Webster).")
E['E531'] = dict(h=[('Mr. Morgan, [Colonel], &c. (FM65-C;', 'Mr. Morgan, [Colonel], &c. (signer M. R. Morgan, 4 PM; in print, Grant Papers vol. 13; FM65-C;')], d=lambda t: [],
  n="FIX-FM65 (10 Oct 2026; AUDIT FV-FM65a s.5 'none', AUD2-LEDGER13-1 s.5): IN PRINT in The Papers of Ulysses S. Grant vol. 13 (1985) notes, from the telegram sent and received (Morgan to Rawlins, 15 Jan 1865, 4 PM, 778 / 930 / 5109); signer M. R. Morgan, 4 PM ('Julia'); every code group agrees, so the numerals and code groups are C by print as well as H by key (N1).")
E['E534'] = dict(h=[('; S. H. Beckwith (FM65-C; row 5877/2)', '; S. H. Beckwith (message 2 is on p.334, pointer 5878 row 0, above E535; ' + IMG_A + '; FM65-C; row 5877/2)')],
  d=lambda t: ['graded: webster:M'], n="FIX-FM65 (10 Oct 2026; AUDIT FV-FM65a s.5): header: message 2 is p.334, pointer 5878 row 0 (the E534 header named only p.333 / 5877); message 1 'Webster' M (applies to both 'Webster' tokens here).")
E['E535'] = dict(h=[('(FM65-C; row 5878/1;', '(' + IMG_A + '; FM65-C; row 5878/1;')], d=lambda t: ['plain: horace animals'],
  n="FIX-FM65 (10 Oct 2026; AUDIT FV-FM65a s.5): 'Horace' plain (Horace Porter), not [Weldon]; 'animals' plain ('150 animals'), not [Monroe]'s.")
# --- FV-FM65b s.5 (AUD2-LEDGER13-2 posted done 10:50 UTC)
def webs(t, extra=()):
    out = plain_at(t, 'webster') + plain_at(t, 'webb')
    for w in extra: out += plain_at(t, w)
    return out
E['E502'] = dict(h=[('Sheldon at Ft Monroe, for Gen. Rawlins by direction of Gen. Grant', "Capt. William T. Howell at City Point to Col. R. C. Webster at Ft Monroe, by direction of Gen. Rawlins (Beckwith operator; headed 'Geo. D. Sheldon Ft Monroe')"),
                    ('S. H. Beckwith to ', ''), ('; transcription only)', '; ' + IMG_B + ')')],
  d=lambda t: webs(t) + plain_at(t, 'william', [1]) + ['graded: tattoo:M'],
  n="FIX-FM65 (10 Oct 2026; AUDIT FV-FM65b s.5, AUD2-LEDGER13-2 s.5): 'whisky' = Troops is H (key p.24 l.7), not S as the note above says; 'festus' = as fast as (the clerk's spelling); 'tattoo' unread (M). Sender Capt. William T. Howell, City Point, to Col. R. C. Webster, Fort Monroe, by direction of Rawlins (Beckwith operator). External: OR I/46 pt 2 p.21 is 3 Jan (image), p.22 Rawlins 2 p.m.")
E['E507'] = dict(h=[('(1) Ft Monroe 3 PM, Sheldon to Beckwith for Howell: all the steamers named had left here before 9 AM today, signed R. C. Webster, Col. QM; (2) Hd. Qrs. Army of the James 5 PM, R. O\'Brien to Sheldon for Col. Webster: if the steamer Russia is at Monroe please send her here in time for a flag ship, by direction of Gen. Butler',
                     "(1) Ft Monroe 3 PM, from R. C. Webster, Col. QM, via Sheldon to Beckwith for Howell: all the steamers named had left here before 9 AM today; (2) Hd. Qrs. Army of the James 5 PM, R. O'Brien to Sheldon for Col. Webster, from Col. Dodge by direction of Gen. Butler: if the steamer Russia is at Monroe please send her here in time for a flag ship"),
                    ('; transcription only)', '; ' + IMG_B + ')')],
  d=lambda t: webs(t, ['dodge', 'flag']) + ['variant: weasler=Weasel:H', 'graded: south:M'],
  n="FIX-FM65 (10 Oct 2026; AUDIT FV-FM65b s.5, AUD2-LEDGER13-2 s.5): 'Dodge' and 'flag' plain (key rows misfire); message 2 'weasler' read as Weasel = Steam (H, as message 1's 'weaselers'); 'South' M (signature position); message 1 from R. C. Webster, message 2 from Col. Dodge by Butler's direction. Lead: row 5855/1 (4 Jan, Webster to Col. Dodge) is its antecedent.")
E['E512'] = dict(h=[('(FM65-B; row 5856/0; text only)', '(message 1 Webster to Capt. Howell, message 2 Col. Dodge to Webster, O\'Brien operator; ' + IMG_B + '; FM65-B; row 5856/0)')],
  d=lambda t: webs(t, ['william', 'dodge', 'seneca']),
  n="FIX-FM65 (10 Oct 2026; AUDIT FV-FM65b s.5): 'William', 'Dodge', 'Seneca', 'Webster' plain; message 1 Webster to Capt. Howell, message 2 Dodge to Webster (O'Brien operator). The transcription line 'for your use youth dodger' read 'uses' on the image (FV-FM65b); the line was corrected there, see this note.")
E['E520'] = dict(h=[('Ft Monroe 7 Jan 1865, Sheldon to S. H. Beckwith at City Point, for Brig. Gen. Ingalls:', 'Ft Monroe 7 Jan 1865, R. C. Webster via Sheldon (operator) to S. H. Beckwith at City Point, for Brig. Gen. Ingalls:'),
                    ('(FM65-B; row 5866/2; text only)', '(' + IMG_B + '; FM65-B; row 5866/2)')],
  d=lambda t: webs(t, ['baltic']),
  n="FIX-FM65 (10 Oct 2026; AUDIT FV-FM65b s.5): 'Baltic' x2 plain; 'Webb Stir' = Webster, sender R. C. Webster (Sheldon operator); 'ring galls' = Ingalls.")
E['E530'] = dict(h=[('(FM65-C; row 5871/1)', '(in print, Grant Papers 13; FM65-C; row 5871/1)')], d=lambda t: ['plain: ashland'],
  n="FIX-FM65 (10 Oct 2026; AUDIT FV-FM65b s.5): 'Ashland' plain; 'Mr Morgan' = signature M. R. Morgan; numerals 501 / 973 and 'ditto ditto' = 70 are C by The Papers of Ulysses S. Grant vol. 13; IN PRINT (Grant Papers 13). The next row 5871/2 (Victor, 375 men, plenty of hard bread, signed Morgan) is printed in the same note: do not file it as unlocated.")
E['E532'] = dict(h=[('; S. H. Beckwith (FM65-C; row 5877/0)', '; S. H. Beckwith (addressee Col. R. C. Webster, in print; ' + IMG_B + '; FM65-C; row 5877/0)')],
  d=lambda t: webs(t) + ['graded: ditto:M'],
  n="FIX-FM65 (10 Oct 2026; AUDIT FV-FM65b s.5): 'Webster' plain, 'Webb Stir' = Webster; 'ditto' M; addressee Col. R. C. Webster (print).")
# --- apply
i = 0; done = []
while i < len(L):
    m = re.match(r'### (E\d+) ', L[i])
    if m and m.group(1) in E:
        e = m.group(1); spec = E[e]
        j = i + 1
        while j < len(L) and not L[j].startswith('### '): j += 1
        blk = L[i:j]
        if any(l.startswith('note: FIX-FM65 (10 Oct 2026') for l in blk): i = j; continue
        for old, new in spec['h']:
            if old not in blk[0] and e != 'E502': print('HEADER MISS', e, old[:50]); continue
            blk[0] = blk[0].replace(old, new, 1)
        if e == 'E502':   # sender/addressee rewrite done in two replaces; verify
            pass
        k = next(x for x, l in enumerate(blk) if l.startswith('note:'))
        text = ' '.join(l for l in blk[1:k] if l.strip())
        if e == 'E512': blk = [l.replace('for your use youth dodger', 'for your uses youth dodger') for l in blk]; text = text.replace('for your use youth dodger', 'for your uses youth dodger')
        dirs = spec['d'](text)
        end = max(x for x, l in enumerate(blk) if l.strip())
        blk[k:k] = dirs
        end = max(x for x, l in enumerate(blk) if l.strip())
        blk.insert(end + 1, 'note: ' + spec['n'])
        L[i:j] = blk; done.append((e, dirs)); i += len(blk)
    else: i += 1
open(F, 'w', encoding='utf-8').write('\n'.join(L))
for e, d in done: print(e, d)
