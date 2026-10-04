#!/usr/bin/env python3
"""C1161-LOLO step 1 (4 Oct 2026, account-3 Fable worker): why did the joint re-anneal's planted control fail 0/3 under
both norms? Disk only. Reuses two/reanneal.py's objective (same stream, model, W, vocabulary) unchanged.

  python3 two/lolo_diag.py rank            # D1: J / 4-gram-only of key.tsv vs the 20 control keys, both norms -> two/lolo/rank.tsv
  python3 two/lolo_diag.py cond            # D2: each free sign's key.tsv letter ranked among 26 given key.tsv context -> cond.tsv
  python3 two/lolo_diag.py ascent          # D3: coordinate ascent from key.tsv (truth-start): what drifts -> ascent.tsv
  python3 two/lolo_diag.py synth --norm none|nc2 --seeds 1-3 [--free all|top8]   # D4: same-design synthetic control -> synth.tsv
  python3 two/lolo_diag.py stage1|blind --norm none --seeds 1   # D5 stage 1 alone on the real control arm; D7 nothing held
  python3 two/lolo_diag.py noise                                # D6 error bracket
  python3 two/lolo_diag.py lolo_run --arm ctl|tgt; lolo_score --arm ctl|tgt   # step 2, tx/PREREG_reanneal_lolo.md
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

def noise():
    """D6: error bracket (rule 3, SALV-DIAG shape): the 4-gram score per letter that genuine French of this length reaches
    when a share q of signs is misread (random other letter), vs the real stream under key.tsv and under the anneal's optimum."""
    import wordcover as w
    use("none")
    g = "".join(w.words(ra.HELD))[300000:300000 + len(ra.SEQ)]
    rows = []
    for q in (0.0, 0.05, 0.084, 0.10, 0.146, 0.20, 0.30, 0.50, 1.0):
        vals = []
        for seed in range(5):
            rng = random.Random(seed); t = list(g)
            for i in range(len(t)):
                if rng.random() < q: t[i] = rng.choice(L.replace(t[i], ""))
            vals.append(ra.L4("".join(t)))
        rows.append([q, f"{sum(vals)/5:.4f}", f"{min(vals):.4f}", f"{max(vals):.4f}"])
    hdr = "misread_share\tL4_mean\tmin\tmax\n"
    open(os.path.join(OUT, "noise.tsv"), "w").write(hdr + "".join("\t".join(map(str, r)) + "\n" for r in rows))
    print(hdr + "".join("\t".join(map(str, r)) + "\n" for r in rows))


def blind(norm, seed):
    """D7: nothing held -- the order-4 anneal on the real stream with all 49 signs free. What 4-gram score does the stream
    reach under ANY homophonic key, and how many of key.tsv's 19 held C/S signs does the blind optimum agree with?"""
    import homophonic_anneal as ha
    use(norm)
    t0 = time.time()
    sc, key = ha.solve(ra.SEQ, ra.G["model"], ra.RESTARTS, ra.ITERS, seed, 1.0, norm=norm)[0]
    with open(os.path.join(OUT, f"blind_{norm}_s{seed}.tsv"), "w") as f:
        f.write("sign\tvalue\n" + "".join(f"{s}\t{key[s]}\n" for s in sorted(key)))
    held = [s for s in TRUE if s not in FREE32]
    row = [norm, seed, f"{sc:.1f}", f"{l4only(key):.5f}", f"{sum(1 for s in held if key[s]==TRUE[s])}/{len(held)}",
           " ".join(f"{s}:{TRUE[s]}>{key[s]}" for s in held if key[s] != TRUE[s]),
           f"{sum(1 for s in FREE32 if key[s]==TRUE[s])}/32", f"{time.time()-t0:.0f}s"]
    p = os.path.join(OUT, "blind.tsv")
    if not os.path.exists(p): open(p, "w").write("norm\tseed\tscore\tL4\theld19_agree_key.tsv\theld_disagree\tfree32_agree\ttime\n")
    open(p, "a").write("\t".join(map(str, row)) + "\n"); print("\t".join(map(str, row)))


LEAVES = ("c185R", "c186R", "c186L", "c187L", "c187R", "c188L")
NLOLO = 5


def leaf_stream(drop):
    import two_instr as ti
    return [r["sign"] for r in ti.rows() if ti.is_cipher(r["sign"]) and r["sign"] in ra.KEY and r["line"][:5] != drop]


def lolo_one(args):
    """Step 2 (tx/PREREG_reanneal_lolo.md): stage 1 only, norm none, one leaf dropped, seed 1."""
    arm, drop = args
    import homophonic_anneal as ha
    use("none")
    free = ra.FREE + (list(ra.PLANT) if arm == "ctl" else [])
    fixed = {s: v for s, v in TRUE.items() if s not in free}
    init = dict(ra.PLANT) if arm == "ctl" else None
    seq = leaf_stream(drop); t0 = time.time()
    sc, key = ha.solve(seq, ra.G["model"], ra.RESTARTS, ra.ITERS, 1, 1.0, fixed=fixed, init=init, norm="none")[0]
    with open(os.path.join(OUT, f"key_lolo_{arm}_{drop}.tsv"), "w") as f:
        f.write("sign\tvalue\n" + "".join(f"{s}\t{key[s]}\n" for s in sorted(key)))
    return [time.strftime("%Y-%m-%d %H:%M", time.gmtime()), arm, drop, len(seq), f"{sc:.1f}", f"{l4only(key):.5f}",
            " ".join(f"{s}={key[s]}" for s in ra.PLANT), sum(1 for s in free if key[s] != TRUE[s]), f"{time.time()-t0:.0f}s"]


def lolo_run(arm, procs):
    if arm == "tgt":
        assert "GATE PASS" in open(os.path.join(OUT, "lolo_ctl_gate.txt")).read(), "control gate not passed"
    p = os.path.join(OUT, "lolo_runs.tsv")
    if not os.path.exists(p): open(p, "w").write("time\tarm\tdropped\tN\tscore\tL4_full_stream\tapd\tfree_differ_key.tsv\ttime\n")
    with Pool(procs) as pool:
        for row in pool.imap_unordered(lolo_one, [(arm, d) for d in LEAVES]):
            open(p, "a").write("\t".join(map(str, row)) + "\n"); print("\t".join(map(str, row)), flush=True)


def lolo_null(args):
    kstar, free, s, A, B, i = args
    if "model" not in ra.G: use("none")
    oth = [x for x in free if x != s]; vals = [kstar[x] for x in oth]; random.Random(i).shuffle(vals)
    k = dict(kstar); k.update(zip(oth, vals)); k[s] = B; jb = l4only(k); k[s] = A
    return jb - l4only(k)


def lolo_score(arm, procs):
    use("none")
    free = ra.FREE + (list(ra.PLANT) if arm == "ctl" else [])
    keys = [dict(r.split("\t") for r in open(os.path.join(OUT, f"key_lolo_{arm}_{d}.tsv")).read().splitlines()[1:]) for d in LEAVES]
    cons = {}
    for s in free:
        c = Counter(k[s] for k in keys); v, n = c.most_common(1)[0]; cons[s] = (v if n >= NLOLO else None, n, dict(c))
    kstar = dict(keys[0]); kstar.update({s: c[0] for s, c in cons.items() if c[0]})
    cnt = Counter(ra.SEQ); plan = []; jobs = []
    for s in free:
        A = ra.PLANT[s] if (arm == "ctl" and s in ra.PLANT) else TRUE[s]; B = cons[s][0]; k = dict(kstar)
        if B and B != A:
            k[s] = B; jb = l4only(k); k[s] = A; d = jb - l4only(k); kind, alt = "change", B
        else:
            k[s] = A; ja = l4only(k); best = None
            for v in L:
                if v == A: continue
                k[s] = v; x = l4only(k)
                if best is None or x > best[0]: best = (x, v)
            d = ja - best[0]; kind, alt = "confirm", best[1]
        plan.append((s, A, B, kind, alt, d)); jobs += [(kstar, free, s, A, alt, i) for i in range(1, 51)]
    with Pool(procs) as pool:
        res = pool.map(lolo_null, jobs, chunksize=10)
    rows = []
    for n_, (s, A, B, kind, alt, d) in enumerate(plan):
        nl = sorted(res[n_ * 50:(n_ + 1) * 50])
        p95 = nl[47] if kind == "change" else sorted(-x for x in nl)[47]; ok = d > 0 and d > p95
        if arm == "ctl":
            dec = (("recovered" if (B == TRUE[s] and ok) else "NOT recovered") if s in ra.PLANT else "-")
        else:
            dec = (f"proposal M: {A}->{B}" if kind == "change" and ok else
                   "key.tsv value is the leaf-stable optimum" if kind == "confirm" and B == A and ok else "no proposal")
        top = sorted(cons[s][2].items(), key=lambda x: -x[1])
        rows.append([s, cnt.get(s, 0), A, "C(planted)" if (arm == "ctl" and s in ra.PLANT) else ra.KEY[s][1], B or "-", cons[s][1],
                     " ".join(f"{a}{b}" for a, b in top), kind, alt, f"{d:.5f}", f"{p95:.5f}", int(ok), dec])
    hdr = "sign\ttokens\tA\tgrade\tconsensus\tleaves_agree\tvotes\tkind\tvs\tdL4\tnull_p95\tclears\tdecision\n"
    open(os.path.join(OUT, f"lolo_{arm}_signs.tsv"), "w").write(hdr + "".join("\t".join(map(str, r)) + "\n" for r in rows))
    print(hdr + "".join("\t".join(map(str, r)) + "\n" for r in rows))
    if arm == "ctl":
        rec = sum(1 for r in rows if r[-1] == "recovered")
        msg = f"LOLO planted control: {rec}/3 recovered -> " + ("GATE PASS" if rec >= 2 else "NON-TEST (target not run)")
        open(os.path.join(OUT, "lolo_ctl_gate.txt"), "w").write(msg + "\n"); print(msg)



if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["rank", "cond", "ascent", "synth", "stage1", "noise", "blind", "lolo_run", "lolo_score"])
    ap.add_argument("--arm", choices=["ctl", "tgt"], default="ctl")
    ap.add_argument("--norm", default="none"); ap.add_argument("--seeds", default="1-3")
    ap.add_argument("--free", default="all", choices=["all", "top8"]); ap.add_argument("--procs", type=int, default=4)
    a = ap.parse_args()
    if a.mode == "synth":
        lo, hi = map(int, a.seeds.split("-")); synth(a.norm, range(lo, hi + 1), a.free, a.procs)
    elif a.mode == "lolo_run":
        lolo_run(a.arm, a.procs)
    elif a.mode == "lolo_score":
        lolo_score(a.arm, a.procs)
    elif a.mode == "blind":
        blind(a.norm, int(a.seeds.split("-")[0]))
    elif a.mode == "stage1":
        stage1(a.norm, int(a.seeds.split("-")[0]))
    else:
        globals()[a.mode]()
