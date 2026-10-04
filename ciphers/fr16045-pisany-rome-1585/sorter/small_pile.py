#!/usr/bin/env python3
"""Put the f.75 sorter's tiny tiles in one pile, SMALL (owner, 4 Oct 2026: "they need to be efficient").

    python3 ciphers/fr16045-pisany-rome-1585/sorter/small_pile.py     (reads signs.tsv, labels.tsv, pages/; writes labels_small.tsv)

A tile is small when it is under 18 px tall or carries under 60 ink pixels (ink = darker than the strip's 8th percentile
+ 20). On the 4 Oct v3 cut that is 99 of 1,290 tiles: mostly dots and specks, about ten real signs (thin strokes, a few
small letters), checked by eye on a montage. They are not dropped: the owner pulls the real ones out of SMALL and marks
the rest "Not a letter" in one go. Every other tile keeps its label."""
import sys
from pathlib import Path
H = Path(__file__).resolve().parent
sys.path.insert(0, str(H.parents[2] / 'tools'))
import sorter_recut  # noqa: E402  (shared since LL-RECUT, 4 Oct 2026)
sorter_recut.small_pile(H)
