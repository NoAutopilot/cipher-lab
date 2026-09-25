"""Offline test (25 Sept 2026, LANE B2): tools/judge_plaintext.py fails closed when the judge block carries no content
check (length only) or names a language code with no corpus wired. Before this, specs/mccormick-1999.json's block
(letters_min/max only) PASSed a letter-salad decode."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import judge_plaintext as jp

def test_length_only_fails():
    r = jp.judge({"judge": {"letters_min": 5, "letters_max": 100}}, "qxzv kwpt hhrm lrrn")
    assert not r["pass"] and not r["checks"]["content"]["pass"], r

def test_unwired_language_fails():
    r = jp.judge({"judge": {"language": "zz-none", "letters_min": 5}}, "qxzv kwpt hhrm lrrn")
    assert not r["pass"] and not r["checks"]["language"]["pass"], r

def test_crib_only_block_still_judged_by_crib():
    r = jp.judge({"judge": {"cribs": ["HELLO"]}}, "xx hello xx")
    assert r["pass"] and "content" not in r["checks"], r

if __name__ == "__main__":
    test_length_only_fails(); test_unwired_language_fails(); test_crib_only_block_still_judged_by_crib(); print("ok")
