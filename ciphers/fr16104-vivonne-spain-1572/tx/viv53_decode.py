#!/usr/bin/env python3
"""N6-VIV53 (+N6-VIV53B f.171v): decode fr.16104 ff.170r-171v (ink 53, 5 Sept 1572, to the duc d'Anjou) with key.tsv and grade every token (rule 4, 7).

    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv53_decode.py [--check]

Same method as tx/viv54_decode.py (whose functions it imports unchanged): tx/rec_<page>/ciphertext_draft.tsv (tools/reconcile_passes.py
on the _c passes) + tx/reconcile_vivk.py's label rules (+ RULES54), asserted equal to tx/<page>_rec.tsv; "o o" -> "oo". Grades:
H = both passes agree (or a label rule settled the split) and the code's key.tsv value is grade C; M = the code is an M code (S, y, b,
A) or the sign is an unsettled split / one-pass gap; U = code not in key.tsv. H is key-source grading (published key checked against a
period decipherment in N5-VIVK), not legibility. Writes reading_piece53.tsv; --check exits 1 if stale.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import viv54_decode as vd  # noqa: E402

PAGES_N6VIV53 = ('f170r', 'f170v', 'f171r')  # the pages of the registered gloss gate (tx/viv53_test.py), frozen
PAGES = PAGES_N6VIV53 + ('f171v',)  # N6-VIV53B added f.171v (PREREG-N6VIV53B.md)


def build():
    k = vd.key()
    lines, n = [], {'H': 0, 'M': 0, 'U': 0}
    for page in PAGES:
        for line, seq in sorted(vd.page_tokens(page).items()):
            dec, gr = [], []
            for c, flag in seq:
                if c not in k:
                    dec.append('_'); g = 'U'
                else:
                    dec.append(k[c][0]); g = 'M' if (flag or k[c][1] == 'M') else 'H'
                gr.append(g); n[g] += 1
            lines.append(f'{page}\t{line}\t{" ".join(c for c, _ in seq)}\t{"".join(dec)}\t{"".join(gr)}')
    return 'page\tline\tcodes\tdecode\tgrades\n' + '\n'.join(lines) + '\n', n


def main():
    text, n = build()
    path = os.path.join(T, 'reading_piece53.tsv')
    if '--check' in sys.argv:
        ok = os.path.exists(path) and open(path, encoding='utf-8').read() == text
        print('reading_piece53.tsv', 'up to date' if ok else 'STALE'); sys.exit(0 if ok else 1)
    open(path, 'w', encoding='utf-8').write(text)
    tot = sum(n.values())
    print(f'tokens {tot}: H {n["H"]} M {n["M"]} U {n["U"]} (H+M share {(n["H"]+n["M"])/tot:.3f})')


if __name__ == '__main__':
    main()
