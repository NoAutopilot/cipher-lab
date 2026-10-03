#!/usr/bin/env python3
"""GAPS157 (PREREG-GAPS157.md): score the leaf's gloss text, the frozen-table decode of the 176 numbers, 200 shuffled-
target decodes and the 23 shifted-rule decodes, raw (judge fold only) and under one spelling normalisation applied
identically to the corpus, under de1600 and de17; apply the registered verdict.

  python3 score157.py           write score157.json, print results
  python3 score157.py --check   exit 1 if score157.json is stale (rule 7)
"""
import json, os, random, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "..", "residue")
sys.path.insert(0, RES); sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "tools"))
import rule, score  # noqa: E402
import judge_plaintext as J  # noqa: E402


def norm(s):
    s = J.fold(s).translate(str.maketrans("vjy", "uii"))
    return re.sub(r"(.)\1+", r"\1", s)


def run(lang, normed):
    f = norm if normed else J.fold
    model = J.NgramModel([f(J.read_corpus(p)) for p in J.LANG_CORPORA[lang]])
    p = lambda a, q: round(J.pct(sorted(a), q), 4)
    gt = f(open(os.path.join(HERE, "..", "gaps150", "gloss_text.txt")).read())
    g_real, g_null, _ = model.controls(len(gt), samples=200)
    rnd = random.Random(1570); g_shuf = []
    for _ in range(200):
        s = list(gt); rnd.shuffle(s); g_shuf.append(model.score("".join(s)))
    gsc = model.score(gt)
    nums = [n for _, n, _ in score.numbers()]
    dec = f(rule.decode(nums))
    real, null, _ = model.controls(len(dec), samples=200)
    sc = model.score(dec)
    rnd = random.Random(157); shuf = []
    for _ in range(200):
        s = nums[:]; rnd.shuffle(s); shuf.append(model.score(f(rule.decode(s))))
    shifted = [model.score(f(rule.decode(nums, shift=k))) for k in range(1, 24)]
    g = {"N": len(gt), "score": round(gsc, 4), "real_p05": p(g_real, .05), "real_p01": p(g_real, .01),
         "real_median": p(g_real, .5), "null_p99": p(g_null, .99), "real_le_gloss": sum(x <= gsc for x in g_real),
         "letter_shuffled_mean": round(sum(g_shuf) / 200, 4), "letter_shuffled_p99": p(g_shuf, .99)}
    d = {"N": len(dec), "score": round(sc, 4), "real_p05": p(real, .05), "null_p99": p(null, .99),
         "real_le_decode": sum(x <= sc for x in real),
         "shuffled_target_mean": round(sum(shuf) / 200, 4), "shuffled_target_p99": p(shuf, .99),
         "shuffled_ge_decode": sum(x >= sc for x in shuf), "shifted_max": round(max(shifted), 4),
         "shifted_ge_decode": sum(x >= sc for x in shifted)}
    g["clears_p05"] = gsc > g["real_p05"]
    d["passes_A"] = bool(sc > d["real_p05"] and sc > d["null_p99"] and sc > d["shuffled_target_p99"]
                         and sc > d["shifted_max"])
    return {"gloss": g, "decode": d}


def compute():
    out = {f"{lang}_{'norm' if n else 'raw'}": run(lang, n) for lang in ("de1600", "de17") for n in (False, True)}
    prim, sec = out["de1600_norm"], out["de17_norm"]
    if prim["gloss"]["clears_p05"] and prim["decode"]["passes_A"]:
        v = "A: reading ready" + ("" if sec["gloss"]["clears_p05"] and sec["decode"]["passes_A"] else " (de17 disagrees)")
    elif prim["gloss"]["clears_p05"]:
        v = "B: calibrated judge FAILs the frozen-table decode"
    else:
        v = "C: judge cannot recognise this leaf's text even normalised"
    out["verdict"] = v
    return out


def main():
    path = os.path.join(HERE, "score157.json")
    res = compute(); txt = json.dumps(res, indent=1) + "\n"
    if "--check" in sys.argv:
        ok = os.path.exists(path) and open(path).read() == txt
        print("gaps157", "current" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(path, "w").write(txt); print(txt)


if __name__ == "__main__":
    main()
