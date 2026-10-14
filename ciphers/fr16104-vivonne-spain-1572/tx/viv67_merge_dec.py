#!/usr/bin/env python3
"""VIV-67: merge the two blind passes of each ink-68 decipherment page with tx/merge_dec.py's rules (imported, unchanged)
and write tx/dec67_norm.txt (ink 41's tx/dec_norm.txt is left untouched).

    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv67_merge_dec.py f205r f205v
"""
import difflib, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import merge_dec as md  # noqa: E402


def main():
    allnorm = []
    for page in sys.argv[1:]:
        rl = lambda q: [l for l in open(os.path.join(HERE, f'dec_{page}_{q}.txt'), encoding='utf-8').read().splitlines() if l.strip()]
        wa = [w for w in ' \n '.join(rl('passA')).split(' ') if w]
        wb = [w for w in ' \n '.join(rl('passB')).split(' ') if w]
        sm = difflib.SequenceMatcher(None, [md.norm(w) for w in wa], [md.norm(w) for w in wb], autojunk=False)
        out = []
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            if op == 'equal':
                out += wa[i1:i2]
            elif op == 'replace':
                out += wa[i1:i2] if md.doubt(wa[i1:i2]) <= md.doubt(wb[j1:j2]) else wb[j1:j2]
            elif op == 'delete':
                out += wa[i1:i2]
            else:
                out += wb[j1:j2]
        merged = ' '.join(out).replace(' \n ', '\n').replace('\n ', '\n')
        open(os.path.join(HERE, f'dec_{page}_merged.txt'), 'w', encoding='utf-8').write(merged + '\n')
        na = len([w for w in wa if w != '\n']); nb = len([w for w in wb if w != '\n'])
        eqw = sum(1 for op, i1, i2, j1, j2 in sm.get_opcodes() if op == 'equal' for w in wa[i1:i2] if w != '\n')
        n = md.norm(merged)
        allnorm.append(n)
        print(f'{page}: words A {na} B {nb}, agreeing words {eqw} ({eqw / max(na, nb):.3f}), merged letters {len(n)}')
    open(os.path.join(HERE, 'dec67_norm.txt'), 'w').write(''.join(allnorm) + '\n')


if __name__ == '__main__':
    main()
