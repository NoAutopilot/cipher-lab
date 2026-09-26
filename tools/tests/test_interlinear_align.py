#!/usr/bin/env python3
"""Offline test for tools/interlinear_align.py align (default mode and --floor/--clear-consumes).
Run: python3 tools/tests/test_interlinear_align.py"""
import csv, os, subprocess, sys, tempfile

TOOL = os.path.join(os.path.dirname(__file__), '..', 'interlinear_align.py')


def run(pairs, *opts):
    d = tempfile.mkdtemp()
    p = os.path.join(d, 'pairs.tsv')
    with open(p, 'w', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['plain_line', 'plain_raw', 'cipher_line', 'cipher_raw'])
        w.writerows(pairs)
    a, k = os.path.join(d, 'a.tsv'), os.path.join(d, 'k.tsv')
    subprocess.run([sys.executable, TOOL, 'align', p, a, k] + list(opts), check=True, capture_output=True)
    with open(k) as f:
        return {r['value']: r for r in csv.DictReader(f, delimiter='\t')}


def main():
    # letters 1-120 one letter each, 150 = a name; a clear word "le" written in the cipher line
    pairs = [
        ['1', 'que le conte jean est ici', '1', '16 36 81 le 150 85 26 31 101 71 101'],
        ['2', 'car le conte jean part', '2', '71 61 21 le 150 11 61 21 31'],
        ['3', 'et le conte jean vient', '3', '81 31 le 150 41 101 82 2 31'],
    ]
    key = run(pairs, '--floor', '121', '--clear-consumes')
    assert key['150']['meaning'] == 'contejean', key['150']
    assert int(key['150']['agree']) == 3, key['150']
    assert key['16']['meaning'] == 'q', key['16']
    # without --clear-consumes the clear 'le' takes nothing, so 150 absorbs it at least once
    key0 = run(pairs, '--floor', '121')
    assert key0['150']['meaning'] != 'contejean' or int(key0['150']['agree']) < 3
    # --prior seeds letters below the floor only; a seeded name code in the key file is ignored
    import tempfile as tf
    kp = os.path.join(tf.mkdtemp(), 'k.tsv')
    open(kp, 'w').write('code\tvalue\n16\tq\n36\tu\n81\te\n150\tzzz\n')
    key2 = run(pairs, '--floor', '121', '--clear-consumes', '--prior', kp)
    assert key2['150']['meaning'] == 'contejean', key2['150']

    # --code-prefix (26 Sept 2026, AX2-BRO4): a homophonic single-letter codebook mixing digit and
    # alpha codes, one clear word thrown in. Code 'x' (masked out of --prior) recovers 'c' from the
    # two sentences that both start with 'c', via the digit codes seeded around it.
    cp_pairs = [
        ['1', 'certo el', '1', '@x @2 @3 @1 @4 el'],
        ['2', 'corte', '2', '@x @4 @3 @1 @2'],
        ['3', 'trote', '3', '@1 @3 @4 @1 @2'],
    ]
    kp2 = os.path.join(tempfile.mkdtemp(), 'k.tsv')
    open(kp2, 'w').write('code\tvalue\n1\tt\n2\te\n3\tr\n4\to\n')
    key3 = run(cp_pairs, '--code-prefix', '@', '--clear-consumes', '--prior', kp2)
    assert key3['x']['meaning'] == 'c', key3['x']
    assert key3['1']['meaning'] == 't', key3['1']
    assert key3['4']['meaning'] == 'o', key3['4']
    print('ok')


if __name__ == '__main__':
    main()
