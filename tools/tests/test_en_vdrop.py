#!/usr/bin/env python3
"""Offline test for tools/data/en_vdrop/build_en_vdrop.py's transform_text() (25 Sept 2026, LANE B2 bMCC2).
No file I/O, no network. Checks: word-initial vowels are kept, word-internal vowels are dropped, single-
letter words and non-letter characters pass through unchanged, and case is preserved on kept letters.
Run: python3 tools/tests/test_en_vdrop.py"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools", "data", "en_vdrop"))
import build_en_vdrop as bv  # noqa: E402


def test_transform_text():
    assert bv.transform_text("encryption") == "encryptn"
    assert bv.transform_text("a") == "a"
    assert bv.transform_text("I am here") == "I am hr"
    assert bv.transform_text("Apple orange, banana!") == "Appl orng, bnn!"
    assert bv.transform_text("123 -- .") == "123 -- ."
    assert bv.transform_text("Aeiou") == "A"  # first letter kept, rest all vowels
    assert bv.transform_text("") == ""
    print("test_transform_text: OK")


if __name__ == "__main__":
    test_transform_text()
    print("ALL TESTS PASSED")
