#!/usr/bin/env python3
"""N5-VIV54: decode fr.16104 f.173r-v (ink 54, 7 Sept 1572) with key.tsv and grade every token (rule 4, rule 7).

    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv54_decode.py [--check]

Reads tx/rec_f173r|f173v/ciphertext_draft.tsv (tools/reconcile_passes.py on the _c passes) and applies
tx/reconcile_vivk.py's label rules (+ RULES54), so it agrees token for token with tx/f173r_rec.tsv / f173v_rec.tsv
(asserted). "o o" -> "oo" as tx/vivk_test.py. Grades: H = both passes agree (or a label rule settled the split) and the
code's key.tsv value is grade C (Tomokiyo's published key, supported by the clerk decipherment in N5-VIVK); M = the code's
key.tsv grade is M (S, y, b, A), or the sign is an unsettled reader split or a one-pass gap; U = code not in key.tsv (unread).
Writes reading_piece54.tsv (line, codes, decode with '_' for U, grades) and prints counts; --check exits 1 if stale.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import reconcile_vivk as rv  # noqa: E402

RULES = {**rv.RULES, **rv.RULES54}


def key():
    k = {}
    for ln in open(os.path.join(T, 'key.tsv'), encoding='utf-8'):
        f = ln.rstrip('\n').split('\t')
        if f[0] != 'code':
            k[f[0]] = (f[1], f[2])
    return k


def page_tokens(page):
    rows = {}
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
                a = w
            else:
                flag = True
        elif why == 'gap':
            flag = True
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
    # agree with the committed wide file
    wide = {}
    for ln in open(os.path.join(HERE, f'{page}_rec.tsv'), encoding='utf-8'):
        f = ln.rstrip('\n').split('\t')
        if f[0] != 'row':
            wide[f[0]] = f[1].split()
    for line in out:
        flat = [t for t, _ in rows[line]]
        assert flat == wide[line], (page, line)
    return out


def build():
    k = key()
    lines, n = [], {'H': 0, 'M': 0, 'U': 0}
    for page in ('f173r', 'f173v'):
        for line, seq in sorted(page_tokens(page).items()):
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
    path = os.path.join(T, 'reading_piece54.tsv')
    if '--check' in sys.argv:
        ok = os.path.exists(path) and open(path, encoding='utf-8').read() == text
        print('reading_piece54.tsv', 'up to date' if ok else 'STALE'); sys.exit(0 if ok else 1)
    open(path, 'w', encoding='utf-8').write(text)
    tot = sum(n.values())
    print(f'tokens {tot}: H {n["H"]} M {n["M"]} U {n["U"]} (H+M share {(n["H"]+n["M"])/tot:.3f})')


if __name__ == '__main__':
    main()
