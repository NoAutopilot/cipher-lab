#!/usr/bin/env python3
"""Offline test for tools/crib_rounds.py: a 300-letter Italian control (fixture Vanzolini chars 150000-150500, held out of the
corpus), K=24 (6 restarts x 60000). Round 0 runs blind; round 1 fixes 4 true cribs and 1 false one; --score must count them 4 right,
1 wrong, and the blind round must read the control at >= 60 percent."""
import json, os, subprocess, sys, tempfile
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
T = os.path.join(R, 'tools', 'crib_rounds.py')
FX = os.path.join(R, 'tools', 'tests', 'fixtures', 'crib_rounds_it300.txt')
C = [os.path.join(R, 'tools', 'data', 'it16', f) for f in
     ('alcuneletteredip00ferr.txt', 'delleletterefam02seghgoog.txt', 'lettereinedited00tassgoog.txt')]
with tempfile.TemporaryDirectory() as d:
    args = [sys.executable, T, '--dir', d]
    subprocess.run(args + ['--control', FX, '--signs', '24', '--length', '300', '--restarts', '6',
                           '--iters', '60000'] + sum((['--corpus', c] for c in C), []), check=True,
                   stdout=subprocess.DEVNULL)
    assert os.path.exists(os.path.join(d, 'round0.txt'))
    truth = json.load(open(os.path.join(d, 'hidden.json')))['truth']  # the test may look; a reader may not
    signs = sorted(truth)
    good = signs[:4]
    bad = signs[4]
    wrong_letter = 'z' if truth[bad] != 'z' else 'x'
    cf = os.path.join(d, 'cribs.txt')
    open(cf, 'w').write(','.join(f'{s}={truth[s]}' for s in good) + f'\n{bad}={wrong_letter}  # false crib\n')
    subprocess.run(args + ['--round', '1', '--cribs', cf], check=True, stdout=subprocess.DEVNULL)
    r1 = json.load(open(os.path.join(d, 'round1.json')))
    assert all(r1['key'][s] == truth[s] for s in good) and r1['key'][bad] == wrong_letter
    assert '   0 ' in subprocess.run(args + ['--view', '1'], check=True, capture_output=True, text=True).stdout
    out = subprocess.run(args + ['--score'], check=True, capture_output=True, text=True).stdout
    rows = [l.split('\t') for l in open(os.path.join(d, 'scores.tsv')).read().split('\n')[1:] if l]
    r0, r1s = rows
    assert float(r0[2]) >= 60, out
    assert (r1s[5], r1s[6], r1s[7]) == ('5', '4', '1'), out
    assert 'hidden' not in out and not any(c.isalpha() and len(c) == 1 for c in out.split()), out
    print('ok', out.strip().replace('\n', ' | '))
