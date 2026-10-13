#!/usr/bin/env python3
"""VIV52-O: decode fr.16104 ink 52 (5 Sept 1572, Vivonne to the Queen) pages with key.tsv and grade every token (rule 4, rule 7).

    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv52_decode.py [--check] [--key key_tomokiyo.tsv]

tx/viv63_decode.py's code path unchanged (page_tokens with reconcile_vivk RULES + RULES54 + RULES63, "o o" -> "oo"; PREREG-VIV52O.md):
no label rule added for ink 52. Grades as viv63_decode: H = both passes agree (or an inherited rule settled the split) and the code's
key.tsv value is grade C (Tomokiyo's published key, N5-VIVK; V -> n from VIV-ANCHOR); M = key grade M, or an unsettled split or a
one-pass gap; U = code not in key.tsv. Writes reading_piece52.tsv and tx/<page>_rec.tsv; --check exits 1 if stale.
--key key_tomokiyo.tsv prints the alternative decode only (descriptive; writes nothing).
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import viv54_decode as vd  # noqa: E402
import viv63_decode as v63  # noqa: E402

PAGES = ('f164r', 'f164v')  # VIV52-O, 13 Oct 2026; ff.165r-168v not transcribed (NOTES "VIV52-O")


def key(name='key.tsv'):
    k = {}
    for ln in open(os.path.join(T, name), encoding='utf-8'):
        f = ln.rstrip('\n').split('\t')
        if f[0] != 'code':
            k[f[0]] = (f[1], f[2] if name == 'key.tsv' else 'C')
    return k


def lines(pages=PAGES):
    return v63.lines(pages)


def build(k):
    out, n = [], {'H': 0, 'M': 0, 'U': 0}
    for page, line, seq in lines():
        dec, gr = [], []
        for c, flag in seq:
            if c not in k:
                dec.append('_'); g = 'U'
            else:
                dec.append(k[c][0]); g = 'M' if (flag or k[c][1] == 'M') else 'H'
            gr.append(g); n[g] += 1
        out.append(f'{page}\t{line}\t{" ".join(c for c, _ in seq)}\t{"".join(dec)}\t{"".join(gr)}')
    return 'page\tline\tcodes\tdecode\tgrades\n' + '\n'.join(out) + '\n', n


def main():
    if '--key' in sys.argv:
        text, n = build(key(sys.argv[sys.argv.index('--key') + 1]))
        print(text); print(n); return
    text, n = build(key())
    files = {os.path.join(T, 'reading_piece52.tsv'): text}
    for page in PAGES:
        _, wide, st = v63.page_tokens(page)
        files[os.path.join(HERE, f'{page}_rec.tsv')] = wide
        if '--check' not in sys.argv:
            print(page, st)
    if '--check' in sys.argv:
        stale = [p for p, t in files.items() if not os.path.exists(p) or open(p, encoding='utf-8').read() != t]
        print('reading_piece52.tsv + rec files', 'up to date' if not stale else 'STALE: ' + ', '.join(stale)); sys.exit(1 if stale else 0)
    for p, t in files.items():
        open(p, 'w', encoding='utf-8').write(t)
    tot = sum(n.values())
    print(f'tokens {tot}: H {n["H"]} M {n["M"]} U {n["U"]} (H share {n["H"]/tot:.3f})')


if __name__ == '__main__':
    main()
