"""Offline test for tools/key_decode_lattice.py (no network, small synthetic language model)."""
import random
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import key_decode_lattice as K
from judge_plaintext import NgramModel

TEXT = "the cat sat on the mat and the dog sat on the log " * 60
KEY = {"A": "t", "B": "h", "C": "e", "D": "c", "E": "a", "F": "s", "G": "o", "H": "n", "X": "q"}


def lm():
    return K.LM(NgramModel([TEXT]))


def test_reader_mass_agree_and_split():
    nb = K.read_confusion(None)
    m = K.finish({**K.reader_mass({"sign_id": "A", "conf": "H"}, nb)})
    assert m == {"A": 1.0}
    mass = K.reader_mass({"sign_id": "A", "conf": "H"}, nb)
    for k, v in K.reader_mass({"sign_id": "B", "conf": "M"}, nb).items():
        mass[k] += v
    m = K.finish(mass)
    assert set(m) == {"A", "B"} and m["A"] > m["B"]


def test_confusion_neighbours_added():
    nb = {"A": {"X": 5.0}}
    m = K.finish(K.reader_mass({"sign_id": "A", "conf": "H"}, nb))
    assert m["A"] > m["X"] > 0


def test_align_skips_insertion():
    assert K.align(["A", "B", "C"], ["A", "Z", "B", "C"]) == {0: 0, 2: 1, 3: 2}


def test_viterbi_uses_language_when_priors_tie():
    # "thecat" with the 'a' sign ambiguous between a (E) and q (X): the 4-gram context "hec" must choose E
    lat = [(("L", i + 1), {s: 1.0}) for i, s in enumerate("ABCD")]
    lat += [(("L", 5), {"X": 0.5, "E": 0.5}), (("L", 6), {"A": 1.0})]
    seq, _ = K.viterbi(lat, KEY, lm(), lam=1.0)
    assert seq == ["A", "B", "C", "D", "E", "A"]


def test_viterbi_follows_prior_when_lam_large():
    lat = [(("L", 1), {"A": 1.0}), (("L", 2), {"X": 0.9, "B": 0.1}), (("L", 3), {"C": 1.0})]
    seq, _ = K.viterbi(lat, KEY, lm(), lam=50.0)
    assert seq == ["A", "X", "C"] and K.top1(lat) == ["A", "X", "C"]


def test_shuffled_key_keeps_values():
    k2 = K.shuffled(KEY, random.Random(3))
    assert sorted(k2.values()) == sorted(KEY.values()) and set(k2) == set(KEY)


def test_unknown_sign_does_not_crash():
    lat = [(("L", 1), {"?": 0.6, "A": 0.4}), (("L", 2), {"B": 1.0})]
    seq, _ = K.viterbi(lat, KEY, lm())
    assert len(seq) == 2


def test_split_cands_decrypt_convention():
    # TX-ALTS: 'a/b?' -> first a, alternative b, H capped at M; plain signs parse as before
    assert K.split_cands({"sign_id": "T18/T98?", "conf": "H"}) == ("T18", ["T98"], "M")
    assert K.split_cands({"sign_id": "T45/T89/T86?", "alt": "T90", "conf": "L"}) == ("T45", ["T89", "T86", "T90"], "L")
    assert K.split_cands({"sign_id": "T33", "alt": "T19", "conf": "H"}) == ("T33", ["T19"], "H")
    assert K.split_cands({"sign_id": "?", "conf": "L"}) == ("?", [], "L")


def test_keep_alts_exempts_alternatives_from_cut():
    # a weak alternative falls under the 0.02 floor / top-4 cut by default but survives with keep
    nb = {"A": {"B": 5.0, "C": 4.0, "D": 3.0}}
    keep = set()
    mass = K.reader_mass({"sign_id": "A/E?", "conf": "L"}, nb, keep)
    for _ in range(3):
        for k, v in K.reader_mass({"sign_id": "A", "conf": "H"}, nb).items():
            mass[k] += v
    assert keep == {"E"}
    assert "E" not in K.finish(mass)
    m = K.finish(mass, keep)
    assert "E" in m and abs(sum(m.values()) - 1) < 1e-9 and max(m, key=m.get) == "A"


def test_flip_mass_bayes_and_matrix_only(tmp_path=None):
    # TXE-E: read T98 is produced by true T98 (0.6) and by true T18 (0.3): the flip gives T18 1/3 of S x w
    M = {"T98": {"T98": 0.6, "T18": 0.3}}
    f = K.flip_mass("T98", 1.0, M, 0.3)
    assert abs(f["T18"] - 0.1) < 1e-9 and abs(f["T98"] - 0.2) < 1e-9
    m = K.finish(K.reader_mass({"sign_id": "T98", "conf": "H"}, {}, None, M, 0.3))
    assert max(m, key=m.get) == "T98" and m["T18"] > 0.02
    assert K.flip_mass("ZZ", 1.0, M, 0.3) == {}


def _write(path, text):
    open(path, "w").write(text)


def test_learn_confusion_counts_and_shuffle():
    import tempfile, os
    d = tempfile.mkdtemp()
    tr = os.path.join(d, "t.tsv"); pa = os.path.join(d, "a.tsv")
    T = lambda ln, sig, sets: "".join("%s\t%d\t%s\t%s\tx\tscored\n" % (ln, i + 1, a, b) for i, (a, b) in
                                      enumerate(zip(sig, sets)))
    R = lambda ln, sig: "".join("%s\t%d\t%s\t\tH\n" % (ln, i + 1, a) for i, a in enumerate(sig))
    _write(tr, "line\tpos\tref_sign\ttruth\tplain\tstatus\n" + T("p_L01", "ABABA", "ABABA")
           + T("p_L02", "ABCBA", ["A", "B", "C|D", "B", "A"]) + T("p_L03", "ABABA", "ABABA"))
    _write(pa, "passage\tpos\tsign_id\talt\tconf\n" + R("L01", "AAABA") + R("L02", "ABBBA") + R("L03", "BBBBB"))
    import tx_bench
    rows, st = K.learn_confusion([pa], tx_bench.read_tsv(tr), ["p_L01", "p_L02"], "p", ["A", "B", "C", "D"])
    assert st["lines"] == 2 and st["positions"] == 10 and st["misses"] == 2  # p_L03 (not named) is never counted
    P = {(t, r): p for _, t, r, p in rows}
    # true B: 4 reads, 1 as A -> (1 + .5) / (4 + 2); truth set C|D read B: 0.5 count each -> (.5 + .5) / (.5 + 2)
    assert abs(P[("B", "A")] - 1.5 / 6) < 1e-9 and abs(P[("C", "B")] - 1.0 / 2.5) < 1e-9
    assert all(abs(sum(p for (t, r), p in P.items() if t == x) - 1) < 1e-9 for x in "ABCD")
    sh = K.shuffle_offdiag(rows, 3)
    for t in "ABCD":
        assert abs(sum(p for _, tt, r, p in sh if tt == t) - 1) < 1e-9
        assert [p for _, tt, r, p in sh if tt == t and r == t] == [P[(t, t)]]
    out = os.path.join(d, "m.tsv")
    K.write_matrix(rows, out, ["learnt from lines: p_L01"])
    assert open(out).readline().startswith("# learnt from lines: p_L01")
    M = K.read_matrix(out)
    assert abs(M[""]["A"]["B"] - P[("B", "A")]) < 1e-9


if __name__ == "__main__":
    for n, f in list(globals().items()):
        if n.startswith("test_"):
            f()
    print("ok")
