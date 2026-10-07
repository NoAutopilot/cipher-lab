#!/usr/bin/env python3
"""Gate G1 for the Duke's 1447 key (SFZ-D, 7 Oct 2026; pre-registered unchanged from SFZ-1, brief
.claude/briefs/runs/2026-10-07-acct2-st-rebuild-workers.md, Wave 2 S2). Imports ../amidani/g1.py's learn() and score()
(same alignment options, seed, 200 shuffles); only the unit list and output paths differ.
    python3 ciphers/sforza-italien1584-1447/duke/g1_duke.py [--check]
Writes gate_g1.tsv, key.tsv (pooled), key_<unit>.tsv, align_<unit>.tsv here.
"""
import os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'amidani'))
import g1  # noqa: E402

UNITS = [
    ('f8', 'ciphertext_f8.tsv', 'clear_f10.txt', None),
    ('f5', 'ciphertext_f5.tsv', 'clear_f7.txt', None),
]

if __name__ == '__main__':
    g1.HERE = HERE
    g1.UNITS = UNITS
    sys.exit(g1.main('--check' in sys.argv))
