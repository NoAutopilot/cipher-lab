#!/usr/bin/env python3
"""Offline test for tools/interlinear_align.py align --shuffle (R9-WVOALIGN, 6 Oct 2026): a letter-over-sign gloss
with a consistent substitution must beat its row-shuffled control; a gloss with no relation to its signs must not.
Run: python3 tools/tests/test_interlinear_shuffle.py"""
import csv, json, os, random, subprocess, sys, tempfile

TOOL = os.path.join(os.path.dirname(__file__), '..', 'interlinear_align.py')
LINES = ['wir konnen auch nit', 'das die adern zweimahl', 'worden sei das man', 'clagen und tausch',
         'purgiren mussen dermassen', 'kein gefahr nit habe', 'unfreundtlich vertrauen', 'gaben das die kein so']


def run(pairs):
    d = tempfile.mkdtemp()
    p = os.path.join(d, 'pairs.tsv')
    with open(p, 'w', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['plain_line', 'plain_raw', 'cipher_line', 'cipher_raw'])
        w.writerows(pairs)
    out = os.path.join(d, 's.json')
    subprocess.run([sys.executable, TOOL, 'align', p, os.path.join(d, 'a.tsv'), os.path.join(d, 'k.tsv'),
                    '--code-prefix', '@', '--seg-bonus', '0', '--keep-fs', '--shuffle', '50', '--shuffle-out', out],
                   check=True, capture_output=True)
    return json.load(open(out))


def main():
    sub = {c: 's%02d' % i for i, c in enumerate('abcdefghijklmnopqrstuvwxyz')}
    real = [[str(i), t, str(i), ' '.join('@' + sub[c] for c in t if c.isalpha())] for i, t in enumerate(LINES)]
    r = run(real)
    assert r['real'] > r['p95'], r            # a true letter-over-sign gloss: kept (must be caught)
    rng = random.Random(7)
    noise = [[str(i), t, str(i), ' '.join('@' + sub[rng.choice('abcdefghijklmnopqrstuvwxyz')] for c in t if c.isalpha())]
             for i, t in enumerate(LINES)]
    r2 = run(noise)
    assert r2['real'] <= r2['p95'], r2        # signs unrelated to the gloss: must NOT pass
    assert len(r2['draws']) == 50
    print('ok')


if __name__ == '__main__':
    main()
