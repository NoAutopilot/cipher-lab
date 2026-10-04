#!/usr/bin/env python3
"""Pre-registered test kp86e (kp86e/PREREG_kp86e.md, RUN5-PIS3): kp86d/kp86d.py run UNCHANGED (same statistic, nulls,
seeds, arms A/B, positive control, gate) on the per-line passes tx86e/. kp86d.py writes its result to
kp86d/kp86d_result.json; this wrapper saves the committed kp86d result first, runs kp86d.main(), moves the new output
to kp86e/kp86e_result.json and restores kp86d's file byte for byte.
    python3 kp86e/kp86e.py --err E   (tokens tx86e/ciphertext_f275r.tsv, extra tx86e/passA.tsv tx86e/passB.tsv)"""
import os, shutil, sys
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(T, 'kp86d'))
import kp86d
D = os.path.join(T, 'kp86d', 'kp86d_result.json'); SAVE = D + '.save'
shutil.copyfile(D, SAVE)
try:
    sys.argv = [sys.argv[0]] + sys.argv[1:] + ['--tokens', 'tx86e/ciphertext_f275r.tsv',
                                               '--extra', 'tx86e/passA.tsv', 'tx86e/passB.tsv']
    kp86d.main()
    shutil.move(D, os.path.join(HERE, 'kp86e_result.json'))
finally:
    shutil.move(SAVE, D)
