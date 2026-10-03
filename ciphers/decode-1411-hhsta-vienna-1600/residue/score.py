#!/usr/bin/env python3
"""GAPS146 gate (PREREG-GAPS146.md): decode residue/numbers.tsv with the frozen rule, write decode.txt, and score it on
de17 against real_p05/p01, null_p99, a shuffled-target decode (200 draws, seed 146) and the 23 shifted rules.

  python3 score.py            write decode.txt and score.json, print the verdict
  python3 score.py --check    exit 1 if the committed decode.txt is stale (rule 7)
"""
import csv, json, os, random, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "..", "tools"))
import rule  # noqa: E402


def numbers():
    rows = []
    with open(os.path.join(HERE, "numbers.tsv")) as f:
        for r in csv.DictReader(f, delimiter="\t"):
            t = r["token"].rstrip("?")
            if t.isdigit() and "intext" not in r.get("note", ""):
                rows.append((r["line"], int(t), r["grade"]))
    return rows


def decode_text():
    rows, tab = numbers(), rule.table()
    out, cur, line = [], [], None
    for ln, n, g in rows:
        if ln != line and cur:
            out.append(f"{line}\t{''.join(cur)}"); cur = []
        line = ln; cur.append(tab[n % 24][0] if g != "M" else tab[n % 24][0].upper())
    if cur:
        out.append(f"{line}\t{''.join(cur)}")
    return "\n".join(out) + "\n"


def main():
    text = decode_text()
    path = os.path.join(HERE, "decode.txt")
    if "--check" in sys.argv:
        ok = os.path.exists(path) and open(path).read() == text
        print("decode.txt", "current" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(path, "w").write(text)
    import judge_plaintext as J
    nums = [n for _, n, _ in numbers()]
    model = J.NgramModel([J.read_corpus(p) for p in J.LANG_CORPORA["de17"]])
    dec = rule.decode(nums)
    N = max(len(dec), 20)
    real, null, _ = model.controls(N, samples=200)
    sc = model.score(dec)
    rnd = random.Random(146); shuf = []
    for _ in range(200):
        s = nums[:]; rnd.shuffle(s); shuf.append(model.score(rule.decode(s)))
    shuf.sort()
    shifted = {k: model.score(rule.decode(nums, shift=k)) for k in range(1, 24)}
    res = {"N_numbers": len(nums), "N_letters": len(dec), "score": round(sc, 4),
           "real_p05": round(J.pct(real, .05), 4), "real_p01": round(J.pct(real, .01), 4),
           "real_median": round(J.pct(real, .5), 4), "null_p99": round(J.pct(null, .99), 4),
           "shuffled_target_mean": round(sum(shuf) / len(shuf), 4), "shuffled_target_p99": round(J.pct(shuf, .99), 4),
           "shuffled_target_ge_real": sum(x >= sc for x in shuf),
           "shifted_max": round(max(shifted.values()), 4), "shifted_max_k": max(shifted, key=shifted.get),
           "shifted_ge_real": sum(v >= sc for v in shifted.values()),
           "shifted": {k: round(v, 4) for k, v in shifted.items()}}
    c1 = sc > res["null_p99"] and sc > res["real_p05"]
    c23 = sc > res["shuffled_target_p99"] and sc > res["shifted_max"]
    res["verdict"] = "PASS" if c1 and c23 else ("CONTROLS BEATEN, JUDGE CANNOT DECIDE" if c23 else "FAIL (rule not favoured over its controls)")
    json.dump(res, open(os.path.join(HERE, "score.json"), "w"), indent=1)
    print(json.dumps({k: v for k, v in res.items() if k != "shifted"}, indent=1))


if __name__ == "__main__":
    main()
