#!/usr/bin/env python3
"""N5-VIVK: merge the two blind passes of each decipherment page and write the normalized plaintext stream.

    python3 ciphers/fr16104-vivonne-spain-1572/tx/merge_dec.py f106r f106v f107r f107v f108r f108v

Per line, words of pass A and pass B are aligned (difflib); equal runs are kept; at a split the side with fewer doubt
marks ('<?>', trailing '?') wins, ties to pass A; a word only one pass wrote is kept. Writes tx/dec_<page>_merged.txt
(as written, with the merge's choices) and tx/dec_norm.txt (all pages in order; PREREG normalization: lowercase,
accents stripped, letters a-z only, u/v -> u, i/j -> i, bracketed expansions kept, {del:...} dropped, {add:...} kept,
'<?>' dropped). Prints per page word counts and the A/B word agreement (err_2reader at word level).
"""
import difflib, os, re, sys, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))


def doubt(ws):
    return sum(w.count('<?>') + w.endswith('?') for w in ws)


def norm(text):
    text = re.sub(r'\{del:[^}]*\}', ' ', text)
    text = re.sub(r'\{add:([^}]*)\}', r' \1 ', text)
    text = text.replace('<?>', ' ')
    text = unicodedata.normalize('NFD', text.lower())
    text = ''.join(c for c in text if 'a' <= c <= 'z')
    return text.replace('j', 'i').replace('v', 'u')


def main():
    allnorm = []
    for page in sys.argv[1:]:
        A = open(os.path.join(HERE, f'dec_{page}_passA.txt'), encoding='utf-8').read().splitlines()
        B = open(os.path.join(HERE, f'dec_{page}_passB.txt'), encoding='utf-8').read().splitlines()
        A = [l for l in A if l.strip()]; B = [l for l in B if l.strip()]
        # align lines too (a pass may split or skip a line): align on the flat word streams
        wa = ' \n '.join(A).split(' '); wb = ' \n '.join(B).split(' ')
        wa = [w for w in wa if w]; wb = [w for w in wb if w]
        key = lambda w: norm(w)
        sm = difflib.SequenceMatcher(None, [key(w) for w in wa], [key(w) for w in wb], autojunk=False)
        out, eq = [], 0
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == 'equal':
                out += wa[i1:i2]; eq += i2 - i1
            elif op == 'replace':
                out += wa[i1:i2] if doubt(wa[i1:i2]) <= doubt(wb[j1:j2]) else wb[j1:j2]
            elif op == 'delete':
                out += wa[i1:i2]
            else:
                out += wb[j1:j2]
        merged = ' '.join(out).replace(' \n ', '\n').replace('\n ', '\n')
        open(os.path.join(HERE, f'dec_{page}_merged.txt'), 'w', encoding='utf-8').write(merged + '\n')
        na = len([w for w in wa if w != '\n']); nb = len([w for w in wb if w != '\n'])
        eqw = sum(1 for op, i1, i2, j1, j2 in sm.get_opcodes() if op == 'equal' for w in wa[i1:i2] if w != '\n')
        n = norm(merged)
        allnorm.append(n)
        print(f'{page}: words A {na} B {nb}, agreeing words {eqw} ({eqw / max(na, nb):.3f}), merged letters {len(n)}')
    open(os.path.join(HERE, 'dec_norm.txt'), 'w').write(''.join(allnorm) + '\n')


if __name__ == '__main__':
    main()
