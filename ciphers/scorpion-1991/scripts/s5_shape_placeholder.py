#!/usr/bin/env python3
"""Shape-only placeholder for cryptogram 2 (S5): N tokens, K distinct, the flattest sign-count profile
(as many hapax as possible, the rest doubletons). NOT a transcription -- S5 has none settled (TRANSCRIPTION.md).
It exists only so tools/family_run.py --control-only reads N, K and a profile=target sign-count profile from it.
A2P4-SCORP3, 3 Oct 2026.  python3 s5_shape_placeholder.py N K > out.txt"""
import sys
n, k = int(sys.argv[1]), int(sys.argv[2])
pairs = n - k                      # signs used twice; k - pairs used once
toks = [f"s{i}" for i in range(k)] + [f"s{i}" for i in range(pairs)]
assert len(toks) == n and len(set(toks)) == k
print(" ".join(toks))
