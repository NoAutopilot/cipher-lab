#!/usr/bin/env python3
"""Offline test for tools/cipher_page_detector.py. No network, no other tool.

Fixtures (tools/tests/fixtures/, under 200 KB total, generated once and committed):
cipher_dense.jpg / cipher_sparse.jpg: synthetic pages of short, widely-spaced
isolated blocks (numeral-group / invented-sign layout).
plain_cursive.jpg / plain_printed.jpg: synthetic pages of long connected runs
(word-like layout), no isolated small tokens.
"""
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(HERE, "..", "cipher_page_detector.py")
FIXTURES = os.path.join(HERE, "fixtures")

sys.path.insert(0, os.path.join(HERE, ".."))
from cipher_page_detector import load_gray, extract_features, FEATURE_NAMES  # noqa: E402

CIPHER_FIXTURES = ["cipher_dense.jpg", "cipher_sparse.jpg"]
PLAIN_FIXTURES = ["plain_cursive.jpg", "plain_printed.jpg"]

failures = []


def check(cond, msg):
    if not cond:
        failures.append(msg)
        print(f"FAIL: {msg}")
    else:
        print(f"ok: {msg}")


def test_fixtures_present():
    total = 0
    for name in CIPHER_FIXTURES + PLAIN_FIXTURES:
        path = os.path.join(FIXTURES, name)
        check(os.path.isfile(path), f"fixture exists: {name}")
        total += os.path.getsize(path)
    check(total < 200_000, f"fixtures under 200 KB total (got {total} bytes)")


def test_feature_separation():
    """small_token_ink_fraction must separate short-isolated-token pages from
    long-connected-run pages: this is the layout signal the brief asks for."""
    cipher_vals = []
    plain_vals = []
    for name in CIPHER_FIXTURES:
        gray = load_gray(os.path.join(FIXTURES, name))
        feats = extract_features(gray)
        check(set(feats.keys()) == set(FEATURE_NAMES), f"{name}: full feature set present")
        cipher_vals.append(feats["small_token_ink_fraction"])
    for name in PLAIN_FIXTURES:
        gray = load_gray(os.path.join(FIXTURES, name))
        feats = extract_features(gray)
        plain_vals.append(feats["small_token_ink_fraction"])
    check(min(cipher_vals) > max(plain_vals),
          f"cipher fixtures' small_token_ink_fraction {cipher_vals} "
          f"all exceed plain fixtures' {plain_vals}")


def test_fit_and_score_roundtrip():
    """--fit on the 4 fixtures (2 train, 2 holdout) produces a weights file
    that --score can load and use; exercises the full CLI, offline."""
    with tempfile.TemporaryDirectory() as td:
        labels_path = os.path.join(td, "labels.tsv")
        weights_path = os.path.join(td, "weights.json")
        with open(labels_path, "w") as f:
            f.write("path\tlabel\tsplit\n")
            f.write(f"{os.path.join(FIXTURES, 'cipher_dense.jpg')}\tcipher\ttrain\n")
            f.write(f"{os.path.join(FIXTURES, 'plain_cursive.jpg')}\tplain\ttrain\n")
            f.write(f"{os.path.join(FIXTURES, 'cipher_sparse.jpg')}\tcipher\tholdout\n")
            f.write(f"{os.path.join(FIXTURES, 'plain_printed.jpg')}\tplain\tholdout\n")
        r = subprocess.run(
            [sys.executable, TOOL, "--fit", labels_path, "--weights", weights_path],
            capture_output=True, text=True)
        check(r.returncode == 0, f"--fit exits 0 (stderr: {r.stderr[-500:]})")
        check(os.path.isfile(weights_path), "--fit writes weights file")
        check("gate" in r.stdout, "--fit reports the gate verdict")

        r2 = subprocess.run(
            [sys.executable, TOOL, "--score", os.path.join(FIXTURES, "cipher_dense.jpg"),
             "--weights", weights_path],
            capture_output=True, text=True)
        check(r2.returncode == 0, f"--score exits 0 (stderr: {r2.stderr[-500:]})")
        parts = r2.stdout.strip().split("\t")
        check(len(parts) == 3, f"--score prints path/score/label (got {parts!r})")


def test_help():
    r = subprocess.run([sys.executable, TOOL, "--help"], capture_output=True, text=True)
    check(r.returncode == 0, "--help exits 0")
    check("numpy+PIL only" in r.stdout, "--help shows the tool docstring")


def main():
    test_fixtures_present()
    test_feature_separation()
    test_help()
    test_fit_and_score_roundtrip()
    if failures:
        print(f"\n{len(failures)} failure(s)")
        return 1
    print("\nall tests passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
