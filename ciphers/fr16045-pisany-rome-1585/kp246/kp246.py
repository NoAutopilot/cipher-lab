#!/usr/bin/env python3
"""Pre-registered test kp246 (kp246/PREREG_kp246.md, PIS-246): kp86d/kp86d.py run UNCHANGED (same statistic, nulls,
seeds, arms A/B, positive control, gate) on the half-page passes of f.246r (tx246/) against the Colbert copy p.52 l.15 - p.54 l.16 for f.246r
(kp246/colbert_f246r.txt). kp86d.main() reads its copy text as HERE/colbert_p121_123.txt and writes HERE/kp86d_result.json;
this wrapper (as kp86e.py did) saves the committed kp86d result first, points kp86d's module-level `open` at
kp246/colbert_f246r.txt for that one filename only, sets kp86d.CLEAR_IN_MS to the in-clear phrase on f.246r (empty if
none, given with --inms), runs kp86d.main(), moves the output to kp246/kp246_result.json and restores kp86d's file.
    python3 kp246/kp246.py --err E [--inms "phrase"]   (tokens tx246/ciphertext_f246r.tsv, extra tx246/passA/passB)"""
import builtins, os, shutil, sys
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(T, 'kp86d'))
import kp86d
args = sys.argv[1:]; inms = ''
if '--inms' in args:
    i = args.index('--inms'); inms = args[i + 1]; del args[i:i + 2]
COPY = os.path.join(HERE, 'colbert_f246r.txt')


def _open(path, *a, **k):
    if os.path.basename(str(path)) == 'colbert_p121_123.txt':
        path = COPY
    return builtins.open(path, *a, **k)


kp86d.open = _open
kp86d.CLEAR_IN_MS = inms if inms else '\x00'   # '\x00' never occurs in the copy: nothing removed
D = os.path.join(T, 'kp86d', 'kp86d_result.json'); SAVE = D + '.save'
shutil.copyfile(D, SAVE)
try:
    sys.argv = [sys.argv[0]] + args + ['--tokens', 'tx246/ciphertext_f246r.tsv',
                                       '--extra', 'tx246/passA.tsv', 'tx246/passB.tsv']
    kp86d.main()
    shutil.move(D, os.path.join(HERE, 'kp246_result.json'))
finally:
    shutil.move(SAVE, D)
