#!/usr/bin/env python3
"""RUN5-C1161RA (4 Oct 2026): joint re-anneal of the M signs (+ contested S 4, S) with the C and agreed S signs held.
Pre-registered in tx/PREREG_reanneal.md (pushed before any run). Outputs in two/ra/.

  python3 two/reanneal.py calib                  # W from held-out fr17 -> two/ra/calib.tsv
  python3 two/reanneal.py run --arm ctl|tgt --seeds 1-10 [--procs 4]   # -> two/ra/key_<arm>_sS.tsv, runs.tsv
  python3 two/reanneal.py score --arm ctl|tgt [--apply]                 # consensus + null -> two/ra/<arm>_signs.tsv
"""
import argparse, csv, glob, math, os, random, sys, time
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE); ROOT = os.path.dirname(os.path.dirname(T))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(ROOT, "tools"))
import two_instr as ti
OUT = os.path.join(HERE, "ra")
FR17 = sorted(glob.glob(os.path.join(ROOT, "tools/data/fr17/*.txt.gz")))
FR16 = sorted(glob.glob(os.path.join(ROOT, "tools/data/fr16/*.txt.gz")))
HELD = os.path.join(ROOT, "tools/data/fr17/lettresducardina01maza.txt.gz")
C_SIGNS = "a d e ee p sd".split()
S_HELD = "+ 3 7 9 box f iii q qb s tri w wb y".split()
FREE = "2 6 6r 8 K L Sorn blot c dia eloop iib l ls o phi psi rc rot spiralG sqc th to tz vdash x z 4 S".split()
PLANT = {"a": "e", "p": "e", "d": "e"}
L = "abcdefghijklmnopqrstuvwxyz"
RESTARTS, ITERS, ORDER, NMIN = 32, 40000, 4, 7

KEY = {r["sign"]: (r["value"], r["grade"]) for r in csv.DictReader(open(os.path.join(T, "key.tsv")), delimiter="\t")}
SEQ = [t for t in ti.stream() if t in KEY]
G = {}


def wc():
    import wordcover as w  # reuse RUN5-C1161WC's vocabulary and cover DP unchanged
    return w


def setup(arm):
    import homophonic_anneal as ha, judge_plaintext as jp
    w = wc(); w.init(w.vocab(FR17 + FR16))
    G["ha"], G["w"] = ha, w
    G["model"] = ha.Model([jp.read_corpus(p) for p in FR17], ORDER)
    G["W"] = float(open(os.path.join(OUT, "calib.tsv")).read().splitlines()[1].split("\t")[0])
    G["free"] = FREE + (list(PLANT) if arm == "ctl" else [])


def L4(text):
    m = G["model"]; o = m.order
    return sum(m.logp(text[i:i + o]) for i in range(len(text) - o + 1)) / len(text)


def J(key):
    t = "".join(key[s] for s in SEQ)
    return L4(t) + G["W"] * G["w"].cover(t)


def calib():
    import homophonic_anneal as ha, judge_plaintext as jp
    w = wc()
    w.init(w.vocab([p for p in FR17 + FR16 if p != HELD]))
    G["model"] = ha.Model([jp.read_corpus(p) for p in FR17 if p != HELD], ORDER)
    g = "".join(w.words(HELD))[300000:303375]
    sh = []
    for i in range(20):
        x = list(g); random.Random(i).shuffle(x); sh.append("".join(x))
    Lr, Cr = L4(g), w.cover(g)
    Ls = sum(map(L4, sh)) / 20; Cs = sum(map(w.cover, sh)) / 20
    W = (Lr - Ls) / (Cr - Cs)
    with open(os.path.join(OUT, "calib.tsv"), "w") as f:
        f.write("W\tL_real\tL_shuf\tC_real\tC_shuf\n" + f"{W:.5f}\t{Lr:.5f}\t{Ls:.5f}\t{Cr:.5f}\t{Cs:.5f}\n")
    print(open(os.path.join(OUT, "calib.tsv")).read())


def one(args):
    arm, seed = args
    setup(arm)
    ha = G["ha"]; free = G["free"]
    fixed = {s: v for s, (v, g) in KEY.items() if s not in free}
    init = {s: PLANT[s] for s in PLANT} if arm == "ctl" else None
    t0 = time.time()
    sc, key = ha.solve(SEQ, G["model"], RESTARTS, ITERS, seed, 1.0, fixed=fixed, init=init)[0]
    j0 = cur = J(key); rng = random.Random(seed); passes = 0
    for passes in range(1, 5):
        order = list(free); rng.shuffle(order); moved = False
        for s in order:
            old = key[s]; best, bl = cur, old
            for v in L:
                if v == old: continue
                key[s] = v; x = J(key)
                if x > best + 1e-12: best, bl = x, v
            key[s] = bl
            if bl != old: cur = best; moved = True
        if not moved: break
    with open(os.path.join(OUT, f"key_{arm}_s{seed}.tsv"), "w") as f:
        f.write("sign\tvalue\n" + "".join(f"{s}\t{key[s]}\n" for s in sorted(key)))
    return [time.strftime("%Y-%m-%d %H:%M", time.gmtime()), arm, seed, len(SEQ), f"{sc:.1f}", f"{j0:.5f}", f"{cur:.5f}",
            passes, f"{time.time()-t0:.0f}s"]


def run(arm, seeds, procs):
    with Pool(procs) as p:
        for row in p.imap_unordered(one, [(arm, s) for s in seeds]):
            with open(os.path.join(OUT, "runs.tsv"), "a") as f:
                f.write("\t".join(map(str, row)) + "\n")
            print("\t".join(map(str, row)), flush=True)


def null_job(args):
    arm, kstar, s, A, B, i = args
    if "model" not in G: setup(arm)
    free = [x for x in G["free"] if x != s]
    vals = [kstar[x] for x in free]; random.Random(i).shuffle(vals)
    k = dict(kstar); k.update(zip(free, vals))
    k[s] = B; jb = J(k); k[s] = A
    return jb - J(k)


def score(arm, apply, procs):
    from collections import Counter
    setup(arm)
    keys = [dict(r.split("\t") for r in open(os.path.join(OUT, f"key_{arm}_s{s}.tsv")).read().splitlines()[1:])
            for s in range(1, 11)]
    cons = {}
    for s in G["free"]:
        c = Counter(k[s] for k in keys); v, n = c.most_common(1)[0]
        cons[s] = (v if n >= NMIN else None, n, v, dict(c))
    kstar = dict(keys[0]); kstar.update({s: c[0] for s, c in cons.items() if c[0]})
    cnt = Counter(SEQ); rows = []; jobs = []; plan = []
    for s in G["free"]:
        A = PLANT[s] if (arm == "ctl" and s in PLANT) else KEY[s][0]; B = cons[s][0]  # bugfix 13:19: non-planted free signs use key.tsv
        k = dict(kstar)
        if B and B != A:
            k[s] = B; jb = J(k); k[s] = A; d = jb - J(k); kind, alt = "change", B
        else:
            base = A; k[s] = base; ja = J(k); best = None
            for v in L:
                if v == base: continue
                k[s] = v; x = J(k)
                if best is None or x > best[0]: best = (x, v)
            d = ja - best[0]; kind, alt = "confirm", best[1]
        plan.append((s, A, B, kind, alt, d))
        jobs += [(arm, kstar, s, A, alt, i) for i in range(1, 51)]
    with Pool(procs) as p:
        res = p.map(null_job, jobs, chunksize=10)
    for n_, (s, A, B, kind, alt, d) in enumerate(plan):
        nl = sorted(res[n_ * 50:(n_ + 1) * 50])
        if kind == "change":
            p95 = nl[47]; ok = d > 0 and d > p95
        else:  # A vs best alternative: null of (alt - A) negated
            neg = sorted(-x for x in nl); p95 = neg[47]; ok = d > 0 and d > p95
        if arm == "ctl":
            true = KEY[s][0] if s in PLANT else None
            dec = ("recovered" if (B == true and ok) else "NOT recovered") if s in PLANT else "-"
        else:
            g = KEY[s][1]
            dec = (f"change {A}->{B}, grade S" if kind == "change" and ok else
                   ("M->S" if g == "M" else "S confirmed") if kind == "confirm" and B == A and ok else "no change")
        top = sorted(cons[s][3].items(), key=lambda x: -x[1])
        rows.append([s, cnt.get(s, 0), A, KEY[s][1] if s not in PLANT or arm == "tgt" else "C(planted)", B or "-", cons[s][1],
                     " ".join(f"{a}{b}" for a, b in top), kind, alt, f"{d:.5f}", f"{p95:.5f}", int(ok), dec])
    hdr = "sign\ttokens\tA\tgrade\tconsensus\tn\tvotes\tkind\tvs\tdJ\tnull_p95\tclears\tdecision\n"
    with open(os.path.join(OUT, f"{arm}_signs.tsv"), "w") as f:
        f.write(hdr + "".join("\t".join(map(str, r)) + "\n" for r in rows))
    print(open(os.path.join(OUT, f"{arm}_signs.tsv")).read())
    if arm == "ctl":
        rec = sum(1 for r in rows if r[-1] == "recovered")
        msg = f"planted control: {rec}/3 recovered -> " + ("GATE PASS" if rec >= 2 else "NON-TEST (target not run)")
        open(os.path.join(OUT, "ctl_gate.txt"), "w").write(msg + "\n"); print(msg)
    if apply and arm == "tgt":
        assert "GATE PASS" in open(os.path.join(OUT, "ctl_gate.txt")).read()
        lines = open(os.path.join(T, "key.tsv")).read().splitlines(); new = [lines[0]]
        dec = {r[0]: r for r in rows}
        for l in lines[1:]:
            s, v, g, src = l.split("\t")
            if s in dec and dec[s][-1] != "no change":
                r = dec[s]; note = f"RUN5-C1161RA re-anneal (tx/PREREG_reanneal.md): consensus '{r[4]}' {r[5]}/10, dJ {r[9]} > null p95 {r[10]}"
                if r[-1].startswith("change"):
                    note += f"; was '{v}' ({g})"; v = r[4]
                g = "S"; src = f"{src} || {note}"
            new.append("\t".join([s, v, g, src]))
        open(os.path.join(T, "key.tsv"), "w").write("\n".join(new) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["calib", "run", "score"])
    ap.add_argument("--arm", choices=["ctl", "tgt"], default="ctl")
    ap.add_argument("--seeds", default="1-10"); ap.add_argument("--procs", type=int, default=4)
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args(); os.makedirs(OUT, exist_ok=True)
    if a.mode == "calib": calib()
    elif a.mode == "run":
        if a.arm == "tgt":
            assert "GATE PASS" in open(os.path.join(OUT, "ctl_gate.txt")).read(), "control gate not passed"
        lo, hi = map(int, a.seeds.split("-")); run(a.arm, range(lo, hi + 1), a.procs)
    else: score(a.arm, a.apply, a.procs)


if __name__ == "__main__":
    main()
