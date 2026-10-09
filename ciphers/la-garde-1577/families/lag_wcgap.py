#!/usr/bin/env python3
"""LAG-RESCORE (9 Oct 2026): the wordcode score-gap gate at err 0.071 on the LAG-V2 spec (PREREG-LAG-WC.md, Amendment 1).

Statistic J = the spec judge's language score of a decode (judge_plaintext NgramModel over the spec's judge corpora, scored on
fold(decode text), the text being wordcode.split_decode joined by newlines -- the number judge_plaintext.py prints). T = target
(solver seed 1); (a) 40 controls at err 0.071 (seeds 1-40); (b) 40 shuffled targets (shuffle seed k, solver seed k); power:
10 held-out controls at err 0.071 (seeds 101-110) each against the max of 10 own shuffles and p05(a). PASS iff J(T) > p95(b)
and J(T) >= p05(a); gap = J(T) - mean J(a). Writes families/lag_wcgap.tsv; --report re-prints; --check re-solves and exits 1
if the committed TSV differs. CPU only, 4 processes.
"""
import os, sys, json, math, random
from multiprocessing import Pool
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import family_run as fr  # noqa: E402
import families  # noqa: E402
import judge_plaintext as jp  # noqa: E402

SPEC = os.path.join(ROOT, "specs", "la-garde-1577.json")
OUT = os.path.join(os.path.dirname(__file__), "lag_wcgap.tsv")
ERR = "0.071"
G = {}


def init():
    os.chdir(ROOT)
    spec = json.load(open(SPEC, encoding="utf-8"))
    msgs, mode = fr.read_spec_cipher(spec, "space")
    toks = [t for m in msgs for t in m]
    corpora = [jp.read_corpus(p) for p in fr.corpus_paths(spec, None)]
    jcorp = [jp.read_corpus(p) for p in spec["judge"]["corpora"]]
    G.update(spec=spec, msgs=msgs, fam=families.load("wordcode"), corpora=corpora, model=jp.NgramModel(jcorp),
             base={"N": len(toks), "K": len(set(toks)), "lengths": [len(m) for m in msgs], "target_msgs": msgs,
                   "messages_independent": "separate" in mode, "codes": "marked", "err": float(ERR)})


def shuffle_msgs(msgs, k):
    toks = [t for m in msgs for t in m]
    random.Random(k).shuffle(toks)
    out, pos = [], 0
    for m in msgs:
        out.append(toks[pos:pos + len(m)]); pos += len(m)
    return out


def J(dec, msgs):
    lines = G["fam"].split_decode(dec, msgs)
    if lines is None:
        lines, pos = [], 0
        for m in msgs:
            lines.append(dec[pos:pos + len(m)]); pos += len(m)
    return G["model"].score(jp.fold("\n".join(lines)))


def job(j):
    kind, noise, s, k = j
    fam, spec = G["fam"], G["spec"]
    if kind == "target":
        dec, _, _ = fam.solve(G["msgs"], spec, 1, 8, G["corpora"], dict(G["base"]))
        return (kind, "-", 1, 0, J(dec, G["msgs"]), "-")
    if kind == "shuf":
        sm = shuffle_msgs(G["msgs"], k)
        dec, _, _ = fam.solve(sm, spec, k, 8, G["corpora"], dict(G["base"]))
        return (kind, "-", 1, k, J(dec, sm), "-")
    p = dict(G["base"], err=float(noise))
    cm, plain, train = fam.make_control(spec, s, G["corpora"], dict(p))
    if kind in ("ctrl", "power"):
        dec, _, _ = fam.solve(cm, spec, s, 8, train, dict(p))
        return (kind, noise, s, 0, J(dec, cm), "%.3f" % fam.score_recovery(dec, plain))
    sm = shuffle_msgs(cm, k)
    dec, _, _ = fam.solve(sm, spec, k, 8, train, dict(p))
    return (kind, noise, s, k, J(dec, sm), "-")


def pct(xs, q):  # ceil(q n)-th smallest
    xs = sorted(xs); return xs[max(1, math.ceil(q * len(xs))) - 1]


def main():
    jobs = [("target", "-", 1, 0)]
    jobs += [("ctrl", ERR, s, 0) for s in range(1, 41)]
    jobs += [("shuf", "-", 1, k) for k in range(1, 41)]
    jobs += [("power", ERR, s, 0) for s in range(101, 111)]
    jobs += [("pshuf", ERR, s, k) for s in range(101, 111) for k in range(1, 11)]
    with Pool(4, initializer=init) as pool:
        res = pool.map(job, jobs, chunksize=1)
    rows = ["kind\tnoise\tseed\tshuffle\tJ\trecovery"] + ["%s\t%s\t%d\t%d\t%.5f\t%s" % r for r in res]
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
    recA = [float(r[5]) for r in res if r[0] == "ctrl"]
    a05, b95, am = pct(A, 0.05), pct(B, 0.95), sum(A) / len(A)
    print(f"J(T)={T:.4f}  (a) n={len(A)} min={min(A):.4f} p05={a05:.4f} mean={am:.4f} max={max(A):.4f}; recovery mean {sum(recA)/len(recA):.3f},"
          f" {sum(x >= 0.6 for x in recA)}/{len(recA)} >= 0.60")
    print(f"  (b) n={len(B)} min={min(B):.4f} p95={b95:.4f} max={max(B):.4f}")
    print(f"  gap = J(T) - mean J(a) = {T - am:.4f}; PASS threshold on gap (p05(a) - mean) = {a05 - am:.4f}")
    print("TARGET:", "PASS" if (T > b95 and T >= a05) else "FAIL", f"(J(T)>{b95:.4f}: {T > b95}; J(T)>={a05:.4f}: {T >= a05})")
    print(f"  J(T) pct in (a) {sum(x <= T for x in A)/len(A):.4f}; in (b) {sum(x <= T for x in B)/len(B):.4f}")
    fp = sum(B[i] > pct(B[:i] + B[i+1:], 0.95) and B[i] >= a05 for i in range(len(B)))
    reach = sum(b >= a05 for b in B)
    print(f"  ARM-C1: shuffled decodes at or above p05(a): {reach}/{len(B)}; leave-one-out false-positive {fp}/{len(B)} ->",
          "judge VOID as gate" if fp > 2 else "judge usable")
    gated = passed = 0
    for r in [r for r in res if r[0] == "power"]:
        own = [x[4] for x in res if x[0] == "pshuf" and x[2] == r[2]]
        ok = r[4] > pct(own, 0.95) and r[4] >= a05
        rec = float(r[5])
        if rec >= 0.60:
            gated += 1; passed += ok
        print(f"  power seed {r[2]}: rec {rec:.4f} J {r[4]:.4f} own-shuf max {pct(own, 0.95):.4f} -> {'pass' if ok else 'fail'}")
    print(f"POWER: {passed}/{gated} gated held-out controls pass ->", "PASS" if gated >= 5 and passed >= 0.8 * gated else "FAIL")


if __name__ == "__main__":
    if "--report" in sys.argv:
        res = []
        for line in open(OUT, encoding="utf-8").read().splitlines()[1:]:
            k, n, s, sh, sc, rec = line.split("\t"); res.append((k, n, int(s), int(sh), float(sc), rec))
        report(res)
    else:
        main()
