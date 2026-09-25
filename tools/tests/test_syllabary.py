#!/usr/bin/env python3
"""Offline test for tools/families/syllabary.py (LANE R8 DSN, 25 Sept 2026). No network; needs tools/data/it16.
(1) make_control lays a window on a synthetic row pattern: N tokens, marked share within 0.05 of the target's, every
    marked token a consonant+vowel, every bare token one letter, marks only from the target's own mark strings;
(2) the measured error mix at err=0.05 gives del/ins/code counts within 3 sigma and a truth_index that aligns
    surviving tokens with their clean origin;
(3) at err=0 the solver reads a clean N=700 control above 0.75 token accuracy (2 restarts x 40k iters), the
    decode file lines follow token counts (split_decode), and score_recovery equals the stash-based token accuracy;
(4) the family is registered in family_run.py (dry run on a temp spec);
(5) DSN2 params (25 Sept 2026): marks=mixed merges only pairs of the mark's class (letter+n/m for ~, a double letter
    for dot/#/o, consonant+vowel for numerals) and gives doubling marks no free symbol; boundary=1 splits the
    control into runs whose stream carries a fixed B symbol at both edges and whose decode holds no boundary letter;
    bases=3 puts every control mark on the three most-marked target bases; the defaults are untouched (the seed-1
    control sequence of (1) is byte-identical before and after).
Run: python3 tools/tests/test_syllabary.py   (under a minute)"""
import json, math, os, random, subprocess, sys, tempfile, time

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import judge_plaintext as jp  # noqa: E402
from families import syllabary as sy  # noqa: E402


def fake_target(rng, n=700):
    """A target-shaped token list: 26 base codes, marks ~ 1 dot 5 7 on six of them, about a third marked."""
    codes = [f"c{i}" for i in range(26)]
    marks = ["~", "1", "dot", "5", "7", "#", "o"]
    toks = []
    for _ in range(n):
        c = rng.choice(codes)
        if c in ("c0", "c1", "c2", "c3", "c4", "c5") and rng.random() < 0.7:
            toks.append(f"{c}^{rng.choice(marks)}")
        else:
            toks.append(f"{c}^")
    return toks


def main():
    t0 = time.time()
    rng = random.Random(3)
    toks = fake_target(rng)
    pattern = "".join("S" * rng.randint(1, 12) + "_" * rng.randint(1, 4) for _ in range(120))
    spec = {"slug": "syllabary-test", "row_pattern": pattern}
    corpora = [jp.read_corpus(os.path.join(ROOT, "tools", "data", "it16", f)) for f in
               ("alcuneletteredip00ferr.txt", "letterescrittea01vanzgoog.txt")]
    msgs = [toks]
    params = {"N": len(toks), "K": len(set(toks)), "lengths": [len(toks)], "target_msgs": msgs,
              "messages_independent": False, "err": 0, "iters": 40000}
    # (1) layout and allotment
    cm, plain, train = sy.make_control(spec, 1, corpora, dict(params))
    seq = cm[0]
    assert len(seq) == len(toks), len(seq)
    tmarked = sum(1 for t in toks if sy.split_tok(t)[1]) / len(toks)
    cmarked = sum(1 for t in seq if sy.split_tok(t)[1]) / len(seq)
    assert abs(tmarked - cmarked) < 0.05, (tmarked, cmarked)
    truth = sy._STASH["truth_tokens"]
    assert "".join(truth) == plain
    tmarks = {sy.split_tok(t)[1] for t in toks if sy.split_tok(t)[1]}
    for s, t in zip(seq, truth):
        code, mark = sy.split_tok(s)
        if mark:
            assert len(t) == 2 and t[0] not in sy.VOW and t[1] in sy.VOW and mark in tmarks, (s, t)
        else:
            assert len(t) == 1, (s, t)
    assert len(train[0]) < len("".join(corpora))  # window held out
    # (2) measured error mix
    types = [(t, c) for t, c in __import__("collections").Counter(toks).most_common()]
    codes = [(c, n) for c, n in __import__("collections").Counter(sy.split_tok(t)[0] for t in toks).most_common()]
    clean = ["c9^"] * 4000
    noisy, tix, cnt = sy.measured_error(clean, types, codes, 0.05, random.Random(5))
    for k, share in zip(("del", "ins", "code"), sy.MIX):
        exp = 4000 * 0.05 * share / sum(sy.MIX)
        assert abs(cnt[k] - exp) < 3 * math.sqrt(exp) + 1, (k, cnt[k], exp)
    assert len(noisy) == len(tix) == 4000 - cnt["del"] + cnt["ins"]
    assert all((j is None) == (i in {k for k, j2 in enumerate(tix) if j2 is None}) for i, j in enumerate(tix))
    surv = [j for j in tix if j is not None]
    assert surv == sorted(surv) and len(set(surv)) == len(surv), "surviving tokens keep their order"
    # (3) clean control solve
    dec, sc, info = sy.solve(cm, spec, 1, 2, train, dict(params))
    rec = sy.score_recovery(dec, plain)
    ok = sum(a == b for a, b in zip(sy._STASH["dec_tokens"], truth)) / len(truth)
    assert abs(rec - ok) < 1e-9
    assert rec > 0.75, (rec, dec[:80])
    lines = sy.split_decode(dec, [toks[:100], toks[100:]])
    assert lines and len(lines) == 2 and "".join(lines) == dec and lines[0] == "".join(sy._STASH["dec_tokens"][:100])
    assert info["symbols"] == len({x for x in sy.expand(seq)[0]})
    # (4) registered
    with tempfile.TemporaryDirectory() as d:
        sp = os.path.join(d, "syllabary-test.json")
        json.dump({"slug": "syllabary-test", "ciphertext": [" ".join(toks[:50])], "row_pattern": pattern,
                   "judge": {"language": "it"}}, open(sp, "w"))
        r = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "family_run.py"), sp, "--family", "syllabary",
                            "--dry-run"], capture_output=True, text=True, cwd=ROOT)
        assert r.returncode == 0 and "N=50 signs" in r.stdout, r.stdout + r.stderr
    # (5) DSN2 params
    cm0, _, _ = sy.make_control(spec, 1, corpora, dict(params))
    assert cm0[0] == seq, "defaults changed the control sequence"
    mc = sy.mark_classes(sorted(tmarks), "mixed")
    assert mc["~"] == "nm" and mc["1"] == sy.VOW and mc["dot"] == "dbl" and mc["o"] == "dbl", mc
    cmx, plainx, _ = sy.make_control(spec, 1, corpora, dict(params, marks="mixed"))
    truthx = sy._STASH["truth_tokens"]
    for s_, t in zip(cmx[0], truthx):
        code, mark = sy.split_tok(s_)
        if mark:
            c = mc[mark]
            assert len(t) == 2 and (t[0] == t[1] if c == "dbl" else t[1] in c), (s_, t, c)
    stream, spans = sy.expand(cmx[0], "regular", mc)
    assert not any(x.startswith("M") and x[1:] in mc and mc[x[1:]] == "dbl" for x in stream), "doubling mark got a symbol"
    dbl_tok = next(i for i, s_ in enumerate(cmx[0]) if sy.split_tok(s_)[1] and mc[sy.split_tok(s_)[1]] == "dbl")
    a, b = spans[dbl_tok]
    assert stream[a:b] == [stream[a], stream[a]], stream[a:b]
    decx, scx, infox = sy.solve(cmx, spec, 1, 1, train, dict(params, marks="mixed", iters=5000))
    assert len(decx) == len(plainx)
    cmb, plainb, trainb = sy.make_control(spec, 1, corpora, dict(params, boundary="1", bases="3"))
    assert len(cmb) > 1, "boundary=1 should split the control into runs"
    assert "w" in trainb[0] and "w" not in plainb.replace("w", "") and sum(len(m) for m in cmb) == len(toks)
    tb = [c for c, _ in __import__("collections").Counter(sy.split_tok(t)[0] for t in toks if sy.split_tok(t)[1]).most_common(3)]
    marked_codes = {sy.split_tok(t)[0] for m in cmb for t in m if sy.split_tok(t)[1]}
    assert marked_codes <= set(tb), (marked_codes, tb)
    streamb, spansb = sy.expand([t for m in cmb for t in m], "regular", mc, True, cmb)
    assert streamb.count("B") == 2 * len(cmb) and streamb[0] == "B" and streamb[-1] == "B"
    decb, scb, infob = sy.solve(cmb, spec, 1, 1, trainb, dict(params, boundary="1", bases="3", iters=5000))
    assert "w" not in decb and len(decb) == len(plainb.replace("w", "")), (len(decb), len(plainb))
    assert infob["key"]["B"] == "w"
    print(f"ok: control N={len(seq)} marked {cmarked:.2f} (target {tmarked:.2f}) use {sy._STASH['use']}; clean solve token "
          f"accuracy {rec:.3f}; error counts {cnt}; {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
