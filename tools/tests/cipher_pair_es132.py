#!/usr/bin/env python3
"""Real two-copy known-answer control for tools/interlinear_align.py --cipher-pair (TT-PAIR, 8 Oct 2026).

Case: BnF Espagnol 132, Philip II to Juan de Vargas Mexia, Madrid 19 Sept 1578: the letter f.89r-f.91r and its duplicate
cipher copy f.93r-f.95r, both transcribed in ciphers/es132-vargas-mexia-1578/ (ciphertext_f*.tsv, two blind passes each,
reconciled, 4 Oct 2026), with the published letter/syllable table Cp.30 (key.tsv; S. Tomokiyo, Cryptiana spanish3.htm
cp30.png, after Devos 1950 and Alcocer 1921). One key, two encipherments by the clerk (about 4% homophone/notation
variants, the rest identical tokens; dup_align_summary.json). The tool gets the two token streams only, no key.
Token stream: align_dup.py's own stream() (f.89r L01 clear opening and {CLEAR} dropped), each token as base+vowel+marks
(align_dup.parts); a cursive {word} (a nomenclature code) is kept as one cipher token 'W:word', not as clear letters.
Truth: test0.dec_tok under key.tsv; a token that does not decode (nomenclature, '?') is unknown and left out of scoring.
Scores: precision = accepted equivalences whose two symbols decode the same / accepted with both decodable; the same over
non-identical pairs only (the homophone part); colagree = share of align_dup.py's key-assisted aligned pairs
(dup_align.tsv, both tokens present) that the keyless alignment reproduces.
Null: copy B replaced by the other Cipher 3 letters on disk (f41r, f41v, f50r, f50v, f51r, f51v, f52r: the same key and
hand, a different text), cut to the duplicate's token count. It can fail differently: with a different text the
co-aligned symbol pairs no longer stand for the same plaintext except by chance.

    python3 tools/tests/cipher_pair_es132.py [--out FILE.tsv]
"""
import csv
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.normpath(os.path.join(HERE, '..', '..', 'ciphers', 'es132-vargas-mexia-1578'))
sys.path.insert(0, T)
import align_dup as AD  # noqa: E402
from test0 import load_key, dec_tok  # noqa: E402

TOOL = os.path.join(HERE, '..', 'interlinear_align.py')
NULL_PAGES = ['f41r', 'f41v', 'f50r', 'f50v', 'f51r', 'f51v', 'f52r']


def toks(stream):
    out = []
    for p, ln, i, t in stream:
        b, v, m = AD.parts(t)
        out.append(('W:' + b) if t.startswith('{') else (b + v + m))
    return out


def truth(stream, key):
    return [dec_tok(t[3].rstrip('?'), key)[0] if not t[3].endswith('?') else None for t in stream]


def run(A, B):
    d = tempfile.mkdtemp()
    open(os.path.join(d, 'a'), 'w').write(' '.join(A))
    open(os.path.join(d, 'b'), 'w').write(' '.join(B))
    p = subprocess.run([sys.executable, TOOL, '--cipher-pair', os.path.join(d, 'a'), os.path.join(d, 'b'),
                        '--out', os.path.join(d, 'o')], check=True, capture_output=True, text=True)
    return os.path.join(d, 'o'), p.stdout.strip()


def score(out, A, B, tA, tB):
    # a symbol's decoded value: its majority over decodable occurrences (one symbol = one value under Cp.30)
    def val(sy, tr):
        c = {}
        for s, v in zip(sy, tr):
            if v is not None:
                c.setdefault(s, {}).setdefault(v, 0)
                c[s][v] += 1
        return {s: max(d.items(), key=lambda kv: kv[1])[0] for s, d in c.items()}
    vA, vB = val(A, tA), val(B, tB)
    acc = list(csv.DictReader(open(os.path.join(out, 'equivalences.tsv')), delimiter='\t'))
    sc = [(r['a'], r['b'], vA[r['a']] == vB[r['b']]) for r in acc if r['a'] in vA and r['b'] in vB]
    prec = sum(ok for *_x, ok in sc) / len(sc) if sc else 0.0
    ni = [ok for a, b, ok in sc if a != b]
    return len(acc), len(sc), prec, len(ni), (sum(ni) / len(ni) if ni else 0.0)


def main():
    key = load_key()
    R, D = AD.stream(AD.REF), AD.stream(AD.DUP)
    A, B = toks(R), toks(D)
    tA, tB = truth(R, key), truth(D, key)
    out, so = run(A, B)
    n, ns, prec, nni, pni = score(out, A, B, tA, tB)
    # column agreement with the key-assisted alignment (dup_align.tsv)
    ref = [ln.rstrip('\n').split('\t') for ln in open(os.path.join(T, 'dup_align.tsv'), encoding='utf-8')
           if not ln.startswith('#')]
    print('es132 f.89-91 x f.93-95: %s' % so)
    rows = list(csv.DictReader(open(os.path.join(out, 'alignment.tsv')), delimiter='\t'))
    ia = ib = 0
    mine = set()
    for r in rows:
        a = ia if r['a'] else None
        b = ib if r['b'] else None
        if r['a']:
            ia += 1
        if r['b']:
            ib += 1
        if a is not None and b is not None:
            mine.add((a, b))
    keyed = set()
    idxR = {(t[0], t[1], t[2]): k for k, t in enumerate(R)}
    idxD = {(t[0], t[1], t[2]): k for k, t in enumerate(D)}
    for r in ref:
        pa, pb = r[0].split(':'), r[3].split(':')
        if len(pa) == 3 and len(pb) == 3:
            x, y = idxR.get((pa[0], pa[1], int(pa[2]))), idxD.get((pb[0], pb[1], int(pb[2])))
            if x is not None and y is not None:
                keyed.add((x, y))
    colagree = len(mine & keyed) / len(keyed) if keyed else float('nan')
    res = [('es132', n, ns, prec, nni, pni, colagree, len(keyed))]
    # null: other Cipher 3 letters of the same key and hand
    N = AD.stream(NULL_PAGES)[:len(D)]
    outn, son = run(A, toks(N))
    nn = score(outn, A, toks(N), tA, truth(N, key))
    res.append(('null', ) + nn + (float('nan'), 0))
    for r in res:
        print('%-6s accepted %d (scored %d) precision %.3f | non-identical %d precision %.3f | colagree %.3f of %d'
              % r)
    if '--out' in sys.argv:
        with open(sys.argv[sys.argv.index('--out') + 1], 'w') as f:
            f.write('case\taccepted\tscored\tprecision\tnonidentical\tprecision_nonidentical\tcolagree\tkeyed_pairs\n')
            for r in res:
                f.write('%s\t%d\t%d\t%.3f\t%d\t%.3f\t%.3f\t%d\n' % r)


if __name__ == '__main__':
    main()
