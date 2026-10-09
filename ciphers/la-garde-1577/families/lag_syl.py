#!/usr/bin/env python3
"""LAG-SYL (9 Oct 2026): the LAG-GAP score-gap gate for the syllabary family at N=239 (PREREG-LAG-SYL.md, Amendment 1).

Copy of lag_gap.py with: the syllabary family on the spec's marks-kept code^mark ciphertext (239 tokens, 48 types); the
statistic is solver score PER CIPHER TOKEN (the family's error mix inserts/deletes tokens, so control N varies); controls at
err 0.084/0.107 (seeds 1-20); 40 shuffled targets; power check at err 0.107 (seeds 101-110 x 20 own shuffles).
Writes families/lag_syl.tsv and prints the read-out. --report re-prints from the TSV; --check re-runs and exits 1 if the
committed TSV differs. CPU only, 4 processes.
"""
import os, sys, json, math, random
from multiprocessing import Pool
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import family_run as fr  # noqa: E402
import families  # noqa: E402
import judge_plaintext as jp  # noqa: E402

SPEC = os.path.join(ROOT, "specs", "la-garde-1577.json")
OUT = os.path.join(os.path.dirname(__file__), "lag_syl.tsv")
G = {}


def init():
    os.chdir(ROOT)
    spec = json.load(open(SPEC, encoding="utf-8"))
    msgs, mode = fr.read_spec_cipher(spec, "space")
    toks = [t for m in msgs for t in m]
    G.update(spec=spec, msgs=msgs, fam=families.load("syllabary"),
             corpora=[jp.read_corpus(p) for p in fr.corpus_paths(spec, None)],
             base={"N": len(toks), "K": len(set(toks)), "lengths": [len(m) for m in msgs],
                   "target_msgs": msgs, "messages_independent": "separate" in mode})


def shuffle_msgs(msgs, k):
    toks = [t for m in msgs for t in m]
    random.Random(k).shuffle(toks)
    out, pos = [], 0
    for m in msgs:
        out.append(toks[pos:pos + len(m)]); pos += len(m)
    return out


def per_tok(sc, msgs):
    return sc / max(1, sum(len(m) for m in msgs))


def control(noise, s):
    p = dict(G["base"], err=noise)
    cm, plain, train = G["fam"].make_control(G["spec"], s, G["corpora"], dict(p))
    return cm, plain, train, p


def job(j):
    kind, noise, s, k = j
    fam, spec = G["fam"], G["spec"]
    if kind == "target":
        _, sc, _ = fam.solve(G["msgs"], spec, 1, 8, G["corpora"], dict(G["base"]))
        return (kind, "-", 1, 0, per_tok(sc, G["msgs"]), "-")
    if kind == "shuf":
        sm = shuffle_msgs(G["msgs"], k)
        _, sc, _ = fam.solve(sm, spec, k, 8, G["corpora"], dict(G["base"]))
        return (kind, "-", 1, k, per_tok(sc, sm), "-")
    cm, plain, train, p = control(noise, s)
    if kind in ("ctrl", "power"):
        dec, sc, _ = fam.solve(cm, spec, s, 8, train, dict(p))
        return (kind, noise, s, 0, per_tok(sc, cm), "%.3f" % fam.score_recovery(dec, plain))
    # power-shuffle: control ciphertext s shuffled with seed k, solver seed k
    sm = shuffle_msgs(cm, k)
    _, sc, _ = fam.solve(sm, spec, k, 8, train, dict(p))
    return (kind, noise, s, k, per_tok(sc, sm), "-")


def pct(xs, q):  # ceil(q n)-th smallest
    xs = sorted(xs); return xs[max(1, math.ceil(q * len(xs))) - 1]


def main():
    jobs = [("target", "-", 1, 0)]
    jobs += [("ctrl", n, s, 0) for n in ("0.084", "0.107") for s in range(1, 21)]
    jobs += [("shuf", "-", 1, k) for k in range(1, 41)]
    jobs += [("power", "0.107", s, 0) for s in range(101, 111)]
    jobs += [("pshuf", "0.107", s, k) for s in range(101, 111) for k in range(1, 21)]
    with Pool(4, initializer=init) as pool:
        res = pool.map(job, jobs, chunksize=1)
    rows = ["kind\tnoise\tseed\tshuffle\tscore\trecovery"] + ["%s\t%s\t%d\t%d\t%.5f\t%s" % r for r in res]
    text = "\n".join(rows) + "\n"
    if "--check" in sys.argv:
        old = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
        sys.exit(0 if old == text else 1)
    open(OUT, "w", encoding="utf-8").write(text)
    report(res)


def report(res):
    T = [r[4] for r in res if r[0] == "target"][0]
    A = [r[4] for r in res if r[0] == "ctrl"]
    B = [r[4] for r in res if r[0] == "shuf"]
    a05, b95 = pct(A, 0.05), pct(B, 0.95)
    print(f"T={T:.4f}  (a) n={len(A)} min={min(A):.4f} p05={a05:.4f} max={max(A):.4f}  (b) n={len(B)} min={min(B):.4f} p95={b95:.4f} max={max(B):.4f}")
    for n in ("0.084", "0.107"):
        An = [r[4] for r in res if r[0] == "ctrl" and r[1] == n]
        print(f"  (a) noise {n}: {min(An):.4f}..{max(An):.4f}")
    print("TARGET:", "PASS" if (T > b95 and T >= a05) else "FAIL", f"(T>{b95:.4f}: {T > b95}; T>={a05:.4f}: {T >= a05})")
    print(f"  T pct in (a) {sum(x <= T for x in A)/len(A):.4f}; in (b) {sum(x <= T for x in B)/len(B):.4f}")
    fp = sum(B[i] > pct(B[:i] + B[i+1:], 0.95) and B[i] >= a05 for i in range(len(B)))
    print(f"  shuffled false-positive (leave-one-out): {fp}/{len(B)}")
    gated = passed = 0
    for r in [r for r in res if r[0] == "power"]:
        own = [x[4] for x in res if x[0] == "pshuf" and x[2] == r[2]]
        ok = r[4] > pct(own, 0.95) and r[4] >= a05
        rec = float(r[5])
        if rec >= 0.60:
            gated += 1; passed += ok
        print(f"  power seed {r[2]}: rec {rec:.4f} score {r[4]:.4f} own-shuf p95 {pct(own, 0.95):.4f} max {max(own):.4f} -> {'pass' if ok else 'fail'}")
    print(f"POWER: {passed}/{gated} gated held-out controls pass ->", "PASS" if gated and passed >= 0.8 * gated else "FAIL")


if __name__ == "__main__":
    if "--report" in sys.argv:
        res = []
        for line in open(OUT, encoding="utf-8").read().splitlines()[1:]:
            k, n, s, sh, sc, rec = line.split("\t"); res.append((k, n, int(s), int(sh), float(sc), rec))
        report(res)
    else:
        main()
