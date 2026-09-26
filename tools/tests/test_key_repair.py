#!/usr/bin/env python3
"""Offline test for tools/key_repair.py (LANE AX2, AX2-4612S, 26 Sept 2026). Uses a small hand-built
fake n-gram model (no real fr16 corpus, no 12s model build) so the algorithm -- candidate generation,
the whole-stream score, the margin gate, the round sweep, the repaired-key TSV output -- is exercised
in well under a second, fully offline."""
import csv
import os
import sys
import tempfile

R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(R, "tools"))
import key_repair as kr  # noqa: E402
import decode_key as dk  # noqa: E402


# ---------------------------------------------------------------- fold()

assert kr.fold("vre.") == "VRE."
assert kr.fold("j") == "I"
assert kr.fold("u") == "V"
assert kr.fold("w") == "VV"
assert kr.fold("élection") == "ELECTION"  # accent stripped
print("ok fold")

# ---------------------------------------------------------------- corpus_ngrams

words = ["DE", "DE", "DE", "LE", "LE", "XY"]  # concatenated with no separator: 'DEDEDELELEXY'
grams2 = kr.corpus_ngrams(words, 2, 3)
# DE: 3 (unambiguous top). Then ED/EL/LE each occur twice (2 word-internal LE plus boundary EL/ED
# from the concatenation), tied -- broken alphabetically: ED < EL < LE.
assert grams2 == ["de", "ed", "el"], grams2
print("ok corpus_ngrams top bigram + alphabetical tie-break:", grams2)

# tie-break is alphabetical: two grams with equal count, 'AA' sorts before 'BB'
tied = kr.corpus_ngrams(["AABB"], 2, 3)  # bigrams AA, AB, BB each once
assert tied == ["aa", "ab", "bb"], tied
print("ok corpus_ngrams tie-break alphabetical")

# ---------------------------------------------------------------- build_template / build_stream

CIPHERTEXT = """line\tposition\tsign\tconfidence\talt\twhy
L1\t1\t=Je\tH\t\tagree
L1\t2\t1\tH\t\tagree
L1\t3\t2\tH\t\tagree
L1\t4\t?\tM\t\tunsettled
L1\t5\t3\tH\t\tagree
"""
with tempfile.TemporaryDirectory() as t:
    p = os.path.join(t, "ciphertext.tsv")
    open(p, "w", encoding="utf-8").write(CIPHERTEXT)
    recs = kr.load_ciphertext(p, "=", ["[blank]"])
    template = kr.build_template(recs)
    # 'line' row (kind='line') contributes nothing; '=Je' is fixed; codes 1,2,3 are ('sign', code);
    # the bare '?' row is kind='sign' with sign '?' -- present as a marker but never in any key,
    # so build_stream below must skip it via is_absent (its "value" lookup returns None).
    kinds = [k for k, _ in template]
    assert kinds == ["fixed", "sign", "sign", "sign", "sign"], kinds
    assert template[0] == ("fixed", "IE"), template[0]  # fold('Je') = 'IE'
    signs = [d for k, d in template if k == "sign"]
    assert signs == ["1", "2", "?", "3"], signs

    values = {"1": "n", "2": "NULL", "3": "e"}
    stream = kr.build_stream(template, values)
    # 'IE' + 'n' (code 1) + '' (code 2 is NULL) + '' (code '?' absent from values) + 'e' (code 3)
    assert stream == "IENE", stream
print("ok build_template/build_stream (clear context kept, NULL and unkeyed codes silent)")

# ---------------------------------------------------------------- candidate_values dedup + order

cv = kr.candidate_values(["a", "b", "a"], ["de", "a"], ["ent"])
assert cv == ["a", "b", "NULL", "de", "ent"], cv
print("ok candidate_values dedups, keeps first-seen order")


# ---------------------------------------------------------------- repair(): a fake scoring model


class FakeModel:
    """Scores a folded string by how many times a chosen target substring occurs -- lets a test
    fix in advance exactly which candidate value should win, without a real corpus."""

    def __init__(self, target, per_hit=10.0):
        self.target = target
        self.per_hit = per_hit

    def logp(self, s):
        n, hits, i = len(self.target), 0, 0
        while True:
            i = s.find(self.target, i)
            if i == -1:
                break
            hits += 1
            i += 1
        return self.per_hit * hits + 0.01 * len(s)  # small length term breaks exact ties deterministically


def make_template(pairs):
    """pairs: list of ('fixed', text) or ('sign', code) already folded/raw as build_stream expects."""
    return list(pairs)


# Code '9' should be repaired from its current wrong value 'x' to the bigram 'en', which is what
# actually appears around it in the (synthetic) surrounding clear text -- FakeModel rewards any
# stream containing 'ENVOYE' (as if the true plaintext were '...envoye...').
template = make_template([
    ("fixed", "ENVOY"),  # everything except the middle 'E' that code 9 should supply, then 'E' after
    ("sign", "9"),
    ("fixed", "E"),
])
key = {"9": {"value": "x", "grade": "M", "source": "test", "note": ""}}
model = FakeModel("ENVOYEE")  # only scores a hit if code 9 decodes to a value ending 'E' -> stream ENVOY+val+E
cand = kr.candidate_values(list("abcdefghijklmnopqrstuvwxyz"), ["en", "de", "le"], ["ent"])
values, changes, rounds_run = kr.repair(template, key, model, margin=3.0, rounds=4, cand_values=cand)
assert values["9"] == "e", values  # 'e' is the only single-letter candidate making ENVOY+E+E = ENVOYEE
assert len(changes) == 1 and changes[0][0] == "9" and changes[0][2] == "x" and changes[0][3] == "e", changes
assert rounds_run == 2, rounds_run  # round 1 changes x->e; round 2 finds no further change and stops
print("ok repair() finds the rewarded candidate and stops once nothing changes")

# Margin gate: same setup, but an absurdly high margin rejects the same improvement.
values2, changes2, _ = kr.repair(template, key, model, margin=1000.0, rounds=4, cand_values=cand)
assert values2["9"] == "x" and changes2 == [], (values2, changes2)
print("ok repair() respects --margin (a real improvement below the margin is rejected)")

# Determinism: two independent runs on the same inputs give byte-identical results.
values3, changes3, _ = kr.repair(template, key, model, margin=3.0, rounds=4, cand_values=cand)
assert values3 == values and changes3 == changes, (values3, changes3)
print("ok repair() is deterministic (repeat run matches)")

# A code that never occurs in the ciphertext is left untouched (frequency 0, not iterated).
key_extra = dict(key)
key_extra["99"] = {"value": "z", "grade": "H", "source": "elsewhere", "note": "unrelated"}
values4, changes4, _ = kr.repair(template, key_extra, model, margin=3.0, rounds=4, cand_values=cand)
assert values4["99"] == "z"
assert all(c[0] != "99" for c in changes4)
print("ok repair() never touches a code absent from this ciphertext")

# ---------------------------------------------------------------- write_key

with tempfile.TemporaryDirectory() as t:
    outp = os.path.join(t, "key_repair_out.tsv")
    kr.write_key(outp, key_extra, values4, changes4)
    rows = list(csv.DictReader(open(outp, encoding="utf-8"), delimiter="\t"))
    by_code = {r["code"]: r for r in rows}
    assert by_code["9"]["value"] == "e" and by_code["9"]["grade"] == "S"
    assert "key_repair.py" in by_code["9"]["source"]
    assert "'x' -> 'e'" in by_code["9"]["note"]
    # unchanged row passes through with its original grade/source/note, byte-for-byte on those fields
    assert by_code["99"]["value"] == "z" and by_code["99"]["grade"] == "H"
    assert by_code["99"]["source"] == "elsewhere" and by_code["99"]["note"] == "unrelated"
print("ok write_key: changed rows graded S with a note, unchanged rows pass through unmodified")

# ---------------------------------------------------------------- CLI smoke test (--help, exit 0)

import subprocess

r = subprocess.run([sys.executable, os.path.join(R, "tools", "key_repair.py"), "--help"],
                    capture_output=True, text=True)
assert r.returncode == 0 and "key_repair" not in r.stderr, r.stderr
assert "--margin" in r.stdout and "--rounds" in r.stdout
print("ok --help exits 0 and documents --margin/--rounds")

print("ALL OK")
