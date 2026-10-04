#!/usr/bin/env python3
"""N7-VIV54L: re-decode ink 54 (fr.16104 f.173r-v) under PREREG-N7VIV54L.md's label rules and grade every token (rules 4, 7).

    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv54L_decode.py [--check] [--before]

Input per page: tx/lookalike54/viv54L_<page>_passD.tsv (`lookalike_pass.py reconcile` of the value-blind re-read: every unsettled split
and one-pass gap of N5-VIV54 is a tile, settled at 2-of-3 or left UNSETTLED with pass A's label) and the tile list beside it.
Rules (PREREG (i)): L2 = the reconcile output; L1 = two consecutive ':' tokens -> one ':' (key ':' = c), flag = either flag; then
"o o" -> "oo" as tx/viv54_decode.py. Grades: H = agreed / N5 label rule / look-alike 2-of-3, AND key.tsv grade C; M = key grade M or
UNSETTLED or a flagged token merged; U = not in key.tsv. key.tsv, tx/viv54_decode.py and reading_piece54.tsv are not touched.
Writes reading_piece54_L.tsv; --check exits 1 if stale. --before returns the committed N5-VIV54 sequence with only L1 applied (diagnostic).
"""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
LA = os.path.join(HERE, 'lookalike54')
sys.path.insert(0, HERE)
import viv54_decode as vd  # noqa: E402

PAGES = ('f173r', 'f173v')


def _read(p):
    return list(csv.DictReader(open(p, encoding='utf-8', newline=''), delimiter='\t'))


def collapse(seq):
    """L1 then the oo rule. seq = [(label, flag)]."""
    out, i = [], 0
    while i < len(seq):
        if seq[i][0] == ':' and i + 1 < len(seq) and seq[i + 1][0] == ':':
            out.append((':', seq[i][1] or seq[i + 1][1], 'L1')); i += 2
        else:
            out.append((seq[i][0], seq[i][1], '')); i += 1
    res, i = [], 0
    while i < len(out):
        if out[i][0] == 'o' and i + 1 < len(out) and out[i + 1][0] == 'o':
            res.append(('oo', out[i][1] or out[i + 1][1], out[i][2])); i += 2
        else:
            res.append(out[i]); i += 1
    return res


def page_seqs(page):
    tiles = {(t['passage'], t['pos']) for t in _read(os.path.join(LA, f'viv54L_{page}_tiles.tsv'))}
    rows = {}
    for r in _read(os.path.join(LA, f'viv54L_{page}_passD.tsv')):
        k = (r['passage'], r['pos'])
        flag = k in tiles and r['note'] == 'lookalike UNSETTLED'
        rows.setdefault(r['passage'], []).append((r['sign_id'], flag))
    return {ln: collapse(seq) for ln, seq in rows.items()}


def before_seqs(page):
    """Committed N5-VIV54 sequence (its own flags), with L1 applied -- diagnostic only."""
    out = {}
    for ln, seq in vd.page_tokens(page).items():
        flat = []
        for c, f in seq:   # undo the oo merge so L1 sees the same token stream, then re-merge
            flat += [('o', f), ('o', f)] if c == 'oo' else [(c, f)]
        out[ln] = collapse(flat)
    return out


def build():
    k = vd.key()
    lines, n, l1 = [], {'H': 0, 'M': 0, 'U': 0}, 0
    for page in PAGES:
        for line, seq in sorted(page_seqs(page).items()):
            dec, gr = [], []
            for c, flag, why in seq:
                l1 += why == 'L1'
                if c not in k:
                    dec.append('_'); g = 'U'
                else:
                    dec.append(k[c][0]); g = 'M' if (flag or k[c][1] == 'M') else 'H'
                gr.append(g); n[g] += 1
            lines.append(f'{page}\t{line}\t{" ".join(c for c, _, _ in seq)}\t{"".join(dec)}\t{"".join(gr)}')
    return 'page\tline\tcodes\tdecode\tgrades\n' + '\n'.join(lines) + '\n', n, l1


def main():
    text, n, l1 = build()
    path = os.path.join(T, 'reading_piece54_L.tsv')
    if '--check' in sys.argv:
        ok = os.path.exists(path) and open(path, encoding='utf-8').read() == text
        print('reading_piece54_L.tsv', 'up to date' if ok else 'STALE'); sys.exit(0 if ok else 1)
    open(path, 'w', encoding='utf-8').write(text)
    tot = sum(n.values())
    print(f'tokens {tot}: H {n["H"]} M {n["M"]} U {n["U"]}; L1 ": :" merges {l1}')


if __name__ == '__main__':
    main()
