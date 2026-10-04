#!/usr/bin/env python3
"""N6-VIV63: decode fr.16105 ink 63 (10 Oct 1573) pages with key.tsv and grade every token (rule 4, rule 7).

    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv63_decode.py [--check]

Same code path as tx/viv54_decode.py (imported: key(), page_tokens() with reconcile_vivk RULES + RULES54, "o o" -> "oo",
assertion against the committed tx/<page>_rec.tsv). Grades: H = both passes agree (or a label rule settled the split) and the
code's key.tsv value is grade C (Tomokiyo's published key, checked against the clerk decipherment in N5-VIVK) -- key-source
grading, not legibility; M = the code's key.tsv grade is M (S, y, b, A), or an unsettled reader split or a one-pass gap;
U = code not in key.tsv. Writes reading_piece63.tsv; --check exits 1 if it is stale.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import viv54_decode as vd  # noqa: E402

PAGES = ('f190r', 'f190v', 'f191r', 'f191v')


def lines():
    return [(page, line, seq) for page in PAGES for line, seq in sorted(vd.page_tokens(page).items())]


def build():
    k = vd.key()
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
    text, n = build()
    path = os.path.join(T, 'reading_piece63.tsv')
    if '--check' in sys.argv:
        ok = os.path.exists(path) and open(path, encoding='utf-8').read() == text
        print('reading_piece63.tsv', 'up to date' if ok else 'STALE'); sys.exit(0 if ok else 1)
    open(path, 'w', encoding='utf-8').write(text)
    tot = sum(n.values())
    print(f'tokens {tot}: H {n["H"]} M {n["M"]} U {n["U"]} (H share {n["H"]/tot:.3f})')


if __name__ == '__main__':
    main()
