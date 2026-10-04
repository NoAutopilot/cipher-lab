#!/usr/bin/env python3
"""Pre-registered test kp86g (kp86g/PREREG_kp86g.md, PIS1-247): kp86d/kp86d.py run UNCHANGED (same statistic, nulls,
seeds, arms A/B, positive control, gate) on the per-line passes of f.247r (tx86g/) against the Colbert copy of f.247r
(kp86g/colbert_f247r.txt). kp86d.main() reads its copy text as HERE/colbert_p121_123.txt and writes HERE/kp86d_result.json;
this wrapper (as kp86e.py did) saves the committed kp86d result first, points kp86d's module-level `open` at
kp86g/colbert_f247r.txt for that one filename only, sets kp86d.CLEAR_IN_MS to the in-clear phrase on f.247r (empty if
none, given with --inms), runs kp86d.main(), moves the output to kp86g/kp86g_result.json and restores kp86d's file.
    python3 kp86g/kp86g.py --err E [--inms "phrase"]   (tokens tx86g/ciphertext_f247r.tsv, extra tx86g/passA/passB)"""
import builtins, os, shutil, sys
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(T, 'kp86d'))
import kp86d
args = sys.argv[1:]; inms = ''
if '--inms' in args:
    i = args.index('--inms'); inms = args[i + 1]; del args[i:i + 2]
COPY = os.path.join(HERE, 'colbert_f247r.txt')


def _open(path, *a, **k):
    if os.path.basename(str(path)) == 'colbert_p121_123.txt':
        path = COPY
    return builtins.open(path, *a, **k)


kp86d.open = _open
kp86d.CLEAR_IN_MS = inms if inms else '\x00'   # '\x00' never occurs in the copy: nothing removed
D = os.path.join(T, 'kp86d', 'kp86d_result.json'); SAVE = D + '.save'
shutil.copyfile(D, SAVE)
try:
    sys.argv = [sys.argv[0]] + args + ['--tokens', 'tx86g/ciphertext_f247r.tsv',
                                       '--extra', 'tx86g/passA.tsv', 'tx86g/passB.tsv']
    kp86d.main()
    shutil.move(D, os.path.join(HERE, 'kp86g_result.json'))
finally:
    shutil.move(SAVE, D)
