#!/usr/bin/env python3
"""SFZ-LOOK2 (11 Oct 2026): pass E = pass D with the 7 labels the look-alike re-read settled (2-of-3 rule,
tools/lookalike_pass.py reconcile on lookalike/look2/; PREREG-SFZ-LOOK2.md). Positions are build.py's normalised positions
(`g ÷` counted as one sign g÷); every other token is copied from pass D unchanged.
  python3 ciphers/sforza-pusterla-1447-f13/lookalike/look2/make_passE.py [--check]   (--check: exit 1 if the file is stale)
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); TGT = os.path.dirname(os.path.dirname(HERE))
CHANGES = {('f13_L01', 4): ('a', 'ze'), ('f13_L02', 18): ('go', 'So'), ('f13_L02', 28): ('a', 'ze'), ('f13_L04', 8): ('h-', 'h'),
           ('f13_L05', 25): ('h-', 'h'), ('f13_L07', 16): ('8', 'g'), ('f13_L09', 26): ('a', 'ze')}


def build():
    out = ['# pass E (SFZ-LOOK2, 11 Oct 2026): pass D with the second look-alike pass applied (lookalike/look2/, So/go 8/g h/h- a/ze,',
           '# 2-of-3 rule against pass A): 7 labels changed (3 a->ze, 1 go->So, 2 h-->h, 1 8->g); every other token exactly as pass D.']
    done = set()
    for l in open(os.path.join(TGT, 'ciphertext_f13_passD.tsv')):
        if l.startswith('#') or '\t' not in l:
            continue
        ln, s = l.rstrip('\n').split('\t', 1)
        raw, toks, i, pos = s.split(), [], 0, 0
        while i < len(raw):
            t = raw[i]; pos += 1
            if t.rstrip('?') == 'g' and i + 1 < len(raw) and raw[i + 1].rstrip('?') == '÷':
                toks += raw[i:i + 2]; i += 2; continue
            if (ln, pos) in CHANGES:
                old, new = CHANGES[(ln, pos)]
                assert t.rstrip('?').split('/')[0] == old, (ln, pos, t, old)
                t = new; done.add((ln, pos))
            toks.append(t); i += 1
        out.append(ln + '\t' + ' '.join(toks))
    assert done == set(CHANGES), set(CHANGES) - done
    return '\n'.join(out) + '\n'


if __name__ == '__main__':
    fn = os.path.join(TGT, 'ciphertext_f13_passE.tsv'); txt = build()
    if '--check' in sys.argv:
        sys.exit(0 if os.path.exists(fn) and open(fn).read() == txt else 1)
    open(fn, 'w').write(txt); print('wrote', fn)
