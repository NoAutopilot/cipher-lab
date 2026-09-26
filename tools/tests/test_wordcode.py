#!/usr/bin/env python3
"""Offline test for tools/families/wordcode.py (bSALW, LANE B12, 26 Sept 2026). No network; needs tools/data/it16.
(1) make_control on a synthetic target (runs of marked/unmarked tokens): N tokens exactly, code token share within
    0.03 of the target's code-capable share, every code token a whole word carried by a marked type name, every
    letter token one letter on an unmarked name;
(2) err=0.064 gives a truth_index aligning surviving tokens with their clean origin (None only for insertions);
(3) at err=0 the solver reads the clean N~800 control above 0.35 token accuracy (chance about 0.05) (2 restarts x 30k iters), per-class numbers
    land in the stash, and split_decode gives one line per run;
(4) the family is registered in family_run.py (dry run on a temp spec).
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
    print(f"all ok in {time.time() - t0:.0f}s")


if __name__ == "__main__":
    main()
