#!/usr/bin/env python3
"""N7-VIV53L: re-decode ink 53 (fr.16104 ff.170r-171v) after the look-alike fold-in, under PREREG-N7VIV53L.md's label rules.

    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv53L_decode.py [--check]

Input per page: tx/lookalike53L/<page>/passD.tsv (`tools/lookalike_pass.py reconcile` of the window re-read against the split tiles;
passage, pos, sign_id, conf, note) and that page's agreement.tsv (status agree | split | gap, from tx/viv53L_prep.py).
Rules (PREREG-N7VIV53L (i)): settled = status agree (both readers, or an N6 reconcile_vivk label rule) OR a look-alike 2-of-3 settle;
everything else (unsettled split, one-reader gap) is flagged. Label map after the vote: reconcile_vivk.MAP plus '+' -> '4'. Then
"o o" -> "oo" (as tx/viv54_decode.py), then every ': :' pair in a line is joined into ONE ':' (key cell col c row 1, value c; a run of
three joins the first two), flagged unless both halves were settled. Grades as tx/viv54_decode.py: U = code not in key.tsv; M = flagged
or key grade M; else H. Writes reading_piece53_L.tsv (page, line, codes, decode, grades) and piece53_L_decode.txt (letters only);
--check exits 1 if either is stale.
"""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import viv54_decode as vd  # noqa: E402
import reconcile_vivk as rv  # noqa: E402

PAGES = ('f170r', 'f170v', 'f171r', 'f171v')
MAP = {**rv.MAP, '+': '4'}
SETTLE = ('lookalike 2-of-3', 'lookalike confirms')


def page_tokens(page):
    d = os.path.join(HERE, 'lookalike53L', page)
    st = {(r['passage'], r['posA']): r['status'] for r in csv.DictReader(open(os.path.join(d, 'agreement.tsv')), delimiter='\t')}
    rows = {}
    for r in csv.DictReader(open(os.path.join(d, 'passD.tsv')), delimiter='\t'):
        s = st[(r['passage'], r['pos'])]
        settled = s == 'agree' or (s == 'split' and r['note'] in SETTLE)
        lab = MAP.get(r['sign_id'], r['sign_id'])
        rows.setdefault(r['passage'].split('_', 1)[1], []).append((lab, not settled, 'K' if s == 'split' and settled else ''))
    out = {}
    for line, toks in rows.items():
        seq, i = [], 0
        while i < len(toks):
            if toks[i][0] == 'o' and i + 1 < len(toks) and toks[i + 1][0] == 'o':
                seq.append(('oo', toks[i][1] or toks[i + 1][1], toks[i][2] + toks[i + 1][2])); i += 2
            else:
                seq.append(toks[i]); i += 1
        seq2, i = [], 0
        while i < len(seq):
            if seq[i][0] == ':' and i + 1 < len(seq) and seq[i + 1][0] == ':':
                seq2.append((':', seq[i][1] or seq[i + 1][1], 'J' + seq[i][2] + seq[i + 1][2])); i += 2
            else:
                seq2.append(seq[i]); i += 1
        out[line] = seq2
    return out


def build():
    k = vd.key()
    lines, n, letters, joins = [], {'H': 0, 'M': 0, 'U': 0}, [], 0
    for page in PAGES:
        for line, seq in sorted(page_tokens(page).items()):
            dec, gr, codes = [], [], []
            for c, flag, j in seq:
                joins += 'J' in j
                codes.append('::' if 'J' in j else c)
                if c not in k:
                    dec.append('_'); g = 'U'
                else:
                    dec.append(k[c][0]); g = 'M' if (flag or k[c][1] == 'M') else 'H'
                gr.append(g); n[g] += 1
            lines.append(f'{page}\t{line}\t{" ".join(codes)}\t{"".join(dec)}\t{"".join(gr)}')
            letters.append(''.join(dec).replace('_', ''))
    return ('page\tline\tcodes\tdecode\tgrades\n' + '\n'.join(lines) + '\n', ''.join(letters) + '\n', n, joins)


def main():
    text, letters, n, joins = build()
    p1, p2 = os.path.join(T, 'reading_piece53_L.tsv'), os.path.join(T, 'piece53_L_decode.txt')
    if '--check' in sys.argv:
        ok = all(os.path.exists(p) and open(p, encoding='utf-8').read() == s for p, s in ((p1, text), (p2, letters)))
        print('reading_piece53_L.tsv', 'up to date' if ok else 'STALE'); sys.exit(0 if ok else 1)
    open(p1, 'w', encoding='utf-8').write(text); open(p2, 'w', encoding='utf-8').write(letters)
    tot = sum(n.values())
    print(f'tokens {tot}: H {n["H"]} M {n["M"]} U {n["U"]}; ": :" pairs joined {joins}; letters {len(letters) - 1}')


if __name__ == '__main__':
    main()
