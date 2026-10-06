#!/usr/bin/env python3
"""Offline test for tools/families/wordcode.py (bSALW, LANE B12, 26 Sept 2026). No network; needs tools/data/it16.
(1) make_control on a synthetic target (runs of marked/unmarked tokens): N tokens exactly, code token share within
    0.03 of the target's code-capable share, every code token a whole word carried by a marked type name, every
    letter token one letter on an unmarked name;
(2) err=0.064 gives a truth_index aligning surviving tokens with their clean origin (None only for insertions);
(3) at err=0 the solver reads the clean N~800 control above 0.35 token accuracy (chance about 0.05) (2 restarts x 30k iters), per-class numbers
    land in the stash, and split_decode gives one line per run;
(4) the family is registered in family_run.py (dry run on a temp spec);
(5) context option (SALV-CTX, 26 Sept 2026): read_context parses a TSV (header, blanks, '#' lines), the padded trigram
    sum scores exactly the run's own trigrams plus the 2*(order-1) that cross into the padding, a control with
    context=control carries context on its runs (ctxshare=0.5 blanks the last half), and on the zero-error toy control
    the true key's recovery with context (2 x 30k, same seed) is at least the no-context recovery;
(6) bnd= boundary letter (R13-KAL10);
(7) seed reproducibility (R14-KAL12, 6 Oct 2026): two family_run.py --control-only runs at the same --seed (different
    PYTHONHASHSEED) print identical CONTROL lines, and so does a third with --shuffle-target 1.
Run: python3 tools/tests/test_wordcode.py   (under two minutes)"""
import json, os, random, subprocess, sys, tempfile, time

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import judge_plaintext as jp  # noqa: E402
from families import wordcode as wc  # noqa: E402


def fake_target(rng, nruns=110):
    """Runs of 3-12 tokens: 20 unmarked base names and 60 marked names (about a third of tokens marked)."""
    base = [f"b{i}^" for i in range(20)]
    marked = [f"m{i}^{rng.choice('~15o#')}" for i in range(60)]
    runs = []
    for _ in range(nruns):
        runs.append([rng.choice(marked) if rng.random() < 0.33 else rng.choice(base) for _ in range(rng.randint(3, 12))])
    return runs


def main():
    t0 = time.time()
    rng = random.Random(5)
    msgs = fake_target(rng)
    toks = [t for m in msgs for t in m]
    spec = {"slug": "wordcode-test", "row_pattern": "".join("S" * 5 + "_" * rng.randint(1, 4) for _ in range(80))}
    corpora = [jp.read_corpus(os.path.join(ROOT, "tools", "data", "it16", f)) for f in
               ("alcuneletteredip00ferr.txt", "letterescrittea01vanzgoog.txt", "lettereinedited00tassgoog.txt")]
    params = {"N": len(toks), "K": len(set(toks)), "lengths": [len(m) for m in msgs], "target_msgs": msgs, "err": 0,
              "iters": 30000}
    cm, plain, train = wc.make_control(spec, 1, corpora, dict(params))
    S = wc._STASH
    flat = [t for m in cm for t in m]
    assert len(flat) == len(toks), (len(flat), len(toks))
    tshare = sum(1 for t in toks if "^" in t and t.split("^")[1]) / len(toks)
    assert abs(S["code_share"] - tshare) < 0.03, (S["code_share"], tshare)
    for name, tt, c in zip(flat, S["truth_tokens"], S["truth_code"]):
        if c:
            assert name.split("^")[1], name
        else:
            assert len(tt) == 1 and not name.split("^")[1], (name, tt)
    print(f"(1) control N={len(flat)} code share {S['code_share']} (target {tshare:.3f}), code types {S['code_types']}: ok")
    p2 = dict(params, err=0.064)
    cm2, _, _ = wc.make_control(spec, 2, corpora, dict(p2))
    tix = wc._STASH["truth_index"]
    assert len(tix) == sum(len(m) for m in cm2)
    surv = [j for j in tix if j is not None]
    assert surv == sorted(surv) and len(surv) < len(wc._STASH["truth_tokens"])
    print(f"(2) err 0.064: {wc._STASH.get('del')} del / {wc._STASH.get('ins')} ins / {wc._STASH.get('code')} code: ok")
    cm, plain, train = wc.make_control(spec, 1, corpora, dict(params))
    dec, sc, info = wc.solve(cm, spec, 1, 2, train, dict(params))
    rec = wc.score_recovery(dec, plain)
    assert "per_class" in wc._STASH
    assert rec > 0.35, rec  # N~800 smoke control; chance is about 0.05
    lines = wc.split_decode(dec, cm)
    assert lines and len(lines) == len(cm)
    print(f"(3) clean control token accuracy {rec:.3f} {wc._STASH['per_class']}: ok")
    with tempfile.TemporaryDirectory() as d:
        sp = os.path.join(d, "s.json")
        json.dump({"slug": "wordcode-test", "ciphertext": [" ".join(m) for m in msgs], "alphabet": "sign tokens",
                   "judge": {"language": "it"}}, open(sp, "w"))
        r = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "family_run.py"), sp, "--family", "wordcode",
                            "--dry-run", "--tokens", "space"], capture_output=True, text=True)
        assert r.returncode == 0 and "wordcode" in r.stdout, r.stdout + r.stderr
    print("(4) registered in family_run.py: ok")
    with tempfile.TemporaryDirectory() as d:
        cp = os.path.join(d, "ctx.tsv")
        open(cp, "w").write("run_index\tprev_word\tnext_word\n# note\n0\tSignoria\tche\n1\t\tVostra\n2\t\t\n")
        cx = wc.read_context(cp)
        assert cx == {0: ("signoria", "che"), 1: ("", "uostra"), 2: ("", "")}, cx
    scr = wc.Scorer(corpora, 3, 200)
    core = "wdelwpapaw"
    base = scr.ngrams(core)
    assert abs(scr.ngrams(core, 0, len(core)) - base) < 1e-9
    padded = scr.ngrams("ra" + core + "ch", 2, 2 + len(core))
    extra = sum((scr.ms.logp if "w" in g else scr.mu.logp)(g) for g in ("raw", "awd", "awc", "wch"))
    assert abs(padded - base - extra) < 1e-6, (padded, base, extra)
    pc = dict(params, context="control")
    cm, plain, train = wc.make_control(spec, 1, corpora, dict(pc))
    cc = wc._STASH["control_context"]
    on = sum(1 for v in cc.values() if v[0] or v[1])
    assert len(cc) == len(cm) and on >= 0.8 * len(cm), (on, len(cm))
    dec, _, info = wc.solve(cm, spec, 1, 2, train, dict(pc))
    rec_c = wc.score_recovery(dec, plain)
    assert info["context_runs"] == on
    cm0, plain0, train0 = wc.make_control(spec, 1, corpora, dict(params))
    dec0, _, _ = wc.solve(cm0, spec, 1, 2, train0, dict(params))
    rec_0 = wc.score_recovery(dec0, plain0)
    assert rec_c >= rec_0 - 1e-9, (rec_c, rec_0)
    wc.make_control(spec, 1, corpora, dict(pc, ctxshare=0.5))
    cc5 = wc._STASH["control_context"]
    half = [k for k, v in cc5.items() if v[0] or v[1]]
    assert half and max(half) < round(0.5 * len(cc5)), (max(half), len(cc5))
    print(f"(5) context: parse, padding, control context {on}/{len(cm)} runs, ctxshare 0.5 -> {len(half)}; "
          f"toy recovery with context {rec_c:.3f} >= without {rec_0:.3f}: ok")
    # (6) bnd (R13-KAL10, 6 Oct 2026): a boundary letter other than w, for corpora that use w as a letter
    wc._set_bnd({"bnd": "x"})
    assert wc._run_string(["a", "b"], {"a": "da", "b": "w"}) == "xdaxwx", wc._run_string(["a", "b"], {"a": "da", "b": "w"})
    assert wc.words_of("swet axe") == ["swet"]
    try:
        wc._set_bnd({"bnd": "j"})  # folded away by ha.fold(): must be refused
        raise AssertionError("bnd=j accepted")
    except SystemExit:
        pass
    wc._set_bnd({})
    assert wc.BND == "w" and wc.words_of("swet axe") == ["axe"]
    print("(6) bnd=x boundary, words_of, j refused, default w restored: ok")
    # (7) seed reproducibility (R14-KAL12, 6 Oct 2026): the same --seed gives the same control in two processes with
    # different PYTHONHASHSEED, and --shuffle-target leaves the control unchanged (it used to be built from the shuffled
    # tokens, whose Counter.most_common tie order differs, so R14-KAL11 saw controls 'not seed-reproducible')
    with tempfile.TemporaryDirectory() as d:
        sp = os.path.join(d, "s.json")
        json.dump({"slug": "wordcode-test", "ciphertext": [" ".join(m) for m in msgs], "alphabet": "sign tokens",
                   "judge": {"language": "it"}}, open(sp, "w"))
        base = [sys.executable, os.path.join(ROOT, "tools", "family_run.py"), sp, "--family", "wordcode", "--tokens",
                "space", "--control-only", "--seeds", "2", "--restarts", "1", "--param", "iters=3000", "--param", "err=0.05",
                "--out", os.path.join(d, "H.md")]
        for f in ("alcuneletteredip00ferr.txt", "letterescrittea01vanzgoog.txt", "lettereinedited00tassgoog.txt"):
            base += ["--corpus", os.path.join(ROOT, "tools", "data", "it16", f)]
        outs = []
        for hs, extra in (("1", []), ("2", []), ("1", ["--shuffle-target", "1"])):
            r = subprocess.run(base + extra, capture_output=True, text=True, env=dict(os.environ, PYTHONHASHSEED=hs))
            assert r.returncode == 0, r.stdout + r.stderr
            outs.append([ln for ln in r.stdout.splitlines() if ln.startswith("CONTROL seed")])
        assert len(outs[0]) == 2 and outs[0] == outs[1] == outs[2], outs
    print(f"(7) same seed -> same control across hash seeds and under --shuffle-target ({outs[0][0].split(': ', 1)[1]}): ok")
    print(f"all ok in {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
