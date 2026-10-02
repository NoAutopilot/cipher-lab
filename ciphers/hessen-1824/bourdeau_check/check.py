"""Re-apply D. Bourdeau's stated key and method for HStAM 9 a Nr. 259 f. 249 (HCPortal 513) to OUR transcription.

Method and key from github.com/dbourdeau/cyphersolver targets/hesse1824/decrypt.py (MIT; HEAD 34e0fc8, read 2 Oct 2026),
re-implemented here, not copied: Vigenere table without j, key 'bcdefg' written continuously over every sign
(letters and the digit signs), key b..g = +2..+7, cipher columns run on past z into 1 2 3 4 ...; word dots take no key
letter. His one key-phase slip (a sign omitted in 'zsskkw' -> 'zsspkkw') is applied to both transcriptions, since it is
part of his method; his eleven letter-level copy-slip corrections are NOT applied (we measure the text as written).

  ours.txt           our blind transcription (NOTES.md 'Image and transcription', 26 Sept 2026), grade M
  bourdeau_ct.txt    his ct.txt, verbatim
  bourdeau_words.txt his per-cipher-word reading with slips corrected (reading.txt), one word per cipher word

Prints the sign diff between the two transcriptions and the per-word agreement of each decrypt with his reading.
--check exits non-zero if the committed result.txt is stale (rule 7).
"""
import difflib, re, sys, os
H = os.path.dirname(os.path.abspath(__file__))
C = 'abcdefghiklmnopqrstuvwxyz123456789'
P = 'abcdefghiklmnopqrstuvwxyz'
SHIFT = {k: 2 + i for i, k in enumerate('bcdefg')}

def words(path):
    t = open(os.path.join(H, path)).read().lower()
    t = t.replace('zsskkw', 'zsspkkw', 1)   # his single key-phase slip
    return re.findall(r'[a-z0-9]+', t)

def decrypt_stream(st):
    out = ''
    for k, ch in enumerate(st):
        if ch in C:
            i = C.index(ch) - SHIFT['bcdefg'[k % 6]]
            out += P[i] if 0 <= i < 25 else '?'
        else:
            out += '?'             # sign outside his alphabet (our 'j')
    return out

def per_word(o_st, b_st, ref):
    """Decrypt ours continuously, align its signs to his by difflib, and score his plaintext words."""
    do, db = decrypt_stream(o_st), decrypt_stream(b_st)
    sm = difflib.SequenceMatcher(None, o_st, b_st, autojunk=False)
    pos = {}                      # his position -> our decrypted letter
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal' or (tag == 'replace' and i2 - i1 == j2 - j1):   # a misread sign keeps its position
            for t in range(j2 - j1):
                pos[j1 + t] = do[i1 + t]
    k, ok, sig, bad = 0, 0, 0, []
    for w in ref:
        got = ''.join(pos.get(k + t, '_') for t in range(len(w)))
        sig += sum(g == c for g, c in zip(got, w))
        if got == w: ok += 1
        else: bad.append(f'{w}<-{got}')
        k += len(w)
    return ok, sig, bad, do

def run():
    o, b = words('ours.txt'), words('bourdeau_ct.txt')
    o_st, b_st = ''.join(o), ''.join(b)
    ref = open(os.path.join(H, 'bourdeau_words.txt')).read().split()
    assert sum(map(len, ref)) == len(b_st), (sum(map(len, ref)), len(b_st))
    L = [f'signs: ours {len(o_st)}, his {len(b_st)} (both after his one inserted sign, zss[p]kkw)']
    sm = difflib.SequenceMatcher(None, o_st, b_st, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag != 'equal':
            L.append(f'  transcription diff ({tag}): ours {o_st[i1:i2]!r} vs his {b_st[j1:j2]!r} at his sign {j1}')
    L.append(f'signs identical in both transcriptions: {sum(m.size for m in sm.get_matching_blocks())}/{len(b_st)}')
    n = sum(map(len, ref))
    for name, st in (('his ct.txt', b_st), ('ours (key phase continuous, as written)', o_st)):
        dec = decrypt_stream(st)
        # as written, with no alignment: the key phase runs straight on over our own signs
        k, ok, sig = 0, 0, 0
        for w in ref:
            got = dec[k:k + len(w)]; sig += sum(g == c for g, c in zip(got, w)); ok += got == w; k += len(w)
        L.append(f'{name}: plaintext words exact {ok}/{len(ref)}, letters {sig}/{n}')
    ok, sig, bad, _ = per_word(o_st, b_st, ref)
    L.append(f'ours, key phase continuous over OUR signs, scored on aligned positions: words {ok}/{len(ref)}, letters {sig}/{n}')
    L.append('  words that differ (his corrected word <- ours; _ = no aligned sign): ' + ' '.join(bad))
    o2 = o_st.replace('erylfe', 'erlylfe', 1)
    ok, sig, bad, _ = per_word(o2, b_st, ref)
    L.append(f'ours with the one dropped sign restored (erylfe -> erlylfe): words {ok}/{len(ref)}, letters {sig}/{n}')
    L.append('  words that differ: ' + ' '.join(bad))
    return '\n'.join(L) + '\n'

if __name__ == '__main__':
    r = run()
    p = os.path.join(H, 'result.txt')
    if '--check' in sys.argv:
        if open(p).read() != r:
            print('result.txt is stale'); sys.exit(1)
        print('result.txt current'); sys.exit(0)
    print(r, end='')
    open(p, 'w').write(r)
