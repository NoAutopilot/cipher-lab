#!/usr/bin/env python3
"""Offline test for tools/homophonic_anneal.py: a matched control (German 1562 plaintext from
ciphers/august-van-saksen-1561-64/align_74.txt, N=282, K=20, w as uu) must be read at >= 90 percent."""
import os, re, subprocess, sys, tempfile, json
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
D = os.path.join(R, 'ciphers', 'august-van-saksen-1561-64')
words = []
for l in open(os.path.join(D, 'align_74.txt'), encoding='utf-8'):
    if l.startswith('#') or ':' not in l:
        continue
    for w in l.split(':', 1)[1].split(';;'):
        if '|' in w:
            words.append(w.split('|')[1].replace(' ', ''))
with tempfile.TemporaryDirectory() as t:
    p = os.path.join(t, 'ctl.txt'); open(p, 'w').write(' '.join(words))
    o = os.path.join(t, 'o.json')
    subprocess.run([sys.executable, os.path.join(R, 'tools', 'homophonic_anneal.py'), '--control', p, '--signs', '20',
                    '--length', '282', '--corpus', os.path.join(R, 'tools', 'data', 'de16', 'composed_enhg.txt'),
                    '--corpus', os.path.join(D, 'plaintext_98.txt'), '--restarts', '3', '--iters', '200000',
                    '--w-as-uu', '--out', o], check=True, stdout=subprocess.DEVNULL)
    share = json.load(open(o))['share']
    assert share >= 0.9, share
    print('ok', share)
