#!/usr/bin/env python3
"""C1161-LOLO step 1 (4 Oct 2026, account-3 Fable worker): why did the joint re-anneal's planted control fail 0/3 under
both norms? Disk only. Reuses two/reanneal.py's objective (same stream, model, W, vocabulary) unchanged.

  python3 two/lolo_diag.py rank            # D1: J / 4-gram-only of key.tsv vs the 20 control keys, both norms -> two/lolo/rank.tsv
  python3 two/lolo_diag.py cond            # D2: each free sign's key.tsv letter ranked among 26 given key.tsv context -> cond.tsv
  python3 two/lolo_diag.py ascent          # D3: coordinate ascent from key.tsv (truth-start): what drifts -> ascent.tsv
  python3 two/lolo_diag.py synth --norm none|nc2 --seeds 1-3 [--free all|top8]   # D4: same-design synthetic control -> synth.tsv
"""
import argparse, csv, os, random, sys, time
from collections import Counter
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE); ROOT = os.path.dirname(os.path.dirname(T))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(ROOT, "tools"))
import reanneal as ra
OUT = os.path.join(HERE, "lolo"); os.makedirs(OUT, exist_ok=True)
L = ra.L
TRUE = {s: v for s, (v, g) in ra.KEY.items()}
FREE32 = ra.FREE + list(ra.PLANT)


def use(norm):
    ra.NORM = norm; ra.OUT = os.path.join(HERE, "ra" if norm == "none" else "ra_nc2"); ra.setup("ctl")


def l4only(key):
    return ra.L4("".join(key[s] for s in ra.SEQ))


def rank():
    rows = []
    for norm in ("none", "nc2"):
        use(norm)
        planted = dict(TRUE); planted.update(ra.PLANT)
        cands = [("key.tsv", TRUE), ("key.tsv+apd=e", planted)]
        for s in range(1, 11):
            p = os.path.join(ra.OUT, f"key_ctl_s{s}.tsv")
            cands.append((f"ctl_s{s}", dict(r.split("\t") for r in open(p).read().splitlines()[1:])))
        for name, k in cands:
            t = "".join(k[s] for s in ra.SEQ)
            rows.append([norm, name, f"{ra.L4(t):.5f}", f"{ra.G['w'].cover(t):.5f}", f"{ra.J(k):.5f}",
                         sum(1 for s in FREE32 if k[s] != TRUE[s]), " ".join(f"{s}={k[s]}" for s in ra.PLANT)])
    hdr = "norm\tkey\tL4\tcover\tJ\tfree32_differ_from_key.tsv\tapd\n"
    open(os.path.join(OUT, "rank.tsv"), "w").write(hdr + "".join("\t".join(map(str, r)) + "\n" for r in rows))
    print(hdr + "".join("\t".join(map(str, r)) + "\n" for r in rows))


def cond():
    cnt = Counter(ra.SEQ); rows = []
    for norm in ("none", "nc2"):
        use(norm)
        for s in FREE32:
            k = dict(TRUE); sc = {}
            for v in L:
                k[s] = v; sc[v] = (l4only(k), ra.J(k))
            r4 = sorted(L, key=lambda v: -sc[v][0]); rj = sorted(L, key=lambda v: -sc[v][1])
            rows.append([norm, s, cnt[s], ra.KEY[s][1], TRUE[s], r4.index(TRUE[s]) + 1, r4[0], f"{sc[r4[0]][0]-sc[TRUE[s]][0]:.4f}",
                         rj.index(TRUE[s]) + 1, rj[0], f"{sc[rj[0]][1]-sc[TRUE[s]][1]:.4f}"])
    hdr = "norm\tsign\ttokens\tgrade\tkey.tsv\trank_4gram\targmax_4gram\tgap_4gram\trank_J\targmax_J\tgap_J\n"
    open(os.path.join(OUT, "cond.tsv"), "w").write(hdr + "".join("\t".join(map(str, r)) + "\n" for r in rows))
    print(hdr + "".join("\t".join(map(str, r)) + "\n" for r in rows))


def ascent():
    rows = []
    for norm in ("none", "nc2"):
        use(norm)
        for obj in ("4gram", "J"):
            f = l4only if obj == "4gram" else ra.J
            key = dict(TRUE); cur = f(key); rng = random.Random(1); passes = 0; moves = []
            for passes in range(1, 5):
                order = list(FREE32); rng.shuffle(order); moved = False
                for s in order:
                    old = key[s]; best, bl = cur, old
                    for v in L:
                        if v == old: continue
                        key[s] = v; x = f(key)
                        if x > best + 1e-12: best, bl = x, v
                    key[s] = bl
                    if bl != old: cur = best; moved = True; moves.append(f"{s}:{old}>{bl}")
                if not moved: break
            drift = [s for s in FREE32 if key[s] != TRUE[s]]
            rows.append([norm, obj, f"{f(TRUE):.5f}", f"{cur:.5f}", passes, len(drift),
                         " ".join(f"{s}={key[s]}" for s in ra.PLANT), " ".join(moves)])
    hdr = "norm\tobjective\tstart\tend\tpasses\tn_drift_of_32\tapd_end\tmoves_in_order\n"
    open(os.path.join(OUT, "ascent.tsv"), "w").write(hdr + "".join("\t".join(map(str, r)) + "\n" for r in rows))
    print(hdr + "".join("\t".join(map(str, r)) + "\n" for r in rows))


TOP8 = "th z o phi ls 6r eloop iib".split()


def synth_build(seed):
    """Same design as key.tsv: one synthetic sign per key.tsv sign, letters' homophone sets and per-sign token shares
    copied from key.tsv x the target stream; held-out fr17 text (the W-calibration passage) as plaintext. Letters the
    design lacks (b g? no: b k w z after fold j>i v>u) get one extra HELD sign each (eases the synthetic; noted)."""
    import wordcover as w
    g = "".join(w.words(ra.HELD))[300000:300000 + len(ra.SEQ)]
    cnt = Counter(ra.SEQ); rng = random.Random(seed)
    by = {}
    for s, v in TRUE.items(): by.setdefault(v, []).append(s)
    truth = dict(TRUE); extra = []
    for a in sorted(set(g) - set(by)):
        by[a] = [f"X{a}"]; truth[f"X{a}"] = a; extra.append(f"X{a}")
    seq = [rng.choices(by[a], [cnt.get(s, 1) for s in by[a]])[0] for a in g]
    return seq, g, truth, extra


def synth_one(args):
    norm, seed, free = args
    import homophonic_anneal as ha
    use(norm)
    seq, g, truth, extra = synth_build(seed)
    freeset = (ra.FREE if free == "all" else TOP8) + list(ra.PLANT)
    fixed = {s: v for s, v in truth.items() if s not in freeset}
    init = dict(ra.PLANT)
    t0 = time.time()
    sc, key = ha.solve(seq, ra.G["model"], ra.RESTARTS, ra.ITERS, seed, 1.0, fixed=fixed, init=init, norm=norm)[0]
    c = Counter(seq)
    ok_signs = sum(1 for s in freeset if key[s] == truth[s]); ok_tok = sum(c[s] for s in freeset if key[s] == truth[s])
    tot_tok = sum(c[s] for s in freeset)
    plant = " ".join(f"{s}={key[s]}({'ok' if key[s]==truth[s] else 'x'})" for s in ra.PLANT)
    dec = "".join(key[s] for s in seq)
    letters_ok = sum(1 for a, b in zip(dec, g) if a == b) / len(g)
    return [norm, free, seed, len(seq), len(freeset), f"{sc:.1f}", ok_signs, f"{ok_tok}/{tot_tok}", f"{letters_ok:.3f}", plant,
            " ".join(f"{s}:{truth[s]}>{key[s]}" for s in freeset if key[s] != truth[s]), f"{time.time()-t0:.0f}s"]


def synth(norm, seeds, free, procs):
    hdr = "norm\tfree\tseed\tN\tn_free\tscore\tfree_signs_right\tfree_tokens_right\tletters_right\tplanted\twrong_signs\ttime\n"
    p = os.path.join(OUT, "synth.tsv")
    if not os.path.exists(p): open(p, "w").write(hdr)
    with Pool(procs) as pool:
        for row in pool.imap_unordered(synth_one, [(norm, s, free) for s in seeds]):
            open(p, "a").write("\t".join(map(str, row)) + "\n"); print("\t".join(map(str, row)), flush=True)


def stage1(norm, seed):
    """D5: the PREREG's stage 1 alone (4-gram anneal, no cover) on the real control arm -- the key reanneal.py did not
    save. Reports planted recovery and how far it sits from key.tsv."""
    import homophonic_anneal as ha
    use(norm)
    fixed = {s: v for s, v in TRUE.items() if s not in FREE32}
    t0 = time.time()
    sc, key = ha.solve(ra.SEQ, ra.G["model"], ra.RESTARTS, ra.ITERS, seed, 1.0, fixed=fixed, init=dict(ra.PLANT), norm=norm)[0]
    with open(os.path.join(OUT, f"stage1_{norm}_s{seed}.tsv"), "w") as f:
        f.write("sign\tvalue\n" + "".join(f"{s}\t{key[s]}\n" for s in sorted(key)))
    row = [norm, seed, f"{sc:.1f}", f"{l4only(key):.5f}", " ".join(f"{s}={key[s]}" for s in ra.PLANT),
           sum(1 for s in FREE32 if key[s] != TRUE[s]), " ".join(f"{s}:{TRUE[s]}>{key[s]}" for s in ra.FREE if key[s] != TRUE[s]),
           f"{time.time()-t0:.0f}s"]
    p = os.path.join(OUT, "stage1.tsv")
    if not os.path.exists(p): open(p, "w").write("norm\tseed\tscore\tL4\tapd\tdiffer_of_32\tmoved_free\ttime\n")
    open(p, "a").write("\t".join(map(str, row)) + "\n"); print("\t".join(map(str, row)))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["rank", "cond", "ascent", "synth", "stage1"])
    ap.add_argument("--norm", default="none"); ap.add_argument("--seeds", default="1-3")
    ap.add_argument("--free", default="all", choices=["all", "top8"]); ap.add_argument("--procs", type=int, default=4)
    a = ap.parse_args()
    if a.mode == "synth":
        lo, hi = map(int, a.seeds.split("-")); synth(a.norm, range(lo, hi + 1), a.free, a.procs)
    elif a.mode == "stage1":
        stage1(a.norm, int(a.seeds.split("-")[0]))
    else:
        globals()[a.mode]()
