#!/usr/bin/env python3
"""DEF1-1411 gate (PREREG-DEF1-1411.md): decode def1411/numbers.tsv (unused p.2 numerals) with the frozen tables T and T21r,
run the ARM-C1 judge-void check on a shuffled copy first, then score each table on de1600 against the shuffled-target
(200 draws, seed 1411) and shifted-rule controls and the leaf's own gloss calibration; residue-21 letter test (24 letters).

  python3 score1411.py           write decode_T.txt, decode_T21r.txt, score1411.json; print the verdict
  python3 score1411.py --check   exit 1 if committed decodes or score1411.json are stale (rule 7)
"""
import csv, json, os, random, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..", "..")
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(ROOT, "tools"))
import tables  # noqa: E402
import judge_plaintext as J  # noqa: E402

ALPHA = "abcdefghiklmnopqrstuwxyz"
SEED = 1411


def numbers():
    rows = []
    for r in csv.DictReader(open(os.path.join(HERE, "numbers.tsv")), delimiter="\t"):
        t = r["token"].rstrip("?")
        if t.isdigit() and "intext" not in r.get("note", ""):
            rows.append((r["line"], int(t), r["grade"]))
    return rows


def dec(nums, tab, shift=0):
    return "".join(tab[(n + shift) % 24][0] for n in nums)


def decode_text(rows, tab):
    out, cur, line = [], [], None
    for ln, n, g in rows:
        if ln != line and cur:
            out.append(f"{line}\t{''.join(cur)}"); cur = []
        line = ln; c = tab[n % 24][0]; cur.append(c.upper() if g == "M" else c)
    if cur:
        out.append(f"{line}\t{''.join(cur)}")
    return "\n".join(out) + "\n"


def main():
    rows = numbers(); nums = [n for _, n, _ in rows]; T = tables.tables()
    texts = {k: decode_text(rows, t) for k, t in T.items()}
    if "--check" in sys.argv:
        ok = all(os.path.exists(os.path.join(HERE, f"decode_{k}.txt")) and
                 open(os.path.join(HERE, f"decode_{k}.txt")).read() == v for k, v in texts.items())
        print("def1411", "current" if ok else "STALE"); sys.exit(0 if ok else 1)
    for k, v in texts.items():
        open(os.path.join(HERE, f"decode_{k}.txt"), "w").write(v)
    N = len(nums)
    res = {"N": N, "n_M": sum(g == "M" for *_, g in rows), "residue21_count": sum(n % 24 == 21 for n in nums)}
    if N < 60:
        res["verdict"] = "NON-TEST (N < 60)"; json.dump(res, open(os.path.join(HERE, "score1411.json"), "w"), indent=1)
        print(json.dumps(res, indent=1)); return
    model = J.NgramModel([J.read_corpus(p) for p in J.LANG_CORPORA["de1600"]])
    real, null, _ = model.controls(N, samples=200)
    p = lambda a, q: round(J.pct(sorted(a), q), 4)
    real_p05, null_p99 = p(real, .05), p(null, .99)
    # step 0 (ARM-C1): one shuffled copy, decoded with each table, through the judge
    s = nums[:]; random.Random(SEED).shuffle(s); void = {}
    for k, t in T.items():
        sd = dec(s, t); open(os.path.join(HERE, f"shuffled_decode_{k}.txt"), "w").write(sd + "\n")
        sc = model.score(sd); void[k] = {"score": round(sc, 4), "judge_pass": bool(sc > real_p05 and sc > null_p99)}
    res["step0_shuffled_copy"] = void
    judge_void = any(v["judge_pass"] for v in void.values())
    res["judge_void"] = judge_void
    gloss = open(os.path.join(HERE, "..", "gaps150", "gloss_text.txt")).read().strip()
    g_sc = round(model.score(gloss), 4)
    res["gloss_calibration"] = {"N": len(J.fold(gloss)), "score": g_sc}
    res["judge"] = {"real_p05": real_p05, "real_p01": p(real, .01), "real_median": p(real, .5), "null_p99": null_p99}
    for k, t in T.items():
        d = dec(nums, t); sc = model.score(d)
        rnd = random.Random(SEED); shuf = []
        for _ in range(200):
            x = nums[:]; rnd.shuffle(x); shuf.append(model.score(dec(x, t)))
        shifted = [model.score(dec(nums, t, k_)) for k_ in range(1, 24)]
        r = {"score": round(sc, 4), "shuffled_target_p99": p(shuf, .99), "shuffled_target_mean": round(sum(shuf) / 200, 4),
             "shuffled_ge_real": sum(x >= sc for x in shuf), "shifted_max": round(max(shifted), 4),
             "shifted_ge_real": sum(x >= sc for x in shifted), "minus_gloss": round(sc - g_sc, 4)}
        r["beats_controls"] = bool(sc > r["shuffled_target_p99"] and sc > r["shifted_max"])
        r["PASS"] = bool(r["beats_controls"] and sc >= g_sc and not judge_void)
        res[k] = r
    # residue-21 letter test
    base = T["T"]; sc21 = {}
    for L in ALPHA:
        t = dict(base); t[21] = (L,) + base[21][1:]; sc21[L] = round(model.score(dec(nums, t)), 4)
    order = sorted(sc21, key=lambda L: -sc21[L])
    res["residue21_test"] = {"rank_r": order.index("r") + 1, "rank_z": order.index("z") + 1, "top5": order[:5],
                             "scores": sc21}
    enough = res["residue21_count"] >= 5
    res["residue21_test"]["verdict"] = ("r favoured" if enough and order[0] == "r" else
                                        "z favoured" if enough and order[0] == "z" else "residue 21 undecided")
    json.dump(res, open(os.path.join(HERE, "score1411.json"), "w"), indent=1)
    print(json.dumps({k: v for k, v in res.items() if k != "residue21_test"}, indent=1))
    print("residue21:", {k: v for k, v in res["residue21_test"].items() if k != "scores"})


if __name__ == "__main__":
    main()
