#!/usr/bin/env python3
"""Offline test for test2.py's {CLEAR:} handling (RUN5-ESFIX, 4 Oct 2026): a page whose passes carry multi-word {CLEAR:...}
spans (a whole clear line, and a clear span then '/') must load, strip and score exactly as the same page with those spans
removed by hand. Before the fix, words 2+ of a span were normalised and key-decoded into S_b. Run: python3 test_test2_clear.py"""
import sys, gzip, random, tempfile
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import test2
from test0 import load_key, shuffled
import judge_plaintext as jp

CIPHER = ['20ρ@rmark 24+@hat 1 24. 28 7ρ@hat 29. 26 6 4@hat 24. 4@acute 8. 24.',
          '26 7σ 18 6. 16σ 23 7ρ 23+@bar 28 6. 15+ 73 6. 23+ 7ρ 24+']
WITH = ['L01\t{CLEAR:del recibo de Vras cartas, Han llegado las de xvj. xvij. xx. xxj}',
        'L02\t{CLEAR:xxv. y xxviij del passado} / ' + CIPHER[0], 'L03\t' + CIPHER[1],
        'L04\t{CLEAR:del Bosq de segovia ± vij de junio 1578.}']
WITHOUT = ['L02\t/ ' + CIPHER[0], 'L03\t' + CIPHER[1]]


def write(d, name, rows):
    p = Path(d) / name; p.write_text('# test\n' + '\n'.join(rows) + '\n', encoding='utf-8'); return p


def main():
    with tempfile.TemporaryDirectory() as d:
        cA = {}
        Lw = test2.load_pass(write(d, 'w.tsv', WITH), cA)
        Lo = test2.load_pass(write(d, 'o.tsv', WITHOUT))
        assert cA == {'L01': 'line', 'L02': 'prefix', 'L04': 'line'}, cA
        flat = lambda L: [t for ln in sorted(L) for t in L[ln]]
        assert flat(Lw) == flat(Lo), (flat(Lw), flat(Lo))
        # reconciled lines as the old leak left them (clear words normalised into tokens): strip_clear must cut them
        R = {'L01': ['rρ', 'dρ', 'V', 'c', 'x.', 'x'], 'L02': ['y', 'x', 'dρ', 'p', '/'] + Lo['L02'][1:], 'L03': Lo['L03'],
             'L04': ['B', 'dρ', 'sρ', 'v', 'dρ']}
        Rs = test2.strip_clear(R, 'test', cA, dict(cA))
        assert flat(Rs) == [t for t in flat(Lo) if t != '/'], flat(Rs)
        try:
            test2.strip_clear(R, 'test', cA, {}); raise AssertionError('pass disagreement not caught')
        except SystemExit:
            pass
        key = load_key(); rng = random.Random(1578); shuf = [shuffled(key, rng) for _ in range(20)]
        model = jp.NgramModel([gzip.open(p, 'rt', encoding='utf-8').read() for p in test2.ES16])
        sw = test2.score(flat(Lw), key, shuf, model, random.Random(1578))
        so = test2.score(flat(Lo), key, shuf, model, random.Random(1578))
        assert sw == so, (sw, so)
        # and the old per-token loader really did leak (guards against a test that cannot fail)
        old = [x for x in (test2.shape_tok(t) for t in WITH[0].split('\t')[1].split()) if x]
        assert old, 'old loader shape no longer leaks; test lost its teeth'
    print('OK: multi-word {CLEAR:} spans score identically to the page without them (S_b %s, %d letters)' % (sw['S_b'], sw['letters']))


if __name__ == '__main__':
    main()
