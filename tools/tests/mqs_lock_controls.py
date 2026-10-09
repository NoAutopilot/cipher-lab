#!/usr/bin/env python3
"""MQS-LOCK controls for family_run.py --param lock=FILE (9 Oct 2026; pre-registered in tools/tests/PREREG-MQS-LOCK.md).

  python3 tools/tests/mqs_lock_controls.py k1     # C1161-LOLO stage 1 through families.homophonic with lock (fidelity)
  python3 tools/tests/mqs_lock_controls.py k2     # synthetic fr16 gain on unlocked positions: arms A B C D, 3 draws x 3 seeds

K1 reads ciphers/clair1161-avis-flandre-1688 READ-ONLY (lolo_diag's stream, key.tsv, held set and null are imported, not
copied); its keys go to the scratchpad given by --keys (default /tmp). K2 runs family_run.py --control-only on fixture
specs under tools/tests/fixtures/ with --out tools/tests/MQS-LOCK-K2-HYPOTHESES.md (control-only writes no decode file).
Both append rows to tools/tests/MQS-LOCK-controls.tsv. Serial: no Pool, nothing in the background."""
import argparse, contextlib, io, json, os, re, statistics, sys, time
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "tools"))
OUT = os.path.join(HERE, "MQS-LOCK-controls.tsv")
HDR = "control\tarm\tN\tK\tseed\tdraw\trestarts\tlocked_share\tunlocked_positions\trecovery\tnote\n"
FIX = os.path.join(HERE, "fixtures")


def row(*cells):
    if not os.path.exists(OUT):
        open(OUT, "w").write(HDR)
    line = "\t".join(str(c) for c in cells) + "\n"
    open(OUT, "a").write(line)
    print(line, end="", flush=True)


def k1(keys_dir):
    import judge_plaintext as jp, families
    sys.path.insert(0, os.path.join(ROOT, "ciphers/clair1161-avis-flandre-1688/two"))
    import lolo_diag as ld  # read-only: its objective, stream, held set, null
    ra = ld.ra
    ld.use("none")
    fam = families.load("homophonic")
    corp = [jp.read_corpus(p) for p in ra.FR17]
    free = ra.FREE + list(ra.PLANT)
    held = {s: v for s, v in ld.TRUE.items() if s not in free}
    os.makedirs(keys_dir, exist_ok=True)
    keys = []
    for drop in ld.LEAVES:
        seq = ld.leaf_stream(drop)
        t0 = time.time()
        dec, sc, info = fam.solve([seq], {}, 1, ra.RESTARTS, corp, {"lock": held, "order": str(ra.ORDER),
                                                                   "iters": str(ra.ITERS)})
        key = info["key"]
        assert info["lock"]["held_in_every_restart"], drop
        keys.append(key)
        with open(os.path.join(keys_dir, f"k1_key_{drop}.tsv"), "w") as f:
            f.write("sign\tvalue\n" + "".join(f"{s}\t{key[s]}\n" for s in sorted(key)))
        print(f"K1 {drop}: N={len(seq)} score {sc:.1f} apd {' '.join(f'{s}={key.get(s)}' for s in ra.PLANT)} "
              f"{time.time() - t0:.0f}s", flush=True)
    cons = {}
    for s in free:
        c = Counter(k[s] for k in keys if s in k)
        v, n = c.most_common(1)[0]
        cons[s] = (v if n >= ld.NLOLO else None, n, dict(c))
    kstar = dict(ld.TRUE)
    kstar.update(keys[0])
    kstar.update({s: c[0] for s, c in cons.items() if c[0]})
    rec = 0
    for s in ra.PLANT:
        A, B = ra.PLANT[s], cons[s][0]
        k = dict(kstar)
        if B and B != A:
            k[s] = B; jb = ld.l4only(k); k[s] = A; d = jb - ld.l4only(k)
            nl = sorted(ld.lolo_null((kstar, free, s, A, B, i)) for i in range(1, 51))
            p95 = nl[47]
        else:
            d, p95 = float("nan"), float("nan")
        ok = B == ld.TRUE[s] and d > 0 and d > p95
        rec += ok
        row("K1", "lock", "6 leaf streams", len(ld.TRUE), 1, s, ra.RESTARTS, "-", "-",
            int(ok), f"planted {s} true {ld.TRUE[s]}: consensus {B} ({cons[s][1]}/6, votes {cons[s][2]}) dL4 {d:.5f} "
                     f"null p95 {p95:.5f} -> {'recovered' if ok else 'NOT recovered'}")
    verdict = "GATE PASS" if rec == 3 else "GATE MISS"
    row("K1", "summary", "-", "-", "-", "-", ra.RESTARTS, "-", "-", f"{rec}/3",
        f"{verdict} (gate 3/3; local C1161-LOLO 3/3); free signs differing from key.tsv per leaf: "
        + " ".join(str(sum(1 for s in free if k.get(s, ld.TRUE[s]) != ld.TRUE[s])) for k in keys))


def k2_run(N, K, restarts, extra, draw):
    import family_run as fr
    spec = os.path.join(FIX, f"mqs-lock-k2-N{N}.json")
    if not os.path.exists(spec):
        os.makedirs(FIX, exist_ok=True)
        json.dump({"slug": "mqs-lock-k2", "name": f"MQS-LOCK K2 fixture: N={N} placeholder tokens, K={K} distinct; "
                   "control-only (the tokens are not a cryptogram)", "alphabet": "numerals",
                   "ciphertext": " ".join(str(i % K) for i in range(N))}, open(spec, "w"), indent=1)
    lock = os.path.join(FIX, "mqs-lock-empty.tsv")
    if not os.path.exists(lock):
        open(lock, "w").write("# MQS-LOCK K2: no target lock (control-only); the control's share is set by lockshare\n")
    corp = [os.path.join(ROOT, "tools/data/fr16/lettresdecatheri01cathuoft_djvu.txt.gz"),
            os.path.join(ROOT, "tools/data/fr16/lettresindites00marg_djvu.txt.gz")]
    argv = [spec, "--family", "homophonic", "--control-only", "--seed", "1", "--seeds", "3", "--restarts", str(restarts),
            "--out", os.path.join(HERE, "MQS-LOCK-K2-HYPOTHESES.md"), "--label", "MQS-LOCK K2",
            "--param", f"lock={lock}", "--param", "lockshare=0.3", "--param", f"lockdraw={draw}"]
    for c in corp:
        argv += ["--corpus", c]
    for e in extra:
        argv += ["--param", e]
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = fr.main(argv)
    assert rc == 0, buf.getvalue()[-2000:]
    out = {}
    for m in re.finditer(r"lock \(control seed (\d+)\): (\d+) sign types locked, token share ([0-9.]+).*?recovery on "
                         r"(\d+) unlocked positions ([0-9.]+)", buf.getvalue()):
        out[int(m.group(1))] = (float(m.group(3)), int(m.group(4)), float(m.group(5)))
    assert len(out) == 3, buf.getvalue()[-2000:]
    return out


ARMS = {"A": (8, []), "B": (8, ["lockapply=0"]), "C": (16, ["lockapply=0"]), "D": (8, ["lockperm=1"])}


def k2(K):
    t0 = time.time()
    N = None
    for n in (150, 200, 300, 400):
        r = k2_run(n, K, 8, ["lockapply=0"], 0)
        m = statistics.mean(v[2] for v in r.values())
        for s, v in sorted(r.items()):
            row("K2-cal", "B", n, K, s, 0, 8, f"{v[0]:.3f}", v[1], f"{v[2]:.4f}", "N calibration (blind, same positions)")
        print(f"K2 calibration N={n}: blind mean {m:.4f} ({time.time() - t0:.0f}s)", flush=True)
        if 0.30 <= m <= 0.80:
            N = n
            break
    if N is None:
        row("K2", "summary", "-", K, "-", "-", "-", "-", "-", "-", "NON-TEST: no N in {150,200,300,400} has blind mean in [0.30,0.80]")
        return
    res = {}
    for arm, (rs, extra) in ARMS.items():
        for d in (0, 1, 2):
            r = k2_run(N, K, rs, extra, d)
            for s, v in sorted(r.items()):
                res[(arm, s, d)] = v[2]
                row("K2", arm, N, K, s, d, rs, f"{v[0]:.3f}", v[1], f"{v[2]:.4f}", "")
            print(f"K2 arm {arm} draw {d} done ({time.time() - t0:.0f}s)", flush=True)
    pairs = [(s, d) for s in (1, 2, 3) for d in (0, 1, 2)]
    B = [res[("B",) + p] for p in pairs]
    gA = statistics.mean(res[("A",) + p] - res[("B",) + p] for p in pairs)
    gC = statistics.mean(res[("C",) + p] - res[("B",) + p] for p in pairs)
    gD = statistics.mean(res[("D",) + p] - res[("B",) + p] for p in pairs)
    sdB = statistics.stdev(B)
    mB = statistics.mean(B)
    ok1, ok2, ok3, ok4 = gA > gC, gA > 2 * sdB, gD <= 2 * sdB, mB < 0.95
    verdict = "PASS" if ok1 and ok2 and ok3 and ok4 else "FAIL"
    row("K2", "summary", N, K, "1-3", "0-2", "-", "0.3", "-", f"gA {gA:+.4f}",
        f"{verdict}: blind B mean {mB:.4f} sd {sdB:.4f}; A {statistics.mean(res[('A',) + p] for p in pairs):.4f} "
        f"C(2x restarts) {statistics.mean(res[('C',) + p] for p in pairs):.4f} D(wrong key) "
        f"{statistics.mean(res[('D',) + p] for p in pairs):.4f}; gA {gA:+.4f} > gC {gC:+.4f}: {ok1}; gA > 2sdB "
        f"{2 * sdB:.4f}: {ok2}; null gD {gD:+.4f} <= 2sdB: {ok3}; B < 0.95: {ok4}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("which", choices=["k1", "k2"])
    ap.add_argument("--keys", default="/tmp/mqs_lock_k1", help="K1 key files (scratch, never under ciphers/)")
    ap.add_argument("--K", type=int, default=35)
    a = ap.parse_args()
    k1(a.keys) if a.which == "k1" else k2(a.K)
