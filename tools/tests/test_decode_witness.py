#!/usr/bin/env python3
"""Offline test for tools/decode_witness.py. Run: python3 tools/tests/test_decode_witness.py"""
import os
import random
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import decode_witness as dw

fails = 0


def check(ok, label):
    global fails
    fails += not ok
    print(("PASS" if ok else "FAIL"), label)


tmp = tempfile.mkdtemp()
try:
    key_path = os.path.join(tmp, "key.tsv")
    signs_path = os.path.join(tmp, "signs.tsv")
    plain_path = os.path.join(tmp, "plain.tsv")
    with open(key_path, "w") as f:
        f.write("# comment line, not counted\n")
        f.write("sign\tvalue\tkind\tgrade\tsource\tnote\n")
        f.write("circle\ta\tletter\tAB\tx\tr1\n")
        f.write("cross\ta\tletter\tAB\tx\tr2\n")
        f.write("tri\tb\tletter\tAB\tx\tr1\n")
        f.write("dot\tc\tletter\tAB\tx\tr1\n")
        f.write("star\tche\tword\tAB\tx\tw1\n")
        f.write("digits85\tcarmagnola\tname\tAB\tx\tn1\n")
    with open(signs_path, "w") as f:
        f.write("line\tpos\tkey_row\tshape_note\tconfidence\n")
        f.write("1\t1\t1\tx\tH\n")   # circle -> a
        f.write("1\t2\t3\tx\tH\n")   # tri -> b
        f.write("1\t3\t4\tx\tH\n")   # dot -> c
        f.write("1\t4\t5\tx\tH\n")   # star -> che
        f.write("1\t5\tn85\tx\tH\n")  # numeral -> carmagnola
        f.write("1\t6\t?\tunread\tL\n")  # unknown -> _
        f.write("2\t1\tn99\tx\tH\n")  # numeral with no matching row -> _
    with open(plain_path, "w") as f:
        f.write("line\ttext\tconfidence\n")
        f.write("1\tabc che carmagnola z\tH\n")

    # 1. key/signs/plain loading and key_row -> value resolution
    key_rows, letter_idxs = dw.load_key(key_path)
    check(len(key_rows) == 6 and key_rows[1]["value"] == "a", "load_key: 6 data rows, comment/header skipped")
    check(letter_idxs == [1, 2, 3, 4], "load_key: letter_idxs picks only kind=letter rows")
    check(dw.key_row_value(key_rows, "1") == "a", "key_row_value: integer row lookup")
    check(dw.key_row_value(key_rows, "n85") == "carmagnola", "key_row_value: nNN numeral lookup by sign text")
    check(dw.key_row_value(key_rows, "n99") == "_", "key_row_value: unmatched numeral -> _")
    check(dw.key_row_value(key_rows, "?") == "_", "key_row_value: '?' -> _")

    # 2. normalize: lower-case, letters only, j->i, v->u
    check(dw.normalize("Vado, Ivi!") == "uadoiui", "normalize: lower/strip/j-i/v-u")

    # 3. exact-match scoring: the constructed decode is a subsequence of the clerk text
    r = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "decode_witness.py"),
                         "--key", key_path, "--signs", signs_path, "--plain", plain_path,
                         "--shuffles", "5", "--seed", "1"], capture_output=True, text=True)
    check(r.returncode == 0, "CLI: exits 0 on well-formed input")
    check("16/17" in r.stdout or "16/" in r.stdout, "CLI: full-passage aligned-letter count as expected")
    check("rank 1 of 6" in r.stdout, "CLI: real key is at least as good as every shuffled key here")

    # 4. --key-rows-out: confirmed/contradicted counts
    kr_path = os.path.join(tmp, "key_rows.tsv")
    r2 = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "decode_witness.py"),
                          "--key", key_path, "--signs", signs_path, "--plain", plain_path,
                          "--shuffles", "3", "--seed", "1", "--key-rows-out", kr_path],
                         capture_output=True, text=True)
    check(r2.returncode == 0 and os.path.exists(kr_path), "CLI: --key-rows-out writes a file")
    kr_lines = open(kr_path).read().splitlines()
    row1 = [ln for ln in kr_lines if ln.startswith("1\t")][0]
    check(row1.split("\t")[3] == "1" and row1.split("\t")[4] == "0", "key_rows_out: row 1 (circle->a) confirmed once, never contradicted")

    # 5. --sample-lines restricts scoring to named lines
    r3 = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "decode_witness.py"),
                          "--key", key_path, "--signs", signs_path, "--plain", plain_path,
                          "--shuffles", "3", "--seed", "1", "--sample-lines", "1"],
                         capture_output=True, text=True)
    check("blind-check sample" in r3.stdout, "CLI: --sample-lines adds a blind-check sample block")

    # 6. malformed input: bad key_row exits non-zero with a clear message
    bad_signs = os.path.join(tmp, "signs_bad.tsv")
    with open(bad_signs, "w") as f:
        f.write("line\tpos\tkey_row\tshape_note\tconfidence\n1\t1\tabc\tx\tH\n")
    r4 = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "decode_witness.py"),
                          "--key", key_path, "--signs", bad_signs, "--plain", plain_path],
                         capture_output=True, text=True)
    check(r4.returncode == 2 and "malformed key_row" in r4.stderr, "CLI: malformed key_row exits 2")

    # 7. malformed input: missing column in key file
    bad_key = os.path.join(tmp, "key_bad.tsv")
    with open(bad_key, "w") as f:
        f.write("sign\tkind\n circle\tletter\n")
    r5 = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "decode_witness.py"),
                          "--key", bad_key, "--signs", signs_path, "--plain", plain_path],
                         capture_output=True, text=True)
    check(r5.returncode == 2, "CLI: key file missing 'value' column exits 2")

    # 8. malformed input: duplicate line id in plain file
    dup_plain = os.path.join(tmp, "plain_dup.tsv")
    with open(dup_plain, "w") as f:
        f.write("line\ttext\tconfidence\n1\tabc\tH\n1\tdef\tH\n")
    r6 = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "decode_witness.py"),
                          "--key", key_path, "--signs", signs_path, "--plain", dup_plain],
                         capture_output=True, text=True)
    check(r6.returncode == 2 and "duplicate line id" in r6.stderr, "CLI: duplicate plain-file line id exits 2")

    # 9. --help exits 0
    r7 = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "decode_witness.py"), "--help"],
                         capture_output=True, text=True)
    check(r7.returncode == 0 and "usage" in r7.stdout.lower(), "CLI: --help exits 0")

    # 10. shuffled control genuinely varies with a different seed (not a no-op)
    rng_a = random.Random(1)
    rng_b = random.Random(2)
    sa = dw.shuffled_key_rows(key_rows, letter_idxs, rng_a)
    sb = dw.shuffled_key_rows(key_rows, letter_idxs, rng_b)
    check(any(sa[i]["value"] != key_rows[i]["value"] for i in letter_idxs)
          or any(sa[i]["value"] != sb[i]["value"] for i in letter_idxs),
          "shuffled_key_rows: seeds 1 and 2 do not always produce the same permutation")
    same_multiset = sorted(sa[i]["value"] for i in letter_idxs) == sorted(key_rows[i]["value"] for i in letter_idxs)
    check(same_multiset, "shuffled_key_rows: letter-value multiset (homophone counts) preserved")
    check(all(sa[i]["value"] == key_rows[i]["value"] for i in (5, 6)),
          "shuffled_key_rows: word/name rows (5, 6) are never shuffled")

finally:
    shutil.rmtree(tmp)

print(f"\n{'ALL PASS' if fails == 0 else str(fails) + ' FAILURE(S)'}")
sys.exit(1 if fails else 0)
