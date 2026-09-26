#!/usr/bin/env python3
"""Offline test for tools/crib_rounds.py: a 300-letter Italian control (fixture Vanzolini chars 150000-150500, held out of the
corpus), K=24 (6 restarts x 60000). Round 0 runs blind; round 1 fixes 4 true cribs and 1 false one; --score must count them 4 right,
1 wrong, and the blind round must read the control at >= 60 percent.
Nomenclator mode (ARM3-LOOP, 26 Sept 2026): a tiny-sweep control on the armstrong-madison-1808 shape; round 1 fixes 2 true
value=word cribs and 1 false; --score must count 2 right, 1 wrong, report particle and book classes and the top-30 floor
count, and print no word of the hidden plaintext; --view must show the crib mark."""
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
    # --cipher-tsv/--plain: reload the same control from files into a fresh dir; round 0 must match the original
    d2 = os.path.join(d, 'reload')
    subprocess.run([sys.executable, T, '--dir', d2, '--cipher-tsv', os.path.join(d, 'cipher.tsv'), '--plain',
                    os.path.join(d, 'hidden.json'), '--restarts', '6', '--iters', '60000'] +
                   sum((['--corpus', c] for c in C), []), check=True, stdout=subprocess.DEVNULL)
    assert json.load(open(os.path.join(d2, 'round0.json')))['decoded'] == \
        json.load(open(os.path.join(d, 'round0.json')))['decoded']
    print('ok --cipher-tsv reload')

# nomenclator mode: make (tiny sweeps), one crib round, score, view
SPEC = os.path.join(R, 'specs', 'armstrong-madison-1808.json')
MS = os.path.join(R, 'ciphers', 'armstrong-madison-1808', 'ciphertext_ms.txt')
if os.path.exists(SPEC) and os.path.exists(MS):
    with tempfile.TemporaryDirectory() as d:
        args = [sys.executable, T, '--family', 'nomenclator', '--dir', d]
        subprocess.run(args + ['--spec', SPEC, '--target-cipher', MS, '--seed', '7', '--restarts', '2', '--param', 'sweeps=1',
                               '--param', 'phase1=1', '--param', 'greedy=0'], check=True, stdout=subprocess.DEVNULL)
        st = json.load(open(os.path.join(d, 'state.json')))
        assert st['N'] == 353 and st['holdout'] == 5 and st['singletons'] == st['singletons_particle'] + st['singletons_book']
        hid = json.load(open(os.path.join(d, 'hidden.json')))  # the test may look; a reader may not
        truth = hid['truth']
        vs = sorted(truth, key=lambda v: (-int(v), v))
        good, bad = vs[:2], vs[2]
        cf = os.path.join(d, 'cribs.txt')
        open(cf, 'w').write(','.join(f'{v}={truth[v]}' for v in good) + f'\n{bad}=zzqqx  # false crib\n')
        subprocess.run(args + ['--round', '1', '--cribs', cf], check=True, stdout=subprocess.DEVNULL)
        r1 = json.load(open(os.path.join(d, 'round1.json')))
        assert all(r1['key'][v] == truth[v] for v in good) and r1['key'][bad] == 'zzqqx'
        view = subprocess.run(args + ['--view', '1'], check=True, capture_output=True, text=True).stdout
        assert f'{bad:>5}   1 zzqqx' in view and ' * |' in view, view[:500]
        out = subprocess.run(args + ['--score'], check=True, capture_output=True, text=True).stdout
        rows = [l.split('\t') for l in open(os.path.join(d, 'scores.tsv')).read().split('\n')[1:] if l]
        assert len(rows) == 2 and (rows[1][8], rows[1][9], rows[1][10]) == ('3', '2', '1'), out
        assert 'particle' in out and 'book' in out and 'top-30' in out
        report_words = {'round', 'blended', 'particle', 'book', 'top', 'repeated', 'values', 'right', 'cribs', 'new',
                        'wrong', 'total', 'none'}
        said = {w.strip('(),;:%>').lower() for w in out.split()} - report_words
        assert not (said & set(truth.values())), sorted(said & set(truth.values()))[:5]
        print('ok nomenclator mode', out.strip().replace('\n', ' | '))
