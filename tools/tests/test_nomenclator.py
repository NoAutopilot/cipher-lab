#!/usr/bin/env python3
"""Offline test for tools/families/nomenclator.py (ARM-C1, 26 Sept 2026). No network; about a minute.

(1) make_control on the en18 corpora builds a letter with exactly the target's coded-token count, one plain word
    per cipher token, wildcards aligned, particle values under 100, book values 100-1899, held-out file removed
    from the training texts, per-class stats recorded;
(2) machinery check from the TRUE key (the solver's `_init` hook): greedy sweeps started at the truth keep
    particle recovery > 0.7, book recovery > 0.15 and blended > 0.4 (measured 26 Sept 2026 at 0.856 / 0.274 /
    0.591: under the blind en18 LM the truth is NOT a fixed point at N=369 -- the objective drifts most singleton
    book values, which is the control battery's own finding -- so these are drift bounds, not a ceiling), and a
    short blind solve runs end to end with a well-formed decode. This says nothing about blind power -- ARM-C1's
    own control battery measures that, and CLAUDE.md rule 3's Salviati warning is why no test here trains on
    the letter;
(3) score_recovery ignores wildcard positions and reports per class; split_decode keeps message lengths;
    `**`, `***` and `<..>` tokens are wildcards; (4) family_run.py lists the family and dry-runs the real spec.
Run: python3 tools/tests/test_nomenclator.py"""
import io, contextlib, os, subprocess, sys, time

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import judge_plaintext as jp  # noqa: E402
from families import nomenclator as nm  # noqa: E402


def test_nomenclator():
    t0 = time.time()
    corpora = [jp.read_corpus(str(p)) for p in jp.LANG_CORPORA["en18"]]
    assert len(corpora) == 6
    target = [l.split() for l in open(os.path.join(ROOT, "ciphers", "armstrong-madison-1808", "ciphertext.txt"))
              if l.strip() and not l.startswith("#")]
    n_coded = sum(1 for m in target for t in m if t.isdigit())
    params = {"N": 404, "K": 219, "target_msgs": target, "holdout": 5}
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        cm, plain, train = nm.make_control({}, 1, corpora, dict(params))
    assert len(train) == 5 and corpora[5] not in train
    toks, words = cm[0], plain.split()
    assert len(toks) == len(words)
    assert sum(t.isdigit() for t in toks) == n_coded == 369
    for t, w in zip(toks, words):
        assert (t == "*") == (w == "*"), (t, w)
        if t.isdigit():
            assert 1 <= int(t) <= 1899
    st = nm._LAST_CONTROL["stats"]
    assert st["coded"] == 369 and st["particle_tokens"] + st["distinct_book"] > 0 and st["holdout_index"] == 5
    assert st["book_forms"] <= 1800
    # (3) wildcards and per-class scoring
    kinds = [k for k, v in nm._split([["12", "**", "1450", "***", "<..>", "99", "100"]])]
    assert kinds == ["P", "W", "B", "W", "W", "P", "B"], kinds
    nm._LAST_CONTROL["classes"] = ["P", "W", "B", "B"]
    with contextlib.redirect_stdout(io.StringIO()):
        r = nm.score_recovery("the * house houses", "the * house home")
    assert abs(r - 2 / 3) < 1e-9, r
    assert nm.split_decode("a b c d e", [["1", "2"], ["3", "4", "5"]]) == ["a b", "c d e"]
    # (2) machinery: greedy from the true key is a near fixed point; a short blind solve is well formed
    truth = {int(t): w for t, w in zip(toks, words) if t != "*"}
    nm._LAST_CONTROL["classes"] = [("W" if w == "*" else ("P" if int(t) < 100 else "B")) for t, w in zip(toks, words)]
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        dec, sc, info = nm.solve(cm, {}, 1, 1, train, {**params, "_init": truth, "sweeps": 0, "greedy": 2})
        rec = nm.score_recovery(dec, plain)
    line = [l for l in out.getvalue().splitlines() if "recovery by class" in l][-1]
    p_rec = float(line.split("P=")[1].split("(")[1].split(")")[0])
    b_rec = float(line.split("B=")[1].split("(")[1].split(")")[0])
    assert p_rec > 0.7 and b_rec > 0.15 and rec > 0.4, (line, rec)
    assert len(dec.split()) == len(toks) and all((d == "*") == (t == "*") for d, t in zip(dec.split(), toks))
    assert info["values"] == len({t for t in toks if t.isdigit()})
    with contextlib.redirect_stdout(io.StringIO()):
        dec2, sc2, info2 = nm.solve(cm, {}, 2, 1, train, {**params, "sweeps": 2, "greedy": 1, "phase1": 2})
    assert len(dec2.split()) == len(toks) and sc2 < 0 and info2["singletons"] > 0 and sc2 != sc
    # (5) cribs (ARM3-LOOP): value=word pairs are held through phase 1, the anneal and the greedy sweeps of every
    # restart, including a singleton and a repeated value and a word the LM has never seen; restart_keys reports
    # one key per restart; a crib naming a value not in the cipher is ignored, not an error
    from collections import Counter
    cnt = Counter(t for t in toks if t.isdigit())
    rep = next(t for t, c in cnt.most_common() if c > 1 and int(t) >= 100)
    sing = next(t for t, c in cnt.items() if c == 1 and int(t) >= 100)
    part = next(t for t, c in cnt.most_common() if int(t) < 100)
    cribs = {rep: "zzqqx", sing: "treaty", int(part): "of", "99999": "nothing"}
    with contextlib.redirect_stdout(io.StringIO()):
        dec3, sc3, info3 = nm.solve(cm, {}, 3, 2, train, {**params, "sweeps": 2, "greedy": 1, "phase1": 2, "cribs": cribs})
    key3 = {t: w for t, w in zip(toks, dec3.split()) if t != "*"}
    assert key3[rep] == "zzqqx" and key3[sing] == "treaty" and key3[part] == "of", (key3[rep], key3[sing], key3[part])
    assert len(info3["restart_keys"]) == 2 and all(k[rep] == "zzqqx" for k in info3["restart_keys"])
    assert info3["cribs"] == {rep: "zzqqx", sing: "treaty", part: "of"} and "99999" not in info3["cribs"]
    # (4) registered in family_run.py
    r = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "family_run.py"),
                        os.path.join(ROOT, "specs", "armstrong-madison-1808.json"), "--family", "nomenclator",
                        "--cipher", os.path.join(ROOT, "ciphers", "armstrong-madison-1808", "ciphertext.txt"),
                        "--tokens", "space", "--control-only", "--dry-run"], capture_output=True, text=True, cwd=ROOT)
    assert r.returncode == 0 and "N=404 signs, K=219 distinct" in r.stdout, r.stdout + r.stderr
    print(f"test_nomenclator OK: truth-start recovery {rec:.3f} ({line.strip()}), {time.time() - t0:.0f}s")


def test_vocab_order():
    """(6) H73 vocab_order mode (3 Oct 2026): rebuild_words joins fragments only when they are not all words and
    turns unread groups into '*'; make_control_vocab is cross-held-out (prior table != book table), reaches the
    target's 369 coded tokens on the two held-out decodes, and its book is one-part at decade level (decade order
    = alphabetical block order); solve_vocab returns a well-formed decode whose decades sit in alphabetical order
    on the prior list. Says nothing about power (h73/results.tsv measures that)."""
    vocab = {"accept", "the", "of", "ment", "govern", "government", "in"}
    assert nm.rebuild_words("ac . ce . pt {12} of the govern . ment", vocab | {"acce"})[1:3] == ["*", "of"]
    assert nm.rebuild_words("{12} x . y", vocab) == ["*", "x", "y"]
    assert nm.rebuild_words("in the", vocab) == ["in", "the"]
    corpora = [jp.read_corpus(str(p)) for p in jp.LANG_CORPORA["en18"]]
    target = [l.split() for l in open(os.path.join(ROOT, "ciphers", "armstrong-madison-1808", "ciphertext.txt"))
              if l.strip() and not l.startswith("#")]
    par = {"vocab_order": 1, "book": "THE972", "prior": "WE028", "target_msgs": target}
    with contextlib.redirect_stdout(io.StringIO()):
        cm, plain, train = nm.make_control({}, 1, corpora, dict(par))
    st = nm._LAST_CONTROL["stats"]
    assert st["coded"] == 369 and st["book_tokens"] > 0 and st["book_list_in_prior"] < 1.0
    pairs = sorted({(int(t), w) for t, w in zip(cm[0], plain.split()) if t.isdigit() and int(t) >= 100})
    by_dec = {}
    for v, w in pairs:
        by_dec.setdefault(v // 10, []).append(w)
    decs = sorted(by_dec)
    for d1, d2 in zip(decs, decs[1:]):
        assert max(by_dec[d1]) < min(by_dec[d2]), (d1, d2)
    with contextlib.redirect_stdout(io.StringIO()):
        dec, sc, info = nm.solve(cm, {}, 1, 1, train, {**par, "sweeps": 1, "greedy": 0})
    assert len(dec.split()) == len(cm[0]) and info["mode"] == "vocab_order" and sc < 0
    prior = [w for w in nm.table_words("WE028", nm.get_lm(train, 3).vocab)]
    key = info["restart_keys"][0]
    seen = {}
    for v, w in key.items():
        if int(v) >= 100:
            seen.setdefault(int(v) // 10, []).append(prior.index(w))
    ds = sorted(seen)
    for d1, d2 in zip(ds, ds[1:]):
        assert max(seen[d1]) < min(seen[d2]), (d1, d2)
    print("test_vocab_order OK")


if __name__ == "__main__":
    test_nomenclator()
    test_vocab_order()
