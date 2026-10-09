"""Offline test for tools/key_decode_lattice.py (no network, small synthetic language model)."""
import os
import random
import tempfile
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


def test_stability_prior():
    """--stability (TXE-J): a box whose top-1 flips under jitter (stab 0.4) keeps the readers' candidates; a stable box
    (1.0) has its top-1 sharpened; boxes map to positions via box_pos (min over a 2:1 position); the shuffle control
    permutes the values only."""
    d = tempfile.mkdtemp()
    stab = os.path.join(d, "stab.tsv"); bp = os.path.join(d, "box_pos.tsv")
    with open(stab, "w") as f:
        f.write("line\tbox\tpos\tstab\n1\tb1\t1\t0.40\n1\tb2\t2\t1.00\n1\tb3\t3\t1.00\n1\tb4\t4\t0.20\n")
    with open(bp, "w") as f:
        f.write("sid\tline\tpos\top\nb1\tp_L01\t1\t1:1\nb2\tp_L01\t2\t1:1\nb3\tp_L01\t3\t2:1\nb4\tp_L01\t3\t2:1\n")
    st = K.read_stability(stab, bp)
    assert st == {("p_L01", 1): 0.4, ("p_L01", 2): 1.0, ("p_L01", 3): 0.2}
    rows = [("p_L01", 1, "A", 0.6), ("p_L01", 1, "B", 0.4), ("p_L01", 2, "C", 0.6), ("p_L01", 2, "D", 0.4),
            ("p_L01", 3, "E", 0.5), ("p_L01", 3, "F", 0.5), ("p_L01", 4, "G", 0.7), ("p_L01", 4, "H", 0.3)]
    out, n = K.apply_stability(rows, st, 0.6, 0.9)
    P = {(pos, c): p for _, pos, c, p in out}
    assert n == 1
    assert P[(1, "A")] == 0.6 and P[(1, "B")] == 0.4                 # doubtful tile: unchanged
    assert abs(P[(2, "C")] - 0.96) < 1e-9 and abs(P[(2, "D")] - 0.04) < 1e-9   # stable: sharpened, sums to 1
    assert P[(3, "E")] == 0.5 and P[(4, "G")] == 0.7                 # min over 2:1 is doubtful; unmapped unchanged
    sh = K.shuffle_stability(st, 1)
    assert sorted(sh.values()) == sorted(st.values()) and set(sh) == set(st)


def test_probs_top3_replaces_hml():
    """TXE2-CONF: --probs uses the reader's own top-3 distribution; a row without top3 keeps the H/M/L rule; '-' = one reader."""
    assert K.parse_top3({"top3": "T50:0.7, T92:0.2,T18:0.1"}) == {"T50": 0.7, "T92": 0.2, "T18": 0.1}
    assert K.parse_top3({"top3": ""}) == {} and K.parse_top3({}) == {}
    row = {"sign_id": "T50", "alt": "T92", "conf": "H", "top3": "T50:0.6,T92:0.3,T18:0.1"}
    m = K.reader_mass(row, {}, probs=True)
    assert abs(m["T50"] - 0.6) < 1e-9 and abs(m["T18"] - 0.1) < 1e-9
    assert K.reader_mass(row, {}) == K.reader_mass({k: v for k, v in row.items() if k != "top3"}, {})  # off: unchanged
    with tempfile.TemporaryDirectory() as d:
        pa = os.path.join(d, "a.tsv")
        with open(pa, "w") as f:
            f.write("passage\tpos\tsign_id\talt\tconf\ttop3\tnote\n")
            f.write("L01\t1\tT50\t\tM\tT50:0.5,T92:0.4,T18:0.1\t\n")
            f.write("L01\t2\tT11\t\tH\t\t\n")
        rows, st = K.from_passes(pa, None, None, {}, probs=True)
        P = {(pos, c): p for _, pos, c, p in rows}
        assert abs(P[(1, "T92")] - 0.4) < 1e-9 and P[(2, "T11")] == 1.0 and st["positions"] == 2


if __name__ == "__main__":
    for n, f in list(globals().items()):
        if n.startswith("test_"):
            f()
    print("ok")
