#!/usr/bin/env python3
"""Offline test for tools/interlinear_align.py --cipher-pair (TT-PAIR, 8 Oct 2026; Tomokiyo practice 7, servien.htm).
Must catch: homophone equivalences between two independent encipherments of one text with wording differences.
Must NOT flag: two different texts of the same length (equivalences there stay at chance precision).
Run: python3 tools/tests/test_interlinear_cipher_pair.py"""
import csv
import os
import random
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import cipher_pair_control as C  # noqa: E402

TOOL = os.path.join(HERE, '..', 'interlinear_align.py')


def run(cA, cB):
    d = tempfile.mkdtemp()
    for n, t in (('a', cA), ('b', cB)):
        open(os.path.join(d, n), 'w').write(t)
    p = subprocess.run([sys.executable, TOOL, '--cipher-pair', os.path.join(d, 'a'), os.path.join(d, 'b'),
                        '--out', os.path.join(d, 'o')], check=True, capture_output=True, text=True)
    return os.path.join(d, 'o'), p.stdout


def case(seed, null):
    rng = random.Random(seed)
    sA = C.corpus_passage(300, 0.15, rng)
    sB = [(rng.random() < 0.15, w) for c, w in sA if rng.random() > 0.04]
    if null:
        sB = C.corpus_passage(sum(len(w) for _c, w in sB), 0.15, rng)
    kA, nA, tA = C.make_key(rng, 's')
    kB, nB, tB = C.make_key(rng, 'B')
    cA, cB = C.encipher(sA, kA, nA, rng, 0.03), C.encipher(sB, kB, nB, rng, 0.03)
    out, _ = run(cA, cB)
    strip = lambda c: [t for t in __import__('re').sub(r'\{[^}]*\}', ' ', c).split()]
    return C.score(out, tA, tB, strip(cA), strip(cB)), out


def main():
    # parsing: braces are clear letters, '|' ignored; an identical clear pair is an anchor, cipher vs clear a crib
    out, so = run('x1 x2 | {ab} x3', '{q} y2 {ab} {c}')
    rows = list(csv.DictReader(open(os.path.join(out, 'alignment.tsv')), delimiter='\t'))
    kinds = [r['kind'] for r in rows]
    assert kinds.count('anchor') == 2, rows
    assert ('x3', '{c}') in [(r['a'], r['b']) for r in rows], rows
    for f in ('equivalences.tsv', 'groups.tsv', 'cribs.tsv'):
        assert os.path.exists(os.path.join(out, f)), f
    # must catch: one text, two keys, word drops and different clear words
    (n, prec, rec, hrec, cacc, _o), _ = case(5, False)
    assert prec >= 0.9 and rec >= 0.2 and cacc >= 0.8, (n, prec, rec, hrec, cacc)
    # must NOT flag: a different text of the same length
    (n0, prec0, rec0, _h, cacc0, _o), _ = case(5, True)
    assert prec0 <= 0.4 and rec0 <= 0.05 and n0 < n, (n0, prec0, rec0, cacc0)
    print('ok')


if __name__ == '__main__':
    main()
