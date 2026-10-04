#!/usr/bin/env python3
"""N6-VIV63: decode fr.16105 ink 63 (10 Oct 1573) pages with key.tsv and grade every token (rule 4, rule 7).

    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv63_decode.py [--check]

Same code path as tx/viv54_decode.py (key() imported; page_tokens() copied with reconcile_vivk RULES + RULES54 + RULES63 below,
"o o" -> "oo"); also writes tx/<page>_rec.tsv (wide) so --check covers them. Grades: H = both passes agree (or a label rule settled the split) and the
code's key.tsv value is grade C (Tomokiyo's published key, checked against the clerk decipherment in N5-VIVK) -- key-source
grading, not legibility; M = the code's key.tsv grade is M (S, y, b, A), or an unsettled reader split or a one-pass gap;
U = code not in key.tsv. Writes reading_piece63.tsv; --check exits 1 if it is stale.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import viv54_decode as vd  # noqa: E402
import reconcile_vivk as rv  # noqa: E402

# N6-VIV63 label rules, settled by this worker's eye on crops BEFORE any decode (NOTES "N6-VIV63"):
#   3/z -> 3: f.191r L01 s1 positions 6 and 26: the sign with a descender below the line is SIGNS.md's round 3; the flat z
#             stays on the line (both readers agree on those, e.g. L01 "d z"); pass B wrote z for both shapes.
#   P/p -> p: f.191r L04 s1 positions 10 and 14: p with a crossed descender (SIGNS.md "may look like p-bar"), not the pi sign.
#   R/r -> R, R/n -> R, n/r -> n: f.190v L01 s1 position 15 and f.191v L05 s1 position 5: the "rt"-like sign (n/r body with a
#             loop or bar at the top right) that SIGNS.md calls R; readers wrote it R, r or n. key.tsv reads R and n both as t, so
#             these rules change no decoded letter, only the H/M grade. NOT settled: r/z (f.190r L05 s1 position 12 is a small
#             r-rotunda, a different shape from the flat z that opens the same line), 2/z, c/e, h/k.
RULES63 = {frozenset(('3', 'z')): '3', frozenset(('P', 'p')): 'p',
           frozenset(('R', 'r')): 'R', frozenset(('R', 'n')): 'R', frozenset(('n', 'r')): 'n'}
RULES = {**rv.RULES, **rv.RULES54, **RULES63}
PAGES_A = ('f190r', 'f190v', 'f191r', 'f191v')  # N6-VIV63 (gate run on these alone: tx/viv63_test.py)
PAGES_B = ('f192r', 'f192v', 'f193r')  # N6-VIV63B (PREREG-N6VIV63B.md; tx/viv63b_test.py)
PAGES = PAGES_A + PAGES_B


def page_tokens(page):
    """viv54_decode.page_tokens with RULES63 added; also returns the wide per-line sign list (tx/<page>_rec.tsv)."""
    rows, stats = {}, {'settled': 0, 'unsettled': 0, 'gaps': 0}
    for ln in open(os.path.join(HERE, f'rec_{page}', 'ciphertext_draft.tsv'), encoding='utf-8'):
        f = ln.rstrip('\n').split('\t')
        if f[0] == 'line':
            continue
        line, pos, sign, conf, alt, why = (f + [''] * 6)[:6]
        a = sign.rstrip('?')
        b = alt[2:].rstrip('?') if alt.startswith('B:') else ''
        flag = False
        if why == 'differ' and b and b != '-':
            w = RULES.get(frozenset((a, b)))
            if w:
                a = w; stats['settled'] += 1
            else:
                flag = True; stats['unsettled'] += 1
        elif why == 'gap':
            flag = True; stats['gaps'] += 1
        if a in ('', '-'):
            continue
        rows.setdefault(line, []).append((rv.MAP.get(a, a), flag))
    out = {}
    for line, toks in rows.items():
        seq, i = [], 0
        while i < len(toks):
            if toks[i][0] == 'o' and i + 1 < len(toks) and toks[i + 1][0] == 'o':
                seq.append(('oo', toks[i][1] or toks[i + 1][1])); i += 2
            else:
                seq.append(toks[i]); i += 1
        out[line] = seq
    wide = 'row\tcodes\n' + ''.join(f'{l}\t{" ".join(t for t, _ in rows[l])}\n' for l in sorted(rows))
    return out, wide, stats


def lines(pages=PAGES):
    return [(page, line, seq) for page in pages for line, seq in sorted(page_tokens(page)[0].items())]


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
    files = {os.path.join(T, 'reading_piece63.tsv'): text}
    for page in PAGES:
        _, wide, st = page_tokens(page)
        files[os.path.join(HERE, f'{page}_rec.tsv')] = wide
        if '--check' not in sys.argv:
            print(page, st)
    if '--check' in sys.argv:
        stale = [p for p, t in files.items() if not os.path.exists(p) or open(p, encoding='utf-8').read() != t]
        print('reading_piece63.tsv + rec files', 'up to date' if not stale else 'STALE: ' + ', '.join(stale)); sys.exit(1 if stale else 0)
    for p, t in files.items():
        open(p, 'w', encoding='utf-8').write(t)
    tot = sum(n.values())
    print(f'tokens {tot}: H {n["H"]} M {n["M"]} U {n["U"]} (H share {n["H"]/tot:.3f})')


if __name__ == '__main__':
    main()
