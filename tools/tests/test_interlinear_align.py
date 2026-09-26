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
    print('ok')


if __name__ == '__main__':
    main()
