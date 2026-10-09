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
        f.write("85\tcarmagnola\tname\tAB\tx\tn1\n")
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
    check(dw.key_row_value(key_rows, "n85") == "carmagnola", "key_row_value: nNN numeral lookup by exact sign text")
    check(dw.key_row_value(key_rows, "n99") == "_", "key_row_value: unmatched numeral -> _")
    check(dw.key_row_value(key_rows, "?") == "_", "key_row_value: '?' -> _")

    # 1b. MONT-4715B, 27 Sept 2026: nNN must be an exact match, not a substring match -- a 1-digit sign
    # (row 2, sign "1") must not resolve against an earlier row whose sign merely contains those digits
    # (row 1, sign "10"), the shape of key_vieuville_nevers.tsv's row 22 ('1'->r) vs row 3 ('10'->b).
    sub_key_path = os.path.join(tmp, "key_substring.tsv")
    with open(sub_key_path, "w") as f:
        f.write("sign\tvalue\tkind\tgrade\tsource\tnote\n")
        f.write("10\tb\tletter\tAB\tx\trow3-shape\n")
        f.write("1\tr\tletter\tAB\tx\trow22-shape\n")
    sub_key_rows, _ = dw.load_key(sub_key_path)
    check(dw.key_row_value(sub_key_rows, "n1") == "r",
          "key_row_value: nNN exact match -- '1' resolves to its own row, not the earlier '10' row (old substring bug)")
    check(dw.key_row_value(sub_key_rows, "n10") == "b",
          "key_row_value: nNN exact match still resolves the 2-digit sign to its own row")

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

    # --label-diffs (MQS-WITNESS-LABELS, 9 Oct 2026)
    W = dw.witness_words("Le Roy veut qu'il aille avec les Princes, et sans faute.")
    def labs(dec_text, names=None):
        items, _ = dw.label_diffs(dw.decode_chars(dec_text), W, names)
        return {(it["kind"], it["w"]): it["label"] for it in items}
    L = labs("L01\tle roy veut qu il aille avec les princes et sans faute")
    check(all(v == "equal" for v in L.values()), "label-diffs: identical text (word division ignored) is all equal")
    L = labs("le roi veut qu il aile auec les princes et sans faute")
    check(L[("word", 1)] == "spelling-only" and L[("word", 5)] == "spelling-only" and L[("word", 6)] == "spelling-only",
          "label-diffs: roy/roi, aille/aile, avec/auec are spelling-only (must catch)")
    L = labs("le loy veut qu il aille avec les princes et pas faute")
    check(L[("word", 1)] == "substitution" and L[("word", 10)] == "substitution",
          "label-diffs: one-letter roy/loy and sans/pas stay substitution (normalisation must NOT hide them)")
    L = labs("le roy veut qu il aille avec princes et sans faute")
    check(L[("word", 7)] == "omission", "label-diffs: a dropped word is an omission")
    L = labs("le roy veut qu il aille avec les princes et sans grande faute")
    check(("gap", 10) in L and L[("gap", 10)] == "addition", "label-diffs: an inserted word is an addition")
    L = labs("le roy veut qu il aille avec les [?[x]] et sans faute")
    check(L[("word", 8)] == "name/code", "label-diffs: an unread sign or code group against a word is name/code")
    L = labs("le roy veut qu il aille avec les prinses et sans faute", names={dw.full("Princes")})
    check(L[("word", 8)] == "name/code", "label-diffs: a --names word rendered otherwise is name/code")
    check(dw.decode_chars("L1\ta [/] b <null> 12 c") == ["a", "b", dw.CODE, "c"],
          "decode_chars: [/] and <..> dropped, numerals become one code mark")
    ab = os.path.join(tmp, "ab.tsv")
    with open(ab, "w") as f:
        f.write("abbrev\texpansion\nS.M.\tsa maieste\n")
    W2 = dw.witness_words("S.M. le veut", dw.load_abbrev(ab))
    check([lt for _, lt in W2] == ["sa", "maieste", "le", "veut"],
          "load_abbrev: 'S.M.' in the witness is expanded before word splitting (PX-BRODEC)")
    check(dw.load_abbrev(ab).get("sm") == "sa maieste", "load_abbrev: key compared after light()")

    # planted control: label accuracy above the label-shuffled null, one-letter substitutions never hidden
    text = ("le ruinant de reputation et de credit tant avec les huguenots du royaume qu avec les princes "
            "protestans et autres avec lesquels il a ses principales intelligences et de telle sorte")
    Wp = dw.witness_words(text)
    base = [ch for _, lt in Wp for ch in lt]
    r = dw.plant_control(base, Wp, seeds=3, per_class=2, shuffles=200, seed0=1)
    check(r["n"] > 0 and r["accuracy"] > r["null_p95"], "plant_control: accuracy above label-shuffled null p95")
    check(r["one_letter_hidden"] == 0, "plant_control: no one-letter substitution labelled spelling-only")
    check(all(dw.full(dw._spelling_variant(w, random.Random(3)) or w) == dw.full(w) for w in ("royaume", "princes")),
          "_spelling_variant: always undone by full()")

    # --criteria-scan: a lead, never a verdict; must not flag a plain courtesy sentence
    cr = dw.load_criteria(dw.CRITERIA_DEFAULT, "fr")
    hits = dw.criteria_scan("Je vous escris en chiffre ce qui suit. Je baise les mains de Vostre Majeste. "
                            "Il y a grand soupcon de trahison.", cr)
    ids = {k: h for k, _, h in hits}
    check(0 in ids and any(h.startswith("C1") for h in ids[0]), "criteria-scan: 'en chiffre' flags C1 (must catch)")
    check(1 not in ids, "criteria-scan: a courtesy sentence is not flagged (must NOT flag)")
    check(2 in ids and any(h.startswith("C3") for h in ids[2]), "criteria-scan: 'soupcon de trahison' flags C3")
    rc = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "decode_witness.py"), "--label-diffs"],
                        capture_output=True, text=True)
    check(rc.returncode == 2, "CLI: --label-diffs without --witness exits 2")

finally:
    shutil.rmtree(tmp)

print(f"\n{'ALL PASS' if fails == 0 else str(fails) + ' FAILURE(S)'}")
sys.exit(1 if fails else 0)
