#!/usr/bin/env python3
"""Offline test for tools/gallica_folio.py on manifests already in the repo (no network).
1. fr.20140 (btv1b52521512h, ciphers/fr20140-danzay-1557/manifest.json): folio 35 -> canvases f69 (35r) and f70 (35v),
   the leaf the Danzay workers confirmed by eye; the two offsets (k=0 to f100, k=1 from f101) and the duplicate '50v'
   label are reported; folio 1 recto -> f9 (range label '1-2r').
2. fr.16092 (ciphers/fr16092-maisse-1582/manifest.json, every label 'NP'): the two eye-checked anchors in its NOTES.md
   (canvas 30 = f.14, canvas 70 = f.21) are flagged inconsistent (slope far from 1 or 2).
Run: python3 tools/tests/test_gallica_folio.py"""
import contextlib, io, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import gallica_folio as gf

fails = 0
def check(ok, what):
    global fails
    fails += not ok
    print('PASS' if ok else 'FAIL', what)

def run(*args):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        r = gf.main(list(args))
    return r, buf.getvalue()

dz = os.path.join(ROOT, 'ciphers', 'fr20140-danzay-1557', 'manifest.json')
r, out = run('btv1b52521512h', '--manifest', dz, '--folio', '35')
check([(h['canvas'], h['label']) for h in r] == [(69, '35r'), (70, '35v')], 'fr.20140 folio 35 -> f69 35r, f70 35v')
check(r[0]['native'].endswith('/btv1b52521512h/f69/full/full/0/native.jpg'), 'native image URL')
check('INCONSISTENT: 2 offsets [0, 1]' in out and "DUPLICATE label '50v' on f100 and f101" in out,
      'fr.20140 offset change and duplicate 50v reported')
r, out = run('ark:/12148/btv1b52521512h', '--manifest', dz, '--folio', '1', '--side', 'r')
check([(h['canvas'], h['label']) for h in r] == [(9, '1-2r')], 'fr.20140 folio 1r -> f9 (range label 1-2r)')
mz = os.path.join(ROOT, 'ciphers', 'fr16092-maisse-1582', 'manifest.json')
r, out = run('btv1b90612993', '--manifest', mz, '--anchor', '30=14', '--anchor', '70=21')
check('0 with a folio label' in out and 'INCONSISTENT anchors' in out, 'fr.16092 all-NP labels; anchors 30=14, 70=21 flagged')
print('gallica_folio:', 'all tests pass' if not fails else f'{fails} failures')
sys.exit(1 if fails else 0)
