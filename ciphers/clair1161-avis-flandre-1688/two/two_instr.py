#!/usr/bin/env python3
"""N4-C1 (4 Oct 2026): two-instrument grading and the fr16142 Noailles shape-key test. Pre-registered in
tx/PREREG_two_instr.md (pushed before any statistic was computed).

  python3 two/two_instr.py anneal --arm real --seed S      # instrument 2: blind anneal on c186L+c187L+c187R+c188L only
  python3 two/two_instr.py anneal --arm shuf --shuf K      # control: same, four-leaf stream order-shuffled (seed 1)
  python3 two/two_instr.py agree                           # statistic A + gate -> two/agree.tsv
  python3 two/two_instr.py grade                           # if PASS: rewrite key.tsv grades/sources per the PREREG
  python3 two/two_instr.py tomokiyo                        # part B -> two/tomokiyo.tsv
Keys go to two/key_<tag>.tsv, anneal rows to two/anneal.tsv.
"""
import argparse, csv, json, os, random, sys, time
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE); ROOT = os.path.dirname(os.path.dirname(T))
sys.path.insert(0, os.path.join(ROOT, "tools"))
SPEC = os.path.join(ROOT, "specs", "clair1161-avis-flandre-1688.json")
NEW4 = ("c186L", "c187L", "c187R", "c188L")
C_SIGNS = {"a", "d", "e", "ee", "p", "sd"}
RESTARTS, ITERS = 32, 40000


def is_cipher(s):
    return s != "/" and not s.startswith("[")


def rows():
    return list(csv.DictReader(open(os.path.join(T, "ciphertext.tsv")), delimiter="\t"))


def stream(leaves=None):
    return [r["sign"] for r in rows() if is_cipher(r["sign"]) and (leaves is None or r["line"][:5] in leaves)]


def read_key(p):
    return {r["sign"]: r["value"] for r in csv.DictReader((l for l in open(p) if not l.startswith("#")), delimiter="\t")
            if r.get("value")}


def anneal(arm, seed, shuf):
    os.chdir(ROOT)
    import homophonic_anneal as ha, family_run as fr, judge_plaintext as jp
    spec = json.load(open(SPEC))
    model = ha.Model([jp.read_corpus(p) for p in fr.corpus_paths(spec, None)], 3)
    seq = stream(NEW4)
    if arm == "shuf":
        random.Random(shuf).shuffle(seq)
    t0 = time.time()
    sc, key = ha.solve(seq, model, RESTARTS, ITERS, seed, 1.0)[0]
    tag = f"real_s{seed}" if arm == "real" else f"shuf{shuf}_s{seed}"
    with open(os.path.join(HERE, f"key_{tag}.tsv"), "w") as f:
        f.write("sign\tvalue\n" + "".join(f"{s}\t{v}\n" for s, v in sorted(key.items())))
    row = [time.strftime("%Y-%m-%d %H:%M", time.gmtime()), tag, len(seq), len(set(seq)), f"{sc:.1f}", f"{time.time()-t0:.0f}s"]
    p = os.path.join(HERE, "anneal.tsv"); new = not os.path.exists(p)
    with open(p, "a") as f:
        if new:
            f.write("utc\ttag\tN\tK\tanneal_score\ttime\n")
        f.write("\t".join(map(str, row)) + "\n")
    print("\t".join(map(str, row)), flush=True)


def agreement(k1, k2, toks):
    use = [t for t in toks if t not in C_SIGNS and t in k1 and t in k2]
    tok = sum(k1[t] == k2[t] for t in use) / max(1, len(use))
    types = sorted(set(use))
    typ = sum(k1[t] == k2[t] for t in types) / max(1, len(types))
    return tok, typ, len(use), len(types)


def agree():
    k1 = read_key(os.path.join(T, "key.tsv"))
    allt = stream(); held = stream(("c185R", "c186R"))
    out = []
    for tag in ["real_s1", "real_s2", "real_s3"] + [f"shuf{k}_s1" for k in range(1, 6)]:
        p = os.path.join(HERE, f"key_{tag}.tsv")
        if not os.path.exists(p):
            continue
        k2 = read_key(p)
        a, ty, n, nt = agreement(k1, k2, allt); h, _, hn, _ = agreement(k1, k2, held)
        out.append([tag, f"{a:.4f}", f"{ty:.4f}", n, nt, f"{h:.4f}", hn])
    shuf = [float(r[1]) for r in out if r[0].startswith("shuf")]
    real = [float(r[1]) for r in out if r[0] == "real_s1"]
    verdict = ("PASS" if real and len(shuf) == 5 and real[0] > max(shuf) else "FAIL") if real and len(shuf) == 5 else "INCOMPLETE"
    with open(os.path.join(HERE, "agree.tsv"), "w") as f:
        f.write("key\tA_token\tA_type\ttokens\ttypes\tA_token_c185R+c186R\ttokens_c185R+c186R\n")
        f.write("".join("\t".join(map(str, r)) + "\n" for r in out))
        f.write(f"# gate: real_s1 {real[0] if real else '-'} vs shuffled max {max(shuf) if shuf else '-'} -> {verdict}\n")
    for r in out:
        print("\t".join(map(str, r)))
    print("gate:", verdict, "real_s1", real, "shuf max", max(shuf) if shuf else None)
    return verdict


def grade_apply(passed):
    k2 = read_key(os.path.join(HERE, "key_real_s1.tsv"))
    p = os.path.join(T, "key.tsv")
    lines = open(p).read().splitlines()
    head, body = lines[0], [l.split("\t") for l in lines[1:]]
    out = [head]; cnt = {}
    for sign, value, g, src in body:
        src = src.split(" || N4-C1")[0]
        if g != "C":
            if passed and k2.get(sign) == value:
                g, note = "S", "instrument 2 (four-leaf blind anneal seed 1) agrees"
            elif sign in k2:
                g, note = "M", f"instrument 2 reads '{k2[sign]}'"
            else:
                g, note = "M", "instrument 2 has no value (sign absent from the four leaves)"
            if not passed:
                g = "M"
            src = f"{src} || N4-C1 two-instrument grade (tx/PREREG_two_instr.md): {note}"
        cnt[g] = cnt.get(g, 0) + 1
        out.append("\t".join([sign, value, g, src]))
    open(p, "w").write("\n".join(out) + "\n")
    print("key.tsv grades:", cnt)


TOMO = [("e", "p"), ("4", "p"), ("7", "f"), ("9", "c"), ("x", "d"), ("iii", "r"), ("ee", "r"), ("f", "y"),
        ("NEW_c188L_2", "a"), ("NEW_c187R_2", "t"), ("tri", "l"), ("z", "n"), ("ls", "e"), ("y", "s"), ("box", "g"),
        ("sqc", "f")]


def tomokiyo():
    k1 = read_key(os.path.join(T, "key.tsv"))
    p2 = os.path.join(HERE, "key_real_s1.tsv"); k2 = read_key(p2) if os.path.exists(p2) else {}
    m1 = sum(k1.get(a) == b for a, b in TOMO); m2 = sum(k2.get(a) == b for a, b in TOMO)
    signs = sorted(k1); vals = [k1[s] for s in signs]; rng = random.Random(1); null = []
    for _ in range(10000):
        v = vals[:]; rng.shuffle(v); kp = dict(zip(signs, v))
        null.append(sum(kp.get(a) == b for a, b in TOMO))
    null.sort(); p99 = null[9899]; pge = sum(x >= m1 for x in null) / len(null)
    with open(os.path.join(HERE, "tomokiyo.tsv"), "w") as f:
        f.write("our_label\ttomokiyo_letter\tkey.tsv\tinstrument2\n")
        f.write("".join(f"{a}\t{b}\t{k1.get(a,'-')}\t{k2.get(a,'-')}\n" for a, b in TOMO))
        f.write(f"# matches key.tsv {m1}/16, instrument2 {m2}/16; permutation null mean {sum(null)/len(null):.2f}, p99 {p99},"
                f" P(null >= {m1}) = {pge:.4f} -> {'FIT' if m1 > p99 else 'NO FIT'}\n")
    print(open(os.path.join(HERE, "tomokiyo.tsv")).read())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mode", choices=["anneal", "agree", "grade", "tomokiyo"])
    ap.add_argument("--arm", choices=["real", "shuf"], default="real")
    ap.add_argument("--seed", type=int, default=1); ap.add_argument("--shuf", type=int, default=0)
    a = ap.parse_args()
    if a.mode == "anneal": anneal(a.arm, a.seed, a.shuf)
    elif a.mode == "agree": agree()
    elif a.mode == "grade": grade_apply(agree() == "PASS")
    else: tomokiyo()


if __name__ == "__main__":
    main()
