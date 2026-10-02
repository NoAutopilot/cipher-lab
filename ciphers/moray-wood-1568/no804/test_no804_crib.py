#!/usr/bin/env python3
"""Offline test for no804_crib.py (GAPS15-moray-wood-1568, 2 Oct 2026). No network.   python3 ciphers/moray-wood-1568/no804/test_no804_crib.py"""
import random, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import no804_crib as m  # noqa: E402

assert len(m.CRIBS) == 16 and all(40 <= len(c) <= 44 for c in m.CRIB_LET)
assert m.lcs("abcde", "ace") == 3 and m.lcs("a?c", "abc") == 2 and m.lcs("??", "??") == 0
assert m.decode(["U", "|", "o2", "4b", "A", "zz_unknown"]) == "theanda?"
rnd = random.Random(7)
clean = m.encipher(m.CRIBS[0], m.KEY, rnd)
r = m.run_test(clean, random.Random(1))
assert r["passed"] and r["S"] > 0.9, r          # the crib under key.tsv, no error, must pass
other = m.encipher(m.CRIBS[0], m.shuffled_key(random.Random(3)), random.Random(4))
assert not m.run_test(other, random.Random(1))["passed"]   # same phrase, a different key, must fail
assert not m.run_test(["A"] * 42, random.Random(1))["passed"]  # degenerate input must fail
tmp = Path(__file__).resolve().parent / "_selftest_input.tsv"
tmp.write_text("line\tpos\tsign\nL1\t1\t" + "\nL1\t1\t".join(clean) + "\n")
try:
    assert m.read_signs(tmp) == clean and m.main(["--score", str(tmp)]) == 0
finally:
    tmp.unlink(); (tmp.parent / "_selftest_input_no804.tsv").unlink(missing_ok=True)
print("test_no804_crib: OK")
