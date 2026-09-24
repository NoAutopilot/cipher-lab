#!/usr/bin/env python3
"""Offline test for tools/print_check.py (no network; writes only to a temporary folder).
Uses the Bowes correspondence djvu text already in the repo (ciphers/bowes-walsingham-1583/corpus/, IA identifier
correspondenceof00bowerich):
1. a phrase printed in it ('delay in hearing from those persons') -> exact hit;
2. the same phrase in early-modern spelling ('delay in hearing from thoſe perſons' with v/u folding) -> exact hit;
3. a phrase with one OCR-broken word inserted -> proximity hit, no exact hit;
4. a phrase not in it -> 'no hits';
5. network sources in --offline mode are logged, not requested.
Run: python3 tools/tests/test_print_check.py"""
import contextlib, io, os, shutil, sys, tempfile
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import print_check as pc

fails = 0
def check(ok, what):
    global fails
    fails += not ok
    print('PASS' if ok else 'FAIL', what)

tmp = tempfile.mkdtemp()
try:
    open(os.path.join(tmp, 'phrases.txt'), 'w').write(
        '# test phrases\ndelay in hearing from those persons\ndelay in hearing from thoſe perſons\n'
        'delay in hearing from those persons with whom he had communicated\n'
        'the quick brown fox of the Tuileries\n')
    open(os.path.join(tmp, 'sources.tsv'), 'w').write('ia\tcorrespondenceof00bowerich\tBowes 1842\ngbooks\tabc123\n')
    with contextlib.redirect_stdout(io.StringIO()):
        rows = pc.main([tmp, '--offline', '--cache', os.path.join(tmp, 'cache')])
    ia = {r[0]: r[2] for r in rows if r[1] == 'ia:correspondenceof00bowerich'}
    check(ia['delay in hearing from those persons'].endswith('exact'), 'printed phrase: exact hit')
    check(ia['delay in hearing from thoſe perſons'].endswith('exact'), 'long-s spelling folds to the same hit')
    check('near' in ia['delay in hearing from those persons with whom he had communicated'],
          'phrase across "(Bowes)" and OCR noise: proximity hit')
    check(ia['the quick brown fox of the Tuileries'] == 'no hits', 'absent phrase: no hits')
    net = [r for r in rows if r[1] in ('ia-global', 'gbooks', 'openalex', 'crossref')]
    check(net and all('offline' in r[2] for r in net), 'network checks skipped and logged in --offline')
    hosts = open(os.path.join(tmp, 'print-check-hosts.tsv')).read()
    check('(offline)' in hosts and os.path.exists(os.path.join(tmp, 'print-check.tsv')), 'print-check.tsv and host log written')
finally:
    shutil.rmtree(tmp)
print('print_check:', 'all tests pass' if not fails else f'{fails} failures')
sys.exit(1 if fails else 0)
