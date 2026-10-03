#!/usr/bin/env python3
"""GAPS150 (PREREG-GAPS150.md): apply the pre-registered table-change rule to the blind re-read (reread.tsv), re-score the
176 numbers with the resulting table on de17 (seed 150), and score the leaf's own period gloss text as a calibration.

  python3 score150.py           write score150.json and gloss_text.txt, print results
  python3 score150.py --check   exit 1 if committed gloss_text.txt or revision decision is stale (rule 7)
"""
import csv, json, os, random, sys

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.join(HERE, "..", "residue")
sys.path.insert(0, RES); sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "tools"))
import rule, score  # noqa: E402

NEED = {21: 2, 12: 2, 2: 1, 22: 2}  # strict majority of C probe positions per residue (prereg)


def revision():
    tab = rule.table(); votes = {r: {} for r in NEED}
    for r in csv.DictReader(open(os.path.join(HERE, "reread.tsv")), delimiter="\t"):
        if r["role"] != "probe" or r["conf"] not in ("H", "M"):
            continue
        res = int(r["residue"]); votes[res][r["letter"]] = votes[res].get(r["letter"], 0) + 1
    decoys = [r for r in csv.DictReader(open(os.path.join(HERE, "reread.tsv")), delimiter="\t") if r["role"] == "decoy"]
    dec_ok = sum(r["letter"] == r["pairs_gloss"] for r in decoys)
    changes = {}
    if dec_ok >= 5:
        for res, v in votes.items():
            for x, c in v.items():
                if c >= NEED[res] and x != tab[res][0]:
                    changes[res] = x
    return dec_ok, len(decoys), changes


def gloss_text():
    rows = csv.DictReader(open(os.path.join(HERE, "..", "gloss", "pairs.tsv")), delimiter="\t")
    return "".join(r["gloss"].replace("ů", "u") for r in rows if r["gloss"].strip())


def main():
    dec_ok, nd, changes = revision(); gt = gloss_text()
    path = os.path.join(HERE, "gloss_text.txt")
    if "--check" in sys.argv:
        ok = os.path.exists(path) and open(path).read() == gt + "\n" and changes == {}
        print("gaps150", "current" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(path, "w").write(gt + "\n")
    import judge_plaintext as J
    model = J.NgramModel([J.read_corpus(p) for p in J.LANG_CORPORA["de17"]])
    tab = rule.table()
    for r, x in changes.items():
        tab[r] = (x,) + tab[r][1:]
    nums = [n for _, n, _ in score.numbers()]
    dec = rule.decode(nums, tab=tab)
    real, null, _ = model.controls(len(dec), samples=200)
    sc = model.score(dec)
    rnd = random.Random(150); shuf = []
    for _ in range(200):
        s = nums[:]; rnd.shuffle(s); shuf.append(model.score(rule.decode(s, tab=tab)))
    shuf.sort()
    shifted = [model.score(rule.decode(nums, shift=k, tab=tab)) for k in range(1, 24)]
    g_real, g_null, _ = model.controls(len(gt), samples=200)
    g_sc = model.score(gt)
    rnd = random.Random(1500); g_shuf = []
    for _ in range(200):
        s = list(gt); rnd.shuffle(s); g_shuf.append(model.score("".join(s)))
    g_shuf.sort()
    p = lambda a, q: round(J.pct(sorted(a), q), 4)
    res = {"decoys_agree": f"{dec_ok}/{nd}", "table_changes": {str(k): v for k, v in changes.items()},
           "decode": {"N": len(dec), "score": round(sc, 4), "real_p05": p(real, .05), "real_p01": p(real, .01),
                      "null_p99": p(null, .99), "shuffled_target_p99": p(shuf, .99),
                      "shuffled_target_mean": round(sum(shuf) / len(shuf), 4),
                      "shuffled_ge_real": sum(x >= sc for x in shuf), "shifted_max": round(max(shifted), 4),
                      "shifted_ge_real": sum(x >= sc for x in shifted)},
           "gloss_calibration": {"N": len(gt), "score": round(g_sc, 4), "real_p05": p(g_real, .05),
                                 "real_p01": p(g_real, .01), "real_median": p(g_real, .5), "null_p99": p(g_null, .99),
                                 "letter_shuffled_mean": round(sum(g_shuf) / len(g_shuf), 4),
                                 "letter_shuffled_p99": p(g_shuf, .99)}}
    d = res["decode"]
    res["decode"]["PASS"] = bool(sc > d["null_p99"] and sc > d["real_p05"] and sc > d["shuffled_target_p99"]
                                 and sc > d["shifted_max"])
    json.dump(res, open(os.path.join(HERE, "score150.json"), "w"), indent=1)
    print(json.dumps(res, indent=1)); print("gloss text:", gt)


if __name__ == "__main__":
    main()
