#!/usr/bin/env python3
"""Offline tests for tools/family_run.py --param lock=FILE (MQS-LOCK, 9 Oct 2026; tools/tests/PREREG-MQS-LOCK.md).

Must catch: a locked pair that changes in any restart (homophonic, nomenclator, wordcode, syllabary); lock= on a family
it is not wired for passing silently; locked tokens counted in the recovery figure; a row without the lock's sha256.
Must NOT block: a run without lock= (byte-identical to the pre-lock code at a fixed seed: goldens recorded from the
code at commit a522b16e before the edit); lockshare=0 (the blind baseline: same number as no lock); a lock file naming
signs absent from the ciphertext (reported, ignored); seeded_code's lock= as an alias of pins= (identical output).
No network. Run: python3 tools/tests/test_family_run_lock.py  (about a minute)"""
import contextlib, hashlib, io, json, os, re, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import family_run as fr  # noqa: E402
import families  # noqa: E402
import judge_plaintext as jp  # noqa: E402

SMALL = os.path.join(ROOT, "tools/data/fr16/lettresindites00marg_djvu.txt.gz")
BIG = os.path.join(ROOT, "tools/data/fr16/lettresdecatheri02cathuoft_djvu.txt.gz")
TMP = tempfile.mkdtemp(prefix="lock_test_")


def quiet(f, *a, **k):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
        r = f(*a, **k)
    return r, buf.getvalue()


def write(name, text):
    p = os.path.join(TMP, name)
    open(p, "w", encoding="utf-8").write(text)
    return p


def spec(name, cipher_lines):
    return write(name, json.dumps({"slug": "locktest", "alphabet": "numerals", "ciphertext": cipher_lines,
                                   "judge": {"language": "fr", "corpora": [SMALL]}}))


def test_unlocked_recovery_fixture():
    flat = ["a", "b", "a", "c"]
    truth = ["x", "y", "x", "z"]
    dec = ["x", "q", "x", "q"]  # locked tokens all right, unlocked all wrong
    r, n = fr.unlocked_recovery(dec, truth, flat, {"a": "x"})
    assert (r, n) == (0.0, 2), (r, n)
    r, n = fr.unlocked_recovery(["x", "y", "x", "z"], [None, "y", "x", "z"], flat, {"a": "x"})
    assert (r, n) == (1.0, 2), (r, n)  # a None truth (null/inserted) is not counted


def test_choose_control_lock():
    flat = [str(i % 10) for i in range(200)] + ["0"] * 50
    truth = [chr(97 + int(t)) for t in flat]
    lock, share = fr.choose_control_lock(flat, truth, 0.3, 1)
    assert share >= 0.3 and all(lock[t] == chr(97 + int(t)) for t in lock), (lock, share)
    lock0, share0 = fr.choose_control_lock(flat, truth, 0.0, 1)
    assert lock0 == {} and share0 == 0.0
    wrong, _ = fr.choose_control_lock(flat, truth, 0.5, 1, perm=True)
    right, _ = fr.choose_control_lock(flat, truth, 0.5, 1)
    assert set(wrong) == set(right) and all(wrong[t] != right[t] for t in right), (wrong, right)


def test_read_lock_contract():
    p = write("l.tsv", "sign\tvalue\tgrade\n# comment\n12\te\tC\n13\tNULL\n14\tq\tS\n")
    v, g = fr.read_lock(p)
    assert v == {"12": "e", "13": "", "14": "q"} and g == {"12": "C", "13": "-", "14": "S"}, (v, g)
    bad = write("bad.tsv", "12 e\n")
    try:
        fr.read_lock(bad)
        raise AssertionError("a row without a TAB value must be an error")
    except SystemExit:
        pass


def test_refuses_unwired_family_and_reports_absent():
    sp = spec("s1.json", " ".join(str(i % 20) for i in range(120)))
    lk = write("abs.tsv", "3\te\n999\tz\n")
    rc, out = quiet(fr.main, [sp, "--family", "masc", "--param", f"lock={lk}", "--dry-run"])
    assert rc == 2 and "not wired for family 'masc'" in out, (rc, out)
    rc, out = quiet(fr.main, [sp, "--family", "homophonic", "--param", f"lock={lk}", "--dry-run"])
    assert rc == 0 and "1 absent from the ciphertext, ignored (999)" in out, out
    rc, out = quiet(fr.main, [sp, "--family", "homophonic", "--param", f"lock={os.path.join(TMP, 'nofile')}", "--dry-run"])
    assert rc == 2, out


def _ctl(name, params, corp, restarts=2, seed=1):
    fam = families.load(name)
    (cm, plain, train), _ = quiet(fam.make_control, {}, seed, corp, dict(params))
    return fam, cm, plain, train


def test_held_in_every_restart():
    corp = [jp.read_corpus(SMALL)]
    # homophonic: lock two signs, one at a value the model would not choose for it, held in every restart
    tm = [[str(i % 30) for i in range(240)]]
    fam, cm, plain, train = _ctl("homophonic", {"N": 240, "K": 30, "lengths": [240], "target_msgs": tm}, corp)
    flat = [t for m in cm for t in m]
    a, b = flat[0], flat[1] if flat[1] != flat[0] else flat[2]
    lock = {a: "z", b: plain[flat.index(b)]}
    (dec, sc, info), _ = quiet(fam.solve, cm, {}, 1, 3, train, {"iters": "3000", "lock": lock})
    assert info["lock"]["held_in_every_restart"] and all(dec[i] == lock[t] for i, t in enumerate(flat) if t in lock)
    # syllabary
    sm = [["%d%s" % (i % 40, "^1" if i % 5 == 0 else "") for i in range(200)]]
    fam, cm, plain, train = _ctl("syllabary", {"N": 200, "K": 44, "lengths": [200], "target_msgs": sm, "err": "0"}, corp)
    flat = [t for m in cm for t in m]
    truth = fam.lock_truth(cm, plain)
    lock = {}
    for t, v in zip(flat, truth):
        if v and len(lock) < 4 and t not in lock:
            lock[t] = v
    (dec, sc, info), _ = quiet(fam.solve, cm, {}, 1, 2, train, {"iters": "3000", "err": "0", "target_msgs": sm, "lock": lock})
    dt = fam.lock_decode(dec, cm)
    assert info["lock"]["held_in_every_restart"] and all(dt[i] == lock[t] for i, t in enumerate(flat) if t in lock), info["lock"]
    # wordcode
    wm = [["%d%s" % (i % 40, "^x" if i % 7 == 0 else "") for i in range(j, j + 20)] for j in range(0, 200, 20)]
    wp = {"N": 200, "K": 45, "lengths": [20] * 10, "target_msgs": wm, "err": "0", "vocab": "200"}
    fam, cm, plain, train = _ctl("wordcode", wp, corp)
    flat = [t for m in cm for t in m]
    truth = fam.lock_truth(cm, plain)
    lock = {}
    for t, v in zip(flat, truth):
        if v and len(lock) < 5 and t not in lock:
            lock[t] = v
    (dec, sc, info), _ = quiet(fam.solve, cm, {}, 1, 2, train, {**wp, "iters": "3000", "lock": lock})
    dt = fam.lock_decode(dec, cm)
    assert info["lock"]["held_in_every_restart"] and all(dt[i] == lock[t] for i, t in enumerate(flat) if t in lock), info["lock"]
    # nomenclator: every restart's final key (info["restart_keys"]) carries the lock
    fam = families.load("nomenclator")
    words = "le roi de france a mande que la reine et le duc".split()
    cm = [[str(100 + 10 * (i % 11)) for i in range(150)]]
    lock = {"100": "roi", "110": "duc", "999": "absent"}
    (dec, sc, info), _ = quiet(fam.solve, cm, {}, 1, 2, corp, {"sweeps": "2", "greedy": "1", "phase1": "1", "lock": lock})
    assert all(k.get("100") == "roi" and k.get("110") == "duc" for k in info["restart_keys"]), info["restart_keys"]
    assert all(w == "roi" for w, t in zip(dec.split(), cm[0]) if t == "100")
    del words


GOLDEN = {"homophonic": ("b21e4c6500d5bac7", -600.639476, 0.2375), "syllabary": ("401a2907ce5e48fc", -599.583642, 0.06),
          "wordcode": ("ecce4154b010c28f", -461.342716, 0.21)}


def test_no_lock_byte_identical():
    corp = [jp.read_corpus(SMALL), jp.read_corpus(BIG)[:200000]]
    cases = {"homophonic": {"N": 240, "K": 30, "lengths": [240], "target_msgs": [[str(i % 30) for i in range(240)]]},
             "syllabary": {"N": 200, "K": 44, "lengths": [200], "err": "0",
                           "target_msgs": [["%d%s" % (i % 40, "^1" if i % 5 == 0 else "") for i in range(200)]]},
             "wordcode": {"N": 200, "K": 45, "lengths": [20] * 10, "err": "0", "vocab": "200",
                          "target_msgs": [["%d%s" % (i % 40, "^x" if i % 7 == 0 else "") for i in range(j, j + 20)]
                                          for j in range(0, 200, 20)]}}
    for name, params in cases.items():
        params["iters"] = "20000" if name == "homophonic" else "3000"  # the goldens' own settings
        fam, cm, plain, train = _ctl(name, params, corp)
        (dec, sc, info), _ = quiet(fam.solve, cm, {}, 1, 2, train, dict(params))
        rec, _ = quiet(fam.score_recovery, dec, plain)
        got = (hashlib.sha256(dec.encode()).hexdigest()[:16], round(sc, 6), round(rec, 6))
        assert got == GOLDEN[name], (name, got, GOLDEN[name])


def test_family_run_rows_share_zero_and_alias():
    toks = [str(i % 30) for i in range(240)]
    sp = spec("s2.json", " ".join(toks))
    lk = write("l2.tsv", "# test lock\n0\te\tC\n1\ts\tS\n")
    out = os.path.join(TMP, "H.md")
    base = [sp, "--family", "homophonic", "--control-only", "--seeds", "1", "--restarts", "2", "--out", out,
            "--param", "iters=3000"]
    rc, o_blind = quiet(fr.main, base)
    rc0, o_zero = quiet(fr.main, base + ["--param", f"lock={lk}", "--param", "lockshare=0"])
    rec = lambda o: re.search(r"CONTROL seed 1: .* recovery ([0-9.]+)", o).group(1)
    assert rc == rc0 == 0 and rec(o_blind) == rec(o_zero), (o_blind, o_zero)
    rc, o_lock = quiet(fr.main, base + ["--param", f"lock={lk}"])
    sha = hashlib.sha256(open(lk, "rb").read()).hexdigest()[:16]
    row = open(out).read().strip().splitlines()[-1]
    assert rc == 0 and f"lock_sha256={sha}" in row and "recovery=unlocked_positions" in row, row
    assert "lock_share_target=0.067" in row, row  # 2 of 30 signs, 16 of 240 tokens
    # seeded_code: lock= is an alias of pins=, identical control output
    sc_toks = [str(1000 + (i * 7) % 60) for i in range(150)]
    sp3 = spec("s3.json", " ".join(sc_toks))
    pins = write("pins.tsv", "1000\tle\n1007\tde\n")
    b3 = [sp3, "--family", "seeded_code", "--control-only", "--seeds", "1", "--restarts", "1", "--out", out,
          "--param", "iters=3000"]
    _, o_pins = quiet(fr.main, b3 + ["--param", f"pins={pins}"])
    _, o_alias = quiet(fr.main, b3 + ["--param", f"lock={pins}"])
    pick = lambda o: [l for l in o.splitlines() if l.startswith(("CONTROL", "  control seed"))]
    assert pick(o_pins) == pick(o_alias) and pick(o_pins), (o_pins, o_alias)


if __name__ == "__main__":
    import time
    t0 = time.time()
    for name, f in list(globals().items()):
        if name.startswith("test_") and callable(f):
            f()
            print(f"ok {name} ({time.time() - t0:.0f}s)")
    print("all family_run lock tests passed")
