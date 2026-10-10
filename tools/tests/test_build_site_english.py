#!/usr/bin/env python3
"""Offline test for research/mockups/site/build_site.py english_for (10 Oct 2026): item file names carry a running-number
prefix that shifts whenever readings are added (75 new items left 154 of 240 pages "English pending"). Must catch: an English
line written under an old number reaches its item after renumbering. Must NOT: give an item another item's line when two
names are the same once the number is gone (15 of 157 on 10 Oct 2026); such names stay pending.
Run: python3 tools/tests/test_build_site_english.py"""
import os
import sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "research", "mockups", "site"))
import build_site as S  # noqa: E402

S._cache["en"] = {"003-alpha-letter": [("L1", "o", "alpha english")],
                  "010-twin-name": [("L1", "o", "twin one")], "011-twin-name": [("L1", "o", "twin two")],
                  "020-exact": [("L1", "o", "exact english")]}
S._cache["per_stable"] = {"alpha-letter": 1, "twin-name": 2, "exact": 1, "solo-new": 1}
fails = 0
for name, want, why in [("045-alpha-letter", "alpha english", "renumbered item finds its line"),
                        ("020-exact", "exact english", "exact name wins"),
                        ("050-twin-name", None, "a name shared by two items stays pending"),
                        ("060-solo-new", None, "an item with no line stays pending")]:
    got = S.english_for(name)
    ok = (got[0][2] if got else None) == want
    fails += not ok
    print(("ok  " if ok else "FAIL") + f": {why}: {got[0][2] if got else None!r}")
print("PASS" if not fails else f"{fails} failure(s)")
sys.exit(1 if fails else 0)
