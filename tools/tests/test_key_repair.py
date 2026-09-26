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
values, changes, rounds_run = kr.repair(template, key, model.logp, margin=3.0, rounds=4, cand_values=cand)
assert values["9"] == "e", values  # 'e' is the only single-letter candidate making ENVOY+E+E = ENVOYEE
assert len(changes) == 1 and changes[0][0] == "9" and changes[0][2] == "x" and changes[0][3] == "e", changes
assert rounds_run == 2, rounds_run  # round 1 changes x->e; round 2 finds no further change and stops
print("ok repair() finds the rewarded candidate and stops once nothing changes")

# Margin gate: same setup, but an absurdly high margin rejects the same improvement.
values2, changes2, _ = kr.repair(template, key, model.logp, margin=1000.0, rounds=4, cand_values=cand)
assert values2["9"] == "x" and changes2 == [], (values2, changes2)
print("ok repair() respects --margin (a real improvement below the margin is rejected)")

# Determinism: two independent runs on the same inputs give byte-identical results.
values3, changes3, _ = kr.repair(template, key, model.logp, margin=3.0, rounds=4, cand_values=cand)
assert values3 == values and changes3 == changes, (values3, changes3)
print("ok repair() is deterministic (repeat run matches)")

# A code that never occurs in the ciphertext is left untouched (frequency 0, not iterated).
key_extra = dict(key)
key_extra["99"] = {"value": "z", "grade": "H", "source": "elsewhere", "note": "unrelated"}
values4, changes4, _ = kr.repair(template, key_extra, model.logp, margin=3.0, rounds=4, cand_values=cand)
assert values4["99"] == "z"
assert all(c[0] != "99" for c in changes4)
print("ok repair() never touches a code absent from this ciphertext")

# ------------------------------------------------ --no-null-below (candidates_for_code, repair())

cv_with_null = kr.candidate_values(["a", "b"], ["de"], ["ent"])
cv_no_null = [v for v in cv_with_null if v != "NULL"]
assert kr.candidates_for_code("63", cv_with_null, cv_no_null, None) == cv_with_null
assert kr.candidates_for_code("63", cv_with_null, cv_no_null, 121) == cv_no_null  # 63 < 121: no NULL
assert kr.candidates_for_code("130", cv_with_null, cv_no_null, 121) == cv_with_null  # 130 >= 121: NULL ok
assert kr.candidates_for_code("ii", cv_with_null, cv_no_null, 121) == cv_with_null  # non-numeric: unrestricted
print("ok candidates_for_code: numeric codes below the threshold lose NULL, others and non-numeric codes keep it")

# End-to-end, reproducing the AX2-4612S bug shape directly: a model that costs every character a
# uniform, context-free amount (so every candidate letter ties with the current value, and only
# NULL -- fewer characters -- can ever change the score) is exactly what "total log-probability of
# the decoded stream" degenerates to once every character's own log-probability is treated as an
# equally-weighted negative term.
class FlatCostModel:
    """logp = cost_per_char * len(s), no context sensitivity at all. bits_per_char (mean -log2 p
    per char on held-out text) is -cost_per_char, matching compute_mu()'s expectations."""

    def __init__(self, cost_per_char):
        self.cost_per_char = cost_per_char
        self.bits_per_char = -cost_per_char

    def logp(self, s):
        return self.cost_per_char * len(s)


flat_template = [("sign", "9")]
flat_key = {"9": {"value": "x", "grade": "M", "source": "test", "note": ""}}
flat_model = FlatCostModel(cost_per_char=-5.0)
flat_cand = kr.candidate_values(list("abcdefghijklmnopqrstuvwxyz"), [], [])

# 'total': every character is a uniformly negative term, so NULL (0 characters) always beats any
# single letter -- the AX2-4612S bug, reproduced exactly, independent of --no-null-below.
v_total, c_total, _ = kr.repair(flat_template, flat_key, flat_model.logp, margin=3.0, rounds=4,
                                 cand_values=flat_cand, no_null_below=None)
assert v_total["9"] == "NULL", v_total
print("ok repair() under --objective total deletes a uniformly-costed code to NULL (the AX2-4612S bug)")

# 'excess' on the same model: mu exactly equals the per-character cost (every character costs
# precisely the held-out average), so NULL no longer has any edge and the current value survives.
flat_mu = kr.compute_mu(flat_model)
flat_scorer = kr.make_scorer(flat_model, "excess", flat_mu)
v_excess, c_excess, _ = kr.repair(flat_template, flat_key, flat_scorer, margin=3.0, rounds=4,
                                   cand_values=flat_cand, no_null_below=None)
assert v_excess["9"] == "x" and c_excess == [], (v_excess, c_excess)
print("ok repair() under --objective excess does not delete the same code (the fix)")

# --no-null-below additionally forbids NULL for code '9' (< 121) even under the buggy 'total'
# objective, so the current value survives regardless of which objective is chosen.
v_blocked, c_blocked, _ = kr.repair(flat_template, flat_key, flat_model.logp, margin=3.0, rounds=4,
                                     cand_values=flat_cand, no_null_below=121)
assert v_blocked["9"] == "x" and c_blocked == [], (v_blocked, c_blocked)
print("ok repair() honours --no-null-below end to end even under the buggy 'total' objective")

# ------------------------------------------------------------------------------- --min-occ
# A code occurring fewer times than --min-occ is never tried, even with an overwhelmingly rewarding
# candidate sitting right there (FakeModel above: any stream containing 'ENVOYEE' scores +10).
low_occ_template = make_template([("fixed", "ENVOY"), ("sign", "9"), ("fixed", "E")])  # code '9' seen once
v_lowocc, c_lowocc, _ = kr.repair(low_occ_template, key, model.logp, margin=3.0, rounds=4,
                                   cand_values=cand, min_occ=3)
assert v_lowocc["9"] == "x" and c_lowocc == [], (v_lowocc, c_lowocc)  # count 1 < min_occ 3: untouched
v_default, c_default, _ = kr.repair(low_occ_template, key, model.logp, margin=3.0, rounds=4,
                                     cand_values=cand)  # min_occ defaults to 1: same code IS tried
assert v_default["9"] == "e" and len(c_default) == 1
print("ok repair() --min-occ skips a code seen fewer times than the threshold entirely")

# ---------------------------------------------------------- --objective paired (AX2-4612S3's fix)
# AX2-4612S2's own diagnosed bug, reproduced directly: a two-character candidate whose SUMMED excess
# gain beats the correct single letter's, even though its MEAN excess per character is lower --
# 'excess' (summed) accepts it, 'paired' (summed AND mean-per-char) rejects it.


class OrderedFakeModel:
    """order-0 character table (context ignored) exposing the .p(context, ch)/.order interface the
    'paired' objective's per-character mean check needs, alongside .logp/.bits_per_char for the
    ordinary excess-scorer machinery."""

    def __init__(self, table, bits_per_char, order=5):
        self.table = table  # ch -> log2 p(ch), a plain probability table (no context dependence)
        self.bits_per_char = bits_per_char
        self.order = order

    def p(self, h, ch):
        return 2 ** self.table[ch]

    def logp(self, s):
        return sum(self.table[ch] for ch in s)


# mu = -2.0. 'E' (current value): log2 p -1.0 -> excess +1.0 (mean +1.0, one character).
# 'A','N' (bigram candidate 'an', folds to 'AN'): log2 p -1.4 each -> excess +0.6 each; SUMMED
# 1.2 > single-E's 1.0 (the bug -- excess alone would swap 'e' for the bigram), but the bigram's
# MEAN +0.6 is below 'e's mean +1.0 (paired's second criterion correctly rejects it).
pair_table = {"E": -1.0, "A": -1.4, "N": -1.4, "X": -6.0}
pair_model = OrderedFakeModel(pair_table, bits_per_char=2.0)
pair_mu = kr.compute_mu(pair_model)
assert pair_mu == -2.0, pair_mu
pair_scorer = kr.make_scorer(pair_model, "excess", pair_mu)
pair_template = make_template([("sign", "9")])
pair_key = {"9": {"value": "e", "grade": "M", "source": "test", "note": ""}}
pair_cand = kr.candidate_values(["e", "x"], ["an"], [])

# Plain excess: the bigram's higher SUMMED excess wins -- the bug, reproduced on purpose.
v_excess_bug, c_excess_bug, _ = kr.repair(pair_template, pair_key, pair_scorer, margin=0.1, rounds=1,
                                           cand_values=pair_cand)
assert v_excess_bug["9"] == "an", v_excess_bug
assert len(c_excess_bug) == 1 and c_excess_bug[0][3] == "an"
print("ok --objective excess alone reproduces AX2-4612S2's bug (longer-but-worse-per-char wins)")

# paired: same margin, same candidates, but now the mean-per-char check blocks the swap.
v_paired_fix, c_paired_fix, _ = kr.repair(pair_template, pair_key, pair_scorer, margin=0.1, rounds=1,
                                           cand_values=pair_cand, pair_model=pair_model,
                                           pair_mu=pair_mu)
assert v_paired_fix["9"] == "e" and c_paired_fix == [], (v_paired_fix, c_paired_fix)
print("ok --objective paired rejects it (mean excess per char must also improve, not just the sum)")

# The reverse direction also holds: a single letter that IS better per character AND in total than
# the current (badly-scoring) value wins under both excess and paired (paired is strictly more
# restrictive than excess, never less -- it never accepts something excess alone would reject). No
# bigram candidate here, so there is nothing for a length-based bias to prefer over the single letter.
pair_key_rev = {"9": {"value": "xx", "grade": "M", "source": "test", "note": ""}}  # 'X' excess -4.0 each
pair_cand_rev = kr.candidate_values(["e", "x"], [], [])
v_rev, c_rev, _ = kr.repair(pair_template, pair_key_rev, pair_scorer, margin=0.1, rounds=1,
                             cand_values=pair_cand_rev, pair_model=pair_model, pair_mu=pair_mu)
assert v_rev["9"] == "e" and len(c_rev) == 1
print("ok --objective paired still accepts a candidate that wins on both the sum and the mean")

# ------------------------------------------------------------------- make_scorer / compute_mu


class FakeMuModel:
    """logp = sum of a fixed per-character table (order-0, so 'excess' vs 'total' is easy to reason
    about by hand); bits_per_char set directly, standing in for a real model's held-out measurement."""

    def __init__(self, table, bits_per_char):
        self.table = table
        self.bits_per_char = bits_per_char

    def logp(self, s):
        return sum(self.table[ch] for ch in s)


# Alphabet where 'E' is better-predicted than the held-out mean (mu=-2.0) and 'X' is worse.
m = FakeMuModel({"E": -1.0, "N": -1.0, "V": -1.0, "O": -1.0, "Y": -1.0, "X": -5.0}, bits_per_char=2.0)
mu = kr.compute_mu(m)
assert mu == -2.0, mu  # -bits_per_char
total_scorer = kr.make_scorer(m, "total")
excess_scorer = kr.make_scorer(m, "excess", mu)
assert total_scorer("ENVOY") == m.logp("ENVOY")  # 'total' is exactly the model's own logp
assert excess_scorer("E") == m.logp("E") - mu * 1  # -1.0 - (-2.0) = +1.0: better than average, a real bonus
assert excess_scorer("X") == m.logp("X") - mu * 1  # -5.0 - (-2.0) = -3.0: worse than average, a real penalty
assert excess_scorer("") == 0.0  # deleting everything scores exactly 0 under excess, never a free lunch
# Under 'total', deleting a well-predicted 'E' always looks better than keeping it (the AX2-4612S bug):
assert total_scorer("") > total_scorer("E")
# Under 'excess', keeping a better-than-average 'E' beats deleting it; only the below-average 'X' loses to NULL:
assert excess_scorer("E") > excess_scorer("")
assert excess_scorer("") > excess_scorer("X")
try:
    kr.make_scorer(m, "excess")
    raise AssertionError("excess without mu should raise")
except ValueError:
    pass
print("ok make_scorer/compute_mu: excess only rewards better-than-average characters, unlike total")

# ------------------------------------------------------- clean synthetic French text: 0 changes
# The brief's own required regression test: on a real fr16 model, a null control (repair run from an
# already-correct key) on ordinary, common French text should propose 0 changes under the excess
# objective -- unlike the old 'total' objective, which AX2-4612S found changed 100/110 codes on real
# 5811 text (almost all toward NULL). Built from very common French words/bigrams so every character
# is at least as predictable as the corpus-wide mean.
sys.path.insert(0, os.path.join(R, "tools"))
import french16_ngram as fr16  # noqa: E402

CLEAN_FRENCH = "que nous vous avons mande de la part de monseigneur pour ceste heure"
letters_used = sorted(set(ch for ch in CLEAN_FRENCH if ch != " "))
clean_key = {str(i): {"value": ch, "grade": "H", "source": "test", "note": ""}
             for i, ch in enumerate(letters_used, start=1)}
by_letter = {row["value"]: code for code, row in clean_key.items()}
clean_template = []
for ch in CLEAN_FRENCH:
    if ch != " ":
        clean_template.append(("sign", by_letter[ch]))

fr16_model = fr16.load()
fr16_mu = kr.compute_mu(fr16_model)
fr16_scorer = kr.make_scorer(fr16_model, "excess", fr16_mu)
fr16_corpus_words = list(fr16.corpus_words())
fr16_bigrams = kr.corpus_ngrams(fr16_corpus_words, 2, 60)
fr16_trigrams = kr.corpus_ngrams(fr16_corpus_words, 3, 20)
fr16_cand = kr.candidate_values(kr.ALPHA26, fr16_bigrams, fr16_trigrams)
clean_values, clean_changes, _ = kr.repair(clean_template, clean_key, fr16_scorer, margin=3.0,
                                            rounds=4, cand_values=fr16_cand, no_null_below=121)
assert clean_changes == [], clean_changes
print(f"ok null control on clean synthetic French text ({len(letters_used)} codes) proposes 0 "
      f"changes under --objective excess (mu={fr16_mu:.4f})")

# Same null control, under --objective paired (AX2-4612S3's own required regression test): paired
# is strictly more restrictive than excess (both criteria must hold, not just the summed one), so a
# null control clean under excess must also be clean under paired.
clean_values_p, clean_changes_p, _ = kr.repair(clean_template, clean_key, fr16_scorer, margin=3.0,
                                                rounds=4, cand_values=fr16_cand, no_null_below=121,
                                                pair_model=fr16_model, pair_mu=fr16_mu)
assert clean_changes_p == [], clean_changes_p
print("ok null control on the same clean synthetic French text proposes 0 changes under "
      "--objective paired too")

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
