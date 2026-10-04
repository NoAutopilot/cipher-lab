#!/usr/bin/env python3
"""Put the f.101v sorter's tiny tiles in one pile, SMALL (LL-RECUT, 4 Oct 2026, as the Pisany build; owner: "they need to
be efficient"). Under 18 px tall or under 60 ink pixels; the owner pulls the real signs out and marks the rest "Not a letter".

    python3 ciphers/fr16106-vivonne-longlee-1579/sorter/small_pile.py   (reads signs.tsv, labels.tsv, pages/; writes labels_small.tsv)
"""
import sys
from pathlib import Path
H = Path(__file__).resolve().parent
sys.path.insert(0, str(H.parents[2] / 'tools'))
import sorter_recut  # noqa: E402
sorter_recut.small_pile(H, focus='focus.tsv')   # SMALL tiles leave the focus box
