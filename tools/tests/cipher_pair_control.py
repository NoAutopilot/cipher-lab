#!/usr/bin/env python3
"""Semi-synthetic known-answer control for tools/interlinear_align.py --cipher-pair (TT-PAIR, 8 Oct 2026).

Case: Tomokiyo's own break of Servien to Sabran 1632 (BnF Baluze 155 f.123 and its duplicate f.127; Cryptiana
servien.htm, practice 7 of LESSONS-TOMOKIYO.md). The page prints both PLAINTEXTS in parallel (fixture
tools/tests/fixtures/servien_1632_parallel.tsv) but the cipher symbols only as images, and no transcription of the two
ciphertexts is on disk (ciphers/decode-2754-bnf-baluze156-1636/NOTES.md, KH-CS3, 8 Oct 2026: "No transcription"). So each
copy's real plaintext is enciphered here with a homophonic key of the period shape -- the per-letter homophone counts of
Tomokiyo's own recovered Servien-Sabran key (key_servien_1632_letters.tsv, H+M rows: a6 b1 c3 d4 e5 f2 g2 h1 i4 l3 m3 n3
o3 p2 q1 r3 s5 t4 u3 x1, 3 nulls) -- homophone chosen at random per occurrence, nulls inserted at --null-rate, words he
marks clear left clear. Two designs:
  same    one key, two independent encipherments (Servien's own case: two copies, one key);
  indep   two independent keys (Viete's case: the same text to two ambassadors on two keys).
Null: copy B replaced by a DIFFERENT text (a fr17 corpus passage of the same letter count, same clear-word rate, same
key design). It can fail differently from the target: the statistic is which A symbol aligns to which B symbol, and with
an unrelated B text that co-alignment falls to chance, so precision drops toward sum(p_letter^2) (about 0.07).
Scores per seed: precision = accepted A<->B equivalences whose two symbols carry the same plaintext letter (nulls count
as wrong); recall = correct accepted pairs / true same-letter pairs with both symbols present as cipher in their copy;
hrecall = pairs of A symbols of one letter placed in one homophone group / all such pairs present; crib = crib
columns (a cipher token against a clear letter of the other copy) whose cipher token truly stands for that letter;
opening = the same over the crib columns of the first 16 columns (Tomokiyo's 'cete' vs 'ceste' shift).

    python3 tools/tests/cipher_pair_control.py [--seeds 10] [--design same|indep|both] [--null] [--out FILE.tsv]
"""
import argparse
import gzip
import itertools
import os
import random
import re
import subprocess
import sys
import tempfile
import unicodedata
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(HERE, '..', 'interlinear_align.py')
FIX = os.path.join(HERE, 'fixtures', 'servien_1632_parallel.tsv')
SHAPE = dict(a=6, b=1, c=3, d=4, e=5, f=2, g=2, h=1, i=4, l=3, m=3, n=3, o=3, p=2, q=1, r=3, s=5, t=4, u=3, x=1)
NULLS = 3
FOLDMAP = {'j': 'i', 'y': 'i', 'v': 'u', 'w': 'u', 'k': 'c', 'z': 's'}


def norm(s):
    s = ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if unicodedata.category(c) != 'Mn')
    return ''.join(FOLDMAP.get(c, c) for c in s if c.isalpha())


def load_servien():
    A, B = [], []
    for ln in open(FIX, encoding='utf-8'):
        if ln.startswith('#') or ln.startswith('line\t'):
            continue
        _l, copy, text = ln.rstrip('\n').split('\t')
        (A if copy == 'A' else B).append(text)
    return ' '.join(A), ' '.join(B)


def segments(text):
    """-> list of (clear?, letters) word by word."""
    out = []
    for m in re.finditer(r'\{([^}]*)\}|([^{}\s]+)', text):
        if m.group(1) is not None:
            for wd in m.group(1).split():
                out.append((True, norm(wd)))
        else:
            out.append((False, norm(m.group(2))))
    return [(c, w) for c, w in out if w]


def make_key(rng, prefix):
    syms = ['%s%02d' % (prefix, k) for k in range(sum(SHAPE.values()) + NULLS)]
    rng.shuffle(syms)
    key, it = {}, iter(syms)
    for L, n in SHAPE.items():
        key[L] = [next(it) for _ in range(n)]
    nulls = list(it)
    truth = {s: L for L, ss in key.items() for s in ss}
    truth.update({s: '#null' for s in nulls})
    return key, nulls, truth


def encipher(segs, key, nulls, rng, null_rate):
    out = []
    for clear, w in segs:
        if clear:
            out.append('{%s}' % w)
            continue
        toks = []
        for ch in w:
            toks.append(rng.choice(key[ch]))
            if rng.random() < null_rate:
                toks.append(rng.choice(nulls))
        out.append(' '.join(toks))
    return ' '.join(out)


def corpus_passage(nletters, clear_rate, rng):
    d = os.path.join(HERE, '..', 'data', 'fr17')
    fs = sorted(f for f in os.listdir(d) if f.endswith('.txt.gz'))
    txt = gzip.open(os.path.join(d, fs[0]), 'rt', encoding='utf-8', errors='replace').read()
    words = [w for w in re.findall(r"[A-Za-zÀ-ÿ']+", txt) if norm(w)]
    start = rng.randrange(0, len(words) - 2000)
    segs, n = [], 0
    for w in words[start:]:
        segs.append((rng.random() < clear_rate, norm(w)))
        n += len(norm(w))
        if n >= nletters:
            break
    return segs


def score(outdir, truthA, truthB, cipherA, cipherB):
    import csv
    acc = list(csv.DictReader(open(os.path.join(outdir, 'equivalences.tsv')), delimiter='\t'))
    groups = list(csv.DictReader(open(os.path.join(outdir, 'groups.tsv')), delimiter='\t'))
    ok = sum(1 for r in acc if truthA[r['a']] == truthB[r['b']] and truthA[r['a']] != '#null')
    prec = ok / len(acc) if acc else 0.0
    presA, presB = set(cipherA), set(cipherB)
    true_pairs = sum(1 for a in presA for b in presB if truthA[a] == truthB[b] and truthA[a] != '#null')
    rec = ok / true_pairs if true_pairs else 0.0
    gid = {}
    for g in groups:
        for s in g['a_symbols'].split():
            gid[s] = g['group']
    hp = [(x, y) for x, y in itertools.combinations(sorted(presA), 2) if truthA[x] == truthA[y] != '#null']
    hrec = sum(1 for x, y in hp if gid.get(x) and gid.get(x) == gid.get(y)) / len(hp) if hp else 0.0
    rows = list(csv.DictReader(open(os.path.join(outdir, 'alignment.tsv')), delimiter='\t'))
    cr = []
    for r in rows:
        if r['kind'] != 'crib':
            continue
        if r['a'].startswith('{'):
            cr.append((int(r['col']), truthB[r['b']] == r['a'][1:-1]))
        else:
            cr.append((int(r['col']), truthA[r['a']] == r['b'][1:-1]))
    cacc = sum(ok for _c, ok in cr) / len(cr) if cr else 0.0
    op = [ok for c, ok in cr if c < 16]
    oacc = sum(op) / len(op) if op else 0.0
    return len(acc), prec, rec, hrec, cacc, oacc


def one(seed, design, null, null_rate=0.03):
    rng = random.Random(seed)
    tA, tB = load_servien()
    sA, sB = segments(tA), segments(tB)
    if null:
        nB = sum(len(w) for _c, w in sB)
        cr = sum(1 for c, _w in sB if c) / len(sB)
        sB = corpus_passage(nB, cr, rng)
    keyA, nullsA, truthA = make_key(rng, 's')
    if design == 'same':
        keyB, nullsB, truthB = keyA, nullsA, truthA
    else:
        keyB, nullsB, truthB = make_key(rng, 'B')
    cA = encipher(sA, keyA, nullsA, rng, null_rate)
    cB = encipher(sB, keyB, nullsB, rng, null_rate)
    d = tempfile.mkdtemp()
    pa, pb = os.path.join(d, 'a.txt'), os.path.join(d, 'b.txt')
    open(pa, 'w').write(cA)
    open(pb, 'w').write(cB)
    subprocess.run([sys.executable, TOOL, '--cipher-pair', pa, pb, '--out', os.path.join(d, 'out')],
                   check=True, capture_output=True)
    symA = [t for t in re.sub(r'\{[^}]*\}', ' ', cA).split()]
    symB = [t for t in re.sub(r'\{[^}]*\}', ' ', cB).split()]
    return score(os.path.join(d, 'out'), truthA, truthB, symA, symB)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--seeds', type=int, default=10)
    ap.add_argument('--design', default='both', choices=['same', 'indep', 'both'])
    ap.add_argument('--null', action='store_true', help='also run the different-text null')
    ap.add_argument('--out')
    a = ap.parse_args()
    rows = []
    designs = ['same', 'indep'] if a.design == 'both' else [a.design]
    for design in designs:
        for null in ([False, True] if a.null else [False]):
            res = [one(1632 + s, design, null) for s in range(a.seeds)]
            for s, r in enumerate(res):
                rows.append((design, 'null' if null else 'servien', 1632 + s) + r)
            m = [sum(x[k] for x in res) / len(res) for k in range(6)]
            print('%-5s %-7s seeds %d: accepted %.1f  precision %.3f (min %.3f max %.3f)  recall %.3f  hrecall %.3f'
                  '  crib %.3f  opening %.3f'
                  % (design, 'null' if null else 'servien', len(res), m[0], m[1], min(x[1] for x in res),
                     max(x[1] for x in res), m[2], m[3], m[4], m[5]))
    if a.out:
        with open(a.out, 'w') as f:
            f.write('design\tcase\tseed\taccepted\tprecision\trecall\threcall\tcrib\topening\n')
            for r in rows:
                f.write('%s\t%s\t%d\t%d\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f\n' % r)


if __name__ == '__main__':
    main()
