#!/usr/bin/env python3
"""RUN3-C1161MS (4 Oct 2026): multi-seed consensus instrument 2 for the M key signs. Pre-registered in
tx/PREREG_consensus.md (pushed 00c7cec4 before any anneal ran). Recipe and stream are two_instr.py's (N4-C1).

  python3 two/consensus.py anneal --arm real --seed S         # -> two/cons/key_real_sS.tsv
  python3 two/consensus.py anneal --arm shuf --shuf K --seed S  # -> two/cons/key_shufK_sS.tsv
  python3 two/consensus.py score [--apply]                    # consensus, A_cons, gate -> two/cons/{consensus,signs}.tsv
"""
import argparse, collections, json, os, random, sys, time
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE); ROOT = os.path.dirname(os.path.dirname(T))
sys.path.insert(0, HERE)
import two_instr as ti
OUT = os.path.join(HERE, "cons")
SEEDS = range(1, 11); SHUFS = range(1, 6); NMIN = 6


def anneal(arm, seed, shuf):
    os.chdir(ROOT)
    sys.path.insert(0, os.path.join(ROOT, "tools"))
    import homophonic_anneal as ha, family_run as fr, judge_plaintext as jp
    spec = json.load(open(ti.SPEC))
    model = ha.Model([jp.read_corpus(p) for p in fr.corpus_paths(spec, None)], 3)
    seq = ti.stream(ti.NEW4)
    if arm == "shuf":
        random.Random(shuf).shuffle(seq)
    t0 = time.time()
    sc, key = ha.solve(seq, model, ti.RESTARTS, ti.ITERS, seed, 1.0)[0]
    tag = f"real_s{seed}" if arm == "real" else f"shuf{shuf}_s{seed}"
    with open(os.path.join(OUT, f"key_{tag}.tsv"), "w") as f:
        f.write("sign\tvalue\n" + "".join(f"{s}\t{v}\n" for s, v in sorted(key.items())))
    with open(os.path.join(OUT, "anneal.tsv"), "a") as f:
        f.write("\t".join(map(str, [time.strftime("%Y-%m-%d %H:%M", time.gmtime()), tag, len(seq), len(set(seq)),
                                     f"{sc:.1f}", f"{time.time()-t0:.0f}s"])) + "\n")


def consensus(prefix):
    keys = [ti.read_key(os.path.join(OUT, f"key_{prefix}_s{s}.tsv")) for s in SEEDS]
    out = {}
    for sign in set().union(*keys):
        c = collections.Counter(k[sign] for k in keys if sign in k)
        letter, n = c.most_common(1)[0]
        out[sign] = (letter if n >= NMIN else None, n, letter)
    return out


def a_cons(k1, cons, toks):
    use = [t for t in toks if t not in ti.C_SIGNS and t in k1]
    ok = lambda t: t in cons and cons[t][0] == k1[t]
    types = sorted(set(use))
    return sum(map(ok, use)) / len(use), sum(map(ok, types)) / len(types), len(use), len(types)


def score(apply):
    k1 = ti.read_key(os.path.join(T, "key.tsv")); toks = ti.stream()
    real = consensus("real"); ctl = {k: consensus(f"shuf{k}") for k in SHUFS}
    rows = [["real"] + list(a_cons(k1, real, toks))] + [[f"shuf{k}"] + list(a_cons(k1, ctl[k], toks)) for k in SHUFS]
    cmax = max(r[1] for r in rows[1:]); verdict = "PASS" if rows[0][1] > cmax else "FAIL"
    s1 = ti.read_key(os.path.join(HERE, "key_real_s1.tsv")); s1n = ti.read_key(os.path.join(OUT, "key_real_s1.tsv"))
    with open(os.path.join(OUT, "consensus.tsv"), "w") as f:
        f.write("consensus\tA_cons_token\tA_cons_type\ttokens\ttypes\n")
        f.write("".join("\t".join(f"{x:.4f}" if isinstance(x, float) else str(x) for x in r) + "\n" for r in rows))
        f.write(f"# gate: real {rows[0][1]:.4f} vs shuffled max {cmax:.4f} -> {verdict}; n>={NMIN} of 10 seeds\n")
        f.write(f"# determinism: fresh seed 1 == two/key_real_s1.tsv: {s1 == s1n}\n")
    cnt = collections.Counter(toks)
    lines = open(os.path.join(T, "key.tsv")).read().splitlines(); body = [l.split("\t") for l in lines[1:]]
    sig = [["sign", "tokens", "value", "grade", "real_cons", "real_n", "real_top", "shuf_agree_n6", "decision"]]
    new = [lines[0]]
    for sign, value, g, src in body:
        rc = real.get(sign, (None, 0, "-")); sh = sum(1 for k in SHUFS if ctl[k].get(sign, (None,))[0] == value)
        dec = "-"
        if g == "M":
            if verdict == "PASS" and rc[0] == value and sh <= 1:
                dec = "M->S"
            elif rc[0] == value:
                dec = f"stays M (shuffled controls agree {sh}/5)" if verdict == "PASS" else "stays M (gate FAIL)"
            elif rc[0]:
                dec = f"stays M (consensus reads '{rc[0]}')"
            else:
                dec = "stays M (no consensus)" if sign in real else "stays M (absent from four leaves)"
        elif g == "S":
            dec = "info: consensus agrees" if rc[0] == value else f"info: consensus {rc[0] or 'none'}"
        sig.append([sign, cnt.get(sign, 0), value, g, rc[0] or "-", rc[1], rc[2], sh, dec])
        if apply and g == "M":
            src = src.split(" || RUN3-C1161MS")[0]
            note = (f"real consensus '{rc[0] or '-'}' n={rc[1]}/10 (top '{rc[2]}'), shuffled controls agree {sh}/5, gate {verdict}")
            if dec == "M->S":
                g = "S"; note = "M->S: " + note
            src = f"{src} || RUN3-C1161MS consensus (tx/PREREG_consensus.md): {note}"
        new.append("\t".join([sign, value, g, src]))
    with open(os.path.join(OUT, "signs.tsv"), "w") as f:
        f.write("".join("\t".join(map(str, r)) + "\n" for r in sig))
    print(open(os.path.join(OUT, "consensus.tsv")).read()); print(open(os.path.join(OUT, "signs.tsv")).read())
    if apply:
        open(os.path.join(T, "key.tsv"), "w").write("\n".join(new) + "\n")
        print("key.tsv grades:", collections.Counter(l.split("\t")[2] for l in new[1:]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["anneal", "score"])
    ap.add_argument("--arm", choices=["real", "shuf"], default="real")
    ap.add_argument("--seed", type=int, default=1); ap.add_argument("--shuf", type=int, default=0)
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    if a.mode == "anneal": anneal(a.arm, a.seed, a.shuf)
    else: score(a.apply)


if __name__ == "__main__":
    main()
