#!/usr/bin/env python3
"""NEAR3-C1POOL (4 Oct 2026): held-out test of key.tsv on the four new leaves, merge, gated pooled re-anneal.
Pre-registered in tx/PREREG_pool.md (pushed before any statistic was computed).

  python3 pool/pool.py build                 # pool/new_leaves.tsv: c186L, c187L, c187R, c188L in ciphertext.tsv columns
  python3 pool/pool.py time                  # one timing anneal (shuffled pooled stream, seed 99; not an arm)
  python3 pool/pool.py heldout               # step (a): real decode vs controls (i) and (ii) -> pool/heldout.tsv
  python3 pool/pool.py anneal --arm real --seed S         # step (b) real arm, seeds 1-5
  python3 pool/pool.py anneal --arm shuf --shuf K --seed S  # step (b) control: order-shuffled pooled stream K=1-5, seeds 1-2
Rows of (b) append to pool/anneal.tsv; keys to pool/key_<arm>_<...>.tsv.

Conventions (as transcribed, never repaired): 'ss' in the c187L/c187R/c188L files is written as two 's' rows (the
c185R/c186R convention: ciphertext.tsv has no 'ss'); 'PLAIN:x' -> '[PLAIN:x]'; '/' kept; NEW labels kept as their own
signs, the two leaf-local 'NEW1' renamed by leaf (NEW_c186L_1, NEW_c187L_1) since they are different shapes.
Unkeyed signs decode to '?' (dropped by the judge's fold) in every arm alike.
"""
import argparse, csv, json, os, random, sys, time
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE); ROOT = os.path.dirname(os.path.dirname(T))
sys.path.insert(0, os.path.join(ROOT, "tools")); sys.path.insert(0, os.path.join(T, "glossctl"))
SPEC = os.path.join(ROOT, "specs", "clair1161-avis-flandre-1688.json")
LEAVES = ["c186L", "c187L", "c187R", "c188L"]
C_SIGNS = ["a", "d", "e", "ee", "p", "sd"]  # READ2-C1161B strict gloss repair, grade C
RESTARTS = int(os.environ.get("POOL_RESTARTS", "32")); ITERS = 40000


def is_cipher(s):
    return s != "/" and not s.startswith("[")


def c186L_rows():
    draft = {}
    for r in csv.DictReader(open(os.path.join(T, "tx", "c186L_rec", "ciphertext_draft.tsv")), delimiter="\t"):
        draft.setdefault(r["line"], []).append(r)
    out = []
    for ln in open(os.path.join(T, "tx", "c186L_rec.tsv")).read().splitlines()[1:]:
        row, codes = ln.split("\t")[:2]
        toks = codes.split(); d = draft.get(row, [])
        same = [x["sign"] for x in d] == toks
        for i, t in enumerate(toks):
            conf = d[i]["confidence"] if same else "H"
            note = (d[i]["why"] if same else "c186L_rec.tsv (line settled in reconciliation; draft conf not aligned)")
            if (row, i + 1) in (("L05", 8), ("L07", 21)):
                conf, note = "M", "M per NEAR3-C1TX-c186L report"
            out.append([f"c186L_{row}", t, conf, note])
    return out


def long_rows(leaf):
    return [[r["line"], r["sign"], r["conf"], r["note"]]
            for r in csv.DictReader(open(os.path.join(T, "tx", f"{leaf}_rec_long.tsv")), delimiter="\t")]


def build():
    rows = []
    for leaf in LEAVES:
        src = c186L_rows() if leaf == "c186L" else long_rows(leaf)
        for line, s, conf, note in src:
            if s == "NEW1":
                s = f"NEW_{leaf}_1"
            if s.startswith("PLAIN:"):
                s = f"[{s}]"
            if s == "ss":
                rows += [[line, "s", conf, (note + "; " if note else "") + "ss written as s s"]] * 2
                continue
            rows.append([line, s, conf, note])
    out, pos, last = [], 0, None
    for line, s, conf, note in rows:
        pos = pos + 1 if line == last else 1; last = line
        out.append([line, str(pos), s, conf, note])
    with open(os.path.join(HERE, "new_leaves.tsv"), "w") as f:
        f.write("line\tpos\tsign\tconf\tnote\n" + "".join("\t".join(r) + "\n" for r in out))
    n = sum(is_cipher(r[2]) for r in out)
    print(f"new_leaves.tsv: {len(out)} rows, {n} cipher signs;",
          {l: sum(is_cipher(r[2]) for r in out if r[0].startswith(l)) for l in LEAVES})


def new_rows():
    return list(csv.DictReader(open(os.path.join(HERE, "new_leaves.tsv")), delimiter="\t"))


def old_rows():
    return list(csv.DictReader(open(os.path.join(T, "ciphertext.tsv")), delimiter="\t"))


def leaf_toks(rows, leaf):
    return [r["sign"] for r in rows if r["line"].startswith(leaf) and is_cipher(r["sign"])]


def read_key(p):
    return {r["sign"]: r["value"] for r in csv.DictReader(open(p), delimiter="\t")}


def dec(key, toks):
    return "".join(key.get(t, "?") for t in toks)


def model_and_judge():
    import judge_plaintext as jp
    spec = json.load(open(SPEC))
    jp._ALPHA = jp._resolve_alphabet((spec.get("judge") or {}).get("alphabet"))
    m = jp.NgramModel([jp.read_corpus(os.path.join(ROOT, p)) for p in spec["judge"]["corpora"]])
    return jp, spec, m


def heldout():
    os.chdir(ROOT)
    jp, spec, m = model_and_judge()
    key = read_key(os.path.join(T, "key.tsv"))
    shuf = [read_key(os.path.join(T, "glossctl", f"key_shuf{k}.tsv")) for k in range(1, 21)]
    rows = new_rows()
    per = {l: leaf_toks(rows, l) for l in LEAVES}
    sets = {"pooled4": LEAVES, "pooled3_no_c188L": LEAVES[:3], **{l: [l] for l in LEAVES}}
    out = []
    for name, ls in sets.items():
        toks = [t for l in ls for t in per[l]]
        real = dec(key, toks)
        J = jp.judge(spec, real)
        L, W = J["checks"]["language"], J["checks"]["words"]
        letters = jp.fold(real)
        # (i) same key on each leaf's order-shuffled signs (shuffle within leaf), 20 seeds
        ci_s, ci_c = [], []
        for s in range(1, 21):
            st = []
            for l in ls:
                x = per[l][:]; random.Random(s * 100 + LEAVES.index(l)).shuffle(x); st += x
            lt = jp.fold(dec(key, st)); ci_s.append(m.score(lt)); ci_c.append(m.cover(lt))
        # (ii) 20 shuffled-ciphertext anneal keys on the unshuffled leaves
        cii_s, cii_c = [], []
        for k in shuf:
            lt = jp.fold(dec(k, toks)); cii_s.append(m.score(lt)); cii_c.append(m.cover(lt))
        p95 = lambda v: sorted(v)[18]  # 19th of 20
        ps, pc = max(cii_s), max(cii_c)
        rs, rc = m.score(letters), m.cover(letters)
        ok = rs > max(ps, p95(ci_s)) and rc > max(pc, p95(ci_c))
        unk = sum(t not in key for t in toks)
        r = [name, len(toks), unk, len(letters), f"{rs:.3f}", f"{rc:.3f}", f"{p95(ci_s):.3f}", f"{max(ci_s):.3f}",
             f"{p95(ci_c):.3f}", f"{ps:.3f}", f"{sorted(cii_s)[10]:.3f}", f"{pc:.3f}",
             "PASS" if ok else "FAIL", f"judge {'PASS' if J['pass'] else 'FAIL'} lang {L['score']} null_p99 {L['null_p99']} "
             f"real_p05 {L['real_p05']} N {L['N']}; cover {W['cover']}"]
        out.append(r); print("\t".join(map(str, r)), flush=True)
        open(os.path.join(HERE, f"heldout_{name}.txt"), "w").write(real + "\n")
    with open(os.path.join(HERE, "heldout.tsv"), "w") as f:
        f.write("set\tsigns\tunkeyed\tletters\treal_score\treal_cover\ti_p95_score\ti_max_score\ti_p95_cover\t"
                "ii_max_score\tii_median_score\tii_max_cover\tgate\tjudge_line\n")
        f.write("".join("\t".join(map(str, r)) + "\n" for r in out))


def pooled_stream():
    """All six leaves in ciphertext order: c185R, c186R block (ciphertext.tsv), then the four new leaves."""
    old = [r["sign"] for r in old_rows() if r["line"][:5] in ("c185R", "c186R") and is_cipher(r["sign"])]
    assert len(old) == 924, len(old)
    return old + [r["sign"] for r in new_rows() if is_cipher(r["sign"])]


def anneal(arm, seed, shuf, timing=False):
    os.chdir(ROOT)
    import homophonic_anneal as ha, family_run as fr, judge_plaintext as jp
    from glossctl import gloss_letters, stat
    spec = json.load(open(SPEC))
    model = ha.Model([jp.read_corpus(p) for p in fr.corpus_paths(spec, None)], 3)
    key0 = read_key(os.path.join(T, "key.tsv"))
    fixed = {s: key0[s] for s in C_SIGNS}
    seq = pooled_stream()
    if arm == "shuf":
        random.Random(shuf).shuffle(seq)
    t0 = time.time()
    sc, key = ha.solve(seq, model, RESTARTS, ITERS, seed, 1.0, fixed=fixed)[0]
    el = time.time() - t0
    if timing:
        print(f"timing: one anneal, {len(seq)} signs, K {len(set(seq))}, restarts {RESTARTS}: {el:.0f}s"); return
    old = old_rows()
    blk = [r["sign"] for r in old if r["line"].startswith("c186R") and is_cipher(r["sign"])]
    c185 = [r["sign"] for r in old if r["line"].startswith("c185R") and is_cipher(r["sign"])]
    g = stat(dec(key, blk), gloss_letters())
    tag = f"real_s{seed}" if arm == "real" else f"shuf{shuf}_s{seed}"
    with open(os.path.join(HERE, f"key_{tag}.tsv"), "w") as f:
        f.write("sign\tvalue\n" + "".join(f"{s}\t{v}\n" for s, v in sorted(key.items())))
    j185 = j924 = "-"
    if arm == "real":
        spec2 = json.load(open(SPEC))
        j185 = jp.judge(spec2, dec(key, c185))["checks"]["language"]["score"]
        j924 = jp.judge(spec2, dec(key, c185 + blk))["checks"]["language"]["score"]
    row = [time.strftime("%Y-%m-%d %H:%M", time.gmtime()), arm, shuf or "-", seed, RESTARTS, len(seq), len(set(seq)),
           f"{sc:.1f}", f"{g:.4f}", j185, j924, f"{el:.0f}s"]
    p = os.path.join(HERE, "anneal.tsv"); new = not os.path.exists(p)
    with open(p, "a") as f:
        if new:
            f.write("utc\tarm\tshuffle\tseed\trestarts\tN\tK\tanneal_score\tgloss_match\tc185R_judge\tc185R+c186R_judge\ttime\n")
        f.write("\t".join(map(str, row)) + "\n")
    print("\t".join(map(str, row)), flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["build", "time", "heldout", "anneal"])
    ap.add_argument("--arm", choices=["real", "shuf"], default="real")
    ap.add_argument("--seed", type=int, default=1); ap.add_argument("--shuf", type=int, default=0)
    a = ap.parse_args()
    if a.mode == "build": build()
    elif a.mode == "time": anneal("shuf", 99, 99, timing=True)
    elif a.mode == "heldout": heldout()
    else: anneal(a.arm, a.seed, a.shuf)


if __name__ == "__main__":
    main()
