"""A2-HAR4 (2 Oct 2026): rerun run_nexthar.py (NEXT-HAR) with the gloss-derived constraints that A2-HAR3 reported
for the R8491 f.84r / R8494 f.90r period glosses: chi = y, delta/8 in {c,d}, L = e, - = b. L = e and - = b are
already in NEXT-HAR's sets, so the two changes are '8' -> 'cd' and the chi sign -> y. The chi sign is taken to be
Bourdeau's 'X' (his i); that identification and the constraints themselves come from A2-HAR3's session summary only:
its glyph table was never pushed, so they are grade I here, not C. Two variants:
  replace - X = 'y'  (chi = y read as a correction of X = i)
  add     - X = 'iy' (y added as an alternative)
The controls are NEXT-HAR's (shuffled-in-place null; Cobham clear words enciphered with the same, changed sets, at
0-40 % sign error), so target, null and known-answer all use one inventory.
    python3 run_har4.py --variant replace|add [--check]
--check exits 1 if out_har4_<variant>.txt differs from a fresh run (rule 7).
"""
import argparse, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import solve, run_nexthar

ap = argparse.ArgumentParser()
ap.add_argument('--variant', choices=('replace', 'add'), required=True)
ap.add_argument('--check', action='store_true')
a = ap.parse_args()
solve.SETS['8'] = 'cd'
solve.SETS['X'] = 'y' if a.variant == 'replace' else 'iy'
sys.argv = [sys.argv[0], '--out', os.path.join(HERE, f'out_har4_{a.variant}.txt')] + (['--check'] if a.check else [])
run_nexthar.main()
