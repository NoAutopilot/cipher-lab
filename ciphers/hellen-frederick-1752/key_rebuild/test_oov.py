#!/usr/bin/env python3
"""Offline test (no corpus) of test_sibling.pmi_from's oov_floor switch (N5-HEL7, 4 Oct 2026). Exit 0 = pass."""
import os, sys, math, collections
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sibling_michell'))
import test_sibling as ts
u = collections.Counter({'le': 50, 'roi': 10, 'de': 40}); b = collections.Counter({('le', 'roi'): 8})
fl = math.log(0.3)
new = ts.pmi_from(u, b, oov_floor=True); old = ts.pmi_from(u, b)
assert abs(new('zzz', 'roi') - fl) < 1e-12, 'OOV left word must score at the floor'
assert abs(new('de', 'roi') - fl) < 1e-12, 'unseen pair must score at the floor'
assert new('le', 'roi') > fl, 'seen pair must score above the floor'
assert old('zzz', 'roi') == 0.0, 'default mode keeps the old 0'
assert old('le', 'roi') == new('le', 'roi')
print('test_oov: OK')
