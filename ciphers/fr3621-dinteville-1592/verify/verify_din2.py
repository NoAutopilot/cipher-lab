#!/usr/bin/env python3
"""VERIFY-DIN2 (account-3 second-audit verifier, 3 Oct 2026): independent checks on the DIN-PRINT result
(f.128 aligned to the 1882 print, f.130r decoded with f128/print_align/key_print.tsv, no repair).

  python3 ciphers/fr3621-dinteville-1592/verify/verify_din2.py           write verify/result2.json
  python3 ciphers/fr3621-dinteville-1592/verify/verify_din2.py --check   exit 1 if verify/result2.json is stale

Re-uses the solvers' functions unchanged (f128/print_align/align_print.py, f130/score_f130.py). Adds:
 1. f.130 controls at fresh seeds (free and frequency-banded shuffles, seeds 52001-52003, 1000 each);
 2. f.128 alignment shuffle control at a fresh seed (52001, 300 shuffles; the rotation control is deterministic);
 3. WRONG-TEXT control (new; can fail differently from the target because it changes which letter each sign gets):
    the f.128 cipher aligned with the same aligner and settings to 20 passages of real 16th-c. French prose
    (fr16 corpus, lettresindites00marg, consecutive words, each print segment's word count kept), each key applied
    to f.130 and scored with the same statistic. Asks whether *any* French plain text forced through this aligner
    yields a key that reads f.130 as well as the print does. The wrong texts are inside the scoring model's own
    corpus, which favours the control (conservative).
 4. grade recount under four rules on f130/print/tokens.tsv (527 cipher tokens, dots excluded).
"""
import csv, gzip, importlib.util, json, random, re, sys, unicodedata
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
TGT = HERE.parent
ROOT = TGT.parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from judge_plaintext import NgramModel, read_corpus  # noqa: E402


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


S = load("score_f130", TGT / "f130" / "score_f130.py")
A = load("align_print", TGT / "f128" / "print_align" / "align_print.py")
SEEDS = (52001, 52002, 52003)


def pct(xs, q):
    xs = sorted(xs); return xs[int(q * (len(xs) - 1))]


def summ(real, xs):
    return {"real": round(real, 4), "n": len(xs), "mean": round(sum(xs) / len(xs), 4), "p95": round(pct(xs, 0.95), 4),
            "max": round(max(xs), 4), "ge_real": sum(1 for x in xs if x >= real)}


def norm(t):
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = t.replace("j", "i").replace("v", "u").replace("y", "i")
    return re.sub(r"[^a-z]+", " ", t).split()


def key_from_counts(counts, name):
    return {name(v): A.ia.top_of(c)[0] for v, c in counts.items() if name(v) != "?" and A.ia.top_of(c)[0]}


def main():
    model = NgramModel([read_corpus(p) for p in sorted((ROOT / "tools" / "data" / "fr16").glob("*.txt.gz"))])
    ct = S.load_ct()
    kp = {r["sign"]: r for r in csv.DictReader(open(TGT / "f128/print_align/key_print.tsv", encoding="utf-8"), delimiter="\t")}
    val = {s: r["meaning"] for s, r in kp.items()}
    real, nwin = S.stat(model, S.runs(ct, val))
    res = {"real": round(real, 4), "windows": nwin}

    # 1. fresh-seed f.130 controls
    signs = sorted(val); cnt = Counter(r["sign"] for r in ct)
    order = sorted(signs, key=lambda s: -cnt.get(s, 0)); blocks = [order[i:i + 4] for i in range(0, len(order), 4)]
    for sd in SEEDS:
        rnd = random.Random(sd); free = []; band = []
        for _ in range(1000):
            l = [val[s] for s in signs]; rnd.shuffle(l); free.append(S.stat(model, S.runs(ct, dict(zip(signs, l))))[0])
        for _ in range(1000):
            v = {}
            for b in blocks:
                l = [val[s] for s in b]; rnd.shuffle(l); v.update(zip(b, l))
            band.append(S.stat(model, S.runs(ct, v))[0])
        res[f"f130_free_{sd}"] = summ(real, free); res[f"f130_banded_{sd}"] = summ(real, band)

    # 2. f.128 alignment shuffle at a fresh seed
    P = [r["print_norm"] for r in A.PP]
    (prep, results, counts, shown), name = A.run(P, "syl")
    creal, nocc = A.consistency(counts, name)
    words = [t.split() for t in P]; cat = "".join("".join(w) for w in words)

    def resplit(s):
        out, pos = [], 0
        for ws in words:
            o = []
            for w in ws:
                o.append(s[pos:pos + len(w)]); pos += len(w)
            out.append(" ".join(o))
        return out
    rnd = random.Random(52001); sh = []
    for _ in range(300):
        l = list(cat); rnd.shuffle(l); sh.append(A.consistency(A.run(resplit("".join(l)), "syl")[0][2], name)[0])
    res["f128_align_shuffle_52001"] = summ(creal, sh); res["f128_align_shuffle_52001"]["occ"] = nocc

    # 3. wrong-text control
    with gzip.open(ROOT / "tools/data/fr16/lettresindites00marg_djvu.txt.gz", "rt", encoding="utf-8", errors="ignore") as f:
        corpus = norm(f.read())
    nw = [len(t.split()) for t in P]; need = sum(nw)
    rnd = random.Random(52001); wrong = []; wcons = []
    for _ in range(20):
        st = rnd.randrange(len(corpus) // 10, len(corpus) - need - 1)
        seq = corpus[st:st + need]; texts, pos = [], 0
        for k in nw:
            texts.append(" ".join(seq[pos:pos + k])); pos += k
        (_, _, c2, _), nm2 = A.run(texts, "syl")
        wcons.append(A.consistency(c2, nm2)[0])
        wrong.append(S.stat(model, S.runs(ct, key_from_counts(c2, nm2)))[0])
    res["wrong_text_f130"] = summ(real, wrong)
    res["wrong_text_f128_consistency"] = summ(creal, wcons)

    # 4. grade recount
    toks = [r for r in csv.DictReader(open(TGT / "f130/print/tokens.tsv", encoding="utf-8"), delimiter="\t") if r["sign"] != "."]

    def grade(rule):
        g = Counter()
        for r in toks:
            k = kp.get(r["sign"])
            if not k:
                g["U"] += 1; continue
            n, a, oth = int(k["n"]), int(k["agree"]), k["others"].strip()
            ok = {"prereg": a >= 3 and a / n >= 0.5,
                  "polyphones_M": a >= 3 and a / n >= 0.5 and r["sign"] not in ("#", "v"),
                  "ratio75": a >= 3 and a / n >= 0.75,
                  "strict_no_conflict": a >= 2 and not oth}[rule]
            g["C" if ok and r["conf"] == "H" else "M"] += 1
        return {k: g[k] for k in ("C", "M", "U")}
    res["grades"] = {r: grade(r) for r in ("prereg", "polyphones_M", "ratio75", "strict_no_conflict")}
    out = json.dumps(res, indent=1) + "\n"
    p = HERE / "result2.json"
    if "--check" in sys.argv:
        ok = p.exists() and p.read_text(encoding="utf-8") == out
        print(out); print("check: committed outputs match" if ok else "check: STALE result2.json"); sys.exit(0 if ok else 1)
    p.write_text(out, encoding="utf-8"); print(out)


if __name__ == "__main__":
    main()
