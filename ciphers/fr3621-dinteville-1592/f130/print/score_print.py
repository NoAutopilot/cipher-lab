#!/usr/bin/env python3
"""DIN-PRINT (3 Oct 2026): f.130r decoded with the key aligned to the 1882 print of f.128 (f128/print_align/key_print.tsv),
no hill-climb repair. Pre-registered in f128/print_align/PREREG.md section 4.

    python3 ciphers/fr3621-dinteville-1592/f130/print/score_print.py [--check]

Statistic, runs and model exactly as f130/score_f130.py (imported unchanged). Controls: 1000 free shuffles of the letter
values among keyed signs (seed 20261003) and 1000 frequency-banded shuffles (blocks of 4 signs adjacent in f.130 frequency
rank, seed 31001, VERIFY-DIN's design). Grades: C if the key_print row has agree >= 3 and agree/n >= 0.5 and the f.130 sign
conf is H; M if keyed otherwise; U if unkeyed. Writes result.json, control.tsv, tokens.tsv, reading.txt and the
decode_key.py inputs key_dk.tsv (decode.json job 3). --check exits 1 if any committed output is stale (rule 7).
"""
import csv, importlib.util, json, random, sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
TGT = HERE.parents[1]
ROOT = TGT.parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from judge_plaintext import NgramModel, read_corpus  # noqa: E402

spec = importlib.util.spec_from_file_location("score_f130", TGT / "f130" / "score_f130.py")
S = importlib.util.module_from_spec(spec); spec.loader.exec_module(S)
KEY = TGT / "f128" / "print_align" / "key_print.tsv"


def pct(xs, q):
    xs = sorted(xs); return xs[int(q * (len(xs) - 1))]


def summ(real, xs):
    return {"real": round(real, 4), "mean": round(sum(xs) / len(xs), 4), "p95": round(pct(xs, 0.95), 4),
            "max": round(max(xs), 4), "ge_real": sum(1 for x in xs if x >= real), "n": len(xs)}


def build():
    rows = list(csv.DictReader(open(KEY, encoding="utf-8"), delimiter="\t"))
    key = {r["sign"]: (r["meaning"], int(r["agree"]) >= 3 and int(r["agree"]) / int(r["n"]) >= 0.5, r) for r in rows}
    ct = S.load_ct()
    model = NgramModel([read_corpus(p) for p in sorted((ROOT / "tools" / "data" / "fr16").glob("*.txt.gz"))])
    val = {s: v[0] for s, v in key.items()}
    real, nwin = S.stat(model, S.runs(ct, val))
    signs = sorted(val)
    rnd = random.Random(20261003); free = []
    for _ in range(1000):
        l = [val[s] for s in signs]; rnd.shuffle(l); free.append(S.stat(model, S.runs(ct, dict(zip(signs, l))))[0])
    cnt = Counter(r["sign"] for r in ct)
    order = sorted(signs, key=lambda s: -cnt.get(s, 0))
    blocks = [order[i:i + 4] for i in range(0, len(order), 4)]
    rnd = random.Random(31001); band = []
    for _ in range(1000):
        v = {}
        for b in blocks:
            l = [val[s] for s in b]; rnd.shuffle(l); v.update(zip(b, l))
        band.append(S.stat(model, S.runs(ct, v))[0])
    res = {"stat": "fr16 4-gram mean log10 P/letter inside keyed runs (score_f130.py)", "key": "f128/print_align/key_print.tsv",
           "windows": nwin, "free_shuffle": summ(real, free), "banded_shuffle": summ(real, band)}
    res["gate_pass"] = real > res["free_shuffle"]["p95"] and real > res["banded_shuffle"]["p95"]
    tok = ["line\tpos\tsign\tconf\tvalue\tgrade"]; g = Counter(); lines = {}; per_sign = Counter()
    for r in ct:
        s = r["sign"]
        if s.startswith("CLEAR:"):
            lines.setdefault(r["line"], []).append("[" + s[6:] + "]"); continue
        if s in key:
            v, ok, _ = key[s]; gr = "C" if ok and r["conf"] == "H" else "M"
        else:
            v, gr = "?", "U"
        g[gr] += 1; per_sign[(s, gr)] += 1
        tok.append(f"{r['line']}\t{r['pos']}\t{s}\t{r['conf']}\t{v}\t{gr}")
        lines.setdefault(r["line"], []).append(v if gr == "C" else (v.upper() if gr == "M" else "?"))
    res["grades"] = {k: g[k] for k in ("C", "M", "U")}
    reading = ["# f.130r decoded with f128/print_align/key_print.tsv (DIN-PRINT). lower = C, UPPER = M, ? = unkeyed (U), [..] = clear.",
               f"# grades: C {g['C']} M {g['M']} U {g['U']}"]
    reading += [f"{ln}\t{' '.join(v)}" for ln, v in lines.items()]
    kr = ["sign\tvalue\tgrade\tsource"]
    for s, (v, ok, r) in sorted(key.items()):
        kr.append(f"{'hash' if s == '#' else s}\t{v}\t{'C' if ok else 'M'}\tf128/print_align/key_print.tsv {r['agree']}/{r['n']}")
    ctl = ["i\tfree\tbanded"] + [f"{i}\t{a:.4f}\t{b:.4f}" for i, (a, b) in enumerate(zip(free, band))]
    return {"result.json": json.dumps(res, indent=1) + "\n", "control.tsv": "\n".join(ctl) + "\n",
            "tokens.tsv": "\n".join(tok) + "\n", "reading.txt": "\n".join(reading) + "\n", "key_dk.tsv": "\n".join(kr) + "\n"}


def main():
    out = build()
    if "--check" in sys.argv:
        bad = [f for f, t in out.items() if not (HERE / f).exists() or (HERE / f).read_text(encoding="utf-8") != t]
        print(out["result.json"]); print("check: committed outputs match" if not bad else f"check: STALE {bad}")
        sys.exit(1 if bad else 0)
    for f, t in out.items():
        (HERE / f).write_text(t, encoding="utf-8")
    print(out["result.json"])


if __name__ == "__main__":
    main()
